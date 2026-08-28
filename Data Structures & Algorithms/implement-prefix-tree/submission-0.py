'''
tree of hashmaps

    [ "a" : yes, "b" : yes ]
     /                 \
[ "t" : "yes" ]        [ "a" : "yes" ]
                            /    \
                [ "l" : "yes" ]    [ "t" : "yes" ]


key is the letter
value is a pointer to the list

each node has:
- a dictionary of [letter, node]
- stop = flag (is it the end of the word?)

node operations:
- ? 

for insert, i need to iterate through the tree?

look at node:
- does letter exist alr? if so go there
- else, create new letter there

once at end of the word, mark as is end of the word

search:
- look at node, does it exist? return false
- else, go there
- check, if is last word

so far it seems like i need a "TryGetNextNode" and a "Set/GetIsLastWord"

startsWith is just search without the last word check
''' 

class Node:
    def __init__(self):
        self.mapping = {}
        self.is_stop = False

    def tryGetNextNode(self, letter: str):
        if letter in self.mapping:
            return self.mapping[letter]
        return None

    def addOrGetNextNode(self, letter: str):
        node = self.tryGetNextNode(letter)
        if node:
            return node
        
        node = Node()
        self.mapping[letter] = node
        return node

    def isStop(self) -> bool:
        return self.is_stop

    def setIsStop(self) -> None:
        self.is_stop = True

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        '''
        for each letter in the word, try to get the next letter
        until you can't
        once you can't, start adding it
        '''
        node = self.root
        for c in word:
            # print('attempting to insert', c)
            node = node.addOrGetNextNode(c)
            # print("got node", node)
        # mark that its stop
        node.setIsStop()

    def search(self, word: str) -> bool:
        '''
        for each letter in the wod, try to get the next letter
        until you can't
        if you can check if it's last word
        '''
        node = self.root
        for c in word:
            node = node.tryGetNextNode(c)
            if node:
                continue
            return False
        
        return node.isStop()

    def startsWith(self, prefix: str) -> bool:
        '''
        same as search but don't check node is stop
        '''
        node = self.root
        for c in prefix:
            node = node.tryGetNextNode(c)
            if node:
                continue
            return False
        
        return True
        
        