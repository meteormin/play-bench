# Play Bench

> Benchmarking programming languages with simple and fun algorithms 🚀

## Overview

**Play Bench** is a project to compare programming languages by running simple algorithms
and measuring execution time (and later CPU & memory usage).  
The goal is to provide a fair, reproducible, and fun playground for benchmarking.

## Requirements

To build and run all benchmarks you will need:

-   **Go** 1.25+
    - `brew install go@1.25`
-   **Python** 3.13+
-   **Java** 21+ (JDK required for `javac` and `java`)
    - `brew install openjdk@21`
-   **C compiler** (GCC 13+ or Clang)
    - `brew install gcc`
-   **Rust** (latest stable, includes `rustc` and `cargo`)
    - `brew install rust`
-   **Node.js** 22+
    - `brew install node@22`
-   **PHP** 8.4+
    - `brew install php@8.4`

Additionally:

-   **GNU Make / Bash** (for build and run scripts)
    -   `brew install make`
-   Linux or macOS environment (Windows may need WSL2 or MinGW)

## Algorithms

Currently included (planned to expand):

-   Fibonacci sequence (iterative)
-   Prime counting
-   Matrix multiplication

## Supported Languages

-   Go 1.25
-   Python 3.13
-   Java 21
-   C (GCC / Clang)
-   Rust (latest stable)
-   JavaScript (Node.js 22+)
-   PHP 8+

## Project Structure

```sh
play-bench/
├── benchmarks/      # Benchmark implementations per language
│   ├── c/
│   ├── go/
│   ├── java/
│   ├── python/
│   ├── rust/
│   ├── js/
│   └── php/
├── runner/          # Automation and result collection tools
├── scripts/         # Build and execution scripts
├── results/         # Raw logs and summarized statistics
└── README.md        # Project documentation
```

## Roadmap

-   Add more algorithms

-   Add memory & CPU usage monitoring

-   Create a unified runner to execute all benchmarks and aggregate results

-   Visualization of benchmark results

-   Explore concurrency and parallelism benchmarks (e.g., threads, async tasks)

## Design

### Input Specification

Each benchmark program must accept:

-   Required:

    -   `N` (integer) → input size parameter (e.g., Fibonacci Nth term, Prime range, Matrix size)

-   Optional:
    -   `--verbose` (flag) → if present, print intermediate steps

Example:

```sh
# run Fibonacci with N=40
./fib 40
# run Fibonacci with N=40 and verbose output
./fib 40 --verbose
```

### Output Specification

Every benchmark must print results in the following format:

```sh
[<Algorithm>] Result = <computed result>
[<Algorithm>] Time = <elapsed time in ms>
```

-   `<Algorithm>` must match the benchmark name (e.g., Fibonacci, Prime, Matrix)

-   `Result` is the computed value or checksum

-   `Time` is the execution time in milliseconds, rounded to 3 decimal places if needed

Example:

```sh
[Fibonacci] Result = 102334155
[Fibonacci] Time = 3.421 ms
```

### Execution Flow

1. Parse CLI arguments (`N`, `--verbose`)
2. Start timer
3. Run algorithm
4. Stop timer
5. Print results in the unified format

This ensures all languages and algorithms have consistent input/output behavior, allowing the runner to parse results automatically.

## Usage

1. Setup

```sh
make setup
```

2. Build

```sh
make build
```

3. Run

```sh
# main python script
./main
```

## License

[MIT](LICENSE)
