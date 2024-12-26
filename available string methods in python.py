
# methods of string variable in python
text="helloworld"
text_upper=text.upper()
print("the data in uppercase letters":,text_upper)

text_lower=text.lower()
print("the data in lowercase letters":,text_lower)

name="     sagar  "
newname=name.strip()
print("the data without space letters:",newname)

lspace=name.lstrip()
print("the data without space from the left:",name)

rspace=name.rstrip()
print("the data without space from the right:",name)


sentence1="python programming is fun"
words = sentence1.split()#["python","programming","is","fun"]
print("the data will be split in this method:",words)

sentence = "i like apples,and i like pineapple."
new_sentence = sentence.replace("like","love")
print(new_sentence)
