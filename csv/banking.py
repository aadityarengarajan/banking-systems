import csv
import os
import random

inter=0.4

f=open('account.csv','r')
rd=csv.reader(f)
c=0
accounts=[]
for line in rd:
    if c==0:
        c+=1
        pass
    else:
        accounts.append(line)
f.close()

def openaccount():
    acctno=random.randint(2543254,3443254)
    name=input("Account Holder Name : ")
    address=input("Account Holder Address : ")
    tel=int(input("Account Holder Telephone # : "))
    mob=int(input("Account Holder Mobile # : "))
    date=input("Today's Date : ")
    dob=(input("Account Holder Date of Birth (DOB) : "))
    bal=int(input("Account Holder Initial Balance : "))
    line=[acctno,name,address,tel,mob,date,dob,inter,bal]
    with open('account.csv', 'w', newline='') as thecsv:
        writer = csv.writer(thecsv)
        writer.writerow(['acctno','name','address','opendate','tel','mob','dob','inter','bal'])
        writer.writerows(accounts)
        writer.writerow(line)

def closeaccount(acctnum):
    thecsv=open('account.csv','w')
    writer = csv.writer(thecsv)
    writer.writerow(['acctno','name','address','opendate','tel','mob','dob','inter','bal'])
    for acct in accounts:
        acctno=acct[0]
        if acctno==acctnum:
            pass
        else:
            writer.writerow(acct)
    thecsv.close()

def modaccount(acctnum):
    opns='''1. Name
2. Address
3. Telephone #
4. Mobile #
5. Date of Birth'''
    option=int(input("Modify : "))
    for acct in accounts:
        if acct[0]==acctnum:
            name=acct[1]
            address=acct[2]
            opendate=acct[3]
            tel=acct[4]
            mob=acct[5]
            dob=acct[6]
            inter=acct[7]
            bal=acct[8]
    if option==1:
        name=input("Name : ")
    if option==2:
        address=input("Address : ")
    if option==3:
        tel=input("Tel : ")
    if option==4:
        mob=input("Mob : ")
    if option==5:
        dob=input("DOB : ")
    modrow=[acctnum,name,address,opendate,tel,mob,dob,inter,bal]
    thecsv=open('account.csv','w')
    writer = csv.writer(thecsv)
    writer.writerow(['acctno','name','address','opendate','tel','mob','dob','inter','bal'])
    for acct in accounts:
        acctno=acct[0]
        if acctno==acctnum:
            writer.writerow(modrow)
        else:
            writer.writerow(acct)
    thecsv.close()

def deposit(acctnum, amount):
    option=int(input("Modify : "))
    for acct in accounts:
        if acct[0]==acctnum:
            name=acct[1]
            address=acct[2]
            opendate=acct[3]
            tel=acct[4]
            mob=acct[5]
            dob=acct[6]
            inter=acct[7]
            bal=acct[8]
    bal=int(bal)+amount
    bal=str(bal)
    modrow=[acctnum,name,address,opendate,tel,mob,dob,inter,bal]
    thecsv=open('account.csv','w')
    writer = csv.writer(thecsv)
    writer.writerow(['acctno','name','address','opendate','tel','mob','dob','inter','bal'])
    for acct in accounts:
        acctno=acct[0]
        if acctno==acctnum:
            writer.writerow(modrow)
        else:
            writer.writerow(acct)
    thecsv.close()

    modrow=[acctnum,'deposit',amount]
    thecsv=open('transaction.csv','w')
    writer = csv.writer(thecsv)
    writer.writerow(['acctno','type','diff'])
    for acct in accounts:
        acctno=acct[0]
        if acctno==acctnum:
            writer.writerow(modrow)
        else:
            writer.writerow(acct)
    thecsv.close()

def withdraw(acctnum, amount):
    option=int(input("Modify : "))
    for acct in accounts:
        if acct[0]==acctnum:
            name=acct[1]
            address=acct[2]
            opendate=acct[3]
            tel=acct[4]
            mob=acct[5]
            dob=acct[6]
            inter=acct[7]
            bal=acct[8]
    bal=int(bal)-amount
    bal=str(bal)
    modrow=[acctnum,name,address,opendate,tel,mob,dob,inter,bal]
    thecsv=open('account.csv','w')
    writer = csv.writer(thecsv)
    writer.writerow(['acctno','name','address','opendate','tel','mob','dob','inter','bal'])
    for acct in accounts:
        acctno=acct[0]
        if acctno==acctnum:
            writer.writerow(modrow)
        else:
            writer.writerow(acct)
    thecsv.close()

    modrow=[acctnum,'withdrawal',amount]
    thecsv=open('transaction.csv','w')
    writer = csv.writer(thecsv)
    writer.writerow(['acctno','type','diff'])
    for acct in accounts:
        acctno=acct[0]
        if acctno==acctnum:
            writer.writerow(modrow)
        else:
            writer.writerow(acct)
    thecsv.close()

def display(acctnum):
    for acct in accounts:
        if acct[0]==acctnum:
            print('Account Holder Name',acct[1])
            print('Account Holder Address',acct[2])
            print('Date Opened',acct[3])
            print('Telephone Number',acct[4])
            print('Mobile Number',acct[5])
            print('Date of Birth',acct[6])
            print('Interest',acct[7])
            print('Balance',acct[8])
        else:
            pass

def inter(acctnum):
    # Interest I = PRT
    t=int(input("Time(in Days): "))
    r=inter
    for acct in accounts:
        if acct[0]==acctnum:
            p=acct[8]
    print("Interest = Rs. ",p*r*t)

def bankstatement(acctnum):
    thecsv=open('transaction.csv','r')
    reader = csv.reader(thecsv)
    for line in reader:
        if line[0]==acctnum:
            print('Account #',line[0])
            print('Transaction Type',line[1])
            print('Change in Balance',line[2])

def passbook(acctnum):
    print('Pass book')
    display(acctnum)
    transrep(acctnum)

menu='''Operations
1.Open an account
2.Close an account
3.Modify details
4.Display Account Details
5.Calculate Interest

Transactions
6.Deposit
7.Withdraw

Reports
8.Balance of Account
9.Passbook
10.Bank Statement

0.Exit
'''
print(menu)
op=int(input('Enter Op : '))
if op==1:
    openaccount()
elif op==2:
    acctno=int(input('Enter Account Number : '))
    closeaccount(acctno)
elif op==3:
    acctno=int(input('Enter Account Number : '))
    modaccount(acctno)
elif op==4:
    acctno=int(input('Enter Account Number : '))
    display(acctno)
elif op==5:
    acctno=int(input('Enter Account Number : '))
    inter(acctno)
elif op==6:
    acctno=int(input('Enter Account Number : '))
    amount=int(input('Enter Amount : '))
    deposit(acctno,amount)
elif op==7:
    acctno=int(input('Enter Account Number : '))
    amount=int(input('Enter Amount : '))
    withdraw(acctno,amount)
elif op==8:
    acctno=int(input('Enter Account Number : '))
    display(acctno)
elif op==9:
    acctno=int(input('Enter Account Number : '))
    passbook(acctno)
elif op==10:
    acctno=int(input('Enter Account Number : '))
    bankstatement(acctno)
elif op==0:
    quit()