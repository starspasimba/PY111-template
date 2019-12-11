"""
My little Stack
"""
from typing import Any


stack_list: list = []
def push(elem: Any) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""

	# print(elem)
	global stack_list
	stack_list.append(elem)
	return None


def pop() -> Any:
	"""
	Pop element from the top of the stack

	:return: popped element
	"""

	global stack_list

	if stack_list:
		last_elem = stack_list[-1]
		del stack_list[-1]
	else:
		last_elem = None

	return last_elem


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""

	global stack_list
	nomer_elem = -1
	# print(ind)
	nomer_elem -= ind
	return stack_list[nomer_elem]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""

	global stack_list
	stack_list = []
	return None

if __name__ == '__main__':
	items = [i for i in range(10)]

	for i in items:
		push(i)

	received_items = []
	for _ in items:
		received_items.append(pop())

	print(list(reversed(items)), received_items)