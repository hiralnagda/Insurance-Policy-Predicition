#!C:\Users\HIRAL\Anaconda3\python
import cgi
import cgitb
import numpy as np
from sklearn import tree
from sklearn.externals import joblib


#import first#found this but isn't used?

form = cgi.FieldStorage()

Age = form.getvalue('age')
income  = int(form.getvalue('Income'))/100000
maratialStatus=form.getvalue('maratialStatus')

if maratialStatus=="Married":
    maratialStatus=1
else:
    maratialStatus=0

gender=form.getvalue('gender')
if gender=="Male":
    gender=1
else:
    gender=0

edu=form.getvalue('edu')
if edu=="student":
    edu=0
elif edu=="HSC":
    edu=1
elif edu=="undergraduate":
    edu=2
else:
    edu=3

smoker=form.getvalue('Smoker')
if smoker=="Yes":
    smoker=1
else:
    smoker=0

No_Kids=int(form.getvalue('No_Kids'))
height=int(form.getvalue('height'))
weight=int(form.getvalue('weight'))
term=int(form.getvalue('term'))
sumAssured=int(form.getvalue('sumAssured'))
#newcustomer=np.array([0,20,0,0,8,1,1,99,180,55,3700000])
newcustomer=np.array([No_Kids,Age,maratialStatus,gender,income,edu,smoker,weight,height,term,sumAssured])
newcustomer=newcustomer.reshape(1,-1)
filename = 'decisiontreeFinal.sav'
loaded_model = joblib.load(filename)
Y1=loaded_model.predict(newcustomer)
a=Y1[0][0]
b=Y1[0][1]
if a==1:
    first="Jeevan Kishore"
elif a==2:
    first="Jeevan Anand"
elif a==3:
    first="Jeevan Akshay"
elif a==4:
    first="Jeevan Tarang"
elif a==5:
    first="Money Back Plan"
elif a==6:
    first="Term Plan"
elif a==7:
    first="Endowment Plan"
elif a==8:
    first="Jeevan Saral"
if b==1:
    second="Endowment Plan"
elif b==2:
    second="Money Back Plan"
elif b==3:
    second=""





print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print("<link rel='stylesheet' type='text/css' href='xyz.css'>")

print("<style> body {  font-family: 'Roboto', Helvetica, Arial, sans-serif;  font-weight: 100;  font-size: 12px;  line-height: 30px;  color: #777;  background: #05AA5E;}.container {max-width: 600px;  width: 100%;margin: 0 auto;position: relative;}#contact {background: #F9F9F9;  padding: 25px;margin: 150px 0; box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);}</style>")
print ("</head>")
print ("<body>")
#print("<h2>%s %s</h2>"%(a,b))
#print("<h2>%s</h2>"%(income))
print("<div class='login-form'><div class='container'><div id='contact'>")
print ("<h2>Policies: %s</h2>" % (first))
if a==1:
    print("<h4>The risk commences either after 2 years from the date of commencement of policy or from the policy anniversary immediately following the completion of 7 years of age of child, whichever is later.<br><br>Premiums:Premiums are payable yearly, half-yearly, quarterly or monthly throughout the term of the policy or till earlier death of child, or single premium.<br><br>Bonuses:This is a with-profits plan and participates in the profits of the Corporation’s life insurance business.  It gets a share of the profits in the form of bonuses. Simple Reversionary Bonuses are declared per thousand Sum Assured annually at the end of each financial year.  Once declared, they form part of the guaranteed benefits of the plan. A Final (Additional) Bonus may also be payable provided policy has run for certain minimum period.</h4>")
elif a==2:
    print("<h4>LIC's New Jeevan Anand Plan is a participating non-linked plan which offers an attractive combination of protection and savings. This combination provides financial protection against death throughout the lifetime of the policyholder with the provision of payment of lumpsum at the end of the selected policy term in case of his/her survival. This plan also takes care of liquidity needs through its loan facility.<br><br>Benefits:<br><b>Death benefit :</b>Provided all due premiums have been paid, the following death benefit shall be paid:On Death during the policy term: Death benefit, defined as sum of Sum Assured on Death and vested Simple Reversionary Bonuses and Final Additional bonus, if any, shall be payable. Where, Sum Assured on Death is defined as higher of 125 percent of Basic Sum Assured or 10 times of annualised premium. This death benefit shall not be less than 105 percent of all the premiums paid as on date of death.The premiums mentioned above exclude service tax</h4>")
    print("<h4>Benefits payable at the end of Policy Term:<b> Basic Sum Assured, along with vested Simple Reversionary Bonuses and Final Additional Bonus, if any, shall be payable in lump sum on survival to the end of the policy term provided all due premiums have been paid.</h4>")
elif a==3:
    print("<h4>It is an Immediate Annuity plan, which can be purchased by paying a lump sum amount. The plan provides for annuity payments of a stated amount throughout the life time of the annuitant. Various options are available for the type and mode of payment of annuities.</h4>")
