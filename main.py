print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n = 1  # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n += 1
#     if takrorlash != "ha":
#         break
# print("Do'stlaringiz ro'yxati: ")
# for ism in ismlar:
#     print(ism.title())
    
    
    
# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# n = 1
# while ishora:
#     ism = input(f"{n} - do'stingiz ismini kiriting: ")
#     yosh = int(input(f"{ism.title()}ning yoshini kiriting: "))
#     dostlar[ism] = yosh
#     n+=1
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob != "ha":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")
    
    
    
# cars = ["lacetti", "nexia", "toyota", "nexia", "audi", "malibu", "nexia", "lacetti"]
# car = "lacetti"
# car2 = "nexia"
# while car in cars:
#     cars.remove(car)
#     cars.remove(car2)
    
# print(cars)


talabalar = ["hasan", "husan", "olim", "botir"]
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = int(baho)



# masala
# talabalar1 = {
#     'id12345': 'ali hakimov',
#     }
