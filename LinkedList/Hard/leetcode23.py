class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        newNode = ListNode(data)
        if not self.head:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode


class solution:
    def mergeKlists(self, lists: LinkedList):
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None

                mergedList.append(self.kMergeList(list1, list2))
            lists = mergedList
        return lists[0]

    def kMergeList(self, lst1, lst2):
        dummy = ListNode(0)
        tail = dummy
        while lst1 and lst2:
            if lst1.val < lst2.val:
                tail.next = lst1
                lst1 = lst1.next
            else:
                tail.next = lst2
                lst2 = lst2.next
            tail = tail.next
        if lst1:
            tail.next = lst1
        if lst2:
            tail.next = lst2
        return dummy.next


l1 = LinkedList()
l1.add(1)
l1.add(2)
l1.add(3)
l1.add(4)
l1.add(5)


l2 = LinkedList()
l2.add(5)
l2.add(3)
l2.add(1)
l2.add(5)


x = solution()
print(x.mergeKlists([l1.head, l2.head]))
