use std::io;
use std::collections::VecDeque;

static di: [[i32; 2]; 4] = [
  [0, 1], [1, 0], [0, -1], [-1, 0]
];


fn main() {
    let mut n = 5;
    for i in 0..n {
        println!("{}", i);
    }
}
