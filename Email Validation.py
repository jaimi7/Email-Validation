email=input("Enter Email Id : ")

# check Length  Example : j@g.in
if len(email)>=6:
    # check first character is alphabet
    if email[0].isalpha():
        # check @ is present or not and check value of @ is 1
        if ("@" in email) and (email.count("@")==1):
            # check position of "."
                # use ^ : both condition can not be true in one email
                #  for      .com         .in
            if (email[-4]==".") ^ (email[-3]=="."):
                # check email character
                j,k,l=0,0,0
                for i in email:
                    # don't have space
                    if i==i.isspace():
                        j=1
                    # all characters are small
                    elif i.isalpha():
                        if i==i.upper():
                            k=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        l=1
                if j==1 or k==1 or l==1:
                    print("Wrong Email. \n # Error in :  check email character")
                else:
                    print("Right Email. ")
            else:
                print("Wrong Email.  \n  # Error in : check position of ' . ' ")
        else:
            print("Wrong Email.  \n # Error in : check @ is present or not and check value of @ is 1")
    else:
        print("Wrong Email. \n # Error in : check first character is alphabet")
else:
    print("Wrong Email.  \n # Error in :  check Length  Example : j@g.in")
