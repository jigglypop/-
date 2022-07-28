package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)
var file, _ = os.Open("dfs/2667.txt")
var in = bufio.NewScanner(file)
// var in = bufio.NewScanner(os.Stdin)

func NextInt() int {
	in.Scan()
	r := 0
	for _, c := range in.Bytes() {
		r *= 10
		r += int(c - '0')
	}
	return r
}

func Next() []byte {
	in.Scan()
	return in.Bytes()
}

type point struct{ x, y int }

func main() {
	m := make(map[point]bool)
	n := NextInt()
	for i := 0; i < n; i++ {
		for j, v := range Next() {
			if v == '1' {
				m[point{i, j}] = true
			}
		}
	}
	var f func(point) int
	f = func(p point) int {
		r := 1
		delete(m, p)
		for _, v := range [...]point{{p.x - 1, p.y}, {p.x + 1, p.y}, {p.x, p.y - 1}, {p.x, p.y + 1}} {
			if m[v] {
				r += f(v)
			}
		}
		return r
	}
	var r []int
	for len(m) > 0 {
		for k := range m {
			r = append(r, f(k))
			break
		}
	}
	sort.Ints(r)
	fmt.Println(len(r))
	for _, v := range r {
		fmt.Println(v)
	}
}