package main

import (
	"bufio"
	"fmt"
	"os"
)
var file, _ = os.Open("./input/2178.txt")
var bufin = bufio.NewReader(file)
// var bufin = bufio.NewReader(os.Stdin)
var bufout = bufio.NewWriter(os.Stdout)

type P struct {
	y, x int
}
var di = [...]P{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

func main() {
	var Y, X int
	fmt.Fscan(bufin, &Y, &X)
	visited := make([][]int, Y)
	board := make([][]int, Y)
	for y := 0; y < Y; y++ {
		visited[y] = make([]int, X)
		board[y] = make([]int, X)
		var temp string
		fmt.Fscan(bufin, &temp)
		for x, v := range temp {
			board[y][x] = int(v - '0')
		}
	}
	Q :=  make([]P, 0, Y * X)
	Q = append(Q, P{0, 0})
	visited[0][0] = 1
	for len(Q) > 0 {
		p := Q[0]
		Q = Q[1:]
		for _, d := range di {
			ny := p.y + d.y
			nx := p.x + d.x
			if 0 <= ny && ny < Y && 0 <= nx && nx < X {
			if (visited[ny][nx] == 0) && (board[ny][nx] == 1) {
				Q = append(Q, P{ny, nx})
				visited[ny][nx] = visited[p.y][p.x] + 1
			}
		}
		}
	}
	for _, v := range visited {
		fmt.Println(v)
	}
	fmt.Println(visited[Y-1][X-1])
}