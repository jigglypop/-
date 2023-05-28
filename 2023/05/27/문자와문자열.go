package main

import (
	"bufio"
	"fmt"
	"os"
)
var file, _ = os.Open("./input/27866.txt")
var bufin = bufio.NewReader(file)
// var bufin = bufio.NewReader(os.Stdin)
var bufout = bufio.NewWriter(os.Stdout)

func main() {
	var S string
	var N int
	fmt.Fscan(bufin, &S)
	fmt.Fscan(bufin, &N)
	fmt.Fprintf(bufout, "%c", S[N - 1])
	bufout.Flush()
}