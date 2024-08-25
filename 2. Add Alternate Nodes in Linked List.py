class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def AddAlternateNodes(head):
    
    if head is None:
        return None
    
    current = head
    
    while current is not None and current.next is not None and current.next.next is not None:
        print("current =",current.data)
        two_ahead = current.next.next
        current.data += two_ahead.data        
        current = current.next
    
    return head


def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print()

# Example usage
if __name__ == "__main__":
    # Creating the linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
    
    print("Original list:")
    print_list(head)
    
    head = AddAlternateNodes(head)
    
    print("Modified list:")
    print_list(head)
