from textblob import TextBlob
str = input("Enter the string:")
text = TextBlob(str)
analysis = text.sentiment
print(analysis)