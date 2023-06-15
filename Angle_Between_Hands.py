h,m=map(int,input().split(':'))
if h==12:
    h=0
if m==60:
    m=0
hr=0.5*(h*60+m)
mn=6*m
angle=abs(hr-mn)
print(min(360-angle,angle))