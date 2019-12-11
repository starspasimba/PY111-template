"""
My little Queue
"""
from typing import Any

que: list = []
def enqueue(elem: Any) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global que
	que.append(elem)
	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	return_elem = 0
	global que
	if que:
		return_elem = que[0]
		del que[0]
	else:
		return_elem = None
	return return_elem


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	peek_elem = 0
	global que
	if que:
		peek_elem = que[ind]
	else:
		peek_elem = None

	return peek_elem


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global que
	que = []
	return None

