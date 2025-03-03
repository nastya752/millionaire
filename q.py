text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent eget tortor maximus ante pretium rhoncus et a diam.")
list = ["a","e","y","u","o","i"]
a = 0
i = 0
o = 0
e = 0
y = 0
u = 0
id = 0
for i in text:
    if i in list:
        if i=="a":
            a+=1
        if i == "e":
            e += 1
        if i == "y":
            y += 1
        if i == "o":
            o += 1
        if i== "i":
            id += 1
        if i == "u":
            u += 1
print(a,y,u,id,o,e)

