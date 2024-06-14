import justpy as jp
import pandas as pd

# Wczytanie danych
df = pd.read_csv('reviews_courses.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
monthly_avg = df.groupby(df['Timestamp'].dt.to_period('M'))['Rating'].mean()

def chart_data_monthly():
    data = [[int(pd.Timestamp(str(date)).timestamp()) * 1000, avg] for date, avg in monthly_avg.items()]
    return data

def web_page_monthly():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Interaktywny wykres ocen miesięcznych", classes="text-h3 text-center q-pa-md")
    chart = jp.HighCharts(a=wp, options={
        'chart': {'type': 'spline'},
        'title': {'text': 'Średnia ocena wg miesięcy'},
        'xAxis': {
            'type': 'datetime',
            'title': {'text': 'Miesiąc'}
        },
        'yAxis': {
            'title': {'text': 'Średnia ocena'}
        },
        'series': [{'name': 'Rating', 'data': chart_data_monthly()}],
        'tooltip': {'shared': True, 'crosshairs': True}
    })
    return wp

jp.justpy(web_page_monthly)
