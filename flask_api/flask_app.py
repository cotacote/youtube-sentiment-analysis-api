from flask import Flask, jsonify
from service.service_impl import ServiceImpl


service = ServiceImpl()
app = Flask(__name__)


@app.route('/analyze/<video_id>', methods=['GET'])
def analyze_video(video_id) -> str:
    return jsonify(service.execute({"video_id": video_id}))

if __name__ == '__main__':
    app.run(debug=True)