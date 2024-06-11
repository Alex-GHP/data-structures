class BSTNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if self.val is val:
            return
        
        if val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
    
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current
    
    def delete(self, val):
        if self.val is None:
            return None
        
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        
        if not self.right: 
            return self.left
        if not self.left:   
            return self.right
        
        min_node = self.right.get_min() 
        self.val = min_node.val        
        self.right = self.right.delete(min_node.val) 
        return self
    
    def reverse(self):
        if self:
            self.right, self.left = self.left, self.right
            if self.right:
                self.right.reverse()
            if self.left:
                self.left.reverse()