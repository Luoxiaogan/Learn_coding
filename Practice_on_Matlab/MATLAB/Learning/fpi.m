%Program 1.2 Fixed_point Iteration
%compute approximate solution of g(x)=x
%Inpute: fuction handle g, starting guess x0,
%        number of iteration steps k
%Output: Approximate solution xc
function xc=fpi(g,x0,k)
    x(1)=x0;
    for i=1:k
        x(i+1)=g(x(i));
    end
    xc=x(k+1);
    