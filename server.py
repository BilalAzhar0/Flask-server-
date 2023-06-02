from flask import Flask, request, render_template
import logging
import os
import datetime

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG) #for better debuging, we will log out every request with headers and body.
@app.before_request
def log_request_info():
    logging.info('Headers: %s', request.headers)
    logging.info('Body: %s', request.get_data())

@app.route("/upload", methods=["POST"])
def upload_image():

    if request.method == "POST": #if we make a post request to the endpoint, look for the image in the request body
        image_raw_bytes = request.get_data()  #get the whole body

        current_datetime = datetime.datetime.now()
        file_name = current_datetime.strftime("%m-%d-%H-%M-%S")
        save_location = os.path.join(app.root_path, "received", file_name)
        #save_location = (os.path.join(app.root_path, "received/test.jpg")) #save to the same folder as the flask app live in
        
        f = open(save_location, 'wb') # wb for write byte data in the file instead of string
        f.write(image_raw_bytes) #write the bytes from the request body to the file
        f.close()

        print("Image saved")

        return "image saved"

if __name__ == '__main__':
    print("Flask server starting...")
    app.run(host='0.0.0.0', port=8000)
