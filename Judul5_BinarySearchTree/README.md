# Sistem Leaderboard Skor Game

Jadi, kode ini buat program sistem Leaderboard Game yang fungsi utamanya untuk mengelola data peringkat skor pemain secara dinamis.
Di kode ini menerapkan konsep struktur data Binary Search Tree (BST) tingkat lanjut, supaya penyimpanan dan pencarian skornya bisa berjalan lebih cepat dan efisien dibanding pakai list biasa.
Selain operasi menambah dan menghapus skor, sistem ini juga punya fitur keren buat menghitung kedalaman tingkat persaingan, serta mencari rival terdekat lewat fitur skor tertinggi sesudah maupun skor terendah sebelum skor tertentu.

Untuk alur programnya, semua dijalankan lewat menu interaktif di fungsi main() yang terus berulang sampai kita memilih opsi keluar.
Di setiap pilihan menu, program bakal meminta input dari user yang keamanannya sudah dijaga pakai validasi try-except biar programnya tidak langsung crash kalau user salah ketik huruf.
Lalu, begitu skor dimasukkan atau dihapus, fungsi rekursif dari BST nya bakal otomatis mengatur posisi node kiri dan kanannya, lalu sistem langsung memanggil fungsi level order buat mencetak gambaran keseluruhan skor berdasarkan urutan level pohonnya saat itu juga.

## Source Code

<img width="698" height="71" alt="image" src="https://github.com/user-attachments/assets/0c41ebfb-7ed5-4ca9-a012-300433ab65d7" />

Baris 1-3 ini hanya untuk mencetak dekorasi garis dan teks judul Tugas Akhir ke layar saat program pertama kali di running.

<img width="878" height="123" alt="image" src="https://github.com/user-attachments/assets/0ec9d73c-a5a4-444c-9ff3-32c782383037" />

Baris 5 itu buat mendefinisikan objek bernama Node. Jadi setiap data yang tersimpan akan dijadikan node.

Baris 6 ini itu fungsi konstruktor yang untuk membuat objek node baru. Dengan key sebagai skor yang baru diinput.

Baris 7 buat menyimpan nilai skor ke dalam node yang dibuat tadi.

Baris 8 ini untuk menyiapkan tempat untuuk anak cabang sebelah kiri, yang awalnya kosong.

Baris 9 ini mirip seperti baris 8, tapi buat anak cabnag kanan.

<img width="626" height="70" alt="image" src="https://github.com/user-attachments/assets/b71d9210-d27c-4005-8eda-add41469c15d" />

Baris 11 ini adalah cetakan buat mengatur operasi-operasi yang ada pada BST.

Baris 12 ini adalah konstruktor juga. Jadi saat si pohon baru pertama kali dibuat, pohonnya dalam keadaan masih kosong.

Baris 13 buat mengatur bahwa si akar utama awalnya bernilai kosong.

<img width="955" height="158" alt="image" src="https://github.com/user-attachments/assets/0449159a-35aa-4f78-bbb4-2582cf8ce995" />

Baris 15 ini adalah fungsi rekursif buat mencari posisi yang tepat bagi skor baru.

Baris 16-17 ini jika posisi saat ini kosong, maka bakal buat node baru di sini pakai node(key).

Baris 18-19 jika si skor yang baru diinputkan itu lebih kecil dari skor dari node saat ini, sistem akan bergerak ke cabang kiri.

Baris 20-21 tapi jika skor yang baru diinputkan itu lebih besar dari si node saat ini, program akan bergerak ke cabang kanan.

Baris 22 akan mengembalikan node yang telah diperbarui strukturnya.

<img width="800" height="44" alt="image" src="https://github.com/user-attachments/assets/8e185296-96f3-4426-b527-ab4846cc682e" />

Baris 24-25 ini adalah fungsi yang membantu agar bisa langsung memanggil si pohon.insert(skor) dari luar tanpa harus memasukkan parameter root secara manual.

<img width="759" height="125" alt="image" src="https://github.com/user-attachments/assets/d0dc967f-2a4c-481f-b203-3c0590ea447f" />

Baris 27 ini fungsi buat mencari nilai terkecil di sebuah cabang. 

Baris 28 buat memulai pencarian dari node yang ditentukan.

Baris 29-30 jika selama cabang masih ada, program akan terus bergerak ke kiri.

Baris 31 ini buat mengembalikan node yang memiliki nilai paling kecil.

