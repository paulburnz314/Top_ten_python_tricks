'''		When you get a lab report the results somestimes have qualifiers such
	as '>' or '<' the method detection limit or practical quantitation limit.
	If you need to use this number in a calculation you will need to strip any
	non numeric characters.  Most likely you will get data from an excel or csv
	file.
'''

def replaceMultiple(mainString, toBeReplaces, newString):   # Iterate over the strings to be replaced
	for elem in toBeReplaces:   # Check if string is in the main string
		if elem in mainString:  # Replace the string
			mainString = mainString.replace(elem, newString)
	return mainString


def remove_q(lab_result):
	checkstr = isinstance(lab_result, str)   # start checking for <, >, empty space or None values
	if checkstr is True:
		lab_result = replaceMultiple(lab_result, ['>', '<'], '')
		if lab_result == ' ':
			lab_result = 0
		elif lab_result is None:
			lab_result = 0
		else:
			lab_result = float(lab_result)    # data is cleaned up and converted to a number

	return lab_result


if __name__ == '__main__':
	print("Example:")
	print(remove_q('< 37.1'))

	assert remove_q('>167') == 167
	assert remove_q('<46.6') == 46.6
	assert remove_q('<0.10') == 0.10
	assert remove_q(' ') == 0
	assert remove_q(99.5) == 99.5
    