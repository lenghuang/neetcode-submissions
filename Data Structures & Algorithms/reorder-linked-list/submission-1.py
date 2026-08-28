# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def parseList(self, head):
        res = []
        curr = head
        while curr != None:
            res.append(curr.val)
            curr = curr.next
        return str(res)

    def getMiddleNode(self, head: Optional[ListNode]):
        print("===getMiddleNode===")
        lo = head
        hi = head
        prev = None

        while hi != None and hi.next != None:
            print("lo", lo.val, "hi", hi.val)
            if lo != None:
                prev = lo
            lo = lo.next
            hi = hi.next.next
            
            
        print("middle is", lo.val)

        if prev != None:
            print('disconnect middle')
            print("prev is", prev.val)
            prev.next = None

        print("===getMiddleNode===\n")
        return lo

    def reverseListInPlace(self, node: Optional[ListNode]) -> Optional[ListNode]:
        print("===reverseInPlace===")
        print("before", self.parseList(node))
        prev = None
        curr = node
        while curr != None:
            # a -> b -> c
            # <- a <- b
            # print("before")
            # print("curr:", curr.val, "curr next", curr.next.val if curr.next != None else '')
            # print("prev:", prev.val if prev != None else "")
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            # print("after")
            # print("curr:", curr.val if curr else "", "curr next", curr.next.val if curr != None and curr.next != None else '')
            # print("prev:", prev.val if prev != None else "")
        
        print("after", self.parseList(prev))
        print("===reverseInPlace===\n")
        return prev

    def mergeTwoLists(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        
        print("===mergeTwoLists===")

        print("before", self.parseList(left), "+", self.parseList(right))
        l = left
        r = right
        curr = left
        while l != None and r != None:
            # l -> templ ->
            # r -> tempr ->
            # we want
            # l -> r -> templ
            # then increment l = templ
            # then increment r = tempr
            print("(l,r)", l.val, r.val)
            prev_l = l
            prev_r = r
            templ = l.next
            tempr = r.next
            l.next = r
            r.next = templ
            l = templ 
            r = tempr 

        print("prev_l", prev_l.val if prev_l else "is none")
        print("prev_r", prev_r.val if prev_r else "is none")
        print("l", l.val if l else "is none")
        print("r", r.val if r else "is none")

        if r != None:
            # implicitly, l must be none
            prev_r.next = r
        if l != None:
            # implicity r must be none
            prev_l.next = l

        print("after", self.parseList(left))
        print("===mergeTwoLists===\n")
        return left

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if head is None:
            return head
        
        middle = self.getMiddleNode(head)

        revtail = self.reverseListInPlace(middle)

        merged = self.mergeTwoLists(head, revtail)


'''

Get the middle of the list

1,2,3,4,5,6
^   ^
1,2,3,4,5,6
  ^     ^
1,2,3,4,5,6
    ^       ^

3rd element is middle therefore even

1,2,3,4,5
^   ^
1,2,3,4,5
  ^     ^
1,2,3,4,5
    ^       ^

3rd element is middle?

i can just get the last one and do the math 

so now i have access to the head, middle, tail

1,2,3,4,5,6,7,8,9,10
^       ^         ^

the middle is now the end...., so what if i move 5 after 10?

1,2,3,4,10,5,6,7,8,9,
^       ^         ^

confused

i should be able to accomplish this moving only 
two things at a time and only with knowledge of next

[0,1,2,3,4]
[0,4,1,3,2]

[0,1,2]
put end at middle and middle at end

but this fails for bigger ones

1,2,3,4,5,6,7,8,9,10
^       ^         ^

unless i swap?

1,2,3,4,5,6,7,8,9,10
^       ^         ^

x = 1 (next, 2)
y = 5 (next, 6)
z = 10 (next, None)

get it so that

x = 1 (next, 10)
y = 6 (next, 7)
z = ?


what if i 

find middle

reverse everything after middle

then merge

1->2->3->4->5->6->7
1->2->3->4<-5<-6<-7

head.next = tail, and so and so forth 

that feels like the right thing to do and in place

'''
        