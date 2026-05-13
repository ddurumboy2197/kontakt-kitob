import random

def loto_oyni():
    # 6 ta tasodifiy son olish
    tasodifiy_sonlar = random.sample(range(1, 46), 6)
    print("Tasodifiy sonlar:", tasodifiy_sonlar)

    # Foydalanuvchi tanlagan sonlar
    foydalanuvchi_sonlar = input("6 ta sonni kiriting (bitta sonni bir qatorda kiriting): ").split()

    # Foydalanuvchi sonlarini ro'yxatga aylantirish
    foydalanuvchi_sonlar = [int(son) for son in foydalanuvchi_sonlar]

    # Foydalanuvchi sonlarini tekshirish
    if len(foydanuvchi_sonlar) != 6 or not all(1 <= son <= 46 for son in foydalanuvchi_sonlar):
        print("Xatolik! 6 ta son kiriting va ular 1 dan 46 gacha bo'lishi kerak.")
        return

    # Foydalanuvchi sonlarini tasodifiy sonlar bilan solishtirish
    to'g'ri_sonlar = [son for son in foydalanuvchi_sonlar if son in tasodifiy_sonlar]

    # Natija chiqarish
    print("To'g'ri sonlar:", to'g'ri_sonlar)
    print("Natija:", len(to'g'ri_sonlar))

loto_oyni()
