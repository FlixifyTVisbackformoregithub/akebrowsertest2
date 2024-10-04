from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual API Key and Search Engine ID
API_KEY = 'YOUR_GOOGLE_API_KEY'
SEARCH_ENGINE_ID = 'YOUR_SEARCH_ENGINE_ID'

@app.route('/')
def home():
    query = request.args.get('query')
    results = []

    if query:
        results = perform_google_search(query)

    return render_template('index.html', query=query, results=results)

def perform_google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}"
    response = requests.get(url)
    data = response.json()

    # Extracting the relevant information from the response
    results = []
    if 'items' in data:
        for item in data['items']:
            results.append({
                'title': item['title'],
                'link': item['link'],
                'snippet': item['snippet'],
            })

    return results

if __name__ == '__main__':
    app.run(debug=True)
