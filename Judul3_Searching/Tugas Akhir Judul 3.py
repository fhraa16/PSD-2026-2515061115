print("=========================")
print("Tugas Akhir - Judul 3")
print("==========================")

def binary_search(arr, n, target):
    l = 0
    r = n - 1
    pos = -1
    while l <= r:
        m = l + (r - l) // 2
        print(f"Median: {m}, nilai: {arr[m]}")
        if arr[m] == target:
            pos = m
            break
        elif arr[m] < target:
            print("Mencari di kanan")
            l = m + 1
        else:
            print("Mencari di kiri")
            r = m - 1
    return pos

def main():
    print("-------Mencari Nomor Kursi Bioskop--------")
    arr = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    print(f"Nomor Kursi: {arr}")
    while True:
        try:
            target = int(input("Masukkan nomor kursi yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")
    n = len(arr)
    pos = binary_search(arr, n, target)
    baris = pos 
    if pos <= 4:
        baris = "Depan"
    elif pos > 4 and pos <= 9:
        baris = "Tengah"
    else:
        pos > 9
        baris = "Belakang"
    if pos != -1:
        print(f"Nomor kursi {target} Ditemukan pada indeks ke-{pos} di area {baris}")
    else:
        print("Tidak ditemukan")
        
if __name__ == "__main__":
    main()
