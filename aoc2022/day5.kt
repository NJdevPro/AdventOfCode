import java.io.File
import java.util.Stack

class Day5 {

    private val height = 8
    private val width = 9

    fun parse(lines: List<String>) : MutableList<Stack<Char>> {
        var stacks : MutableList<Stack<Char>> = MutableList(width) { Stack() }
        for (i in height-1 downTo 0) {
            var row = lines[i].windowed(size=4, step=4, partialWindows = true).map { it[1] }
            row.mapIndexed { index, c -> if (c.isLetter()) stacks[index].add(c) }
        }
        return stacks
    }

    fun moveOneByOne(stacks:  MutableList<Stack<Char>>, from: Int, to: Int, qty: Int) {
        for(i in 1.. qty) {
            stacks[to - 1].push(stacks[from - 1].pop())
        }
    }

    fun moveBySubstack(stacks:  MutableList<Stack<Char>>, from: Int, to: Int, qty: Int) {
        var temp = Stack<Char>()
        for(i in 1.. qty) { temp.push(stacks[from - 1].pop()) }
        temp.reversed().forEach(){stacks[to - 1].push(it)}
    }

    fun solution(lines: List<String>,
                 method: (stacks:  MutableList<Stack<Char>>, from: Int, to: Int, qty: Int) -> Int ) : String {
        var stacks = parse(lines.subList(0, height))
        val moves = lines.subList(height + 2, lines.size)
        val regex = "move (\\d+) from (\\d+) to (\\d+)".toRegex()
        moves.forEach {
            val (qty, from, to) = regex.find(it)!!.destructured.toList().map { it.toInt() }
            method(stacks, from, to, qty)
        }
        return stacks.map { it.lastOrNull() }.joinToString()
    }

    fun part1(lines: List<String>) : String = solution(lines, ::moveOneByOne)

    fun part2(lines: List<String>) : String = solution(lines, ::moveBySubstack)
}


fun main() {
    val lines = File("src\\main\\kotlin\\input5.txt").readLines()
    val day5 = Day5()
    println(day5.part1(lines))
    println(day5.part2(lines))
}
