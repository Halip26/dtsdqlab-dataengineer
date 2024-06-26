# 1. Pengantar
## Pengantar
Di masa pandemi seperti ini, kompetisi coding seperti Competitive Programming maupun Hackathon banyak diselenggarakan karena sangat memungkinkan untuk dilakukan secara online.

**Hackathon** merupakan kompetisi membuat perangkat lunak (software) yang dilaksanakan secara marathon yang biasanya diikuti secara tim. Umumnya, peserta hackathon diminta untuk mengembangkan platform (mobile, web, desktop, dll.) dalam kurun waktu tertentu untuk menyelesaikan permasalahan yang sudah ditetapkan/didefinisikan oleh penyelenggara ataupun berdasarkan tema yang dipilih oleh tim tersebut.

Untuk bisa mengikuti _hackathon_ dari suatu instansi, calon peserta diwajibkan untuk mendaftarkan diri mereka pada situs/form tertentu dengan memasukkan beberapa informasi yang diminta oleh penyelenggara tersebut.

Extract, Transform dan Load (ETL) merupakan kumpulan proses untuk "memindahkan" data dari satu tempat ke tempat lain.
Tempat yang dimaksud adalah dari sumber data (bisa berupa database aplikasi, file, logs, database dari 3rd party, dan lainnya) ke data warehouse.

Apa itu data warehouse?

Singkatnya, data warehouse merupakan database yang berisi data-data (tabel-tabel) yang sudah siap untuk dilakukan analisis oleh Data Analyst maupun Data Scientist.

Lebih lengkapnya bisa dilihat di:
https://en.wikipedia.org/wiki/Data_warehouse.

## Project yang akan dikerjakan
Pada proyek kali ini, Anda diminta untuk mengolah data pendaftar hackathon yang diselenggarakan oleh DQLab bernama DQThon.

Dataset ini terdiri dari 5000 baris data (5000 pendaftar) dengan format CSV (Comma-separated values) dan memiliki beberapa kolom diantaranya:

1. **participant_id**: ID dari peserta/partisipan hackathon. Kolom ini bersifat unique sehingga antar peserta pasti memiliki ID yang berbeda
2. **first_name**: nama depan peserta
3. **last_name**: nama belakang peserta
4. **birth_date**: tanggal lahir peserta
5. **address**: alamat tempat tinggal peserta
6. **phone_number**: nomor hp/telepon peserta
7. **country**: negara asal peserta
8. **institute**: institusi peserta saat ini, bisa berupa nama perusahaan maupun nama universitas
9. **occupation**: pekerjaan peserta saat ini
10. **register_time**: waktu peserta melakukan pendaftaran hackathon dalam second

Namun pada proyek ini nantinya Anda diminta untuk menghasilkan beberapa kolom dengan memanfaatkan kolom-kolom yang ada, sehingga akhir dari proyek ini berupa hasil transformasi data dengan beberapa kolom baru selain dari 10 kolom diatas.

Sebagai pemanasan dalam proyek ini, Anda dipersilakan untuk membuka isi datasetnya dan melihat values-nya. Jika sudah siap dengan perjalanan di proyek ini, silakan klik Next.

# 2. Transform Data
## Extract
Extract merupakan proses meng-ekstraksi data dari sumber, sumber data ini bisa berupa relational data (SQL) atau tabel, nonrelational (NoSQL) maupun yang lainnya.

Tugas Anda adalah baca terlebih dahulu dataset ini sebagai CSV agar nantinya bisa diolah. Gunakan live code editor untuk menampilkan dataset.

File tersebut bisa diakses melalui URL: **https://storage.googleapis.com/dqlab-dataset/dqthon-participants.csv.**

