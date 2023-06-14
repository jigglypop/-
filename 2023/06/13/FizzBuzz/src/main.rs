fn main() {
    // for i in 1..101 {
    //     if i % 3 == 0 && i % 5 == 0 {
    //         println!("FizzBizz");
    //     } else if i % 3 == 0 {
    //         println!("Fizz");
    //     } else if i % 5 == 0 {
    //         println!("Bizz");
    //     } else {
    //         println!("{}", i);
    //     }
    // }
    // 
    // for i in 1..9 {
    //     for j  in 1..9 {
    //         print!("{:3},", i * j);
    //     }
    //     println!();
    // }
    for i in 1..9 {
        let s = (1..10)
            .map(|j| format!("{:3}", i * j))
            .collect::<Vec<String>>().join(",");
        println!{"{}", s};
    }
}
