function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

n = 2;
minErr = 10000;

for C_i = 0.2:0.05:0.4
  for sigma_j = 0.05:0.03:0.15
    model = svmTrain( X, y, C_i, @(x1, x2) gaussianKernel( x1, x2, sigma_j ) );
    pred = svmPredict( model, Xval );
    err_ij = mean( double( pred ~= yval ) );
    if err_ij < minErr
      C = C_i;
      sigma = sigma_j
      minErr = err_ij
    end
  end
end

		       





% =========================================================================

end
