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

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        
        def find_node(node):
            if not node:
                return None, None
            
            self.myPrint("looking at", node.val)

            curr_p = node.val == p.val
            curr_q = node.val == q.val

            left_p, left_q = find_node(node.left)
            right_p, right_q = find_node(node.right)

            self.myPrint("curr_p, curr_q", curr_p, curr_q)
            self.myPrint("looking at", left_p, left_q, right_p, right_q)

            if curr_p:
                self.myPrint('curr_p')
                return node, node
            if curr_q:
                self.myPrint('curr_q')
                return node, node
            if left_p and right_q:
                self.myPrint('left_p and right_q')
                return node, node 
            if right_p and left_q:
                self.myPrint('right_p and left_q')
                return node, node
            if left_p and left_q:
                self.myPrint("left_p and left_q:")
                return left_p, left_q
            if right_p and right_q:
                self.myPrint("right_p and right_q")
                return right_p, right_q

            return None, None
        
        p_node, q_node = find_node(root)
        
        self.myPrint("p_node", p_node.val if p_node else p_node)
        self.myPrint("q_node", q_node.val if q_node else q_node)

        return p_node

                

        
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

can we keep track of the parent in some way?

5, parent is null, try left
3, parent is 5
- try left is 1, parent is 3, 
  try right is 2, parent is 1
- try right is 4, parent is 3, leaf.
both of these are true, at node 3. this is my LCA


let my recursion be

isAncestor(node, p, q)

we want the lowest one. return order should work, but if not, try using heights to differentiate
'''