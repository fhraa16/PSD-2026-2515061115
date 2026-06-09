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

Baris 1-4 terdapat class SlotState yang bergna untuk mendeklarasikan nilai EMPTY(2), OCCUPIED(3), dan DELETED(4)

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

Baris 20, terdapat fungsi insert yang berguna untuk menambahkan data ke daftar yanag mana fungsi ini mencakup baris 21-44.

Baris 21, terdapat variabel idx yang akan menyimpan hasil hash function dengan memanggil fungsi tersebut.

baris 22, terdapat variabel yang menyatakan bahwa aksi deleted pertama bernilai -1 atau belum pernah di lakukan.

Baris 23, terdapat perulangan for yang akan di gunakan untuk memeriksa seluruh tempat atau daftar, perulangan ini mencakup baris 24-38.

Baris 24, terdapat variabel i yang menyimpan nilai yang digunakan untuk memastikan tidak keluar dari jumlah pengecekan

Baris 25, terdapat percabangan if dengan kondisi jika table dengan indeks ke i tersebut telah terisi maka akan mengeksekusi baris 21-38

Baris 28, terdapat percabangan kembali dimana jika key dari data indeks table ke i sama dengan key yang dimasukkan user maka akan mengeksekusi baris 29-30 akan di eksekusi dimaana baris 29 akan mengganti value data sebelumnya pada indeks tabel tersebut dengan value baru yang di masukkan oleh user dan mengembalikan niLai True (30)

baris 31 merupakan lanjutan dari kondisi pada baris 27 yang mana jika data dari tabel indeks ke i ternyata pernah di hapus sebelumnya maka baris 32-33 akan diekseksui

baris 32 terdapat percabangan dimana jika first deleted pada saat itu bernilai -1 maka akan mengeksekusi baris 33 yang akan menggantikan nilai firts deleted dengan nilai dari i

baris 34, merupakan lanjutan dari percabangan sebelumnya di baris 31 yang mana akan dijalankan jika kondisi kedua percabangan sebelumnya tidak terpenuhi maka akan mengeksekusi baris 35-40

baris 35, merupakan percabangan baru dimana jika first deleted tidak bernilai -1 maka akan mengeksekusi baris 36 yang mana merubah nilai i menjadi nilai first deleted

baris 37, merupakan pergantian nilai key pada indeks ke i pada table menjadi nilai key yang di masukkan pengguna, begitu pula pada baris 38 yang mengubah nilai value indeks ke i table menjadi value yang di masukkan oleh user, lalu pada baris 39 merupakan pemberian status bahwa pada indeks tersebut telah menyimpan data, dan pada baris 40 merupakan pengembalian nilai true.

baris 41, akan dikesekusi ketika tidak kondisi percabangan dalam perulangan for telah dieksekusi tanpa ada pengembalian nilai ataupun ketika tidak terpenuhi dan percabangannya tidak memiliki kondisi lain atau 'else'. dimana pada baris ini terdapat percabangan dengan kondisi dimana jika first_deleted bukan bernilai -1 maka akan mengeksekusi baris 42-45

baris 42, merupakan pergantian nilai key pada indeks ke first_deleted dengan nilai key yang dimasukkan user, begitu pula pada baris 43 yang mengganti nilai valuenya dengan value yang di masukkan oleh user, lalu pada baris 44, state pad indeks tersebut akan di berikan status telah diisi lalu dikembalikan nilai True pada baris 45.

baris 46 merupakan pengembalian nilai false ketika tidak ada pengembalian nilai yang di lakukan sebelumnya.

<img width="889" height="174" alt="image" src="https://github.com/user-attachments/assets/965d7273-e093-44c4-9c15-1fdb64af3108" />

baris 48, terdapat fungsi search yang akan di gunakan untuk mencari informasi psaien berdasarkan kode unik dimana mencakup baris 49-56

baris 49, terdapat variabel idx yang akan di gunakan untuk menyimpan hasil nilai function hash dengan memanggil fungsi tersebut

baris 50, terdapat perulangan for yang akan melakukan looping sebanyak jumlah size daftar pasien (yaitu 10), dimana perulangan ini mencakup baris 51-56

baris 51, terdapat variabel i yang menyimpan nilai yang digunakan untuk memastikan tidak keluar dari jumlah pengecekan

baris 52, terdapat percabangan dengan kondisi dimana jika indeks ke i pada table kosong maka akan mengembalikan nilai false dan none (53)

baris 54, terdapat percabangan dengan kondisi jika data pada indeks ke i pada table daftar telah terisi data dan nilai key nya sama dengan yang dimasukkan user maka akan mengeksekusi baris 55 yang akan mengembalikan nilai True dan isi data indeks ke i dari tabel daftar.

