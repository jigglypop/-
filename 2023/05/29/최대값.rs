use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::str::FromStr;

fn main() -> io::Result<()> {
    let path = Path::new("./input/2566.txt");
    let file = File::open(&path)?;
    let reader = io::BufReader::new(file);

    let mut max = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let mut nums: Vec<i32> = line.split_whitespace()
            .map(|num| i32::from_str(num).unwrap())
            .collect();

        nums.sort();
        max.push(nums[0]);
    }

    println!("{:?}", max);

    Ok(())
}