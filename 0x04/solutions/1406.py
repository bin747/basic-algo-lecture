import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.before = None
        self.next = None


def add(node, data):
    insert_node = Node(data)
    if node.next:
        node.next.before = insert_node
        insert_node.next = node.next

    node.next = insert_node
    insert_node.before = node


def remove(node):
    if node.before:
        node.before.next = node.next
        node.next.before = node.before
    else:
        node.next.before = None


N = list(sys.stdin.readline().strip())
M = int(input())

head = Node(None)
result = head
for i in range(len(N)):
    nextNode = Node(N[i])
    head.next = nextNode
    nextNode.before = head
    head = head.next

for _ in range(M):
    d = list(sys.stdin.readline().strip().split())
    if d[0] == 'P':
        add(head, d[1])
        head = head.next
    if d[0] == 'L':
        if head.before:
            head = head.before
    if d[0] == 'D':
        if head.next:
            head = head.next
    if d[0] == 'B':
        if head.before:
            if head.next:
                head.next.before = head.before
            head.before.next = head.next
            head = head.before

while result.next:
    print(result.next.data, end='')
    result = result.next
