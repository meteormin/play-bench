function fib(n, verbose) {
    let a = 0n,
        b = 1n;
    for (let i = 0; i < n; i++) {
        if (verbose) console.log(`Step ${i}: ${a}`);
        [a, b] = [b, a + b];
    }
    return a;
}

function main() {
    const args = process.argv.slice(2);
    if (args.length < 1) {
        console.log("Usage: node fib.js <N> [--verbose]");
        return;
    }
    const n = parseInt(args[0]);
    const verbose = args.length > 1 && args[1] === "--verbose";

    const start = process.hrtime.bigint();
    const result = fib(n, verbose);
    const elapsed = Number(process.hrtime.bigint() - start) / 1e6;

    console.log(`[Fibonacci] Result = ${result.toString()}`);
    console.log(`[Fibonacci] Time   = ${elapsed.toFixed(3)} ms`);
}

main();