<img width="1030" height="387" alt="image" src="https://github.com/user-attachments/assets/ffc9ece9-1192-4825-b549-8feb9b3a3fd6" />

Baris 33 ini adalah fungsi rekursif buat menghapus skor tertentu dari pohon.

Baris 34-35 ini jika skor yang ingin dihapus tidak ditemukan hingga akhir pohon, maka program akan mengembalikan nilai none.

Baris 36-39 ini buat mencari letak skor yang mau dihapus. Jika lebih kecil, akan cari ke kiri. Tapi jika lebih besar, akan cari ke kanan.

Baris 40 ini akan berjalan jika skor yang dicari sudah ditemukan.

Baris 41-42 ini jika ada node yang mau dihapus tidak punya anak, maka akan langsung dihapuskan. Dan program akan menyelesaikan fungsi.

Baris 43-44 nah kalau nodenya punya anak di sebelah kanan, maka  akan digantikan dengan node anaknya.

Baris 45-46 kalau nodenya punya anak di sebelah kiri, maka akan digantikan dengan anak kirinya.
Baris 47 nah kalau punya dua anak,

Baris 48 ini akan buat mencari nilai terkecil di cabang kanan buat menggantikan node yang dihapus.

Baris 49 nanti nilai terkecil tersebut akan di salin di node saat ini.

Baris 50 karena sudah disalin maka node yang di cabang kanan tadi akan dihapus.

Baris 51 lalu, program akan mengembalikan struktur BST yang baru.

<img width="796" height="77" alt="image" src="https://github.com/user-attachments/assets/f5d7d3f2-dace-4799-8bb7-b8b713779bdc" />

Baris 53-54 ini adalah fungsi yang membantu agar pas pemanggilan fungsi hapus di menu utama lebih mudah.

<img width="833" height="139" alt="image" src="https://github.com/user-attachments/assets/ac42610b-2ca6-4e4c-b596-b50fd81d97ef" />

Baris 56 buat menghitung kedalaman BST nya secara rekursif.

Baris 57-58 ini jika si pohonnya kosong, maka tingginya dianggap -1 yang berarti tidak ada tingkatan.

Baris 59-60 ini buat menghitung tinggi cabaang sebelah kiri dan kanan secara terpisah.

Baris 61 ini buat mengambil nilai tertinggi antara cabang kiri atau kanan, lalu ditambah 1 tingkatan pada pohonnya.

<img width="949" height="276" alt="image" src="https://github.com/user-attachments/assets/5850fec3-f7d6-4100-8282-eeaf33e89754" />

Baris 63 ini buat menampilkan skor berdasarkan tingkatannya, jadi nanti akan ditampilkan dari root smapai leaf paling bawah.

Baris 64-66 ini kalau si pohonnya kosong, sistem bakal mencetak teks (kosong).

Baris 67 ini buat bikin antrian untuk mencatat urutan node yang akan dicetak.

Baris 68 ini buat masukin akar utama sebagai antrian pertama.

Baris 69 jadi selama antriannya masih ada isi, maka perulangam akan selalu terjadi.

Baris 70 ini buat mengambil antrian elemen pertama dari antrian untuk diproses.

Baris 71 buat mencetak skor dari node tersebut ke layar secara mendatar.

Baris 72-76 jika si node punya anak kiri atau kanan, maka anak-anaknya juga akan diikutkan di dalam antriannya biar nanti dicetak di giliran berikutnya.

<img width="1010" height="353" alt="image" src="https://github.com/user-attachments/assets/90057185-e935-4d8e-8f27-09ae2529a295" />

Baris 78-80 fungsi buat mencari successor.

Baris 81 ini buat mencari dari atas sampai bawah si nilainya.

Baris 82-84 ini jika si skor yang dicari lebih kecil, maka si node saat ini berpotensi jadi successornya. Jadi si successor di simpan di variabel current dan akan di geser ke kiri.

Baris 85-86 nah kalau si skor nya lebih besar, maka akan bergerak ke kanan.

Baris 87-88 tapi kalau nilainya ketemu, maka sistem akan menghentikan pencarian sementara.

Baris 89-90 kalau si skor acuannya tidak ada di dalam pohon maka sistem bakal balikin status gagal.

Baris 91-92 tapi kalau si node acuan punya node cabang kanan, maka si successornya nilai paling kecil di cabang kanan itu.

Baris 93-95 ini bakal mengembalikan nilai skor susccessor beserta status sukses.

