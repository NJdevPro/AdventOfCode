import itertools as it
import re
import timing
import copy

lines =  open("puzzle20.txt","r").readlines()

print('----------- Part 1 -----------')

tiles, transform = {}, {}

def read_tiles():
    raster = []
    for line in lines:
        m = re.match("Tile (\d+):", line)
        if m:
            tile_num = m.groups(0)[0]
            raster = []
        elif line in ['\n', '\r\n']:
            tile = (tile_num, 'N', '')
            tiles[tile] = raster
        else:
            raster.append(list(line.strip()))
    tile = (tile_num, 'N', '')
    tiles[tile] = raster
    return tiles

def flip(tile, axis):
    new_raster = copy.deepcopy(transform[tile])
    if axis == 'h':
        new_raster.reverse()
    elif axis == 'v':
        for row in new_raster:
            row.reverse()
    new_tile = (tile[0], tile[1], axis)
    transform[new_tile] = new_raster
    return new_tile, new_raster

def rotate(tile, raster, orient:str):
    new_raster = copy.deepcopy(raster)
    side = len(new_raster)
    for row in range(side):
        for col in range(side):
            new_raster[col][side-row-1] = raster[row][col]
    new_tile = (tile[0], orient, '')
    transform[new_tile] = new_raster
    return new_tile, new_raster

def rotations(tile_N):
    tile_E, raster = rotate(tile_N, tiles[tile_N], 'E')
    transform[tile_E] = raster
    tile_S, raster = rotate(tile_E, raster, 'S')
    transform[tile_S] = raster
    tile_W, raster = rotate(tile_S, raster, 'W')
    transform[tile_W] = raster
    return tile_N, tile_E, tile_S, tile_W

def generate_transforms(tiles):
    for tile in tiles.keys():
        for r in rotations(tile):
            flip(r, 'v')
            flip(r, 'h')
    # these transforms are congruent to other ones
    transform.pop((tile[0], 'S', 'h'))
    transform.pop((tile[0], 'S', 'v'))
    transform.pop((tile[0], 'W', 'h'))
    transform.pop((tile[0], 'W', 'v'))
    print(len(transform))

match_left = lambda l, r: l[:][-1] == r[:][0]
match_right = lambda l, r: l[:][0] == r[:][-1]
match_bottom = lambda b, t: t[0] == b[0-1]
match_top = lambda b, t: t[-1] == b[0]

def border_tiles(match_borders): # upper left corner
    border = set()
    matches = 0
    for this_tile in transform:
        #print("This tile: ", this_tile)
        is_border = True
        for tile in transform:
            raster1 = transform[this_tile]
            raster2 = transform[tile]
            if tile[0] != this_tile[0] and match_borders(raster1, raster2):
                matches += 1
                print(matches, this_tile, tile)
                is_border = False
                break
        if is_border:
            border.add(this_tile[0])
    return border

def print_tile(tile):
    print(tile)
    raster = transform[tile]
    for row in raster:
        print(row)

tiles = read_tiles()
transform = tiles.copy()
generate_transforms(tiles)
# for tile in transform:
#     print_tile(tile)

top_border = border_tiles(match_top)
bottom_border = border_tiles(match_bottom)
left_border = border_tiles(match_left)
right_border = border_tiles(match_right)
print("Border lengths: ",  len(top_border), len(bottom_border), len(left_border), len(right_border))

top_left_corner = top_border.intersection(left_border)
top_right_corner = top_border.intersection(right_border)
bottom_left_corner = bottom_border.intersection(left_border)
bottm_right_corner = bottom_border.intersection(right_border)
print("corners: ", top_left_corner, top_right_corner, bottom_left_corner, bottm_right_corner)

print(int(top_left_corner[0]) * int(top_right_corner[0]) * int(bottom_left_corner[0]) * int(bottm_right_corner[0]))
