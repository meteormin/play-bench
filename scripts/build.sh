#!/usr/bin/env bash
set -euo pipefail

# 항상 프로젝트 루트 기준에서 실행되도록 고정
cd "$(dirname "$0")/.."

# bin 디렉토리 보장
mkdir -p bin

echo "Building C"
echo "* fib"
gcc benchmarks/c/fib.c \
    -I$(brew --prefix gmp)/include \
    -L$(brew --prefix gmp)/lib \
    -lgmp \
    -o benchmarks/c/fib

echo "Building Rust (Cargo)"
(
    cd benchmarks/rust
    cargo build --release
)

echo "Building Java"
echo "* fib"
javac benchmarks/java/Fib.java -d benchmarks/java

echo "Building Go (fib)"
echo "* fib"
go build -o benchmarks/go/fib benchmarks/go/fib.go

echo "Building runner"
go build -o bin/runner runner/main.go

echo "All builds completed successfully!"