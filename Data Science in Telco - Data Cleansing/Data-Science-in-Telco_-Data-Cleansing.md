# 1. Introduction
## Latar Belakang
DQLab Telco merupakan perusahaan Telco yang sudah mempunyai banyak cabang tersebar dimana-mana. Sejak berdiri pada tahun 2019, DQLab Telco konsisten untuk memperhatikan customer experience-nya sehingga tidak akan ditinggalkan pelanggan.

Walaupun baru berumur 1 tahun lebih sedikit, DQLab Telco sudah mempunyai banyak pelanggan yang beralih langganan ke kompetitor. Pihak management ingin mengurangi jumlah pelanggan yang beralih (churn) dengan menggunakan machine learning.

Oleh karena itu, tim Data Scientist diminta untuk mempersiapkan data sekaligus membuat model prediksi yang tepat untuk menentukan pelanggan akan berhenti berlangganan (churn) atau tidak

## Tugas dan Langkah
Sebagai seorang data scientist, kamu diminta untuk menyiapkan data sebelum dilakukan permodelan.

Pada tugas kali ini, kamu akan melakukan Data Preprocessing (Data Cleansing) bulan lalu, yakni Juni 2020.

Langkah yang akan dilakukan adalah,

1. Mencari ID pelanggan (Nomor telepon) yang valid
2. Mengatasi data-data yang masih kosong (Missing Values)
3. Mengatasi Nilai-Nilai Pencilan (Outlier) dari setiap Variable
4. Menstandardisasi Nilai dari Variable


# 2. Library dan Data yang Digunakan
## Library yang Digunakan
Pada analisis kali ini, akan digunakan beberapa package yang membantu kita dalam melakukan analisis data.

**1. Pandas**

Pandas (Python for Data Analysis) adalah library Python yang fokus untuk proses analisis data seperti manipulasi data, persiapan data, dan pembersihan data.

* _read_csv_() digunakan untuk membaca file csv
* _str.match_() digunakan untuk mencocokan dengan karakter tertentu
* _drop_() digunakan untuk menghapus
* _count_() digunakan untuk menghitung masing-masing variable
* _drop_duplicates_() digunakan untuk menghapus data duplicate rows
* _fillna_() digunakan untuk mengisi dengan nilai tertentu
* _quantile_() digunakan untuk melihat quantile ke tertentu
* _mask_() mengganti nilai tertentu jika kondisi memenuhi
* _astype_() mengubah tipe data
* _value_counts_() digunakan untuk menghitung unik dari kolom
* _sort_values_() digunakan untuk sort values
* _isnull_() digunakan untuk mendeteksi missing values
* _dropna_() digunakan untuk menghapus missing values
* _replace_() digunakan untuk mengganti nilai

**2. Matplotlib**

Matplotlib adalah library Python yang fokus pada visualisasi data seperti membuat plot grafik. Matplotlib dapat digunakan dalam skrip Python, Python dan IPython shell, server aplikasi web, dan beberapa toolkit graphical user interface (GUI) lainnya.

* _figure_() digunakan untuk membuat figure gambar baru

**3. Seaborn**

Seaborn membangun di atas Matplotlib dan memperkenalkan tipe plot tambahan. Ini juga membuat plot Matplotlib tradisional Anda terlihat sedikit lebih cantik.

* _box_plot_() digunakan untuk membuat box plot


## Data yang Digunakan
Untuk dataset yang digunakan sudah disediakan dalam format csv, silahkan baca melalui fungsi pandas di python df_load = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqlab_telco.csv')

 
Untuk detail datanya adalah sebagai berikut:

