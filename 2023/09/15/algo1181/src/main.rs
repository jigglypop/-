use std::{fs::File, io::{BufReader, Read, stdin}, collections::{VecDeque, HashMap}, cmp::Ordering};

fn next_parse<T: std::str::FromStr>(it: &mut std::str::SplitAsciiWhitespace) -> T {
    it.next().unwrap().parse().ok().unwrap()
}

fn order(a: &String, b: &String) -> Ordering {
    if a.len() == b.len() {return a.cmp(b);}
    else {return a.len().cmp(&b.len());}
}

fn main() {
    let file = File::open("./input.txt").unwrap();
    let stdin = || BufReader::new(file);
    let mut str = String::new();
    stdin().read_to_string(&mut str).unwrap();
    let mut buf = str.split_ascii_whitespace();
    let N = next_parse::<usize>(&mut buf);
    let mut words = Vec::<String>::new();
    let mut words_map = HashMap::<String, usize>::new();
    for _ in 0..N {
        let word = next_parse::<String>(&mut buf);
        if words_map.contains_key(&word) {
           continue;
        } else {
            words_map.insert(word.clone(), 1);
        }
        words.push(word);
    }
    words.sort_by(order);
    for word in words {
        println!("{}", word);
    }
}
