import plotly # To plot sankey diagram
from matplotlib import pyplot as plt
from scripts import get_data

def related_articles(search_term):
    """
        Returns a list of related articles with only top 5 (source, destination) pairs
        where destination is Holland and top 5 (source, destination) pair where
        source is Holland    
    """
    # Get dataframe
    df = get_data.get_dataframe(title = search_term)
    # Filter the dataframe with type as link
    df = df[df['Type'] == 'link']
    # Finding minimum pageview among top 5 (source, destination) pairs where destination is Holland 
    resource_min_in_5 = df[(df['Destination']==search_term)].sort_values(['TotalNum'],ascending=False).head(5)['TotalNum'].min()

    # Dropping the data where destination is holland and pageview is less than resource_min_in_5
    x = df[(df['Destination']==search_term) & (df['TotalNum'] < resource_min_in_5)].index
    df = df.drop(x, axis=0)

    #Finding minimum pageview among top 5 (source, destination) pairs where Source is Holland
    referer_min_in_5 = df[(df['Source']==search_term)].sort_values(['TotalNum'],ascending=False).head(5)['TotalNum'].min()

    # Dropping the data where source is holland and pageview is less than referer_min_in_5
    x = df[(df['Source']==search_term)& (df['TotalNum'] < referer_min_in_5)].index
    df = df.drop(x, axis=0)

    df = df.reset_index(drop=True)

    related_articles = []

    for i in list(df['Source']):
        if i.upper()  == search_term.upper():
            pass
        elif i in related_articles:
            pass
        else:
            related_articles.append(i)

    for i in list(df['Destination']):
        if i.upper()  == search_term.upper():
            pass
        elif i in related_articles:
            pass
        else:
            related_articles.append(i)

    response = dict()
    response["related article"] = related_articles
    response["total"] = len(related_articles)

    return response