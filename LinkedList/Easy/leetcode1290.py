class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.Length = 0

    def add(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.Length += 1


class solution:
    def getDecimalValue(Self, head: Node):
        def getDecimal(x):
            ans, power = 0, 0
            while x:
                ans += (x % 10) * (2 * power)
                power += 1
                x //= 10
            return ans
        curr = head
        res = 0
        while curr:
            res = res * 10 + curr.val
            curr = curr.next
        return getDecimal(res)


Lnode = LinkedList()
Lnode.add(1)
Lnode.add(0)
Lnode.add(1)

x = solution()
print(x.getDecimalValue(Lnode.head))
