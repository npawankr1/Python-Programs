# https://www.facebook.com/harhar.modi.1232/posts/706155836649246
# Subscribed by Jayant Gupta

# A python program to remove punctuation from a sentance

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hi!! My name is Jayant Gupta.."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)
