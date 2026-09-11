# Node class
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def append_at_head(self, data):
        new_node = Node(data)

        # New node points to current head
        new_node.next = self.head

        # New node becomes the head
        self.head = new_node

    def append_at_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return True

        current = self.head
        while current.next is not None:
             current = current.next

        current.next = new_node
        return True
        
    def show_nodes(self): #traversal
        current = self.head

        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

        print("None")

    def search_node(self, data):
        current = self.head

        while current is not None:
             if current.value == data:
                 return f"Found"
             
             current = current.next

        return f"Not found"

    def length_of_nodes(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return f"I have {length} items"

    def sum_of_nodes(self):
        total = 0
        current = self.head
        while current is not None:
             sum += current.value
             current = current.next
        return f"Total sum of nodes is {total}"


llist = MyLinkedList()

llist.append_at_head(10)
llist.append_at_head(20)
llist.append_at_head(30)
llist.append_at_last(40)
llist.show_nodes()
print(llist.search_node(30))
print(llist.search_node(50))
print(llist.length_of_nodes())
print(llist.sum_of_nodes())
print(llist.average_of_nodes())