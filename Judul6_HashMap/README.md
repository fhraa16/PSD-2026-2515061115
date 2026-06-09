# Status Ketersediaan Ruangan

Program ini merupakan program sederhana untuk mengelola status ketersediaan ruangan ke dalam suatu daftar, yang mana di daftar tersebut berisi nomor ruangan serta status ruangannya seperti "Tersedia", "Dipakai", atau "Terreservasi".
Di program ini, user dapat mencari status ruangan, menghapus data ruangan tertentu berdasarkan nomornya, dan melihat keseluruhan status yang ada, yang mana program ini hanya menampung 10 ruangan aja.
Program ini menggunakan metode HashMap Open Addresing dengan startegi Linear Probing, metode ini itu akan memetakan data ruangan ke dalam daftar di mana urutan indeksnya ditentukan oleh fungsi hash dari nomor ruangan tersebut. 
Program ini juga menggunakan jenis Open Addressing karena memiliki tiga status slot yang jelas yaitu empty, occupied, dan deleted, sehingga memastikan setiap indeks hanya memuat satu informasi ruangan saja untuk mengurangi adanya collision sekaligus menjaga proses pencarian tetap lancar meskipun ada data di baris tengah yang baru saja dihapus.

Nah untuk alur jalannya program, sistem ini itu menggunakan perulangan while untuk menampilkan menu utama secara terus-menerus dan mengantisipasi adanya pilihan input dari user yang tidak sesuai dengan yang diarahkan.
Di dalam perulangan tersebut, terdapat manajemen error yaitu try-except yang digunakan untuk memastikan tipe data input menu dari user berupa angka bulat, sehingga jika terjadi kesalahan tipe data, program tidak akan crash melainkan menampilkan pesan peringatan secara berulang-ulang sampai user memasukkan input yang benar.
Selain while, terdapat perulangan for yang digunakan di dalam fungsi hashmap untuk melakukan probing atau pergeseran indeks satu demi satu secara berurutan saat proses memasukkan data, menghapus data, maupun saat mengecek data ruangan untuk menemukan nomor ruangan yang dicari.
Program ini juga mengandalkan struktur percabangan if, elif, dan else yang digunakan untuk menentukan keputusan perilaku sistem, baik dalam memilih menu aksi yang diinginkan user maupun dalam mendeteksi status slot memori apakah sedang kosong atau terisi.

## Source Code
<img width="225" height="82" alt="image" src="https://github.com/user-attachments/assets/863c0eaa-48ee-4156-afdb-0272c9b42f64" />

Baris 1-4 terdapat class SlotState yang berguna untuk mendeklarasikan nilai EMPTY(2), OCCUPIED(3), dan DELETED(4)

<img width="388" height="103" alt="image" src="https://github.com/user-attachments/assets/7b4a042d-d4c9-4a4a-a917-1e753492db8d" />

Baris 6-10 terdapat class Entry, yang berfungsi untuk mengosongkan key dan value sehingga status awalnya nanti akan menjadi SlotState.EMPTY

<img width="639" height="137" alt="image" src="https://github.com/user-attachments/assets/927ce0d6-d8d4-4a24-9f1d-d96a0e307534" />

Baris 12 ini berfungsi untuk mendeklarifisikan kelas utama hash Map yang di dalamnya ada

Baris 13 ada konstruktor

Baris 14 self.SIZE yang berguna untuk menentukan kapasitas maksimal tabel

Baris 15 ini untuk membuat deretan objek Entry kosong sebanyak ukuran SIZE menggunakan teknik list comprehension.

Baris 17 terdapat fungsi hash function yang mana digunakan untuk mengubah key menjadi nilai tertentu yang akan menjadi indeks untuk menyimpan data key

Baris 18, merupakan pengembalian nilai berupa hasil perubahan key menjadi suatu angka indeks

<img width="1069" height="478" alt="image" src="https://github.com/user-attachments/assets/b5e56b9a-2f75-45cb-b834-5bf27000207f" />

