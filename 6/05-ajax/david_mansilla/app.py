from flask import Flask, render_template, session, request, redirect, url_for
import csv
from operator import itemgetter



app= Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/home",methods=["GET","POST"])
def home():
    stat_type = request.form.get('stat_type', '')    
    print stat_type
    top10 = niceify_top_10(get_top_10(stat_type), stat_type)
    return render_template("home.html", top10 = top10)

def get_top_10(key_stat):
    # Finding top 10 players based on the key_stat of choice (must match a datapoint in the csv file)
    top10 = []
    with open('stats.csv') as stats:
        reader = csv.DictReader(stats)
        for row in reader:
            top10.append({'Player': row['Player'], key_stat : float(row[key_stat])})
    result = sorted(top10, key=itemgetter(key_stat), reverse=True)
    
    # TOP 10 List Creation
    counter = 1
    while counter <= 10:
        r = result[counter]
        #print str(counter) + ". " + r['Player'] + ": " + r[key_stat] + " " + key_stat 
        counter +=1 
    return result

def niceify_top_10(top10List, key_stat):
    res = []
    counter = 1
    while counter <= 10:
      r = top10List[counter]
      res.append( r['Player'] + ": " + str(r[key_stat]) + " " + key_stat )
      counter+= 1
    return res

if __name__ == "__main__":
    
    print "\nPPG\n"
    print niceify_top_10(get_top_10('PPG'), 'PPG')
    print "\nAPG\n"
    print niceify_top_10(get_top_10('APG'), 'APG')
    print "\nRPG\n"
    print niceify_top_10(get_top_10('RPG'), 'RPG')
    print "\nBPG\n"
    print niceify_top_10(get_top_10('BPG'), 'BPG')
    print "\nDRPG\n"
    print niceify_top_10(get_top_10('DRPG'), 'DRPG')
    #print "\nFGP\n"
    #print niceify_top_10(get_top_10('FGP'), 'FGP')
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
