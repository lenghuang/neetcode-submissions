# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def myPrint(self, *args):
        if False:
            print(*args)

    def parseNodeList(self, node_list):
        res = ""
        for node in node_list:
            res += str(node.val) + ","
        return res

    def findNode(self, curr, target, acc):
        if not curr:
            self.myPrint("curr is null")
            return None

        self.myPrint("find node, looking at", curr.val)

        new_acc = acc + [curr]

        if curr.val == target.val:
            return new_acc
        
        left = self.findNode(curr.left, target, new_acc)
        if left:
            return left

        right = self.findNode(curr.right, target, new_acc)
        if right:
            return right

        return None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        p_path = self.findNode(root, p, [])
        q_path = self.findNode(root, q, [])

        self.myPrint("p path", self.parseNodeList(p_path))
        self.myPrint("q path", self.parseNodeList(q_path))

        if len(p_path) == 0 or len(q_path) == 0:
            return TreeNode()
        
        i = 0
        while i < len(p_path) \
            and i < len(q_path) \
            and p_path[i] == q_path[i]:
            i += 1

        i = max(i - 1, 0)

        self.myPrint("set i to", i)

        return p_path[i]

        

        
'''

consider 3 and 4

start at 5

[5]

go left

[5,3,8]
found one!

its 3

so if q is descendant of p, LCA is p

else, there exists some common ancesotr

given p, q, comm ancestor if

I can traverse up and eventually they meet

whats time if i find both nodes, then work my way up?

O(h) find one O(h) find two, O(h) backtrack

probably a more efficient way to "backtrack"

p = 2, q = 4

whats the traversal path to find p?

5 --> 3 -> 1 -> 2
5 -> 3 -> 4

traverse those lists and see what is the lowest common, it's 3!


'''