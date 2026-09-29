def sum_array(A):
    n = len(A)
    total = 0
    for i in range(n):
        total += A[i]
    return total


input_angka = input("Masukkan elemen: ")

A = [int(x) for x in input_angka.split()]

print("Array : ", A)
print("Jumlah (n) : ", len(A))
print("Total : ", sum(A))
