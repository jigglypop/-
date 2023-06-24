#![allow(unused)]
#![allow(non_snake_case)]
use std::{fs::File, io::{BufReader, Read, stdin}};

fn main() {
    let stdin = || {
        BufReader::new(File::open("./input.text").unwrap())
    };

    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();
    let mut split = input.split_ascii_whitespace();
    let mut read = || split.next().unwrap().parse::<i32>().unwrap();
    let [Y,X] = [0;2].map(|_| read() as usize);
    let mut A = vec![vec![0; X]; Y];
    let mut B = vec![vec![0; X]; Y];
    let mut C = vec![vec![0; X]; Y];
    for y in 0..Y {
        for x in 0..X {
            A[y][x] = read();
        }
    }
    for y in 0..Y {
        for x in 0..X {
            B[y][x] = read();
        }
    }
    for y in 0..Y {
        for x in 0..X {
            C[y][x] = A[y][x] + B[y][x];
            print!("{} ", C[y][x]);
        }
        println!();
    }
}