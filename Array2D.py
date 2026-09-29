def print_matrix(M):
    n = len(M)
    elemen = 0

    for i in range(n):
        for j in range(n):
            print(f"{M[i][j]} ", end="")
            elemen += 1
        print()
    return elemen


M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Isi Matrix:")
total_elemen = print_matrix(M)
print("Jumlah seluruh elemen matriks:", total_elemen)
