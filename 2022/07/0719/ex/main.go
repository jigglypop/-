package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)



func main() {
	file, _ := os.Open("text/2751.txt")
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