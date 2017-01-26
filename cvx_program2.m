n=100;

cvx_begin
    variable xcvx(n);
    minimize (sum(abs(xcvx)+0.1*(xcvx)));
cvx_end