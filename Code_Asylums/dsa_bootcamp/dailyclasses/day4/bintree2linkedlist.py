class tree:
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None

    def inorder(self):
        if self.left!=None: 
            self.left.inorder()
        print(self.value)
        if self.right!=None:
            self.right.inorder()

    def insert(self, val):
        if self.left==None and self.value>val:
            self.left=tree(val)
        elif self.value>val:
            self.left.insert(val)
        elif self.right==None and self.value<=val:
            self.right=tree(val)
        else:
            self.right.insert(val)

    def lowestCommonAncestor(self, x, y):
        node=self.helper(self, x, y)
        if type(node)!=int:
            return node.value
        else:
            return "Either one or neither nodes exist"

    def helper(self, node, x, y):
        sumVal=0
        if x==node.value or y==node.value:
            return 1
        
        s1=s2=0
        if node.left!=None:
            s1=self.helper(node.left, x, y)
        if node.right!=None:
            s2=self.helper(node.right, x, y)

        if type(s1)!=int:
            return s1
        elif type(s2)!=int:
            return s2
        elif s1+s2==2:
            return node
        else:
            return s1+s2

    def levelOrderTraversal(self):
        soln=[]
        parents=[self]
        while parents:
            for i in parents:
                soln.append(i.value)
            children=[]
            for i in parents:
                if i.left!=None:
                    children.append(i.left)
                if i.right!=None:
                    children.append(i.right)
            parents=children.copy()
        return soln

    def verifyBst(self, max=float("-inf"), min=float("inf")):
        if self.value<max or self.value>min:
            print(self.value)
            return False
        s1=s2=True
        if self.left!=None:
            s1=self.left.verifyBst(max, self.value)
        if self.right!=None:
            s2=self.right.verifyBst(self.value, min)
        return s1 and s2

    def bintree2ll(self):
        if self.left==None and self.right==None:
            return
        
        if self.left!=None:
            self.left.bintree2ll()
            temp=self.right
            self.left=None
            thisNode=self.right
            while(thisNode.right!=None):
                thisNode=thisNode.right
            thisNode.right=temp
        self.right.bintree2ll()

    def findDiameter(self):
        self.findMaxPath()
        return 
    
    def findDiameter(self):
        leftMax, rightMax= 0,0
        if tree.left!=None:
            leftMax=self.left.findDiameter()
        if tree.right!=None:
            rightMaxPath= self.right.findDiameter()

        thisHeight=1
        maxChild=max(leftMax, rightMax)
        maxBranch=maxChild+1
        maxPath=max(leftMax+rightMax+1, maxBranch)
        return maxPath



        
t=tree(50)
l=[12, 51, 43, 12, 12]
for i in l:
    t.insert(i)
t.inorder()
while True:
    print("Enter option: ")
    option=int(input())
    if option==1:
        t.bintree2ll()
        t.inorder()
    else:
        break

