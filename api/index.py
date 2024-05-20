from flask import Flask, request
import sys
import os
from pathlib import Path
from tempfile import mkdtemp
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# ChromeDriverManager().install()
import undetected_chromedriver as uc

app = Flask(__name__)
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        data = ''
        for f in files:
            data = data + '{}{}'.format(subindent, f))
        return data

@app.route('/')
def home():
    path = request.args.get('path')
    path = "/" if path == None else path
    return list_files(path)

@app.route('/about')
def about():
    ### Dirty fixes for Lambda
    driver_executable_path = '/var/tmp/chromedriver'
    print(os.getcwd())
    print( os.path.join(os.getcwd(), 'chromedriver'))
    # driver_path = '/tmp/chromedriver'
    browser_executable_path = '/var/opt/chrome/chrome'
    service = webdriver.ChromeService(driver_executable_path)
    
    # os.system(f'cp /var/opt/chromedriver {driver_path}')
    # os.chmod(driver_path, 0o777)

    options = webdriver.ChromeOptions()
    options.binary_location = '/var/opt/chrome/chrome'
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280x1696')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-dev-tools')
    options.add_argument('--no-zygote')
    options.add_argument(f'--user-data-dir={mkdtemp()}')
    options.add_argument(f'--data-path={mkdtemp()}')
    options.add_argument(f'--disk-cache-dir={mkdtemp()}')
    options.add_argument('--remote-debugging-port=9222')
    driver = uc.Chrome(options=options, driver_executable_path=driver_executable_path, browser_executable_path=browser_executable_path, version_main=114, service=service)
    driver.get('https://api.myip.com/')
    return 'About - Python Version: ' + python_version + driver.page_source

@app.route('/housenow-crawl', methods=['POST'])
def home2():
    
    url = request.json.get('url')
    # my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
  
    # options = uc.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument(f"user-agent={my_user_agent}")
  
    # Initialize Chrome WebDriver with the specified options
    # driver = uc.Chrome(version_main = 120,options=options,user_multi_procs=False, use_subprocess=False, headless=True)
    # driver.get(url)
    # page_source = driver.page_source
    # driver.quit()
    return {
        'html': page_source
    }
    
    


def get_page_source(url):
  # Define a custom user agent
  
  return page_source
