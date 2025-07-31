from flask import Flask, render_template, request, redirect, url_for
import os
from k.utils import secure_filename
import read_text_modified as rt # Import the modified script

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads/'
ANNOTATED_FOLDER = 'static/annotated/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ANNOTATED_FOLDER'] = ANNOTATED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload size

# Ensure the necessary folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ANNOTATED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    """Serves the main page with the upload form."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handles file upload and calls the text recognition script."""
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Call the text recognition function
        analysis_results = rt.recognize_text_in_image(filepath, app.config['ANNOTATED_FOLDER'])
        
        # Pass results to the results page
        return render_template('results.html', results=analysis_results, original_image=filename)

    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)