> ![image](https://user-images.githubusercontent.com/36031213/163110659-56701733-fea3-4398-83ef-db9320397306.png)

## Transform
Transform merupakan proses melakukan transformasi data, atau perubahan terhadap data. Umumnya seperti:
1. Merubah nilai dari suatu kolom ke nilai baru,
2. Menciptakan kolom baru dengan memanfaatkan kolom lain,
3. Transpose baris menjadi kolom (atau sebaliknya),
4. Mengubah format data ke bentuk yang lebih standard (contohnya, kolom date, maupun datetime yang biasanya memiliki nilai yang tidak standard maupun nomor HP yang biasanya memiliki nilai yang tidak sesuai format standardnya), dan lainnya.

## Transform Bagian I - Kode Pos
Ada permintaan datang dari tim logistik bahwa mereka membutuhkan kode pos dari peserta agar pengiriman piala lebih mudah dan cepat sampai. Maka dari itu buatlah kolom baru bernama postal_code yang memuat informasi mengenai kode pos yang diambil dari alamat peserta (kolom address).

Diketahui bahwa kode pos berada di paling akhir dari alamat tersebut.

Note:
Jika regex yang dimasukkan tidak bisa menangkap pattern dari value kolom address maka akan menghasilkan NaN.
> ![image](https://user-images.githubusercontent.com/36031213/163110822-0c284eeb-c820-4d3f-9400-c189d5a01290.png)

## Transform Bagian II - Kota
Selain kode pos, mereka juga membutuhkan kota dari peserta.

Untuk menyediakan informasi tersebut, buatlah kolom baru bernama city yang didapat dari kolom address. Diasumsikan bahwa kota merupakan sekumpulan karakter yang terdapat setelah nomor jalan diikuti dengan \n (newline character) atau dalam bahasa lainnya yaitu enter.
> ![image](https://user-images.githubusercontent.com/36031213/163111001-2f49a251-dcab-45b6-a0e4-76a2dfa951f8.png)

## Transform Bagian III - Github
Salah satu parameter untuk mengetahui proyek apa saja yang pernah dikerjakan oleh peserta yaitu dari _git repository_ mereka.

Pada kasus ini kita menggunakan profil _github _sebagai parameternya. Tugas Anda yaitu membuat kolom baru bernama **github_profile** yang merupakan _link _profil _github _dari peserta.

Diketahui bahwa profil github mereka merupakan gabungan dari **first_name **dan **last_name **yang sudah di-lowercase. 

> ![image](https://user-images.githubusercontent.com/36031213/163111154-4485b641-ac68-423a-9d99-8116cc881c1f.png)

## Transform Bagian IV - Nomor Handphone
Jika kita lihat kembali, ternyata nomor handphone yang ada pada data csv kita memiliki format yang berbeda-beda. Maka dari itu, kita perlu untuk melakukan cleansing pada data nomor handphone agar memiliki format yang sama. Anda sebagai Data Engineer diberi privilege untuk menentukan format nomor handphone yang benar. Pada kasus ini mari kita samakan formatnya dengan aturan:

1. Jika awalan nomor HP berupa angka 62 atau +62 yang merupakan kode telepon Indonesia, maka diterjemahkan ke 0.
2. Tidak ada tanda baca seperti kurung buka, kurung tutup, strip⟶ ()-
3. Tidak ada spasi pada nomor HP nama kolom untuk menyimpan hasil cleansing pada nomor HP yaitu **cleaned_phone_number**
> ![image](https://user-images.githubusercontent.com/36031213/163111374-4fbc3f9b-7c1d-41a5-a48e-0f3ff24e3e0a.png)

## Transform Bagian V - Nama Tim
Dataset saat ini belum memuat nama tim, dan rupanya dari tim Data Analyst membutuhkan informasi terkait nama tim dari masing-masing peserta.

Diketahui bahwa nama tim merupakan gabungan nilai dari kolom **first_name, last_name, country dan institute**.

Tugas Anda yakni buatlah kolom baru dengan nama **team_name **yang memuat informasi nama tim dari peserta.
> ![image](https://user-images.githubusercontent.com/36031213/163111536-8c3c8e7b-5357-42db-a37f-1edf29625ec5.png)

## Transform Bagian VI - Email
> ![image](https://user-images.githubusercontent.com/36031213/163111623-9cb7ec3a-88eb-4f13-a1f0-b0b0b4c9b732.png)
> ![image](https://user-images.githubusercontent.com/36031213/163112500-63b77876-f9a8-4d1f-b36d-6d776ec4091c.png)

https://codeshare.io/qPzmrk

## Transform Bagian VII - Tanggal Lahir
> ![image](https://user-images.githubusercontent.com/36031213/163113781-3ee18d4c-6f47-4042-bc91-22fa8e87fbc9.png)

> https://www.mysqltutorial.org/mysql-date/

> ![image](https://user-images.githubusercontent.com/36031213/163113939-d5dc248d-8619-4b83-9ae4-2065c91d317d.png)

https://codeshare.io/yo80Ml

## Transform Bagian VIII - Tanggal Daftar Kompetisi
> ![image](https://user-images.githubusercontent.com/36031213/163114905-0da48a50-0e6c-4963-b938-061256d078e2.png)
> ![image](https://user-images.githubusercontent.com/36031213/163114996-fa8d24ab-94a6-4b2e-840d-b067c509c4b9.png)

https://codeshare.io/nzJoWj

## Kesimpulan
Dengan begitu, tibalah kita di penghujung dari chapter bagian transform ini.

Jika dilihat kembali, dataset Anda saat ini sudah berbeda dengan saat proses extract sebelumnya. Ada beberapa kolom tambahan yang memanfaatkan nilai kolom lain.

Dataset Anda saat ini memuat kolom:

1. **participant_id**: ID dari peserta/partisipan hackathon. Kolom ini bersifat unique sehingga antar peserta pasti memiliki ID yang berbeda
2. **first_name**: nama depan peserta
3. **last_name**: nama belakang peserta
4. **birth_date**: tanggal lahir peserta (sudah diformat ke YYYY-MM-DD)
5. **address**: alamat tempat tinggal peserta
6. **phone_number**: nomor hp/telepon peserta
7. **country**: negara asal peserta
8. **institute**: institusi peserta saat ini, bisa berupa nama perusahaan maupun nama universitas
9. **occupation**: pekerjaan peserta saat ini
10. **register_time**: waktu peserta melakukan pendaftaran hackathon dalam second
11. **team_name**: nama tim peserta (gabungan dari nama depan, nama belakang, negara dan institusi)
12. **postal_code**: kode pos alamat peserta (diambil dari kolom alamat)
13. **city**: kota peserta (diambil dari kolom alamat)
14. **github_profile**: link profil github peserta (gabungan dari nama depan, dan nama belakang)
15. **email**: alamat email peserta (gabungan dari nama depan, nama belakang, institusi dan negara)
16. **cleaned_phone_number**: nomor hp/telepon peserta (sudah lebih sesuai dengan format nomor telepon)
17. **register_at**: tanggal dan waktu peserta melakukan pendaftaran (sudah dalam format DATETIME)

## Load
Pada bagian load ini, data yang sudah ditransformasi sedemikian rupa sehingga sesuai dengan kebutuhan tim analyst dimasukkan kembali ke database yaitu Data Warehouse (DWH). Biasanya, dilakukan pendefinisian skema database terlebih dahulu seperti:

1. Nama kolom
2. Tipe kolom
3. Apakah primary key, unique key, index atau bukan
4. Panjang kolomnya

Karena umumnya Data _Warehouse _merupakan database yang terstruktur sehingga mereka memerlukan skema sebelum datanya dimasukkan.

Pandas sudah menyediakan fungsi untuk memasukkan data ke _database _yaitu _to_sql_().

Detail dari fungsi tersebut bisa dilihat pada dokumentasi Pandas: **https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html**

# 3. Quiz
## Quiz 1
> ![image](https://user-images.githubusercontent.com/36031213/163116208-fa929edf-efb4-41e1-9120-3cbd5ef060c6.png)

## Quiz 2
> ![image](https://user-images.githubusercontent.com/36031213/163116287-c2037293-4310-49ea-855c-6d6cdf3536fe.png)

## Quiz 3
> ![image](https://user-images.githubusercontent.com/36031213/163116482-2887e089-11cd-4bad-b8e8-46166cf1e0c2.png)

## My certificate of completion
> ![image](/assets/certificate-DQLABDEPROGHEVVG.png)