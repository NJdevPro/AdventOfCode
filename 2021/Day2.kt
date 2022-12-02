package com.njdev.aoc2021

import java.io.File

class Day2 {

    data class Pos(var x: Int, var y: Int)

    companion object {
        var pos = Pos(0,0)

        fun run(fileName: String) = File(fileName).forEachLine { l ->
            val words = l.split(' ')
            val (command, value) = Pair(words[0], words[1].toInt())
            when (command) {
                "forward" -> pos.x += value
                "up" -> pos.y -= value
                "down" -> pos.y += value
            }
        }

        data class Pos2(var x: Int, var y: Int, var aim: Int)
        var pos2 = Pos2(0,0,0)

        fun run2(fileName: String) = File(fileName).forEachLine { l ->
            val words = l.split(' ')
            val (command, value) = Pair(words[0], words[1].toInt())
            when (command) {
                "forward" -> { pos2.x += value
                    pos2.y += pos2.aim * value }
                "up" -> pos2.aim -= value
                "down" -> pos2.aim += value
            }
        }
    }
}

fun main() {
    val fileName = "src\\main\\kotlin\\com\\njdev\\aoc2021\\day2_input.txt"
    println("part 1")
    Day2.run(fileName)
    println(Day2.pos.x * Day2.pos.y)

    println("part 2")
    Day2.run2(fileName)
    println(Day2.pos2.x * Day2.pos2.y)
}

