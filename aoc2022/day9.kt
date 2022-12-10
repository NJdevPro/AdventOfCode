package AOC2022

import java.io.File
import java.lang.Integer.max
import kotlin.math.min

typealias Pos = Day9.Knot

class Day9 {

    data class Knot (var x: Int, var y: Int) {
        operator fun plus(pos: Pos?) : Pos = Pos(this.x + pos!!.x, this.y + pos.y)
        operator fun minus(pos : Pos) : Pos = Pos(this.x - pos.x, this.y - pos.y)
        companion object {
            val move = mapOf( "U" to Pos(0,-1), "D" to Pos(0,1), "L" to Pos(-1, 0), "R" to Pos(1,0))
        }
    }

    var H = Knot(0,0)
    var T = Knot(0, 0)

    fun draw() {
        val xmin = node.map{it.x}.min() - 4
        val xmax = node.map{it.x}.max() + 4
        val ymin = node.map{it.y}.min() - 4
        val ymax = node.map{it.y}.max() + 4
            for (y in ymin..ymax) {
                for (x in xmin..xmax) {
                    for (i in 0..8) {
                        H = node[i]
                        T = node[i + 1]
                        if (Pos(x, y) == H) print(i)
                        else if (Pos(x, y) == T) print(i + 1)
                        if (Pos(x, y) == Pos(0, 0)) print("s")
                        else print(".")
                    }
                }
                println()
            }
            println()

    }

    fun moveString(move: String) : Set<Pos> {
        var visited : MutableSet<Pos> = mutableSetOf()
        move.split(' ').let { (dir, steps) ->
            for(step in 1..steps.toInt()) {
                H += Knot.move[dir]    // move head
                val dist = H - T
                if (H.x != T.x && H.y != T.y){
                    when (dist){
                        Pos(2,1), Pos(1,2) -> {T += Pos(1,1)}
                        Pos(2,-1), Pos(1, -2) -> {T += Pos(1,-1)}
                        Pos(-2,1), Pos(-1, 2) -> {T += Pos(-1,1)}
                        Pos(-2,-1), Pos(-1, -2) ->{T += Pos(-1,-1)}
                    }
                } else {
                    if (dist.x > 1) T.x++ else if (dist.x < -1) T.x--
                    if (dist.y > 1) T.y++ else if (dist.y < -1) T.y--
                }
                visited.add(T.copy())
                println("move  ${step}, ${dir}, H=${H}, T=${T}")
                draw()
            }
        }
        return visited
    }

    var node: Array<Knot> = Array(size=10, init = { Knot(0,0)})

    fun moveRope(move: String, n:Int) : Set<Pos> {
        var visited : MutableSet<Pos> = mutableSetOf()
        move.split(' ').let { (dir, steps) ->
            for(step in 1..steps.toInt()) {
                node[0] = node[0] + Knot.move[dir]    // move head
                for (i in 1..n-2) {
                    H = node[i]
                    T = node[i+1]
                    val dist = H - T
                    if (H.x != T.x && H.y != T.y) {
                        when (dist) {
                            Pos(2, 1), Pos(1, 2) -> T += Pos(1, 1)
                            Pos(2, -1), Pos(1, -2) -> T += Pos(1, -1)
                            Pos(-2, 1), Pos(-1, 2) -> T += Pos(-1, 1)
                            Pos(-2, -1), Pos(-1, -2) -> T += Pos(-1, -1)
                        }
                    } else {
                        if (dist.x > 1) T.x++ else if (dist.x < -1) T.x--
                        if (dist.y > 1) T.y++ else if (dist.y < -1) T.y--
                    }
                }
                visited.add(T.copy())
                println("move  ${step}, ${dir}, H=${H}, T=${T}")
                draw()
            }
        }
        return visited
    }

    fun part1(lines: List<String>) : Int {
        var positions : MutableSet<Knot> = mutableSetOf()
        lines.forEachIndexed{ step, move -> println("Step" + step + " - "+ move); positions.addAll(moveString(move));  }
        return positions.size
    }

    fun part2(lines: List<String>) : Int {
        var positions : MutableSet<Knot> = mutableSetOf()
        lines.forEachIndexed{ step, move -> println("Step" + step + " - "+ move); positions.addAll(moveRope(move, 10));  }
        return positions.size
    }

}

fun main() {
    val lines = File("src/main/kotlin/AOC2022/input9.txt").readLines()
    val day9 = Day9()
    println(day9.part1(lines))
    println(day9.part2(lines))
}
