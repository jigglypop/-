const isPrime = (number) => {
    if (number < 2) return false;
    if (number === 2) return true;
    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) return false;
    }
    return true;
};
console.log(isPrime(10));
console.log(isPrime(2));
console.log(isPrime(1));
console.log(isPrime(5));
