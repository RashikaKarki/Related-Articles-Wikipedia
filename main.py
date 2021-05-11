from flask import Flask, render_template, request
from scripts import article
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('search.html')


@app.route('/result', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["input"]
    language = request.form["language"]
    res = article.related_articles(search_term, language)
    return render_template('results.html', res=res)


if __name__ == '__main__':
    app.run()
