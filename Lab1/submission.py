## import modules here 

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    '''Use Newton's method
    '''
    i, j = x, (x+1)//2
    while j < i:
        i = j
        j = (i + x//i)//2
    return i


################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    if not MAX_ITER:
        return x_0
    x_new = x_0 - f(x_0)/fprime(x_0)
    return x_new if abs(x_new-x_0)<EPSILON else find_root(f, fprime, x_new, EPSILON, MAX_ITER-1)


################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def make_tree(tokens): # do not change the heading of the function
    stack = []
    for token in tokens:
        token = Tree(token) if token != '[' and token != ']' else token
        if token != ']':
            stack.append(token)
        else:
            children = []
            while stack[-1] != '[':
                children.append(stack.pop())
            stack.pop() # ged rid of '['
            parent = stack.pop()
            while children:
                child = children.pop()
                parent.add_child(child)
            stack.append(parent)
    return stack[0]  

def max_depth(root): # do not change the heading of the function
    if root is None:
        return 0
    elif not root.children:
        return 1
    depth = 2
    nodes, next_nodes = root.children, []
    while any([node.children for node in nodes]):
        depth += 1
        for node in nodes:
            next_nodes.extend(node.children)
        nodes, next_nodes = next_nodes, []
    return depth