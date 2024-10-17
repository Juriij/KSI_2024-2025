class BinHeap:

    def __init__(self, heap_list):
        """Already gets a heap in list on the input"""
        self.heap_list = heap_list[:]

    def _left(self, i):
        """Get index of left child."""
        return (2*i)+1

    def _right(self, i):
        """Get index of right child."""
        return (2*i)+2

    def _up(self, i):
        """Get index of parent."""
        return (i-1)//2
