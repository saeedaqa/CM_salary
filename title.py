#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:54:23 2020

@author: shaki
"""
def title_simplifier(title):
    if 'construction manager' in title.lower():
        return 'construction manager'
    elif 'project manager' in title.lower():
        return 'porject manager'
    elif 'construction manager' and 'project' in title.lower():
        return 'construction manager'
    elif 'project coordinator' in title.lower():
        return 'project coordinator'
    elif 'internship' in title.lower():
        return 'internship'
    elif 'superintendent' in title.lower():
        return 'construction manager'
    else:
        return 'na'
    
def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
            return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower():
        return 'jr'
    else:
        return 'na'

