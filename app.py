from flask import Flask, render_template, jsonify, request
import app.scrap.scrap as scrap
import app.api.upload as upload
import json
app = Flask(__name__)

UPLOAD_FOLDER = "storage/file"
json_path = "config/dashboard.json"

@app.route('/', methods=['GET'])
def timer():
    json_data = open(json_path).read()
    data = json.loads(json_data)
    namu_urls = data['namu']
    naver_news_urls = data['naver']
    dc_urls = data['dc']
    river = data['river']
    return render_template('index.html', namu_urls=namu_urls, naver_urls = naver_news_urls, dc_urls = dc_urls, river=river)


@app.route('/file/upload', methods=['POST'])
def file():
    return jsonify(upload.file_upload(request, UPLOAD_FOLDER))






if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8080", debug=True)
