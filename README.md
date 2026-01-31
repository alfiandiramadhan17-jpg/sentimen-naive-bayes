PROJECT UAS  
KLASIFIKASI SENTIMEN MENGGUNAKAN ALGORITMA NAIVE BAYES  

Project ini merupakan tugas Ujian Akhir Semester (UAS) pada mata kuliah Natural Language Processing (SIF405). Sistem yang dibangun bertujuan untuk melakukan klasifikasi sentimen terhadap teks komentar ke dalam tiga kategori sentimen, yaitu Positif, Netral, dan Negatif dengan menggunakan algoritma Naive Bayes.

INFORMASI MATA KULIAH  
Mata Kuliah : Natural Language Processing (SIF405)  
Tahun Ajaran : Ganjil 2025/2026  
Dosen Pengampu : Teuku Rizky Noviandy, S.Kom., M.Kom.

IDENTITAS MAHASISWA  
Nama : Alfiandi Ramadhan  
NIM  : 24146023  

DESKRIPSI PROJECT  
Sistem klasifikasi sentimen ini dibangun menggunakan bahasa pemrograman Python dan library machine learning Scikit-learn. Proses klasifikasi dilakukan dengan menerapkan algoritma Multinomial Naive Bayes yang cocok digunakan untuk data teks berbasis frekuensi kata. Sebelum dilakukan pelatihan model, data teks akan melalui tahapan preprocessing untuk meningkatkan kualitas data dan akurasi model.

DATASET  
Dataset yang digunakan berupa kumpulan komentar pengguna yang telah diberi label sentimen. Dataset disimpan dalam format CSV dengan dua kolom, yaitu review_text sebagai teks komentar dan sentiment sebagai label sentimen. Label sentimen terdiri dari:
0 = Negatif  
1 = Netral  
2 = Positif  

Dataset digunakan sebagai data latih dan data uji dalam proses klasifikasi.

PREPROCESSING TEKS  
Tahapan preprocessing teks yang diterapkan dalam project ini meliputi:
1. Case Folding, yaitu mengubah seluruh teks menjadi huruf kecil.  
2. Tokenizing, yaitu memecah teks menjadi kata-kata.  
3. Stopword Removal, yaitu menghapus kata-kata umum yang tidak memiliki makna penting dalam analisis sentimen.  
4. Stemming, yaitu mengubah kata ke bentuk dasar menggunakan Sastrawi Stemmer.

PEMBAGIAN DATASET  
Dataset dibagi menjadi dua bagian, yaitu data latih (training) dan data uji (testing) dengan rasio 80% data latih dan 20% data uji. Proses pembagian dataset dilakukan menggunakan fungsi train_test_split dari library sklearn.model_selection.

ALGORITMA NAIVE BAYES  
Algoritma yang digunakan adalah Multinomial Naive Bayes. Algoritma ini bekerja berdasarkan Teorema Bayes dengan asumsi bahwa setiap fitur bersifat independen satu sama lain. Data teks diubah menjadi representasi numerik menggunakan metode TF-IDF Vectorizer sebelum dilakukan proses pelatihan model.

EVALUASI MODEL  
Evaluasi performa model dilakukan menggunakan classification_report dari sklearn.metrics yang mencakup metrik:
- Accuracy  
- Precision  
- Recall  
- F1-Score  

Selain itu, ditampilkan confusion matrix untuk melihat hasil klasifikasi antara kelas sentimen aktual dan hasil prediksi model.

STRUKTUR PROJECT  
sentimen-naive-bayes  
├── alfiandi_ramadhan.py  
├── preprocessing.py  
├── train_model.py  
├── dataset_sentimen.csv  
└── README.md  

CARA MENJALANKAN PROGRAM  
1. Pastikan Python telah terinstall pada komputer.  
2. Install library yang dibutuhkan dengan perintah:
   pip install pandas scikit-learn nltk Sastrawi  
3. Jalankan program utama dengan perintah:
   python alfiandi_ramadhan.py  

Hasil evaluasi model akan ditampilkan langsung pada terminal.

KESIMPULAN  
Berdasarkan hasil pengujian, algoritma Naive Bayes mampu melakukan klasifikasi sentimen teks dengan cukup baik. Sistem ini dapat digunakan sebagai metode dasar dalam analisis sentimen berbasis teks dan dapat dikembangkan lebih lanjut dengan penambahan data serta metode klasifikasi lainnya.
