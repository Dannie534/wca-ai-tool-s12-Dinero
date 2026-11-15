import json
import os
import glob
from datetime import datetime
from dotenv import load_dotenv
from anthropic import Anthropic

# --- Load API Key ---
load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    print("❌ ERROR: ANTHROPIC_API_KEY not found in .env file.")
    print("Create a file called .env and add: ANTHROPIC_API_KEY=sk-ant-...")
    exit()

client = Anthropic(api_key=API_KEY)

# --- Constants / Files ---
DATA_FILE = "dinero_data.json"          # Persistent members + payments
SESSIONS_DIR = "sessions"               # Folder for saved conversations
TARGET = 1000                          # Target per member per month in KES
MODEL = "claude-haiku-5-5"             # Fast, cheap, best for summaries