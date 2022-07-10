package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var file, _ = os.Open("test/2178.txt")
var reader = bufio.NewReader(file)

func nextInt() int {
	var n int
	_, _ = fmt.Fscan(reader, &n)
	return n
}

func nextString() string {
	var s string
	_, _ = fmt.Fscan(reader, &s)
	return s
}

func main() {
	sc := bufio.NewScanner(file)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	var N int
	var nums []int

	if sc.Scan() {
		N, _ = strconv.Atoi(sc.Text())
	}
	nums = make([]int, N)
	for i := 0;i < N;i++ {
		if sc.Scan() {
			nums[i], _ = strconv.Atoi(sc.Text())
		}
	}

	sort.Ints(nums)
	for _, v := range nums {
		fmt.Fprintln(w, v)
	}
}