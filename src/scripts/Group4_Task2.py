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


def main():
    #Casualty_Age_Casualty_Sex()
    #Accident_Light_Casualty_Sex()


if __name__ == "__main__":
    main()