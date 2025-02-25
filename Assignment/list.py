import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = 0
        self.next = None
    def add_node(self):
        data = int(input("Enter data to insert: "))
        position = int(input("Enter position to insert: "))
        node = Node(data)

        if position < 0 or position > self.head+1:
            print("Invalid position!")
            return

        if position == 0:
            node.next = self.next
            self.next = node
        else:
            prev = None
            temp = self.next
            for _ in range(position):
                prev = temp
                temp = temp.next
            node.next = temp
            prev.next = node

        self.head += 1

    def del_node(self):
        if self.next is None:
            print("Empty list, cannot delete")
            return
        
        position = int(input("Enter position to be deleted: "))
        
        if position < 0 or position >= self.head:
            print("Invalid position!")
            return

        if position == 0:
            self.next = self.next.next
            self.head -= 1
            return

        pos = 0
        temp1 = self.next
        prev = None

        while pos != position:
            prev = temp1
            temp1 = temp1.next
            pos += 1

        prev.next = temp1.next
        self.head -= 1

    def display_reverse(self):
       if self.next is None:
            print("List is empty")
            return

       def _reverse_display(node):
            if node is not None:
                    _reverse_display(node.next)
                    print(node.data, end=" ")

       _reverse_display(self.next)
       print(f"\nNumber of nodes: {self.head}")

class Menu:
    def match_choice(self,choice,l):
        match choice:
            case 1:
                l.add_node()
            case 2:
                l.del_node()
            case 3:
                l.display_reverse()
            case 4:
                self.sys_exit()
            case _:
                self.invalid_choice()

    def invalid_choice(self):
        print("invalid choice")
    def sys_exit(self):
        sys.exit("end of program")
    def run_menu(self):
        l1 = Linked_list()
        while True:
            choice = int(input("choose 1.add 2.delete 3.display 4.exit:"))
            self.match_choice(choice,l1)

def start_app():
    menu = Menu()
    menu.run_menu()

start_app()
