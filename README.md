# AI Learning Journey

Dokumentasi terstruktur dan repositori kode eksperimen mandiri mengenai komputasi sains, analisis data numerik, dan algoritma machine learning.

Disusun oleh: **Bagaskara Amukti Palapa**  
Program Studi: S1 Teknik Informatika, Universitas Bina Darma  
Tujuan: Membangun pemahaman komprehensif mulai dari dasar algoritma matematika hingga implementasi model prediksi secara mandiri.

---

## 1. Peta Kurikulum & Struktur Modul

Repositori ini diorganisasi secara bertahap berdasarkan tingkat kompleksitas komputasi:

### Bagian 1: Python Foundations (`01-python-foundations`)
Penguasaan sintaks inti, paradigma pemrograman terstruktur, dan penanganan data memori sebelum beralih ke komputasi numerik.
- `01_syntax_and_types.py`: Sistem tipe data primitif, casting eksplisit, presisi numerik, dan formatting string.
- `02_control_flow.py`: Percabangan logis, iterasi efisien, dan penanganan kondisi batas (*edge cases*).
- `03_data_structures.py`: Karakteristik kompleksitas waktu List, Tuple, Set, dan Dictionary.
- `04_functions_and_modules.py`: Dekomposisi modular, argumen dinamis (*args, **kwargs), closure, dan penanganan exception.

### Bagian 2: Scientific Computing & Data Wrangling (`02-scientific-computing`)
Fondasi manipulasi matriks dan pembersihan dataset tabular yang menjadi masukan model AI.
- `01_numpy_basics.py`: Operasi N-dimensional array (`ndarray`), broadcasting, dan slicing vektor.
- `02_linear_algebra_ops.py`: Operasi perkalian dot matrix, transposisi, invers, dan vektorisasi aljabar linier.
- `03_pandas_data_wrangling.py`: Struktur Series dan DataFrame, manipulasi indeks, filter kondisional, dan agregasi grup.
- `04_data_cleaning_pipeline.py`: Imputasi data hilang (*missing values*), deteksi outlier, normalisasi Min-Max, dan standarisasi Z-Score.

### Bagian 3: Classical Machine Learning (`03-classical-machine-learning`)
Implementasi algoritma inferensi data klasik menggunakan penalaran statistik dan pustaka Scikit-Learn.
- `01_linear_regression.py`: Pemodelan regresi linier, fungsi rugi Ordinary Least Squares (OLS), dan evaluasi MSE/R2.
- `02_logistic_regression.py`: Klasifikasi biner, fungsi sigmoid, log-loss, dan kurva batas keputusan (*decision boundary*).
- `03_decision_trees_knn.py`: Klasifikasi berbasis jarak (K-Nearest Neighbors) dan pemisahan entropi / Gini Impurity (Decision Tree).
- `04_model_evaluation_metrics.py`: Matriks konfusi (*confusion matrix*), metrik presisi, recall, F1-Score, dan validasi silang (*cross-validation*).

### Bagian 4: Neural Foundations & Deep Learning (`04-deep-learning-basics`)
Transisi dari machine learning klasik ke arsitektur jaringan saraf tiruan.
- `01_perceptron_from_scratch.py`: Model perseptron biner mandiri, pembaruan bobot berbasis learning rate, dan fungsi aktivasi step.
- `02_feedforward_neural_network.py`: Konsep lapisan tersembunyi (*hidden layers*), aktivasi non-linier (ReLU, Softmax), dan propagasi maju (*forward propagation*).

---

## 2. Persyaratan Lingkungan & Instalasi

Proyek ini menggunakan runtime Python 3 dengan dependensi ilmiah standar:

```bash
# 1. Masuk ke direktori repositori
cd ai-learning-journey

# 2. Buat virtual environment lokal
python3 -m venv venv

# 3. Aktifkan virtual environment
source venv/bin/activate

# 4. Pasang pustaka esensial
pip install numpy pandas scikit-learn matplotlib
```

---

## 3. Standar Penulisan Kode

Setiap skrip dalam repositori ini mematuhi prinsip berikut:
- **Standar Eksekusi Mandiri:** Setiap file `.py` dapat langsung dijalankan mandiri via terminal (`python3 nama_file.py`).
- **Pemisahan Logika:** Setiap konsep komputasi dipisahkan dalam fungsi terisolasi dengan dokumentasi teknis (*docstrings*).
- **Validasi Output:** Mengeluarkan log deterministik di konsol terminal untuk mengonfirmasi hasil kalkulasi.
