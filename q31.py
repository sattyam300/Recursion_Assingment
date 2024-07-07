class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    if l1.value < l2.value:
        l1.next = merge_sorted_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_sorted_lists(l1, l2.next)
        return l2

# Helper function to print the linked list
def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Example usage
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
print("List 1:")
print_list(l1)
print("List 2:")
print_list(l2)
merged_head = merge_sorted_lists(l1, l2)
print("Merged list:")
print_list(merged_head)
