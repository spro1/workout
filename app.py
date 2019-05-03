from flask import Flask, render_template, jsonify, request, url_for, redirect
from flask_socketio import SocketIO
import app.scrap.scrap as scrap
import app.api.upload as upload
import json
import datetime
import pymongo

app = Flask(__name__)

UPLOAD_FOLDER = "storage/file"
json_path = "config/dashboard.json"

socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def timer():
    json_data = open(json_path).read()
    data = json.loads(json_data)
    #namu_urls = data['namu']
    naver_news_urls = data['naver']
    #dc_urls = data['dc']
    river = data['river']
    dogdrip = data['dogdrip']
    korea = data['korea']
    return render_template('index.html', dog_urls=dogdrip, korea_urls=korea,naver_urls = naver_news_urls, river=river)

@app.route('/poop', methods=['GET'])
def poop():
    conn = pymongo.MongoClient("192.168.0.3",27017)
    now = datetime.datetime.strptime(datetime.date.today().strftime("%Y-%m-%d"),"%Y-%m-%d")
    data = conn.poop.log.find({"date":{"$gte":now}}).limit(20).sort("_id",-1)
    conn.close()

    return render_template('poop.html', data=data)


@app.route('/file/upload', methods=['POST'])
def file():
    return jsonify(upload.file_upload(request, UPLOAD_FOLDER))


@app.route('/upload_poop', methods=['POST'])
def poop_upload():
    if request.method == 'POST':
        conn = pymongo.MongoClient("192.168.0.3",27017)
        save_info = {}
        try:
            poop_type = request.form["type"]
            poop_result = request.form["result"]
            poop_comment = request.form["comment"]
            poop_addr = request.remote_addr
            date = datetime.datetime.now()
            save_info["type"] = poop_type
            save_info["result"] = poop_result
            save_info["comment"] = poop_comment
            save_info["addr"] = poop_addr
            save_info["date"] = date
            conn.poop.log.insert(save_info)
            conn.close()
        except:
            conn.close()
            return redirect(url_for('poop'))

    return redirect(url_for('poop'))

@socketio.on('message', namespace='/ws')
def handle_event(message):
    conn = pymongo.MongoClient("192.168.0.3",27017)
    now = datetime.datetime.strptime(datetime.date.today().strftime("%Y-%m-%d"),"%Y-%m-%d")
    data = conn.poop.log.find({"date":{"$gte":now}}).limit(20).sort("_id",-1)
    send(data,broadcast=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8080", debug=True)
