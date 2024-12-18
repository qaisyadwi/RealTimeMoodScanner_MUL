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
                                                              


## **Instruksi Instalasi**

### **Prasyarat**
- Python versi 3.8 atau lebih baru.
- Webcam (untuk deteksi real-time).

### **Langkah Instalasi**

1. **Kloning Repositori**
   ```bash
   git clone https://github.com/qaisyadwi/RealTimeMoodScanner_MUL.git
   ```

2. **Masuk ke Direktori Proyek**
   ```bash
   cd RealTimeMoodScanner_MUL
   ```

3. **Buat Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # Untuk Linux/MacOS
   env\Scripts\activate    # Untuk Windows
   ```

4. **Instal Dependensi**
   ```bash
   pip install -r requirements.txt
   ```

5. **Siapkan Dataset**
   - Tempatkan dataset dalam folder `data/`.
   - Jalankan script pra-pemrosesan jika diperlukan:
     ```bash
     python preprocess.py
     ```

6. **Konfigurasi File**
   - Sesuaikan `config.json` untuk parameter model dan direktori dataset.

---

## **Penggunaan Program**

