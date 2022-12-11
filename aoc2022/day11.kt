package AOC2022

import java.io.File

class Day11 {

    companion object{
        fun gcd(a: ULong, b: ULong): ULong {
            if (b == 0UL) return a
            return gcd(b, a % b)
        }
        fun lcm(a: ULong, b: ULong): ULong {
            return a / gcd(a, b) * b
        }
        fun lcm(num: List<ULong>): ULong {
            return num.reduce {r, n -> lcm(r, n) }
        }
        var lcm = 1UL
    }

    data class Monkey(val items: MutableList<ULong>,
                      private val operation: String,
                      val divisor: ULong,
                      private val throwToIfTrue: Int, private val throwToIfFalse: Int) {

        var inspected = 0

        fun operate(item : ULong, moderator: (n:ULong)->ULong): ULong {
            var worry = operation.split(' ')
                .let { (instr, operand) ->
                    when(instr) {
                        "+" -> item + if (operand != "old") operand.toULong() else item
                        "*" -> item * if (operand != "old") operand.toULong() else item
                        else -> throw Exception("Unknown operation: $instr")
                    }
                }
            if (worry < 0UL) throw Exception("Negative number: $worry")
            return moderator(worry)
        }

        fun throwTo(worryLevel: ULong) : Pair<Int, ULong> {
            inspected++
            return Pair(if (worryLevel % divisor == 0UL) throwToIfTrue else throwToIfFalse, worryLevel)
        }
    }

    var monkeys: MutableList<Monkey> = mutableListOf()

    fun monkeyBusiness(lines: List<String>, iter: Int, moderator: (n:ULong)->ULong) : ULong {
        for (monkey in parse(lines)) {
            println(monkey)
        }
        lcm = Day11.lcm(monkeys.map{it.divisor}.toList())
        println("LCM = " + lcm)

        (1..iter).forEach{ i ->
            //println("Round " + i)
            for(monkey in monkeys) {
                for (item in monkey.items.toULongArray()) {   // copy to avoid concurrent modification
                    monkey.items.removeAt(0)
                    val (recipient, item) = monkey.throwTo(monkey.operate(item, moderator))
                    monkeys[recipient].items.add(item)
                }
            }
        }
        val sortedByInspected = monkeys.map { it.inspected.toULong() }.sorted().takeLast(2)
        println(sortedByInspected)
        return sortedByInspected[0] * sortedByInspected[1]
    }

    fun parse(lines: List<String>): List<Monkey> {
        var numChunk = 0
        val chunks = lines
            .chunked(7)
            .map { it.filter { it.isNotBlank() } }
        for(chunk in chunks) {
            val monkey = Monkey(
                chunk[1].substring(18).split(',').map { it.trim().toULong() }.toMutableList(),
                chunk[2].substring(23).trim(),
                chunk[3].substring(20).trim().toULong(),
                chunk[4].substring(29).trim().toInt(),
                chunk[5].substring(29).trim().toInt(),
            )
            monkeys.add(monkey)
        }
        return monkeys
    }

    fun part1(lines: List<String> ): ULong {
        return monkeyBusiness(lines, 20, { n : ULong -> n / 3UL })
    }

    fun part2(lines: List<String>  ): ULong {
        monkeys.clear()
        return monkeyBusiness(lines, 10000, { n : ULong -> n / Day11.lcm })
    }
}

fun main() {
    val lines = File("src/main/kotlin/AOC2022/input11.txt").readLines()
    val day11 = Day11()
    println(day11.part1(lines))
    println(day11.part2(lines))
}
