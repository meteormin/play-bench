<?php
function fib($n, $verbose) {
    $a = gmp_init(0);
    $b = gmp_init(1);
    for ($i = 0; $i < $n; $i++) {
        if ($verbose) {
            echo "Step $i: " . gmp_strval($a) . PHP_EOL;
        }
        $tmp = $a;
        $a = $b;
        $b = gmp_add($tmp, $b);
    }
    return $a;
}

function main($argv) {
    if (count($argv) < 2) {
        echo "Usage: php fib.php <N> [--verbose]\n";
        return;
    }

    $n = intval($argv[1]);
    $verbose = count($argv) > 2 && $argv[2] === "--verbose";

    $start = microtime(true);
    $result = fib($n, $verbose);
    $elapsed = (microtime(true) - $start) * 1000;

    echo "[Fibonacci] Result = " . gmp_strval($result) . "\n";
    printf("[Fibonacci] Time   = %.3f ms\n", $elapsed);
}

main($argv);
?>
