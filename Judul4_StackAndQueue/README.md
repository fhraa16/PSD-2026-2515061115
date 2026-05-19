# Sistem Antrian Bank Bahagia

Jadi, di sini kita membuat sistem Antrian Bank Bahagia yang menerapkan struktur data Queue yang menggunakan Linked List. 
Alurnya dimulai dengan menampilkan pilihan menu interaktif, dimana user bisa nambah antrian, hapus antrian dari depan, melihat antrian terdepan, atau melhiat seluruh is antrian.
Lalu biar programmnya tidak mudah nge-crash pas user milih menu, di sini ditambahkan validasi try-excpet buat menanganin error kalau ada usernya salah input, yang harusnya angka malah huruf.

Lalu dibagian enqueue nya disini ditambahin kondisi khusus dimana kalau jumlah antriannya udah mencapai 7 atau lebih, nanti sistem ini akan ngasih peringatan "Antrian sudah padat!" lalu nanya ke user apakah mau lanjut ngantri atau tidak.
Selain itu, saat user milih opsi keluar, sistemnya tidak akan langsung berhenti, tapi bakal kosongin dulu sisa antriannya.
Nah prosesnya itu menggunakan proses looping dequeue sampai si antriannya benar-benar kosong.

## Source Code

<img width="492" height="70" alt="image" src="https://github.com/user-attachments/assets/ef376f91-9834-48dc-89e2-4175dcbf1500" />

Baris 1- 3 ini hanya buat mencetak judul besar di sistem ini.

<img width="650" height="107" alt="image" src="https://github.com/user-attachments/assets/afb7a8f6-0b02-4653-99de-ff15151516cb" />

Baris 5 ini seperti buat template untuk wadah data. Dan di linked list itu, setiap data yang masuk itu akan dibungkus dalam satu "Node".

Baris 6 ini adalah konstruktor yang disiapkan untuk data awal tiap kali user baru masuk antrian.

Baris 7 ini buat menyimpan data asli, jadi seperti nama-nama yang sedang mengantri.

Baris 8 ini adalah pointer atau penunjuk ke data setelanhnya. Sedangkan kalau baru dibuat, pointer ini tidak akan menunjuk ke siapa-siapa.

<img width="531" height="113" alt="image" src="https://github.com/user-attachments/assets/a0ec6411-ebd8-486f-81d2-211ddbde57c5" />

Baris 10 ada struktur utama buat ngatur jalannya antrian.

Baris 11 ini seperti penunjuk buat mencatat siapa aja yang ada di barisan paling depan.

Baris 12 ini kebalikan dari baris 11 yaitu buat mencatat siapa aja yang ada di barisan belakang.

Baris 13 buat menghitung jumlah yang ada di antrian saat ini.

Baris 14 ini berguna buat menghitung jumlah data atau antrian yang ada. Di sini sama dengan 0 karena saat sistem pertama kali dijalankan dalam keadaan antrian kosong.

<img width="478" height="67" alt="image" src="https://github.com/user-attachments/assets/89a01aff-30dd-4903-8318-f3d9d874486b" />

Baris 16-17 ini adalah fungsi buat mengecek antriannya lagi kosong atau tidak. Nah kalau pas dicek ternyata kosong, berarti memamg tidak ada antrian.

<img width="770" height="331" alt="image" src="https://github.com/user-attachments/assets/74223b7a-7667-4f9f-9b5c-731642d38aff" />

Baris 19 berfungsi untuk menambah dat abaru ke dalam antrian.

Baris 20-21 ini buat mengecek kondisi, kalau jumlah orang yang di antrian sudah 7 atau lebih sistem bakal kasih peringatan kalau antriannya sudah padat.

Baris 22 ini buat nanya ke user, mau tetap lanjut antri atau tidak.

Baris 23-25 kalau user ternyata input selain 'y' maka proses buat nambahin orangnya dibatalin.

Baris 26 buat node baru yang berisi dengan data yang baru diinput oleh user.

