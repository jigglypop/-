class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    return nodes


deserialize('[1,2,3,null,null,4,null,null,5]')
deserialize(
    '[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')
