# AVIATION EXAMINATION & TRAINING PLATFORM

Platform ujian, latihan, dan evaluasi mandiri berbasis web statis modern untuk personil dan kru penerbangan. Platform ini memuat materi **BOLD FACE**, **LIMITATION**, dan **EMERGENCY PROCEDURES** yang bersumber langsung dari dokumen acuan manual resmi pesawat dan helikopter.

Website ini 100% statis (HTML5, CSS3 murni, dan Vanilla JavaScript), responsif di seluruh perangkat (Desktop, Laptop, Tablet, Android, dan iPhone), serta siap dipublikasikan secara gratis melalui **GitHub Pages**.

---

## 🛩️ Cakupan Armada & Bank Soal Resmi

| No | Jenis Pesawat / Helikopter | Dokumen Acuan Sumber | Total Soal | Status Verifikasi | Bagian Materi Utama |
|---|---|---|---|---|---|
| 1 | **MI-17V5** | `BOLD FACE MI-17V5 ISI.docx` | **53 Soal** | 100% Terverifikasi | Isian Beban, Kecepatan, Ceiling, CG, Tabel IAS, Bank, Mesin, Gearbox, APU, Slopes, Maneuver Khusus (External Load, Fastroping, Hoist, Fuel Reserve) |
| 2 | **BELL 412 EP** | `bold face bell 412 EP.pdf` | **147 Soal** | 100% Terverifikasi | Limitation lengkap 106 item (Crew, Weight, Cargo, CG, Speeds, Altitudes, Slopes, Maneuvering, Temps, Battery, Gen, Starter, N1, N2, ITT, Torque, Pressures, Rotor RPM, Hyd, AHRS), Indikator Instrumen, dan Emergency Procedures |
| 3 | **FENNEC AS550** | `BOLD FACE FENNEC AS550.docx` | **49 Soal** | 100% Terverifikasi | Weight Limits, VNE, Operating Altitude, Slopes, Running Landing, Rotor Speed, FLI, Torque Transmission, N2, N1, TOT, Oil Temp/Press, Electrical, Compartment Loads |
| 4 | **SIKORSKY S300C** | `BOLD FACE SIKORSKY S300C.docx` | **23 Soal** | 100% Terverifikasi | Gross Weight, CG, VNE, Engine Limits, Manifold Pressure, Wind Velocity, dan Prosedur Darurat Mesin & Transmisi |
| **TOTAL** | **4 Armada Penerbangan** | **Semua Dokumen Sumber Asli** | **272 Soal** | **100% Valid** | **Lengkap dengan Kunci Dokumen & Sitasi Halaman** |

---

## 🌟 Fitur Utama Platform

1. **Format Asli Dokumen Dipertahankan (Fill-in-the-Blank & Manual Form)**
   - Soal isian mempertahankan titik-titik dan garis pengisian dokumen manual asli (`Maximum gross weight: [_____] Lbs`).
   - Tidak mengubah soal manual teknis secara sembarangan menjadi pilihan ganda.
2. **Tiga Mode Pengerjaan Fleksibel**:
   - **Mode Ujian (Exam Mode)**: Tanpa bocoran jawaban selama tes, timer aktif dengan peringatan sisa waktu, navigasi nomor soal, penanda ragu-ragu (flag), dan evaluasi nilai otomatis setelah dikumpulkan.
   - **Mode Latihan (Practice Mode)**: Pengguna dapat memeriksa jawaban langsung per nomor (*Instant Check*) serta membuka kunci acuan dokumen resmi (*Reveal Answer*).
   - **Mode Lembar Manual (Printable Exam Mode)**: Tampilan formal lembar ujian cetak di atas kertas putih standar dengan tabel identitas peserta ujian (Nama, Pangkat/NRP, Jabatan, Tanggal, Nilai). Desain cetak didukung `@media print` otomatis tanpa menu navigasi dan tombol.
