'''#1.Count no of vovels
name = str(input("enter name here:"))
vowels="aeiou"
count = sum(1 for i in name if i in vowels)
print(count)

#3.Reverse a string
word = input("enter word here:")
text = ""
for i in word:
    text=i+text
print(text)'''

'''#5 Remove the spaces
word = input("enter word here:")
text=word.strip( )
print(text)

#7 Replace all spaces with -.
word = input("enter word here:")
print(word.replace(" ","-"))

#8 First word into uppercase
k= input("enter word here:")
print(k.capitalize())'''

#9 Find the frequency of each character in a string
word= input("enter word here:")
print(word.count('='))


























