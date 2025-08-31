import json
import sys
import os
from dotenv import load_dotenv
from pathlib import Path
from models import ask_to_openai, ask_to_gemini

load_dotenv()

USE_MODEL = os.getenv("MCP_MODEL", "gemini")  # openai | gemini


def load_summary(path: str):
    with open(path, "r") as f:
        return json.load(f)


def generate_base_report(summary: dict) -> str:
    algo = summary["algo"]
    n = summary["n"]
    date = summary["date"]

    results = summary["results"]
    # 성능 정렬
    sorted_res = sorted(results, key=lambda r: r["time_ms"])

    report = []
    report.append(f"# Benchmark Report: {algo.upper()} (N={n})")
    report.append(f"- Date: {date}")
    report.append("")

    # 1. 실행 결과 테이블
    report.append("## Results")
    report.append("| Language | Version | Time (ms) |")
    report.append("|----------|---------|-----------|")
    for r in sorted_res:
        report.append(f"| {r['lang']} | {r['version']} | {r['time_ms']:.3f} |")

    report.append("")

    # 2. 요약 분석
    fastest = sorted_res[0]
    slowest = sorted_res[-1]
    ratio = (
        slowest["time_ms"] / fastest["time_ms"]
        if fastest["time_ms"] > 0
        else float("inf")
    )

    report.append("## Analysis")
    report.append(f"- Fastest: **{fastest['lang']}** ({fastest['time_ms']:.3f} ms)")
    report.append(f"- Slowest: **{slowest['lang']}** ({slowest['time_ms']:.3f} ms)")
    report.append(f"- Slowest/Fastest Ratio: {ratio:.1f}x")
    report.append("")

    return "\n".join(report)


def ask_ai(summary: dict) -> str:
    """AI에게 성능 차이 원인 + 알고리즘 복잡도 분석 요청"""
    prompt = f"""
I have benchmark results for algorithm "{summary['algo']}" with N={summary['n']}:

{json.dumps(summary['results'], indent=2)}

Please write a clear and structured analysis in markdown that includes:

1. **Algorithmic Complexity**
    - What is the time complexity of this algorithm?
    - How does the complexity explain scaling as N increases?

2. **Language Performance Differences**
    - Why are some languages faster/slower?
    - Impact of compiler vs interpreter
    - Impact of BigInt (arbitrary precision integer) vs native int
    - Memory management and runtime overhead considerations

3. **Cross-language Comparison**
    - Any surprising results?
    - Which languages perform similarly and why?

4. **Summary**
    - High-level conclusions about performance trade-offs
    - When to choose each language for computation-heavy tasks
"""

    if USE_MODEL == "openai":
        ask_to_openai(os.getenv("OPENAI_API_KEY"), prompt)

    elif USE_MODEL == "gemini":
        ask_to_gemini(os.getenv("GEMINI_API_KEY", prompt))
    else:
        raise ValueError(f"Unsupported MCP_MODEL={USE_MODEL}")


def generate_full_report(summary: dict, reports_dir: Path) -> Path:
    """Generate markdown report and return output path."""
    base_report = generate_base_report(summary)
    ai_insights = ask_ai(summary)

    final_report = base_report + "\n\n## AI Insights\n" + ai_insights

    out_path = reports_dir / f"{summary['algo']}_report.md"
    with open(out_path, "w") as f:
        f.write(final_report)

    return out_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python report.py <summary.json>")
        sys.exit(1)

    summary_file = Path(sys.argv[1])
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    summary = load_summary(summary_file)
    out_path = generate_full_report(summary, reports_dir)

    print(f"✅ Report written to {out_path}")


if __name__ == "__main__":
    main()
