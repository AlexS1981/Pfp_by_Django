import json

f = open("virtual_city_data.json", 'r')
file_data = json.loads(f.read())
f.close()
# print(file_data)
# a = file_data.get("провулок Діївський, 7")
# print(a)
str1 = "{\n"
for i in file_data:
    str1 += '\t"' + i + '": ' + str(file_data.get(i)) + ',\n'
    list1 = file_data.get(i)
    print(list1[1])
str1 += "}"

# f = open("virtual_city_data.json", 'w')
# f.write(str1)
# f.close()
