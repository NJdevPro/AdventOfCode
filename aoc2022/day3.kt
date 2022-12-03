import java.io.File

fun <T> splitEqual(list: List<T>, n: Int): List<List<T>> {
    val len = list.size / n
    return list.windowed(size = len, step = len)
}

fun priority(c: Char): Int = if(c.isLowerCase()) c.code - 'a'.code + 1 else c.code - 'A'.code + 27

fun line2LetterVal(line: String): Int{
    val halves = splitEqual(line.toList(), 2)
    for (c in halves[0]) {          // could have used intersect like in part 2
        val found = halves[1].filter{it == c};
        if (found.isNotEmpty()) {return priority(c) }
    }
    return 0
}

fun part1(lines: List<String>):Int = lines.map { line2LetterVal(it) }.sum()

fun lines2Val(block:List<String>): Int {
    val found = block.map{ it.toSet() }.reduce { a, b -> a.intersect(b) }.first()
    return priority(found)
}

fun part2(lines: List<String>):Int = lines.windowed(size = 3, step = 3).sumOf { lines2Val(it) }

fun main() {
    val lines = File("src\\main\\kotlin\\input3.txt").readLines()
    println(part1(lines))
    println(part2(lines))
}
