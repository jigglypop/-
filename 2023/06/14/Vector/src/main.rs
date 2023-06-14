use std::io::*;
// use std::fs::File;

fn main() {
    // let stdin = || {BufReader::new(File::open("./10813.txt").unwrap())};

    let mut input = String::new();
    stdin().read_to_string(&mut input).unwrap();
    let value: i32 = input.split_ascii_whitespace().map(|s| s.parse::<i32>().unwrap()).sum();
    println!("{}", value);
}
