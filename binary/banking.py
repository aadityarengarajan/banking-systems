#Date Account Opened, Account Number,Name,Date of Birth,Telephone Number,Mobile Number,Address,Balance

import random
import pickle
from os import remove,rename

fn='accounts.dat'

def reCreate():
    f1=open(fn,'wb')
    f2=open('trans.dat','wb')
    f1.close()
    f2.close()

def newacc():
    f=open(fn,'ab')
    while True:
        date=input("enter the date:")
        code=int(random.randint(64765348,6325432544))
        name=input("enter the name:")
        birth=input("enter the date of birth:")
        telno=int(input("enter the telephone number:"))
        mobno=int(input("enter the mobile number:"))
        address=input("enter the address:")
        rec=[date,code,name,birth,telno,mobno,address,0.0]
        pickle.dump(rec,f)
        print(rec)
        more=input("More data (y/n)? ")
        if more in 'Nn':
            break
    f.close()

def transaction():
    print("     Modify")
    code=int(input("account number: "))
    transactiontype=input("transaction type (W=withdraw/D=deposit): ")
    tf=open("temp.tmp",'wb')
    trf=open("tr.tmp",'wb')
    f=open(fn,'rb')
    found=0
    while True:
        try:
            rec=pickle.load(f)
            if rec[1]==code:
                print(rec)
                qty=float(input("change in balance: "))
                date=(input("date: "))
                if transactiontype in "Ww":
                    qty=qty*(-1)
                rec[7]=rec[7]+qty
                transrec=[random.randint(2543254,3443254),rec[1],date,transactiontype,qty]
                found=1
            pickle.dump(rec,tf)
            pickle.dump(transrec,trf)
        except:
            break
    f.close()
    tf.close()
    trf.close()
    if found==0:
        print("Account does not exist")
    else:
       remove(fn)
       remove('trans.dat')
       rename("temp.tmp",fn)
       rename("tr.tmp",'trans.dat')
    print()

def modifyacc():
    f=open(fn,'rb')
    tf=open("temp.tmp",'wb')
    code=int(input("enter the account number:"))
    found=0
    while True:
        try:
            rec=pickle.load(f)
            if rec[1]==code:
                print(rec)
                rec[2]=input("enter the name:")
                rec[3]=input("enter the date of birth:")
                rec[4]=int(input("enter the telephone number:"))
                rec[5]=int(input("enter the mobile number:"))
                rec[6]=input("enter the address:")
                found=1
            pickle.dump(rec,tf)
        except:
            break
    f.close()
    tf.close()
    if found==0:
        print("Account does not exist")
    else:
       remove(fn)
       rename("temp.tmp",fn)
    print()
    

def calculateinterest():
    f=open(fn,'rb')
    code=int(input("enter account number:"))
    t=int(input("enter time of interest in days:"))
    r=int(input("enter rate of interest:"))
    while True:
        try:
            rec=pickle.load(f)
            if rec[1]==code:
                p=rec[7]
                interest=p*r*t/100
                print('interest will be ',interest)
                found=1
        except:
            break
    if found==0:
        print("Account does not exist")
    f.close()
    print()

def closeacc():
    f=open(fn,'rb')
    tf=open("temp.tmp",'wb')
    code=int(input("enter the account number:"))
    found=0
    while True:
        try:
            rec=pickle.load(f)
            if rec[1]==code:
                pass
                found=1
            else:
                pickle.dump(rec,tf)
        except:
            break
    f.close()
    tf.close()
    if found==0:
        print("Account does not exist")
    else:
       remove(fn)
       rename("temp.tmp",fn)


def dispinfo():
    f=open(fn,'rb')
    while True:
        try:
            rec=pickle.load(f)
            print(rec)
        except:
            break
    print()
    f.close()

def transactionhist():
    f=open('trans.dat','rb')
    while True:
        try:
            rec=pickle.load(f)
            print(rec)
        except:
            break
    print()
    f.close()

def passbook():
    code=int(input("enter the account number:"))
    f=open('trans.dat','rb')
    while True:
        try:
            rec=pickle.load(f)
            if rec[1]==code:
                print(rec)
                found=1
        except:
            break
    if found==0:
        print("Account does not exist")
    print()
    f.close()

menu='''1-open account
2-modify account
3-close account
4-transaction
5-calculate interest
6-display information
7-bank transaction history
8-passbook
9-exit
'''

while 1:
    print(menu)
    print()
    choice=int(input('enter ur choice : '))
    if choice==1:
        newacc()
    elif choice==2:
        modifyacc()
    elif choice==3:
        closeacc()
    elif choice==4:
        transaction()
    elif choice==5:
        calculateinterest()
    elif choice==6:
        dispinfo()
    elif choice==7:
        transactionhist()
    elif choice==8:
        passbook()
    elif choice==9:
        quit()