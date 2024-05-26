class ListNode:
    def _init_(self,val=0,next=None):
        self.val=val
        self.next = next 
    def reverse_linked_list(head):
        prev = None 
        current = head 
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node 
            return prev 
         # creat a linked list : 1-> 2-> 3-> 4-> 5
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_head = reverse_linked_list.head 
        # Print the reversed linked list
while reversed_head:
    print(reversed_head.val, end=" -> ")
    reversed_head = reversed_head.next


