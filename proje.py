print("Karanlık bir ormandasınız. Yol ikiye ayrılıyor: Sol veya Sağ?")
secim = input("Hangi yöne gidersiniz? (sol/sag): ").lower()
if secim == "sol":
    print("Karşınıza dost canlısı bir büyücü çıktı ve size bir harita verdi. Kazandınız!")
if secim == "sağ":
    print("Bir canavarla karşılaştınız ve kaçamadınız. Oyun bitti!")
