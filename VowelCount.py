#Please note: this program tells you the ordinal space of vowels, not their location according to python (e.g. First letter = 1, not 0)
Word = input("Please enter a word or phrase: ").lower()
iter = len(Word)
a = 0
vowel_list = []
for letter in range (iter):
	letter = Word[a]
	if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
		vowel_list.append(a + 1)
	a = a + 1
print (vowel_list)