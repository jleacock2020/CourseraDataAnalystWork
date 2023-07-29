#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2023-01-01">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **JOBS API Implementation Using FLASK**
# 
# 

# Estimated time needed: **45 to 60** minutes
# 

# ## Objectives
# 
# You will be executing this code  so that the client application **Collecting Jobs API**  will be accessing this code executing on the server 
# 

# In[1]:


get_ipython().system('pip install flask')


# ## Dataset Used in this Assignment
# 
# The dataset used in this lab comes from the following source: https://www.kaggle.com/promptcloud/jobs-on-naukricom under the under a **Public Domain license**.
# 
# > Note: We are using a modified subset of that dataset for the lab, so to follow the lab instructions successfully please use the dataset provided with the lab, rather than the dataset from the original source.
# 
# The original dataset is a csv. We have converted the csv to json as per the requirement of the lab.
# 

# In[2]:


get_ipython().system('wget  https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json')


# In[ ]:


import flask
from flask import request, jsonify
import requests
import re

def get_data(key,value,current):
    results = list()
    pattern_dict = {
        'C'      : '(C)',
        'C++'    : '(C\+\+)',
        'Java'   :'(Java)',
        'C#'     : '(C\#)',
        'Python' :'(Python)',
        'Scala' : '(Scala)',
        'Oracle' : '(Oracle)',
        'SQL Server': '(SQL Server)',
        'MySQL Server' :'(MySQL Server)',
        'PostgreSQL':'(PostgreSQL)',
        'MongoDB'    : '(MongoDB)',
        'JavaScript'    : '(JavaScript)',
        'Los Angeles' :'(Los Angeles)',
        'New York':'(New York)',
        'San Francisco':'(San Francisco)',
        'Washington DC':'(Washington DC)',
        'Seattle':'(Seattle)',
        'Austin':'(Austin)',
        'Detroit':'(Detroit)',
        
        
        
        
        
    }
    for rec in current:
        print(rec[key])
        print(type(rec[key]))
        print(rec[key].find(value))
        #if rec[key].find(value) != -1:
        import re
        #reex_str = """(C)|(C\+\+)|(JavaScript)|(Java)|(C\#)|(Python)|(Scala)|(Oracle)|(SQL Server)|(MySQL Server)|(PostgreSQL)|(MongoDB)"""
        if re.search(pattern_dict[value],rec[key]) != None:
            results.append(rec)
    return results

app = flask.Flask(__name__)

import json
data = None
with open('jobs.json',encoding='utf-8') as f:
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    

@app.route('/', methods=['GET'])
def home():
    
    return '''<h1>Welcome to flask JOB search API</p>'''


@app.route('/data/all', methods=['GET'])
def api_all():
    return jsonify(data)


@app.route('/data', methods=['GET'])
def api_id():
    # Check if keys such as Job Title,KeySkills, Role Category and others  are provided as part of the URL.
    #  Assign the keys to the corresponding variables..
    # If no key is provided, display an error in the browser.
    res = None
    for req in request.args:
        
        if req == 'Job Title':
            key = 'Job Title'
        elif req == 'Job Experience Required' :
            key='Job Experience Required'
        elif req == 'Key Skills' :
            key='Key Skills'
            
        elif req == 'Role Category' :
            key='Role Category'
        elif req == 'Location' :
            key='Location'
        
        elif req == 'Functional Area' :
            key='Functional Area'
        
        elif req == 'Industry' :
            key='Industry'
        elif req == 'Role' :
            key='Role'
        elif req=="id":
             key="id"
        else:
            pass
    
        value = request.args[key]
        if (res==None):
            res = get_data(key,value,data)
        else:
            res = get_data(key,value,res)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(res)

app.run()


# ## Authors
# 

# Lakshmi Holla  
# 

# ### Other Contributors
# 

# Malika Singla  
# Ayushi Jain
# 

# ## Changelog
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
# | ----------------- | ------- | ----------------- | ---------------------------------- |
# | 2022-01-03        | 0.1     | Lakshmi Holla  | Created Initial Version
# 

# Copyright © 2022 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2021-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
