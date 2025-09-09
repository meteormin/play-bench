#!/usr/bin/env bash
set -euo pipefail

# 항상 프로젝트 루트 기준에서 실행되도록 고정
cd "$(dirname "$0")/.."

# bin 디렉토리 보장
mkdir -p bin

# ===== 빌드 타겟 정의 =====
TARGETS=("fib" "prime")

# ===== C 빌드 =====
echo "Building C"
for target in "${TARGETS[@]}"; do
    src="benchmarks/c/$target.c"
    if [[ -f "$src" ]]; then
        echo "* $target"
        gcc "$src" \
            -I"$(brew --prefix gmp)/include" \
            -L"$(brew --prefix gmp)/lib" \
            -lgmp \
            -o benchmarks/c/$target
    else
        echo "* (skip: $src not found)"
    fi
done

# ===== Rust 빌드 =====
echo "Building Rust (Cargo)"
(
    cd benchmarks/rust
    cargo build --release
)

# ===== Java 빌드 =====
echo "Building Java"
for target in "${TARGETS[@]}"; do
    class_name="$(tr '[:lower:]' '[:upper:]' <<< ${target:0:1})${target:1}"
    src="benchmarks/java/$class_name.java"
    if [[ -f "$src" ]]; then
        echo "* $target"
        javac "$src" -d benchmarks/java
    else
        echo "* (skip: $src not found)"
    fi
done

# ===== Go 빌드 =====
echo "Building Go"
for target in "${TARGETS[@]}"; do
    src="benchmarks/go/$target/main.go"
    if [[ -f "$src" ]]; then
        echo "* $target"
        go build -o benchmarks/go/build/$target "$src"
    else
        echo "* (skip: $src not found)"
    fi
done

# ===== Runner 빌드 =====
echo "Building runner"
if [[ -f "runner/main.go" ]]; then
    go build -o bin/runner runner/main.go
else
    echo "* (skip: runner/main.go not found)"
fi

echo "All builds completed successfully!"
