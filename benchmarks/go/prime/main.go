package main

import (
	"fmt"
	"math/big"
	"os"
	"strconv"
	"time"
)

func primeCount(n int, verbose bool) *big.Int {
	count := big.NewInt(0)
	if n < 2 {
		return count
	}

	isPrime := make([]bool, n+1)
	for i := 2; i <= n; i++ {
		isPrime[i] = true
	}

	for p := 2; p*p <= n; p++ {
		if isPrime[p] {
			for multiple := p * p; multiple <= n; multiple += p {
				isPrime[multiple] = false
			}
		}
	}

	for i := 2; i <= n; i++ {
		if isPrime[i] {
			count.Add(count, big.NewInt(1))
			if verbose {
				fmt.Printf("Prime: %d\n", i)
			}
		}
	}

	return count
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: primecount <N> [--verbose]")
		return
	}

	n, _ := strconv.Atoi(os.Args[1])
	verbose := len(os.Args) > 2 && os.Args[2] == "--verbose"

	start := time.Now()
	result := primeCount(n, verbose)
	elapsed := float64(time.Since(start).Nanoseconds()) / 1e6

	fmt.Printf("[PrimeCount] Result = %s\n", result.String())
	fmt.Printf("[PrimeCount] Time   = %.3f ms\n", elapsed)
}
