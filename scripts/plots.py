import plotly
import plotly.graph_objs as go
import json

def sankey_diagram(df, title):
    labelList = []
    colorNumList = []
    for catCol in ['Source','Destination']:
        labelListTemp =  list(set(df[catCol].values))
        colorNumList.append(len(labelListTemp))
        labelList = labelList + labelListTemp

    # remove duplicates from labelList
    labelList = list(dict.fromkeys(labelList))
    
    # giving each source and detination unique integer id
    df['SourceID'] = df['Source'].apply(lambda x: labelList.index(x))
    df['TargetID'] = df['Destination'].apply(lambda x: labelList.index(x))
    
    data = [go.Sankey(
            node = dict(
              pad = 15,
              thickness = 20,
              line = dict(
                color = "black",
                width = 0.5
              ),
              label = labelList
            ),
            link = dict(
              source = df['SourceID'],
              target = df['TargetID'],
              value = df['TotalNum']
            )
          )]


    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON