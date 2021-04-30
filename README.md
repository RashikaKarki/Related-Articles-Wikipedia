# Related Articles Wikipedia

![Demo](https://github.com/RashikaKarki/Related-Articles-Wikipedia/blob/main/resource/demo.gif)


A simple web application that gives you list of related articles to the searched term in wikipedia. Uses Wikipedia Clickstream data. 

## About the data:

> The data contains counts of (referer, resource) or (source, destination) pairs extracted from the request logs of Wikipedia.

### Format of the data

The data has 4 columns: Source, Destination, Type and TotalNum

- **Source :** The result of mapping the source/referrer URL to the fixed set of values
    - **the article title** : an article in the main namespace
    - **other-internal** : a page from any other Wikimedia project 
    - **other-search** : an external search engine 
    - **other-external** : any other external site 
    - **other-empty** : an empty source 
    - **other-other** : anything else 
- **Destination :** The title of the article client requested
- **Type :** Described the relation between source and destination
    - **link** : if the source and request are both articles and the source links to the request
    - **external** : if the source host is not en(.m)?.wikipedia.org
    - **other** : if the source and request are both articles but the source does not link to the request. This can happen when clients search or spoof their refer.
- **TotalNum :** The number of occurrences of the (source, destination) pair


The data can be found at: https://dumps.wikimedia.org/other/clickstream/

## How to run the application locally?

- Step 1:
Clone the repo
- Step 2: 
Install the required packages

```pip install requirements.txt```
- Step 3:
Run the application

```
set FLASK_APP=main.py
flask run
```

The server will run on port `5000`
