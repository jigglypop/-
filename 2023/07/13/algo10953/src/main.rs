use std::io::stdin;

fn input() -> String {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    buf
}

fn split() -> Vec<i32> {
    let input = input();
    let v : Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse::<i32>().unwrap()).collect();
    v
}


fn split_comma() -> Vec<i32> {
    let input = input();
    let v: Vec<i32> = input
        .split(',')
        .map(|s| String::from(s).trim().parse::<i32>().unwrap())
        .collect();
    v
}

fn main() {
    let input = split();
    let n = input[0];
    for _ in 0..n {
        let input = split_comma();
        println!("{}", input[0] + input[1]);
    }
}
