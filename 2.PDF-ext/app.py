from flask import Flask, render_template, request
import os
#from core import 
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/summarize/file', methods = ['GET', 'POST'])
def handlefile():
    if request.method == 'POST':
        if request.files:
            f = request.files['file']
            print(f)
            cmd = 'python core.py ./static/'+f.filename
            os.system(cmd)
            print(os.system(cmd))
            print(f.filename[0]+"_highlight.pdf")
            print(f.filename[0]+"_summary.pdf")
            return render_template('pdfsummarize.html', active = 1, fhl = f.filename[0]+"_highlight.pdf", fs = f.filename[0]+"_summary.pdf")
        else:
            return request.files
        # do something for core.py do run the code
    return "Upload file error"

@app.route('/summarize')
def summarize():
    return render_template('pdfsummarize.html', active = 0) 
      

if __name__ == '__main__':
   app.run(debug = True)