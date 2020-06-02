"""

push(element) :append() O(1) , maintain LAst pointer
pop() : deleteFirst() maintain head pointer
seek() : current top () return head Value

"""


class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def _is_empty(self):
        return not self.head

    def push(self, elem):
        if self._is_empty():
            self.head = Node(elem)
        else:
            new_node = Node(elem)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self._is_empty():
            return -1
        else:
            val_to_pop = self.head.val
            self.head = self.head.next
            return val_to_pop


def test_stack():
    stack_obj = Stack()
    stack_obj.push(1)
    stack_obj.push(2)
    stack_obj.push(3)
    assert stack_obj.pop() == 3, "should be 3"
    # assert stack_obj._is_empty() == True, "Should be True"
    # assert stack_obj.pop() == -1, "Value should be -1"
    # assert stack_obj.push(1) == stack_obj.pop(), "Value should be same"
    print("Everything Passed")
    

test_stack()
