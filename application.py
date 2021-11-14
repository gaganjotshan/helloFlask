from flask import Flask
from flask import jsonify
import numpy as np 

application = Flask(__name__)

@application.route('/')
def hello():
    return 'Hello Shan\n'
    
@application.route('/random/<n>')
def randomvalues(n):
    values = np.random.randint(0,10,int(n))
    result = {'values' : values.tolist()}
    return jsonify(result)
    
if __name__ == '__main__':
    application.run(debug=True)