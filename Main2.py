print("bilgi yarismasina hosgeldiniz!")

isim = input("oyuncunun adi:")

puan = 0

sorular = [
    ["osmanlinin baskenti neresiydi?", istanbul] ,
    ["bir haftada kac saat vardir? ","168"]
    ["python da ekrana yazi yazdiran fonksiyon nedir","print"]
    ["dunyanin dogal uydusu nedir ?","ay"]
]

for soru in sorular
    print("\n"+soru[0])
    cevap = input("cevabin : ").strip().lower()

    if cevap == soru[1]:
        print("dogru!" + 10 puan kazandin!)
        puan+10
    else:
        print(f"yanlis! dogru cevap: {soru[1]}")

maksimum_puan = len(sorular)*10

print(f"\n tebrikler {isim}, yarismayi tamamladin!")

print(f"puanin: {puan}/{maksimum_puan}")