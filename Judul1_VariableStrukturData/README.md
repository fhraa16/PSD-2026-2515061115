# Sistem Absensi Siswa
Study case yang saya buat ini adalah Sistem Absensi Siswa sederhana yang menerapkan konsep List 1D. Lalu buat nambah data ke dalam array yang telah dibuat saya menggunakan fungsi .append(). Di sistem ini juga kita bisa liat id dari list-nya dan tiap-tiap objek yang diinputkan oleh user.

Untuk alurnya, di sistem ini menggunakan perulangan while True untuk membuat sistem terus berulang jalan sampai kita pilih menu keluar. Lalu buat nampilin id tiap siswa, sistem ini menggunakan iterasi enumerasi buat dapatin nomor urut otomatis. Di sistem ini juga untuk menghindari terjadinya sistem error ketika user salah menginput nomor menggunakan try except. Jadi ketika si user salah input nomor atau malah masukan nama sistem akan memberikan semacam informasi bahwa yang user input itu tidak valid.

## Source Code
<img width="525" height="208" alt="image" src="https://github.com/user-attachments/assets/85a94d9f-1850-4b3a-b501-8be2fe37dbe5" />

Pada baris 1-3 berfungsi untuk mencetak tampilan judul besar program yang dibuat. 

Di baris ke 5 ada def menu() yang berfungsi untuk mencetak fungsi menu yang sudah dibuat tiap kali dipanggil.

Di baris ke 6 itu akan mencetak nama sistem yang sedang berjalan.

Di baris 7 sampai 10 akan menampilkan opsi yang akan dipilih oleh user. Seperti 1. Nambah nama siswa, 2. Nampilin id list yang telah dibuat, 3. Nampilin id per nama yang sudah dimasukin oleh user, dan yanng ke 4 itu buat menyelesaikan sistem yang sedang berjalan.

<img width="587" height="611" alt="image" src="https://github.com/user-attachments/assets/26ceec7b-3b12-46b6-a835-830f263775a4" />

Di baris 12 ada kode def main() yang berguna sebagai fungsi tempat program utama yang akan dijalankan.

Di baris 13 kita membuat list kosong. Yang berguna untuk menampung nama-nama siswa yang sudah diinputkan.

Di baris 14 itu buat mengulangi sistem terus menerus sebelum user memilih opsi keluar.

Di baris 15 ada menu () yang berguna untuk memanggil fungsi menu di terminal.

Di baris 16 sampai 20 itu ada try except yang berfungsi untuk menangani kesalahan input. Jadi semisal sistem minta angka opsi yang ingin dipilih sedangkan user malah masukin nama sistem akan memberi peringatan dengan mencetak "Masukkan angka yang valid" lalu akan menjalan kembali sistemnya.

Di baris 22 sampai 23 jika user memilih opsi 1 maka sistem akan meminta agar user menginput nama siswa.

Di baris 24 setelah user memasukkan nama maka sistem akan menambahkan nama tersebut ke dalam list kosong yang telah dibuat tadi.

Di baris 25 sesudah disimpan oleh sistem maka sistem akan menampilkan (nama) telah ditambahkan.

Di baris 26 dan 27 jika user milih opsi 2 maka sistem akan menampilkan id dari keseluruhan list yang telah dibuat.

Di baris 28 sampai 29 jika user memilih opsi 3 maka sistem akan mengecek list-nya

Di baris 30 akan mencetak sub judul berupa "Detail id dari setiap nama siswa: "

Di baris 31 dan 32 untuk setiap nama-nama nya akan diurutkan dari 1 oleh sistem menggunakan enumerate. Lalu akan mencetak urutan tersebut beserta id-nya.

Di baris 33 dan 34 jika ternyata user belum menginput nama siswa, maka sistem akan mencetak "Belum ada siswa yang diabsen."

Di baris 35 dan 36 jika user memilih opsi 4 maka sistem akan mencetak "Absensi telah selesai. Terima kasih!".

Di baris 37 sistem akan dipaksa berhenti oleh break sehingga sistem akan berhenti.

Di baris 38 dan 39 jika ternyata user ketika menginput angka, tapi ternyata angka melebihi opsi yang disediakan maka sistem akan memberi peringatan.

Di baris 41 dan 42 ini bertugas buat memastikan fungsi main berjalan ketika dieksekusi langsung di terminalnya.

## Output Program
<img width="416" height="631" alt="image" src="https://github.com/user-attachments/assets/b6e0f708-ec65-419c-9666-ef0152341125" />

Pada output ini ditampilkan jika user memasukkan opsi berupa kata atau angka di luar opsi yang disediakan maka sistem akan mencetak peringatan. Lalu saat user memilih opsi 1 dan menginput nama, nama itu akan disimpan ke list yang sudah dibuat sebelumnya. Lalu nama tersebut akan dicetak bahwa nama yang diinput sudah tersimpan atau ditambahkan.

<img width="422" height="560" alt="image" src="https://github.com/user-attachments/assets/75efd363-99b9-485a-82b1-807af36634cf" />

Pada output yang ini akan menampilkan output jika user meninput opsi 2 dan 3, di opsi 2 ada id untuk semua list nama siswa sedangkan di opsi 3 akan menampilkan id untuk setiap siswa yang sudah diinput namanya.

Lalu ketika user menginput opsi 4 sistem akan langsung berhenti.

<img width="397" height="309" alt="image" src="https://github.com/user-attachments/assets/baa22a34-9ff9-42cb-99cc-8366c3c31a4b" />

Output yang ini ketika user memilih opsi 3 sedangkan ia belum memasukkan nama-nama siswa.


## Link YT
