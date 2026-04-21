def transform(character: str) -> str:
	if character == ')':
		return '('
	elif character == '}':
		return '{'
	elif character == ']':
		return '['
	return ""

def bracket_validator(s: str) -> bool:
	open = '([{'
	close = ')]}'
	stack = []
	for c in s:
		if c in open:
			stack.append(c)
		elif c in close and stack:
			if transform(c) == stack[-1]:
				stack.pop(-1)
			else:
				return False
		elif c in close:
			return False

	return True
