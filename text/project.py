import os
import random

def accinformation():
    code=(input("Account Number: "))
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


def opennewaccount():
    f=open('accounts.txt','a')
    date=input("Input date:")
    code=int(random.randint(4356,5432))
    name=input("Input Name:")
    birth=input("Input DOB:")
    telno=int(input("Input Telephone Number:"))
    mobno=int(input("Input Mobile Number:"))
    address=input("Input Address:")
    rec=str(code)+','+name+','+address+','+date+','+str(telno)+','+str(mobno)+','+birth+','+',0.0\n'
    f.write(rec)
    print(rec)
    f.close()


def detmodification():
    code=(input("Account Number: "))
    tf=open("temp.txt",'w')
    f=open('accounts.txt','r')
    found=0
    found=0
    for rec in f:
        rec=rec.strip().split(',')
        if rec[0]==code:
                print(rec)
                rec[1]=input("New Name:")
                rec[2]=input("New Adress:")
                rec[4]=str(int(input("New Tele #:")))
                rec[5]=str(int(input("New Mobile #:")))
                rec[6]=input("New DOB:")
                found=1
        rec=','.join(rec)
        print(rec)
        tf.write(rec)
    f.close()
    tf.close()
    if found==0:
        print("Account does not exist")
    else:
       os.remove('accounts.txt')
       os.rename("temp.txt",'accounts.txt')


def closeaccount():
    f=open('accounts.txt','r')
    tf=open("temp.txt",'w')
    code=(input("Enter the Account Number:"))
    found=0
    for rec in f:
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
       os.remove('accounts.txt')
       os.rename("temp.txt",'accounts.txt')


def transaction():
    code=(input("Account Number: "))
    trans=input("Withdrawal or Deposit? (W/D): ")
    tf=open("temp.txt",'w')
    trf=open("tr.txt",'w')
    f=open('accounts.txt','r')
    found=0
    for rec in f:
        rec=rec.strip().split(',')
        if rec[0]==code:
            print(rec)
            qty=str(float(input("Enter the amount: ")))
            td=input("Enter today's date: ")
            if trans=='W':
                rec[7]=str(float(rec[7])-float(qty))
            else:
                rec[7]=str(float(rec[7])+float(qty))
            found=1
            trec=[rec[0],str(td),str(trans),str(qty)]
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
       os.remove('accounts.txt')
       os.remove('trans.txt')
       os.rename("temp.txt",'accounts.txt')
       os.rename("tr.txt",'trans.txt')
    print()


def transhistory():
    code=(input("Account Number: "))
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
    code=(input("Account Number:"))
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


menu='''1.OPENING AN ACCOUNT
2.CLOSING AN ACCOUNT
3.MODIFICATION OF PERSONAL DETAILS
4.TRANSACTION, DEPOSIT(D) OR WITHDRAWAL(W)
5.DISPLAY ACCOUNT INFORMATION
6.CALCULATION OF INTEREST
7.TRANSACTION HISTORY
8.PASSBOOK
0.EXIT
'''
while 1:
    print(menu)
    print()
    choice=int(input('Input Choice : '))
    if choice==1:
        opennewaccount()

    elif choice==2:
        closeaccount()

    elif choice==3:
        detmodification()

    elif choice==4:
        transaction()

    elif choice==5:
        accinformation()

    elif choice==6:
        interest()

    elif choice==7:
        transhistory()

    elif choice==8:
        passbook()

    elif choice==0:
        exit()
