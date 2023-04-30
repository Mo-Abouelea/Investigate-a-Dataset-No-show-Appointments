#!/usr/bin/env python
# coding: utf-8

# # Project: No-show Appointments
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# <div style="text-align: justify">
# The aim of this project is to conduct a thorough investigation of a medical appointment dataset collected from 100,000 patients in Brazil. The dataset contains information on various characteristics of patients, including age, gender, and neighborhood, as well as whether or not they showed up for their scheduled appointment. The primary focus of this project is to answer the question of whether there is a relationship between these patient characteristics and the likelihood of them attending their appointment. Through careful analysis and interpretation of the data, we aim to gain insights into the factors that may influence patient attendance and inform strategies for improving appointment adherence in the future.
# </div>
# 
# ### Question(s) for Analysis
# 
# This question group set ilustrates the relationships between several variables that affect the patient to make it to his appiontment by looking at how two independent variables relate to a single dependent variable:
# 
# * How does gender affects the number of patients attended and did not attended the appointment?
# 
# * How does age affects the number of patients attended and did not attended the appointment?
# 
# * How does the Scholarship affects the number of patients attended and did not attended the appointment?
# 
# * How does received SMS affects the number of patients attended and did not attended the appointment?
# 
# * How does gender affects the number of patients attended and did not attended the appointment compared with age ?
# 

# In[1]:


# Here are the import statements for all of the packages needed in the project.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Upgrade pandas to use dataframe.explode() function.
get_ipython().system('pip install --upgrade pandas==0.25.1')


# In[3]:


get_ipython().system('pip install -U seaborn')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# ### General Properties
# 

# In[4]:


# Load the data and print out a few lines. 
df = pd.read_csv('noshowappointments-kagglev2-may-2016.csv')
df.head()


# In[5]:


# Performing operations to inspect data types and look for instances of missing or possibly errant data.
df.info()


# In[6]:


# show a quick descriptive data summary
df.describe()


# 
# ### Data Cleaning

# In[7]:


# check for duplicates
df.duplicated().sum()


# In[8]:


# check the number of unique patients
df.PatientId.nunique()


# In[9]:


# Replace negative values for age with a zero value
df['Age'].replace({-1: 0}, inplace=True)


# In[10]:


# Convert appointment statues datatype from object to boolean
df['No-show'].replace({'No': 0, 'Yes': 1}, inplace=True)
df['No-show'] = df['No-show'].astype('bool')


# In[11]:


df.rename(columns={'No-show':'No_show'},inplace=True)


# In[12]:


# show a descriptive data summary after data cleaning
df.describe()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 

# In[13]:


# Quick exploratory to see patient attendance
pt_attendance = df.No_show.value_counts()
labels = ['Show', 'No_Show']
plt.pie(pt_attendance , labels = labels, autopct= '%1.1f%%');
plt.title("Number of Patients : Attendance Statues");
plt.legend();
plt.show();


# <hr />
# The analysis shows that around 20% of the patients did not show up for their appointments. Therefore, we need to examine the given parameters more closely to investigate the reason for this.
# <hr />

# ### Single Variable Questionnaire
# 
# #### How does gender affects the number of patients attended and did not attend the appointment?

# In[14]:


# Define a function "analyze" that plots the statues of a specific character for all patients from the dataset. 
def analyze(f,t,x,y,a,b):
    sns.set_theme(style="whitegrid")
    sns.countplot(x=df[f])
    plt.title(t)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xticks([0, 1],[a,b])
    plt.show();


# In[15]:


# Patients "Gender" analysis.
analyze("Gender","Number of Male and Female Patients","Patients Gender","Number of Patients",'Female','Male')


# In[16]:


# Patients "Gender" analysis with respect to attendance.
sns.set_theme(style="whitegrid")
sns.countplot(data=df, x="Gender", hue="No_show")
plt.legend(["Show", "No_Show"]);
plt.title('Gender : Attendance Analysis')
plt.xlabel('Gender')
plt.ylabel('Patients Number')
plt.show();


# In[17]:


#Patients "Gender" analysis comparison
df.groupby('Gender').No_show.value_counts()


# <hr />
# The investigation found that more females than males attended the appointment, indicating that females place a higher importance on their health.
# <hr />

