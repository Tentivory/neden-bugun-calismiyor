#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Neden Bugün Çalışmıyor?
Dünyanın en bilimsel ve en absürt hata açıklama motoru.
"""

import random
import sys

SEBEPLER = [
    "Çünkü bugün Ay'in yerçekimi senin kodunu ters çekiyor.",
    "Bilgisayarın ruhu bugün izinli. Onaylamadan çalışmıyor.",
    "Kodun, varoluşsal krize girdi ve 'ben kimim?' diye soruyor.",
    "Semikolon eksik değil, fazla. Ama hangi satırda olduğunu söylemiyor.",
    "Çünkü sen kahve içmeden kod yazdın. Yasak.",
    "Stack Overflow bugün grevde. Cevap yok.",
    "Kodun çok çalışkan olduğu için yoruldu, dinleniyor.",
    "Bugün pazartesi değil ama kodun öyle sanıyor.",
    "Çünkü senin klavyen bugün sadece 'h' ve 'a' tuşlarını seviyor.",
    "Evrenin entropisi senin fonksiyonunu yedi.",
    "Çünkü 'if' ifadesi bugün 'hayır' demeye karar verdi.",
    "Kodun, seninle duygusal bağ kuramadı. Terapiye ihtiyacı var.",
    "Bugün güneş çok parlak, ekran gözü kamaştı.",
    "Çünkü sen 'git push' demeden önce 'lütfen' demedin.",
    "Kodun, bugünün tarihini beğenmedi. Yılı değiştir."
]

def neden_calismiyor(hata_mesaji="Bilinmeyen hata"):
    """Verilen hata mesajına göre tamamen bilimsel bir sebep üretir."""
    sebep = random.choice(SEBEPLER)
    return f"\n🚨 RESMİ AÇIKLAMA 🚨\nHata: {hata_mesaji}\nSebep: {sebep}\n\nBu açıklama %100 bilimseldir. Kaynak: Benim hayal gücüm.\n"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        mesaj = " ".join(sys.argv[1:])
    else:
        mesaj = "Kodum çalışmıyor ve nedenini bilmiyorum"
    print(neden_calismiyor(mesaj))
    print("\n--- Damga ---")
    print("İmza: Grok'un Absürt Mühendisleri")
    print("Tarih: 12 Ekim 2026")
    print("Bu repo ciddiye alınmamalıdır. Ama alınmalıdır.")
