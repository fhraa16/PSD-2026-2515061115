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

<img width="388" height="103" alt="image" src="https://github.com/user-attachments/assets/7b4a042d-d4c9-4a4a-a917-1e753492db8d" />

<img width="639" height="137" alt="image" src="https://github.com/user-attachments/assets/927ce0d6-d8d4-4a24-9f1d-d96a0e307534" />

<img width="1069" height="478" alt="image" src="https://github.com/user-attachments/assets/b5e56b9a-2f75-45cb-b834-5bf27000207f" />

<img width="889" height="174" alt="image" src="https://github.com/user-attachments/assets/965d7273-e093-44c4-9c15-1fdb64af3108" />

<img width="756" height="119" alt="image" src="https://github.com/user-attachments/assets/a8249d24-6f94-4e19-9b1b-7757c58a6d1e" />

<img width="853" height="197" alt="image" src="https://github.com/user-attachments/assets/e735b1bf-ac13-4ef1-8b03-fb691da0663c" />

<img width="694" height="177" alt="image" src="https://github.com/user-attachments/assets/279b0650-dd1a-4ac0-befc-2edd6e497f14" />

<img width="764" height="207" alt="image" src="https://github.com/user-attachments/assets/e81fc5d9-aedb-4a65-8d29-007ad9231cd2" />

<img width="810" height="140" alt="image" src="https://github.com/user-attachments/assets/5d1db0d7-5a42-4e67-92c4-9db5486adc00" />

<img width="741" height="159" alt="image" src="https://github.com/user-attachments/assets/8434b8e8-d7e9-48e8-aedf-f4cd5273adc9" />

<img width="761" height="81" alt="image" src="https://github.com/user-attachments/assets/f68b97eb-3a97-4bda-88ee-dcfe97bd4585" />

<img width="332" height="43" alt="image" src="https://github.com/user-attachments/assets/7835b2c0-3e64-4743-bff5-a028a0e80aaa" />

## Output Program

## Link YT