3. **Sistem Penilaian Cerdas & Toleran (Unit-Aware Grading)**:
   - Normalisasi huruf kapital, spasi berlebih, tanda baca, simbol derajat (`°`), dan koma/titik desimal.
   - Deteksi satuan ketat: Menolak salah satuan yang berpotensi fatal (contoh: membedakan `1000 ft` vs `1000 m`, `100 knots` vs `100 km/h`).
   - Mendukung variasi sinonim teknis yang setara (`acceptedAnswers`).
4. **Penyimpanan Lokal Otomatis (LocalStorage)**:
   - Jawaban disimpan secara real-time saat pengguna mengetik sehingga progres tidak hilang jika browser tidak sengaja di-refresh.
   - Tombol **Lanjutkan Latihan** tersedia di kartu pesawat pada halaman utama.
   - Riwayat ujian tersimpan lengkap dengan persentase skor, durasi pengerjaan, dan analisis per kategori.
5. **Katalog & Pencarian Bank Soal**:
   - Pencarian instan berdasarkan kata kunci soal, nama pesawat, atau kategori.
   - Ekspor Bank Soal ke format JSON.
   - Ekspor rincian hasil ujian peserta ke format spreadsheet CSV.
6. **Desain Modern & Aksesibel**:
   - Skema warna Navy Blue, Slate, White, Gold, dan Emerald Green khas lingkungan pendidikan penerbangan.
   - Dukungan tema Gelap (Dark Mode) dan Terang (Light Mode) dengan tombol toggle instan.
   - Tata letak responsif untuk Smartphone Android, iPhone, Tablet, Laptop, dan Komputer Desktop.

---

## 📂 Struktur Berkas Proyek

```
/
├── index.html                  # Halaman utama aplikasi (SPA)
├── test_suite.js               # Pengujian otomatis regresi (47 pengujian)
├── test_engine.js              # Pengujian simulasi siklus ujian dan penyimpanan
├── generate_all_data.py        # Skrip kompilasi bank soal dari dokumen sumber
├── .nojekyll                   # Mencegah GitHub Pages mengabaikan folder aset
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions workflow untuk rilis otomatis
├── assets/
│   ├── css/
│   │   └── style.css           # Desain sistem, tema gelap/terang, dan aturan cetak
│   └── js/
│       ├── app.js              # Koordinator tampilan antarmuka dan interaksi pengguna
│       ├── navigation.js       # Router navigasi berbasis URL Hash
│       ├── exam-engine.js      # Mesin pengatur sesi ujian, timer, dan status jawaban
│       ├── grading.js          # Mesin penilaian normalisasi teks dan deteksi satuan
│       ├── question-loader.js  # Pemuat data berkas JSON secara asinkron
│       └── storage.js          # Pengelola persistensi data LocalStorage browser
└── data/
    ├── aircraft-index.json     # Metadata indeks seluruh jenis pesawat
    ├── mi-17v5.json            # Bank soal helikopter MI-17V5 (53 soal)
    ├── bell-412-ep.json        # Bank soal helikopter BELL 412 EP (147 soal)
    ├── fennec-as550.json       # Bank soal helikopter FENNEC AS550 (49 soal)
    └── sikorsky-s300c.json     # Bank soal helikopter SIKORSKY S300C (23 soal)
```

---

## 💻 Panduan Menjalankan Secara Lokal

Website ini murni berbasis berkas statis dan dapat dijalankan langsung menggunakan peramban web modern apa pun. Namun, karena peramban membatasi permintaan `fetch()` lokal pada protokol `file://`, gunakan server lokal sederhana:

### Menggunakan Python (Direkomendasikan)
1. Buka terminal atau PowerShell di dalam direktori proyek:
   ```bash
   cd c:\Ballface
   ```
2. Jalankan server lokal:
   ```bash
   python -m http.server 8080
   ```
