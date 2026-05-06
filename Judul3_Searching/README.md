# Sistem Pencarian Letak Nomor Kursi Bioskop

Jadi sistem ini dibuat untuk mencari letak nomor kursi bioskop.
Sistem ini menerapkan algoritma binary search buat nyari posisi nomor kursi tertentu yang sudah diurutkan di dalam listnya. 
Lalu alurnya itu pertama, program bakal nampilin daftar nomor kursinya.
Kedua user disuruh meng-input nomor kursi yang mau dicari.
Nah di sini biar program tidak langsung error atau nge-crash saat user input berupa huruf atau karakter lain, kita pakai try-except.

Kemudian fungsi binary searchnyaa akan jalan buat membagi rentang pencarian jadi dua ruang secara berulang sampai angka yang dicari ketemu.
Lalu kalau udah dapat angkanya dimana, sistem bakal menentukan si nomor kursinya ini masuk ke baris yang mana.
Misal di indeks 0-4 itu berarti kursinya di depan.
Di indeksi 5-9 itu kursi tengah.
Dan Indeks nya sisanya berarti kursi belakang.
Nah nanti kalau udah sampai akhir, sistem bakal mencetak nomor kursinya itu ada di indeks mana dan letaknya dimana.
Atau malah bilang kalau nomor yang dicari tidak ada di dalam list.

## Source Code
<img width="322" height="67" alt="image" src="https://github.com/user-attachments/assets/336b29cb-1a44-4fe8-be1d-e751e531b4ac" />

Baris 1-3 ini berfungsi buat mencetak judul besar di sistem ini.

<img width="568" height="349" alt="image" src="https://github.com/user-attachments/assets/c3073704-7988-47c7-b596-a73a2ec31fc8" />

Baris 5 ini fungsi binary search yang memiliki 3 parameter yaitu list arraynya, panjang list n, dan angka yang dicari/ target.

Baris 6 ini berfungsi sebagai batas, jadi kek batas dari bagian kiri itu dari indeks ke-0

Baris 7 ini berfungsi sebagai batas bagian kanan, yang batasnya berada di indeks paling akhir.

Baris 9-11 ini adalah bentuk perulangan, dimana nilai yang dicari lebih dari yang sebelah kiri atau sama dengan yang sebelah kanan.
Lalu akan mengecek indeks tengah buat membagi menjadi dua ruang pencarian. Setelah itu nanti akan dicetak.

Baris 12-14 ini buat mengecek apakah nilai yang dicari sama dengan indeks yang tengah.
jika iya, maka indeks tengah tadi dimasukkan ke dalam variabel pos.
Dan akan menghentikan perulangan karena nilai yang dicari sudah ditemukan.

Baris 15-17 nah jika ternyata nilai dicari malah lebih besar dari si nilai tengah, maka pencarian akan dicari di sebelah kanan.
Rumus l = m + 1 ini buat menggeser pencarian ke dari indeks tengah ke sebelah kanan.

Baris 18-20 kalau yang tadi ketika nilai yang dicari lebih dari nilai di indeks tengah, kalau yang dibagian ini adalah ketika nilai yang dicari itu ternyata lebih kecil dari nilai indeks tengah.
Maka pencarian akan dilakukan ke sebelah kiri. Yang digambarkan dengan rumus r = m - 1 yang berarti pencarian akan dilakukan dari indeks tengah dikurangi 1 atau berarti pindah ke sebelah kiri.

Baris 21 ini untuk mengembalikan nilai indeksnya ke posisi awal jika ternyata angka yang dicari tidak ditemukan.

<img width="627" height="481" alt="image" src="https://github.com/user-attachments/assets/9ef19871-9e7f-4556-bb32-3ea8e0b8f239" />

Baris 23 ini adalah fungsi menu utama, yang ketika sistem dijalankan, maka bagian sistem ini yang akan berjalan.

Baris 24 ini buat mencetak nama sistem yang dijalankan setiap dijalankannya sistem.

Baris 25 ini adalah array yang tersimpan sebagai nomor kursi bioskop yang sudah berurutan.

Baris 26 ini akan mencetak nomor kursi dan isi arraynya.

Baris 27 ini ada perulangan While True yang berarti akan berjalan terus sampai user meng-input data yang valid.

Baris 28-32 ini adalah bentuk Try-Except. Jadi semisal input yang dimasukkan user bukan berupa angka, tapi malah berupa huruf, maka sistem akan memberikan peringatan. Dan sistem akan meminta inputan baru.

Baris 33 ada variabel n yang berfungsi buat mengitung panjang dari array.

Baris 34 ada variabel pos yang berfungsi buat memanggil fungsi binary search dan menyimpan hasilny dalam bentuk pos.

Baris 35 baris = pos ini itu buat menyiapkan variabel baris untuk menyimpan kategori letak tempat duduk.

Baris 36-37 jika indeks dari nilai yang ditemukan adalah dibawah atau sama dengan 4 maka sistem akan mencetak letak "Depan"

Baris 38-39 jika indeks berada di antara indeks 5 sampai 9 maka akan dicetak "Tengah"

Baris 40-41 Nah ini jika berada di indeks di atas indeks 9 maka akan mencetak "Belakang"

Baris 42-46 Nah kalau nomor kursinya ketemu, maka akan dicetak nomor kursi ini ditemukan dan letaknya dimana akan dicetak juga.
Tapi jika tenyata nomor yang dicari tidak ketemu, maka akan mencetak "Tidak ditemukan".

<img width="362" height="46" alt="image" src="https://github.com/user-attachments/assets/974c73d3-1437-4cb1-b4c0-aa1fef68e3aa" />

Baris 48-49 berfungsi buat ketika si program dijalankan dia akan langsung menjalankan fungsi menu utamanya.

## Output Program
<img width="539" height="239" alt="image" src="https://github.com/user-attachments/assets/bc4c5451-6102-46d4-b19d-164cef7f3398" />

Di output ini pertama user meng-input huruf, dan sistem akan langsung memberikan peringatan, dan menanyakan kembali nomor berapa yang ingin dicari.

Lalu user memasukkan nomor 5, lalu langsung dijalankan pencariannya. 
Dan ditemukan di indeks ke 1 dan letaknya berada di depan.

<img width="566" height="140" alt="image" src="https://github.com/user-attachments/assets/a263bb24-c0bd-49eb-8da4-92baae57c564" />

Nah ini kalau user memasukkan nilai tengah yaitu 17.

<img width="560" height="237" alt="image" src="https://github.com/user-attachments/assets/9f4aa6cb-fa46-4082-81a2-62c3f8a0b151" />

Dan ini jika user memasukkan nomor kursi 27. 
Nomor kursi ini berada di indeks 13 yaitu indeks hampir ahir.
Yang berarti berada di letak "Belakang".

## Link YT
