def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
	if brackets_row[0] == ")":
		return False
	x = 0
	for i in brackets_row:
		if i == "(":
			x += 1
		else:
			x -= 1
	if x == 0:
		return True
	return False
