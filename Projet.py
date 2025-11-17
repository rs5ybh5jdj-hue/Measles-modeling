# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
### DATASETS ###
# ---------------------------------------------------------------------------

## Reported cases of measles
# World Health Organization
reported_cases_WHO = pd.read_csv("C:/Users/Joséphine/OneDrive - UCL/Master 1/Process modelling/Projet - measles/Measles reported cases WHO.csv", encoding='utf-8', sep=";")
print(reported_cases_WHO.head())

# Our World in Data
reported_cases_OWID = pd.read_csv("C:/Users/Joséphine/OneDrive - UCL/Master 1/Process modelling/Projet - measles/reported-cases-of-measles OWD.csv")

cases_OWID = reported_cases_OWID.drop(columns = ['Entity','Code'], axis=1) # "axis=1" = columns
print(cases_OWID.head())

## Vaccination
# World Health Organization
vaccin = pd.read_csv("C:/Users/Joséphine/OneDrive - UCL/Master 1/Process modelling/Projet - measles/Measles vaccination coverage WHO.csv", sep=";")
print(vaccin)

columns_to_drop = ['GROUP', 'CODE', 'NAME', 'ANTIGEN_DESCRIPTION', 'COVERAGE_CATEGORY', 'COVERAGE_CATEGORY_DESCRIPTION']

vaccin_cleaned = vaccin.drop(columns=columns_to_drop, axis=1)

mcv1 = vaccin_cleaned[vaccin_cleaned['ANTIGEN'] == 'MCV1']
print(mcv1.head())

mcv2 = vaccin_cleaned[vaccin_cleaned['ANTIGEN'] == 'MCV2']
print(mcv2.head())

# ---------------------------------------------------------------------------
### PARAMETERS ###
# ---------------------------------------------------------------------------
 
# Average period of time after which they succumb to the infection
gamma = 1/12
 
