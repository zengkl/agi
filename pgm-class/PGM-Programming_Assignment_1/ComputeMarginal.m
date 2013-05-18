%ComputeMarginal Computes the marginal over a set of given variables
%   M = ComputeMarginal(V, F, E) computes the marginal over variables V
%   in the distribution induced by the set of factors F, given evidence E
%
%   M is a factor containing the marginal over variables V
%   V is a vector containing the variables in the marginal e.g. [1 2 3] for
%     X_1, X_2 and X_3.
%   F is a vector of factors (struct array) containing the factors 
%     defining the distribution
%   E is an N-by-2 matrix, each row being a variable/value pair. 
%     Variables are in the first column and values are in the second column.
%     If there is no evidence, pass in the empty matrix [] for E.


function M = ComputeMarginal(V, F, E)

% Check for empty factor list
if (numel(F) == 0)
      warning('Warning: empty factor list');
      M = struct('var', [], 'card', [], 'val', []);      
      return;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% YOUR CODE HERE:
% M should be a factor
% Remember to renormalize the entries of M!
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

M = ComputeJointDistribution( F );
M = ObserveEvidence(M, E);
irrelevantVars = setdiff(M.var, V);
if isempty(setdiff(M.var, irrelevantVars))
  M = struct('var', [], 'card', [], 'val', []);
else
  assignments = IndexToAssignment(1:length(M.val), M.card );
  M = SetValueOfAssignment(M, assignments, M.val/sum(M.val));    
  M = FactorMarginalization(M, irrelevantVars );
end
% for (i = 1:numel(F)),
%   F(i) = ObserveEvidence(F(i),E);
%   irrelevantVars = setdiff(F(i).var, V);

%   if isempty(setdiff(F(i).var, irrelevantVars))
%     F(i) = struct('var', [], 'card', [], 'val', []);
%   else
%     assignments = IndexToAssignment(1:length(F(i).val), F(i).card );
%     F(i) = SetValueOfAssignment(F(i), assignments, F(i).val/sum(F(i).val));    
%     F(i)

%     F(i) = FactorMarginalization(F(i), irrelevantVars );
%   end
% end

  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

M = StandardizeFactors(M);

end
