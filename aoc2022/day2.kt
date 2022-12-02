import java.io.File

fun readFileAsLines(fileName: String): List<String>  = File(fileName).useLines { it.toList() }

fun rate(line: String): Int = when (line) {
        "A X" -> 1+3
        "A Y" -> 2+6
        "A Z" -> 3+0
        "B X" -> 1+0
        "B Y" -> 2+3
        "B Z" -> 3+6
        "C X" -> 1+6
        "C Y" -> 2+0
        "C Z" -> 3+3
        else -> -99999999
    }

fun rate2(line: String): Int = when (line) {
        "A X" -> 3 + 0 // Z
        "A Y" -> 1 + 3 // X
        "A Z" -> 2 + 6 // Y
        "B X" -> 1 + 0 // X
        "B Y" -> 2 + 3 // Y
        "B Z" -> 3 + 6 // Z
        "C X" -> 2 + 0 // Y
        "C Y" -> 3 + 3 // Z
        "C Z"-> 1 + 6 // X
        else -> -99999999
    }

fun part1(lines: List<String> ): Int = lines.map{rate(it)}.sum()

fun part2(lines: List<String> ): Int = lines.map{rate2(it)}.sum()

fun main(){
    val lines = readFileAsLines("/home/njanin/IdeaProjects/kotlin_dp/src/main/kotlin/AOC2022/input2.txt")
    println("Score : ${part1(lines)}")
    println("Score : ${part2(lines)}")
}
