import sys
sys.setrecursionlimit(10**6)


class Tree:
    def __init__(self, dataList):
        self.data = max(dataList, key=lambda x: x[1])
        leftList = list(filter(lambda x: x[0] < self.data[0], dataList))
        rightList = list(filter(lambda x: x[0] > self.data[0], dataList))
        if leftList:
            self.left = Tree(leftList)
        else:
            self.left = None
        if rightList:
            self.right = Tree(rightList)
        else:
            self.right = None


def post_pre(root):
    post = []
    pre = []

    def fix(node, post, pre):
        post.append(node.data[2])
        if node.left:
            fix(node.left, post, pre)
        if node.right:
            fix(node.right, post, pre)
        pre.append(node.data[2])
    fix(root, post, pre)
    return [post, pre]


def solution(nodeinfo):
    answer = []
    nodeinfo_index = [nodeinfo[i] + [i+1] for i in range(len(nodeinfo))]
    root = Tree(nodeinfo_index)
    answer = post_pre(root)
    return answer


print(solution([[5, 3], [11, 5], [13, 3], [3, 5],
                [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
