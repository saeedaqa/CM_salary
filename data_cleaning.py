# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:27:06 2020

@author: Ken
"""

import pandas as pd 

df = pd.read_csv('glassdoor_cms.csv').dropna()



df['Salary Estimate']=df['Salary Estimate'].astype(str)
df = df[df['Salary Estimate'] != '-1']
#salary parsing 
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if ('per hour') in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)



salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.lower().replace('k','').replace('ca$',''))
min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))



df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2

#Company name text only
df['Company Name']=df['Company Name'].astype(str)
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)


#age of company 
df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020 - x)

#parsing of job description (PMP, etc.)

#PMP
df['pmp_yn'] = df['Job Description'].apply(lambda x: 1 if 'pmp' in x.lower() else 0)
df.pmp_yn.value_counts()
 
#Agile
df['agile_yn'] = df['Job Description'].apply(lambda x: 1 if 'agile' in x.lower() or 'scrum' in x.lower() else 0)
df.agile_yn.value_counts()

#Excel 
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

#primavera 
df['primavera'] = df['Job Description'].apply(lambda x: 1 if 'primavera' in x.lower() or 'p6' in x.lower() else 0)
df.primavera.value_counts()

df.columns
#cleaning_title

import title
    
df['job_simp'] = title.title_simplifier('Job Title')
df['seniority'] = title.seniority('Job Title')
df.job_simp.value_counts()






df.to_csv('salary_data_cleaned.csv',index = False)

