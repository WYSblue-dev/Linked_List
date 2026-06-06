"""
Exercise: Build and Use
Module 2 — Advanced Python & Data Handling
Estimated time: 40 minutes

Objective: Extend a LinkedList with 3 new methods, implement a stack-based
string reversal, and build a FIFO task queue using collections.deque.
"""

from collections import deque

# ============================================================
# PART 1 — Extend the LinkedList
# The Node and LinkedList classes below are provided.
# Your job: add the three new methods marked TODO.
# ============================================================


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list."""

    def __init__(self):
        self.head = None

    # ---- provided methods (do not modify) ----

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # ---- methods to implement ----

    def delete(self, target):
        """Remove the FIRST node whose data equals target.

        Returns True if found and deleted, False if target wasn't in the list.

        Hint: You need a reference to the node BEFORE the one you're deleting
        so you can re-link the chain. Handle the special case where the head
        itself is the target.
        Time: O(n)  Space: O(1)
        """
        current = self.head
        previous = None
        # runs while value at next
        while current:
            # conditional statement to see if correct value
            if current.data == target:
                # preivious is a obj value through loop otherwise None(head)
                if previous is None:
                    # deleting the head node and set to next
                    self.head = current.next
                else:
                    # set the value of next of previous to next value
                    previous.next = current.next
                return True
            # assign previous name value to the current of the while loop
            previous = current
            # reassign value to current next value
            current = current.next
        return False
        # TODO: implement delete

    def length(self):
        """Return the number of nodes in the list.
        Time: O(n)  Space: O(1)
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

        # TODO: walk the list and count nodes

    def to_list(self):
        """Convert the linked list to a plain Python list and return it.

        Time: O(n)  Space: O(n)
        """
        # TODO: walk the list, append each node's data, return the list
        current = self.head
        stacked_python = []
        # loop through nodes(data points)
        while current:
            # add the point to new list.
            stacked_python.append(current.data)
            # update the current point to next
            current = current.next

        # return data outside of loop
        return stacked_python


# ============================================================
# PART 2 — Stack: Reverse a String
# A stack is LIFO — Last In, First Out.
# Python lists work as stacks: append() = push, pop() = pop.
# ============================================================


def reverse_string(text):
    """Reverse a string using a stack (list with append/pop).

    Args:
        text: The string to reverse
    Returns:
        The reversed string

    Time: O(n)  Space: O(n)
    """
    # TODO:
    # 1. Push every character onto a stack (list).
    # 2. Pop all characters off the stack into a result list.
    # 3. Return "".join(result)
    text_list = list(text)
    result = []
    while text_list:
        result.append(text_list.pop())
    return "".join(result)


# ============================================================
# PART 3 — Queue: Task Processor
# A queue is FIFO — First In, First Out.
# Use collections.deque: append() adds to the right,
# popleft() removes from the left — both O(1).
# ============================================================


class TaskProcessor:
    """FIFO task queue backed by collections.deque."""

    def __init__(self):
        self._queue = deque()  # deque gives O(1) append and popleft

    def add_task(self, name):
        """Add a task to the back of the queue and print a confirmation.

        Args:
            name: Task name string
        """
        # TODO: append name to self._queue, then print:
        #   f"  Added task: {name!r}"
        self._queue.append(name)
        return print(f"  Added task: {name!r}")

    def process_next(self):
        """Remove and return the next task (the one waiting longest).

        Prints the task name when processing it.
        Returns None if the queue is empty.
        """
        # TODO: if _queue is empty, return None.
        # Otherwise popleft(), print f"  Processing: {task!r}", return the task.
        if self._queue:
            task = self._queue.popleft()
            print(f"  Processing: {task!r}")
            return task
        else:
            return None


# ============================================================
# Tests — run these after implementing each part
# ============================================================
if __name__ == "__main__":
    # --- Part 1: LinkedList ---
    print("=" * 60)
    print("PART 1: LinkedList")
    print("=" * 60)

    ll = LinkedList()
    for value in [10, 20, 30, 40, 50]:
        ll.insert_at_end(value)

    print("Initial list:  ", end="")
    ll.display()
    print(f"Length: {ll.length()}")
    print(f"As Python list: {ll.to_list()}")

    ll.delete(30)
    print("After delete(30):", end=" ")
    ll.display()

    ll.delete(10)  # delete head
    print("After delete(10) [head]:", end=" ")
    ll.display()

    print(f"delete(99) returned: {ll.delete(99)}")  # should be False

    # --- Part 2: Stack ---
    print("\n" + "=" * 60)
    print("PART 2: Stack — String Reversal")
    print("=" * 60)
    for word in ["hello", "Python", "12345"]:
        print(f"  reverse_string({word!r}) → {reverse_string(word)!r}")

    # --- Part 3: Queue ---
    print("\n" + "=" * 60)
    print("PART 3: Queue — Task Processor")
    print("=" * 60)

    processor = TaskProcessor()
    processor.add_task("send_email")
    processor.add_task("resize_image")
    processor.add_task("update_database")

    print()
    processor.process_next()  # should process "send_email" first (FIFO)
    processor.process_next()
    processor.process_next()

    result = processor.process_next()  # queue empty
    print(f"  Empty queue returns: {result}")  # should be None
