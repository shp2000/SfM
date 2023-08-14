from lse import least_squares_estimation
import numpy as np

def ransac_estimator(X1, X2, num_iterations=60000):
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None

    for i in range(num_iterations):
        # permuted_indices = np.random.permutation(np.arange(X1.shape[0]))
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]

        """ YOUR CODE HERE
        """
        e3 = [[0,-1, 0],
              [1, 0, 0],
              [0, 0, 0]]
        E = least_squares_estimation(X1[sample_indices], X2[sample_indices])
        
        inliers = sample_indices
        for i in range(0,len(test_indices)):
            dx2 = ((X2[test_indices[i]].T@E@X1[test_indices[i]])**2)/(np.linalg.norm(e3@E@X1[test_indices[i]]))**2
            dx1 = ((X1[test_indices[i]].T@E.T@X2[test_indices[i]])**2)/(np.linalg.norm(e3@E.T@X2[test_indices[i]]))**2
            if(dx1+ dx2<eps):
                inliers=np.append(inliers,test_indices[i])
        

        """ END YOUR CODE
        """
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_E = E
            best_inliers = inliers


    return best_E, best_inliers