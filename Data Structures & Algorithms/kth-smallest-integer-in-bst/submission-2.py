# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''

k'th smallest integer

so for example 1, the 1st smallest integer is 1
the 2nd smallest integer would be 2
and 3rd smallest is 3

so i guess in a way, if we had this as a list, we want index k - 1?

[1,2,3] is the ordered list that the tree [2,1,3] represents
k=1 --> index 0 = 1

[2,3,4,5] is similar. k=4 --> index 3 == 5

so a really silly solution would be to recurse the tree, create the list, and get the k-1'th object

how does this traversal work

i start at 4 --> [4]
- go left to 3, --> [3,4] (appendLeft?)
- go left to 2, --> [2,3,4]
- reached leaf, other side, go right appendRight? 

breaks down a bit if i had like
    5
  3   6
2   4

i start at [5]
go left, [3,5]
go left, [2,3,5]

i guess maybe if i reiplmeneted the bst as a dll?

i guess -- the question really is do i know how to do an in-order traversal of a binary tree?

inorder(x) = x
inorder(l,x,r) = inorder(l) + x + inorder(r)
'''

class Solution:

    def __init__(self):
        self.visited = 0 # Counter for visited nodes

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # traversed = []

        # define an inorder traversal that adds values to a list as it goes
        def inorder(node):
            if node is None:
                return None
            
            left = inorder(node.left)
            if left:
                return left
            
            self.visited += 1
            if (self.visited == k):
                return node.val
            
            right = inorder(node.right)
            if right:
                return right
            
            return None
            
        return inorder(root)    