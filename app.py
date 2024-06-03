from flask import Flask, render_template, request, redirect, url_for  
import random    
  
app = Flask(__name__)    
  
names = {    
    "Audrey": 0,    
    "Ashton": 0,    
    "Collin": 0,    
    "Yogi": 0,    
    "Andrew": 0,    
    "Jayce": 0,    
    "Doyle": 0,    
    "Brian": 0,    
    "Maggie": 0,    
    "Sharon": 0,    
    "Archie": 0    
}    
  
@app.route('/')    
def home():    
    return render_template('index.html', names=names)    
  
@app.route('/add_point/<name>', methods=['POST'])    
def add_point(name):    
    names[name] += 1    
    return redirect(url_for('home'))    
  
@app.route('/random_winner', methods=['POST'])    
def random_winner():    
    total_points = sum(names.values())    
    if total_points == 0:    
        winner = "No points yet"    
    else:    
        winner = random.choices(list(names.keys()), weights=names.values(), k=1)[0]    
    return render_template('index.html', names=names, winner=winner)    
  
@app.route('/reset', methods=['POST'])  
def reset():  
    for key in names:  
        names[key] = 0  
    return redirect(url_for('home'))  


if __name__ == '__main__':    
    app.run(debug=True)    
