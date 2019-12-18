from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	null_ind = 0
	ind = len(arr) - 1
	if (elem < arr[0]) or (elem > arr[ind]):
		return None
	if elem == arr[null_ind]:
		return null_ind
	if elem == arr[ind]:
		return ind

	while (ind - null_ind) > 1:
		search_ind = (ind + null_ind) // 2
		if elem > arr[search_ind]:
			null_ind = search_ind
		if elem < arr[search_ind]:
			ind = search_ind
		if elem == arr[search_ind]:
			return search_ind



	print(elem, arr)
	return None
