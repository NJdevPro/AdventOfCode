import java.io.File
import kotlin.collections.maxOrNull

fun file2List(fileName: String): List<String> = File(fileName).useLines { it.toList() }
fun readFileAsText(fileName: String): String = File(fileName).readText(Charsets.UTF_8)

fun calories(lines: List<String>): List<Int> {
    var menus : MutableList<MutableList<Int>> = mutableListOf()
    for (line in lines){
        if(line.isEmpty()){
            menus.add(mutableListOf<Int>())
        }
        else {
            menus.last().add(line.toInt())
        }
    }

    return menus.map{it.sum()}
}

fun top3(calories: List<Int>): Int? = calories.sortedDescending().take(3).sum()

fun main(args: Array<String>) {
    val lines = file2List("C:\\Users\\Nicolas\\IdeaProjects\\untitled1\\src\\main\\kotlin\\input1.txt")
    val calories = calories(lines)
    println("Max calories: ${calories.maxOrNull()}")
    println("Top 3 sum: ${top3(calories)}")
}
