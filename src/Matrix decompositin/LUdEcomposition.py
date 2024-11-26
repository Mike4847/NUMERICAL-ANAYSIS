# program that decomposes a matrix A into LU components.



def lu_decomposition(matrix_A :list[list]):
  # Note that the above algorithm works for square matrix
  # length of the matrix(entries)
  n = len(matrix_A)

  # construct the L and U matrices 
  L = [[0.0] * n for _ in range(n)]

  U = [[0.0] * n for _ in range(n)]

  for i in range(n):
    """ their are two flavours for the matrix decompositon, depending on the matrix were
      gonna set diagonal entries to 1
      i. u_ii = 1 (crouts method)
      ii. l_ii = 1 (doolite's method)
  Args:
      matrix_A (int, optional): _description_.
        Defaults to len(matrix_A)L=[[0] * n for i in range(n)]U=[[0] * n for i in range(n)]foriinrange(n.
  """
    U[i][i] = 1.0
    for k in range(i , n):
      L[i][k] = matrix_A[i][k] - sum(L[i][j] * U[j][k] for j in range(i))
    

    for k in range(i+1, n):
      U[k][i] = matrix_A[k][i] - sum(L[i][j] * U[j][k] for j in range(i))/U[i][i]
  

  return L,U

# utility for printing entries of a matrix
def Print_matrix(matrix:list[list]):
  n = len(matrix)

  for i in range(n):
    for j in range(n):
      print(f"{matrix[i][j]:.4f}", end=" ")
  
    print("\n")
  
# driver code
if __name__ == "__main__":
    
    # example code 3 x 3

  A = [
      [3,2,-3],
      [2,2,5],
      [1,1,-1]
    ]

  Upper, Lower =lu_decomposition(A)
  print("Upper triangular matrix after decomposition")

  Print_matrix(Upper)

  print("Lower triangular matrix after decomposition")

  Print_matrix(Lower)

