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
        self.prev = None


class LinkedList:
    """Singly linked list."""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        """Insert a new node at the end of the list.

        Time: O(1) because we maintain self.tail.

        Space: O(1)

        """

        new_node = Node(data)

        # Empty list case

        if not self.head:

            self.head = new_node

            self.tail = new_node

            return

        # Current tail points forward to the new node

        self.tail.next = new_node

        # New node points backward to the old tail

        new_node.prev = self.tail

        # Move the tail pointer to the new node

        self.tail = new_node

    def display(self):
        """Print the list from head to tail.

        Time: O(n)

        Space: O(1)

        """

        current = self.head

        while current:

            print(current.data, end=" <-> ")

            current = current.next

        print("None")

    def display_reverse(self):
        """Print the list from tail to head without converting to a Python list.

        Time: O(n)

        Space: O(1)

        """

        current = self.tail

        while current:

            print(current.data, end=" <-> ")

            current = current.prev

        print("None")

    def delete(self, target):
        """Remove the FIRST node whose data equals target.

        Returns True if found and deleted, False otherwise.

        Time: O(n), because we still may need to search the list.

        Space: O(1)

        """

        current = self.head

        while current:

            if current.data == target:

                # Case 1: deleting the head

                if current.prev is None:

                    self.head = current.next

                else:

                    current.prev.next = current.next

                # Case 2: deleting the tail

                if current.next is None:

                    self.tail = current.prev

                else:

                    current.next.prev = current.prev

                return True

            current = current.next

        return False

    def length(self):
        """Return the number of nodes in the list.

        Time: O(n)

        Space: O(1)

        """

        count = 0

        current = self.head

        while current:

            count += 1

            current = current.next

        return count

    def to_list(self):
        """Convert the linked list to a Python list.

        Time: O(n)

        Space: O(n)

        """

        result = []

        current = self.head

        while current:

            result.append(current.data)

            current = current.next

        return result


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


# test the doublylinked list
if __name__ == "__main__":
    ll = LinkedList()

    for value in [10, 20, 30, 40, 50]:
        ll.insert_at_end(value)

    print("Forward: ", end="")
    ll.display()

    print("Reverse: ", end="")
    ll.display_reverse()

    print(f"Length: {ll.length()}")
    print(f"As Python list: {ll.to_list()}")

    ll.delete(30)
    print("After delete(30): ", end="")
    ll.display()

    ll.delete(10)
    print("After delete(10) [head]: ", end="")
    ll.display()

    ll.delete(50)
    print("After delete(50) [tail]: ", end="")
    ll.display()

    print("Reverse after deletes: ", end="")
    ll.display_reverse()

    print(f"delete(99) returned: {ll.delete(99)}")
