x=[5,2,4,18,9,1]

def nho_den_lon(x):
  #  n=len(v)
    #for i in range(0,x-1):
     #   for j in range(i+1,x):
      #      if v[i]>v[j]:
       #         v[i],v[j]=v[j],v[i]
   x.sort()
   return x

a=nho_den_lon(x)
print(a)

    