Baris 20–22, Menghitung indeks awal (idx) menggunakan fungsi hash. Variabel first_deleted diset awal -1, gunanya untuk mencatat indeks berstatus DELETED pertama yang ditemui selama perjalanan mencari slot kosong.

Baris 23–24, Melakukan perulangan (looping for) maksimal sebanyak ukuran tabel untuk menerapkan metode Linear Probing. Variabel i akan bergeser satu demi satu dari indeks awal jika terjadi tabrakan data (collision). Rumus % self.SIZE memastikan pencarian berputar kembali ke indeks 0 jika pergeseran sudah mentok di ujung tabel.

Baris 25–28: Jika slot yang diperiksa statusnya OCCUPIED dan ternyata nomor kuncinya (key) sama dengan yang ingin dimasukkan, maka sistem akan memperbarui status ruangan lamanya dengan value yang baru, lalu mengembalikan nilai True.

Baris 29–31, Jika slot berstatus DELETED dan variabel first_deleted masih -1, maka indeks i tersebut disimpan ke dalam first_deleted. Slot bekas hapus ini ditandai agar nantinya bisa kita pakai ulang untuk menaruh data baru demi menghemat ruang memori.

Baris 32–39, else ini dipicu jika slot berstatus EMPTY. Sebelum menaruh data, program mengecek dulu, jika sebelumnya kita sempat melewati slot DELETE, maka data ruangan baru akan dialihkan untuk menduduki slot bekas hapus tersebut. Setelah itu, nomor ruangan dimasukkan, status ketersediaan ditulis, status slot diubah menjadi OCCUPIED, dan fungsi mengembalikan nilai True.

Baris 40–45, Jika perulangan selesai dan tabel ternyata penuh, program melakukan pengecekan terakhir. Jika ada slot bekas hapus yang tersimpan di first_deleted, data akan dimasukkan ke sana. Namun jika benar-benar penuh total, fungsi mengembalikan nilai False.

<img width="889" height="174" alt="image" src="https://github.com/user-attachments/assets/965d7273-e093-44c4-9c15-1fdb64af3108" />

Baris 46–49, Menghitung letak indeks tebakan awal, lalu melakukan perulangan linear probing untuk mencari letak data ruangan yang diminta.

Baris 50–54, Jika di tengah jalan program menemui slot EMPTY, proses pencarian langsung dihentikan dan menghasilkan None, karena secara teori open addressing, jika data itu ada, ia tidak mungkin melompati slot kosong. Jika slot berstatus OCCUPIED dan nomor kuncinya cocok dengan target, objek data ruangan tersebut langsung dikembalikan.

<img width="756" height="119" alt="image" src="https://github.com/user-attachments/assets/a8249d24-6f94-4e19-9b1b-7757c58a6d1e" />

Baris 56–61, Memanggil fungsi search(key) untuk menemukan ruangan yang mau dihapus. Jika hasilnya None, fungsi mengembalikan False. Jika ketemu, program tidak mengosongkan objek menjadi None, melainkan hanya mengubah status slotnya menjadi SlotState.DELETED agar rantai pencarian probing pada fungsi search tidak terputus.

<img width="853" height="197" alt="image" src="https://github.com/user-attachments/assets/e735b1bf-ac13-4ef1-8b03-fb691da0663c" />

Baris 63-66, Mencetak judul tabel, lalu melakukan perulangan untuk menelusuri isi daftar dari indeks ke-0 sampai ke-9. 

Baris 67-72, Melakukan pengecekan kondisi jika slot kosong dicetak EMPTY, jika telah terhapus dicetak DELETED, dan jika berisi data aktif maka dicetak berupa pasangan (Nomor Ruangan, Status Ruangan).

<img width="694" height="177" alt="image" src="https://github.com/user-attachments/assets/279b0650-dd1a-4ac0-befc-2edd6e497f14" />

Baris 76–82, Membuat objek tabel hash map baru bernama hashmap. Melakukan pengisian data awal untuk beberapa ruangan beserta statusnya, lalu memanggil fungsi display() untuk memunculkan tabel awal di terminal.

