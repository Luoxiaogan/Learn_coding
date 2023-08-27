%Program 1.5 Gaussian Elimination 
%compute approximate solution of AX=b, where A is a lower triangular matrix
%Inpute: matrix L, colume b
%Output: solution X
function xc=lower_triangular_matrix(L,b)
    n=length(L); %a lower triangular matrix A is absolutly n*n
    for j=1:n-1
        b(j)=b(j)/L(j,j);
        b(j+1:n)=b(j+1:n)-b(j+1:n)-b(j)*L(j+1:n,j);
    end
    b(n)=b(n)/L(n,n);
    xc=b;