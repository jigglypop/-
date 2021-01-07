class Node {
  constructor(value, left, right) {
    this.value = value;
    this.left = left;
    this.right = right;
  }
}

const preorder = (x) => {
  if (x === -19) return;
  process.stdout.write(makeString(x))
  preorder(tree[x].left);
  preorder(tree[x].right);
};

const inorder = (x) => {
  if (x === -19) return;
  inorder(tree[x].left);
  process.stdout.write(makeString(x))
  inorder(tree[x].right);
};

const postorder = (x) => {
  if (x === -19) return;
  postorder(tree[x].left);
  postorder(tree[x].right);
  process.stdout.write(makeString(x))
};

var fs = require("fs");
// var input = fs.readFileSync('dev/stdin').toString().split('\n');
var input = fs.readFileSync("./1991.txt").toString().split("\r\n");

const makeNumber = (x)=>{
  return x.charCodeAt(0) - 65
}
const makeString = (x)=>{
  return String.fromCharCode(x + 65)
}
const N = parseInt(input[0]);
input.shift();
const tree = new Array(26);
for (let i = 0 ; i < N; i++) {
  const [A, B, C] = input[i].split(" ").map(x => makeNumber(x));
  tree[A] = new Node(A, B, C);
}

preorder(0);
process.stdout.write('\n')
inorder(0);
process.stdout.write('\n')
postorder(0);
process.stdout.write('\n')
