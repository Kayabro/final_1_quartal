list_1 = ["hello", "2,", "world", ';-)']
list_2 = []
for i in list_1:
  if len(i) <= 3:
    list_2.append(i)
print(list_2)