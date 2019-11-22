from flask import Flask, render_template_string, render_template

app = Flask(__name__) 

@app.route('/') 
def hello_world(): 
    return 'Hello World' 


page = '''
<html>
	<head>
		<title>Hello World</title>
	</head>
   <body style="background-color:#E6E6FA">
    	<h2>Hello, {{ name }}!</h2>
   </body>
</html>
'''

@app.route('/h1/<user>')
def hello_name_string(user):
    return render_template_string(page, name = user)


@app.route('/h2/<user>')
def hello_name_file(user):
    return render_template('hello.html', name = user)

if __name__ == '__main__': 
    app.run(debug = True)
