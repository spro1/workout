from flask import Flask, render_template
import app.scrap.scrap as scrap

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    namu_urls = scrap.namu_crawler()
    naver_news_urls = scrap.naver_news_crawler()
    dc_urls = scrap.dc_crawler()
    river = scrap.river_temp()
    return render_template('index.html', namu_urls=namu_urls, naver_urls = naver_news_urls, dc_urls = dc_urls, river=river)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8080", debug=True)
