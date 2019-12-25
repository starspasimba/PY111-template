from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
	"""
	Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

	:param stairway: list of ints, where each int is a cost of appropriate step
	:return: minimal cost of getting to the top
	"""
	straicount_sum = [0] * len(stairway)
	straicount_sum[0], straicount_sum[1] = stairway[0], stairway[1]
	for i in range(2, len(stairway)):
		straicount_sum[i] = stairway[i] + min(straicount_sum[i - 1], straicount_sum[i - 2])

	return straicount_sum[-1]
