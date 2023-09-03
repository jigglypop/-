use std::{io::stdin, collections::VecDeque};

fn input() -> String {
    let mut buf = String::new();
    stdin().read_line(&mut buf).unwrap();
    buf
}

fn split() -> Vec<i32> {
    let buf = input();
    let vec: Vec<i32> = buf
        .split_whitespace()
        .map(|x| x.parse().unwrap()).collect();
    vec
}


fn bfs(di: &[(i32, i32); 4], visited: &mut Vec<Vec<bool>>, board: &mut Vec<Vec<usize>>, start: (usize, usize)) -> usize {
    visited[start.0][start.1] = true;
    let mut q = VecDeque::<(usize, usize)>::new();
    let mut count = 1;
    q.push_back(start);
    while !q.is_empty() {
        let (sy, sx) = q.pop_front().unwrap();
        for (dy, dx) in di.iter() {
            let (y, x) = (sy as i32 + dy, sx as i32 + dx);
            if y < 0 || x < 0 || y >= board.len() as i32 || x >= board.len() as i32 {
                continue;
            } else {
                let (y, x) = (y as usize, x as usize);
                if board[y][x] == 1 && !visited[y][x] {
                    count += 1;
                    visited[y][x] = true;
                    q.push_back((y, x));
                }
            }
        }
    }
    count
}

fn main() {
    let n = split()[0];
    let mut board: Vec<Vec<usize>> = Vec::new();
    let mut visited: Vec<Vec<bool>> = Vec::new();
    let di = [(0, 1), (0, -1), (1, 0), (-1, 0)];

    for _ in 0..n {
        let input = input();
        let v: Vec<usize> = input
            .trim()
            .chars()
            .map(|x| x.to_digit(10).unwrap() as usize)
            .collect();
        board.push(v);
        visited.push(vec![false; n as usize]);
    }
    let mut result:Vec<usize> = Vec::new();

    for y in 0..n {
        for x in 0..n {
            if board[y as usize][x as usize] == 1 && !visited[y as usize][x as usize]{
                result.push(bfs(&di, &mut visited, &mut board,  (y as usize, x as usize)));
            } 
        } 
    }

    result.sort();

    println!("{}",result.len());
    for i in result {
        println!("{}",i);
    }

}
