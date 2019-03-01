from dotenv import load_dotenv  # to use .env
import os  # read from os

class Config:
    """ config class for environment dependencies """

    env_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(env_path,verbose=True) 
    MAP_LOCATION_X = float(os.environ.get("MAP_LOCATION_X"))
    MAP_LOCATION_Y = float(os.environ.get("MAP_LOCATION_Y"))
    