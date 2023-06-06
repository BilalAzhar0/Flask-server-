from flask import Flask, request, render_template
import logging
import os
import datetime

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG) #log out every request with headers and body.
@app.before_request
def log_request_info():
    logging.info('Headers: %s', request.headers)
    logging.info('Body: %s', request.get_data())

@app.route("/upload", methods=["POST"])
def upload_image():

    if request.method == "POST":
        filename = request.headers.get("Filename")
        image_raw_bytes = request.get_data()  

        if filename:
            save_location = os.path.join(app.root_path, "received", filename)
            f = open(save_location, 'wb')
            f.write(image_raw_bytes)
            f.close()
            print("Image saved:", filename)
            return "Image saved: " + filename
        else:
            return "Filename not provided"







    #    save_location = os.path.join(app.root_path, "received", header_string)
   #     f = open(save_location, 'wb') 
  #      f.write(image_raw_bytes) 

 #       print("Image saved")

#        return "image saved"

if __name__ == '__main__':
    print("Flask server starting...")
    app.run(host='0.0.0.0', port=8000)
