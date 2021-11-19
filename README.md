# Dorks
This script will allow you to run your google dorks within the CLI of your machine and place the links in an excel sheet for you to browse. In the Excel sheet, It will display which links return a 200 response -- so you're not wasting time going to non-existant links.

# Notes
-Currently limited to 100 results per search. <br>
-The script is only looking for 200 responses from sites, so sometimes a link that displayed as red in the excel will still return a valid page. <br>
-There is a way to create a search tool by using Google's API (after receving an API-Key), but it's very limited in free results. I found more success using the googlesearch module. 

# Python Module
import googlesearch
import requests
from urllib.request import urlretrieve
from pathlib import Path
import os
import pandas as pd
import xlsxwriter

<p>
  To install one of the above modules type: (example) <br>
  python3 -m pip install googlesearch-python


<b>To read the excel file in linux, ensure gnumeric is installed. </b> <br>
apt-get install gnumeric 
