# coding=utf-8﻿
import random
print "\t\t\t\t\t\t\t\t         Welcome to Hariyali Bank"
transaction= []
account_dictonery={}
def creating_new_account ():
    global account_dictonery
    value=[]
    print"\t\t\t\t\t\t\t\t\tCreating a new Account"
    print "\t\t\t\t\t\t\t\tEnter the whole Form in Capital Letters"
    aadhar_card_number=raw_input("Enter your Aadhar Card Number: ")
    while len(aadhar_card_number)!=12:
        aadhar_card_number=raw_input("Wrong entry Please enter your Aadhar Card Number Again: ")
    value.append(aadhar_card_number)
    first_name=raw_input("Enter your First Name: ")
    middle_name=raw_input("Enter your middle Name: ")
    last_name=raw_input("Enter your Last Name: ")
    full_name=first_name+" "+middle_name+" "+last_name
    value.append(full_name)
    YYYY="" 
    while YYYY<0000 or YYYY>2019:
        YYYY=raw_input("Enter your Date of Birth-YYYY: ")
        if YYYY.isdigit():
            YYYY=int(YYYY)
            pass
        else:
            YYYY=raw_input("Wrong entry Please Enter your Date of Birth-YYYY Again: ")
    YYYY=int(YYYY)
    MM=""
    while MM<1 or MM>12:
        MM=raw_input("Enter your Date of Birth-MM: ")
        if MM.isdigit():
            MM=int(MM)
            pass
        else:
            MM=raw_input("Wrong enter Please Enter your Date of Birth-MM Again: ")
    DD=0
    while DD<1 or DD>s:
        DD=raw_input("Enter your Date of Birth-DD: ")
        s=0
        if DD.isdigit():
            DD=int(DD)
            if MM==1 or MM==3 or MM==5 or MM==7 or MM==8 or MM==10 or MM==12:
                s=31
            elif MM==2:
                if YYYY%4==0:
                    s=29
                else:
                    s=28
            else:
                s=30
        else:
            DD=raw_input("Wrong entry Please Enter your Date of Birth-DD Again: ")
    DD=str(DD)
    MM=str(MM)
    YYYY=str(YYYY)
    date_of_birth=DD+"/"+MM+"/"+YYYY
    value.append(date_of_birth)
    gender=raw_input("Enter your Gender:")
    if gender=="MALE" or gender=="FEMALE" :
        pass
    else:
        gender=raw_input("Wrong entry Please enter again: ")
    value.append(gender)
    age=raw_input("Enter your Age: ")
    if age.isdigit():
        pass
    else:
        age=raw_input("Wrong entry Please enter your Age Again: ")
    age=int(age)
    value.append(age)
    email=""
    email=raw_input("Enter your Email Address: ")
    v=email.split("@")
    while len(v)!=2:
        email=raw_input("Enter your Email Address Again: ")
        v=email.split("@")
    value.append(email)
    city=raw_input("Enter Your City Name: ")
    value.append(city)
    district=raw_input("Enter Your District name: ")
    value.append(district)
    state=raw_input("Enter Your State Name: ")
    value.append(state)
    pincode=raw_input("Enter Pincode of your Address:")
    if pincode.isdigit():
        pincode=int(pincode)
        pass
    else:
        pincode=input("Enter Your Pincode of your Address again:")
    value.append(pincode)
    residential_address=raw_input("Enter your Residential Address: ")
    value.append(residential_address)
    permanent_address=raw_input("Enter your Permanent Address: ")
    value.append(permanent_address)
    phone_no=""
    while len(phone_no)!=10 or not phone_no.isdigit():
        phone_no=raw_input("Enter your phone number: ")
    value.append(phone_no)
    print "\t\t\t\t\t\tIt is Compulsory to Deposit RS 2000 in your Bank Account"
    cash=input("Enter cash amount for making Bank account ")
    while cash<2000:
        cash=input("Enter the Amount again: ")
    value.append(cash)
    password=random.choice(range(1000,9999))
    value.append(password)
    account_number_in_string=""
    for i in range(15):
        n=random.choice(["1","2","3","4","5","6","7","8","9"])
        account_number_in_string+=n
    print "Your Account Number: ",account_number_in_string
    print "Your Password: ",password
    account_dictonery[str(account_number_in_string)]=value
    print account_dictonery
