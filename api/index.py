from flask import Flask, request
import sys
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# ChromeDriverManager().install()
import undetected_chromedriver as uc

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    python_version = f"{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}"
    driver = uc.Chrome(user_multi_procs=False, use_subprocess=False, headless=True)
    driver.get('https://api.myip.com/')
    return 'About - Python Version: ' + python_version

@app.route('/housenow-crawl', methods=['POST'])
def home2():
    
    url = request.json.get('url')
    my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
  
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument(f"user-agent={my_user_agent}")
  
    # Initialize Chrome WebDriver with the specified options
    driver = uc.Chrome(options=options,user_multi_procs=False, use_subprocess=False, headless=True)
    driver.get(url)
    page_source = driver.page_source
    driver.quit()
    return {
        'html': page_source
    }
    
    


def get_page_source(url):
  # Define a custom user agent
  
  return page_source