import java.io.File

class Day4 {
    private val rex = "^(\\d+)-(\\d+),(\\d+)-(\\d+)".toRegex()

    fun parse(line: String, regex: Regex): Pair<IntRange, IntRange> {
        val matches = regex.find(line);
        val (a,b,c,d) = matches!!.destructured
        val team = a.toInt()..b.toInt()
        val section = c.toInt()..d.toInt()
        return Pair(team, section)
    }

    operator fun IntRange.contains(r: IntRange) = this.first <= r.first && this.last >= r.last

    fun IntRange.overlaps(r: IntRange) =
        (r.first >= this.first && r.first <= this.last) || (r.last >= this.first && r.last <= this.last)

    fun part1(lines: List<String>) = lines.map {
            val (team, section) = parse(it, rex)
            if(team in section || section in team) 1 else 0
    }.sum()

    fun part2(lines: List<String>) :Int =  lines.map {
        val (team, section) = parse(it, rex)
        if(section.overlaps(team)) 1 else 0
    }.sum()
}

fun main() {
    val lines = File("src\\main\\kotlin\\input4.txt").readLines()
    val day4 = Day4()
    println(day4.part1(lines))
    println(day4.part2(lines))
}