Baris 27-29 ini kalau semisal antrian lagi benar-benar kosong, maka data yang baru masuk tadi bakal jadi orang pertama sekaligus orang yang terakhir.

Baris 30-32 tapi kalau sudah terisi, orang terakhir yang lama akan menunjuk ke orang baru, dan status orang belakang akan digeser ke data baru ini.

Baris 33 ini berarti jumlah total antrian bertambah 1

Baris 34 ini itu buat konfirmasi ke layar kalau nama yang sudah diinputkan tadi sudah masuk ke antrian.

<img width="794" height="218" alt="image" src="https://github.com/user-attachments/assets/cc17d62c-27b2-431c-af16-d58a544e1bc4" />

Baris 36 berfungsi untuk memanggil dan menghapus data yang berada di antrian paling depan.

Baris 37-39 ini buat mengecek antriannya, apakah antriannya kosong atau tidak, kalau antriannya ternyata kosong maka fungsi akan langsung berhenti.

Baris 40 ini buat jadi penyimpanan sementara buat data-data orang paling depan yang mau dihapus.

Baris 41 ini buat memberi tahu kalau orang tersebut sedang mau dilayani.

Baris 42 ini itu buat menggeser petunjuk "orang paaling depan" ke orang di belakangnya.

Baris 43-44 Nah kalau pas digeser tadi ternyata antriannya kosong, maka penunjuk belakangnya sama dengan tidak ada (none).

Baris 45 karena sudah ada data yang dipanggil atau dihapus, maka jumlah total di antrian dikurangi 1.

<img width="643" height="123" alt="image" src="https://github.com/user-attachments/assets/84ae3355-9153-44ad-b11a-7c73e15d8ee0" />

Baris 47 ini fungsi buat melihat data antrian yang paling awal tanpa menghapus data tersebut.

Baris 48-50 ini misal ternyata pas dicek ternyata antriannya kosong, maka sistem bakal kasih tau bahwa antrian kosong, lalu akan menghentikam fungsi tersebut.

Baris 51 ini jika antriannya tidak kosong, maka sistem akan mencetak siapa saja yang berada di antrian depan.

<img width="753" height="289" alt="image" src="https://github.com/user-attachments/assets/d9c94f09-18df-45f1-bc4c-faaaca811c06" />

Baris 53 ini berfungsi buat memunculkan semua list orang yang masih antri, dari yang di depan sampai yang belakang.

Baris 54-56 ini buat mengecek lagi apakah antriannya kosong atau tidak, kalau kosong maka sistem akan memberikan pemberitahuan antrian kosong dan fungsi ini akan berhenti.

Baris 57 ini buat menampilkan teks dari awal antrian.

Baris 58 ini mulai penelusuran dari data yang paling depan.

Baris 59 ini berarti akan melakukan perulangan selama node yang dicek ini masih ada isinya.

Baris 60 di sini akan mencetak data nya ke samping, agar tidak perlu buat baris baru.

Baris 61 ini buat memindahkan node ke node berikutnya.

Baris 62 ini berguna untuk memindahkan baris.

Baris 63-64 ini buat nampilin status kepadatan antrian, kalau sama dengan atau lebih dari dari 7 maka sistem akan memberi peringatan "Sangat Padat"

Baris 65-66 sebaliknya kalau antrain ternyata totalnya di bawah 7 maka sistem akan memberikan pemberitahuan "Status Lancar".

<img width="964" height="619" alt="image" src="https://github.com/user-attachments/assets/14a80d4a-5535-4362-87d8-626538dbfdfd" />

Baris 68 ini adalah fungsi utama buat menjalankan sistemnya.

Baris 69 buat bikin obbjek antrian baru dari class yang sudah dibuat tadi.

Baris 70 ini adalah variabel yang akan menampung pilihan menu user, diatur dari awal 0 agar masuk ke perulangan.

Baris 71 ini berarti program akan berjalan selama user belum memilih opsi keluar.

Baris 72 ini menampilkan judul menu.

Baris 73-77 ini akan menampilkan daftar menunya.

