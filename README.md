# 🌟 Real-Time Mood Scanner 🌟

## 👥Anggota Kelompok  
| No | Nama                              | NIM          | ID                           |
|----|-----------------------------------|--------------|------------------------------|
| 1  | Giovanni Lucy Faustine Sitompul   | 121140060    |  060giovanni                 |
| 2  | Qaisya Dwi Aryana                 | 121140063    |  qaisyadwi                   |
| 3  | Marsella Yesi Natalia Sinaga      | 121140174    |  MarsellaSinaga121140174     |

## 📝Deskripsi Singkat  
Proyek Real-Time Mood Scanner adalah filter yang mendeteksi ekspresi wajah pengguna secara real-time menggunakan Mediapipe dan OpenCV.  Berdasarkan ekspresi (senyum, sedih, kaget, atau netral), filter menampilkan visual interaktif seperti animasi bunga, hujan, petir, atau perubahan latar belakang lainnya.  Sistem ini bekerja dengan mendeteksi landmark wajah melalui Mediapipe, lalu menampilkan efek visual yang sesuai secara real-time menggunakan OpenCV.  


## 📋Logbook Mingguan

| Minggu  | Progress                                                                                     | Update project                                                       |
|---------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| **1** | Membuat file `main.py` sebagai skrip utama untuk menjalankan aplikasi.                    | Fitur dasar seperti pengaturan proyek awal dan antarmuka awal selesai. |
| **2** | Membuat file `datagen.py` untuk menghasilkan data pelatihan, dan file `data.csv` untuk menyimpan data yang dihasilkan. | Dataset awal berhasil dibuat dan siap digunakan untuk pengujian. |
| **3** | Membuat `training.py` untuk mencatat metrik training. | Berhasil membuat facemesh | 
| **3** | Memperbarui `main.py`. | Menyesuaikan `main.py` dengan facemesh yang lebih akurat. | 
                                                              


## **Instruksi Instalasi**

### **Langkah Instalasi**

Berikut revisi langkah instalasi dengan penambahan tautan untuk unduh data pada nomor 3:  

---

1. **Kloning Repositori**  
   ```bash
   git clone https://github.com/qaisyadwi/RealTimeMoodScanner_MUL.git
   ```

2. **(Opsional) Buat Virtual Environment**  
   Langkah ini direkomendasikan untuk menjaga dependensi proyek tetap terisolasi.  
   ```bash
   python -m venv env
   source env/bin/activate  # Untuk Linux/MacOS  
   env\Scripts\activate    # Untuk Windows  
   ```

3. **Unduh Background dan Siapkan File Video**  
   - Unduh background dan file video dari tautan berikut:  
     [Unduh data](https://drive.google.com/drive/folders/1NZr_wdj6qoDXZjH7Wx_QERgHH23408bc?usp=sharing)  
   - Masukkan file di folder data ke folder RealTimeMoodScanner_MUL

4. **Instal Dependensi**  
   Instal semua pustaka yang diperlukan:  
   ```bash
   pip install -r requirements.txt
   ```

5. **Jalankan `datagen.py` untuk Persiapan Dataset**  
   Skrip `datagen.py` digunakan untuk mempersiapkan dataset yang akan digunakan dalam pelatihan model. Pastikan file dataset yang relevan tersedia atau diatur sesuai kebutuhan. Jalankan perintah:  
   ```bash
   python datagen.py
   ```

6. **Jalankan `training.py` untuk Melatih Model**  
   Skrip `training.py` akan digunakan untuk melatih model berdasarkan dataset yang telah disiapkan. Jalankan perintah:  
   ```bash
   python training.py
   ```

7. **Jalankan `main.py` untuk Menjalankan Aplikasi**  
   Skrip `main.py` berfungsi sebagai program utama untuk menjalankan aplikasi Real-Time Mood Scanner. Jalankan perintah:  
   ```bash
   python main.py
   ```

---

## **Penggunaan Program**

Setelah instalasi selesai, berikut cara menggunakan **Real-Time Mood Scanner**:  

1. **Buka Terminal**  
   Arahkan terminal ke direktori proyek, jika belum berada di sana:  
   ```bash
   cd RealTimeMoodScanner_MUL
   ```

2. **Aktifkan Virtual Environment (Jika Digunakan)**  
   ```bash
   source env/bin/activate  # Untuk Linux/MacOS  
   env\Scripts\activate     # Untuk Windows  
   ```

3. **Jalankan Aplikasi**  
   Jalankan skrip utama untuk memulai aplikasi:  
   ```bash
   python main.py
   ```

4. **Antarmuka Aplikasi**  
   - Aplikasi akan menampilkan antarmuka kamera real-time.  
   - Pastikan kamera perangkat berfungsi.  

5. **Deteksi Mood**  
   - Arahkan wajah ke kamera, dan aplikasi akan memindai ekspresi wajah.  
   - Sistem akan menampilkan hasil prediksi mood seperti *senang*, *sedih*, atau *kaget*.  