<img width="756" height="119" alt="image" src="https://github.com/user-attachments/assets/a8249d24-6f94-4e19-9b1b-7757c58a6d1e" />

baris 58, terdapat fungsi remove untuk menghapus data pada indeks tertentu yang mana fungsi ini mencakup baris 59-63

baris 59, terdapat variabel bool dan entry yang akan menampung pengembalian nilai dari fungsi search yang di panggil

baris 60 terdapat percabangan dimana jika entry bernilai none dan bool bernilai false maka akan mengeksekusi baris 61 yang akan mengembalikan nilai False

baris 62, merupakan pendefinisian bahwa data entry telah dihapus lalu pada baris 63 akan di lakukan pengembalian nilai True.

<img width="853" height="197" alt="image" src="https://github.com/user-attachments/assets/e735b1bf-ac13-4ef1-8b03-fb691da0663c" />

baris 65, terdapat fungsi display yang berguna untuk menampilkan keseluruhan daftar, dimana fungsi ini mencakup baris 66-74

baris 66, akan menampilkan "daftar informasi antrian pasien"

baris 67, terdapat perulanagn for yang mencakup baris 68-74

baris 68, akan menampilkan urutan antrian pada daftar pasien atau table dengan penambahan +1 untuk menghindari antrian 0

baris 69, terdapat percabangan dengan kondisi dimana jika status data pada indeks ke i table sama dengan empty atau kosong maka akan mengekseskusi baris 70 yang mana akan menampilkan empty

baris 71, merupakan lanjutan percabangan sebelumnya dengan kondisi jika status data pada indeks ke i di daftar tabel sama dengan deleted atau telah dihapus sebelumya maka akan mengeksesuki baris 72 yang akan menampilkan "DELETED"

baris 73, merupakan lanjutan dari percabangan sebelumnya dimana jika tidak ada kondisi yang terpenuhi sebelumnya maka akan mengeksekusi baris 74 yang mana akan menampilkan key serta value data dari indeks ke i daftar table.

<img width="694" height="177" alt="image" src="https://github.com/user-attachments/assets/279b0650-dd1a-4ac0-befc-2edd6e497f14" />

baris 76, terdapat fungsi menu mencakup baris 77-81 yang mana berfungsi untuk menampilkan menu berupa apa saja yang user dapat lakukan dengan program ini

<img width="764" height="207" alt="image" src="https://github.com/user-attachments/assets/e81fc5d9-aedb-4a65-8d29-007ad9231cd2" />

Baris 84–89 Menginisialisasi variabel kontrol menu pilih = 0. Menggunakan struktur perulangan while yang akan terus menampilkan pilihan menu interaktif selama user tidak memilih angka 3.

Baris 90-94 bentuk try except yang berguna untuk menghindari error saat user salah masukin inputan.

<img width="810" height="140" alt="image" src="https://github.com/user-attachments/assets/5d1db0d7-5a42-4e67-92c4-9db5486adc00" />

Baris 99–105, Jika memilih menu 1, program meminta input nomor ruangan yang dicari, lalu memanggil fungsi hashmap.search(int(hasil)). Menggunakan percabangan if-else untuk mengecek hasil kembalian: jika tidak None maka informasi ruangan dicetak, jika None dimunculkan pesan tidak ditemukan.

<img width="741" height="159" alt="image" src="https://github.com/user-attachments/assets/8434b8e8-d7e9-48e8-aedf-f4cd5273adc9" />

Baris 107–115, Jika memilih menu 2, program meminta input nomor ruangan yang ingin dihapus, lalu mengecek fungsi hashmap.remove_key(int(hasil)). Jika bernilai True dicetak pesan sukses, jika False dicetak pesan gagal. Di akhir aksi, kondisi tabel terbaru langsung dipanggil lewat hashmap.display().

<img width="761" height="81" alt="image" src="https://github.com/user-attachments/assets/f68b97eb-3a97-4bda-88ee-dcfe97bd4585" />

Baris 117–120: Jika memilih menu 3, program menampilkan teks penutup dan otomatis keluar dari perulangan while. Blok else terakhir menangani situasi jika user memasukkan angka selain angka 1, 2, atau 3. 

<img width="332" height="43" alt="image" src="https://github.com/user-attachments/assets/7835b2c0-3e64-4743-bff5-a028a0e80aaa" />

Baris 119-120, Blok standar di Python untuk memastikan bahwa fungsi main() hanya akan dieksekusi secara otomatis jika file skrip ini dijalankan secara langsung.

## Output Program

## Link YT
