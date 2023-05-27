package main

import (
	"bufio"
	"fmt"
	"os"
)

var board [101][101]int
var di = [4][2]int {
	{-1, 0}, 
	{1, 0}, 
	{0, -1}, 
	{0, 1},
}
var visited [101][101]bool
var bufin = bufio.NewReader(os.Stdin)
var bufout = bufio.NewWriter(os.Stdout)

func main() {
	var Y, X int
	fmt.Fscan(bufin, &Y, &X)
	board := make([][]int, Y)
	visited := make([][]bool, Y, X)

	for y := range board {
		board[y] = make([]int, X)
		visited[y] = make([]bool, X)
		var temp string
		fmt.Fscan(bufin, &temp)
		for x, c := range temp {
			board[y][x] = int(c - '0')
		}
	}

	fmt.Println()
	for y := 0; y < Y; y++ {
		for x := 0; x < X; x++ {
			fmt.Print(visited[y][x])
		}
		fmt.Println()
	}
}