<img width="1143" height="429" alt="image" src="https://github.com/user-attachments/assets/6cec3b2e-7c25-41a5-aeb5-b0bbcfecc174" />

Baris 97-99 fungsi buat mencari predecessor.

Baris 100 ini buat mencari dari atas sampai bawah si nilainya.

Baris 101-103 ini jika si skor yang dicari lebih besar, maka si node saat ini berpotensi jadi predecessornya. Jadi si predecessor di simpan di variabel current dan akan di geser ke kanan

Baris 104-105 nah kalau si skor nya lebih kecil, maka akan bergerak ke kiri.

Baris 106-107 ini buat menghentikan perulangan kalau si key yang dicari sudah ketemu.

Baris 108-109 kalau si skor acuannya tidak ada di dalam pohon maka sistem bakal balikin status gagal.

Baris 110-114 tapi kalau si node acuan punya node cabang kiri, maka si predecessornya nilai paling besar di cabang kiri itu.

Baris 115-116 jika si predecessornya tidak ada, maka akan mengembalikan status gagal.

Baris 117 ini bakal mengembalikan nilai skor predecessor beserta status sukses.

<img width="913" height="315" alt="image" src="https://github.com/user-attachments/assets/b793c130-a5ae-469c-b5d7-4189f3d24771" />

Baris 119 ini adalah fungsi utama si sistemnya.

Baris 120 ini membuat satu objek pohon kosong baru yang diberi nama bst.

Baris 121 ini adalah variabel menu.

Baris 122 ini adalah perulangan yang akan selalu berjalan selama user tidak menginput angka 6.

Baris 123-129 buat menampilkan menu.

Baris 130-134 ini adalah bentu try-excpet agar si sistem tidak langsung crash ketika user malah masukin huruf saat diminta angka pada pemilihan menu.

<img width="897" height="172" alt="image" src="https://github.com/user-attachments/assets/3252adcf-5424-4819-9968-c8116c67710f" />

Baris 135-143 ketika user memilih menu 1 maka sistem akan meminta inputan skor baru dari user, dan menyimpan si variabel x, lalu mengambil fungsi bst.insert(x). lalu, lansung menampilkan struktur papan skor saat ini menggunakan bst.level.order.

<img width="997" height="175" alt="image" src="https://github.com/user-attachments/assets/9a1d54bf-46ab-486a-b227-f132f673e807" />

Baris 144-152 saat user milih menu 2, ini akan meminta user buat masukin input skor yang ingin dihapus, dengan memanggil fungsi bst.delete(x), lalu bakal nampiln sisa skor yang ada di papan peringkat.

<img width="799" height="47" alt="image" src="https://github.com/user-attachments/assets/ee921c60-c10c-4524-b966-20e262f8086a" />

Baris 153-154 saat memilih menu 3 maka akan memamnggil fungsi bst.height buat mengetahui berapa tingkatan/level pohon yang terbentuk saat ini.

<img width="923" height="192" alt="image" src="https://github.com/user-attachments/assets/8833bfd6-ad13-4360-b37f-665b1bd55531" />

Baris 155-164 kalau user milih menu 4 maka fungsi buat mencari nilai terdekat yang posisinya berada di tepat atas skor si x, nah kalau ada nilai/ skornya itu maka akan langsnung dicetak. Tapi kalau teryata tidak ada maka akan muncul pesan pemberitahuan.

<img width="1004" height="195" alt="image" src="https://github.com/user-attachments/assets/a6094e51-6e5f-4332-a930-e0811830b5c0" />

Baris 165-174 ini kalau user milih menu 5, maka fungsi buat mencari predecessor nya akan dijalankan, yang mana buat mencari nilai skor terdekat yang posisinya berada di bawah skor.

<img width="934" height="80" alt="image" src="https://github.com/user-attachments/assets/cd1a0042-a2f3-4f46-ae6d-c31b3f6e21fd" />

Baris 175-176 ini kalau user milih menu 6, maka sistem akan mengakhiri perulangan menu dan menutup program.

Baris 177-178 ini akan dijalankan ketika user menginput angka di luar 1-6. Sistem akan langsung memberi tahu bahwa si user salah memasukkan inputan.

<img width="1023" height="52" alt="image" src="https://github.com/user-attachments/assets/41e8f55d-c8ad-48e9-9a96-c099be395fdb" />

Baris 180-181 ini fungsi buat memastikan saat di running nanti fungsi utama otomatis di jalankan.


## Output Program

## Link YT
