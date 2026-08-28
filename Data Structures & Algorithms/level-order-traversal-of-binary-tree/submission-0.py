# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
example 1

level 1: 1 -> done
then level 2: 2,3 -> done

looks like a bfs

so for one node: do the thing, then append all children to visited
then for each thing in visited, do the thing

so im on node 1, i add left and right to a list,
now i go through that list, and for each node, add the stuff to next level list
while "queue" is not empty

[(node 1, level 1)]
[(node 2, level 2), (node 3, level 2)]
[(node 3, level 2), (node 4, level 3), (node 5, level 3)]
[...]
'''
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        prev_level = -1
        queue = deque([(root, 0)])
        result = []

        while len(queue) != 0:
            
            # Do the operation
            node, level = queue.popleft()
            # print("got node", node.val, "at level", level)

            if prev_level != level:
                result.append([])
                prev_level = level
                # print("level change detected")
            
            result[prev_level].append(node.val)
            # print('added node to list at index', prev_level)

            # Enqueue the next ones
            if node.left is not None:
                # print('adding left to queue')
                queue.append((node.left, level + 1))
            if node.right is not None:
                # print('adding right to queue')
                queue.append((node.right, level + 1))
            
        return result

        
        