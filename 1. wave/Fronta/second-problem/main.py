from collections import deque

documents_needed = {"stavba iglu": {75, 41, 5},
                    "registracia sani": {98, 5, 80},
                    "trafenie snehovou gulou": {33, 75},
                    "roztopenie snehuliaka": {41, 98, 4},
                    "presun ladovych soch": {33, 98, 75, 80}}


class Office:
    def __init__(self):
        self.queue = deque()


    def add_to_queue(self, penguin: tuple[str, set[int]]) -> None:
        self.queue.append(penguin)

    
    def next(self) -> None:
        if len(self.queue) > 0:
            action = self.queue[0][0]
            
            if action in documents_needed:
                if documents_needed[action] == self.queue[0][1]:
                    self.queue.popleft()

                else:
                    missing_docs = documents_needed[action] - self.queue[0][1]
                    all_papers = self.queue[0][1] | missing_docs  
                    the_action = self.queue[0][0]

                    self.queue[0] = (the_action, all_papers)

                    moved_penguin = self.queue[0]
                    self.queue.popleft()
                    self.queue.append(moved_penguin)

            else:
                self.queue.popleft()



    

# Testy
okienko = Office()
okienko.add_to_queue(("stavba iglu", {5, 75}))
okienko.add_to_queue(("roztopenie snehuliaka", {41}))

assert okienko.queue == deque([("stavba iglu", {5, 75}), ("roztopenie snehuliaka", {41})])
okienko.next()
assert okienko.queue == deque([("roztopenie snehuliaka", {41}), ("stavba iglu", {41, 75, 5})])
okienko.next()
assert okienko.queue == deque([("stavba iglu", {41, 75, 5}), ("roztopenie snehuliaka", {41, 98, 4})])
okienko.next()
assert okienko.queue == deque([("roztopenie snehuliaka", {41, 98, 4})])
okienko.next()
assert len(okienko.queue) == 0

okienko.next()  # nic sa nestane lebo fronta je prazdna
