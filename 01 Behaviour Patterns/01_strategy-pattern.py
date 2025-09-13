from abc import ABC, abstractmethod


class Sort(ABC):
    @abstractmethod
    def sort(self, elements: list[int]): ...


class MergeSort(Sort):
    def sort(self, elements: list[int]):
        print(f"Sorting elements {elements} using merge sort")


class QuickSort(Sort):
    def sort(self, elements: list[int]):
        print(f"Sorting elements {elements} using quick sort")


class BubbleSort(Sort):
    def sort(self, elements: list[int]):
        print(f"Sorting elements {elements} using bubble sort")


class Client:
    def __init__(self, sort: Sort):
        self.sort_tech = sort

    def sort(self, elements: list[int]):
        self.sort_tech.sort(elements)


c = Client(MergeSort())
c.sort([1, 2, 3, 4])
