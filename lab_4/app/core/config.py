from os import getenv
from dotenv import load_dotenv

from app.core.saving_place_type import SavingPlaceType

load_dotenv()

DATA_SOURCE = getenv('DATA_SOURCE')
DATA_FILE_CSV = getenv('DATA_FILE_CSV')
SAVING_PLACE = getenv('SAVING_PLACE')
