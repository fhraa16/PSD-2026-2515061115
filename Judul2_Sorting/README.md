# Sistem Pengurutan Berat Badan Bayi di Posyandu Ceria
Studi case yang saya buat ini adalah Sistem Pengurutan Berat Badan Bayi di Posyandu yang menerapkan algoritma Insertion Sort buat mengurutkan berat badan dari yang terkecil smapai yang terbesar.
Yang mana program ini dimulai dari sistem minta user buat masukin berapa banyak data balita yang ingin dihitung. 
Lalu dengan menggunakan perulangan buat mengumpulkan berat badan nya ke dalam sebuah list, lengkap dengan validasi error nya juga buat menghindari program akan mengcrash saat user menginput selain angka.

Setelah semua data terkumpul dan ditampilkan sebelum diurutkan, fungsi insertion_sort itu buat membandingkan dan menggeser nilai yang ada di list, ke posisi yang tepat.
Kemudian program akan mencetak data berat badan yang sudah terurut rapi dengan nomor urut.

## Source Code

<img width="507" height="75" alt="image" src="https://github.com/user-attachments/assets/7637c84e-70a1-486d-beaa-9684968e0a5a" />

Baris 1-3 ini berfungsi buat mencetak Judul Tugas Akhir di terminalnya.

<img width="526" height="172" alt="image" src="https://github.com/user-attachments/assets/5e491e02-4579-4d21-b420-0fb0a6988370" />

Baris 5 ada fungsi insertion_sort yang menerima dua parameter yaitu arr (list yang nantinya akan diisi berat bada balita), dan n (jumlah data balita yang mau dihitung).

Baris 6 itu buat melakukan perulangan untuk mengambil elemen data dari indeks yang pertama atau 0 sanpai indeks yang terakhir yang berupa elemen yang akan disisipkan nantinya.

Baris 7 buat menyimpan nilai data yang sekarang ke dalam variabel sementara "temp".

Baris 8 ini buat menunjukkan elemen tepat sebelah kiri dari elemen yang diperiksa

Baris 9 sampai 11 itu perulangan buat menggeser elemen ke kanan, jika nilainya lebih besar dari elemen yang disisipkan.

Baris 12 buat menyisipkan nilai "temp" ke posisi yang benar di list yang sudah terurut sebagiannya.

<img width="678" height="56" alt="image" src="https://github.com/user-attachments/assets/6fb1728e-5442-4bd6-b841-fdcd7c13a922" />

Baris 14 dan 15 itu buat mencetak nama program yang sedang dijalankan.

<img width="792" height="233" alt="image" src="https://github.com/user-attachments/assets/fdfe5699-153c-455a-85e1-bc4548b71ea9" />

Baris 17 ada fungsi utama tempat alur programnya berjalan.

Baris 18 itu buat mencetak sapaan saat program baru dimulai atau dijalankan.

Baris 20 sampai 27 ini ada try-excpet yang berfungsi buat mengatisipasi jika user salah menginput, yang seharusnya bilangan bulat malah jadi bilangan desimal atau bahkan huruf. Ini juga agar program tidak langsung crash ketika user melalukan kesalah input tersebut. Jadi di sini ada dua syarat user tidak boleh mengsi data yang ingin dicari ini kurang atau sama dengan 0 dan tidak boleh berbetuk desimal atau huruf.

<img width="704" height="248" alt="image" src="https://github.com/user-attachments/assets/e6c072d7-f34b-4bc8-84c5-52c85cfcf0e9" />

Baris 29 ini membuat list kosong, buat menampung data yang bakal diinputkan oleh user.

Baris 31 ini melakukan perulangan sebanyak n kali.

Baris 32 sampai 38 itu ada try excpet yag tugsnya juga sama seperti yang sebelumnya udah dibahas tadi.

Baris 34 ada float(input(...)) itu buat menginput berat badan balita, dan dia bisa dalam bentuk desimal juga.

Baris 35 ada arr.append(nilai) yang berfungsi buat nambahin data yang baru masuk ke dalam list array yang usdah dibuat tadi.

Baris 40 itu buat mencetak data yang sudah dimasukkan tapi dalam kondisi belum diurutkan.

<img width="619" height="114" alt="image" src="https://github.com/user-attachments/assets/906aa73d-034a-4611-824a-ef2d90b99702" />

Baris 42 ini sebagai pemanggil fungsi dari fungsi yang telah kita buat tadi.

Baris 44 buat melakukan suatu iterasi untuk mencetak hasil berat badan yang berurutan dari yang terkecil sampai yang terbesar.

<img width="412" height="58" alt="image" src="https://github.com/user-attachments/assets/7a819459-336d-4d6a-b6f8-270c3d904d9e" />

Baris 48 sampai 49 ini adalah pemanggil fungsi main atau menu utama, jadi ketika file program ini dijalankan, program akan langsung memanggil si fungsi main tersebut.

## Output Program

<img width="917" height="165" alt="image" src="https://github.com/user-attachments/assets/31c92ff3-5473-4c30-8fb2-246220649721" />

Ini adalah bentuk output dimana user input nya adalah huruf, dia akan memberikan peringatan dan memaksa berhenti program.

<img width="890" height="157" alt="image" src="https://github.com/user-attachments/assets/c1a72145-fc4d-478b-919f-a0af2fa26f9e" />

Ini adalah bentuk output dimana user input nya adalah desimal, dia akan memberikan peringatan dan memaksa berhenti program.

<img width="918" height="588" alt="image" src="https://github.com/user-attachments/assets/95b41cfe-e66d-4790-9d3a-fe6eff19af4f" />

Sedangkan yang ini adalah versi benar, dimana user menginput 5 sebagai data balita yang ingin dihitung, lalu memasukkan berat badan balitanya. Baru setelah itu program akan mencetak data yang belum terurut dan data yang sudah terurut jugaa.

## Link YT
https://youtu.be/ICHt90AjL1c
