num_of_pass=3
num_of_bag=2
security_check=True

for passenger in range(1,num_of_pass+1):
    for bag in range(1,num_of_bag+1):
        if(security_check==True):
            print(f"Security check of passenger:{passenger} baggage={bag} baggage cleared")
        else:
            print(f"Security check of passengers:{passenger} baggage={bag} baggage not cleared")
