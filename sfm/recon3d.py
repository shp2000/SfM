import numpy as np

def reconstruct3D(transform_candidates, calibrated_1, calibrated_2):
  """This functions selects (T,R) among the 4 candidates transform_candidates
  such that all triangulated points are in front of both cameras.
  """

  best_num_front = -1
  best_candidate = None
  best_lambdas = None
  for candidate in transform_candidates:
    R = candidate['R']
    T = candidate['T']
    
    lambdas = np.zeros((2, calibrated_1.shape[0]))
    """ YOUR CODE HERE
    """
    A=[]
    lambd=[]
    B=[]
    
    for i in range(0,calibrated_1.shape[0]):
      B=-(R@np.array([[calibrated_1[i][0]], [calibrated_1[i][1]],[calibrated_1[i][2]]])).reshape(3,1)
      
      A=np.array([[calibrated_2[i][0], B[0][0]],
         [calibrated_2[i][1], B[1][0]],
        [calibrated_2[i][2], B[2][0]] ])
      
      lambd = np.dot(np.linalg.pinv(A),(T.reshape(3,1)))
      
      lambdas[0][i]=lambd[0]
      lambdas[1][i]=lambd[1]
    
   
    
  #  """
    """ END YOUR CODE
    """
    num_front = np.sum(np.logical_and(lambdas[0]>0, lambdas[1]>0))

    if num_front > best_num_front:
      best_num_front = num_front
      best_candidate = candidate
      best_lambdas = lambdas
      print("best", num_front, best_lambdas[0].shape)
    else:
      print("not best", num_front)


  P1 = best_lambdas[1].reshape(-1, 1) * calibrated_1
  P2 = best_lambdas[0].reshape(-1, 1) * calibrated_2
  T = best_candidate['T']
  R = best_candidate['R']
  return P1, P2, T, R