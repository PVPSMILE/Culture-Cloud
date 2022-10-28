import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3 
import random

low_case = list('qwertyuiopasdfghjklzxcvbnm')
high_case = list('QWERTYUIOPASDFGHJKLZXCVBNM')
number_case = list('1234567890')

path_to_driver = os.path.join(os.path.abspath(__file__+'/..'),'chromedriver.exe')
driver = webdriver.Chrome(path_to_driver) 
driver.maximize_window()
driver.implicitly_wait(1)
list_url = []
delay = 10

with open('uri_films.txt','r') as file:
    list_url = file.read().split(',')

domen_name = 'https://www.imdb.com/title/'

dict_xpaths = {
                
                'NAME':'//div[@class="sc-dae4a1bc-0 gwBsXc"]',
                'AUTHOR':'//ul[@class="ipc-metadata-list ipc-metadata-list--dividers-all sc-18baf029-10 jIsryf ipc-metadata-list--base"]/li[2]',
                'RAITING':'//span[@class="sc-7ab21ed2-1 jGRxWM"]',
                'IMAGE':'//div[@class="ipc-poster ipc-poster--baseAlt ipc-poster--dynamic-width sc-aae05e05-0 fBcbjp celwidget ipc-sub-grid-item ipc-sub-grid-item--span-2"]/a',
                'DESCRIPTION':'//div[@class="ipc-overflowText ipc-overflowText--pageSection ipc-overflowText--height-long ipc-overflowText--long ipc-overflowText--base"]',
                'DATE':'//li[@data-testid="title-details-releasedate"]//div[@class="ipc-metadata-list-item__content-container"]', 
                'COUNT_RAITING':'//div[@class="sc-7ab21ed2-3 dPVcnq"]',
                'SEARCH_ID':'',         
}
dict_db = {}


def pars_func():
    for url in list_url:
        dict_elements = {}
        url = domen_name+url
        site = driver.get(url)
        try:
            WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, '//a[@class="link-gray"]')))
        except TimeoutException:
            print('Вау, здесь была ошибка')
        for key in dict_xpaths.keys():
            if key == 'SEARCH_ID':
                for i in range(20):
                    list_cases = [high_case,low_case,number_case]
                    random.shuffle(list_cases)
                    list_choice = random.choice(list_cases)
                    random.shuffle(list_choice)
                    dict_xpaths['SEARCH_ID'] += random.choice(list_choice)
                element = dict_xpaths['SEARCH_ID']
                dict_xpaths['SEARCH_ID'] = ''
            elif key == 'IMAGE':
                element = driver.find_element(by=By.XPATH,value=dict_xpaths[key]).get_attribute('href')
            elif key == 'NAME':
                element = driver.find_element(by=By.XPATH,value=dict_xpaths[key]).text.split(': ')[1]
            elif key == 'DESCRIPTION':
                element = driver.find_element(by=By.XPATH,value=dict_xpaths[key]).text
                if '\n' in element:
                    element = element.replace('\n',' ')
                dict_elements['DESCRIPTION_SHORT'] = element[0:10]
            elif key == 'RATING':
                element = driver.find_element(by=By.XPATH,value=dict_xpaths[key]).text
                if len(element) == 0:
                    element = '0'
                if '\n' in element:
                    element = element.replace('\n',' ')
            elif key == 'COUNT_RAITING':
                element = driver.find_element(by=By.XPATH,value=dict_xpaths[key]).text
                if 'M' in element:
                    element = element.replace('M','000000')
            else:
                element = driver.find_element(by=By.XPATH,value=dict_xpaths[key]).text
                if '\n' in element:
                    element = element.replace('\n',' ')
                
            dict_elements[key] = element
        dict_db[url] = dict_elements
    driver.quit()
    return dict_db
dict_db = pars_func()
def add_pars_to_db(name_table):
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM '+name_table)
    for key_url in dict_db.keys():
        tuple_values = dict_db[key_url].values()
        cursor.execute('INSERT INTO '+name_table+' (NAME,AUTHOR,RAITING,IMAGE,DESCRIPTION_SHORT,DESCRIPTION,DATE,COUNT_RAITING,SEARCH_ID) VALUES (?,?,?,?,?,?,?,?,?);', tuple(tuple_values) )
        connection.commit()
    connection.close()
add_pars_to_db('FirstApp_book')
print(dict_db)

def read_pars_from_db(name_table):
    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        command_take_id = "SELECT id from "+name_table
        cursor.execute(command_take_id)
        count_id = cursor.fetchall()
        for i in range(len(count_id)):
            command_take_data = 'SELECT NAME,RAITING,IMAGE,AUTHOR,DESCRIPTION,DATE,COUNT_RAITING from FirstApp_book where id = ?'
            id = i+1
            cursor.execute(command_take_data,(id,)) 
            data = cursor.fetchall()
            print(data)
    except:
        pass
# read_pars_from_db('FirstApp_book')
