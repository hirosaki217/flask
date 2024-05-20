from flask import Flask, request
import sys
import os
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# ChromeDriverManager().install()
import undetected_chromedriver as uc

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World.!'

@app.route('/about')
def about():
    ### Dirty fixes for Lambda
    driver_executable_path = '/tmp/chromedriver'
    browser_executable_path = '/opt/chrome/chrome'
    
    os.system(f'cp /opt/chromedriver {driver_executable_path}')
    os.chmod(driver_executable_path, 0o777)
    python_version = f"{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}"
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')
    driver = uc.Chrome(options=chrome_options, driver_executable_path=driver_executable_path, browser_executable_path=browser_executable_path, version_main=114)
    driver.get('https://api.myip.com/')
    return 'About - Python Version: ' + python_version

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
