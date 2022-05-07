# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
# import additional libraries below
import cv2
import numpy as np

app = Flask(__name__)

# Open and redirect to default upload webpage
@app.route('/')
def load_form():
    return render_template('upload.html')

# Function to upload image and redirect to new webpage
@app.route('/gray', methods=['POST'])
def upload_image():
    file = request.files['file']
    filename = secure_filename(file.filename)
    # write the read and write function on image below 
    file_data=make_grayscale(file.read())
    with open(os.path.join('static/',filename),'wb') as f:
    	f.write(file_data)
        # ends here

    display_message = 'Image successfully uploaded and displayed below'
    return render_template('upload.html', filename=filename, message = display_message)


# Write the make_grayscale() function below
def make_grayscale(input_image):
	image_array=np.fromstring(input_image,dtype='uint8')
	print("Image Array : ",image_array)
	decode_array_to_image=cv2.imdecode(image_array,cv2.IMREAD_UNCHANGED)
	print("Decode Values of Image : ",decode_array_to_image)
	converted_grey_image=cv2.cvtColor(decode_array_to_image,cv2.COLOR_RGB2GRAY)
	status,output_image=cv2.imencode('.PNG',converted_grey_image)
	print("Status : ",status)
	return output_image







# make_grayscale() function ends above

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))



if __name__ == "__main__":
    app.run()


