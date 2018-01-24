
# coding: utf-8

# In[15]:


class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


# In[35]:


def getHeight(node):
    if node is None:
        return 0
    return 1 + max(getHeight(node.left), getHeight(node.right))

def isBalanced(node):
    if node is None:
        return True
    if abs(getHeight(node.left) - getHeight(node.right)) > 1:
        return False
    return isBalanced(node.left) and isBalanced(node.right)


# In[38]:


root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"
 
root.left.left = Tree()
root.left.left.data = "left 2"
root.left.left.left = Tree()
root.left.left.left.data = 'fasdfas'
root.left.right = Tree()
root.left.right.data = "left-right"


# In[39]:


isBalanced(root)

