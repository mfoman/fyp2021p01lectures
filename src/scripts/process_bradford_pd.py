# === Imports
from pathlib import Path
import pandas as pd


# === Set Constants
PATH = {
    'raw': Path('./data/raw/'),
    'processed': Path('./data/processed/'),
    'interim': Path('./data/interim/'),
}

PATH['accidents'] = PATH['raw'] / "Road Safety Data - Accidents 2019.csv"
PATH['casualties'] = PATH['raw'] / "Road Safety Data - Casualties 2019.csv"
PATH['vehicles'] = PATH['raw'] / "Road Safety Data - Vehicles 2019.csv"


# === Read the data
DATA = {}

DATA['accidents'] = pd.read_csv(PATH['accidents'], dtype={0: 'string', 31: 'string'}, encoding='utf-8-sig')

DATA['casualties'] = pd.read_csv(PATH['casualties'], dtype={0: 'string'}, encoding='utf-8-sig')

DATA['vehicles'] = pd.read_csv(PATH['vehicles'], dtype={0: 'string'}, encoding='utf-8-sig')


# === Process it
# Get all bradford accidents as we know they're in local district 200
DATA['brad_accidents'] = DATA['accidents'][DATA['accidents']['Local_Authority_(District)'] == 200]


# Get the accident indexes from brad_accident
accident_index = DATA['brad_accidents']['Accident_Index']


# Use the index to find all matching rows in casualties and vehicles
brad_cass_mask = DATA['casualties']['Accident_Index'].isin(accident_index)
brad_vehi_mask = DATA['vehicles']['Accident_Index'].isin(accident_index)

DATA['brad_casualties'] = DATA['casualties'][brad_cass_mask]
DATA['brad_vehicles'] = DATA['vehicles'][brad_vehi_mask]


# === Save it
DATA['brad_accident'].to_csv(PATH['interim'] / 'bradford_accidents.csv')
DATA['brad_casualties'].to_csv(PATH['interim'] / 'bradford_casualties.csv')
DATA['brad_vehicles'].to_csv(PATH['interim'] / 'bradford_vehicles.csv')
