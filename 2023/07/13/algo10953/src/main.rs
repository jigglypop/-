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


fn split_comma() -> Vec<&'static str> {
    let input = input();
    let v: Vec<&str>  = input
        .split(',').collect();
    v
}


fn main() {
    let input = split();
    let n = input[0];
    println!("{}", n);
    for _ in 0..n {
        let input = split_comma();
        println!("{} {}", input[0], input[1]);
    }
}
