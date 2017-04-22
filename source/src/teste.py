from api import ApiSearch

path = int(input("> "))
if path == 1:
    print(ReverseIP("google.com"))
else:
    print(ApiSearch("google.com"))
