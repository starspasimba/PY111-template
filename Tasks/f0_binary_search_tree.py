"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Hashable, Any, Optional, Tuple
# import networkx as nx

tree = dict()

def insert(key: Hashable, value: Any) -> None:
	"""
	Insert (key, value) pair to binary search tree

	:param key: key from pair (key is used for positioning node in the tree)
	:param value: value associated with key
	:return: None
	tr {key:(value, left, right)}

	"""
	global tree
	tr = tree
	while True:
		if not tr:
			tr.update({"key":key, "value":value, "left": {}, "right": {}})
			break
		elif tr["key"] > key:
			tr = tr["left"]
		elif tr["key"] < key:
			tr = tr["right"]
		elif tr["key"] == key:
			tr.update({"value": value})
			break

	print(key, value)
	return None


def remove(key: Hashable) -> Optional[Tuple[Hashable, Any]]:
	"""
	Remove key and associated value from the BST if exists

	:param key: key to be removed
	:return: deleted (key, value) pair or None
	"""
	# global tree
	tr = find_tree(key)

	if tr:
		while True:
			if tr["left"]:
				tr = tr["left"]
			elif tr["right"]:
				trsavevalue = tr["value"]
				trsavekey = tr["key"]
				tr = tr["right"]
				break
			else:
				trsavevalue = tr["value"]
				trsavekey = tr["key"]
				tr = dict()
				break
	tr = find_tree(key)
	if tr:
		tr.update({"key": trsavekey, "value": trsavevalue})

	print(key)
	return None


def find(key: Hashable) -> Optional[Any]:
	"""
	Find value by given key in the BST

	:param key: key for search in the BST
	:return: value associated with the corresponding key
	"""
	global tree
	tr = tree
	while True:
		if tr["key"] == key:
			return tr["value"]
		elif (tr["key"] > key) and (tr["left"]):
			tr = tr["left"]
		elif (tr["key"] < key) and (tr["right"]):
			tr = tr["right"]
		else:
			raise KeyError("ErrorKey")

def find_tree(key: Hashable) -> Optional[Any]:
	"""
	Find value by given key in the BST

	:param key: key for search in the BST
	:return: value associated with the corresponding key
	"""
	global tree
	tr = tree
	while True:
		if tr["key"] == key:
			print(tr["key"])
			return tr
		elif (tr["key"] > key) and (tr["left"]):
			tr = tr["left"]
		elif (tr["key"] < key) and (tr["right"]):
			tr = tr["right"]
		else:
			print(" nothing ")
			return None

def clear() -> None:
	"""
	Clear the tree

	:return: None
	"""
	global tree

	tree = dict()

	return None
