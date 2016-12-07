import cgitb
import json
import os.path
cgitb.enable()


import cgi
form = cgi.FieldStorage()
if form.getvalue('user'):
   users = form.getvalue('user')
if form.getvalue('cmd'):
   cmd = form.getvalue('cmd')
# prints a minimal HTTP header
print ('Content-Type: text/html')
print()

# print the HTTP body, which is the HTML file representing lecture1.html)

print ('<html>')
print ('	<head>')

print ('		<title>')

print ('''
			Game
		</title>

		<style type="text/css">
			h1 {
				font-size: 100px;
				font-family: arial;
			}

			img {
				width: 300px;
			}

			p#myLine {
				color: red;
			}
		</style>

	</head>
''')

print ('<body>')
print ('<h2>Your name is: ' + form['my_name'].value + '</h2>')

print ('<h2>Your Password is: ' + form['my_pw'].value + '</h2>')
val=logins(form['my_name'].value, form['my_pw'].value)
if(val==True):
	print ('<form method="post" action=".\cgi-bin\game.py">')
	print ('<input type="submit" name="'form['my_name'].value'" value="Start Game"/>')
else:
	print ('<form method="post" action="..lecture3-form.html">')
	print ('<input type="submit" name="login" value="Create User"/>')
	addUserData(form['my_name'].value, form['my_pw'].value,datafile,"userdata.json")
print ('''
	</body>
</html>''')