creating_new_account()
first=True
while True:
    if first:
        print "\t\t1.LOG IN"
        user_choice=input("\t\tEnter your Choice number: ")
        ac=""
        email=""
        password=""
    if user_choice==1:
        if first:
            ac=raw_input("Enter your Account number: ")
            email=raw_input("Enter your Email Address: ")
            password=raw_input("Enter Your Password: ")
            first=False
        if ac in account_dictonery:
            print "Do you Want to-"
            print "\t1.Create a new account"
            print "\t2.Money Transfer"
            print "\t3.Account details"
            print "\t4.Shopping"
            print "\t5.Help"
            print "\t6.SIGN OUT"
            choice=input("Enter your choice number: ")
            if choice==1:
                creating_new_account()
            elif choice==2:
                transaction.append(ac)
                money_transfer_account=raw_input("Enter Account number to send money to that person: ")
                transaction.append(money_transfer_account)
                amount=input("Enter The amount: ")
                transaction.append(amount)
                date=raw_input("Enter Date: ")
                transaction.append(date)
                purpose=raw_input("Enter the reason why you want to transfer money to this bank account: ")
                transaction.append(purpose)
                print transaction
                if money_transfer_account in account_dictonery:
                    account_dictonery[ac][-2]-=amount
                    account_dictonery[money_transfer_account][-2]+=amount
                    print account_dictonery 
                else:
                    money_transfer_account=raw_input("Enter Account number to send money to that person: ")
            elif choice==3:
                print "\t\t\t\t\t\t\t Your acount details"
                print "Your Account Number-",ac
                print "Name-",account_dictonery[ac][1]
                print "Adhar Card Number-",account_dictonery[ac][0]
                print "Date of Birth-",account_dictonery[ac][2]
                print "Gender-",account_dictonery[ac][3]
                print "Age-",account_dictonery[ac][4]
                print "Email Address-",account_dictonery[ac][5]
                print "Your City Name-",account_dictonery[ac][6]
                print "Your District name-",account_dictonery[ac][7]
                print "Your State name-",account_dictonery[ac][8]
                print "Your Address Pincode-",account_dictonery[ac][9]
                print "Your Residential Address-",account_dictonery[ac][10]
                print "Your permanent address-",account_dictonery[ac][11]
                print "Your Phone Number-",account_dictonery[ac][12]
                print "Amount present in this account-",account_dictonery[ac][-2]
            elif choice==4:
                while True:
                    print "1.Mobile"
                    print "2.Laptop"
                    print "3.DSLR"
                    print "press any number to Exit"
                    ch=input("Enter your choice to buy that product: ")
                    if ch==1:
                        print "Which phone you want to buy ?"
                        print "1.Redmi Note 8 Pro (Shadow Black, 6GB RAM, 128GB Storage) by Redmi \nPrice:    ₹ 15,999.00"
                        print "2.Realme XT (Pearl Blue, 64 GB) (4 GB RAM) by realme \nPrice:    ₹17,190"
                        print "3.Vivo Y15 (Burgundy Red, 4GB RAM, 64GB Storage) by Vivo \nPrice:	 ₹ 15,990.00"
                        print "4.Vivo Y17 (Mineral Blue, 4GB RAM, 128GB Storage) by Vivo \nPrice:	₹ 18,990.00"
                        print "5.Nokia 9 PureView (Blue, 6GB RAM | 128GB Storage) by Nokia \nPrice:	   ₹ 56,299.00"
                        pch=input("Enter your choice to buy phone: ")
                        if pch==1:
                            c=15999
                            if account_dictonery[ac][-2]<c:
                                print "Your account dont have that much money"
                                pass
                            elif account_dictonery[ac][-2]>c:
                                account_dictonery[ac][-2]-=c
                            else:
                                break
                        elif pch==2:
                            c=17190
                            if account_dictonery[ac][-2]<c:
                                print "Your account dont have that much money"
                                pass
                            elif account_dictonery[ac][-2]>c:
                                account_dictonery[ac][-2]-=c
                            else:
                                break
                        elif pch==3:
                            c=15990
                            if account_dictonery[ac][-2]<c:
                                print "Your account dont have that much money"
                                pass
                            elif account_dictonery[ac][-2]>c:
                                account_dictonery[ac][-2]-=c
                            else:
                                break
                        elif pch==4:
                            c=18990
                            if account_dictonery[ac][-2]<c:
                                print "Your account dont have that much money"
                                pass
                            elif account_dictonery[ac][-2]>c:
                                account_dictonery[ac][-2]-=c
                            else:
                                break
                        elif pch==5:
                            c=56299
                            if account_dictonery[ac][-2]<c:
                                print "Your account dont have that much money"
                                pass
                            elif account_dictonery[ac][-2]>c:
                                account_dictonery[ac][-2]-=c
                            else:
                                break
                        else:
                            pch=input("Enter your choice to buy phone: ")
                    elif ch==2:
                        print "Which Laptop you want to buy ?"
                        print "1.HP Pavilion x360 Core i3 8th Gen 14-inch Touchscreen 2-in-1 Thin and Light Laptop (4GB/256GB SSD/Windows 10/MS Office/Inking Pen/Natural Silver/1.59 kg), 14-dh0107T by HP \nPrice:	₹ 52,618.50"
                        print "2.Apple MacBook Air (13-inch Retina Display, 1.6GHz Dual-core Intel Core i5, 256GB) - Gold \nPrice: 	  ₹ 1,34,900.00"
                        lch=input("Enter your choice to buy Laptop: ")
                        if lch==1:
                            c=52618
                            if account_dictonery[ac][-2]<c:
                                print "Your account dont have that much money"
                                pass
                            elif account_dictonery[ac][-2]>c:
                                account_dictonery[ac][-2]-=c
                            else:
                                break
                        elif lch==2:
                            c=134900
                            if account_dictonery[ac][-2]<c:
                                print "Your account dont have that much money"
                                pass
                            elif account_dictonery[ac][-2]>c:
                                account_dictonery[ac][-2]-=c
                            else:
                                break
                        else:
                            lch=input("Enter your choice to buy Laptop: ")
                    elif ch==3:
                        print "Which DSLR you want to buy ?"
                        print "1.Nikon COOLPIX P1000  (16 MP, 125x Optical Zoom, 4x Digital Zoom, Black)\nPrice ₹69,950"
                        print "2.Sony ILCE-7M3 Full-Frame 24.2MP Mirrorless Interchangeable Lens Camera Body Only (Black) by Sony\nPrice:	₹ 1,58,490.00"
                        print "3.Canon PowerShot SX430B 20MP Digital Camera with 45x Optical Zoom (Black) + 16GB Memory Card + Camera Case by Canon\nPrice:	₹ 14,295.00"
                        Dch=input("Enter your choice to buy DSLR: ")
                        if Dch==1:
                            c=69950
                            if account_dictonery[ac][-2]<c:
                                print "Your account dont have that much money"
                                pass
                            elif account_dictonery[ac][-2]>c:
                                account_dictonery[ac][-2]-=c
                            else:
                                break
                        elif Dch==2:
                            c=158490
                            if account_dictonery[ac][-2]<c:
                                print "Your account dont have that much money"
                                pass
                            elif account_dictonery[ac][-2]>c:
                                account_dictonery[ac][-2]-=c
                            else:
                                break
                        elif Dch==3:
                            c=14265
                            if account_dictonery[ac][-2]<c:
                                print "Your account dont have that much money"
                                pass
                            elif account_dictonery[ac][-2]>c:
                                account_dictonery[ac][-2]-=c
                            else:
                                break
                        else:
                            Dch=input("Enter your choice to buy DSLR: ")
                    else:
                        break
            elif choice==5:
                print "\t\t\t\t\tWelcome To our Help Option"
                print "1. What is Online Hariyali?"
                print "2. What is special about Internet banking?"
                print "3. I do not have a PC?"
                print "4. How do I access OnlineHariyali?"
                print "5. I do not have an account with Hariyali?"
                print "6. I am an Indian Resident. How do I open an account?"
                print "7. I am a Non-resident Indian. How do I open an account?"
                print "8. Can my school going daughter open such account?"
                print "9. I want to register for OnlineHariyali now. What do I do?"
                print "10. Why are the user name and password so cryptic?"
                print "11. Can I change the user name and password that were sent to me by courier?"
                print "12. Can I change my password?"
                print "13. What are the good practices for creating a password?"
                print "14. What happens if I forget my logon password?"
                print "15. What happens if I forget my Internet banking username?"
                print "16. I am unable to login with the user name and password sent to me by courier."
                print "17. I want to know more about State Bank of India?"
                print "18. I want to know more about OnlineHariyali?"
                print "If your problem is not present it this options then you can contact us on our \nGmail Account-Bank@gmail.com \nFacebook-Bank.Official\nTwiter-Bank.Official\nInstagram-Bank.Official\nYou can call us on our Helpline Number 1800-112211"
                problem=input("Enter Serial Number of your problem: ")
                if problem==1:
                    print"Solution-OnlineHariyali is the Internet banking service provided by State Bank of India, India's largest and premier coMMercial bank"
                elif problem==2:
                    print"Solution-Internet banking is the most convenient way to bank- anytime, any place, at your convenience."
                elif problem==3:
                    print"Solution-You can access OnlineHariyali from any computer that has connectivity to the Internet. But make sure your computer is Malware free. For more details please Click here."
                elif problem==4:
                    print"Solution-You need to have an account at a branch. You also need to register for the Internet banking service with the branch. Branch will provide you a Pre Printed Kit (PPK) containing username and password for first login. If you are not in a position to collect PPK in person, the bank will arrange to send a username through SMS and a mailer containing password to your registered address. Logon to www.onlineHariyali.com using this username and password. At the first login, you will need to go through a simple initialization process. Our Net banking assistant will guide you step by step through this process on the site."
                elif problem==5:
                    print"Solution-You are welcome to open it now. It is very easy to open an account with Hariyali. You can apply online for opening of a savings bank account. A link 'Online SB Account Application' is available on the home page of www.onlineHariyali.com or just walk in to any of our branches nearby. Our staff would be pleased to assist you."
                elif problem==6:
                    print"Solution-Follow the below simple steps:You can apply online for opening of a savings bank account. A link 'Online SB Account Application' is available on the home page of www.onlineHariyali.com OR You can collect the account opening form from a branch or download it from www.onlineHariyali.com under the link Registration Forms. ..."
                elif problem==7:
                    print"Solution-If you are on a visit to India, please follow the procedure described for a resident Indian. Please carry your passport also.If you want to open the account when you are outside India:Collect and fill the NRI Application Form...."
                elif problem==8:
                    print"Solution-Of course. Children of any age can have joint accounts with their parent or guardian.Children above 10 years of age can have their own bank account, subject to certain financial limits."
                elif problem==9:
                    print"Solution-Download the Registration Forms in the OnlineHariyali site, complete the form and submit it at your branch. Your registration formalities are complete after your details are verified and authenticated by the branch"
                elif problem==10:
                    print"Solution-The user name and password are system generated. OnlineHariyali has no control over this process. During your first visit to OnlineHariyali, you must mandatorily change your user name and password."
                elif problem==11:
                    print"Solution-Yes. It is mandatory for you to change the system generated user name and password when you first logon to OnlineHariyali. Later at any point of time, you can change your password but not the user name."
                elif problem==12:
                    print"Solution-Passwords can be changed any time and any number of times. In fact we recommend that your password should be changed periodically to secure access to your account information."
                elif problem==13:
                    print"Solution-You are requested to select a word that is not available in an English Dictionary.\nDo not assign your name, your family or vehicle number as your password as it can be easily guessed...."
                elif problem==14:
                    print"Solution-Click on the 'Forgot password' link in the site and provide the requested information. A new password will be sent to your registered address within 10 working days."
                elif problem==15:
                    print"Solution-If you forget the Internet banking user name, contact your branch and re-register yourself."
                elif problem==16:
                    print"Solution-The user name and password are cryptic in nature because they are system generated and are case sensitive. When you are typing the user name and password for the first time, ensure that you type the characters as they appear in the document sent to you. If you still encounter problems, register your issue in the 'Complaints' link in the login page."
                elif problem==17:
                    print"Solution-We are glad about the interest you have evinced in Hariyali. Please log into www.Hariyali.co.in for more details."
                elif problem==18:
                    print"Solution-We would be glad to answer any specific queries. Please call our toll free number 1800-112211"
            elif choice==6:
                    print "Thanks For using This program"
                    print "You are successfull LOG OUT"
                    break
        else:
            print "\t\t\t\t\t\tWrong entry please enter all the Entry again"
            ac=raw_input("Enter Your account number again:")
            email=raw_input("Enter your email address again:")
            password=raw_input("Enter your password again:")