# #### How does age affects the number of patients attended and did not attend the appointment?

# In[18]:


# Patients "Age" analysis
sns.set_theme(style="whitegrid")
plt.figure(figsize=[15,5])
sns.histplot(data = df, x = 'Age')
plt.title("Patients Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.show();


# In[19]:


# Patients "Age" analysis with respect to attendance.
sns.set_theme(style="whitegrid")
plt.figure(figsize=[15,5])
sns.histplot(data = df, x = 'Age', hue="No_show")
plt.legend(["No_show", "Show"]);
plt.title("Age : Attendance Analysis")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.show();


# <hr />
# The majority of the attended patients belong to the adult and middle-aged categories. where as children and elders are less likely to attended. this could be due to less medical experties are provided for these to categories.
# <hr />

# #### How does the Scholarship affects the number of patients attended and did not attend the appointment?

# In[20]:


# Patients "Scholarship" analysis.
analyze("Scholarship","Number of Patients with Scholarship","Scholarship Statues",
        "Number of Patients",'Not_Enrolled','Enrolled')


# In[21]:


# Patients "Scholarship" analysis with respect to attendance.
sns.set_theme(style="whitegrid")
sns.countplot(data=df, x="Scholarship", hue="No_show")
plt.legend(["Show", "No_Show"]);
plt.title("Scholarship : Attendance Analysis")
plt.xlabel("Scholarship")
plt.ylabel("Number of Patients")
plt.xticks([0, 1],['Not_Enrolled','Enrolled'])
plt.show();


# In[22]:


#Patients "Scholarship" analysis comparison
df.groupby('Scholarship').No_show.value_counts()


# <hr />
# Out of all the patients, 10861 do not have a scholarship. This suggests that further investigation may not be very informative in this case, as almost all patients share this characteristic. However, it is still worth examining how the scholarship affects attendance.
# <hr />

# #### How does received SMS affects the number of patients attended and did not attend the appointment?

# In[23]:


# Patients "Received SMS" analysis.
analyze("SMS_received","Number of Patients who received SMS","SMS_Received Statues",
        "Number of Patients",'Not_Received','Received')


# In[24]:


# Patients "SMS_Received" analysis with respect to attendance.
sns.set_theme(style="whitegrid")
sns.countplot(data=df, x="SMS_received", hue="No_show")
plt.legend(["Show", "No_Show"]);
plt.title("SMS_Received : Attendance Analysis")
plt.xlabel("SMS_Received")
plt.ylabel("Number of Patients")
plt.xticks([0, 1],['Not_Received','Received'])
plt.show();


# In[25]:


#Patients "SMS_received" analysis comparison
df.groupby('SMS_received').No_show.value_counts()


# <hr />
# The investigation found that receiving a SMS reminder reduces the no-show rate, as appointments with a reminder had a lower rate of no-shows than those without.
# <hr />

# <a id='conclusions'></a>
# ## Conclusions
# 
# According to the dataset, the investigation has taken a closer look at four key areas of interest, including Gender, Age, SMS received, and Scholarship. The objective of the analysis is to identify which of these characteristics have the greatest impact on patient attendance, in order to enhance the medical appointment system.
# 
# * The investigation indicates that there are more females than males, and the analysis reveals that a greater proportion of females attended the appointment compared to males, demonstrating that females place a greater emphasis on taking care of their health.
# 
# * The investigation indicated that receiving an SMS reminder has a positive impact on the no-show rate, as appointments with a reminder have a lower rate of no-shows compared to those without a reminder.
# 
# * Patient age investigation shows that the number of attendace didnt increase by age, where the majorty of the attended patients lies in the both classs of adults and middle aged that varies from 19 to 64 according to the national institute of health classification. A further investigation should be implemented in order to justify why elders are less frequent to show up in their appointments.
# 
# ### Limitations
# 
# The enrollment status in the scholarship program appears to have minimal significance, as the number of patients who have attended and not enrolled is significantly higher than those who are enrolled, with a ratio of 79925 to 8283. As a result, this characteristic can be disregarded in further investigations.
# 
#  
# A deeper examination can be carried out by utilizing other features as the medical record and location, which would provide valuable insight of patient attendance statues.
# 

# In[27]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




