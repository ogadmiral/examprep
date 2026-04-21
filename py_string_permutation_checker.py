def string_permutation_checker(s1: str, s2: str) -> bool:
	if len(s1) != len(s2):
		return False
	for c in s1:
		s1 = s1.replace(c, "")
		s2 = s2.replace(c, "")
		if len(s1) != len(s2):
			return False
	return True
