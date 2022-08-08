from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
app = Flask(__name__)

@app.route('/',methods=['post','get']) # will use get for the first page-load, post for the form-submit
def predict(): # this function can have any name
	model = load_model('mymodel.h5') # the nand.h5 file was created in Colab, downloaded and uploaded using Filezilla
	in1 = request.form.get('in1') # get the two numbers from the request object
	# in2 = request.form.get('in2')
	if in1 == None: 
        #or in2 == None: # check if any number is missing
		return render_template('index.html', result="0")
		# calling render_template will inject the variable 'result' and send index.html to the browser
	else:
		arr = np.array([[ int(in1) ]]) # cast string to decimal number, and make 2d numpy array.
		predictions = model.predict(arr) # make new prediction
		return render_template('index.html', result=str(predictions[0][0]))
		# the result is set, by asking for row=0, column=0. Then cast to string.

if __name__ == '__main__':
	app.run()
