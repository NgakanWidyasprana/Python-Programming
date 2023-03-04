# If using .index() in string method
# You can do like this
def cek_index(log):
    index_first = log.index("[")
    index_last = log.index("]")
    return print(log[index_first+1:index_last])

error_log = cek_index("16/10/2020 17:00:12, code error [404102] : saving error")
error_log = cek_index("16/10/2020 17:00:20, code error [123] : load error")
error_log = cek_index("16/10/2020 17:00:30, code error [1021218212] : database error")

# If using re module for regex
# You can do this

import re
error_log = "16/10/2020 17:00:12, code error [404102] : saving error"
regex = r"\[(\d+)\]"
result = re.search(regex, error_log)
print(result[1])

# Using special character to search formatting words
print("\n")
def search_key_word(text,key):
    value = re.search(key,text,re.IGNORECASE)
    return value

print(search_key_word("makanan",r"kanan$")) # Using $
print(search_key_word("minuman",r"^minum")) # Using ^
print(search_key_word("indonesia",r"d.n.")) # Using .
print(search_key_word("inggris",r"ras"))    # Not found
print(search_key_word("raSa",r"ras"))       # addtional IGNORECASE

# Using character class
def check_punctuation (text):
   result = re.search(r"[,.:;?']", text)
   return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

# Using .groups() and (\w*)
def group(name):
    result = re.search(r"^(\w*):(\w*)$",name)                  # ^([\w \.-]*), ([\w \.-]*)$
    if result is None:                                         # alternatif solution if the name like Ngakan M. or John L.
       return name,None
    return "{}:{}".format(result[2],result[1]),result.groups()

name,tuples = group("Ngakan:William")
print(name)
print(tuples)
