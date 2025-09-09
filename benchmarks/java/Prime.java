import java.math.BigInteger;

public class Prime {
    public static BigInteger primeCount(int n, boolean verbose) {
        BigInteger count = BigInteger.ZERO;
        if (n < 2) {
            return count;
        }

        boolean[] isPrime = new boolean[n + 1];
        for (int i = 2; i <= n; i++) {
            isPrime[i] = true;
        }

        for (int p = 2; p * p <= n; p++) {
            if (isPrime[p]) {
                for (int multiple = p * p; multiple <= n; multiple += p) {
                    isPrime[multiple] = false;
                }
            }
        }

        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                count = count.add(BigInteger.ONE);
                if (verbose) {
                    System.out.printf("Prime: %d%n", i);
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java PrimeCount <N> [--verbose]");
            return;
        }
        int n = Integer.parseInt(args[0]);
        boolean verbose = args.length > 1 && args[1].equals("--verbose");

        long start = System.nanoTime();
        BigInteger result = primeCount(n, verbose);
        long end = System.nanoTime();

        double elapsedMs = (end - start) / 1_000_000.0;
        System.out.printf("[PrimeCount] Result = %s%n", result.toString());
        System.out.printf("[PrimeCount] Time   = %.3f ms%n", elapsedMs);
    }
}
