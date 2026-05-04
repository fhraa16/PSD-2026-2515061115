print("===========================")
print("Tugas Akhir PSD - Judul 2")
print("===========================")

def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

print("PROGRAM PENGECEKAN BERAT BADAN ANAK DI POSYANDU CERIA")
print("--------------------------------------------------------")

def main():
    print("Selamat Datang di Posyandu Ceria!")

    try:
        n = int(input("Masukkan jumlah balita yang akan dicatat: "))
        if n <= 0:
            print("Jumlah balita tidak boleh kurang dari atau sama dengan 0.")
            return
    except ValueError:
        print("Input tidak valid! Harap masukkan angka bulat.")
        return
        
    arr = []
    print("\nMasukkan berat badan balita:")
    for i in range(n):
        while True:
            try:
                nilai = float(input(f"Berat badan balita ke-{i+1}: "))
                arr.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
                
    print(f"\nBerat badan sebelum diurutkan: {arr}")
    
    insertion_sort(arr, n)
    
    print("\nBerat badan dari yang terkecil hingga terbesar:")
    for i in range(n):
        print(f"{i+1}. {arr[i]} kg")

if __name__ == "__main__":
    main()