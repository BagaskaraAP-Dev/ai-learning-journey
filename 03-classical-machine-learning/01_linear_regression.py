"""
Modul: 01 - Classical Machine Learning: Linear Regression
Penulis: Bagaskara Amukti Palapa
Tanggal: 15 September 2026
Deskripsi:
Implementasi Regresi Linier sederhana untuk memprediksi nilai ujian
berdasarkan jam belajar. Membandingkan perhitungan rumus manual Ordinary Least Squares (OLS)
dengan pustaka Scikit-Learn, disertai metrik evaluasi dan visualisasi.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def main():
    print("==================================================================")
    print("BELAJAR MACHINE LEARNING: REGRESI LINIER (BAGASKARA AMUKTI PALAPA)")
    print("==================================================================\n")

    # -------------------------------------------------------------
    # 1. MENYIAPKAN DATASET
    # -------------------------------------------------------------
    # X = Fitur (Jam Belajar per hari) -> Wajib 2 Dimensi: (jumlah_sampel, jumlah_fitur)
    # y = Target (Nilai Ujian)         -> 1 Dimensi: (jumlah_sampel,)
    X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
    y = np.array([35, 45, 50, 65, 68, 80, 85, 95])

    print("=== 1. DATASET ===")
    for jam, nilai in zip(X.flatten(), y):
        print(f"- Belajar: {jam} Jam -> Nilai Ujian: {nilai}")
    print(f"\nBentuk X (Shape): {X.shape} (8 baris sampel, 1 fitur)")
    print(f"Bentuk y (Shape): {y.shape} (8 target nilai)\n")

    # -------------------------------------------------------------
    # 2. LOGIKA MATEMATIKA MANUAL (ORDINARY LEAST SQUARES / OLS)
    # -------------------------------------------------------------
    # Rumus Garis Linier: y = m*X + c
    # m (Slope/Kemiringan) = Cov(X, y) / Var(X)
    # c (Intercept/Titik Potong) = mean(y) - m * mean(X)
    x_flat = X.flatten()
    x_mean = np.mean(x_flat)
    y_mean = np.mean(y)

    m_manual = np.sum((x_flat - x_mean) * (y - y_mean)) / np.sum((x_flat - x_mean) ** 2)
    c_manual = y_mean - (m_manual * x_mean)

    print("=== 2. PERHITUNGAN MANUAL (RUMUS OLS) ===")
    print(f"Kemiringan Garis (m / Slope)      : {m_manual:.4f}")
    print(f"Titik Potong Sumbu (c / Intercept): {c_manual:.4f}")
    print(f"Persamaan Garis                   : y = {m_manual:.4f} * X + {c_manual:.4f}\n")

    # -------------------------------------------------------------
    # 3. IMPLEMENTASI DENGAN SCIKIT-LEARN
    # -------------------------------------------------------------
    print("=== 3. TRAINING MODEL DENGAN SCIKIT-LEARN ===")
    model = LinearRegression()

    # Melatih model (mencari nilai weight & bias terbaik)
    model.fit(X, y)

    slope_sklearn = model.coef_[0]
    intercept_sklearn = model.intercept_

    print(f"Slope (model.coef_)          : {slope_sklearn:.4f}")
    print(f"Intercept (model.intercept_) : {intercept_sklearn:.4f}")
    print("-> Hasil Scikit-Learn sama persis dengan rumus manual kita!\n")

    # -------------------------------------------------------------
    # 4. PREDIKSI DATA BARU
    # -------------------------------------------------------------
    print("=== 4. PREDIKSI (INFERENCE) ===")
    # Melakukan prediksi untuk data latihan
    y_pred = model.predict(X)

    # Contoh memprediksi jam belajar baru yang belum pernah dilihat model:
    jam_baru = np.array([[3.5], [9], [10]])
    prediksi_baru = model.predict(jam_baru)

    for jam, hasil in zip(jam_baru.flatten(), prediksi_baru):
        print(f"Prediksi nilai jika belajar {jam:4.1f} jam : {hasil:.2f}")
    print()

    # -------------------------------------------------------------
    # 5. METRIK EVALUASI MODEL
    # -------------------------------------------------------------
    # MSE (Mean Squared Error): Rata-rata kuadrat selisih antara nilai asli dan prediksi
    # R2 Score: Seberapa baik variabel X menjelaskan variasi variabel y (skala 0.0 - 1.0)
    mse = mean_squared_error(y, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y, y_pred)

    print("=== 5. EVALUASI MODEL ===")
    print(f"Mean Squared Error (MSE) : {mse:.4f}")
    print(f"Root MSE (RMSE)          : {rmse:.4f} (rata-rata meleset +- {rmse:.2f} poin)")
    print(f"R-squared Score (R2)     : {r2:.4f} ({r2 * 100:.2f}% akurasi kecocokan garis)\n")

    # -------------------------------------------------------------
    # 6. VISUALISASI GRAFIK
    # -------------------------------------------------------------
    print("=== 6. MENAMPILKAN VISUALISASI GRAFIK ===")
    print("Jendela grafik sedang dibuka... (tutup jendela grafik jika ingin melanjutkan di terminal)")

    plt.figure(figsize=(8, 5))
    # Titik data asli (Scatter Plot)
    plt.scatter(X, y, color="blue", label="Data Aktual (Siswa)")
    # Garis regresi hasil prediksi
    plt.plot(X, y_pred, color="red", linewidth=2, label=f"Garis Regresi (y = {slope_sklearn:.2f}x + {intercept_sklearn:.2f})")

    plt.title("Regresi Linier: Jam Belajar vs Nilai Ujian", fontsize=14)
    plt.xlabel("Jam Belajar per Hari (X)", fontsize=12)
    plt.ylabel("Nilai Ujian (y)", fontsize=12)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()

    print("Program selesai dijalankan dengan sukses!")


if __name__ == "__main__":
    main()
