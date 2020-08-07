from collections import defaultdict

def distinct_string(string):
	distinct_length = len(set(list(string))) 
	i = j = 0
	string_size = float('inf')
	window = defaultdict(int)
	
	while (i <= j) and (j < len(s)):
		window[string[j]] +=1
		while len(window) == distinct_length and i <= j: 
			string_size = min(string_size, j-i+1)
			window[string[i]] -= 1
			if window[string[i]] == 0:
				del window[string[i]]
			i += 1
		j += 1
	return string_size


if __name__ == '__main__':
	n = int(input("Number of strings: "))
	print("Enter testcases: \n")
	kappa = list()
	for i in range(n):
		s = input()
		kappa.append(s)

	for string in kappa:
		print(distinct_string(string))