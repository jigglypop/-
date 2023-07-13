use std::{io::stdin, collections::VecDeque};

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


fn bfs(visited: &mut Vec<Vec<bool>>, board: &mut Vec<Vec<i32>>, start: (i32, i32), Y: usize, X: usize) {
    let di = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)];
    let mut Q = VecDeque::<(i32, i32)>::new();
    visited[start.0 as usize][start.1 as usize] = true;
    Q.push_back(start);
    while !Q.is_empty() {
        let (sy, sx) = Q.pop_front().unwrap();
        for i in 0..8 {
            let (dy, dx) = di[i];
            let ny = (sy + dy) as usize;
            let nx = (sx + dx) as usize;
            if 0 <= ny && ny < Y && 0 <= nx && nx < X {
                if board[ny][nx] == 1 && visited[ny][nx] == false {
                    visited[ny][nx] = true;
                    Q.push_back((ny as i32, nx as i32));
                }
            }
        }
    }

}

fn main() {
    loop {
        let input = split();
        let X = input[0] as usize;
        let Y = input[1] as usize;
        if Y == 0 && X == 0 { 
            break; 
        }
        let mut visited = vec![vec![false; X]; Y];
        let mut board: Vec<Vec<i32>> = Vec::new();
        
        for _ in 0..Y {
            let temp = split();
            board.push(temp);
        }

        let mut count = 0;
        for y in 0..Y {
            for x in 0..X {
                if board[y][x] == 1 && visited[y][x] == false {
                    count += 1;
                    bfs(&mut visited, &mut board, (y as i32, x as i32), Y, X);
                }
            }
        }
        println!("{}", count);
    }
}
