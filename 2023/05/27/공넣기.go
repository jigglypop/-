package main

import (
	"bufio"
	"fmt"
	"os"
)
var file, _ = os.Open("./input/10810.txt")
var bufin = bufio.NewReader(file)
// var bufin = bufio.NewReader(os.Stdin)
var bufout = bufio.NewWriter(os.Stdout)

func main() {
	var N, M int
	fmt.Fscan(bufin, &N, &M)
	board := make([]int, N + 1)
	for i := 0; i< M;i++ {
		var s, e, v int
		fmt.Fscan(bufin, &s, &e, &v)
		for i := s;i<= e;i++ {
			board[i] = v
		}
	}
	for i := 1;i<= N;i++ {
		fmt.Print(board[i], " ")
	}
}