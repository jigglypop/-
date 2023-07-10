// use std::{io::{stdin}};
// 
// // 리드라인 헬퍼
// fn read_line(s: &mut String) {
//     s.clear();
//     stdin().read_line(s).unwrap();
// }

// fn main() {
//     let mut input = String::new();
//     
//     let mut _y = 0;
//     let mut _x = 0;
//     let mut _n = -1;
// 
//     for y in 0..9 {
//         read_line(&mut input);
//         let temp: Vec<i32> = input
//             .split_whitespace()
//             .map(|s| s.parse::<i32>().unwrap())
//             .collect();
//         for x in 0..9{
//             if _n < temp[x] {
//                 _y = y;
//                 _x = x;
//                 _n = temp[x];
//             }
//         }
//     }
// 
//     println!("{}", _n);
//     println!("{} {}", _y + 1, _x + 1);
// }

use std::io::{self, Read};

fn main() {
    let mut s = String::new();
    io::stdin().lock().read_to_string(&mut s).unwrap();
    let (idx, x) = s
        .split_ascii_whitespace()
        .map(|x| x.parse::<u32>().unwrap())
        .enumerate()
        .max_by_key(|x| x.1)
        .unwrap();
    
    let r = idx / 9 + 1;
    let c = idx % 9 + 1;
    println!("{x}\n{r} {c}");
}

#[link(name = "c")]
extern "C" {}