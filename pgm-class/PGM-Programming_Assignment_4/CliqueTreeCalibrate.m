%CLIQUETREECALIBRATE Performs sum-product or max-product algorithm for 
%clique tree calibration.

%   P = CLIQUETREECALIBRATE(P, isMax) calibrates a given clique tree, P 
%   according to the value of isMax flag. If isMax is 1, it uses max-sum
%   message passing, otherwise uses sum-product. This function 
%   returns the clique tree where the .val for each clique in .cliqueList
%   is set to the final calibrated potentials.
%
% Copyright (C) Daphne Koller, Stanford University, 2012

function P = CliqueTreeCalibrate(P, isMax)


% Number of cliques in the tree.
N = length(P.cliqueList);

% Setting up the messages that will be passed.
% MESSAGES(i,j) represents the message going from clique i to clique j. 
MESSAGES = repmat(struct('var', [], 'card', [], 'val', []), N, N);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% We have split the coding part for this function in two chunks with
% specific comments. This will make implementation much easier.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% YOUR CODE HERE
% While there are ready cliques to pass messages between, keep passing
% messages. Use GetNextCliques to find cliques to pass messages between.
% Once you have clique i that is ready to send message to clique
% j, compute the message and put it in MESSAGES(i,j).
% Remember that you only need an upward pass and a downward pass.
%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[i,j] = GetNextCliques(P, MESSAGES);
while (i  && j )
    delta = P.cliqueList(i);
    if isMax
       delta.val = log(delta.val);
    end
    for (k = setdiff(find(P.edges(i,:) == 1), [j]))
      if isMax
	 delta = FactorSum(delta, MESSAGES(k,i));
      else
	delta = FactorProduct(delta, MESSAGES(k,i) );
      end
    end
    % Note: Compute the FactorMarginalization AFTER
    % FactorProduct. I have screwed this up twice now.
    sepset_vars = intersect(P.cliqueList(i).var, P.cliqueList(j).var);
    marginal_vars = setdiff( delta.var, sepset_vars );
    if isMax
      delta = FactorMaxMarginalization( delta, marginal_vars );
    else
      delta = FactorMarginalization( delta, marginal_vars );
      delta.val = delta.val ./ sum(delta.val);
    end
    MESSAGES(i,j) = delta;
    %P.cliqueList(i).var
    %P.cliqueList(j).var
    [i,j] = GetNextCliques(P, MESSAGES);
  end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% YOUR CODE HERE
%
% Now the clique tree has been calibrated. 
% Compute the final potentials for the cliques and place them in P.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for (i = 1:N)
      belief = P.cliqueList(i);
      if isMax
	 belief.val = log(belief.val);
      end
  for (k = find(P.edges(i,:) == 1))
      if isMax
	 belief = FactorSum( belief, MESSAGES( k, i ) );
      else
	belief = FactorProduct( belief, MESSAGES(k,i) );
      end
  end
  P.cliqueList(i) = belief;
end
P.cliqueList = StandardizeFactors(P.cliqueList);
return
