package main

import (
	"bufio"
	"fmt"
	"os"
)
var file, _ = os.Open("./input/10870.txt")
var bufin = bufio.NewReader(file)
// var bufin = bufio.NewReader(os.Stdin)
var bufout = bufio.NewWriter(os.Stdout)

func main() {
	var N int
	fmt.Fscan(bufin, &N)
	dp := make([]int, N + 1)
	dp[1] = 1
	if (N >= 2) {
		for i := 2;i <= N; i++ {
			dp[i] = dp[i - 1] + dp[i - 2]
		}
	}
	fmt.Println(dp[N])
}