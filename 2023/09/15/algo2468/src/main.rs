use std::{fs::File, io::{BufReader, Read, stdin}, collections::VecDeque};

fn next_parse<T: std::str::FromStr>(it: &mut std::str::SplitAsciiWhitespace) -> T {
    it.next().unwrap().parse().ok().unwrap()
}

fn bfs(board: &Vec<Vec<usize>>, visited: &mut Vec<Vec<bool>>, y: usize, x: usize, n: usize, i: usize) {
    let mut Q = VecDeque::<(usize, usize)>::new();
    let di = [(0, 1), (0, -1), (1, 0), (-1, 0)];
    Q.push_back((y, x));
    visited[y][x] = true;
    while !Q.is_empty() {
        let (y, x) = Q.pop_front().unwrap();
        for (dy, dx) in di.iter() {
            let ny = y as i32 + dy;
            let nx = x as i32 + dx;
            if ny < 0 || nx < 0 || ny >= n as i32 || nx >= n as i32 {
                continue;
            }
            let ny = ny as usize;
            let nx = nx as usize;
            if !visited[ny][nx] && board[ny][nx] > i {
                visited[ny][nx] = true;
                Q.push_back((ny, nx));
            }
        }
    }
}

fn main() {
    let file = File::open("./input.txt").unwrap();
    let stdin = || BufReader::new(file);
    let mut str = String::new();
    stdin().read_to_string(&mut str).unwrap();
    let mut buf = str.split_ascii_whitespace();
    
    let n = next_parse::<usize>(&mut buf);
    let mut board = vec![vec![0; n]; n];
    let mut max = 0;
    for y in 0..n {
        for x in 0..n {
            let temp = next_parse::<usize>(&mut buf);
            if temp > max {
                max = temp;
            }
            board[y][x] = temp
        }
    }

    let mut result = 0;
    for i in 0..max {
        let mut _board = board.clone();
        let mut visited = vec![vec![false; n]; n];
        let mut temp_count = 0;
        for y in 0..n {
            for x in 0..n {
                if board[y][x] > i && !visited[y][x]{
                    temp_count += 1;
                    bfs(&_board, &mut visited, y, x, n, i)
                }
            }
        }
        if temp_count > result {
            result = temp_count;
        }
    }
    println!("{}", result);
}
