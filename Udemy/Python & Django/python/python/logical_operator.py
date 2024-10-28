#case 1
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for Loan")

#case 2
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for Loan")
else:
    print("NOT Eligible for Loan")

#case 3

has_high_income = True
has_criminal_rec = False
if has_high_income and not has_criminal_rec:
    print("Eligible for Loan")
else:
    print("NOT Eligible for Loan")


#case 4

has_high_income = True
has_criminal_rec = True
if has_high_income and not has_criminal_rec:
    print("Eligible for Loan")
else:
    print("NOT Eligible for Loan")