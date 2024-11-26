import random

# Seed untuk hasil random yang konsisten
random.seed(40)

# Generate bilangan random integer 0-100 sebanyak 50 bilangan
data = [random.randint(0, 100) for _ in range(50)]

# Save data ke file untuk pengecekan
with open("data.txt", "w") as f:
    f.write("Data sebelum sorting:\n")
    f.write(", ".join(map(str, data)) + "\n\n")

    # naive.py
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    import random
    random.seed(40)
    data = [random.randint(0, 100) for _ in range(50)]

    # Sorting menggunakan Bubble Sort
    sorted_data = bubble_sort(data.copy())

    # Simpan hasil ke file
    with open("sorted_naive.txt", "w") as f:
        f.write("Hasil sorting dengan Bubble Sort:\n")
        f.write(", ".join(map(str, sorted_data)))

# conquer.py
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Rekursi pada masing-masing bagian
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge bagian kiri dan kanan
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy elemen yang tersisa
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

if __name__ == "__main__":
    import random
    random.seed(40)
    data = [random.randint(0, 100) for _ in range(50)]

    # Sorting menggunakan Merge Sort
    sorted_data = merge_sort(data.copy())

    # Simpan hasil ke file
    with open("sorted_conquer.txt", "w") as f:
        f.write("Hasil sorting dengan Merge Sort:\n")
        f.write(", ".join(map(str, sorted_data)))

