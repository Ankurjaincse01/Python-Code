sales=int(input("enter a total sales of the month "))
if sales>=100000:
    baisc=4000
    hra=20*baisc/100
    da=110*baisc/100
    inentive=4*baisc/100
    bonus=1000
    coveyance=500
else:
    baisc=4000
    hra=10*baisc/100
    da=110*baisc/100
    inentive=sales*4/100
    bonus=500
    coveyance=500
salary=baisc+hra+da+inentive+bonus+coveyance
print("salary reepit of emplyment ")
print("total slaes =",sales)
print("basic =",hra)
print("HRA=",hra)
print("DA",da)
print("incenvtive=",inentive)
print("bonus", bonus)
print("conveyance",coveyance)
print("gross salary ",salary)
