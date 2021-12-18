const perm = (k, N, used, choice, numbers) => {
    if (k === N) {
        console.log(choice.join(" "));
        return;
    }
    for (let i = 0; i < numbers.length; i++) {
        if (used & (1 << i)) continue;
        choice.push(numbers[i]);
        perm(k + 1, N, used | (1 << i), choice, numbers);
        choice.pop();
    }
};

perm(0, 2, 0, [], [1, 2, 3]);
