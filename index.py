import requests
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from scrapy.crawler import CrawlerRunner
import shop_parser.config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secta'
socketio = SocketIO(app)
crawler = CrawlerRunner()

@socketio.on('/message')
def handle_message(data):
  return 'WELLCOME!! ' + data

@app.route('/test')
def text():
  spider = BaseSpider()
  print(spider)
  return 'watch console'

@app.route('/', methods=['GET'])
def index():
  return render_template('parse.html', **{'hello': 'word'}) 

@app.route('/parse', methods=['POST'])
def parse():
  if request.method == 'POST':
    site = request.form.get('site')
    contex = requests.get('http://127.0.0.1:9080/crawl.json?spider_name=base&url={}'.format(site))
    return contex.json()

def finish():
  print(json)

if __name__ == '__main__':
  socketio.run(app, SERVER_CONFIG['debug_mode'], SERVER_CONFIG['host'])
