def case(n):
    print("+"+("-"*(n+1))+"+")
    tiretfin=n
    for i in range(n):
        print("|"+("#"*n)+" "+("#"*i)+"|")
        n=n- 1
    print("+"+("-"*(tiretfin+1)+"+"))
case(10)
