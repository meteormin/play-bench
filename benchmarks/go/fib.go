package main

import (
	"fmt"
	"math/big"
	"os"
	"strconv"
	"time"
)

func fib(n int, verbose bool) *big.Int {
	a := big.NewInt(0)
	b := big.NewInt(1)

	for i := 0; i < n; i++ {
		if verbose {
			fmt.Printf("Step %d: %s\n", i, a.String())
		}
		tmp := new(big.Int).Set(a)
		a.Set(b)
		b.Add(tmp, b)
	}
	return a
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: fib <N> [--verbose]")
		return
	}
	n, _ := strconv.Atoi(os.Args[1])
	verbose := len(os.Args) > 2 && os.Args[2] == "--verbose"

	start := time.Now()
	result := fib(n, verbose)
	elapsed := float64(time.Since(start).Nanoseconds()) / 1e6

	fmt.Printf("[Fibonacci] Result = %s\n", result.String())
	fmt.Printf("[Fibonacci] Time   = %.3f ms\n", elapsed)
}
