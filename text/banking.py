#Account Number, Name, Address, Date, Tel, Mob, DOB, Balance
from os import remove,rename
import random
def dispinfo():
    code=int(input("Account Number: "))
    f=open("accounts.txt",'r')
    found=0
    for rec in f:
        rec=rec.strip().split(',')
        if rec[0]==code:
            print(rec)
            found=1
    if found==0:
        print("Code does not exist")
    print()
def interest():
    p=int(input("Input Principle:"))
    t=int(input("Input Time:"))
    r=int(input("Input Rate:"))
    print(p*r*t/100)
    print()
def openanewaccount():
    f=open('accounts.txt','a')
    while True:
        date=input("Input date:")
        code=int(random.randint(5432,4356))
        name=input("Input Name:")
        birth=input("Input DOB:")
        telno=int(input("Input Telephone Number:"))
        mobno=int(input("Input Mobile Number:"))
        address=input("Input Address:")
        rec=f"{date},{code},{name},{birth},{telno},{mobno},{address},{0.0}\n"
        f.write(rec)
        print(rec)
    f.close()
def modifyacc():
    code=int(input("Account Number: "))
    trans=input("Withdrawal or Deposit? (W/D): ")
    tf=open("temp.tmp",'w')
    trf=open("tr.tmp",'w')
    f=open('accounts.txt','r')
    found=0
     found=0
    for rec in f:
        rec=rec.strip().split(',')
        if rec[0]==code:
                print(rec)
                rec[1]=input("New Name:")+'\n'
                rec[2]=input("New Adress:")+'\n'
                rec[4]=int(input("New Tele #:"))+'\n'
                rec[5]=int(input("New Mobile #:"))+'\n'
                rec[6]=input("New DOB:")+'\n'
                found=1
        rec=','.join(rec)
        print(rec)
        tf.write(rec)
        trf.write(trec)
    f.close()
    tf.close()
    trf.close()
    if found==0:
        print("Account does not exist")
    else:
       remove('accounts.txt')
       remove('trans.txt')
       rename("temp.tmp",'accounts.txt')
       rename("tr.tmp",'trans.txt')
def closeanaccount():
    f=open('accounts.txt','r')
    tf=open("temp.tmp",'w')
    code=int(input("Enter the Account Number:"))
    found=0
    for rec in f1:
        rec=rec.strip().split(',')
        if rec[0]==code:
            found=1
        else:
            tf.write(rec)
    print()
    f.close()
    tf.close()
    if found==0:
        print("Account does not exist")
    else:
       remove('accounts.txt')
       rename("temp.tmp",'accounts.txt')
def transaction():
    code=int(input("Account Number: "))
    trans=input("Withdrawal or Deposit? (W/D): ")
    tf=open("temp.tmp",'w')
    trf=open("tr.tmp",'w')
    f=open('accounts.txt','r')
    found=0
     found=0
    for rec in f:
        rec=rec.strip().split(',')
        if rec[0]==code:
            print(rec)
            qty=float(input("Enter the amount: "))
            td=input("Enter today's date: ")
            if trans=='W':
                rec[7]=str(float(rec[7])-qty)
            else:
                rec[7]=str(float(rec[7])+qty)
            found=1
            trec=[rec[0],td,trans,qty]
        rec[7]=rec[7]+'\n'
        rec=','.join(rec)
        trec=','.join(trec)
        print(rec)
        tf.write(rec)
        trf.write(trec)
    f.close()
    tf.close()
    trf.close()
    if found==0:
        print("Account does not exist")
    else:
       remove('accounts.txt')
       remove('trans.txt')
       rename("temp.tmp",'accounts.txt')
       rename("tr.tmp",'trans.txt')
    print()
def transactionhist():
    code=int(input("Account Number: "))
    f=open("trans.txt",'r')
    found=0
    for rec in f:
        rec=rec.strip().split(',')
        print(rec)
        found=1
    if found==0:
        print("Code does not exist")
    print()
def passbook():
    code=int(input("enter the account number:"))
    f=open("trans.txt",'r')
    found=0
    for rec in f:
        rec=rec.strip().split(',')
        if rec[0]==code:
            print(rec)
            found=1
    if found==0:
        print("Code does not exist")
    print()
menu='''
'''
while 1:
    print(menu)
    print()
    choice=int(input('Input Choice : '))
    if choice==1:

    elif choice==2:

    elif choice==3:

    elif choice==4:

    elif choice==5:

    elif choice==6:

    elif choice==7:

    elif choice==8:

    elif choice==9:
