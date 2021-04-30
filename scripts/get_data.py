import pandas as pd

def get_chunks(dataset_dir):
    # Loading the data in chunks of 1000000 data at a time
    chunksize = 1000000
    chunks = pd.read_csv(dataset_dir, chunksize = chunksize, header = None, compression='gzip', sep='\t', error_bad_lines=False, low_memory=False, quoting=3)
    return chunks


def get_dataframe(title, language = "dewiki", month = "2021-01"):
    LANGUAGE = language
    MONTH = month
    SITENAME = LANGUAGE.replace('wiki', '.wikipedia')
    # directory on PAWS server that holds Wikimedia dumps of the given month(Jan)
    DUMP_DIR = f"https://dumps.wikimedia.org/other/clickstream/{MONTH}/"
    CLICKSTREAM_FN = f'clickstream-{LANGUAGE}-{MONTH}.tsv.gz'

    data = [ ]
    for chunk in get_chunks(DUMP_DIR + CLICKSTREAM_FN):
        # Memory Optimization
        # Changing the datatype of "Type" attribute to category 
        chunk[2] = chunk[2].astype('category')
        chunk = chunk[(chunk[0].str.title() == title.title())|(chunk[1].str.title() == title.title())]
        data.append(chunk)

    df = pd.concat(data)
    df = df.reset_index(drop=True)
    # Renaming the column
    df.columns = ['Source','Destination','Type','TotalNum']
    df['TotalNum'].max()
    # Memory Optimization
    # Changing the datatype of "TotalNum" attribute to uint16 to reduce memory usage
    df['TotalNum'] = df['TotalNum'].astype('uint16')
    # Memory Optimization
    # Changing the datatype of "Type" attribute to category 
    df['Type'] = df['Type'].astype('category')

    return df

