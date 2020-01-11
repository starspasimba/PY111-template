from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	for i in range(len(container), 0, -1):
		for x in range(i):
			if ((x + 1) < i) and (container[x]>container[x + 1]):
				z = container[x + 1]
				container[x + 1] = container[x]
				container[x] = z

	return container
 