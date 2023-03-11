MIN_NAR_DEGERİ = 1000

soru = "e"

# DEĞİŞKEN TANIMLAMALARI:
h_nar_sayi = 0
d_nar_sayi = 0
h_top_tane_say = 0
d_top_tane_say = 0
d_max_degerli = 0  # Deve dişi çeşidinde toplam tane sayısı 1000 üstünde olan narların sayısını hesaplamak için atama
h_max_degerli = 0  # Hicaz çeşidinde toplam tane sayısı 1000 üstünde olan narların sayısını hesaplamak için atama
curuk_olmayan_nar = 0

while soru == "e":
    nar_cesit = input("Kasadaki bir narın çeşidini (h/d) şeklinde giriniz:(h:hicaz nar çeşidi, d:deve dişi nar çeşidi)")

    if nar_cesit == "h":  # "h" harfi hicaz çeşidini belirtiyor.
        h_saglam_tane = int(input("Hicaz çeşidi narın sağlam tane sayısını giriniz:"))
        h_curuk_tane = int(input("Hicaz çeşidi narın çürük tane sayısını giriniz:"))

        if h_curuk_tane == 0:
            curuk_olmayan_nar += 1

        h_nar_sayi += 1
        h_top_tane = h_saglam_tane + h_curuk_tane
        h_saglam_yuzde = h_saglam_tane / h_top_tane * 100  # Yüzde hesaplamak için gerekli formül yazımı
        h_top_tane_say += h_top_tane

        print("Bu narın sağlam tane yüzdesi : %{:.2f}".format(h_saglam_yuzde))

        if h_top_tane >= MIN_NAR_DEGERİ:
            h_max_degerli += 1
            print("Bu nar için bilmecenin cevabı doğrudur.")
        else:
            print("Bu nar için bilmecenin cevabı yanlıştır.")

        if h_max_degerli >= h_nar_sayi / 2:
            h_cevap = "Hicaz nar çeşidi için bilmecenin cevabı doğrudur."
        else:
            h_cevap = "Hicaz nar çeşidi için bilmecenin cevabı yanlıştır."

    if nar_cesit == "d":  # "d" harfi deve dişi çeşidini belirtiyor.

        d_sag_tane = int(input("Deve dişi çeşidi narın sağlam tane sayısını giriniz:"))
        d_curuk_tane = int(input("Deve dişi çeşidi narın çürük tane sayısını giriniz:"))

        if d_curuk_tane == 0:
            curuk_olmayan_nar += 1
        d_nar_sayi += 1
        d_top_tane = d_sag_tane + d_curuk_tane
        d_saglam_yuzde = d_sag_tane / (d_curuk_tane + d_sag_tane) * 100  # Yüzde hesaplamak için gerekli formül yazımı
        d_top_tane_say += d_top_tane

        print("Bu narın sağlam tane yüzdesi : %{:.2f}".format(d_saglam_yuzde))

        if d_top_tane >= MIN_NAR_DEGERİ:
            d_max_degerli += 1
            print("Bu nar için bilmecenin cevabı doğrudur.")
        else:
            print("Bu nar için bilmecenin cevabı yanlıştır.")

        if d_max_degerli >= d_nar_sayi / 2:
            d_cevap = "Deve dişi nar çeşidi için bilmecenin cevabı doğrudur."
        else:
            d_cevap = "Deve dişi nar çeşidi için bilmecenin cevabı yanlıştır."

    soru = input("Kasada başka nar var mı? (e/h) cinsinden giriniz:")

# Problem çözümü için gerekli hesaplama değerleri
toplam_nar_say = h_nar_sayi + d_nar_sayi
toplam_tane_say = h_top_tane_say + d_top_tane_say
hicaz_tane_say_ort = h_top_tane_say / h_nar_sayi
deve_dis_tane_say_ort = d_top_tane_say / d_nar_sayi
tum_nar_ort = toplam_tane_say / toplam_nar_say
curuk_olmayan_nar_yuzde = curuk_olmayan_nar / toplam_nar_say * 100

print("Hicaz çeşidi narlar için tane sayısı ortalaması:{:.2f}".format(hicaz_tane_say_ort))
print("Deve dişi çeşidi narlar için tane sayısı ortalaması:{:.2f}".format(deve_dis_tane_say_ort))
print("Tüm narlar için tane sayısı ortalaması:{:.2f}".format(tum_nar_ort))
print("Hiç çürük tanesi olmayan narların yüzdesi: %{}".format(curuk_olmayan_nar_yuzde))
print(h_cevap)
print(d_cevap)
