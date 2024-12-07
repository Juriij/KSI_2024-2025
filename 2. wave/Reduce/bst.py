#!/usr/bin/env python3

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BST:
    def __init__(self):
        self.root = None
        self.actual = None

    def _add(self, actual, key):
        if key < actual.key:
            if actual.left is None:
                actual.left = Node(key)
                actual.left.parent = actual
            else:
                self._add(actual.left, key)
        else:
            if actual.right is None:
                actual.right = Node(key)
                actual.right.parent = actual
            else:
                self._add(actual.right, key)

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._add(self.root, key)
        return self

    def __iter__(self):
        self.actual = self.root
        if self.actual is None:
            return self
        while self.actual.left is not None:
            self.actual = self.actual.left
        return self

    def __next__(self):
        actual = self.actual
        if self.actual is None:
            raise StopIteration
        if self.actual.right is not None:
            self.actual = self.actual.right
            while self.actual.left is not None:
                self.actual = self.actual.left
            return actual.key
        else:
            if self.actual.parent is None:
                self.actual = None
                return actual.key
            while self.actual.parent.right is self.actual:
                self.actual = self.actual.parent
                if self.actual.parent is None:
                    self.actual = None
                    return actual.key
            self.actual = self.actual.parent
            if self.actual is None:
                return actual.key
            return actual.key
        