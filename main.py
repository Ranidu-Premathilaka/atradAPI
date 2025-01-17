from dotenv import load_dotenv
from atradAPI import AtradAPI
import os

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

api = AtradAPI(username, password)
api.buy("AAIC.N0000",2,11.2,day=1)

#print(api.getUserInfo())
#print(api.genDuplicateOrderId())
