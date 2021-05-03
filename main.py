from flask import Flask, render_template, request

from scripts import article,plots,get_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/result', methods=['GET', 'POST'])
def search_request():
    search_term = request.form["input"]
    res = article.related_articles(search_term)
    plot = plots.sankey_diagram(res["dataframe"], "Common Pathway to and from "+ search_term + " article")
    return render_template('results.html', res=res, plot = plot )

if __name__ == '__main__':
    app.run()