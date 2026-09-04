"""
Modul 01: Sintaks Inti dan Sistem Tipe Data
Repositori: AI Learning Journey
Penulis: Bagaskara Amukti Palapa

Tujuan:
Mempelajari perilaku tipe data primitif, casting eksplisit,
serta operasi aritmatika numerik yang menjadi dasar komputasi sains.
"""

def demonstrasi_tipe_primitif():
    """Menampilkan karakteristik dasar tipe data di Python."""
    print("=== 1. Tipe Data Primitif ===")
    
    nilai_integer = 42
    nilai_float = 3.1415926535
    nilai_string = "Model Machine Learning"
    nilai_boolean = True
    nilai_none = None

    data_samples = [
        ("Integer", nilai_integer),
        ("Float", nilai_float),
        ("String", nilai_string),
        ("Boolean", nilai_boolean),
        ("NoneType", nilai_none),
    ]

    for label, val in data_samples:
        print(f"[{label:10}] Nilai: {str(val):25} | Tipe: {type(val).__name__:10} | Memori ID: {id(val)}")
    print()


def demonstrasi_aritmatika_numerik():
    """Operasi numerik penting untuk kalkulasi vektor dan matriks."""
    print("=== 2. Operasi Aritmatika & Presisi Numerik ===")
    
    a = 17
    b = 4

    print(f"Nilai a = {a}, b = {b}")
    print(f"Penjumlahan (a + b)        : {a + b}")
    print(f"Pengurangan (a - b)        : {a - b}")
    print(f"Perkalian (a * b)          : {a * b}")
    print(f"Pembagian Floating (a / b) : {a / b} (Tipe: {type(a / b).__name__})")
    print(f"Pembagian Integer (a // b) : {a // b} (Floor division)")
    print(f"Modulus / Sisa Bagi (a % b): {a % b}")
    print(f"Eksponensial (a ** b)      : {a ** b} (Pemangkatan)")
    print()


def demonstrasi_casting_tipe():
    """Konversi tipe data eksplisit yang umum digunakan saat membaca dataset mentah."""
    print("=== 3. Type Casting Eksplisit ===")
    
    # Simulasi data mentah dari file teks atau input pengguna
    input_str_angka = "1024"
    input_str_float = "98.75"

    angka_int = int(input_str_angka)
    angka_float = float(input_str_float)
    angka_ke_str = str(angka_int * 2)

    print(f"String '{input_str_angka}' dikonversi ke int: {angka_int} (Tipe: {type(angka_int).__name__})")
    print(f"String '{input_str_float}' dikonversi ke float: {angka_float} (Tipe: {type(angka_float).__name__})")
    print(f"Hasil kalkulasi dikembalikan ke str: '{angka_ke_str}' (Tipe: {type(angka_ke_str).__name__})")
    
    # Perilaku konversi boolean
    print(f"bool(1) -> {bool(1)} | bool(0) -> {bool(0)}")
    print(f"bool('data') -> {bool('data')} | bool('') -> {bool('')}")
    print()


def main():
    print("==================================================")
    print("AI LEARNING JOURNEY: 01_SYNTAX_AND_TYPES")
    print("==================================================\n")
    demonstrasi_tipe_primitif()
    demonstrasi_aritmatika_numerik()
    demonstrasi_casting_tipe()
    print("Validasi eksekusi modul 01 selesai tanpa error.")


if __name__ == "__main__":
    main()
