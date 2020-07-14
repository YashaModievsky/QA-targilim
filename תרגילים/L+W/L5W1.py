lenght = int(input("enter you desired lenght: "))
width = int(input("enter your desired width: "))

L = "* "
W = "*"
print(L*lenght)
for i in range(width-2):
    print(W, ("  ")*(lenght*2-3),W, sep='')
print(L*lenght)
