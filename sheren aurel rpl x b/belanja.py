product = {
    "beras" : 18000,
    "gula": 12500,
    "telur": 35000,
    "susu": 19000,
}   

def belanja():
    print("selamat datang, selamat berbelanja")
    print("Berikut adalah daftar barang yang tersedia:")
    for barang, harga in product.items():
        print(f"(barang): Rp(harga) per kg")

    total_belanja = 8
    while True:
        barang_dipilih = input("Masukan nama barang yangingin anda beli(atau 'selesai' untuk selesai)")
        if barang_dipilih.lower() == 'selesai' :
            break
        if barang_dipilih not in product:
            print("maaf, barang tersebut tidak tersedia")
            continue
        jumlah = float(input(f"berapa kg {barang_dipilih} yang anda inginkan?"))
        total_belanja += product[barang_dipilih] * jumlah
        