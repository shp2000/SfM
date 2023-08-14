import numpy as np

def least_squares_estimation(X1, X2):
  """ YOUR CODE HERE
  """
  
  E_int=np.zeros((3,3))
  
  l=len(X1)
  A=np.zeros((l,9))
  for i in range(0,l):
    A[i][0] =X1[i][0]*X2[i][0]
    A[i][1] =X1[i][0]*X2[i][1]
    A[i][2] =X1[i][0]*X2[i][2]
    A[i][3] =X1[i][1]*X2[i][0]
    A[i][4] =X1[i][1]*X2[i][1]
    A[i][5] =X1[i][1]*X2[i][2]
    A[i][6] =X1[i][2]*X2[i][0]
    A[i][7] =X1[i][2]*X2[i][1]
    A[i][8] =X1[i][2]*X2[i][2]
  #print(A)
  U, S , Vt = np.linalg.svd(A)
  V=np.transpose(Vt)
  # print(V)
  v9=V[:, -1]
  #print(v9)
  p=0
  """for i in range(0,3):
    for j in range(0,3):
      E_int[i][j]=v9[p]
      p=p+1"""
  E_int=Vt[-1,:].reshape(3, 3)
  E_int=np.transpose(E_int)
  
  U, S , Vt = np.linalg.svd(E_int)
  #print(S)
  #si = [[(S[0]+S[1])/2, 0,0],
        #[0,(S[0]+S[1])/2,0],
        #[0,0,0]]
  si = [[1, 0,0],
        [0,1,0],
        [0,0,0]]
  E = U@si@Vt
 
  """ END YOUR CODE
  """
  return E
