use std::collections::HashSet;
use std::fs::File;
use std::io::{BufReader, Read, stdin};

fn main()  {
    let file = File::open("./input.txt").unwrap();
    let stdin = || BufReader::new(file);
    let mut str = String::new();
    stdin().read_to_string(&mut str);
    let mut buf = str.split_ascii_whitespace();

    let n: usize = buf.next().unwrap().parse().unwrap();
    let m: usize = buf.next().unwrap().parse().unwrap();

    let a: HashSet<&str> = buf.by_ref().take(n).collect();
    let mut b: Vec<_> = buf.into_iter().filter(|x| a.contains(x)).collect();
    b.sort_unstable();
    println!("{}", b.len());
    for i in b {
        println!("{}", i);
    }
}