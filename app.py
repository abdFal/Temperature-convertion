# In your terminal, install the Flask library by running pip install Flask

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        celsius = float(request.form['celsius'])
        fahrenheit = (celsius * 9/5) + 32
        return str(fahrenheit) + ' degrees Fahrenheit'
    return '''
        <form method="post">Suhu
            Celsius:<br> <input type="text" name="celsius"><br>
            <input type="submit" value="Convert to Fahrenheit">
        </form>
    '''
if __name__ == '__main__':
    app.run(debug=True)

# you can change the program depends on the example konversi-suhu.py file