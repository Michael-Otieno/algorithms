class Node:
    """
    Object for storing a single node of a linked list
    Models two attributes-data and the link to the next node in the list
    """
    data=None
    next_node=None

    def __init__(self,data):
        self.data=data
        # self.next_node=next_node

     
class LinkedList:
    """
    Singly linked list
    """
    # head=None
    def __init__(self):#modeling singly linked list
        self.head = None#only node that the list will have reference to

    def is_empty(self):#if head is none
        return self.head==None

    def size(self):
        '''
        Returns the number of nodes in the list
        Takes 0(n)time
        '''
        current=self.head
        count=0

        while current:#while current != None
            count+=1
            current=current.next_node#assigning next node to current
            
        return count

    def add(self,data):
        """
        Adds new node containing data at head(adds to start of node) of the list
        Takes 0(1) time
        """
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node

    def search(self,key):
        """
        Search for the first node containing data that matches the key
        Returns the node or None if not found
        Takes 0(n)time
        """
        current=self.head
        while current:
            if current.data==key:
                return current
            else:
                current=current.next_node
        return None


    def insert(self,data,index):
        """
        Inserts a new Node containing data at index position
        Insertion takes 0(1) but finding the node at the insertion point takes 0(n)

        Takes overall 0(n)
        """
        if index==0:
            self.add(data)
        if index>0:
            new=Node(data)

            position=index
            current=self.head

            while position>1:
                current = current.next_node#######
                position -= 1

            prev_node=current
            next_node=current.next_node

            prev_node.next_node=new
            new.next_node=next_node


    def remove(self,key):
        '''
        Removes node containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes 0(n) time
        '''
        current = self.head
        previous=None
        found=False

        while current and not found:
            if current.data==key and current is self.head:
                found=True
                self.head=current.next_node

            elif current.data==key:
                found=True
                previous.next_node=current.next_node
            else:
                previous=current
                current=current.next_node
        return current
        


    def node_at_index(self, index):
        if index==0:
            return self.head
        else:
            current=self.head
            position=0
            while position<index:
                current = current.next_node
                position += 1
            return current

    def __repr__(self):
        """
        Returns string representation of the list.
        Takes 0(n) time.
        """
        nodes=[]#create empty list
        current=self.head#asign pointer to headnode
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:#asign pointer to tailnode
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current=current.next_node
        return '->'.join(nodes)


