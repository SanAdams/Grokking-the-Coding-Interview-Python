# So what happens if I want to use the %= operator and subtact from something afterwards. Can I do that in one line?
def reset():
    global x
    x = 7
    global y
    y = 6

reset()
x %= y - 1
print(x) # I expect 0
         # Actual result: 2, because subtraction happens first. 7 % 5 = 2


reset()
x %= y
x -= 1
print(x) # I expect 0
         # Actual result: 0

# Looks like whatever I wanted to do can't be done in Python