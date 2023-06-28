"""Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells."""

string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
str2 = string.upper()
my_list = str2.split()
print (my_list)
phrase = set (my_list)
my_list = list(phrase)
print (len(my_list))