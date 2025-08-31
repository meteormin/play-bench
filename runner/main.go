package main

import (
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"strings"
	"time"
)

// BenchmarkResult holds one run result
type BenchmarkResult struct {
	Lang    string  `json:"lang"`
	Version string  `json:"version"`
	Result  string  `json:"result"`
	TimeMS  float64 `json:"time_ms"`
}

// Summary holds the benchmark summary
type Summary struct {
	Benchmark string            `json:"benchmark"`
	Date      string            `json:"date"`
	Algo      string            `json:"algo"`
	N         int               `json:"n"`
	Results   []BenchmarkResult `json:"results"`
}

func runCommand(name string, args ...string) (string, error) {
	cmd := exec.Command(name, args...)
	out, err := cmd.CombinedOutput()
	return string(out), err
}

func parseResult(output string) (result string, elapsed float64) {
	lines := strings.Split(strings.TrimSpace(output), "\n")
	for _, line := range lines {
		if strings.Contains(line, "Result") {
			parts := strings.Split(line, "=")
			if len(parts) > 1 {
				result = strings.TrimSpace(parts[1])
			}
		} else if strings.Contains(line, "Time") {
			parts := strings.Split(line, "=")
			if len(parts) > 1 {
				// "123.456 ms"
				val := strings.TrimSpace(parts[1])
				val = strings.TrimSuffix(val, "ms")
				f, _ := strconv.ParseFloat(strings.TrimSpace(val), 64)
				elapsed = f
			}
		}
	}
	return
}

var commands = map[string]map[string][]string{
	"fib": {
		// ✅ 사전 빌드된 바이너리/클래스 실행
		"go":     {"benchmarks/go/fib"},                     // go build -o benchmarks/go/fib fib.go
		"python": {"python3", "benchmarks/python/fib.py"},   // 인터프리터 그대로
		"java":   {"java", "-cp", "benchmarks/java", "Fib"}, // javac으로 class 미리 생성
		"c":      {"benchmarks/c/fib"},                      // gcc fib.c -o fib
		"rust":   {"benchmarks/rust/target/release/fib"},    // rustc fib.rs -o fib
		"js":     {"node", "benchmarks/js/fib.js"},          // Node.js 그대로 실행
		"php":    {"php", "benchmarks/php/fib.php"},         // PHP 그대로 실행
	},
	// TODO: "prime": {...},
}

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Usage: runner <algo> <N>")
		return
	}
	algo := os.Args[1]
	n := os.Args[2]

	algoCmds, ok := commands[algo]
	if !ok {
		fmt.Printf("Unknown algorithm: %s\n", algo)
		return
	}

	var results []BenchmarkResult
	totalStart := time.Now()

	for lang, baseCmd := range algoCmds {
		args := append(baseCmd[1:], n)
		output, err := runCommand(baseCmd[0], args...)
		if err != nil {
			fmt.Printf("Error running %s (%s): %v\n", algo, lang, err)
			fmt.Println(output)
			continue
		}
		result, elapsed := parseResult(output)

		results = append(results, BenchmarkResult{
			Lang:    lang,
			Version: "TODO",
			Result:  result,
			TimeMS:  elapsed,
		})
		fmt.Printf("[%s-%s] reported %.3f ms\n", algo, lang, elapsed)
	}

	totalElapsed := time.Since(totalStart).Milliseconds()

	summary := Summary{
		Benchmark: "play-bench",
		Date:      time.Now().UTC().Format(time.RFC3339),
		Algo:      algo,
		N:         func() int { i, _ := strconv.Atoi(n); return i }(),
		Results:   results,
	}

	outPath := filepath.Join("results", fmt.Sprintf("%s_summary.json", algo))
	data, _ := json.MarshalIndent(summary, "", "  ")
	if err := os.WriteFile(outPath, data, 0644); err != nil {
		fmt.Printf("Error writing summary file: %v\n", err)
		return
	}

	fmt.Printf("Summary written to %s (runner time: %d ms)\n", outPath, totalElapsed)
}
