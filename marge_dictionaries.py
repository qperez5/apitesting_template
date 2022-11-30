dictionary1 = {1: "Ana", 2: "Edith", 3: "Rachel"}
dictionary2 = {4: "Pri", 5: "Ines", 6: "Gus"}

dictionary1.update(dictionary2)
print("Dictionary 1 merged: ", dictionary1)

dictionary3 = {**dictionary1, **dictionary2}

print("dictionary 3: ", dictionary3)
