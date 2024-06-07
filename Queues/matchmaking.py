def matchmake(queue, player):
    name = player[0]
    action = player[1]
    if action == "leave":
        queue.search_and_remove(name)
    if action == "join":
        queue.push(name)
    if queue.size() >= 4:
        player1 = queue.pop()
        player2 = queue.pop()
        return f"{player1} matched {player2}!"
    else:
        return "No match found"


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def search_and_remove(self, item):
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self):
        return f"[{', '.join(self.items)}]"
