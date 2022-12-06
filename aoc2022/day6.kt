package AOC2022

import java.io.File
import java.nio.charset.Charset

fun readFileAsLines(fileName: String): String  = File(fileName).readText(Charset.defaultCharset())

class Day6 {
    fun part1(lines: String ): Int = lines.windowed(size=4, step=1) {it.toSet()}.indexOfFirst { it.size == 4 } + 4

    fun part2(lines: String): Int = lines.windowed(size=14, step=1) {it.toSet()}.indexOfFirst { it.size == 14 } + 14
}

fun main(){
    val lines = readFileAsLines("src/main/kotlin/AOC2022/input6.txt")
    val day6 = Day6()
    println("Score : ${day6.part1(lines)}")
    println("Score : ${day6.part2(lines)}")
}
