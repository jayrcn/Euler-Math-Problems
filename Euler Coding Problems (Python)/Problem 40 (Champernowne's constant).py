chn = "0." #string of numbers 
l = 1000001 #value up to 1,000,000 in the fraction
for a in range (1,l):
    chn += str(a)
def d(a):
    return(int(chn[a+1]))
print(d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000))