use std::{fs::File, io::{BufReader, Read, stdin}, collections::VecDeque};

fn next_parse<T: std::str::FromStr>(it: &mut std::str::SplitAsciiWhitespace) -> T {
    it.next().unwrap().parse().ok().unwrap()
}

fn bfs(board: &Vec<Vec<usize>>, visited: &mut Vec<Vec<bool>>, y: usize, x: usize, Y: usize, X: usize) -> usize {
    let mut Q = VecDeque::<(usize, usize)>::new();
    let di = [(0, 1), (0, -1), (1, 0), (-1, 0)];
    Q.push_back((y, x));
    visited[y][x] = true;
    let mut count = 1;
    while !Q.is_empty() {
        let (y, x) = Q.pop_front().unwrap();
        for (dy, dx) in di.iter() {
            let ny = y as i32 + dy;
            let nx = x as i32 + dx;
            if ny < 0 || ny >= Y as i32 || nx < 0 || nx >= X as i32 {
                continue;
            }
            let ny = ny as usize;
            let nx = nx as usize;
            if board[ny][nx] == 1 && !visited[ny][nx] {
                visited[ny][nx] = true;
                count += 1;
                Q.push_back((ny, nx));
            }
        }
    }
    return count;
}


fn main() {
    let file = File::open("./input.txt").unwrap();
    let stdin = || BufReader::new(file);
    let mut str = String::new();
    stdin().read_to_string(&mut str).unwrap();
    let mut buf = str.split_ascii_whitespace();
    
    let Y: usize = next_parse(&mut buf);
    let X: usize = next_parse(&mut buf);
    let k: usize = next_parse(&mut buf);
    let mut board = vec![vec![1; X]; Y];
    for _ in 0..k {
        let x1: usize = next_parse(&mut buf);
        let y1: usize = next_parse(&mut buf);
        let x2: usize = next_parse(&mut buf);
        let y2: usize = next_parse(&mut buf);
        for y in y1..y2 {
            for x in x1..x2 {
                board[y][x] = 0;
            }
        }
    }

    let mut visited = vec![vec![false; X]; Y];
    let mut result = Vec::<usize>::new();
    for y in 0..Y {
        for x in 0..X {
            if board[y][x] == 1 && !visited[y][x] {
               result.push( bfs(&board, &mut visited, y, x, Y, X));
            }
        }
    }
    result.sort();
    println!("{}", result.len());
    for i in result {
        print!("{} ", i);
    }
}
