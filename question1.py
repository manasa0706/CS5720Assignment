import random
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
  
s = input("enter your string atleast 5 characters")
  
print("The original string is : ", end="")
print(s)
res_str = s[:2] +  s[3:]
res = res_str[:2] +  res_str[3:]

print("The reversed string(using loops) is : ", end="")
print(reverse(res))