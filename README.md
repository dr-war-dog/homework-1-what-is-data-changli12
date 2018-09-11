
# Homework01

#### Question 1: What is the average/mean score of the LA County Resturant Inspections?


```python
import pandas as pd

df=pd.DataFrame.from_csv("data/la-county-restaurant-inspections.csv")
score_mean=df['score'].mean()

print("The average/mean score of the LA County Resturant Inspections is "+str(score_mean)+".")
```

The average/mean score of the LA County Resturant Inspections is 93.75330640483668.<br/>
The type of data is countinuous data.

#### Question 2: How many times was facility address 17660 CHATSWORTH ST visited?


```python
import pandas as pd

df=pd.DataFrame.from_csv("data/la-county-restaurant-inspections.csv")
count=0
for index,row in df.iterrows():
    if row['facility_address']=='17660 CHATSWORTH ST':
        count+=1
        
print("Facility address 17660 CHATSWORTH ST was visited "+str(count)+" times.")
```

Facility address 17660 CHATSWORTH ST was visited 6 times.<br/>
The type of data is categorical data.

#### Question 3: How many times was facility city LANCASTER visited?


```python
import pandas as pd

df=pd.DataFrame.from_csv("data/la-county-restaurant-inspections.csv")
count=0
for index,row in df.iterrows():
    if row['facility_city']=='LANCASTER':
        count+=1
        
print("Facility city LANCASTER was visited "+str(count)+" times.")
```

Facility city LANCASTER was visited 2371 times.<br/>
The type of data is categorical data.

#### Question 4: What percentage of times did employee EE0000145 visit any facility?


```python
import pandas as pd

df=pd.DataFrame.from_csv("data/la-county-restaurant-inspections.csv")
count=0
em_count=0
for index,row in df.iterrows():
    count+=1
    if row['employee_id']=='EE0000145':
        em_count+=1

print("The percentage of times that employee EE0000145 visited facility is "+str((em_count/count)*100)+"%.")
```

The percentage of times that employee EE0000145 visited facility is 0.5800251866792774%.<br/>
The type of data is categorical data.

#### Question 5: What percentage of times was facility FA0013858 visited?


```python
import pandas as pd

df=pd.DataFrame.from_csv("data/la-county-restaurant-inspections.csv")
count=0
fa_count=0
for index,row in df.iterrows():
    count+=1
    if row['facility_id']=='FA0013858':
        fa_count+=1

print("The percentage of times that facility FA0013858 was visited is "+str((fa_count/count)*100)+"%.")
```

The percentage of times that facility FA0013858 was visited is 0.00992835905126691%.<br/>
The type of data is categorical data.

#### Question 6: What percentage of times did employee EE0000593 visit GRANADA HILLS?


```python
import pandas as pd

df=pd.DataFrame.from_csv("data/la-county-restaurant-inspections.csv")
count=0
gr_count=0
for index,row in df.iterrows():
    count+=1
    if row['employee_id']=='EE0000593'and row['facility_city']=='GRANADA HILLS':
        gr_count+=1

print("The percentage of times that employee EE0000593 visited GRANADA HILLS is "+str((gr_count/count)*100)+"%.")
```

The percentage of times that employee EE0000593 visited GRANADA HILLS is 0.2591824257593888%.<br/>
The type of data is categorical data.
