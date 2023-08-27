%Program 1.5 Gaussian Elimination 
%compute approximate solution of UX=b, where U is a upper triangular matrix
%Inpute: matrix L, colume b
%Output: solution X
function xc=upper_triangular_matrix(U,b)
    n=length(U);
    for j=n-1:2
        b(j)=b(j)/U(j,j);
        b(1:j-1)=b(1:j-1)-b(j)*U(1:j-1,j);
    end
    b(1)=b(1)/U(1,1);
    xc=b;