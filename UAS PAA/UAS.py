import random
import time
import matplotlib.pyplot as plt

# Fungsi untuk menghasilkan array dengan elemen acak dan seed tertentu
def generate_array(n, max_val, seed=42):
    random.seed(seed)
    return [random.randint(1, max_val) for _ in range(n)]

# Fungsi untuk memeriksa apakah elemen array unik
def is_unique(array):
    seen = set()
    for num in array:
        if num in seen:
            return False
        seen.add(num)
    return True

# Fungsi untuk mengukur waktu eksekusi
def measure_time(n, max_val, iterations=10):
    worst_case_time = 0
    average_case_time = 0

    # Mengukur worst case
    worst_case_array = generate_array(n, max_val, seed=42)
    worst_case_array.append(worst_case_array[0])  # Tambahkan duplikat
    start = time.perf_counter()
    is_unique(worst_case_array)
    worst_case_time = time.perf_counter() - start

    # Mengukur average case
    total_time = 0
    for i in range(iterations):
        avg_case_array = generate_array(n, max_val, seed=42 + i)
        start = time.perf_counter()
        is_unique(avg_case_array)
        total_time += time.perf_counter() - start
    average_case_time = total_time / iterations

    return worst_case_time, average_case_time

# Main program
def main():
    n_values = [100, 150, 200, 250, 300, 350, 400, 500]
    stambuk_last_3_digits = 49  # Ganti dengan 3 digit terakhir stambuk Anda
    max_value = 250 - stambuk_last_3_digits

    results = []
    for n in n_values:
        worst, avg = measure_time(n, max_value)
        results.append((n, worst, avg))

    # Simpan hasil perhitungan ke file
    with open("worst_avg.txt", "w") as f:
        for n, worst, avg in results:
            f.write(f"n = {n}, Worst Case = {worst:.6f}s, Average Case = {avg:.6f}s\n")

    # Plot hasil
    plt.figure(figsize=(10, 6))
    worst_cases = [r[1] for r in results]
    average_cases = [r[2] for r in results]

    plt.plot(n_values, worst_cases, label="Worst Case", marker="o")
    plt.plot(n_values, average_cases, label="Average Case", marker="s")

    plt.title("Time Complexity of Unique Element Check")
    plt.xlabel("Array Size (n)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid()

    # Simpan grafik sebagai file
    plt.savefig("time_complexity_graph.jpg")
    plt.show()

    print("Program selesai. Semua file telah disimpan.")

if _name_ == "_main_":
    main()