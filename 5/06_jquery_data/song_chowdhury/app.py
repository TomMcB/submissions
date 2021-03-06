from flask import Flask, render_template, request, redirect, url_for, session
import json, urllib2
import string

app = Flask(__name__)
data = []
counter = 1
file = open("MOCK_DATA.csv", 'r')
lines = file.readlines() #realines() should return list of lines
for line in lines:
    newlist = line.split(',')
    data.append(newlist)

file.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getdata")    #####puts csv data into global variable data
def getdata():
    print "starting getdata"
    print "ending getdata"
    return json.dumps(data)              ##json.dumps returns a string

@app.route("/getprofile")      ######returns a line from global variable data
def getprofile():
    print "starting getprofile"
    global counter
    line = data[counter]
    #print line[1]                  ##this is not a string, but a line
    counter += 1
    dict = {}
    dict["first"] = line[1]
    dict["last"] = line[2]
    dict["age"] = line[3]
    dict["email"] = line[4]
    dict["country"] = line[5]

    #GOOGLE IMAGE API NO LONGER AVAILABLE?
    #################################
    #picture_url = """https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s"""
    #search = line[1] +"%20"+ line[2]   #replace all spaces with %20
    #print search
    #picture_url = picture_url%(search)
    #print picture_url
    #request_picture_url = urllib2.urlopen(picture_url)
    #picture_result = request_picture_url.read()
    #picture_r = json.loads(picture_result)
    #print picture_r
    #picture = picture_r['responseData']['results'][0]['url']
    #dict["picture"] = picture
    #print picture
    print "ending getprofile"
    if counter > 99:
        counter = 1
    return json.dumps(dict)   ##returns a dictionary instead of string

@app.route("/findprofile")
def findprofile():
	global counter
	s = request.args.get("data")
	for line in data:
		if string.lower(s) in string.lower(line[1]) + " " + string.lower(line[2]) or s in line[4]:
			dict = {}
			dict["first"] = line[1]
			dict["last"] = line[2]
			dict["age"] = line[3]
			dict["email"] = line[4]
			dict["country"] = line[5]
			counter = int(line[0]) + 1
			return json.dumps(dict)
	counter = counter - 1
	return getprofile()


if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)