* _UpdatedAt _Periode of Data taken
* _customerID _Customer ID
* _gender _Whether the customer is a male or a female (Male, Female)
* _SeniorCitizen _Whether the customer is a senior citizen or not (1, 0)
* _Partner _Whether the customer has a partner or not (Yes, No)
* _Dependents _Whether the customer has dependents or not (Yes, No)
* _tenure _Number of months the customer has stayed with the company
* _PhoneService _Whether the customer has a phone service or not (Yes, No)
* _MultipleLines _Whether the customer has multiple lines or not (Yes, No, No phone service)
* _InternetService _Customer’s internet service provider (DSL, Fiber optic, No)
* _OnlineSecurity _Whether the customer has online security or not (Yes, No, No internet service)
* _OnlineBackup _Whether the customer has online backup or not (Yes, No, No internet service)
* _DeviceProtection _Whether the customer has device protection or not (Yes, No, No internet service)
* _TechSupport _Whether the customer has tech support or not (Yes, No, No internet service)
* _StreamingTV _Whether the customer has streaming TV or not (Yes, No, No internet service)
* _StreamingMovies _Whether the customer has streaming movies or not (Yes, No, No internet service)
* _Contract _The contract term of the customer (Month-to-month, One year, Two year)
* _PaperlessBilling _Whether the customer has paperless billing or not (Yes, No)
* _PaymentMethod _The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))
* _MonthlyCharges _The amount charged to the customer monthly
* _TotalCharges _The total amount charged to the customer
* _Churn_ Whether the customer churned or not (Yes or No)

