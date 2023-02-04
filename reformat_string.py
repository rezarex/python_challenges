def str_to_list( str ) :
	new_list = []
	for index in range(len(str)):
		if str[index] == ' ':
			continue
		elif str[index].isdigit():
			if int(str[index]) > 5:
				continue
		new_list.append(str[index])

	return new_list

str = "5 dollar"
print(str_to_list( str ))