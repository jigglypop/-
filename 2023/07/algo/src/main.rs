#![allow(unused)]
#![allow(non_snake_case)]
use std::{fs::File, io::{BufReader, Read, stdin}};

fn main() {
    let stdin = || {
        BufReader::new(File::open("./input.text").unwrap())
    };
    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();
    println!("{}", input);
}
