from random import shuffle
from operator import eq, ne, gt, lt, ge, le


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def push(self, val):
        """ Appends node to end on LL """
        n = self
        while n.next:
            n = n.next
        n.next = Node(val)

    def push_many(self, array):
        """
        :param array: list<int>
        :return: void
        :Appends every elem from array to end of LinkedList
        """
        for elem in array:
            self.push(elem)

    def __str__(self):
        """ Overrides print() function """
        return str(self.value)

    def print(self):
        """ Prints value/reference details of LinkedList. Prints: 1->2->5->->7->None """
        n = self
        text = str(n.value) + '->'
        while n.next:
            n = n.next
            text += str(n.value) + '->'
        text += 'None'
        print(text)

    def __radd__(self, other):
        """ Implements sum() function """
        return self.value + other

    def remove(self, index):
        """ Removes a node at a specified index and shifts later nodes forward """
        counter = 0
        n = self
        prev = None
        while n.next:
            if counter >= index:
                n.value = n.next.value
            prev = n
            n = n.next
            counter += 1
        prev.next = None

    def to_array(self):
        """ Returns a list of node values in order """
        values = [self.value]
        n = self
        while n.next:
            n = n.next
            values.append(n.value)
        return values

    def __add__(self, other):
        """ Overloads '+' operator. Takes LinkedList1(self) + LinkedList2(other) and returns new LinkedList3"""
        new_node = Node(self.value)
        new_node.push_many(self.to_array()[1:])
        new_node.push_many(other.to_array())
        return new_node

    def __iadd__(self, other):
        """ Overloads '+=' operator. Takes node or int and appends to end as new node """
        if type(other) == int:
            self.push(other)
        elif type(other) == Node:
            self[-1].next = other
        else:
            raise Exception()
        return self

    def __imul__(self, other):
        """ Overloads the '*=' operator. Duplicates the array by 'other' times """
        count = other - 1
        array = self.to_array() * count
        self.push_many(array)
        return self

    def shuffle(self):
        """ Shuffles the values of all nodes in the Linked List """
        array = self.to_array()
        shuffle(array)
        n = self
        n.value = array.pop(0)
        while n.next:
            n = n.next
            n.value = array.pop(0)

    def sort(self):
        """ Sorting method that relies on List.sort()"""
        array = self.to_array()
        array.sort()
        n = self
        n.value = array.pop(0)
        while n.next:
            n = n.next
            n.value = array.pop(0)

    def quick_sort(self, array, low, high):
        """ Broken-ass quicksort implementation """
        def partition(array, low, high):
            i = low - 1
            pivot = array[high]
            for j in range(low, high):
                if array[j] <= pivot:
                    i += 1
                    array[i].value, array[j].value = array[j].value, array[i].value
            array[i + 1].value, array[high].value = array[high].value, array[i + 1].value
            return i + 1

        print(True)
        if low < high:
            pi = partition(array, low, high)
            self.quick_sort(array, low, pi-1)
            self.quick_sort(array, pi+1, high)

    def __iter__(self):
        """ Implements self as iterator. Usage: for node in linked_list: """
        yield self
        n = self
        while n.next:
            n = n.next
            yield n

    def __getitem__(self, index):
        """ Implements list indexing """
        return list(self.__iter__())[index]

    def calculate(self, operator, other):
        """ Helper function for operator overloaders """
        if type(other) == int:
            return operator(sum(self), other)
        elif type(other) == Node:
            return operator(sum(self), sum(other))
        else:
            return False

    def __eq__(self, other):
        """ Overloads the '==' operator """
        return self.calculate(eq, other)

    def __ne__(self, other):
        """ Overloads the '!=' operator """
        return self.calculate(ne, other)

    def __gt__(self, other):
        """ Overloads the '>' operator """
        return self.calculate(gt, other)

    def __lt__(self, other):
        """ Overloads the '<' operator """
        return self.calculate(lt, other)

    def __ge__(self, other):
        """ Overloads the '>=' operator """
        return self.calculate(ge, other)

    def __le__(self, other):
        """ Overloads the '<=' operator """
        return self.calculate(le, other)

    def __len__(self):
        """ Implements len() function """
        return len([1 for _ in self])

    def __reversed__(self):
        """ Implements reversed() function """
        j = -1
        for i in range(len(self) // 2):
            self[i].value, self[j].value = self[j].value, self[i].value
            j -= 1

    def __contains__(self, item):
        """ Implements 'in' syntax. Usage: 5 in self, 6 in instance """
        for node in self:
            if node.value == item:
                return True
        return False


root = Node(0)
root.push_many(range(1, 5))

root.print()
print(sum(root))
print(root == 10, root != 10)
print(4 in root, 5 in root)
