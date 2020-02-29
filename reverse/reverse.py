class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

# *** Plan ***
# creating a variable current_node to head which is our starting point
# previous is none at the moments meaning we are at the begging of the list
# make a loop and check if there is a current head if so we do code below
# we move to the next node so the next node is now the current node
# the node we moved away from now because the previous node
# sorting the new linked list
# our head now beacuse our previous since we iterated from it

  def reverse_list(self):
    current_node = self.head # creating a variable current_node to head which is our starting point
    prev = None # previous is none at the moments meaning we are at the begging of the list
    while current_node is not None: # make a loop and check if there is a current head if so we do code below
      next_node = current_node.next_node # we move to the next node so the next node is now the current node
      current_node.next_node = prev # the node we moved away from now because the previous node
       # sorting
      prev, current_node = current_node, next_node # sorting the new linked list
    self.head = prev # our head now beacuse our previous since we iterated from it

