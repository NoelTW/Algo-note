class Node:

    def __init__(self):
        self.chidren:dict = dict()
        self.word: bool= False


class PrefixTree:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.chidren:
                curr.chidren[c] = Node()
            curr = curr.chidren[c]
        curr.word = True
        return 


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.chidren:
                return False
            curr = curr.chidren[c]
        return curr.word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.chidren:
                return False
            curr = curr.chidren[c]
        return True
        
        