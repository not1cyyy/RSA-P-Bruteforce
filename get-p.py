from Crypto.Util.number import isPrime

q = int(input("Enter Q : "))
dp = int(input("Enter DP : "))
e = int(input("Enter e : "))

if isPrime(q):
    for kp in range(3, e):
        p_mul = dp * e - 1
        if p_mul % kp == 0:
            p = (p_mul // kp) + 1
            if isPrime(p):
                print(f"Integer P found : {p} ")
                break
else :
    print("Error : Q is not a prime integer")
    exit(1)