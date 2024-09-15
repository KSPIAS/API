import os
import pandas as pd
import json
from googletrans import Translator
from weatherstack.models import api_location

def get_city():
    city = "Pathum Thani"
    return city

def wind_dir_to_th(wind_dir):
    if wind_dir == "N":
        return "ทิศเหนือ"
    elif wind_dir == "NE":
        return "ทิศตะวันออกเฉียงเหนือ"
    elif wind_dir == "E":
        return "ทิศตะวันออก"
    elif wind_dir == "SE":
        return "ทิศตะวันออกเฉียงใต้"
    elif wind_dir == "S":
        return "ทิศใต้"
    elif wind_dir == "SW":
        return "ทิศตะวันตกเฉียงใต้"
    elif wind_dir == "W":
        return "ทิศตะวันตก"
    elif wind_dir == "NW":
        return "ทิศตะวันตกเฉียงเหนือ"
    elif wind_dir == "SSW":
        return "ทิศใต้-ตะวันตกเฉียงใต้"
    elif wind_dir == "ESE":
        return "ทิศตะวันออกเฉียงใต้"
    else:
        return f"{wind_dir}"

def trans_to_th(text):
    translator = Translator()
    try:
        translated = translator.translate(text, src='en', dest='th')
        return translated.text
    except Exception as e:
        print(f"An error occurred: {e}")

######################### Read/Write CSV #######################
def w_csv():
    all_fields = [field.name for field in api_location._meta.get_fields()]
    # print("all_fields" ,all_fields)
    data_location = api_location.objects.all()
    data_list = list(data_location.values(*all_fields))
    # print("Data List:", data_list)
    df = pd.DataFrame(data_list)
    # print(df)
    directory = "weatherstack/csv"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, "api_location.csv")
    try:
        df.to_csv(file_path ,index=False)
        print(f"DataFrame successfully saved to '{file_path}'.")
    except PermissionError:
        print(f"Permission denied. The file '{file_path}' may be open or in use.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def r_csv():
    try:
        directory = "weatherstack/csv"
        file_path = os.path.join(directory, "api_location.csv")
        df = pd.read_csv(file_path ,dtype=str)
        print(df)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
################################################################

########################### Read JSON ##########################
def read_file_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
################################################################