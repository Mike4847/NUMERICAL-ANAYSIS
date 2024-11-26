# program that decomposes a matrix A into LU components.



def lu_decoposition(matrix_A :list[list]):
  # Note that the above algorithm works for square matrix
  # length of the matrix(entries)
  n = len(matrix_A)

  # construct the L and U matrices 
  L = [[0] * n for _ in range(n)]

  U = [[0] * n for _ in range(n)]

  for i in range(n):
    """ their are two flavours for the matrix decompositon, depending on the matrix were
      gonna set diagonal entries to 1
      i. u_ii = 1 (crouts method)
      ii. l_ii = 1 (doolitels method)
  Args:
      matrix_A (int, optional): _description_.
        Defaults to len(matrix_A)L=[[0] * n for i in range(n)]U=[[0] * n for i in range(n)]foriinrange(n.
  """
    U[i][i] = 1
    for k in range(i , n):
      L[i][k] = matrix_A[i][k] - sum(L[i][j] * U[j][k] for j in range(i))
    

    for k in range(i+1, n):
      U[k][i] = matrix_A[k][i] - sum(L[j][k] * U[k][j] for j in range(i))/U[i][i]
  

  return L, U
  
  