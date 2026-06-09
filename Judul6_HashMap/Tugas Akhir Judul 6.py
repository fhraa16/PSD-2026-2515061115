class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2

class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY

class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nStatus Ruangan:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"({self.table[i].key},{self.table[i].value})")

def main():
    hashmap = HashMapOpenAddressing()
    hashmap.insert(1, "Tersedia")
    hashmap.insert(3, "Dipakai")
    hashmap.insert(5, "Terreservasi")
    hashmap.insert(6, "Dipakai")
    hashmap.insert(7, "Tersedia")
    hashmap.insert(8, "Terreservasi")
    hashmap.display()
    
    pilih = 0 
    while pilih != 3 :
        print("\nMenu Status Ketersediaan Ruangan:")
        print("1. Cari Ruangan")
        print("2. Hapus Ruangan")
        print("3. Keluar")
        try:
            pilih = int(input("Masukkan pilihan: "))
        except ValueError:
            print("\nInput tidak valid!")
            continue
            
        if pilih == 1:
            hasil = input("Masukkan nomor ruangan yang ingin dicari: ")
            hasil = hashmap.search(int(hasil))
            if hasil is not None:
                print(f"\nRuangan {hasil.key} ditemukan, status = {hasil.value}")
            else:
                print(f"\nRuangan tidak ditemukan/maintenance")
                
        elif pilih == 2:
            hasil = input("Masukkan nomor ruangan yang ingin dihapus: ")
            if hashmap.remove_key(int(hasil)):
                print(f"\nRuangan {hasil} berhasil dihapus")
            else:
                print(f"\nRuangan tidak ditemukan/maintenance")
            print("\nSetelah menghapus ruangan:")
            hashmap.display()
            
        elif pilih == 3:
                print("\nKeluar dari program.")
        else:
                print("\nPilihan tidak valid. Silakan coba lagi.")

   
if __name__ == "__main__":
    main()