3. Buka peramban dan akses:
   [http://localhost:8080/](http://localhost:8080/)

### Menggunakan Node.js (Alternatif)
Jika memiliki `npx`:
```bash
npx serve .
```

---

## 🧪 Cara Menjalankan Pengujian Otomatis

Platform ini dilengkapi dengan rangkaian pengujian terotomatisasi (*Automated Test Suite*) untuk memverifikasi integritas berkas, struktur JSON, logika mesin penilaian, dan ketersediaan titik akhir:

```bash
node test_suite.js
```
Hasil yang diharapkan: **47 / 47 tests passed (0 failed)**.

Untuk menguji siklus lengkap mesin ujian dan penyimpanan LocalStorage:
```bash
node test_engine.js
```

---

## 🚀 Panduan Deployment ke GitHub Pages

Proyek ini telah dikonfigurasi untuk terpublikasi secara otomatis ke GitHub Pages menggunakan **GitHub Actions**.

### Langkah 1: Hubungkan ke Repository GitHub Anda
1. Buka terminal di folder proyek:
   ```bash
   git add .
   git commit -m "feat: inisialisasi platform ujian penerbangan lengkap dengan 4 armada"
   ```
2. Hubungkan repository lokal ke remote GitHub Anda:
   ```bash
   git remote add origin https://github.com/USERNAME/NAMA-REPO.git
   git branch -M main
   git push -u origin main
   ```

### Langkah 2: Mengaktifkan GitHub Pages di Repository
1. Masuk ke halaman repository Anda di GitHub.
2. Klik tab **Settings** (Pengaturan).
3. Di panel sebelah kiri, pilih menu **Pages**.
4. Di bagian **Build and deployment** → **Source**, pilih opsi:
   - **GitHub Actions**
5. Alur kerja `.github/workflows/deploy.yml` akan berjalan secara otomatis saat ada *push* ke branch `main`.

### Langkah 3: Memeriksa Status Rilis
1. Masuk ke tab **Actions** di repository GitHub Anda.
2. Periksa workflow **Deploy Aviation Exam Platform to GitHub Pages**.
3. Setelah tanda centang hijau muncul, buka tautan website Anda yang beralamat di:
   `https://USERNAME.github.io/NAMA-REPO/`

---

## ✏️ Cara Menambah atau Mengubah Bank Soal

Semua bank soal dipisahkan dari kode tampilan antarmuka dan disimpan di direktori `data/`.

Contoh struktur soal di dalam berkas JSON (misal `data/bell-412-ep.json`):
```json
{
  "id": "B412-LIM-002",
  "aircraft": "BELL 412 EP",
  "section": "LIMITATION",
  "category": "GROSS WEIGHT",
  "questionType": "fill-blank",
  "question": "Maximum gross weight for take off and landing",
  "answer": "11.900 Lbs",
  "acceptedAnswers": ["11.900", "11900", "11,900", "11.900 Lbs", "11900 lbs"],
  "unit": "Lbs",
  "sourceDocument": "bold face bell 412 EP.pdf",
  "sourcePage": 16,
  "points": 1,
  "verified": true
}
```

### Prosedur Penambahan:
1. Buka berkas JSON pesawat terkait di folder `data/` (atau jalankan skrip `generate_all_data.py`).
2. Masukkan item soal baru dengan ID unik.
3. Tetapkan `answer` sesuai dokumen resmi, serta `acceptedAnswers` untuk variasi format pengetikan siswa yang valid.
4. Simpan berkas, lakukan commit, dan push ke GitHub:
   ```bash
   git add data/
   git commit -m "update: penambahan materi bank soal"
   git push origin main
   ```

---

## 🔒 Kebijakan Penyimpanan & Privasi

- **Penyimpanan Lokal Browser**: Data jawaban, nilai, dan riwayat disimpan secara privat di dalam LocalStorage peramban pengguna. Tidak ada data pribadi atau nilai yang dikirim ke server luar.
- **Transparansi Sistem Statis**: Karena dihosting di GitHub Pages statis tanpa backend, platform ini dirancang untuk latihan mandiri, pendalaman pengetahuan, dan persiapan ujian internal. Jika kelak dibutuhkan pengawasan ketat anti-kecurangan untuk ujian seleksi resmi, disarankan menambahkan sistem autentikasi dan server backend terpisah.

---

*Aviation Examination & Training Platform — Mengutamakan Ketepatan Materi Teknis, Kecepatan, dan Kemudahan Evaluasi Personil Penerbangan.*
