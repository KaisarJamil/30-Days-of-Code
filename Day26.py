a_date=str(input()).split(" ")
e_date=str(input()).split(" ")

ad=int(a_date[0])
am=int(a_date[1])
ay=int(a_date[2])

ed=int(e_date[0])
em=int(e_date[1])
ey=int(e_date[2])

fine=0

if ay>ey:
    fine=10000
elif ay==ey:
    if am>em:
        fine=500*(am-em)
        
    elif am==em and ad>ed:
        fine=15*(ad-ed)

print(fine)
        
