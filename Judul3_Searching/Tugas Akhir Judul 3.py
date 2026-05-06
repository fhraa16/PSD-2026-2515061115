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
    arr = [5, 7, 10, 12, 15, 18, 22, 25]
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
    if pos == 0 or pos == 1 or pos == 2 or pos == 3:
        baris = "Depan"
    else:
        if pos == 4 or pos == 5 or pos == 6 or pos == 7:
            baris = "Belakang"
    if pos != -1:
        print(f"Nomor kursi {target} Ditemukan pada indeks ke-{pos} di area {baris}")
    else:
        print("Tidak ditemukan")
        
if __name__ == "__main__":
    main()