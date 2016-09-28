class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def queue(self, element):
        self.data.append(element)

    def unqueue(self):
        return self.data.pop(0)

    def empty(self):
        return len(self.data)