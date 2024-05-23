import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from tempfile import mkdtemp
from flask import Flask,request
import requests 
import zipfile
import os
app = Flask(__name__)
 

@app.route('/')
def home():
    download_url("https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.76/linux64/chromedriver-linux64.zip", "/tmp/chromedriver.zip")
    return 'HOUSENOW'

@app.route('/test')
def test():
    driver = get_uc_driver()
    driver.get('http://checkip.amazonaws.com/')
    return driver.page_source
def get_uc_driver():
        
    options = uc.ChromeOptions()
    # options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--single-process")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")    
    driver_executable_path = '/tmp/chromedriver-linux64/chromedriver'
    if os.path.isfile('/tmp/chromedriver-linux64/chromedriver'):
        print('chromedriver exists')
    else:
        print('chromedriver is dowloading')
        download_url("https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.76/linux64/chromedriver-linux64.zip", "/tmp/chromedriver.zip")
    # os.system(f'cp /opt/chromedriver {driver_executable_path}')
    os.chmod(driver_executable_path, 0o777)

    driver = uc.Chrome( options=options, driver_executable_path= driver_executable_path, headless=True, version_main=125)#, use_subprocess=True)

    return driver  


# driver = get_uc_driver()
# driver.get('http://checkip.amazonaws.com/')
# print(driver.page_source)

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
    with zipfile.ZipFile("/tmp/chromedriver.zip", 'r') as zip_ref:
        zip_ref.extractall("/tmp")
        
# download_url("https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.76/linux64/chromedriver-linux64.zip", "/tmp/chromedriver.zip")