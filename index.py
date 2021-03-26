from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from scrapy.crawler import CrawlerRunner
from shop_parser import BaseSpider

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
    global json
    json = []
    result = crawler.crawl(BaseSpider, json = json, start_urls = [site])
    result.addCallback(finish)
    return 'Парсин начался' 

def finish():
  print(json)

if __name__ == '__main__':
  socketio.run(app, debug=True, host='0.0.0.0') #TODO вынести в конфиг