Baris 78-82 ini adalah buat memvalidasi input-annya, kalau user tidak sengaja salah input yang harusnya input berupa angka, maka sistem tidak akan langsung nge-crash ataupun error, tapi sistem akan kasih peringatan bahwa input tidak valid dan akan mengulan menunya lagi.

Baris 84-92 ini mengarahkan ke fungsi sesuai dengan angka yang dipilih oleh user. Pilihan satu ke fungsi enqueue, pilihan 2 ke fungsi dequeue, pilihan 3 ke fungsi peek, dan pilihan ke 4 ke fungsi display.

Baris 93-96 nah kalau user memilih keluar, sistem bakal jalanin perulangan untuk mengosongkan antrian satu per satu sampai habis sebelum sistem benar-benar selesai.

Baris 97-98 ini jika user input angka, tapi angkanya selain 1,2,3,4,5

<img width="519" height="53" alt="image" src="https://github.com/user-attachments/assets/a861a877-a1fb-44a4-948e-0d935b6ac085" />

Baris 100 ini buat mengecek apakag file nya dijalankan langsung atau tidak

Baris 101 ini buat manggil si fungsi utama sistem.

## Output Program
<img width="835" height="411" alt="image" src="https://github.com/user-attachments/assets/1d45ee9c-af12-41f1-85aa-f60ae700c883" />

User masih meng-inputkan nama

<img width="654" height="476" alt="image" src="https://github.com/user-attachments/assets/6702fb34-1f64-4140-b9be-f97a2aa3a3b9" />

User masih menginputkan nama, tapi di output ada peringatan input tidak valid, karena user belum memasukkan inputan tapi sudah mengirimkannya.

<img width="748" height="165" alt="image" src="https://github.com/user-attachments/assets/8cb416c5-8398-442d-a9cd-5d1dd9977f33" />

Ini adalah bentuk ouput ketika user memilih menu ke 4, dan antrian masih berjumlah 4 antrian.

<img width="571" height="156" alt="image" src="https://github.com/user-attachments/assets/5eb01bae-d849-42a4-9b4c-0a9e9cfbff89" />

INi adalah bentuk output ketika user memilih opsi 3 yang berupa melihat data antrian pertama.

<img width="648" height="153" alt="image" src="https://github.com/user-attachments/assets/e987e79e-9a5a-4395-b04a-8006b630e7aa" />

Nah ini adalah bentuk user ketika salah memasukkan inputan, sistem akan memberikan peringatan tidak valid, dan akan menanyakan kembali menu yang akan dipilih oleh user.

<img width="866" height="205" alt="image" src="https://github.com/user-attachments/assets/3c7bd038-1291-44c3-a248-1f7db970ff5d" />

Ketika user ingin memasukkan lagi nama, tapi antrian sudah ada 7, maka sistem akan memberikan peringatan, nah kalau user memilih 'n' maka pengambilan antrian akan dibatalkan.

<img width="883" height="505" alt="image" src="https://github.com/user-attachments/assets/d8e894a2-0813-4761-8f64-6f06755f065f" />

Di sini ketika user mau lihat semua yang antri dan total yang antri sudah mencapai 7 maka sistem akan kasih tau bahwa status antrianya itu udah padat.

Lalu ketika user memilih menu ke 2 yang berarti menghapus data pertama, maka nama Fahra akan ditampilkan dan diarahkan untuk ke teller/cs, dan data pertama akan langsung digantikan dengan nama gojo.

Setelah itu, ketika user menampilkan keseluruhan antrian maka antrian menjadi status lancar, karena antrian suadh berkurang satu.

<img width="688" height="255" alt="image" src="https://github.com/user-attachments/assets/caaa1744-5d7e-4e0b-8095-1d45baec165e" />

Di Output ini user memilih menu ke 5 dimana menu tersebut berupa menu keluar, tapi sebelum sistemnya benar-benar selesai, sistem akan mengosongkan antriannya terlebih dahulu, setelah antriannya kosong, baru sistem akan selesai.

## Link YT

https://youtu.be/JGnSp5KO7yE
