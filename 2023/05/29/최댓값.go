package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)
var file, _ = os.Open("./input/2566.txt")
var bufin = bufio.NewReader(file)
// var bufin = bufio.NewReader(os.Stdin)
var bufout = bufio.NewWriter(os.Stdout)

func main() {
	max := make([]int, 9)
	for i := 0; i < 9; i++ {
		list := make([]int, 9)
		for i := 0; i < 9; i++ {
			fmt.Fscan(bufin, &list[i])
		}
		sort.Ints(list)
		max[i] = list[0]
	}
	fmt.Println(max)
}