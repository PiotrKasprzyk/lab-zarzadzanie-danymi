import justpy as jp
import pandas as pd

# Wczytanie danych
try:
    df = pd.read_csv('reviews_courses.csv')
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    daily_avg = df.groupby(df['Timestamp'].dt.date)['Rating'].mean()
    
    # Wyświetlenie wczytanych danych w konsoli
    print(df.head())
    print(daily_avg.head())
except Exception as e:
    print(f"Błąd przy wczytywaniu pliku: {e}")

def chart_data():
    # Używamy listy krotek (timestamp, wartość) zgodnie z wymaganiami HighCharts
    data = [[int(pd.Timestamp(date).timestamp()) * 1000, avg] for date, avg in daily_avg.items()]
    return data

def web_page():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Interaktywny wykres ocen", classes="text-h3 text-center q-pa-md")
    if daily_avg.empty:
        error_message = jp.QDiv(a=wp, text="Brak danych do wyświetlenia", classes="text-subtitle2 text-center")
    else:
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
