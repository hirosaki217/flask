from flask import Flask, request
from utils.undetected_chromedriver import get_page_source

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/housenow-crawl', methods=['POST'])
def home2():
    url = request.json.get('url')
    data = get_page_source(url)
    return {
        'html': data
    }