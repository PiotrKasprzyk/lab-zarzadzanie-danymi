import justpy as jp
import pandas as pd

# Wczytanie danych
df = pd.read_csv('reviews_courses.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['DayOfWeek'] = df['Timestamp'].dt.day_name()
day_of_week_avg = df.groupby('DayOfWeek')['Rating'].mean()

def chart_data_day_of_week():
    data = [[day, avg] for day, avg in day_of_week_avg.items()]
    return data

def web_page_day_of_week():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Zadowolenie użytkowników wg dni tygodnia", classes="text-h3 text-center q-pa-md")
    chart = jp.HighCharts(a=wp, options={
        'chart': {'type': 'line'},
        'title': {'text': 'Zadowolenie użytkowników wg dni tygodnia'},
        'xAxis': {
            'title': {'text': 'Dzień tygodnia'},
            'categories': list(day_of_week_avg.index)
        },
        'yAxis': {
            'title': {'text': 'Średnia ocena'}
        },
        'series': [{'name': 'Rating', 'data': chart_data_day_of_week()}],
        'tooltip': {'shared': True, 'crosshairs': True}
    })
    return wp

jp.justpy(web_page_day_of_week)
