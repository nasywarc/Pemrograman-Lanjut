# PROGRAM 2 (Online Pymart)
# Nama    : Nasywa Azizah Zharifah
# NIM     : 225150307111060

# mendeklarasikan harga setiap barang yang dijual
bread = 17000
noodle = 5000
spaghetti = 8000
sausage = 30000
chicken = 10000
apple = 16000
banana = 9000
orange_juice = 12000

# mengambil input sebagai nama pelanggan
name = str(input("Welcome to Pymart. Please enter your name.\n"))

# mengoutputkan kembali nama pelanggan
print("\nHappy shopping, " + name +".")
# menjelaskan cara kerja program pada pelanggan
print("Please enter the quantity of items in the input column for the items you want.\n")

# mengambil input sebagai jumlah item sesuai barang yang ingin dibeli
apple_quant = int(input("How many apples do you want?\n"))
banana_quant = int(input("How many bananas do you want?\n"))
bread_quant = int(input("How many pieces of bread do you want?\n"))
chicken_quant = int(input("How many chickens do you want?\n"))
noodle_quant = int(input("How much noodles do you want?\n"))
or_juice_quant = int(input("How much orange juice do you want?\n"))
sausage_quant = int(input("How many sausages do you want?\n"))
spaghetti_quant = int(input("How much spaghetti do you want?\n"))

# mengambil input pelanggan sebagai jumlah persen total belanja mereka sebagai donasi
donation_percent = int(input("\nYour donation is very valuable to us.\nWhat percentage of your total purchase price would you like to contribute as a donation?\n"))

# seolah olah program sedang mengkalkulasi tagihan
print("\nCalculating your bill..\n")

# menghitung total belanja pelanggan dengan mengalikan jumlah item dengan harga item
total = (apple * apple_quant) + (banana * banana_quant) + (bread * bread_quant) + (chicken * chicken_quant) + (noodle * noodle_quant) + (orange_juice * or_juice_quant) + (sausage * sausage_quant) + (spaghetti * spaghetti_quant)
# menghitung total donasi pelanggan dengan mengalikan total dengan jumlah donasi/100
donation = total * (donation_percent/100)
# menambahkan jumlah total dengan jumlah donasi dalam bentuk float
total_donation = float(total + donation)

# mengoutputkan jumlah total ditambah donasi kepada pelanggan
print("Your total purchase is " + "Rp"+ str(total_donation))

# mengoutputkan tipe data dari jumlah total+donasi pelanggan
print("\nYour total donation data type is ", type(total_donation))
# mengoutputkan ucapan terima kasih kepada pelanggan beserta namanya
print("Thank you for shopping, " + name + ".\n")