# list1 = ["chemistry", "physics", "chemistry", "PHYSICS"]
# print(list1)
# print (list1[7]) 1
# error karena list index out of range

# list1[7] = "mathematics" 2
# error karena list index out of range

# list1[1:5] = ["biology", "english"] 3

# print(list1)
# jika diprint hasilnya hanya chemistry, biology, english

# list1.insert(2, "biology")
# print (list1)
# chemis, physics, bio, chemis, chemis, Physics

dict = {'Course': 'PemLan', 'Code': 'CCE61207', 'Credit': 4}
print(dict)

dict[0] = 'NewCode'
print("dict['Code']: ", dict[0])
print(dict)
