package com.njdev.aoc2021

import java.io.File

class Day1 {
    val depth: List<Int> = listOf(
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263
    )

    companion object {
        fun inc(depth: List<Int>): Int = depth.zipWithNext() { a, b -> a >= b }.count { it -> !it }

        fun readInput(fileName: String) = File(fileName).readLines().map { it.toInt() }

        fun avg_w(depth: List<Int>): List<Int> =
            depth.windowed(size = 3, step = 1, partialWindows = false).map { l -> l.sum() }
    }
}
fun main(){
    val depth = Day1.readInput("src\\main\\kotlin\\com\\njdev\\aoc2021\\Day1_input.txt")
    println("Part 1")
    println(Day1.inc(depth))
    println("Part 2")
    // println(Day1.avg_w(depth))
    print(Day1.inc(Day1.avg_w(depth)))
}