elif a==4:
    print("<h4>This is a with-profits whole of life plan which provides for annual survival benefit at a rate of 5½ % of the Sum Assured after the chosen Accumulation Period. The vested bonuses in a lump sum are payable on survival to the end of the Accumulation Period or on earlier death. Further, the Sum Assured, along with Loyalty Additions, if any, is payable on survival to age 100 years or on earlier death.<h4>")
    print("<h4>Premiums can be paid regularly at yearly, half-yearly, quarterly or monthly intervals or through salary deductions over the Accumulation Period. Alternatively, a Single Premium can be paid on commencement of a policy.</h3>")
elif a==5:
    print("<h4>It is a participating non-linked plan which offers an attractive combination of protection against death throughout the term of the plan along with the periodic payment on survival at specified durations during the term. This unique combination provides financial support for the family of the deceased policyholder any time before maturity and lump sum amount at the time of maturity for the surviving policyholders. This plan also takes care of liquidity needs through its loan facility.<h4>")
    print("<h4>Benefits:<br>Death benefit: On death during the policy term provided the policy is in full force, death benefit, defined as sum of “Sum Assured on Death” and vested Simple Reversionary Bonuses and Final Additional Bonus, if any, shall be payable. Where, “Sum Assured on Death” is defined as higher of 125percent f the Basic Sum Assured or 10 times of annualized premium. This death benefit shall not be less than 105 percent of the total premiums paid as on date of death.The premiums mentioned above exclude tax, extra premium and rider premium, if any.</h4>")
    print("<h4>Survival Benefits: In case of Life Assured surviving to the end of the specified durations 15percent of the Basic Sum Assured at the end of each of 5th, 10th, 15th & 20th policy year.</h4>")
    print("<h4>Maturity Benefit: In case of Life assured surviving the stipulated date of maturity, 40 percent of the Basic Sum Assured along with vested Simple Reversionary Bonuses and Final Additional bonus, if any, shall be payable.</h4>")
    print("<h4>Participation in Profits: The policy shall participate in profits of the Corporation and shall be entitled to receive Simple Reversionary Bonuses declared as per the experience of the Corporation, provided the policy is in full force.</h4>")
elif a==6:
    print("<h4> It is a protection plan which provides financial protection to the insured’s family in case of his/her unfortunate demise.Benefits:Death Benefit: In case of unfortunate death of the Life Assured during the policy term Sum Assured shall be payable.Maturity Benefit: On survival to the end of the policy term, nothing shall be payable.</h4>")
elif a==7:
    print("<h4>There is no limit on the maximum sum assured and the minim sum assured is Rs 1 lakh.The plan comes with tenures ranging from 12 years to 35 years.<br>The premiums can be paid every month, quarter, 6 months or every year.</h4>")
elif a==8:
    print("<h4>The plan provides financial protection against death throughout the term of the plan. The death benefit is directly related to the premiums paid. The Maturity Sum Assured depends on the age at entry of the life to be assured and is payable on survival to the end of the policy term. It also offers the flexibility of term and a lot of liquidity.<br>Premiums:Premiums are payable yearly, half-yearly, quarterly, or monthly through salary deductions as opted by you throughout the term of the policy or till earlier death.Loyalty Additions:This is a with-profits plan and participates in the profits of the Corporation’s life insurance business.  It gets a share of the profits in the form of loyalty additions which are terminal bonuses payable along with death benefit or maturity benefit.  Loyalty Additions may be payable from the 10th year onwards depending upon the experience of the Corporation.</h4>")
print ("<h2> %s</h2>" % (second))
if b==1:
    print("<h3>There is no limit on the maximum sum assured and the minim sum assured is Rs 1 lakh.The plan comes with tenures ranging from 12 years to 35 years.<br>The premiums can be paid every month, quarter, 6 months or every year.</h3>")
elif b==2:
    print("<h4>It is a participating non-linked plan which offers an attractive combination of protection against death throughout the term of the plan along with the periodic payment on survival at specified durations during the term. This unique combination provides financial support for the family of the deceased policyholder any time before maturity and lump sum amount at the time of maturity for the surviving policyholders. This plan also takes care of liquidity needs through its loan facility.<h4>")
    print("<h4>Benefits:<br>Death benefit: On death during the policy term provided the policy is in full force, death benefit, defined as sum of “Sum Assured on Death” and vested Simple Reversionary Bonuses and Final Additional Bonus, if any, shall be payable. Where, “Sum Assured on Death” is defined as higher of 125percent f the Basic Sum Assured or 10 times of annualized premium. This death benefit shall not be less than 105 percent of the total premiums paid as on date of death.The premiums mentioned above exclude tax, extra premium and rider premium, if any.</h4>")
    print("<h4>Survival Benefits: In case of Life Assured surviving to the end of the specified durations 15percent of the Basic Sum Assured at the end of each of 5th, 10th, 15th & 20th policy year.</h4>")
    print("<h4>Maturity Benefit: In case of Life assured surviving the stipulated date of maturity, 40 percent of the Basic Sum Assured along with vested Simple Reversionary Bonuses and Final Additional bonus, if any, shall be payable.</h4>")
    print("<h4>Participation in Profits: The policy shall participate in profits of the Corporation and shall be entitled to receive Simple Reversionary Bonuses declared as per the experience of the Corporation, provided the policy is in full force.</h4>")



print("</div></div></div>")
print ("</body>")
print ("</html>")
