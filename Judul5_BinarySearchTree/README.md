# Sistem Leaderboard Skor di Game Puzzle

Jadi, kode ini buat program sistem Leaderboard Game yang fungsi utamanya untuk mengelola data peringkat skor pemain secara dinamis.
Di kode ini menerapkan konsep struktur data Binary Search Tree (BST) tingkat lanjut, supaya penyimpanan dan pencarian skornya bisa berjalan lebih cepat dan efisien dibanding pakai list biasa.
Selain operasi menambah dan menghapus skor, sistem ini juga punya fitur keren buat menghitung kedalaman tingkat persaingan, serta mencari rival terdekat lewat fitur skor tertinggi sesudah maupun skor terendah sebelum skor tertentu.

Untuk alur programnya, semua dijalankan lewat menu interaktif di fungsi main() yang terus berulang sampai kita memilih opsi keluar.
Di setiap pilihan menu, program bakal meminta input dari user yang keamanannya sudah dijaga pakai validasi try-except biar programnya tidak langsung crash kalau user salah ketik huruf.
Lalu, begitu skor dimasukkan atau dihapus, fungsi rekursif dari BST nya bakal otomatis mengatur posisi node kiri dan kanannya, lalu sistem langsung memanggil fungsi level order buat mencetak gambaran keseluruhan skor berdasarkan urutan level pohonnya saat itu juga.

## Source Code

Baris 1-3 ini hanya untuk mencetak dekorasi garis dan teks judul Tugas Akhir ke layar saat program pertama kali di running.

Baris 5 itu buat mendefinisikan objek bernama Node. Jadi setiap data yang tersimpan akan dijadikan node.
Baris 6 ini itu fungsi konstruktor yang untuk membuat objek node baru. Dengan key sebagai skor yang baru diinput.
Baris 7 buat menyimpan nilai skor ke dalam node yang dibuat tadi.
Baris 8 ini untuk menyiapkan tempat untuuk anak cabang sebelah kiri, yang awalnya kosong.
Baris 9 ini mirip seperti baris 8, tapi buat anak cabnag kanan.

Baris 11 ini adalah cetakan buat mengatur operasi-operasi yang ada pada BST.
Baris 12 ini adalah konstruktor juga. Jadi saat si pohon baru pertama kali dibuat, pohonnya dalam keadaan masih kosong.
Baris 13 buat mengatur bahwa si akar utama awalnya bernilai kosong.

Baris 15 ini adalah fungsi rekursif buat mencari posisi yang tepat bagi skor baru.
Baris 16-17 ini jika posisi saat ini kosong, maka bakal buat node baru di sini pakai node(key).
Baris 18-19 jika si skor yang baru diinputkan itu lebih kecil dari skor dari node saat ini, sistem akan bergerak ke cabang kiri.
Baris 20-21 tapi jika skor yang baru diinputkan itu lebih besar dari si node saat ini, program akan bergerak ke cabang kanan.
Baris 22 akan mengembalikan node yang telah diperbarui strukturnya.

Baris 24-25 ini adalah fungsi yang membantu agar bisa langsung memanggil si pohon.insert(skor) dari luar tanpa harus memasukkan parameter root secara manual.

Baris 27 ini fungsi buat mencari nilai terkecil di sebuah cabang. 
Baris 28 buat memulai pencarian dari node yang ditentukan.
Baris 29-30 jika selama cabang masih ada, program akan terus bergerak ke kiri.
Baris 31 ini buat mengembalikan node yang memiliki nilai paling kecil.

Baris 33 ini adalah fungsi rekursif buat menghapus skor tertentu dari pohon.
Baris 34-35 ini jika skor yang ingin dihapus tidak ditemukan hingga akhir pohon, maka program akan mengembalikan nilai none.
Baris 36-39 ini buat mencari letak skor yang mau dihapus. Jika lebih kecil, akan cari ke kiri. Tapi jika lebih besar, akan cari ke kanan.
Baris 40 ini akan berjalan jika skor yang dicari sudah ditemukan.
Baris 41-42 ini jika ada node yang mau dihapus tidak punya anak, maka akan langsung dihapuskan. Dan program akan menyelesaikan fungsi.
Baris 43-44 nah kalau nodenya punya anak di sebelah kanan, maka  akan digantikan dengan node anaknya.
Baris 45-46 kalau nodenya punya anak di sebelah kiri, maka akan digantikan dengan anak kirinya.
Baris 47 nah kalau punya dua anak
Baris 48 ini akan buat mencari nilai terkecil di cabang kanan buat menggantikan node yang dihapus.
Baris 49 nanti nilai terkecil tersebut akan di salin di node saat ini.
Baris 50 karena sudah disalin maka node yang di cabang kanan tadi akan dihapus.
Baris 51 lalu, program akan mengembalikan struktur BST yang baru.



## Output Program

## Link YT
