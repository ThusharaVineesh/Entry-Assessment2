#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Bank:
    bankname='SBI'
    branch='Thrissur'
    ifsccode='45689466'
    def __init__(self,username,pin_number):
        self.u=username
        self.p=pin_number
        self.balance=0
    def logininfo(self):
        address=input('Enter your address ')
        pancardnumber=input('Enter your PAN card number')
        mobilenumber=input('Enter your mobile number ')
        adharnumber=input('Enter your Adhar')
    def deposition(self):
        depositing_amount=int(input('Enter the amount = '))
        self.balance+=depositing_amount
        print(f'Amount of {depositing_amount} credited to your account successfully ,your current balance is{self.balance}')
    def withdrawel(self):
        withdrawying_amount=int(input('Enter the amount = '))
        if withdrawying_amount<=self.balance:
            self.balance-=withdrawying_amount
            print(f'Amount of {withdrawying_amount} debited from your account successfully ,your current balance is{self.balance}')
        else:
            print('Insufficient Amount')
    def customerdetails(self):
        print('Customer name :',self.username)
        print('Address : ',self.address)
        print('MobileNumber :',self.mobilenumber)
        print('Adhar number :',self.adharnumber)
        print('Bank Name : ',self.bankname)
        print('ifsccode : ',self.ifsccode)
        print('Branch :',self.branch)
        
def main():
    print(' Heloo Welcome to State bank of india ')
    function=int(input('if you are a new user please choose 1\n if your are a exisiting user please choose 2'))
    if function==1:
        username=input('Enter yourname ')
        pin_number=input('Enter a new Atm Pin ')
        user=Bank(username,pin_number)
        user.logininfo()
    elif function==2:
                username=input('Enter your existing user name')
                pin_number=input('Enter your existing pin_number')
                user=Bank(username,pin_number)
    selection=int(input('select 1 for deposit\nselect 2 for withdraw \nselect 3 for checking  your customer details'))
    if selection==1:
            user.deposition()
    elif selection==2:
            user.withdrawel()
    elif selection==3:
            user.customerdetails()
            
    print('Thank you for using SBI')
                        
                 
                
        
        
        


# In[6]:


main()


# In[ ]:




