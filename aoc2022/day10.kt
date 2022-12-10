package AOC2022

import java.io.File

class Day10 {

    private var clock = 1
    private var reg = 1
    private val peeks = (20..220 step 40)
    private val cycles : MutableMap<Int, Int> = mutableMapOf()

    fun exec(line: String) : Unit {
        if (line.startsWith ("noop")) { cycles[clock++] = reg; }
        else if (line.startsWith("addx")) {
            line.split(' ').let { (instr, operand) ->
                cycles[clock++] = reg
                cycles[clock++] = reg
                reg += operand.toInt()
            }
        }
    }

    fun printPix(clock: Int, reg: Int) {
        print(if((clock % 40) -1 in (reg-1..reg+1)) '*' else " ")
        if(clock % 40 == 0) println()
    }

     fun update() {            
        printPix(clock, cycles[clock]!!)
        clock++
    }
    
    fun draw(line: String) : Unit {
        if (line.startsWith ("noop")) {
            update()
        }
        else if (line.startsWith("addx")) {
            (1..2).forEach { update() }
        }
    }

    fun part1(lines: List<String> ): Int {
        lines.forEach{exec(it)}
        return peeks.map {cycles[it]!! * it }.sum()
    }

    fun part2(lines: List<String>  ): Unit {
        clock = 1
        reg = 1
        lines.forEach{ draw(it) }
    }
}

fun main() {
    val lines = File("src/main/kotlin/AOC2022/input10.txt").readLines()
    val day10 = Day10()
    println(day10.part1(lines))
    println(day10.part2(lines))
}
