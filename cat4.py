import string, sys
def ispangram(str1,alphabet=string.ascii_lowercase):
    alphabet=set(alphabet)
    return alphabet<=set(str1.lower())
a=input("Enter a sentence:")
print(ispangram(a))
