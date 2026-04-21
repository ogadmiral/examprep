def echo_validator(text: str) -> bool:
	text = text.lower().replace(" ", "")
	txt = text
	i = len(text) - 1
	j = 0
	while i >= 0:
		if txt[i] != text[j]:
			return False
		j += 1
		i -= 1
	if txt == "":
			return False
	return True
	