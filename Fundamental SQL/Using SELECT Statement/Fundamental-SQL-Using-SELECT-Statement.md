# Structured Query Language
## Modul SQL dari Senja
Senja baru saja menaruh tumpukan modul baru di mejaku. Kuintip, beberapa judulnya bertuliskan SQL. Seperti menjawab rasa keingintahuanku, Senja menyahut, “SQL adalah bahasa pemograman untuk pengolahan database. Fungsinya untuk memperbarui, membuat tabel, prosedur, dan sejenisnya. Makanya materinya banyak. Masih semangat?” 

“Yup,” jawabku mantap. Sejak dulu aku selalu menyukai data. Buatku, data adalah dasar pertimbangan tiap tindakan. Saat ada kesempatan belajar seperti ini, walau berat aku tidak akan menyerah.

## Pendahuluan
Aku menemukan tumpukan modul di meja kerjaku. Aku menemukan post-it kuning di atas modul itu yang bertuliskan:

“Buat jadi Data Analyst, enggak cukup mahir mengoperasikan Python aja. Semangat!”

Aku menaruh tas selempangku dan segera membuka laptop. Kalau baca modul saja enggak akan paham, aku terbiasa membaca sembari mempraktikkannya. Jadi, mari mulai belajar. Dear SQL, here we go!

## Apa itu SQL?
SQL yang merupakan singkatan dari Structured Query Language, yaitu bahasa komputer standar yang digunakan untuk berinteraksi dengan suatu **sistem database** - atau lebih tepatnya **sistem manajemen database relasional**. Jadi, user dapat menambahkan, mengubah, mengupdate, mencari dan menghapus data dari suatu sistem database dengan menggunakan SQL.

SQL dilafalkan dengan membaca tiap karakternya S Q L (es kiu el) atau sikuel.

