

class DoublyListNode:
    def __init__(self, data=0, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next



def merge_double_link_list(L1, L2):
    head = tail = DoublyListNode()
    while L1 and L2:
        if L1.data <= L2.data:
            L1.prev = tail
            tail.next = L1
            tail = L1
            L1 = L1.next
        else:
            L2.prev = tail
            tail.next = L2
            tail = L2
            L2 = L2.next
    tail.next = L1 or L2
    return head.next

if __name__ == "__main__":
    A, B, C, D = DoublyListNode(1), DoublyListNode(8), DoublyListNode(15), DoublyListNode(22)
    A.next, B.prev, B.next, C.prev, C.next, D.prev = B, A, C, B, D, C
    E, F, G, H, I, J = DoublyListNode(2), DoublyListNode(4), DoublyListNode(9), DoublyListNode(23), DoublyListNode(24), DoublyListNode(25)
    E.next, F.prev, F.next, G.prev, G.next, H.prev, H.next, I.prev, I.next, J.prev = F, E, G, F, H, G, I, H, J, I

    head = merge_double_link_list(A, E)
    while head:
        try:
            print(head.data, end=" ")
            print("%d %d" % (head.prev.data, head.next.data))
            head = head.next
        except AttributeError:
            print("Head.next.data will not exist in last element of merged doubly linked list")
            break
