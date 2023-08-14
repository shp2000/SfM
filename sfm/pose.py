import numpy as np

def pose_candidates_from_E(E):
  transform_candidates = []
  ##Note: each candidate in the above list should be a dictionary with keys "T", "R"
  """ YOUR CODE HERE
  """
  
  U, S , Vt = np.linalg.svd(E)
  print(U[:,-1])
  t1 = {"T":U[:,-1],
   "R" : U@[[0,1,0],
        [-1,0,0],
        [0,0,1]]@Vt
  }
  t2= {"T":U[:,-1],
   "R" : U@[[0,-1,0],
        [1,0,0],
        [0,0,1]]@Vt
  }

  t3 = {"T":(-U)[:,-1],
   "R" : U@[[0,1,0],
        [-1,0,0],
        [0,0,1]]@Vt
  }

  t4={"T":(-U)[:,-1],
   "R" : U@[[0,-1,0],
        [1,0,0],
        [0,0,1]]@Vt
  }

  transform_candidates = [t1,t2,t3,t4]


  """ END YOUR CODE
  """
  return transform_candidates