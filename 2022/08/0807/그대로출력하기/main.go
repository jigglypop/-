package main

import (
	"bufio"
	"fmt"
	"os"
)
var file, _ = os.Open("text/11718.txt")
var in = bufio.NewScanner(file)
// var in = bufio.NewScanner(os.Stdin)
var	out = bufio.NewWriter(os.Stdout)

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

func main() {
	defer out.Flush()
	for in.Scan() {
		line := in.Text()
		fmt.Fprintln(out, line)
	}
}