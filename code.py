import pandas as pd

df=pd.DataFrame.from_csv("data/la-county-restaurant-inspections.csv")

#Question 1

score_mean=df['score'].mean()

print("The average/mean score of the LA County Resturant Inspections is "+str(score_mean)+".")

#Question 2

count = 0
for index, row in df.iterrows():
    if row['facility_address'] == '17660 CHATSWORTH ST':
        count += 1

print("Facility address 17660 CHATSWORTH ST was visited " + str(count) + " times.")

#Question 3

count = 0
for index, row in df.iterrows():
    if row['facility_city'] == 'LANCASTER':
        count += 1

print("Facility city LANCASTER was visited " + str(count) + " times.")

#Question 4

count=0
em_count=0
for index,row in df.iterrows():
    count+=1
    if row['employee_id']=='EE0000145':
        em_count+=1

print("The percentage of times that employee EE0000145 visited facility is "+str((em_count/count)*100)+"%.")

#Question5

count=0
fa_count=0
for index,row in df.iterrows():
    count+=1
    if row['facility_id']=='FA0013858':
        fa_count+=1

print("The percentage of times that facility FA0013858 was visited is "+str((fa_count/count)*100)+"%.")

#Question 6

count=0
gr_count=0
for index,row in df.iterrows():
    count+=1
    if row['employee_id']=='EE0000593'and row['facility_city']=='GRANADA HILLS':
        gr_count+=1

print("The percentage of times that employee EE0000593 visited GRANADA HILLS is "+str((gr_count/count)*100)+"%")