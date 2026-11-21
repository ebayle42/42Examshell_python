from __future__ import annotations


class MinHeap:
    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        data = self.data
        data.append(val)
        i = len(data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if data[parent] <= data[i]:
                break
            data[parent], data[i] = data[i], data[parent]
            i = parent

    def pop(self) -> int | None:
        data = self.data
        if not data:
            return None
        top = data[0]
        last = data.pop()
        if data:
            data[0] = last
            i = 0
            n = len(data)
            while True:
                left, right, smallest = 2 * i + 1, 2 * i + 2, i
                if left < n and data[left] < data[smallest]:
                    smallest = left
                if right < n and data[right] < data[smallest]:
                    smallest = right
                if smallest == i:
                    break
                data[i], data[smallest] = data[smallest], data[i]
                i = smallest
        return top

    def peek(self) -> int | None:
        return self.data[0] if self.data else None

    def size(self) -> int:
        return len(self.data)