## Quiz: 
> ![image](https://user-images.githubusercontent.com/36031213/163083922-dcb3f4b3-f99d-4df0-bddc-5595584f36bd.png)

## Contoh komunikasi SQL
Terdapat dua kategori dari interaksi SQL: 

* **Data Definition Language (DDL)**, yaitu berbagai perintah yang berfungsi lebih kepada memanipulasi struktur database, seperti Membuat (CREATE), meubah (ALTER), dan menghapus (DROP) struktur penyimpanan data, yaitu database, table, kolom dan tipe data.
* **Data Manipulation Language (DML)**, yaitu berbagai perintah yang digunakan untuk Menyisipkan data (INSERT), Mengambil data atau query (SELECT), Meubah data (UPDATE) dan Menghapus data (DELETE).

Berikut adalah satu contoh query atau perintah untuk mengambil data:

> `SELECT nama_produk FROM ms_produk;`

Dengan perintah tersebut, sistem database akan mengerti bahwa ‘dia’ harus menampilkan data ‘nama_produk’ dari suatu tabel yang namanya ‘ms_produk’ seperti berikut.

> ![image](https://user-images.githubusercontent.com/36031213/163084035-e4b70314-dd76-4b2c-947c-61f8666425a2.png)

Terlihat ada sepuluh nama peralatan kantor dengan label DQLab yang ditampilkan. Ini menunjukkan bahwa interaksi antara SQL dan sistem database telah berjalan dengan baik.

## Mengapa Perlu Belajar SQL?
“Halo, Aksara! Sudah baca modul barunya?” ujar Senja yang menghampiriku jelang makan siang.

Aku mengangguk sembari mengangkat modul. Selagi ada Senja, aku pun penasaran untuk bertanya. “Nja, kenapa sih data analyst perlu memahami SQL? Bukankah ada tools lain untuk analisis data, tapi kenapa harus SQL?”

“Begini, Aksara. Pada dasarnya, setiap perusahaan memiliki sistem penyimpanan data, khususnya untuk perusahaan yang memiliki sistem IT. Sistem penyimpanan ini bukan di komputer atau laptop dalam bentuk file atau folder, tetapi di suatu sistem database. Nah, sistem database ini biasanya diakses menggunakan SQL. Sebagai analyst, tugas kita tidak hanya menganalisa data yang sudah tersedia tetapi juga mampu untuk mengambil, memodifikasi dan mengakses sendiri data tersebut dari sumber datanya, yaitu dari database,” jelas Senja dengan rinci.  Bahkan, ia juga sempat memberiku buku catatannya padaku.

“Nih coba kamu baca. Selain yang tadi kujelaskan, penguasaan SQL akan membantu perusahaan pada area berikut,” tunjuk Senja pada salah satu halaman buku catatannya:

* Manajemen memerlukan laporan dengan informasi yang semakin beragam, seperti: tren penjualan bulan ke bulan, pertumbuhan pelanggan, apakah perusahaan mencapai target, dan lain-lain. Dan ini membutuhkan keahlian SQL yang mumpuni.
* Programmer yang membangun sistem aplikasi hampir dipastikan selalu bergantung kepada sistem database SQL agar aplikasinya berjalan dengan baik. Dengan demikian, penguasaan SQL adalah hal mutlak.
* Bisa meningkatkan kinerja perusahaan karena informasi yang kaya dapat dihasilkan melalui SQL.

“Jadi, untuk beberapa alasan inilah, maka tidak heran SQL menjadi keterampilan utama yang diminta oleh banyak perusahaan?” ujarku menyimpulkan.

Senja mengangguk puas. Aku pun kembali mempelajari isi modul.

## Quiz: 
> ![image](https://user-images.githubusercontent.com/36031213/163084116-3208e445-6f96-46e2-bbfb-802ec8f81dc5.png)

## Dimana saja SQL Digunakan?
Perusahaan – perusahaan yang sudah menerapkan sistem IT pasti memiliki sistem database dan bisa dipastikan menyimpan datanya dalam suatu database. Contohnya perusahaan berbasis teknologi, seperti e-commerce, menyimpan data baik itu data profile user, data transaksi pembelian dan penjualan, data produk dan data traffic kunjungan user ke halaman website di sistem database - atau lebih tepatnya sistem manajemen database atau database management system (DBMS).

Semua informasi ataupun analisa yang dibutuhkan oleh manajemen, umumnya bersumber dan diolah dari data DBMS ini. Dan di perusahaan, sistem database biasanya tidak hanya satu, bisa dua, tiga bahkan puluhan. Oleh karena itu, SQL sangat berperan disini, karena dengan menggunakan SQL dapat memenuhi kebutuhan manajemen tersebut. Tanpa penguasaan SQL  akan kesulitan memperoleh data yang dibutuhkan, dan akan kesulitan dalam melakukan analisa dan menghasilkan informasi yang dibutuhkan manajemen dan perusahaan.

Akan tetapi, perlu diketahui bahwa tidak semua sistem database mendukung SQL. Hanya sistem database berbasis relational database management system (RDBMS) yang mendukung bahasa ini. Untuk RDBMS sendiri akan dijelaskan kemudian.

**SQL hanya digunakan di sistem database berbasis Relational Database Management System**.

## Kesimpulan
SQL singkatan dari Structured Query Language, adalah sebuah **bahasa komputer** sederhana yang menjadi standar untuk memungkinkan seseorang berkomunikasi dengan suatu **sistem database manajemen relasional (RDBMS)**.

Karena RDBMS bisa dikatakan digunakan oleh sistem IT oleh seluruh perusahaan di dunia dan di Indonesia, maka pengetahuan SQL menjadi aset yang penting di perusahaan. Walaupun sederhana, aspek SQL sangat luas.

Aku semangat sekali, karena pada module Fundamental SQL using SELECT statement, aku akan mempelajari proses pengambilan data dengan pendekatan best practice yang dibutuhkan oleh mayoritas perusahaan di dunia dan Indonesia.

# Sistem Database Relasional
## Pendahuluan
“Dasar mengenai SQL sudah cukup paham, Aksara?”

“Sudah, ini baru saja selesai baca dan latihan soal,” sahutku sembari membuka halaman baru modul.

“Oke, berarti sekarang lagi belajar **R**elational **D**atabase **M**anagement **S**ystem ya? Itu bagian penting karea RDBMS ini perlu kamu kuasai sebelum mempraktikkan penggunaan SQL lebih lanjut.”

Aku jadi makin penasaran isi materinya!

## Apa Itu RDBMS ?
**R**elational **D**atabase **M**anagement **S**ystem yang biasa disingkat dengan RDMBS adalah suatu program yang memungkinkan untuk Membuat, Memperbarui, dan Mengelola suatu basis data relasional (Relational Database). Nah, Umumnya RDMBS ini menggunakan SQL untuk mengakses database.

Basis data relasional sendiri merupakan suatu jenis database dimana data – data umumnya disimpan dalam bentuk yang terstruktur berupa tabel (baris dan kolom) dan setiap tabel/ data yang terdapat dalam database memiliki relasi (relational) satu sama lain. Seperti terlihat pada gambar berikut

> ![image](https://user-images.githubusercontent.com/36031213/163084317-cf93cf4a-e4e5-4855-8b59-9fae99ff86a5.png)

Basis data relasional sangat popular dan banyak digunakan oleh perusahaan – perusahaan karena jenis database ini mudah dikelola terlebih jika memiliki banyak data atau informasi yang perlu disimpan, scalable dan flexibel.
* Basis data rasional cukup mudah dikelola. Setiap tabel/data dapat diupdate atau dimodifikasi tanpa mengganggu tabel/data yang lain.
* Flexible : jika perlu memperbarui data, hanya perlu melakukannya sekali saja - jadi tidak perlu lagi mengubah banyak file satu per satu. Selain itu, basis data rasional juga cukup mudah untuk di-extend. Misalnya saat data sudah semakin banyak, dapat dengan mudah memperbesar kapasitas dari database yang dimiliki.

## Produk-produk RDBMS di Pasaran
Selain MySQL, masih ada produk lain RDBMS, baik yang berbayar (proprietary) maupun open source. Berikut adalah sebagian produk yang cukup populer di pasaran :
* **MySQL**
Open-source SQL database yang cukup populer. Umumnya digunakan untuk pengembangan aplikasi web.
* **PostgreSQL**
Open-source RDBMS product, dan juga umumnya digunakan untuk pengembangan aplikasi web. Akan tetapi secara kinerja, postgreSQL lebih lambat dibandingkan  MySQL.
* **Oracle DB**
Produk RDBMS yang dimiliki oleh Oracle Corporation dan produk ini bersifat proprietary atau tidak open source. Oracle DB umumnya digunakan di industri perbankan.
* **Microsoft SQL Server** 
SQL Server adalah produk RDBMS yang dimiliki oleh Microsoft dan sama seperti Oracle DB, SQL Server bersifat proprietary atau tidak open source, SQL Server umumnya digunakan di perusahaan skala besar yang juga menggunakan produk keluaran Microsoft lainnya.
* **SQLite**
Open source RDBMS, umumnya digunakan sebagai database di handphone, MP3 player, and perangkat lainnya.

Selain itu, juga ada MariaDB yang juga gratis atau open source, IBM DB2, Microsoft Access, dan masih banyak lainnya.

Umumnya RDBMS menggunakan SQL untuk mengakses database dan produk RDBMS tidak hanya satu macam saja tetapi ada berbagai macam produk, maka SQL syntax pun bisa jadi sedikit berbeda untuk setiap produk tersebut. Berikut contoh perbandingan MySQL, Oracle, dan SQLSERVER untuk menampilkan beberapa baris data dari suatu tabel :

> ![image](https://user-images.githubusercontent.com/36031213/163084549-6eb0aa5a-d501-4e34-bc65-79ca1d285e71.png)

## Quiz:
> ![image](https://user-images.githubusercontent.com/36031213/163084635-283eb588-f8c4-4ea8-9301-dde3bb0fcf73.png)

## Struktur Penyimpanan RDBMS
Sebagai penyimpan data, sistem database relasional memiliki struktur hirarki objek penyimpanan sebagai berikut:

* Database
* Tabel (table)
* Kolom (column) atau Field

Dari sini aku belajar informasi menarik yaitu setiap database bisa berisi beberapa tabel, dan setiap tabel bisa terdiri dari beberapa kolom. Di setiap database, tabel dan kolom memiliki nama sendiri sebagai identitas mereka. Tabel dan kolom inilah yang akan diisi data yang kemudian membentuk row (baris data). 

## Quiz: 
> ![image](https://user-images.githubusercontent.com/36031213/163084891-f640de75-68ea-42a8-a676-86ab32a6cbe7.png)

## Tabel dan Kolom
Gambar berikut adalah contoh suatu Tabel dalam database. Karena setiap tabel dalam database memiliki nama, maka, nama tabel ini adalah **ms_produk**.

> ![image](https://user-images.githubusercontent.com/36031213/163084975-cf9d7003-f148-4894-814d-c169424665eb.png)

Jika aku perhatikan, struktur tabel **ms_produk** terdiri dari empat kolom (column), masing-masing dengan nama berikut:
* no_urut
* kode_produk
* nama_produk
* harga

Dan dalam tabel tersebut terdapat 10 baris data (row) dengan isi data yang bervariasi, contoh isi data untuk kolom **"nama_produk"** pada baris kelima adalah **"Gift Voucher DQLab 250rb"**.

## Quiz: Apa Nama Komponen Tabel Ini ?
> ![image](https://user-images.githubusercontent.com/36031213/163085228-4a72533f-31ef-486f-971c-01dd460afc4b.png)

## Quiz: Mana yang sisebut Sebagai row ?
> ![image](https://user-images.githubusercontent.com/36031213/163085324-77d2d514-1abb-42bb-8102-52119493a0b9.png)

## Kesimpulan
Wah ternyata seru sekali belajar SQL! 
Aku mulai membuka catataanku, mengambil pena, dan menuliskan apa yang aku pelajari:
1. Sistem relasional database atau relational database management system (RDBMS) adalah sistem database paling populer di dunia saat ini dan menggunakan bahasa SQL untuk pengolahannya.
2. Beberapa produk RDBMS yang terkenal antara lain adalah Microsoft SQL Server, Oracle, MySQL, PostgreSQL, IBM DB2, dan masih banyak lainnya.
3. Struktur penyimpanan data di RDBMS menggunakan hirarki:
* Database
* Tabel (Table)
* Kolom (Column)
4. Data akan diisi ke dalam table dalam bentuk Baris (Row) data
 
# Penggunaan Perintah SELECT… FROM…
## Pendahuluan
“Nja, aku sudah selesai dengan SQL dan RDMS. Sekarang mau lanjut ke materi SELECT. Ada catatan penting darimu soal materi lanjutan ini?” tanyaku karena biasanya Senja punya catatan khusus untuk tiap materi.

“Oh, sudah? Kalau mau pakai perintah SELECT untuk akses data, lebih baik belajarnya langsung praktik. Sini perhatikan, sambil bawa modulnya,”

## Mengambil Seluruh Kolom dalam suatu Tabel
“Jadi, bagaimana cara mengakses data dari database, Nja? Soalnya sejauh aku mencoba, aku sudah dapat hak akses tapi tidak paham cara membuka maupun mengakses tabel dan data dari database.”

Aku akhirnya menyampaikan kendalaku pada Senja.

“Untuk mengakses data di database, kita dapat menggunakan **SELECT** statement. Pada SELECT statement kita menyatakan kolom - kolom mana saja yang ingin kita tampilkan dari suatu tabel di database. SELECT statement tidak berdiri sendiri. Setelah menyatakan kolom - kolom yang ingin ditampilkan, kita melanjutkan dengan FROM. Di FROM inilah kita menyatakan dari tabel mana data yang ingin kita tampilkan berada. **SELECT… FROM…** adalah statement paling sederhana di SQL, dan merupakan bagian utama dari query. Kita tidak bisa meng-query data tanpa menggunakan statement ini,” jelas Senja.

Senja juga menunjukkan padaku Query dasar dan sederhana perintah SELECT yang berfungsi untuk menampilkan seluruh kolom, sebagai berikut:

> ![image](https://user-images.githubusercontent.com/36031213/163085600-a7d972b6-1670-43e6-a684-69e2b2e2c833.png)

* Kata awal, yaitu **SELECT** digunakan untuk menginformasikan kepada sistem bahwa kita ingin mengambil data. 
* Tanda * (bintang) artinya seluruh kolom perlu diambil dari tabel yang dirujuk. Tanda ini sering juga disebut sebagai **wildcard**.
* **FROM [NAMA_TABLE]**, artinya table yang akan diambil datanya.
* Tanda ; (titik koma) adalah tanda yang menyatakan akhir dari perintah SELECT atau SQL lain.
 
Senja mengajak aku untuk langsung mempraktekkan perintah SQL SELECT untuk menampilkan data pada tabel yang bernama **ms_produk**.

> ![image](https://user-images.githubusercontent.com/36031213/163085709-5682f274-2cc5-4942-9587-ba0db6ae1312.png)

> ![image](https://user-images.githubusercontent.com/36031213/163085824-04dfb086-df55-46cd-86cb-bd9db98814ce.png)

## Mengambil satu kolom dari tabel
Aku sudah cukup paham dengan penjelasan Senja tadi. Tapi, masih ada satu yang mengganjal. “Bagaimana kalau aku hanya ingin menampilkan satu kolom saja dari suatu tabel/data, Nja?”

“Secara umum penggunaan perintah SELECT untuk mengambil satu kolom dinyatakan oleh sintaks berikut ini,” ujar Senja sambil menggeser layar laptopnya agar bisa kuperhatikan:

> ![image](https://user-images.githubusercontent.com/36031213/163085952-99aa2333-94d1-4f5e-aab3-81e49fa3d45d.png)

“Kita coba ya dengan menampilkan data pelanggan yang ada di database. Kita sudah menggunakan perintah SELECT sebelumnya untuk mengambil seluruh kolom. Nah, berikut adalah contoh query untuk mengambil satu kolom saja yaitu nama_produk,” tambah Senja.

Aku mencatat beberapa tampilan penting yang menjadi contoh dari Senja buatku.

Ketikkan perintah berikut pada code editor dan kemudian klik tombol **Run**,

> ![image](https://user-images.githubusercontent.com/36031213/163086031-39e98b71-c219-4b4e-b503-3e554f1217b6.png)

> ![image](https://user-images.githubusercontent.com/36031213/163086095-35b4decf-cb22-4739-b04b-318eba708498.png)

## Quiz: 
> ![image](https://user-images.githubusercontent.com/36031213/163086191-7bec8fcd-84a7-4316-9b65-60a9a53aa00b.png)

## Mengambil lebih dari satu kolom dari tabel
Tabel **ms_produk** memiliki lebih dari satu kolom data. Kalau aku ingin mengambil kolom lainnya, aku hanya perlu menuliskan tiap kolom yang ingin ditampilkan dipisahkan dengan tanda koma, seperti contoh berikut untuk dua kolom.

Menggunakan tabel **ms_produk**, aku menggunakan perintah SELECT berikut untuk menampilkan dua kolom, **kode_produk** dan **nama_produk**

> ![image](https://user-images.githubusercontent.com/36031213/163086785-13a59673-6fc2-4032-8f11-27e7e89041ec.png)

Terlihat data dengan dua kolom ditampilkan yaitu kode_produk dan nama_produk. Jumlah data yang dikeluarkan masih sepuluh, sesuai dengan jumlah seluruh row yang terdapat pada tabel ms_produk.

### Tugas:
Sekarang gantilah perintah SELECT di code editor untuk menampilkan nama_produk dan harga dari tabel yang sama. Ingat untuk memisahkan setiap kolom dengan comma (,).

Jika berjalan dengan lancar, maka hasilnya akan terlihat sebagai berikut.
> ![image](https://user-images.githubusercontent.com/36031213/163087326-703c62bb-afa0-4e26-9ffb-31be1c42b0ed.png)

> ![image](https://user-images.githubusercontent.com/36031213/163087361-1ebe4ef0-9865-4922-abf7-e5107a25f173.png)

## Quiz: 
> ![image](https://user-images.githubusercontent.com/36031213/163087523-4c4eb07a-5815-427a-9d8d-4d929cf2dceb.png)

## Membatasi pengambilan Jumlah Row Data
Selain pembatasan kolom, aku bisa membatasi jumlah baris data yang diambil. Seperti yang aku pelajari di materi RDMS sebelumnya, bahwa untuk tiap produk RDBMS, caranya agak berbeda-beda. Untuk MySQL dan PostgreSQL, aku dapat menggunakan LIMIT. Secara umum syntaxnya dinyatakan sebagai berikut

> ![image](https://user-images.githubusercontent.com/36031213/163087654-6a4ec4b7-1b24-4c36-8d80-82c3bb6b97fc.png)

Sebagai contoh, aku bisa menggunakan perintah LIMIT untuk membatasi pengambilan data dari tabel **ms_produk **sebanyak tiga baris data (row).

> ![image](https://user-images.githubusercontent.com/36031213/163087759-dd6264ec-429a-43a7-ae8f-e3199d32ae36.png)

Jika berjalan dengan lancar, akan terlihat hasil tiga data pertama yang ditampilkan seperti berikut
Terlihat hanya tiga baris data pertama yang ditampilkan dari keseluruhan sepuluh baris data yang ada.

### Tugas:
> ![image](https://user-images.githubusercontent.com/36031213/163087848-0d91d2f7-6bbf-40d9-a047-51feaef5acb6.png)

> ![image](https://user-images.githubusercontent.com/36031213/163087927-c23a4afc-1deb-465c-a345-d5d2951d9e69.png)

## Quiz: 
> ![image](https://user-images.githubusercontent.com/36031213/163088222-b557c21d-8997-410e-b96e-679e4f1ebd20.png)

## Penggunaan SELECT DISTINCT statement
Aku diminta mengambil data dari tabel ms_pelanggan oleh Senja. Menggunakan perintah yang telah dipelajari, aku menuliskan Syntax pada Live Code Editor:

> ![image](https://user-images.githubusercontent.com/36031213/163088283-efd6fe5f-70ee-4ea7-bf81-4f7f429cd58e.png)

Ternyata, dari data pelanggan, aku menemukan duplikasi data, dalam nama_customer dan alamat untuk no_urut 3 & 11, serta 5 & 12 yang sama persis dengan kode_pelanggan yang berbeda. Tentunya ini akan berdampak pada hasil analisaku nantinya.

> ![image](https://user-images.githubusercontent.com/36031213/163088332-90065da5-5b8d-43a2-be46-d16d364e3655.png)

Untuk menghilangkan data duplikasi, aku bisa menggunakan **SELECT DISTINCT** statement. Dengan **SELECT DISTINCT**, data yang sama atau duplikat akan dieliminasi dan akan ditampilkan data yang unik saja.
Berikut syntax-nya:

> ![image](https://user-images.githubusercontent.com/36031213/163088421-ad4d5fa2-c578-49e5-a635-897fb18e91ed.png)

### Tugas:
> ![image](https://user-images.githubusercontent.com/36031213/163088615-063cdca1-37f2-406d-832b-29c3d48fe53a.png)

> ![image](https://user-images.githubusercontent.com/36031213/163088660-414b7aca-f306-4cf9-9268-b4c0ffbee1af.png)

## Kesimpulan
Aku mengambil catatanku, dan mulai menulis apa yang aku pelajari, sebelum aku melanjutkan belajarku:
1. Perintah SELECT dapat digunakan untuk menentukan apa saja kolom yang akan diambil dengan menuliskan nama-nama kolom yang diinginkan menggunakan pemisah tanda koma.
2. Perintah SELECT juga dapat digunakan untuk membatasi jumlah data yang dikeluarkan. Namun untuk berbagai produk bisa berbeda penulisannya. MySQL menggunakan LIMIT untuk tujuan tersebut.
3. Perintah SELECT DISTINCT dapat digunakan untuk menghilangkan duplikasi baris dalam tabel dan hanya menampilkan baris data yang unik tanpa duplikasi.

# Prefix dan Alias
## Pendahuluan
Sejauh ini, aku sudah cukup paham cara menggunakan SQL dengan perintah SELECT, terutama untuk mengakses data dari database. Aku pun berniat untuk mengambil dan menganalisis data produk dengan syntax yang ada:

> `SELECT t1.kode_produk AS product_code, t1.nama_produk AS product_name, t1.harga AS price FROM ms_produk AS t1;`

Beberapa detik aku termenung melihat syntax ini. Mengapa ada **‘t1’**, dan **‘AS’?** Apa maksudnya? Aku terdorong untuk bertanya kembali pada Senja.

“Nja, sorry gangguin kamu lagi. Aku lagi mau nyoba latihan nih. Tapi aku nemu syntax ini dan agak bingung terutama karena ada ‘t1’, dan ‘AS’. Maksudnya?”

“Oh, ini hanya variasi penggunaan nama table dan kolom pada bagian SELECT. Sini saya kasih tahu.”

Aku pun mencatat penjelasan Senja, walau sederhana tapi penting:
* **Prefix**, dimana kita akan menambahkan nama tabel di depan nama kolom.
* **Alias**, dimana kita memberikan alias atau nama lain untuk tabel maupun kolom.

## Menggunakan Prefik pada Nama Kolom
“Agar kamu lebih jelas, saya coba praktikkan untuk kamu ya, Aksara.  Pertama, kita mulai dengan menggunakan prefix pada kolom. Pada dasarnya, penulisan nama kolom yang lengkap perlu mencantumkan nama tabel di depan nama kolom tersebut, dengan tanda penyambung berupa tanda titik. Umumnya, jika kita hanya mengambil kolom dari satu tabel, prefix ini jarang digunakan karena sudah jelas dari tabel mana kolom itu berasal. Tetapi ketika kita mengambil data dari dua tabel, misalnya dengan menggabungkan 2 tabel menggunakan JOIN, dan terdapat 2 kolom dengan nama yang sama, maka penggunaan prefix menjadi penting untuk menghindari error karena ambiguitas,” jelas Senja panjang lebar.

Aku masih menyimak pada layar laptop Senja yang menunjukkan syntax dasar dari penggunaan prefix pada nama kolom.

> ![image](https://user-images.githubusercontent.com/36031213/163088995-7a44e551-64f7-48ad-bf28-acb8522ac57a.png)

Untuk mengambil nama kolom nama_produk data dari tabel ms_produk dengan penulisan prefix nama tabel adalah sebagai berikut

> ![image](https://user-images.githubusercontent.com/36031213/163089058-6d97b4e6-5bcc-4443-83b0-42c4a98ff02a.png)

### Tugas:
![image](https://user-images.githubusercontent.com/36031213/163089137-b1a150eb-eb6b-41cf-8931-9e5521790920.png)

> ![image](https://user-images.githubusercontent.com/36031213/163089209-331ad3db-05dc-44fc-b2fd-5813f4a2736e.png)

## Quiz: 
> ![image](https://user-images.githubusercontent.com/36031213/163089389-495d1227-cedf-48b1-a8c1-d3ed5a593b5e.png)

## menggunakan alias pada kolom
Selain prefix, aku dapat mengubah identitas nama kolom yang diambil dengan SELECT dengan menggunakan keyword AS. Ini dinamakan alias. Perubahan nama tabel bersifat temporary, artinya hanya berubah ketika mengambil/meng-query data, sedangkan nama kolom di tabel dalam database tidak akan berubah.

> ![image](https://user-images.githubusercontent.com/36031213/163089472-e08a68d2-8176-4ffa-bfdd-7f8cf6c23728.png)

Berikut adalah contoh untuk mengubah nama kolom dari **kode_produk** menjadi **product_code** dari table **ms_produk**.
> ![image](https://user-images.githubusercontent.com/36031213/163089614-d52697f4-bc7b-4ebe-9933-2ff4dfc59555.png)

### Tugas:
> ![image](https://user-images.githubusercontent.com/36031213/163089673-7cdf770b-6664-4fc6-aaf4-b8d7fc023e1b.png)

> ![image](https://user-images.githubusercontent.com/36031213/163089764-c81f9c93-d0f6-4ee2-958a-a5a84b44bdf0.png)

## Quiz: 
> ![image](https://user-images.githubusercontent.com/36031213/163089887-ad5f9a84-2640-4480-adf1-4fb1ee1ef678.png)

## Menghilangkan Keyword "AS"
Keyword **AS** yang digunakan sebagai penanda alias pada kolom dapat dihilangkan dengan syntax:

![image](https://user-images.githubusercontent.com/36031213/163089937-90bdaf7d-70ae-424d-9f71-5bba269fabcb.png)

Berikut adalah contoh yang sama dari sub-chapter sebelumnya, dimana untuk mengubah nama kolom dari **kode_produk** menjadi **product_code** dari tabel ms_produk dapat dilakukan tanpa menggunakan alias.

> ![image](https://user-images.githubusercontent.com/36031213/163090778-e992b5c1-7c1f-40be-8692-5c2250c62bfb.png)

### Tugas:
> ![image](https://user-images.githubusercontent.com/36031213/163090821-e297fda8-e38f-4e81-a945-f27c906ff2ad.png)
> ![image](https://user-images.githubusercontent.com/36031213/163090870-b8b15005-479f-4f50-99cb-c64442c528f9.png)

## Quiz: 
> ![image](https://user-images.githubusercontent.com/36031213/163090963-31dbcdf0-d85b-4cfc-a023-e2e844ed81c3.png)

## Menggabungkan Prefik dan Alias

Prefix dan alias juga dapat digunakan secara bersamaan.

> ![image](https://user-images.githubusercontent.com/36031213/163091058-06f411dd-4b2d-4112-9575-cf4219e4cece.png)

Aku menerapkannya dengan tabel ms_produk, menggunakan prefix nama tabel dan alias untuk merubah nama_produk menjadi nama. 

![image](https://user-images.githubusercontent.com/36031213/163091096-a5469618-7c4b-4352-99e0-7b444e630d01.png)

### Tugas:
> ![image](https://user-images.githubusercontent.com/36031213/163091180-f1c23afd-8e0e-4b30-8fda-92a489ab5b8e.png)

## Menggunakan Alias Pada Tabel
Selain kolom, nama alias juga bisa digunakan untuk tabel dengan menggunakan keyword AS setelah nama tabel. Dan, keyword ini juga bisa digunakan atau tidak. Umumnya penggunaan alias pada tabel jika nama tabel tersebut cukup panjang dan muncul atau dirujuk beberapa kali dalam query. Sehingga dengan menggunakan alias pada tabel, dapat menghemat waktu dalam menuliskan query, khususnya untuk query yang cukup rumit, panjang dan melibatkan banyak tabel.

Penulisannya adalah sebagai berikut.

> ![image](https://user-images.githubusercontent.com/36031213/163091318-11c63033-b684-48b1-80aa-24757b27d506.png)

![image](https://user-images.githubusercontent.com/36031213/163091352-30744e85-698d-4a38-9e16-5a9a3d545249.png)

> ![image](https://user-images.githubusercontent.com/36031213/163091416-05905343-419b-4e71-9359-37b461a02bf4.png)

## Prefik dengan Alias Tebel
Aku menyela sebentar penjelasan Senja karena masih penasaran mengenai Prefix ini.

“Nja, kalau kita menggunakan alias tabel, maka nama prefix yang digunakan untuk kolom adalah alias tabel dan bukan nama original tabel, seperti yang ditunjukkan berikut ini. Gimana hasilnya?”

> ![image](https://user-images.githubusercontent.com/36031213/163091569-0a207e28-cc38-4891-9493-6a09f7bb3f77.png)

“Penggunaan nama original tabel sebagai prefix akan menimbulkan error saat query dijalankan karena dengan penggunaan alias, nama tabel secara temporary sudah di-gantikan oleh alias, Aksara,” jawab Senja lugas.

Aku mengangguk. Senja pun kembali melanjutkan penjelasannya.

Mari lihat contoh berikut ini dari tabel ms_produk yang telah digunakan sebelumnya

> ![image](https://user-images.githubusercontent.com/36031213/163091624-fde9632f-0bf4-4b11-8948-b3e61d1601d6.png)

Jika kolom dan tabel memiliki alias, dapat dilakukan dengan mengetikkan perintah berikut di code editor

> ![image](https://user-images.githubusercontent.com/36031213/163091723-16b879c1-613e-4418-a3fa-be3fc800c11b.png)

### Tugas:
> ![image](https://user-images.githubusercontent.com/36031213/163091768-66aa4f2e-5e25-436a-8776-e40feae07bfc.png)

## Quiz: 
> ![image](https://user-images.githubusercontent.com/36031213/163092746-ff7c120a-77b1-47c4-88bc-f691aa79d213.png)

## Kesimpulan
Aku kembali mengambil catatanku dan menuliskan apa yang telah aku pelajari:

1. Perintah SELECT dapat ditulis dengan variasi identitas kolom dan tabel berupa prefix dan alias.
* Penulisan lengkap untuk nama kolom adalah prefix berupa nama tabel disertai tanda titik sebelum nama kolom itu sendiri.
* Alias adalah nama lain yang diberikan untuk kolom maupun tabel.
* Alias dapat digunakan dengan keyword AS atau tanpa keyword AS setelah nama kolom dan tabel.
* Prefix nama tabel bisa menggunakan alias.

Pemahaman mengenai prefix dan alias akan mendorong kemampuan identifikasi tabel maupun kolom yang terlibat untuk perintah SELECT yang lebih kompleks.

# Menggunakan Filter
## Pendahuluan
 “Nja, sampai sini aku sudah paham bagaimana menggunakan alias dan prefix. Tapi aku masih ada pertanyaan. Terkadang kita hanya ingin menampilkan data berdasarkan kondisi tertentu, jadi kita tidak butuh semua data dari tabel. Kalau seperti itu, berarti kita hanya ingin mengambil data produk dengan nama produk tertentu. Nah, di SQL caranya gimana ya?” tanyaku. Hal ini sedari tadi membuatku penasaran.

“Untuk case dimana kita ingin mengambil data berdasarkan kondisi tertentu saja, kita bisa menggunakan filter. SQL memiliki fungsi filter dengan menggunakan klausul WHERE. Jika kondisi WHERE terpenuhi, maka hasil query hanya akan menampilkan data yang sudah terfilter.”

Seperti biasa, aku akan lebih memahami Senja jika ada praktik yang menyertai penjelasannya. Jadi kusampaikan saja, “Nja, boleh sekalian praktik enggak?”

Senja hanya tersenyum dan hafal kebiasaanku. “Oke, biar lebih mudah dipahami, selanjutnya kita akan mempraktikkan bagaimana menggunakan klausul WHERE.”

Aku pun segera membuka modul bagian klausul WHERE:

Klausul WHERE untuk:

* Filter data dengan kondisi teks tertentu.
* Filter data dengan nilai angka tertentu.
* Filter data dengan dua kondisi menggunakan operator AND dan OR.

## Menggunakan Where
Klausul WHERE dari SELECT digunakan untuk memfilter data berdasarkan kondisi tertentu. Untuk syntax lengkapnya adalah sebagai berikut.

> ![image](https://user-images.githubusercontent.com/36031213/163092863-e71ed1ed-b2ca-4301-bae7-60f0f5fe347a.png)

Kondisi paling sederhana memiliki format sebagai berikut
> ` [nama_kolom] = 'nilai_untuk_filter'`

Biar lebih jelasnya, mari langsung contohkan dengan perintah berikut.
> ![image](https://user-images.githubusercontent.com/36031213/163092952-765417e9-e9d4-4519-b542-16a5ad5a5a78.png)

## Menggunakan Operator OR
Pada subbab sebelumnya, aku telah menggunakan filter teks sederhana untuk mengeluarkan data masing-masing dengan nama_produk 'Gantungan Kunci DQLab' dan 'Tas Travel Organizer DQLab'.

Pertanyaannya, bagaimana jika ingin mengeluarkan keduanya sekaligus? Aku bisa menggunakan Operand OR
> ![image](https://user-images.githubusercontent.com/36031213/163093499-fdddd8f8-594c-4d64-9287-7c151e5cf45a.png)

Untuk memunculkan hasil query yang memuat data produk dengan nama_produk 'Gantungan Kunci DQLab' dan 'Tas Travel Organizer DQLab', aku dapat menggunakan logika sederhana, yaitu: Aku perlu mengambil data dengan kondisi nama_produk itu bernilai 'Gantungan Kunci DQLab' ATAU 'Tas Travel Organizer DQLab'. Logika ini bisa dinotasikan dengan menggunakan logika **OR**.

Sehingga, dengan menggunakan logika **OR**, aku dapat menggabungkan dua atau lebih kondisi untuk memfilter data. Jadi, untuk menyelesaikan problem yaitu memunculkan data dengan kondisi kolom nama_produk bernilai 'Gantungan Kunci DQLab' ATAU 'Tas Travel Organizer DQLab', dapat menggunakan syntax berikut:

> ![image](https://user-images.githubusercontent.com/36031213/163094219-364a61b9-8cda-4752-928b-8c1e4e767dee.png)

## Filter Untuk Angka
Sebelumnya, aku telah melakukan filtering untuk teks, namun WHERE tidak terbatas untuk tipe data teks saja tapi malah umumnya untuk angka.

Berikut adalah contoh filter dimana kolom harga harus memiliki nilai di bawah 50000.

> `Select * From ms_produk WHERE harga < 50000`

Jika dijalankan, maka aku akan mendapatkan tiga baris data sebagai berikut.

> ![image](https://user-images.githubusercontent.com/36031213/163094454-2a8a4e94-e1ec-4140-bb4d-01470656bf7f.png)

### Tugas:
> ![image](https://user-images.githubusercontent.com/36031213/163094495-ed51ce25-2ee0-48dc-8202-9f7ecb76cb79.png)

## Menggunakan Operator END

Jika sebelumnya aku mempelajari Operand OR, aku juga bisa menggunakan operand AND agar dua atau lebih kondisi terpenuhi semuanya. Jika salah satu kondisi tidak terpenuhi, data tidak akan diambil. Secara umum syntaxnya diilustrasikan berikut ini

> ![image](https://user-images.githubusercontent.com/36031213/163095679-f3b1d07a-cd06-495c-ad7a-be68d4ae5905.png)

Berikut adalah contoh dimana kedua kondisi digunakan dengan penghubung AND.

> ![image](https://user-images.githubusercontent.com/36031213/163094705-b604bb36-c12d-4574-9e92-b28d5b8db21c.png)

### Tugas:
> ![image](https://user-images.githubusercontent.com/36031213/163094767-58380cac-1292-4b76-abee-bcee775e369e.png)

## Quiz: 
> ![image](https://user-images.githubusercontent.com/36031213/163094908-5b8ff5f4-fc3a-47f5-b1fe-f0e9d771c81e.png)

## Quiz: 
> ![image](https://user-images.githubusercontent.com/36031213/163094980-a550bee1-488c-44d8-9248-cbfa62bb8d01.png)

## Kesimpulan
Wah, semakin seru saja nih belajar SQL! Sebelum aku lupa, aku mencatat apa yang aku pelajari tadi. Siapa yang punya kebiasaan seperti aku? Dengan mencatat apa yang aku pelajari, aku merasa ilmu yang aku pelajari tadi lebih mudah untuk aku pahami.
1. Filter di SQL diimplementasikan dengan menggunakan WHERE diikuti dengan satu atau lebih kondisi logis.
2. Kondisi logis ini memiliki format nama kolom diikuti dengan nilai yang akan difilter. Untuk teks sederhana bisa menggunakan tanda sama dengan, sedangkan untuk nilai angka bisa menggunakan operator perbandingan matematika.
3. Aku juga bisa menggunakan operand OR dan AND untuk menggabungkan beberapa kondisi menjadi satu kondisi baru yang harus terpenuhi untuk pengambilan data.

# Mini Project
## Pendahuluan
“Oke, selamat Aksara! Materi SQL untuk hari ini sudah selesai dan saya lihat kamu bisa mengikutinya dengan baik,” puji Senja.
“Ini juga berkat penjelasan dan bimbinganmu, Nja.” Dalam hati aku kembali menobatkan Senja sebagai mentor terbaik!
“Agar kemampuan di SQL lebih teruji lagi, bagaimana kalau kamu membantu saya menangani proyek baru dari cabang A ini?”
Aku menggeser bangku ke sebelah Senja untuk melihat tabel yang ditunjukkannya.

## Proyek dari Cabang A
“Jadi, apakah kamu bisa menyiapkan data transaksi penjualan dengan total revenue >= IDR 100.000? 

Format datanya yang akan kamu tampilkan adalah: **kode_pelanggan, nama_produk, qty, harga, dan total**, serta diurutkan mulai dari total revenue terbesar,” pinta Senja padaku.

Kalau kasusnya seperti ini, berarti aku perlu meng-query data tersebut dari tabel **tr_penjualan** yang terdapat di database perusahaan.

Aku dapat melakukan
* perkalian antara kolom qty dan harga untuk memperoleh total revenue setiap kode pelanggan yang dinyatakan ke dalam kolom total, dan
* menggunakan “ORDER BY total DESC” pada akhir query untuk mengurutkan data.
 
Aku pun menerima tantangan proyek ini! Senja pun segera mengirim detailnya melalui email yang berisi contoh tabel sebagai berikut untuk segera kukerjakan.

> ![image](https://user-images.githubusercontent.com/36031213/163095223-506f60ee-2152-42e6-987c-9bf76df939a3.png)

> ![image](https://user-images.githubusercontent.com/36031213/163095251-0bb26003-6c0d-40c4-bfe2-943a7513d5ea.png)

## Hasil Belajarku
Wah seru sekali bagian pertama dari Module SQL ini! Dari materi yang telah aku pelajari dalam 'Fundemental SQL using SELECT Statement', aku telah memahami dan mampu mempraktekkan:

1. Konsep SQL, yaitu:
* Konsep Sistem Database Relasional atau Relational Database Management System (RDBMS).
* Struktur penyimpanan RDBMS yang terdiri dari database, tabel, kolom (column) dan baris (row).
* Pengenalan perintah SELECT untuk mengambil data dari tabel.
2. Teknik SELECT, dimana aku dapat:
* Mengambil kolom tertentu.
* Mengambil jumlah data tertentu.
* Menggunakan prefix dan alias.
* Menggunakan filter.

Dengan kemampuan ini, aku telah siap untuk mengambil dan mengolah data secara sederhana. Keterampilan ini sendiri adalah 60% aktivitas awal yang akan dilakukan seorang analis.

## My certificate of completion
> ![image](/assets/certificate-DQLABSQLT1QUJLJA.png)