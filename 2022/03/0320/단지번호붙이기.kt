import java.util.*
import java.io.*

lateinit var visited: Array<Array<Boolean>>
lateinit var board: Array<Array<Int>>
var n = 0;
var count = 0;
var dx = arrayOf(0, 0, 1, -1)
var dy = arrayOf(1, -1, 0, 0)

fun dfs(y: Int, x: Int) {
  count++
  visited[y][x] = true
  for (i in 0..3) {
    var ny = y + dy[i]
    var nx = x + dx[i]
    if (0 <= nx && nx < n && 0 <= ny && ny < n) {
      if (!visited[ny][nx] && board[ny][nx] == 1) {
        dfs(ny, nx)
      }
    }
  }
  return
}

fun main() = with(BufferedReader(InputStreamReader(FileInputStream("./단지번호붙이기.txt")))) {
// fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
  n = readLine().toInt()
  board = Array(n, { Array(n, { 0 }) })
  for (y in 0..n-1) {
    var str = StringTokenizer(readLine()).nextToken()
    for (x in 0..str!!.length - 1) {
      board[y][x] = str[x].toInt() - 48
    }
  }
  var counts = 0
  visited = Array(n, { Array(n, { false }) })
  var results = arrayListOf<Int>()
  for (y in 0..n-1) {
    for (x in 0..n-1) {
      if (!visited[y][x] && board[y][x] == 1){
        counts++
        dfs(y, x)
        results.add(count)
        count = 0
      }
    }
  }
  results.sort()
  println(counts)
  for (i in 0..results.size - 1) {
    println(results[i])
  }
}