<img width="764" height="207" alt="image" src="https://github.com/user-attachments/assets/e81fc5d9-aedb-4a65-8d29-007ad9231cd2" />

Baris 84–89 Menginisialisasi variabel kontrol menu pilih = 0. Menggunakan struktur perulangan while yang akan terus menampilkan pilihan menu interaktif selama user tidak memilih angka 3.

Baris 90-94 bentuk try except yang berguna untuk menghindari error saat user salah masukin inputan.

<img width="810" height="140" alt="image" src="https://github.com/user-attachments/assets/5d1db0d7-5a42-4e67-92c4-9db5486adc00" />

Baris 96-102, Jika memilih menu 1, program meminta input nomor ruangan yang dicari, lalu memanggil fungsi hashmap.search(int(hasil)). Menggunakan percabangan if-else untuk mengecek hasil kembalian: jika tidak None maka informasi ruangan dicetak, jika None dimunculkan pesan tidak ditemukan.

<img width="741" height="159" alt="image" src="https://github.com/user-attachments/assets/8434b8e8-d7e9-48e8-aedf-f4cd5273adc9" />

Baris 104-111, Jika memilih menu 2, program meminta input nomor ruangan yang ingin dihapus, lalu mengecek fungsi hashmap.remove_key(int(hasil)). Jika bernilai True dicetak pesan sukses, jika False dicetak pesan gagal. Di akhir aksi, kondisi tabel terbaru langsung dipanggil lewat hashmap.display().

<img width="761" height="81" alt="image" src="https://github.com/user-attachments/assets/f68b97eb-3a97-4bda-88ee-dcfe97bd4585" />

Baris 113-116, Jika memilih menu 3, program menampilkan teks penutup dan otomatis keluar dari perulangan while. Blok else terakhir menangani situasi jika user memasukkan angka selain angka 1, 2, atau 3. 

<img width="332" height="43" alt="image" src="https://github.com/user-attachments/assets/7835b2c0-3e64-4743-bff5-a028a0e80aaa" />

Baris 119-120, Blok standar di Python untuk memastikan bahwa fungsi main() hanya akan dieksekusi secara otomatis jika file skrip ini dijalankan secara langsung.

## Output Program

<img width="599" height="555" alt="image" src="https://github.com/user-attachments/assets/a0a9328e-65d7-4da0-8114-779571dcd016" />

Ini hasil dari saat user memilih menu 1 yaitu mencari ruangan, dan memasukkan ruangan 5 yang statusnya adalah terreservasi.

<img width="720" height="242" alt="image" src="https://github.com/user-attachments/assets/02b14e98-06d5-475c-a290-ef6f9766b6dd" />

Ini jika user mencari ruangan yang tidak ada, maka akan menampilkan ruangan tidak tersedia/maintenance.

<img width="830" height="593" alt="image" src="https://github.com/user-attachments/assets/8b05e1f1-41a2-4add-9de3-b1b9d7ebeb07" />

Ini jika user memilih menu 2 yang mana menu tersebut adalah menu buat menghapus ruangan, dan di sini user mau menghapus ruangan 5.
Jadi setelah penghapusan ruangan berhasil, maka program akan otomatis menampilkan tabel terbaru.

<img width="742" height="605" alt="image" src="https://github.com/user-attachments/assets/463c75ee-8b5c-4235-99d5-0de4d42596e5" />

Akan tetapi, jika user memasukkan ruangan kosong ke dalam ruangan yang mau dihapus. 
Maka program akan menampilkan pesan ruangan tidak tersedia/maintenance

<img width="602" height="197" alt="image" src="https://github.com/user-attachments/assets/52ed9596-c5f9-40b7-ad0a-8e7c27c7dca0" />

Jika user sudah selesai dengan ruangan yang ingin dicari, maka user akan memilih menu 3, yaitu menu selesai.

## Link YT

https://youtu.be/LUYQeOsw10o
