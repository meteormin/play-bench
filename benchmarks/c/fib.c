#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <gmp.h>
#include <time.h>

void fib(int n, int verbose, mpz_t result)
{
    mpz_t a, b, tmp;
    mpz_inits(a, b, tmp, NULL);
    mpz_set_ui(a, 0);
    mpz_set_ui(b, 1);

    for (int i = 0; i < n; i++)
    {
        if (verbose)
        {
            gmp_printf("Step %d: %Zd\n", i, a);
        }
        mpz_set(tmp, a);
        mpz_set(a, b);
        mpz_add(b, tmp, b);
    }
    mpz_set(result, a);
    mpz_clears(a, b, tmp, NULL);
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: fib <N> [--verbose]\n");
        return 1;
    }

    int n = atoi(argv[1]);
    int verbose = (argc > 2 && strcmp(argv[2], "--verbose") == 0);

    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);

    mpz_t result;
    mpz_init(result);
    fib(n, verbose, result);

    clock_gettime(CLOCK_MONOTONIC, &end);
    double elapsed = (end.tv_sec - start.tv_sec) * 1000.0 + (end.tv_nsec - start.tv_nsec) / 1e6;

    gmp_printf("[Fibonacci] Result = %Zd\n", result);
    printf("[Fibonacci] Time   = %.3f ms\n", elapsed);

    mpz_clear(result);
    return 0;
}
