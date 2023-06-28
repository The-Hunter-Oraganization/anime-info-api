from flask import Flask, render_template, redirect

import requests

app = Flask(__name__)

@app.route('/anime/info/<int:anime_id>')
def get_anime_info(anime_id):
    try:
        anilist_url = f'https://graphql.anilist.co'
        query = '''
        query ($id: Int) {
          Media (id: $id, type: ANIME) {
            id
            title {
              romaji
              english
              native
            }
            description (asHtml: false)
            coverImage {
              large
            }
            bannerImage
            studios(isMain: true) {
              edges {
                node {
                  name
                }
              }
            }
            genres
            episodes
            duration
            startDate {
              year
              month
              day
            }
            endDate {
              year
              month
              day
            }
            averageScore
          }
        }
        '''
        variables = {
            'id': anime_id
        }
        response = requests.post(anilist_url, json={'query': query, 'variables': variables})
        response.raise_for_status()
        data = response.json()

        anime_title = data['data']['Media']['title']['romaji']
        anime_synopsis = data['data']['Media']['description']
        anime_poster = data['data']['Media']['coverImage']['large']
        anime_thumbnail = data['data']['Media']['bannerImage']
        anime_english_name = data['data']['Media']['title']['english']
        anime_japanese_name = data['data']['Media']['title']['native']
        anime_studio = data['data']['Media']['studios']['edges'][0]['node']['name']
        anime_genre = ', '.join(data['data']['Media']['genres'])
        anime_episodes = data['data']['Media']['episodes']
        anime_episode_duration = data['data']['Media']['duration']
        anime_start_date = f"{data['data']['Media']['startDate']['year']}-{data['data']['Media']['startDate']['month']}-{data['data']['Media']['startDate']['day']}"
        anime_end_date = f"{data['data']['Media']['endDate']['year']}-{data['data']['Media']['endDate']['month']}-{data['data']['Media']['endDate']['day']}"
        anime_score = data['data']['Media']['averageScore']

        return render_template('anime_info.html', title=anime_title, synopsis=anime_synopsis,
                               poster=anime_poster, thumbnail=anime_thumbnail, english_name=anime_english_name,
                               japanese_name=anime_japanese_name, studio=anime_studio, genre=anime_genre,
                               episodes=anime_episodes, episode_duration=anime_episode_duration,
                               start_date=anime_start_date, end_date=anime_end_date, score=anime_score)
    except requests.exceptions.RequestException as e:
        return f'Error: {str(e)}'

@app.route('/json/info/<int:anime_id>')
def get_anime_info_json(anime_id):
    try:
        anilist_url = f'https://graphql.anilist.co'
        query = '''
        query ($id: Int) {
          Media (id: $id, type: ANIME) {
            id
            title {
              romaji
              english
              native
            }
            description (asHtml: false)
            coverImage {
              large
            }
            bannerImage
            studios(isMain: true) {
              edges {
                node {
                  name
                }
              }
            }
            genres
            episodes
            duration
            startDate {
              year
              month
              day
            }
            endDate {
              year
              month
              day
            }
            averageScore
          }
        }
        '''
        variables = {
            'id': anime_id
        }
        response = requests.post(anilist_url, json={'query': query, 'variables': variables})
        response.raise_for_status()
        data = response.json()

        return data
    except requests.exceptions.RequestException as e:
        return f'Error: {str(e)}'

@app.route('/')
def redirect_to_telegram():
    return render_template('documentation.html')

if __name__ == '__main__':
    app.run()
