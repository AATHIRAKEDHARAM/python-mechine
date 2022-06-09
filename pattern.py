def pattern(n):
     
    for i in range(0, n):
     
        for j in range(i-1,4):
         
            print("* ",end="")
      
        print("\r")

n = 5
pattern(n)