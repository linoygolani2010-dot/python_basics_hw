num = int(input("enter a decimal number: "))
length = int(input("enter the memory size: in bits: "))

def decimal_to_binary(num, length):
    x = []
    while num > 0:
        temp = num %2
        x.insert(0,temp)
        num = num // 2

    if length > len(x):
        for i in range(length - len(x)):
            x.insert(0, 0)
    return x

x = decimal_to_binary(num, length)

y=x.copy()

for i in range(len(y)):
    if y[i] == 0:
        y[i] = 1
    else:
        y[i] = 0
for i in reversed(range(len(y))):
      if y[i] == 0:
          y[i] = 1
          break
      else:
        y[i] = 0

binary_string = ""
for i in range(len(y)):
    binary_string  += str(y[i])


print("The negative binary representation of the number is: ", binary_string)
