import datetime
import requests
from django.shortcuts import render
from .forms import DateForm

def fetch_events_from_wikipedia(date):
    formatted_date = date.strftime('%m/%d')
    url = f'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/{formatted_date}'
    headers = {
        'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJmYWM1YjBjYjhiNjI0M2QzODNmODY3MmFiZTVlOWM5YyIsImp0aSI6Ijg0MTM1Mjk1YmU4NzYzMGM1ODJhZGQ5OWZkZTc2NGE4OGY2OTc0MjhhZDA3ZjBhMDhkMGY4NzJjOTYyMDJlNDQyY2VjOWI3ZjU5ODA4NjRmIiwiaWF0IjoxNzIyMTUxOTYyLjQ4MzMzLCJuYmYiOjE3MjIxNTE5NjIuNDgzMzMzLCJleHAiOjMzMjc5MDYwNzYyLjQ4MTI0Nywic3ViIjoiNzYxNjA4NzgiLCJpc3MiOiJodHRwczovL21ldGEud2lraW1lZGlhLm9yZyIsInJhdGVsaW1pdCI6eyJyZXF1ZXN0c19wZXJfdW5pdCI6NTAwMCwidW5pdCI6IkhPVVIifSwic2NvcGVzIjpbImJhc2ljIl19.GGsbCt6ZduGdR-51VC8B1bCK1TAdfqm3YA8hm3Nqqkmp3abrflaSk5FHAs2ZWXtb9lSJOOAlNXrlgWad9TE5Xdh-qR5I8N83-bzNGsq86irUp9LNr8ObqyXLrmzhkhZp5Fj7XhcdJsnqebp2HesSAD40TLOa2z_ShvmxrvikUpTlsgSiL5uHGlF5vd-iJ7iJ1VQAiuHSmY_Tph5igRXu1G7U2FYbr6wd2lrj21IsyMNBShFbiJ2EpycxSssUXssdVQHuhzew5douvM6bXoM-K0RoNCjsEISsSCsYNFC1e18Go_e-8cC4oAVAv7UFf7JaXca6hJ7Hzo99FJmu5jKDgJzvHnkXXeMYfiNDbIYMwnw29wsU15XUP7fUd3Z9qERxOKIV4YpfLKqmHl1Agnh1YOcH12u2hBdI6HKpceMpzeHac2RJ7vfTA_aGqENeNg6MM1Q3bUGXd5TFGs-A-hr1oflzkdEUsmxfBm0siIZD7BZwQ12X8bj6Binc_pRzVKjdsc_etuPlGIQG25xA13Mot2Afy8e2uKHlLEFgNLbZubC13mGTdCi58TBcurNLcohW5o0qaBgq6lHUdbP-n-VGl7d_qX4iUlOVnhzpdWZ-OmCRL66mt61d98EIekzOLEA9LvQP7fPYmD51n8NDxNRygJfP4ROArFVpmICJGb7QD3Q',  
        'User-Agent': 'MyWikiApp (ablaze.coder@proton.me)'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
       

        data = response.json()
        events = data.get('events', []) + data.get('births', []) + data.get('deaths', [])
        return events
    else:
        return []

def events_view(request):
    form = DateForm()
    events = None

    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            events = fetch_events_from_wikipedia(date)

    return render(request, 'events/events.html', {'form': form, 'events': events})
