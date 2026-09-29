# 1. Array 1 Dimensi (Kompleksitas : 0(n))
def sum_array(A):
    n = len(A)
    total = 0

    for i in range(n):
        total += A[i]
    return total


# Input
A = [10, 20, 30, 40, 50]

# Output
hasil = sum_array(A)

print("Array : ", A)
print("Jumlah (n) : ", len(A))
print("Jumlah : ", hasil)
