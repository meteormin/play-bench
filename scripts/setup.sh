#!/usr/bin/env bash
set -e  # 에러 발생 시 즉시 종료

# 항상 프로젝트 루트 기준에서 실행되도록 고정
cd "$(dirname "$0")/.."

# 가상환경 경로
VENV_DIR=".venv"

if [ ! -d "$VENV_DIR" ]; then
    echo "⚡ No venv: setup venv and install package"
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    pip install --upgrade pip
    pip install -r ./mcp/requirements.txt
fi

echo "run: source $VENV_DIR/bin/activate"