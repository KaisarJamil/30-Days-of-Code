

class Solution:
    def __init__(self):
        self.stack = []
        self.queue= []

    def pushCharacter(self,ch):
        self.stack.append(ch)
    def enqueueCharacter(self,ch):
        self.queue.append(ch)

    def popCharacter(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
    def dequeueCharacter(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

