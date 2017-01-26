% Generate a random problem instance.
%randn('state', 10239); 
m = 400; n = 200;
A = randn(m, n); %ATA = A'*A;
b = randn(m, 1);
l = 0.1;
TOL = 0.001;
xcoord = zeros(n, 1);
% Solve in cvx as a benchmark.
cvx_begin
    variable xcvx(n);
    minimize (sum_square(A*xcvx + b) + l*norm(xcvx, 1));
cvx_end
% Solve using coordinate-wise descent.
while abs(cvx_optval - (sum_square(A*xcvx + b) + l*norm(xcvx, 1)))/cvx_optval > TOL
    for i = 1:n
        xcoord(i) = 0; ei = zeros(n,1); ei(i) = 1;
        c = 2/l*ei'*(ATA*xcoord + A'*b);
        xcoord(i) = -sign(c)*pos(abs(c) - 1)/(2*ATA(i,i)/l);
    end
%display(sum_square(A*xcoord + b) + ...
                  %l*norm(xcoord, 1))
end