package main

import (
	"bufio"
	"os"
)

func main() {
	// file, _ := os.Open("text/2751.txt")
	// sc := bufio.NewScanner(file)
	// sc := bufio.NewScanner(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

}