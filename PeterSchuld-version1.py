import csv
costcoFile=open('costco-citi-visa-due-soon - bob copy - sorted - with categories.csv')
costcoReader=csv.reader(costcoFile)
costcoData=list(costcoReader)
n=(len(costcoData))
amountfloat=0
total=0
entertainment=0
food=0
household=0
pet=0
petMedical=0
kid=0
kidMedical=0
travel=0
utilities=0
gift=0
charity=0
findDetail=0
ignore=0
fixedInsurance=0


for i in range(n-1):
    category=costcoData[i+1][5]
    amount=costcoData[i+1][1].strip('$()')
    amountfloat=float(amount.replace(',',''))
    
    if '(' in costcoData[i+1][1]:amountfloat=amountfloat*-1
    if category=='entertainment':entertainment=entertainment+amountfloat
    if category=='food':food=food+amountfloat
    if category=='household':household=household+amountfloat
    if category=='pet':pet=pet+amountfloat
    if category=='pet-medical':petMedical=petMedical+amountfloat
    if category=='kid':kid=kid+amountfloat
    if category=='kid-medical':kidMedical=kidMedical+amountfloat
    if category=='travel':travel=travel+amountfloat
    if category=='utilities':utilities=utilities+amountfloat
    if category=='gift':gift=gift+amountfloat
    if category=='charity':charity=charity+amountfloat
    if category=='find-detail':findDetail=findDetail+amountfloat
    if category=='ignore':ignore=ignore+amountfloat
    if category=='fixed-insurance':fixedInsurance=fixedInsurance+amountfloat
    
    
outputFile=open('output.version-1.budget-monthly-totals-and-tracking.csv','w')
outputWriter=csv.writer(outputFile)
outputWriter.writerow(['Which Card?','Month','entertainment','food','household','pet','pet-medical','kid','kid-medical','travel','utilities','gift','charity','find-detail','ignore','fixed-insurance'])
outputWriter.writerow(['Costco Visa','March 2017',str(entertainment),str(food),str(household),str(pet),str(petMedical),str(kid),str(kidMedical),str(travel),str(utilities),str(gift),str(charity),str(findDetail),str(ignore),str(fixedInsurance)])
outputFile.close()
                      
print("'budget-monthly-totals-and-tracking.csv' file was created !'")

