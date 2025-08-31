import sys, time

# 무제한 허용
sys.set_int_max_str_digits(0)


def fib(n, verbose=False):
    a, b = 0, 1
    for i in range(n):
        if verbose:
            print(f"Step {i}: {a}")
        a, b = b, a + b
    return a


def main():
    if len(sys.argv) < 2:
        print("Usage: python fib.py <N> [--verbose]")
        return

    n = int(sys.argv[1])
    verbose = len(sys.argv) > 2 and sys.argv[2] == "--verbose"

    start = time.time()
    result = fib(n, verbose)
    elapsed = (time.time() - start) * 1000

    print(f"[Fibonacci] Result = {result}")
    print(f"[Fibonacci] Time   = {elapsed:.3f} ms")


if __name__ == "__main__":
    main()
