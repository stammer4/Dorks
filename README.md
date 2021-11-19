# Dorks
This script will allow you to run your google dorks within the CLI of your machine and place the links in an excel sheet for you to browse. In the Excel sheet, It will display which links return a 200 response -- so you're not wasting time going to non-existant links.

# Notes
-Currently limited to 100 results per search. <br>
-The script is only looking for 200 responses from sites, so sometimes a link that displayed as red in the excel will still return a valid page. <br>
-There is a way to create a search tool by using Google's API (after receving an API-Key), but it's very limited in free results. I found more success using the googlesearch module. <br> 
-I'm planning on making a few small changes to the script in the future, I want to expand on the results displayed in the excel sheet. 

# Python Modules
import googlesearch <br>
import requests <br>
from urllib.request import urlretrieve <br>
from pathlib import Path <br>
import os <br>
import pandas as pd <br>
import xlsxwriter <br>

<p>
  To install one of the above modules if you do not have it: (example) <br>
  python3 -m pip install googlesearch-python

# gnumeric
<b>To read the excel file in linux, ensure gnumeric is installed. </b> <br>
apt-get install gnumeric 
