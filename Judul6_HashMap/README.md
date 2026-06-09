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


## Output Program

## Link YT
