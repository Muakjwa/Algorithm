import sys
input = sys.stdin.readline

class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right
def pre_order(p):
    print(p.root, end='')
    if p.left!=None:
        pre_order(Tree[p.left])
    if p.right!=None:
        pre_order(Tree[p.right])
def in_order(p):
    if p.left!=None:
        in_order(Tree[p.left])
    print(p.root, end='')
    if p.right != None:
        in_order(Tree[p.right])
def post_order(p):
    if p.left != None:
        post_order(Tree[p.left])
    if p.right != None:
        post_order(Tree[p.right])
    print(p.root, end='')
Tree = {}
N = int(input())
for i in range(N):
    a,b,c = input().split()
    if b == '.':
        b=None
    if c == '.':
        c=None
    Tree[a] = Node(a,b,c)
pre_order(Tree['A'])
print()
in_order(Tree['A'])
print()
post_order(Tree['A'])