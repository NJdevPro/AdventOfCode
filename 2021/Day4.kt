package com.njdev.aoc2021

import java.io.File

class Day4 {

    lateinit var draws: List<Int>

    class Card(val grid: Array<IntArray>,
               var sum: Int = 0, var win: Int = 0,
               var h: IntArray = IntArray(5),
               var v: IntArray = IntArray(5)
    )

    private val cards: MutableList<Card> = ArrayList()

    fun draws(line: String) = line.split(',').map { s -> s.toInt() }

    private fun readCard(lines: List<String>): Card {
        val grid = Array(5) { IntArray(lines[0].split(' ').size) }
        for(i in grid.indices){
            val numbers = lines[i].split(' ').filter{ !it.isEmpty() }
            grid[i] = numbers.map { s -> s.trim().toInt() }.toIntArray()
        }
        return Card(grid)
    }

    fun readInput(fileName: String) {
        val lines = ArrayDeque(File(fileName).readLines())

        draws = draws(lines.removeFirst())
        lines.removeFirst()

        // read the tables
        while(!lines.isEmpty()){
            cards.add(readCard(lines.take(5)))
            lines.subList(0,5).clear()
            if (!lines.isEmpty()) lines.removeFirst()
        }
    }

    fun mark(): Card {

        for (num in draws) {
            for (card in cards){
                for(j in card.grid.indices) {   // colomns
                    var row = card.grid[j]
                    for(i in row.indices){
                        if(row[i] == num){
                            card.h[i] += 1
                            card.v[j] += 1
                            card.sumv += row[i]
                        }
                        if(card.h[i] == 5){   // Bingo
                            card.sum = row.sum()
                            card.win = num
                            return card
                        }
                        if(card.v[i] == 5){   // Bingo
                            card.sum = sumv
                            card.win = num
                            return card
                        }
                    }
                }
            }
        }
        return Card(Array(5){ IntArray(5) })
    }

    fun score(card: Card) : Int {
        var sum = card.grid.flatMap { it.toList() }.sum()
        if(card.sum > 0){
            sum -= card.sum
        }
        return sum * card.win
    }

}

fun main() {
    val fileName = "C:\\Users\\Nicolas\\IdeaProjects\\AoC\\src\\main\\kotlin\\com\\njdev\\aoc2021\\day4_input.txt"
    val d4 = Day4()

    println("part 1")
    d4.readInput(fileName)
    val winningCard = d4.mark()
    println("Score: " + d4.score(winningCard))

    println("part 2")
}