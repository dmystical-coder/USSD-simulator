import random
import time

print("This is a Console based Simulation of a USSD operation in Python.")
time.sleep(2)
print("")

print("Author : Abdulsalam Baruwa(de_mystical_coder)")
time.sleep(2)
print("")

print("Buy #500 Data plan and get a whooping 1GB data on your line valid for 14 days.Dial *141# now to Subscribe!")
time.sleep(2)
print("")

dialer = input("Dial *141# here! : ")
print("")
print("...USSD Code Running, Please wait...")
time.sleep(3)
print("")
if dialer == "*141#":
    print("Dear Valued Customer, WELCOME TO THE SMARTPHONE NETWORK.")
    print(" Please Select the action you want to perform:")
    print("1) Buy a Data Plan")
    print("2) Buy Airtime")
    print("3) Check Data Balance")
    print("4) Buy a Mega Plan")
    print("5) Check Account Balance")
    print("6) EXIT")
else:
    print("Connection Problem or invalid MMI code.")
    exit()

reply = input("  Reply : ")
print("")
print("...USSD Code Running, Please wait...")
time.sleep(3)
print("")
if reply == "1":
    print(" Please select:")
    print(" a) Mini plans")
    print(" b) Monthly Plans")
    print(" c) Night and Weekend plans")
    print(" d) Exit")
    reply1 = input("Reply : ")
    print("")
    print("...USSD Code Running, Please wait...")
    time.sleep(3)
    print("")
    if reply1 == "a":
        print("1.N50 for 40MB \n2.N100 for 115MB \n3.N200 for 350MB\n4.N500 for 750MB (Valid for 14 days.) ")
        response_a = input("Reply: ")
        print("")
        print("...USSD Code Running, Please wait...")
        if response_a == "1":
            print("Congrats! Your account has been credited with 40MB valid for 1 day.")
        elif response_a == "2":
            print("Congrats! Your account has been credited with 115MB valid for 1 day.")
        elif response_a == "3":
            print("Congrats! Your account has been credited with 350MB valid for 3 days.")
        elif response_a == "4":
            print("Congrats! Your account has been credited with 750MB valid for 14 days.")
        else:
            print("Invalid Response")

    elif reply1 == "b":
        print("1.N1000=2.9GB 30Days incl 1GB night \n2.N1500=4.1GB 30Days incl 600MB night \n "
              "3.N2000=5.8GB 30Days incl 600MB night \n4.N2500=7.7GB 30 days incl 900MB night ")
        response_b = input("Reply : ")
        print("")
        print("...USSD Code Running, Please wait...")
        time.sleep(3)
        print("")
        if response_b == "1":
            print("Congrats! Your account has been credited with 2.9GB valid for 30 days.")
        elif response_b == "2":
            print("Congrats! Your account has been credited with 4.1GB valid for 30 days.")
        elif response_b == "3":
            print("Congrats! Your account has been credited with 5.8GB valid for 30 days.")
        elif response_b == "4":
            print("Congrats! Your account has been credited with 7.7GB valid for 30 days.")
        else:
            print("Invalid Response")

    elif reply1 == "c":
        print("1.N25= 250MB 1Day(12am-05am) \n2.N50= 500MB 1Day (12am-05am) \n "
              "3.N100= 1GB 5Days (12am-05am) \n4.N200= 1.25GB 1Day SUN \n 5.N500= 3GB 2Days SAT-SUN ")
        response_c = input("Reply : ")
        print("")
        print("...USSD Code Running, Please wait...")
        time.sleep(3)
        print("")
        if response_c == "1":
            print("Congrats! Your account has been credited with 250MB night plan valid 12am-05am.")
        elif response_c == "2":
            print("Congrats! Your account has been credited with 500MB night plan valid 12am-05am.")
        elif response_c == "3":
            print("Congrats! Your account has been credited with 1GB night plan valid 12am-05am.")
        elif response_c == "4":
            print("Congrats! Your account has been credited with 1.25GB weekend plan valid for Sunday.")
        elif response_c == "5":
            print("Congrats! Your account has been credited with 3GB weekend plan valid SAT-SUN.")
        else:
            print("Invalid Response")

    elif reply1 == "d":
        exit()
    
elif reply == "2":
    print("Please Select:")
    print("1.N100")
    print("2.N200")
    print("3.N500")
    print("4.N1000")
    reply2 = input("Reply : ")
    print("")
    print("...USSD Code Running, Please wait...")
    time.sleep(3)
    print("")
    if reply2 == "1":
        for (x) in range(1):
            print("Here's Your Recharge Card :", random.randint(1, 5)*1232, 4213, 1423, 1042)
            print("To recharge: Dial *126*recharge card#")
            print("Thanks so much for your patronage")
    elif reply2 == "2":
        for (x) in range(1):
            print("Here's Your Recharge Card :", random.randint(1, 5) * 1232, 4213, 1324, 1204)
            print(" To recharge: Dial  *126*recharge card#")
            print("Thanks so much for your patronage")
    elif reply2 == "3":
        for (x) in range(1):
            print("Here's Your Recharge Card :", random.randint(1, 5) * 1232, 4213, 1221, 1004)
            print("To recharge:*126*recharge card#")
            print("Thanks so much for your patronage")
    elif reply2 == "4":
        for (x) in range(1):
            print("Here's Your Recharge Card :", random.randint(1, 5) * 1232, 4213, 2233, 4102)
            print("To recharge:*126*recharge card#")
            print("Thanks so much for your patronage")
    else:
        print("you haven't replied correctly,please try to be more careful next time!")

elif reply == "3":
    print("Dear Customer, You are using Flexi Recharge at #1 per MB.\n "
          "Please Dial *777# to choose a data bundle of your choice.")
elif reply == "4":
    print("Please Select:")
    print("1.N10000= 32.5GB 30Days")
    print("2.N15000= 52.5GB 30Days")
    print("3.N20000= 78.7GB 30Days")
    print("4.Exit")
    print("")
    time.sleep(1)
    reply4 = input("Reply: ")
    time.sleep(3)
    print("")
    if reply4 == "1":
        print("Congrats! Your account has been credited with 32.5GB valid for 30Days.")
    elif reply4 == "2":
        print("Congrats! Your account has been credited with 52.5GB valid for 30Days.")
    elif reply4 == "3":
        print("Congrats! Your account has been credited with 78.7GB valid for 30Days.")
    elif reply4 == "4":
        exit()
    else:
        print("you haven't replied correctly,please try to be more careful next time!")

elif reply == "5":
    print("ON YOUR MAIN BALANCE, YOUR CREDIT IS EMPTY")
elif reply == "6":
    quit()
else:
    print("You have entered an incorrect option.")
time.sleep(2)
print("GLO... Unlimited!")
