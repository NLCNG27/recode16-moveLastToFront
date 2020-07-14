# Author: Nguyen L.
# Date: July 14th, 2020
# Move last element to front of the linear linked list
# Example: 1 -> 2 -> 3 -> 4 will become 4 -> 1 -> 2 -> 3


from random import randint

# Node class
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# LinkedList class
class LinkedList:
    def __init__(self, data=None):
        self.head = Node(data)

    # insert beginning method
    def addBeginning(self, newData):
        temp = Node(newData)
        temp.next = self.head
        self.head = temp

    # generating random list of nodes
    def randomList(self, limit=5):
        i = 0

        while i < limit:
            value = randint(1, 20)
            self.addBeginning(value)
            i += 1


    # searching iteratively function
    def searchElement(self, number):

        # default case if there's no list in the first place
        if not self.head:
            return False

        current = self.head

        # going through the linked list
        while current is not None:
            if current.data == number:
                return True
            current = current.next

        return False

    # move last to front
    def moveLastToFront(self):

        current = self.head
        previous = None
        temp = None

        # empty or single node
        if not current or not current.next:
            return

        # traverse the list
        while current is not None and current.next is not None:
            temp = current
            previous = current
            current = current.next

        previous.next = None

        self.addBeginning(temp.data)


    # display method
    def display(self):
        temp = self.head

        while temp.next is not None:
            print(temp.data, end=" ")
            temp = temp.next    


# TESTING OUT THE PROGRAM
myList = LinkedList()
limit = randint(5, 10)
print("*" * 40)
print("Original list: ", end="")
myList.randomList(limit)
myList.display()
print()

print("*" * 40)
print("Moving last node to first....")
myList.moveLastToFront()
print("New list: ", end="")
myList.display()
print()



