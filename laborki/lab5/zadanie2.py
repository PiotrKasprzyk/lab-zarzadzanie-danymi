import justpy as jp
import pandas as pd

# Wczytanie danych
df = pd.read_csv('reviews_courses.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
monthly_course_avg = df.groupby([df['Timestamp'].dt.to_period('M'), 'Course Name'])['Rating'].mean().unstack()

def chart_data_course():
    data = []
    for course in monthly_course_avg.columns:
        course_data = [[int(pd.Timestamp(str(date)).timestamp()) * 1000, avg] for date, avg in monthly_course_avg[course].items()]
        data.append({'name': course, 'data': course_data})
    return data

def web_page_course():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Średnia ocena wg miesięcy dla kursów", classes="text-h3 text-center q-pa-md")
    chart = jp.HighCharts(a=wp, options={
        'chart': {'type': 'areaspline'},
        'title': {'text': 'Średnia ocena wg miesięcy dla kursów'},
        'xAxis': {
            'type': 'datetime',
            'title': {'text': 'Miesiąc'}
        },
        'yAxis': {
            'title': {'text': 'Średnia ocena'}
        },
        'series': chart_data_course(),
        'tooltip': {'shared': True, 'crosshairs': True}
    })
    return wp

jp.justpy(web_page_course)
