from textblob import TextBlob

wrongdata = input("enter any statement :")

b = TextBlob(wrongdata)

print("correct statement : ",str(b.correct()))

