import java.io.File

fun readInput(fileName: String): List<String> = File(fileName).readLines()

fun letter2Val(c: Char): Int = if(c.isLowerCase()) c.code - 'a'.code + 1 else c.code - 'A'.code + 27

fun line2LetterVal(line: String): Int{
    val half1 = line.toList().subList(0, line.length/2+1)
    val half2 = line.toList().subList(line.length/2, line.length)
    for (c in half1) {
        var found = half2.filter{it == c};
        if (found.isNotEmpty()) {return letter2Val(c) }
    }
    return 0
}

fun part1(lines: List<String>):Int {
    return lines.map { line2LetterVal(it) }.sum()
}

fun lines2Val(group:List<String>): Int {
    var found = group[0].toList().intersect(group[1].toList().intersect(group[2].toList())).last()
    return letter2Val(found)
}

fun part2(lines: List<String>):Int {
    return lines.windowed(size = 3, step = 3).map { lines2Val(it) }.sum()
}

fun main() {
    val filename = "C:\\Users\\Nicolas\\IdeaProjects\\untitled1\\src\\main\\kotlin\\input3.txt"
    val lines = readInput(filename)
    println(part1(lines))
    println(part2(lines))
}