package AOC2022

import java.io.File
import java.lang.Integer.max
import kotlin.math.abs
import kotlin.math.min

class Day9 {

    data class Pos (var x: Int, var y: Int) {
        operator fun plus(pos: Pos?) : Pos = Pos(this.x + pos!!.x, this.y + pos.y)
        operator fun minus(pos : Pos) : Pos = Pos(this.x - pos.x, this.y - pos.y)
        companion object {
            val move = mapOf( "U" to Pos(0,-1), "D" to Pos(0,1), "L" to Pos(-1, 0), "R" to Pos(1,0))
        }
    }

    var H = Pos(0,0)
    var T = Pos(0, 0)

    fun follow (H: Pos, T: Pos) : Pos {
        val dist = H - T
        var T2 = T
        if (abs(dist.x) > 1 && abs(dist.y) > 1) {
            T2 = Pos(if (H.x > T.x) H.x - 1 else H.x + 1, if (H.y > T.y) H.y - 1 else H.y + 1)
        } else if (abs(dist.x) > 1) {
            T2 = Pos(if (H.x > T.x) H.x - 1 else H.x + 1, H.y)
        } else if (abs(dist.y) > 1) {
            T2 = Pos(H.x, if (H.y > T.y) H.y - 1 else H.y + 1)
        }
        return T2
    }

    fun moveString(move: String) : Set<Pos> {
        var visited : MutableSet<Pos> = mutableSetOf()
        move.split(' ').let { (dir, steps) ->
            for(step in 1..steps.toInt()) {
                H += Pos.move[dir]    // move head
                T = follow(H, T)
                visited.add(T.copy())
            }
        }
        return visited
    }

    fun moveRope(move: String, node: Array<Pos>) : Set<Pos> {
        var visited : MutableSet<Pos> = mutableSetOf()
        move.split(' ').let { (dir, steps) ->
            for(step in 1..steps.toInt()) {
                node[0] = node[0] + Pos.move[dir]    // move head, compiler bug against +=
                H = node[0]
                for (i in 0..node.size-2) {
                    node[i+1] = follow(node[i], node[i+1])
                }
                T = node.last()
                visited.add(T.copy())
                //println("move  ${step}, ${dir}, H=${H}, T=${T}")
            }
        }
        return visited
    }

    fun part1(lines: List<String>) : Int {
        var positions : MutableSet<Pos> = mutableSetOf()
        lines.forEachIndexed{ step, move ->
            //println("Step" + step + " - "+ move);
            positions.addAll(moveString(move));
        }
        return positions.size
    }

    fun part2(lines: List<String>) : Int {
        var positions : MutableSet<Pos> = mutableSetOf()
        var knots: Array<Pos> = Array(size=10, init = { Pos(0,0)})
        lines.forEachIndexed{ step, move ->
            //println("Step" + step + " - "+ move);
            positions.addAll(moveRope(move, knots));
        }
        return positions.size
    }

}

fun main() {
    val lines = File("src/main/kotlin/AOC2022/input9.txt").readLines()
    val day9 = Day9()
    println(day9.part1(lines))
    println(day9.part2(lines))
}
