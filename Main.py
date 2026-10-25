print("bilgi yarismasina hosgeldin!")

isim = input("adin ne!")

puan = 0

print("turkiyenin baskenti neresidir!")

cevap = input("cevabin :").strip().lower()

if cevap == "ankara":
    print("dogru cevap!")
    puan += 10

else:
    print("yanlis! dogru cevap ankara!")

print(f"{isim},toplam puanin: {puan}")    