# from flask import Flask, render_template, request, send_file
# import os
# from Instruction import BrailleTypeWritter

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads'
# app.config['FILE_LIST_FILE'] = 'static/uploads/file_list.txt'
# app.config['Target_FILE'] = ''
# target = ""

# def save_file_list(filename):
#     with open(app.config['FILE_LIST_FILE'], 'a') as file_list:
#         file_list.write(filename + '\n')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return 'No file part'

#     file = request.files['file']

#     if file.filename == '':
#         return 'No selected file'

#     if file:
#         filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#         file.save(filename)
#         save_file_list(file.filename)
#         BrailleTypeWritter(filename)
#         app.config['Target_FILE'] = filename.split('.')[0] + '.png'
#         return 'File uploaded successfully!'

# @app.route('/file_list')
# def get_file_list():
#     with open(app.config['FILE_LIST_FILE'], 'r') as file_list:
#         content = file_list.read()
#     return content

# @app.route('/download')
# def download_file():
#     return send_file(app.config['Target_FILE'], as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, send_file
from Instruction import BrailleTypeWritter
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['FILE_LIST_FILE'] = 'static/uploads/file_list.txt'
app.config['test'] = ''

def save_file_list(filename):
    with open(app.config['FILE_LIST_FILE'], 'a') as file_list:
        file_list.write(filename + '\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        ## print(filename)
        file.save(filename)
        BrailleTypeWritter(filename)
        print("finish!")
        app.config['test'] = filename.split('.')[0] + '.gcode'
        save_file_list(file.filename)
        return 'File uploaded successfully!'

@app.route('/file_list')
def get_file_list():
    with open(app.config['FILE_LIST_FILE'], 'r') as file_list:
        content = file_list.read()
    return content

@app.route('/download')
def download_file():
    return send_file(app.config['test'], as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)