from flask import Flask, render_template, jsonify, request
import app.scrap.scrap as scrap
import app.api.upload as upload

app = Flask(__name__)

UPLOAD_FOLDER = "storage/file"


@app.route('/', methods=['GET'])
def timer():
    namu_urls = scrap.namu_crawler()
    naver_news_urls = scrap.naver_news_crawler()
    dc_urls = scrap.dc_crawler()
    river = scrap.river_temp()
    return render_template('index.html', namu_urls=namu_urls, naver_urls = naver_news_urls, dc_urls = dc_urls, river=river)


@app.route('/file/upload', methods=['POST'])
def file():
    return jsonify(upload.file_upload(request, UPLOAD_FOLDER))






if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8080", debug=True)
