#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:44:38 2020

@author: shaki
"""


import glassdoor_scraper as gs
import pandas as pd
path="/Users/shaki/Documents/my_projects/CM_salary/chromedriver"

df=gs.get_jobs('construction manager', 2000, False, path, 15)
df.to_csv('glassdoor_cms.csv', index= False)