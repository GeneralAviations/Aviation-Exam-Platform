# ✈️ AVIATION EXAMINATION & EVALUATION SUITE
### Standardized Flight Crew Bold Face, Limitations & Emergency Procedures Platform

[![GitHub Pages](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-0284c7?style=for-the-badge&logo=github&logoColor=white)](https://generalaviations.github.io/Aviation-Exam-Platform/)
[![Build Status](https://img.shields.io/badge/Build-Passing-10b981?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/generalaviations/Aviation-Exam-Platform/actions)
[![Test Suite](https://img.shields.io/badge/Tests-65%20Passed-10b981?style=for-the-badge&logo=node.js&logoColor=white)](test_suite.js)
[![Standard](https://img.shields.io/badge/Aviation%20Standard-AFM%20%26%20Bold%20Face-f59e0b?style=for-the-badge)](data/aircraft-index.json)
[![License](https://img.shields.io/badge/License-MIT-64748b?style=for-the-badge)](LICENSE)

Platform evaluasi, ujian interaktif, dan simulasi mandiri berbasis web statis modern untuk personil dan kru penerbangan militer maupun sipil. Seluruh materi **BOLD FACE**, **LIMITATIONS**, dan **EMERGENCY PROCEDURES** diselaraskan **100% persis** dengan dokumen asli *Aircraft Flight Manual* (AFM), *Pilot Operating Handbook* (POH), dan *Flight Checklist* resmi.

> 🌐 **Akses Aplikasi Langsung**: [https://generalaviations.github.io/Aviation-Exam-Platform/](https://generalaviations.github.io/Aviation-Exam-Platform/)

---

## 🛩️ Katalog 8 Armada Pesawat & Bank Soal Resmi

Platform mencakup 8 jenis alutsista pesawat terbang sayap tetap (*fixed wing*), helikopter serbu/angkut (*rotary wing*), dan drone intai taktis (*UAV*):

| No | Armada Pesawat / Helikopter | Kategori | Dokumen Acuan Resmi | Total Soal | Karakteristik Materi |
|:---:|:---|:---:|:---|:---:|:---|
| 1 | **AH-64E APACHE** | ⚔️ Tempur | `AH-64E Rv. 3.0 Emergency Procedures Practice Test.pdf` | **76 Soal** | Batasan Mesin T701D, Airspeed, Rotor NR, TGT, Dual/Single Engine Failure, Prosedur Darurat Kebakaran, Transmisi, dan 15 Warning/Caution/Advisories |
| 2 | **ANKA MALE UAV** | 🛸 UAV | `ANKAID-T0544-AFM-2` | **132 Soal** | Limitations & Emergency Procedures lengkap: Engine, Fuel, Electrical, Satcom Link Loss, Payload, Flight Controls |
| 3 | **BELL 412 EP** | 🚁 Helikopter | `bold face bell 412 EP.pdf` | **122 Soal** | 106 Batasan Operasional lengkap, 5 Dial Indikator Mesin/Rotor, dan 11 Prosedur Darurat Lengkap dengan sub-langkah tindakan |
| 4 | **BO-105** | 🚁 Helikopter | `BOLD FACE BO-105.pdf` | **79 Soal** | Rigid Rotor limits, Engine Limits, Autorotation, Slopes, Mast Moment, Single Engine In-Flight Procedures |
| 5 | **CASA 212-200** | ✈️ Sayap Tetap | `BOLD FACE CASA 212-200 AVIOCAR.pdf` | **9 Soal Multi-Item** | 9 Soal Utama berformat tabel multi-parameter resmi (a s/d k): TGT, Torque, Oil, Engine Starting, Emergency In-Flight Fire |
| 6 | **FENNEC AS550** | 🚁 Helikopter | `BOLD FACE FENNEC AS550.docx` | **15 Soal Multi-Item** | 15 Soal Utama berformat tabel multi-parameter resmi (a s/d n): FLI limits, Arriel Turbomeca, NR, Slopes, Running Landing |
| 7 | **MI-17V5** | 🚁 Helikopter | `BOLD FACE MI-17V5 ISI.docx` | **25 Soal** | Penomoran resmi 1-25 halaman 1-4: Engine Ratings, VNE, Speeds, Bank, Slopes, Ceiling, External Load, Hoist, Fuel Reserve |
| 8 | **SIKORSKY S-300C** | 🚁 Helikopter | `BOLD FACE SIKORSKY S300C.docx` | **23 Soal** | Gross Weight, CG, Airspeed Limits, Lycoming HIO-360 Piston, Manifold Pressure, Prosedur Darurat Mesin & Ekor |
| | **TOTAL KESELURUHAN** | **8 SUITE ARMADA** | **DOKUMEN MANUAL RESMI 1:1** | **481 SOAL** | **113 Soal Multi-Parameter Resmi** |

---

## 🌟 Fitur Unggulan Platform

### 1. 📋 Mode Lembar Kertas Dokumen Asli (*Bold Face Paper Sheet Mode*)
- **Simulasi Kertas Ujian Asli**: Menampilkan tata letak lembar ujian putih formal militer lengkap dengan garis isian titik-titik dan tabel identitas penerbang (Nama, Pangkat/NRP, Jabatan, Kualifikasi, Tanggal, dan Nilai).
- **Mode Cetak Otomatis (`@media print`)**: Siap dicetak langsung ke printer atau diekspor ke PDF dengan tata letak bersih tanpa menu tombol, navigasi, atau elemen website.
- **Interaktif Real-time**: Peserta dapat mengisi lembar kerja langsung di layar browser dengan validasi warna cerdas (Hijau = Tepat, Merah = Koreksi, Biru = Kunci Terbuka).
- **Penomoran Dokumen Otentik**: Penomoran soal (1, 2, ... 8, ... 22) mempertahankan nomor resmi dari dokumen acuan asli di setiap seksi.

### 2. 🎯 Mode CBT Ujian Terstandarisasi (*Interactive Exam Mode*)
- **Fokus 1-per-1**: Pertanyaan disajikan dalam kartu kuis elegan dengan indikator satuan dan kartu sub-parameter terstruktur (`a.`, `b.`, `c.`).
- **Timer Adaptif & Peringatan Otomatis**: Dilengkapi countdown timer dan notifikasi darurat saat waktu tersisa 5 menit.
- **Navigator Grid Soal**: Grid navigasi cepat ke seluruh nomor soal dengan indikator status (Sudah Dijawab, Belum Dijawab, dan Ditandai Ragu-ragu).
- **Penyimpanan Draft Instan (Anti-Hilang)**: Seluruh jawaban disimpan otomatis ke browser `LocalStorage` secara real-time. Jika browser ditutup atau baterai habis, sesi ujian dapat dilanjutkan tanpa kehilangan data.

### 3. 🔍 Mode Latihan Mandiri (*Practice Mode*)
- **Instant Feedback**: Memeriksa kebenaran jawaban langsung per parameter saat berlatih.
- **Buka Kunci Dokumen (*Reveal Key*)**: Menampilkan kunci acuan dan nomor halaman dokumen asli untuk sarana belajar cepat.

### 4. 🧠 Mesin Penilaian Cerdas (*Aviation Unit-Aware Grading Engine*)
- **Normalisasi Teks**: Menghilangkan spasi ganda, huruf besar/kecil, dan tanda baca minor.
- **Ekivalensi Rentang Nilai**: Memahami kesetaraan tanda hubung `-` dengan kata `sampai`, `to`, `s/d`, maupun `hingga` (contoh: `980 sampai 2320` setara dengan `980-2320`).
- **Ekivalensi Konjungsi**: Memahami kesetaraan simbol `&` dengan kata `dan` atau `and`.
- **Deteksi Kesalahan Satuan Kritis**: Menolak ketidaksesuaian satuan yang berpotensi fatal (contoh: membedakan `1000 ft` vs `1000 m`, `100 kts` vs `100 km/h`).

### 5. 📊 Dasbor Analisis Hasil & Bank Soal Explorer
- **Analisis per Kategori**: Rekapitulasi perolehan poin per sistem pesawat (Airspeed, Torque, Engine, Hydraulic, Emergency).
- **Pencarian Cepat Bank Soal**: Menelusuri seluruh 481 bank soal dengan filter armada dan pencarian kata kunci instan.
- **Ekspor Riwayat**: Kemampuan ekspor hasil evaluasi ke spreadsheet CSV dan JSON.

---

## 🎨 Desain Sistem & Aksesibilitas
- **Modern Aerospace UI**: Menggunakan perpaduan palet warna Deep Navy (`#070e18`), Aeronautic Cyan (`#0284c7`), White (`#f8fafc`), dan High-Visibility Alerts.
- **Typography Premium**: Font Google `Outfit` (judul aerospace mewah), `Inter` (antarmuka presisi), dan `JetBrains Mono` (telemetri & angka avionik).
- **Dukungan Tema Gelap & Terang**: Toggle instan Light / Dark Mode yang nyaman dioperasikan baik siang maupun malam.
- **100% Responsif**: Dioptimalkan sempurna untuk layar Smartphone Android, iPhone, iPad/Tablet, Laptop, dan Monitor Desktop tanpa ada teks tertimpa atau terpotong.

---

## 📂 Struktur Berkas Proyek

```
Aviation-Exam-Platform/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions: Otomasi tes dan rilis ke GitHub Pages
├── assets/
│   ├── css/
│   │   └── style.css           # Desain sistem, tema gelap/terang, dan aturan print
│   └── js/
│       ├── app.js              # Koordinator utama antarmuka & rendering data
│       ├── exam-engine.js      # Mesin ujian, timer, navigasi, dan state jawaban
│       ├── grading.js          # Mesin penilaian normalisasi teks dan toleransi satuan
│       ├── navigation.js       # Router SPA hash-based deep linking
│       ├── question-loader.js  # Pemuat data berkas JSON asinkron
│       └── storage.js          # Pengelola persistensi LocalStorage browser
├── data/
│   ├── aircraft-index.json     # Metadata master seluruh 8 armada pesawat
│   ├── ah-64e.json             # Bank soal AH-64E Apache (76 soal)
│   ├── anka-male-uav.json      # Bank soal ANKA MALE UAV (132 soal)
│   ├── bell-412-ep.json        # Bank soal BELL 412 EP (122 soal)
│   ├── bo-105.json             # Bank soal BO-105 (79 soal)
│   ├── casa-212-200.json       # Bank soal CASA 212-200 (9 soal multi-item)
│   ├── fennec-as550.json       # Bank soal FENNEC AS550 (15 soal multi-item)
│   ├── mi-17v5.json            # Bank soal MI-17V5 (25 soal resmi)
│   └── sikorsky-s300c.json     # Bank soal SIKORSKY S-300C (23 soal)
├── scripts/                    # Skrip pengembang & kompilasi dataset
│   ├── build_all_data_perfect.py # Kompiler dataset master seluruh armada
│   ├── build_ah64e.py          # Generator builder AH-64E
│   ├── build_ballface_datasets.py # Generator builder MI-17 & Bell 412
│   ├── build_full_suite.py     # Generator builder CASA 212 & Fennec AS550
│   └── generate_anka_data.py   # Generator builder ANKA MALE UAV
├── generate_all_data.py        # Titik masuk eksekusi kompilasi data master
├── index.html                  # Single Page Application (SPA) entry point
├── package.json                # Konfigurasi npm scripts & dependensi pengujian
├── test_suite.js               # Pengujian otomatis regresi (65 pengujian)
├── test_engine.js              # Pengujian simulasi siklus ujian & penyimpanan
├── test_layout_inspect.js      # Pengujian verifikasi visual layout & anti-overlap
├── .gitignore                  # Berkas pengecualian Git
├── .nojekyll                   # Mencegah Jekyll mengabaikan folder statis
├── LICENSE                     # Lisensi open-source MIT
└── README.md                   # Dokumentasi resmi repositori GitHub
```

---

## 🚀 Panduan Menjalankan Secara Lokal

Website ini 100% murni berkas statis (tanpa server database luar) sehingga sangat cepat dan hemat sumber daya.

### 1. Menjalankan Server Lokal (Python atau Node.js)
Gunakan server lokal untuk menghindari restriksi CORS browser saat membaca berkas JSON:

**Menggunakan Python:**
```bash
python -m http.server 8080
```
Buka peramban dan akses: [http://localhost:8080/](http://localhost:8080/)

**Menggunakan Node.js:**
```bash
npm start
```

### 2. Menjalankan Rangkaian Pengujian Otomatis (*Automated Test Suite*)
Seluruh integritas berkas, grading engine, dan layout visual dapat diuji dengan perintah:
```bash
npm test
```
Hasil pengujian:
```text
✓ PASS: 65 / 65 test suite criteria passed (0 failed)
✓ PASS: Exam Engine lifecycle & LocalStorage simulation passed
✓ PASS: Layout, responsive dots, and anti-overlap verification passed
```

### 3. Mengompilasi Ulang Data Bank Soal
Jika ingin mengompilasi ulang seluruh dataset pesawat dari skrip sumber:
```bash
python generate_all_data.py
```

---

## 🛠️ Otomasi Deployment ke GitHub Pages

Repositori ini telah dikonfigurasi dengan **GitHub Actions** (`.github/workflows/deploy.yml`):
1. Setiap kali kode di-push ke branch `main`, GitHub Actions akan menjalankan **Platform Test Suite** secara otomatis.
2. Jika seluruh pengujian lulus (*green check*), website akan langsung diperbarui di GitHub Pages:
   👉 **[https://generalaviations.github.io/Aviation-Exam-Platform/](https://generalaviations.github.io/Aviation-Exam-Platform/)**

---

## 📜 Lisensi & Atribusi
Proyek ini dirilis di bawah lisensi terbuka [MIT License](LICENSE). Seluruh dokumen acuan dan batasan penerbangan bersumber dari dokumentasi resmi pabrikan pesawat dan manual penerbangan militer terkait.
