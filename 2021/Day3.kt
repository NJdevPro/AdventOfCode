package com.njdev.aoc2021

import java.io.File

class Day3 {

    companion object {

        fun readInput(fileName: String): List<String> = File(fileName).readLines()

        fun zeros(nums: List<String>, idx: Int): Int = nums.count{it[idx] == '0'}

        fun power(nums: List<String>): Int {
            var gamma : String = ""
            var epsilon : String = ""
            for (i in nums[0].indices){
                val zeros = zeros(nums, i)
                val ones = nums.size - zeros
                if (zeros >= ones) {
                    gamma += '0'
                    epsilon += '1'
                } else {
                    gamma += '1'
                    epsilon += '0'
                }
            }
            return Integer.parseInt(gamma, 2) * Integer.parseInt(epsilon, 2)
        }

        fun o2GR(nums: MutableList<String>) : Int {
            for (i in nums[0].indices){
                val zeros = zeros(nums, i)
                val ones = nums.size - zeros
                if (nums.size == 1) break
                if (zeros <= ones) {
                    nums.removeIf { it[i] == '1' }
                } else {
                    nums.removeIf { it[i] == '0' }
                }
            }
            return Integer.parseInt(nums[0], 2)
        }

        fun co2(nums: MutableList<String>) : Int {
            for (i in nums[0].indices){
                val zeros = zeros(nums, i)
                val ones = nums.size - zeros
                if (nums.size == 1) break
                if (ones >= zeros) {
                    nums.removeIf { it[i] == '0' }
                } else {
                    nums.removeIf { it[i] == '1' }
                }
            }
            return Integer.parseInt(nums[0], 2)
        }
    }
}

fun main() {
    val fileName = "C:\\Users\\Nicolas\\IdeaProjects\\AoC\\src\\main\\kotlin\\com\\njdev\\aoc2021\\day3_input.txt"
    println("part 1")
    val nums = Day3.readInput(fileName)
    println(Day3.power(nums))

    println("part 2")
    val nums2 = nums.toMutableList()
    val nums3 = nums.toMutableList()
    println(Day3.co2(nums3) * Day3.o2GR(nums2))
}