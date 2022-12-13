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
    fun bfs(m : grid, start : Tile, end: Tile) : Tile {
        var queue : ArrayDeque<Tile> = ArrayDeque()
        var visited: Array<Array<Boolean>> = Array(m.size) { Array(m[0].size) { false } }
        visited[start.i][start.j] = true
        queue.addFirst(start)
        while(queue.isNotEmpty()) {
            val v = queue.removeLast()
            if (v.equals(end)) { return v }
            edges.forEach {
                val i = v.i + it.i
                val j = v.j + it.j
                var c = Tile(i, j)
                if( c within m && !visited[i][j]
                    && ( m[i][j] - m[v.i][v.j] <= 1) ){
                        visited[i][j] = true
                        c.prev = v
                        queue.addFirst(c)
                }
            }
        }
        println("No path found from $start to $end !")
        return start
    }

    fun solve(m: grid, S: Char, E: Char) : Int {
        var start: Tile = Tile(0, 0)
        var end: Tile = Tile(0, 0)

        for (i in m.indices) {
            for (j in m[0].indices) {
                if (m[i][j] == S - 'a') {
                    start = Tile(i, j)
                    m[i][j] = 0
                }
                else if (m[i][j] == E - 'a') {
                    end = Tile(i, j)
                    m[i][j] = 'z' - 'a'
                }
            }
        }
        //printMap(m)
        return backtrack(bfs(m, start, end)).size
    }

    fun solve2(m: grid, S: Char, E: Char) : List<Int> {
        var starts: MutableList<Tile> = mutableListOf()
        var end: Tile = Tile(0, 0)

        for (i in m.indices) {
            for (j in m[0].indices) {
                if (m[i][j] == S - 'a') {
                    starts.add(Tile(i, j))
                    m[i][j] = 0
                }
                else if (m[i][j] == E - 'a') {
                    end = Tile(i, j)
                    m[i][j] = 'z' - 'a'
                }
            }
        }
        return starts.map{ backtrack(bfs(m, it, end)).size }
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

    fun part1(lines: List<String> ): Int {
        val map = readMap(lines)
        //printMap(map)
        return solve(map, 'S', 'E')
    }

    fun part2(lines: List<String>  ): Int {
        val map = readMap(lines)
        //printMap(map)
        return solve2(map, 'a', 'E').min()

    }
}

fun main() {
    val lines = File("src/main/kotlin/AOC2022/input12.txt").readLines()
    val day12 = Day12()
    println(day12.part1(lines))
    println(day12.part2(lines))
}
