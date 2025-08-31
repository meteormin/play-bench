import java.math.BigInteger;

public class Fib {
    public static BigInteger fib(int n, boolean verbose) {
        BigInteger a = BigInteger.ZERO;
        BigInteger b = BigInteger.ONE;
        for (int i = 0; i < n; i++) {
            if (verbose) {
                System.out.printf("Step %d: %s%n", i, a.toString());
            }
            BigInteger tmp = a;
            a = b;
            b = tmp.add(b);
        }
        return a;
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java Fib <N> [--verbose]");
            return;
        }
        int n = Integer.parseInt(args[0]);
        boolean verbose = args.length > 1 && args[1].equals("--verbose");

        long start = System.nanoTime();
        BigInteger result = fib(n, verbose);
        long end = System.nanoTime();

        double elapsedMs = (end - start) / 1_000_000.0;
        System.out.printf("[Fibonacci] Result = %s%n", result.toString());
        System.out.printf("[Fibonacci] Time   = %.3f ms%n", elapsedMs);
    }
}
