function solution(n) {
    // 1일때 조심
    let primes = Array(n + 1).fill(false);
    primes[1] = true;
    for (let i = 2; i <= n; i++) {
        if (primes[i] === false) {
            for (let j = i + i; j <= n; j += i) {
                primes[j] = true;
            }
        }
    }
    for (let i = 2; i <= n; i++) {
        if (primes[i] === false) {
            answer += 1;
        }
    }
    return primes;
}
console.log(solution(10));
