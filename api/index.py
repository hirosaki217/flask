import undetected_chromedriver as uc
from pyvirtualdisplay import Display
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from tempfile import mkdtemp
from flask import Flask,request
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
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--single-process")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")    
    ChromeDriverManager(driver_version="125").install()
    # driver_executable_path = '/tmp/undetected_chromedriver/undetected_chromedriver'
    # os.system(f'cp /opt/chromedriver {driver_executable_path}')
    # os.chmod(driver_executable_path, 0o777)

    driver = uc.Chrome( options=options, headless=True, no_sandbox=True)#, use_subprocess=True)

    return driver  



