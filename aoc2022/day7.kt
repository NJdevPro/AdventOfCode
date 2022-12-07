import java.io.File

private const val MAX_SPACE = 100000
private const val NEEDED_SPACE = 30000000
private const val TOTAL_SPACE = 70000000

private fun buildFilesystem() = parseInput().fold(Filesystem()) { fs, input -> fs.parse(input) }

data class Filesystem(val root: Dir, var current: Dir?) {
    constructor() : this(root = Dir("/"))
    constructor(root: Dir) : this(root = root, current = root)

    fun parse(input: List<String>): Filesystem =
        input.let { (arg1, arg2, arg3) ->
            when (arg1) {
                "$" -> current = when (arg3) {
                    null -> current
                    "/" -> root
                    ".." -> current?.parent
                    else -> current?.directories?.find { it.path == arg3 }
                }
                "dir" -> current?.directories?.add(Dir(path = arg2, parent = current))
                else -> current?.files?.add(arg1.toInt())
            }

            return this
        }
}

data class Dir(
    val path: String,
    val parent: Dir? = null,
    val directories: ArrayList<Dir> = ArrayList(),
    val files: ArrayList<Int> = ArrayList()
) {
    fun size(): Int = files.sumOf { it } + directories.sumOf { it.size() }

    fun flatten(): List<Dir> = directories + directories.flatMap { it.flatten() }
}

private fun parseInput() = File("src/main/kotlin/AOC2022/input7.txt").readLines().map { it.split(" ") }

operator fun List<String>.component3(): String? = getOrNull(2)

fun partOne() = buildFilesystem().root.flatten().map { it.size() }.filter { space -> space <= MAX_SPACE }.sum()

fun partTwo() = buildFilesystem().let { fs ->
    fs.root.flatten().map { it.size() }.sorted().first { space -> space >= NEEDED_SPACE - (TOTAL_SPACE - fs.root.size()) }
}

fun main() {
    println(partOne())
    println(partTwo())
}
