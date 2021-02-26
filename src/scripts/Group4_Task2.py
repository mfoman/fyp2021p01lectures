#Group4_Task2.py
#Two-Variable Analysis
#By Daniel

import pandas as pd

#Read Files
Accidents = pd.read_csv("../../data/interim/bradford_accidents.csv")
Casualties = pd.read_csv("../../data/interim/bradford_casualties.csv")
Vehicles = pd.read_csv("../../data/interim/bradford_vehicles.csv")

#Merge dataframes such that if there's multiple Casualties/Vehicles for individual accident_index values, 
    #...it duplicates the corresponding rows by accident_index in the Accidents dataframe.
Accidents_Casualties = pd.merge(Accidents, Casualties, how="inner", on=["Accident_Index", "Accident_Index"])
Accidents_Vehicles = pd.merge(Accidents, Vehicles, how="inner", on=["Accident_Index", "Accident_Index"])


def Casualty_Age_Casualty_Sex():
    #Create dataframes for data isolated to males/females.
    data_male = Accidents_Casualties[Accidents_Casualties["Sex_of_Casualty"] == 1]
    data_female = Accidents_Casualties[Accidents_Casualties["Sex_of_Casualty"] == 2]
    
    #Statistical analysis on the median ages of the male/female casualties. (Casualty-variable/Casualty-variable analysis)
    Age_m_mean = data_male["Age_of_Casualty"].describe().loc["50%"]
    Age_f_mean = data_female["Age_of_Casualty"].describe().loc["50%"]


def Accident_Light_Casualty_Sex():
    #label/code for Light Conditions
    light_key = [["data_daylight",1],["data_l_lit",4],["data_l_unlit",5],["data_l_none",6],["data_l_unknown",7],["data_missing",-1]]
    
    #Create dataframes for data isolated to light conditions.
    Light_dict = {}
    for light in light_key:
        Light_dict[light[0]] = Accidents_Casualties[Accidents_Casualties["Light_Conditions"] == light[1]]
    
    #Statistical analysis on the median ages depending on the light conditions of the accidents. (Accident-variable/Casualty-variable analysis)
    Age_Light_dict = {}
    for light in Light_dict:
        df = Light_dict[light]
        Age_Light_dict["Age_"+light] = df["Age_of_Casualty"].describe().loc["50%"]

import numpy as np
import scipy.stats as stats
from scipy.stats import chi2_contingency

def Analysis():
    mask = (Accidents_Casualties["Speed_limit"] != -1)
    severity_speed = np.array([Accidents_Casualties["Speed_limit"][mask], Accidents_Casualties["Accident_Severity"][mask]]).T
    
    severity_speed_pd = pd.crosstab(severity_speed[:, 0], severity_speed[:, 1], rownames = ["Speed limit"], colnames = ["Accident Severity"]) 
    severity_speed = severity_speed_pd.to_numpy()
    
    chiVal, pVal, df, expected = chi2_contingency(severity_speed)
    print(chiVal)
    print(pVal)
    print(df)
    print(expected)
    
    rowTotals = severity_speed.sum(axis = 1)
    N = rowTotals.sum()
    V = np.sqrt((chiVal/N) / (min(severity_speed.shape)-1))
    print(V)


def main():
    #Casualty_Age_Casualty_Sex()
    #Accident_Light_Casualty_Sex()
    #Analysis()


if __name__ == "__main__":
    main()