import re

phrase = "I am learning Ruby. I really enjoy the ruby programming language!"

#syntax
# string.replace(old_text, new_text, count)
# replace is case sensitive

# replace all instances of 'o' with 'a'
# substituted_phrase = phrase.replace("o", "a" )

# replace only the first two instances of 'o' with 'a'
# substituted_phrase = phrase.replace("o", "a", 2 )

# For case insensitive we have to use sub()
# syntax
# re.sub(pattern, replace, string, count, flags)

substituted_phrase = re.sub("ruby", "python", phrase)
# This does not change "Ruby" word bc of case for that we use flag re.IGNORECASE
substituted_phrase = re.sub("ruby", "python", phrase,flags=re.IGNORECASE)



print(phrase)
print(substituted_phrase)


# re.search(pattern, string) # similar to the find()

hand = open(file)
for i in hand:
    i = i.rstrip()
    if re.search('form: ', i):
        print(i)