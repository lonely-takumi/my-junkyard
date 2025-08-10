import os
from dotenv import load_dotenv

def load_env():
  dotenvPath = os.path.join(os.path.dirname(__file__), '.env')
  load_dotenv(dotenvPath)
  print(f"Environment variables loaded from {dotenvPath}")