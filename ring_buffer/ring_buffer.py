class RingBuffer:
    def __init__(self, capacity):
        # Set the storage capacity to be empty
        self.storage = []
        # set the oldest to be None
        self.oldest = None
        self.capacity = capacity

    def append(self, item):
        # Check if the storage is empty and capacity is not reached
        # if it is empty add the item
        if self.capacity > 0:
            if self.oldest == None:
                self.storage.append(item)
                self.oldest = 0
        # if storage is not empty and the capacity is full
        # Override it
            elif len(self.storage) == self.capacity:
                self.storage[self.oldest] = item

                if self.oldest == self.capacity - 1:
                    self.oldest = 0
                else:
                    self.oldest = self.oldest + 1

            else:
                self.storage.append(item)

    def get(self):
        return self.storage
