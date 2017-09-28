class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList :

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):

        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prints(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next



#driver code
if __name__=='__main__':
    LL = LinkedList()
    for value in range(0,10):
        LL.push(value)
        LL.append(value+value)
    LL.prints()
