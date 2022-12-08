import java.io.File

class Day8{

    fun grid(lines: List<String>): ArrayList<List<Int>> = ArrayList(lines.map{it.toList().map{it.digitToInt()}})

    fun part1(lines: List<String>): Int {
        var visible = 0
        val rows = grid(lines)
        for(i in 0.. rows.size-1) {
            val row = rows.get(i)
            for (j in 0.. row.size-1){
                if(i ==0 || i == rows.size-1 || j == 0 || j == row.size-1) {
                    visible++
                    continue
                }
                var tree = row.get(j)
                var col = mutableListOf<Int>()
                for(k in 0.. rows.size-1) { col.add(rows.get(k).get(j)) }
                val left = row.subList(0,j).all{ it < tree }
                val right = row.subList(j+1, row.size).all{it < tree}
                val up = col.subList(0,i).all{it < tree }
                val down = col.subList(i+1, col.size).all{it < tree}
                if (left || right || up || down ) visible++
            }
        }
        return visible
    }

    inline fun <T> Iterable<T>.takeUntil(predicate: (T) -> Boolean): List<T> {
        val list = ArrayList<T>()
        for (item in this) {
            list.add(item)
            if (predicate(item))
                break
        }
        return list
    }

    fun part2(lines: List<String>) : Int {
        var max = 0
        val rows = grid(lines)
        for(i in 0.. rows.size-1) {
            val row = rows.get(i)
            for (j in 0.. row.size-1){
                var tree = row.get(j)
                var col = mutableListOf<Int>()
                for(k in 0.. rows.size-1) { col.add(rows.get(k).get(j)) }
                val left = row.subList(0,j).reversed().takeUntil{ it >= tree }.count()
                val right = row.subList(j+1, row.size).takeUntil{ it >= tree }.count()
                val up = col.subList(0,i).reversed().takeUntil{ it >= tree }.count()
                val down = col.subList(i+1, col.size).takeUntil{ it >= tree }.count()
                //println("($i,$j) = $tree : ${left}, ${right}, ${up}, ${down}")
                val scenic_score = left * right * up * down
                if (scenic_score >= max) max = scenic_score
            }
        }
        return max
    }
}

fun main() {
    val lines = File("src/main/kotlin/AOC2022/input8.txt").readLines()
    val day8 = Day8()
    println(day8.part1(lines))
    println(day8.part2(lines))
}
