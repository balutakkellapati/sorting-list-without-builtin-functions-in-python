def split_string(input_string):
	input_list = []
	temp = ''
	for i in input_string:
		if i == ' ':
			input_list.append(temp)
			temp = ''
		else:
			temp += i
	if temp:
		input_list.append(temp)
	return input_list


def sorting(input_list):
	if not input_list:
		return []
	return (sorting([x for x in input_list[1:] if x < input_list[0]])
		+ [input_list[0]] +
			sorting([x for x in input_list[1:] if x >= input_list[0]]))

input_string = input('Enter the input string to be split: ')

split_list = split_string(input_string)
print(split_list)

sorted_list = sorting(split_list)
print(sorted_list)

final_sorted_list = []
for word in sorted_list:
	temp = list(word)
	temp = sorting(temp)
	temp = ''.join(temp)
	final_sorted_list.append(temp)

print(final_sorted_list)


