from splitwise_api import SplitwiseConnect

toby_splitwise = SplitwiseConnect(1)
rishin_splitwise = SplitwiseConnect(2)
hamzah_splitwise = SplitwiseConnect(3)
mary_splitwise = SplitwiseConnect(4)

getInfo = lambda f: f.id

print(list(map(getInfo,toby_splitwise.getFriends())))
print(list(map(getInfo,rishin_splitwise.getFriends())))
print(list(map(getInfo,hamzah_splitwise.getFriends())))
print(list(map(getInfo,mary_splitwise.getFriends())))
print(toby_splitwise.getCurrentUser().id)