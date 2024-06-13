class BSTNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val == None:
            self.val = val
        
        if self.val == val:
            return
        
        if val < self.val:
            if self.left:
                self.left.insert(val)
            self.left = BSTNode(val)

        if val > self.val:
            if self.right:
                self.right.insert(val)
            self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val
    
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    
    def delete(self, val):
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val) 

        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)

        else: 
            if self.left is None: 
                return self.right
            elif self.right is None: 
                return self.left
            else: 
                successor = self.right.get_min()  
                self.val = successor  
                self.right = self.right.delete(successor)  

        return self
    
    def reverse(self):
        self.left, self.right = self.right, self.left
        if self.left:
            self.left.reverse()
        if self.right:
            self.right.reverse()

    def preorder(self, visited):
        visited.append(self.val)
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)
    
    def postorder(self, visited):
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postoder(visited)
        visited.append(self.val)

    def inorder(self, visited):
        if self.left:
            self.left.inorder(visited)
        visited.append(self.val)
        if self.right:
            self.right.inorder(visited)

    def exists(self, val):
        if self.val == val:
            return True
        if self.left and self.left.exists(val):
            return True
        if self.right and self.right.exists(val):
            return True
        return False

    def height(self):
        left_height, right_height = 0, 0
        if self.val is None:
            return 0
        if self.left:
            left_height = self.left.height()
        if self.right:
            right_height = self.right.height()
        return max(left_height, right_height) + 1        