## Import Library dan Dataset
> ![image](https://user-images.githubusercontent.com/36031213/163353625-22b327e5-95af-443b-b1a1-70b0c33d8833.png)
> ![image](https://user-images.githubusercontent.com/36031213/163353694-25b10b3f-6d75-4beb-bffd-91a41aad845f.png)

> https://storage.googleapis.com/dqlab-dataset/dqlab_telco.csv'

# 3. Mencari Validitas ID Number Pelanggan
## Memfilter ID Number Pelanggan Format Tertentu
> ![image](https://user-images.githubusercontent.com/36031213/163354290-d3178b46-d998-4867-affd-799b6564e6e5.png)
> ![image](https://user-images.githubusercontent.com/36031213/163354360-83ef4db5-975c-40ae-b6af-74bf7939f560.png)

## Memfilter Duplikasi ID Number Pelanggan
> ![image](https://user-images.githubusercontent.com/36031213/163354526-a17bff67-a0e8-45e8-97cf-3544a555f7d7.png)
> ![image](https://user-images.githubusercontent.com/36031213/163354597-221b30a7-7d57-42b8-9961-9602eca32b7a.png)

## Kesimpulan
Validitas dari ID Number pelanggan sangat diperlukan untuk memastikan bahwa data yang kita ambil sudah benar. Berdasarkan hasil tersebut, terdapat perbedaan jumlah nomor ID dari data pertama kali di load sampai dengan hasil akhir. Jumlah row data ketika pertama kali di load ada sebanyak 7113 rows dan 22 columns dengan 7017 jumlah ID yang unique. Kemudian setelah di cek validitas dari ID pelanggan, maka tersisa 6993 rows data

# 4. Mengatasi Missing Values
## Mengatasi Missing Value dengan Penghapusan Rows
> ![image](https://user-images.githubusercontent.com/36031213/163354830-7de2269c-bbe4-487e-9424-676a9926a3d1.png)
> ![image](https://user-images.githubusercontent.com/36031213/163354873-0dabba31-8244-455b-bcaf-f28deb0606b1.png)

## Mengatasi Missing Value dengan Pengisian Nilai tertentu
> ![image](https://user-images.githubusercontent.com/36031213/163355045-094ca6f4-73d7-4faa-971c-0ee4a5e85fba.png)
> ![image](https://user-images.githubusercontent.com/36031213/163355101-fda5427c-022c-4a56-b3db-0fa3ce7d3b4d.png)
> ![image](https://user-images.githubusercontent.com/36031213/163355179-d423bb71-3056-466c-b034-8199c452fffd.png)

## Kesimpulan
Setelah kita analisis lebih lanjut, ternyata masih ada missing values dari data yang kita sudah validkan Id Number pelanggannya. Missing values terdapat pada kolom Churn, tenure, MonthlyCharges & TotalCharges. Setelah kita tangani dengan cara penghapusan rows dan pengisian rows dengan nilai tertentu, terbukti sudah tidak ada missing values lagi pada data, terbukti dari jumlah missing values masing-masing variable yang bernilai 0. Selanjutnya kita akan melakukan penanganan pencilan (_outlier_)

# 5. Mengatasi Outlier
## Mendeteksi adanya Outlier (Boxplot)
> ![image](https://user-images.githubusercontent.com/36031213/163357065-3101a739-a015-45d8-a684-a0818c079a8c.png)
> ![image](https://user-images.githubusercontent.com/36031213/163357164-f81358d1-bf9f-4470-83d7-99be8f7bcaca.png)

> ![image](https://user-images.githubusercontent.com/36031213/163357338-31bf90a0-e299-4b5c-973b-44ca22cf0bfb.png)
> ![image](https://user-images.githubusercontent.com/36031213/163357375-36a51ce0-d162-45dd-ba21-1d4f31887799.png)
> ![image](https://user-images.githubusercontent.com/36031213/163357409-8f8b35eb-08c8-4a3d-95ef-7d2ce0894cb8.png)

> https://storage.googleapis.com/dqlab-dataset/dqlab_telco.csv

## Mengatasi Outlier
> ![image](https://user-images.githubusercontent.com/36031213/163357645-7c4f03e7-dd38-4bce-b4e6-507554c29684.png)
> ![image](https://user-images.githubusercontent.com/36031213/163357722-41a7781a-0337-4a2c-940c-cba78d9e91e9.png)

## Kesimpulan
Dari ketiga boxplot dengan variable 'tenure','MonthlyCharges' & 'TotalCharges' terlihat jelas bahwasannya ada outlier. Hal ini bisa di identifikasi dari adanya titik-titik yang berada jauh dari gambar boxplot-nya. Kemudian kalau kita liat persebaran datanya dari kolom **max** nya juga ada nilai yang sangat tinggi sekali.

Kemudian nilai outlier tersebut ditangani dengan cara merubah nilainya ke nilai maximum & minimum dari interquartile range (IQR). Setelah di tangani outlier-nya, dan dilihat perseberan datanya, terlihat sudah tidak ada lagi nilai yang outlier.

# 6. Menstandarisasi Nilai
## Mengatasi Nilai yang tidak Standar
> ![image](https://user-images.githubusercontent.com/36031213/163358036-e53bbabf-ac73-4c6e-95f2-26eabfdc006b.png)
> ![image](https://user-images.githubusercontent.com/36031213/163358155-5b6caf4d-4d5d-4543-a39b-3602e757fb3b.png)

## Menstandarisasi Variabel Kategorik
> ![image](https://user-images.githubusercontent.com/36031213/163358336-b6eb6aa0-02d1-46e3-81e4-4fd30985c61f.png)
> ![image](https://user-images.githubusercontent.com/36031213/163358455-742365c2-cc13-43db-a7d1-20c4d741bb03.png)

## Kesimpulan
Ketika kita amati lebih jauh dari jumlah unique value dari masing-masing variable kategorik, terlihat jelas bahwa ada beberapa variable yang tidak standar. Variable itu adalah:

* _Gender (Female, Male,_ Wanita, Laki-Laki), yang bisa di standardkan nilainya menjadi (Female, Male) karena mempunyai makna yang sama.
* _Dependents (Yes, No_, Iya), yang bisa di standardkan nilainya menjadi (Yes, No) karena mempunyai makna yang sama.
* _Churn (Yes, No, Churn)_, yang bisa di standardkan nilainya menjadi (Yes, No) karena mempunyai makna yang sama.
Setelah kita standardkan nilainya, dan kita amati kembali bentuk datanya, sudah terstandar dengan baik untuk unique value-nya.

## My certificate of completion
> ![image](/assets/certificate-DQLABAPL1ALOGFQ.png)
