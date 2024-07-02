def merge_sorted_lists_recursive(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val < l2.val:
        l1.next = merge_sorted_lists_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_sorted_lists_recursive(l1, l2.next)
        return l2