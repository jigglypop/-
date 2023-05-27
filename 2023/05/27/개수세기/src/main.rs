use std::io::Read;
// fn main() {
//   let mut file = std::fs::File::create("input.txt").unwrap();
//   file.write_all("Hello World".as_bytes()).unwrap();
//   file.write_all("\nTutorialsPoint".as_bytes()).unwrap();
//   println!("data written to file" );
// }

// 파일 읽기

fn main() {
  let mut file = std::fs::File::open("input.txt").unwrap();
  let mut content = String::new();
  file.read_to_string(&mut content).unwrap();
  println!("{}", content);
}