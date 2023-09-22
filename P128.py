s = ""

f = open("sample2.txt","w")

for i in range(50000):
    str = f"{str},{(50000-i)//2}"
    str = f"{str},{(50000-i)//2+1}"

print(str)
f.write(str)
f.close