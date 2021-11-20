import pandas as pd

def get_data():
    df = pd.read_csv('data2.csv')
    filenames = []
    for n in df['EName']:
        if len(n.split(' '))>1:
            n = n.replace(' ','_')
        filenames.append(n+".png")
    df.loc[:,'filename'] = filenames
    df = df.to_dict('records')
    return df

if __name__ == '__main__':
    print(get_data())