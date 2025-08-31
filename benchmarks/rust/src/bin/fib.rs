use std::env;
use std::time::Instant;
use num_bigint::BigUint;
use num_traits::{One, Zero};

fn fib(n: usize, verbose: bool) -> BigUint {
    let mut a = BigUint::zero();
    let mut b = BigUint::one();
    for i in 0..n {
        if verbose {
            println!("Step {}: {}", i, a);
        }
        let tmp = a.clone();
        a = b.clone();
        b = tmp + b;
    }
    a
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: fib <N> [--verbose]");
        return;
    }

    let n: usize = args[1].parse().unwrap_or(0);
    let verbose = args.len() > 2 && args[2] == "--verbose";

    let start = Instant::now();
    let result = fib(n, verbose);
    let elapsed = start.elapsed().as_secs_f64() * 1000.0;

    println!("[Fibonacci] Result = {}", result);
    println!("[Fibonacci] Time   = {:.3} ms", elapsed);
}
