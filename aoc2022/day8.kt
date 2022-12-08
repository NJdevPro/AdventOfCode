import java.io.File

class Day8{

    fun grid(lines: List<String>): ArrayList<List<Int>> = ArrayList(lines.map{it.toList().map{it.digitToInt()}})

    fun part1(lines: List<String>): Int {
        var visible = 0
        var colsize = 0
        val grid = grid(lines)
        for(i in 1.. grid.size-2) {
            val row = grid.get(i)
            for (j in 1.. row.size-2){
                var tree = row.get(j)
                var col = mutableListOf<Int>()
                for(k in 0.. grid.size-1) {
                    col.add(grid.get(k).get(j))
                }
                colsize = col.size-2
                val left = row.subList(0,i).all{it < tree }
                val right = row.subList(i+1,row.size).all{it < tree}
                val up = col.subList(0,j).all{it < tree }
                val down = col.subList(j+1, col.size).all{it < tree}
                if (left || right || up || down ) visible++
            }
        }
        return 1+visible + grid.size*2 + colsize*2
    }

//    fun part2(lines: List<String>): Int = lines.windowed(size = 3, step = 3).sumOf { lines2Val(it) }
//
//    }
}

fun main() {
    val lines = File("src\\main\\kotlin\\input8.txt").readLines()
    val day8 = Day8()
    println(day8.part1(lines))
    //println(day8.part2(lines))
}