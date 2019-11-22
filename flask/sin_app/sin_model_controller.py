from flask import Flask, request, render_template
from wtforms import Form, validators, FloatField
import math

app = Flask(__name__)

# function is the model. Calculate sine and return a formatted string
def compute(val):
	result = math.sin(val)
	result_str = "Sine of {} is: {:.4f} (in radian)".format(val,result)
	return result_str

# Input form  and below is our controller
# form with a single Floatfield
class InputForm(Form):
	float_field = FloatField(validators = [validators.InputRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
	sine_val = None
	form = InputForm(request.form)
	if request.method == 'POST' and form.validate():
		input_val = form.float_field.data
		sine_val = compute(input_val)
	return render_template("sine_view.html", template_form = form, result = sine_val)

if __name__ == "__main__":
	app.run(debug=True)
