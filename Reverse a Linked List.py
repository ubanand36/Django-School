# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next  # store next
        curr.next = prev       # reverse pointer
        prev = curr            # move prev forward
        curr = next_node       # move curr forward
    
    return prev  # new head

# Example usage:
# Creating linked list 1→2→3→4→5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Reverse it
new_head = reverse_list(head)

# Print reversed list
while new_head:
    print(new_head.val, end=" → ")
    new_head = new_head.next
# Output: 5 → 4 → 3 → 2 → 1 →
