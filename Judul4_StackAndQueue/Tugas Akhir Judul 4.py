print("-----------------------")
print("--Tugas Akkhir Judul 4--")
print ("----------------------")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None
        self.count = 0

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, x):
        if self.count >= 7:
            print("Antrian sudah padat!")
            lanjut = input("Apakah tetap ingin mengambil antrian? (y/n): ")
            if lanjut.lower() != 'y':
                print("Pengambilan antrian dibatalkan.")
                return
        new_node = Node(x)
        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node
        self.count += 1
        print(f"Antrian {x} berhasil ditambahkan")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        temp = self.front_ptr
        print(f"Antrian {temp.data} silakan ke teller/cs")
        self.front_ptr = self.front_ptr.next
        if self.front_ptr is None:
            self.rear_ptr = None
        self.count -= 1

    def peek(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print(f"Antrian depan: {self.front_ptr.data}")

    def display(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print("Isi antrian (depan ke belakang): ", end="")
        current = self.front_ptr
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()
        if self.count > 7:
            print("Status Padat")
        else:
            print("Status Lancar")

def main():
    queue = QueueLinkedList()
    pilih = 0
    while pilih != 5:
        print("\n=== Antrian Bank Bahagia ===")
        print("1. Tambah Antrian")
        print("2. Hapus Antrian")
        print("3. Lihat Antrian Depan")
        print("4. Tampilkan Antrian")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        
        if pilih == 1:
            val = input("Masukkan Nama Anda: ")
            queue.enqueue(val)
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            while not queue.is_empty():
                queue.dequeue()
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
