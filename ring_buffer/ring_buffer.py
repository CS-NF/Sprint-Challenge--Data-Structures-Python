from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()


# *** Plan ***
# make sure that the capacity is greater then the len of our storage
# if we have enough space we will then add item to the tail
# then we initialize that we are at the head of the LL beacuse it's a queue (first in first out) 
# checking to see if we are at the tail of the list
# the prev node will be the head 
# saving node after the current 
# we are overwriting the current value with the new item 
# the current node is not the next from current 
    def append(self, item):
        if self.capacity > self.storage.length: # checking to make sure that our capacity is greater then the len of our storage 
            self.storage.add_to_tail(item) # if so then we add item to the tail of our LL
            self.current = self.storage.head # then we initialize that we are at the head of the LL beacuse it's a queue (first in first out) 
        else:
            if self.current == self.storage.tail: # checking to see if we are at the tail of the list
                 next_oldest_node = self.storage.head # the prev node will be the head 
            else:
                next_oldest_node = self.current.next # saving node after the current 
            self.current.value = item # we are overwriting the current value with the new item 
            self.current = next_oldest_node # the current node is now the next from current 



# *** Plan ***
# create a variable and assigne the head to it
# create a loop so we can iterate through the list
# add the value of our head to the list_buffer_contents 
# we then iterate to the next node and the loops repeats
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current_head = self.storage.head # created variable called current_head and assigned the head to it

        while current_head is not None: # as long as we are at our head and it's not None then execute the code below
            list_buffer_contents.append(current_head.value) # we add the heads value into our now not empty list list_biffer_contents
            current_head = current_head.next # then we iterate to the next node 

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
