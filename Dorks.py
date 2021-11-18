import googlesearch
import requests
from urllib.request import urlretrieve
from pathlib import Path
import os
import pandas as pd
import xlsxwriter

#Present working Dir
pwd = os.popen('pwd')
pwd = pwd.read().strip('\n')


# function to create folder within osint for search
def folder_str(a_site):
    try:
        os.makedirs(pwd + '/' + a_site)
    except:
        print('Folder Exists:')


# function will use google dorks
def dorking(a_dork):

    # Search, pause for 20 to minimize too many request errors
    search_results = googlesearch.search(a_dork, num_results=100)
    return search_results


def write_to_excel(the_dork, a_site, file_name, urls):

    # write urls to txt file
    print('...writing pages to file')

    # create excel workbook/worksheet
    workbook = xlsxwriter.Workbook(pwd + '/' + a_site + '/' + file_name + '.xlsx')
    worksheet = workbook.add_worksheet('Hyperlinks')

    # Write Headers to table
    worksheet.write('A1', the_dork)
    worksheet.write('B1', 'Errors')

    # format excel
    green_format = workbook.add_format({
        'bg_color': 'green',
        'bold': 1,
        'underline': 1,
        'font_size': 12,
    })

    red_format = workbook.add_format({
        'bg_color': 'red',
        'bold': 1,
        'underline': 1,
        'font_size': 12,
    })

    # loop through the search results, write urls to excel
    x = 2
    for url_link in urls:

        # Determines http response
        request_data = valid_404(url_link)

        if '200' in str(request_data):
            worksheet.write_url('A' + str(x), url_link, green_format)
        else:
            worksheet.write_url('A' + str(x), url_link, red_format)
            worksheet.write('B' + str(x), request_data)

        x += 1

    workbook.close()


# function to download files
def file_download(your_dork, the_site, a_file):

    try:
        os.makedirs(pwd + '/' + the_site + '/downloads')
    except:
        print('Folder Exists:')

    # to determine filetype
    filetype = input('What is the filetype: ')

    # Read data from excel file
    data = pd.read_excel(pwd + '/' + the_site + '/' + a_file + '.xlsx')

    # Parse url data
    new_data = data[your_dork].tolist()

    # Download files
    for item in new_data:
        url = item
        text = url.replace('/', '')
        new_text = text.replace(':', '')
        dst = pwd + '/' + the_site + '/downloads/' + new_text + '.' + filetype

    # Prints errors if there are issues with downloading file
        try:
            urlretrieve(url, dst)
        except:
            print('error: ' + url)
            with open(pwd + '/' + the_site + '/' + a_file + '.txt', 'a+') as error_file:
                error_file.write(url + '\n')
            continue

    print('Finished')


# function will test for valid HTTP responses
def valid_404(dork_url):
    try:
        data = requests.get(dork_url)
        return data.status_code
    except:
        return 'Some HTTP Error'


dork = input('Enter google search parameters: ')
file_name = input('File name for results: ')
site = input('Target Site: ')

folder_str(site)

dork_results = dorking(dork)

write_to_excel(dork, site, file_name, dork_results)

to_download = input('Do you want to download files discovered? (y:n): ')

if to_download == 'y' or to_download == 'Y':
    file_download(dork, site, file_name)
