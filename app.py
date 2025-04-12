from flask import Flask, request, jsonify, send_file
from gtts import gTTS
import os
import uuid
import traceback

app = Flask(__name__)

# Output directory for generated audio files
output_dir = os.path.join(os.path.dirname(__file__), "python_scripts")
os.makedirs(output_dir, exist_ok=True)

@app.route('/')
def index():
    return jsonify({"message": "Flask TTS Backend is live!"})

@app.route('/generate_speech', methods=['POST'])
def generate_speech():
    try:
        data = request.get_json()
        text = data.get('text')
        language = data.get('language', 'en')

        if not text:
            return jsonify({"error": "Text is required"}), 400

        # Generate a unique filename to avoid conflicts
        file_name = f"{uuid.uuid4()}.mp3"
        file_path = os.path.join(output_dir, file_name)

        # Generate speech
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(file_path)

        if not os.path.exists(file_path):
            return jsonify({"error": "Failed to generate MP3"}), 500

        # Return the audio file as a downloadable file
        return send_file(
            file_path,
            mimetype="audio/mpeg",
            as_attachment=True,
            download_name="speech.mp3"
        )

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
