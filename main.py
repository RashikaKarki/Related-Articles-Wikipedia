from flask import Flask, render_template, request

from scripts import article

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search/results', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["input"]
    res = article.related_articles(search_term)
    return render_template('results.html', res=res )

if __name__ == '__main__':
    app.run()