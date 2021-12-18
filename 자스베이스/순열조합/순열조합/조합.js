const comb = (k, N, start, choice, numbers) => {
    if (k === N) {
        console.log(choice.join(" "));
        return;
    }
    for (let i = start; i < numbers.length; i++) {
        choice.push(numbers[i]);
        comb(k + 1, N, i + 1, choice, numbers);
        choice.pop();
    }
};

comb(0, 2, 0, [], [1, 2, 3]);
