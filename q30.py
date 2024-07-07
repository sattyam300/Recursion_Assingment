class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_list_recursive(head):
    if head is None or head.next is None:
        return head
    
    rest = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return rest

# Helper function to print the linked list
def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original list:")
print_list(head)
reversed_head = reverse_list_recursive(head)
print("Reversed list:")
print_list(reversed_head)
