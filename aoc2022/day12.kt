package AOC2022

import java.io.File
import kotlin.collections.ArrayDeque


typealias grid = Array<Array<Int>>

data class Tile(val i:Int, val j:Int){
    var prev: Tile? = null // previous coordinate

    operator fun plus(other: Tile) = Tile(i+other.i, j+other.j)
    infix fun within(m :grid) = 0 <= i && i < m.size && 0 <= j && j < m[0].size
}

class Day12 {

    fun readMap(lines: List<String>) : grid {
        val map = Array(lines.size) { Array(lines[0].length) { 0 } }
        for (i in lines.indices) {
            for (j in lines[0].indices) {
                map[i][j] = lines[i][j] - 'a'
            }
        }
        return map
    }

    fun printMap(map: grid) {
        for (i in map.indices) {
            for (j in map[0].indices) {
                print("\t${map[i][j]}")
            }
            println()
        }
    }

    val edges : Array<Tile> = arrayOf( Tile(1, 0), Tile(0, -1), Tile(-1, 0), Tile(0,1) )

    // https://en.m.wikipedia.org/wiki/Breadth-first_search
    fun bfs(m : grid, start : Tile, destination : (Tile) -> Boolean,
            constraint : (a: Int, b: Int) -> Boolean) : Tile {
        var queue : ArrayDeque<Tile> = ArrayDeque()
        var visited: Array<Array<Boolean>> = Array(m.size) { Array(m[0].size) { false } }
        visited[start.i][start.j] = true
        queue.addFirst(start)
        while(queue.isNotEmpty()) {
            val v = queue.removeLast()
            if (destination(v)) { return v }
            edges.forEach {
                val i = v.i + it.i
                val j = v.j + it.j
                var c = Tile(i, j)
                if( c within m && !visited[i][j]
                    && constraint( m[i][j], m[v.i][v.j]) ){
                    visited[i][j] = true
                    c.prev = v
                    queue.addFirst(c)
                }
            }
        }
        println("No path found from $start to destination !")
        return start
    }

    fun backtrack(t: Tile) : List<Tile> {
        var path : MutableList<Tile> = mutableListOf()
        var c = t
        while(c.prev != null) {
            path.add(c)
            c = c.prev!!
        }
        return path.reversed()
    }

    fun find( searched: Int, map: grid) : Tile {
        map.mapIndexed { row, chars -> chars.mapIndexed {col, char -> if (char == searched) return Tile(row, col) } }
        throw IllegalArgumentException("There is no such hill int he map")
    }

    fun part1(lines: List<String> ): Int {
        val map = readMap(lines)
        //printMap(map)
        val start = find('S' - 'a', map)
        map[start.i][start.j] = 0
        val end = find('E' - 'a', map)
        map[end.i][end.j] = 'z' - 'a'
        return backtrack( bfs(map, start, { t : Tile -> t == end}) {a: Int, b : Int -> a - b <= 1 } ).size
    }

    fun part2(lines: List<String>  ): Int {
        val map = readMap(lines)
        val start = find('E' - 'a', map)
        map[start.i][start.j] = 'z' - 'a'
        return backtrack( bfs(map, start, { t : Tile -> map[t.i][t.j] == 0}) {a: Int, b : Int -> b - a <= 1 } ).size
    }
}

fun main() {
    val lines = File("src/main/kotlin/AOC2022/input12.txt").readLines()
    val day12 = Day12()
    println(day12.part1(lines))
    println(day12.part2(lines))
}
