class HuffmanTree:

    def __init__(self, weight, char=None, left=None, right=None):
        self.wt = weight
        self.char = char
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"\"symbol\" : {self.char}, \"frequency\" : {self.wt}"
    
    def weight(self):
        return int(self.wt)

    def symbol(self):
        return self.char
    
    def is_leaf(self):
        return self.left is None and self.right is None
        
    def __lt__(self, other):
        return self.wt < other.wt
    
    def print_all_nodes(self):
        print(self.char, self.wt, self.is_leaf())

        if self.left != None:
            self.left.print_all_nodes()
        if self.right != None:
            self.right.print_all_nodes()