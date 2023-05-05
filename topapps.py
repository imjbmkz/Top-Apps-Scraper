import requests
import json
from bs4 import BeautifulSoup
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load JSON configuration file as dictionary
with open("config.json", "r") as fp:
    config = json.load(fp)

# Constants
DESTINATION_SHEET_ID = config["DESTINATION_SHEET_ID"]
DESTINATION_RANGE = config["DESTINATION_RANGE"]
SERVICE_ACCOUNT_FILE = config["SERVICE_ACCOUNT_FILE"]
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

url = "https://topapps.ai/"

# Send a request to the website and get the HTML content
response = requests.get(url)

# Use Beautiful Soup to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the links on the website with the class name "jet-listing-dynamic-link__link"
links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        if href.startswith('https://topapps.ai/'):
            links.append([href])

# Creating credentials object and building Google Sheets API
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the Sheets API client
service = build("sheets", "v4", credentials=credentials)

body = {"values": links}
result = service.spreadsheets().values().append(
    spreadsheetId=DESTINATION_SHEET_ID,
    range=DESTINATION_RANGE,
    valueInputOption="USER_ENTERED",
    body=body
).execute()
    
print(result["updates"]["updatedCells"], "records have been added.")