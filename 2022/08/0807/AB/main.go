package main

import (
	"bufio"
	"fmt"
	"os"
)
var file, _ = os.Open("text/2558.txt")
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


func main() {
	A := NextInt()
	B := NextInt()
	fmt.Println(A + B)
}