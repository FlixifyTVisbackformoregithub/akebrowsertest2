from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    query = request.args.get('query', '')
    return render_template('index.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)
