class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

class LinkedList: 
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def add_at_end(self, data):

        if self.head is None:
            self.insert_at_beginning(data)
            return

        itr = self.head

        while itr :
            lastnode = itr
            itr = itr.next
        

        lastnode.next = Node(data)

    def print(self):
        if self.head is None:
            print("Empty")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        
        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    ll.add_at_end(10)
    ll.print()