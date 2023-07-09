#![allow(unused)]
#![allow(non_snake_case)]
use std::fs::File;
use std::io::{self, BufReader, stdin};

fn read_line(str: &mut String) {
    str.clear();
    stdin().read_line(str).unwrap();
}

fn main() {
    let stdin = || {BufReader::new(File::open("./input.text").unwrap())};
    // stdin 출력
    println!("{:?}", stdin());

    let mut str = String::new();
    read_line(&mut str);
    read_line(&mut str);
    
    let prime_nums = str
        .split_whitespace()
        .map(|s| s.parse::<i32>().unwrap())
        .filter(|&n| is_prime(n));

    println!("{}", prime_nums.count());
}

fn is_prime(num: i32) -> bool {
    if num == 1 { return false; }
    if num == 2 { return true; }
    for n in 2..=(num as f64).sqrt() as i32 {
        if num % n == 0 {
            return false;
        }
    }
    true
}
