class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self, num):
        self.head = 0  # Number of nodes
        self.next = None  # Head node pointer
        print(f'List-{num} is created')

    def create_node(self, data):
        return Node(data)

    def add_node_at_front(self, data):
        new_node = self.create_node(data)
        new_node.link = self.next
        self.next = new_node
        self.head += 1

def create_list(num):
    linked_list = LinkedList(num)
    print(f'Creating List-{num}')
    while True:
        data = int(input('Enter data of the new node: '))
        linked_list.add_node_at_front(data)
        choice = input('Enter 1 to add node, other number to stop: ')
        if choice != '1':
            break
    return linked_list

def check_if_converges(list1, list2):
    if list1.next is None or list2.next is None:
        return "Lists do not converge"

    nodes_set = set()
    temp1 = list1.next
    temp2 = list2.next
    
    while temp1 is not None:
        nodes_set.add(temp1)
        temp1 = temp1.link

    position = 0
    while temp2 is not None:
        if temp2 in nodes_set:
            return position
        temp2 = temp2.link
        position += 1

    return "Lists do not converge"

list1 = create_list(1)
list2 = create_list(2)
result = check_if_converges(list1, list2)

if result == "Lists do not converge":
    print(result)
else:
    print(f'The lists converge at position-{result}')
