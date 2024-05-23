import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from tempfile import mkdtemp
from flask import Flask,request
import os
app = Flask(__name__)
 

@app.route('/')
def home():
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
    driver_executable_path = ChromeDriverManager(driver_version="125", url="https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.76/linux64/chromedriver-linux64.zip").install()
    # os.system(f'cp /opt/chromedriver {driver_executable_path}')
    # os.chmod(driver_executable_path, 0o777)

    driver = uc.Chrome( options=options, driver_executable_path= driver_executable_path, headless=True, version_main=125)#, use_subprocess=True)

    return driver  


# driver = get_uc_driver()
# driver.get('http://checkip.amazonaws.com/')
# print(driver.page_source)
print()