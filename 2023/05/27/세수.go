package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var bufin = bufio.NewReader(os.Stdin)
var bufout = bufio.NewWriter(os.Stdout)

func main() {
	var list = make([]int, 3)
	fmt.Fscan(bufin, &list[0], &list[1], &list[2])
	sort.Ints(list)
	fmt.Printf("%d", list[1])
}