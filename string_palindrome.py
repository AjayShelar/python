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

    def pop(self, n):
        lst = [0] * n
        temp = self.head
        i = 0
        while (temp):
            lst[i] = temp.data
            temp = temp.next
            i += 1
        return lst

#driver code
if __name__=='__main__':
    LL = LinkedList()
    string = 'abacaba'
    for i in string:
        LL.push(i)
    rev = []
    rev = LL.pop(len(string))
    count = 0
    for i in range(len(string)):
        if string[i] == rev[i]:
            count += 1
        else:
            pass
    if count == len(string):
        print('string is palindrome')
    else:
        print('not a palindrome')