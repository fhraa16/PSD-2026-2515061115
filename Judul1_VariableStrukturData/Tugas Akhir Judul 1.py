print("=================================================")
print("Tugas Akhir Judul 1 - List 1D")
print("=================================================")

def menu():
    print("\n---- SISTEM ABSENSI SISWA ----")
    print("1. Masukkan nama siswa")
    print("2. Tampilkan address list kehadiran siswa")
    print("3. Tampilkan detail id dari setiap nama siswa")    
    print("4. Keluar")
    
def main():
    daftar_siswa = []
    while True:
        menu()
        try:
            pilihan = int(input("Pilih opsi: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        
        if pilihan == 1:
            nama = input("Masukkan nama siswa: ")
            daftar_siswa.append(nama)
            print(f"{nama} telah ditambahkan.")
        elif pilihan == 2:
            print(f"Address list kehadiran siswa: {id(daftar_siswa)}")
        elif pilihan == 3:
            if daftar_siswa:
                print("Detail id dari setiap nama siswa:")
                for idx, siswa in enumerate(daftar_siswa, start=1):
                    print(f"{idx}. id {siswa}: {id(siswa)}")
            else:
                print("Belum ada siswa yang diabsen.")
        elif pilihan == 4:
            print("Absensi telah selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
            
if __name__ == "__main__":
    main()