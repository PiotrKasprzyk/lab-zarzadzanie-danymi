import justpy as jp
import pandas as pd

# Wczytanie danych
df = pd.read_csv('reviews_courses.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
daily_avg = df.groupby(df['Timestamp'].dt.date)['Rating'].mean()

def chart_data():
    data = [[int(pd.Timestamp(date).timestamp()) * 1000, avg] for date, avg in daily_avg.items()]
    return data

def web_page():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Interaktywny wykres ocen", classes="text-h3 text-center q-pa-md")
    chart = jp.HighCharts(a=wp, options={
        'chart': {'type': 'spline'},
        'title': {'text': 'Średnia ocena wg dni'},
        'xAxis': {
            'type': 'datetime',
            'title': {'text': 'Data'}
        },
        'yAxis': {
            'title': {'text': 'Średnia ocena'}
        },
        'series': [{'name': 'Rating', 'data': chart_data()}],
        'tooltip': {'shared': True, 'crosshairs': True}
    })
    return wp

jp.justpy(web_page)
