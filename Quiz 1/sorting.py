
# Merge Sort adalah algoritma pengurutan yang selalu membagi array menjadi dua bagian hingga ukuran terkecil, lalu menggabungkannya kembali dalam keadaan terurut. Algoritma ini memiliki kompleksitas waktu 𝑂 ( 𝑛 log ⁡ 𝑛 )dalam semua kondisi, baik untuk best case, worst case, maupun average case. Hal ini karena proses pembagian dan penggabungan array selalu dilakukan dengan cara yang sama, tanpa tergantung pada bagaimana data diurutkan. Keunggulan Merge Sort adalah konsistensinya, tetapi membutuhkan ruang tambahan untuk menyimpan hasil pembagian.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

# Quick Sort bekerja dengan memilih elemen pivot, yaitu elemen patokan yang digunakan untuk membagi array menjadi dua bagian: elemen yang lebih kecil dari pivot dan elemen yang lebih besar. Pivot tidak selalu berada di tengah posisi array, tetapi nilai pivot akan menjadi acuan pembagian data. Best case terjadi jika pivot membagi array menjadi dua kelompok yang hampir sama besar, sehingga kompleksitasnya adalah 𝑂 ( 𝑛 log ⁡ 𝑛 ). Namun, pada worst case, seperti ketika array sudah terurut atau hampir terurut, pembagian menjadi tidak seimbang. Hal ini membuat algoritma menjadi tidak efisien dengan kompleksitas 𝑂 ( 𝑛^2 ). Pada average case, Quick Sort biasanya tetap 𝑂 ( 𝑛 log ⁡ 𝑛 ), terutama jika pemilihan pivot dilakukan dengan strategi yang baik, seperti memilih median atau elemen secara acak. Keunggulan utama Quick Sort adalah lebih hemat ruang dibanding Merge Sort karena tidak membutuhkan array tambahan, tetapi algoritma ini tidak stabil, yang berarti elemen dengan nilai yang sama dapat berubah urutannya setelah pengurutan.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    patokan = arr[len(arr) // 2]
    elemenKiri = [x for x in arr if x < patokan]
    elemenTengah = [x for x in arr if x == patokan]
    elemenKanan = [x for x in arr if x > patokan]
    return quick_sort(elemenKiri) + elemenTengah + quick_sort(elemenKanan)

x = [1, 5, 6, 4, 3, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Menggunakan Merge Sort
sorted_merge = merge_sort(x)
print("Sorted with Merge Sort:", sorted_merge)

# Menggunakan Quick Sort
sorted_quick = quick_sort(x)
print("Sorted with Quick Sort:", sorted_quick)


# Secara umum, Merge Sort lebih cocok untuk situasi yang membutuhkan stabilitas dan performa konsisten, sementara Quick Sort lebih cepat pada kebanyakan kasus tetapi bisa lambat jika data kurang mendukung pemilihan pivot.
