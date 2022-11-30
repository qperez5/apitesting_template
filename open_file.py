pf = open("testtext.txt", "r")

data = pf.read()

lines = data.split('/n')

for line in lines:
    words = line.split(" ")

    for word in words:
        print(word)

pf.close()