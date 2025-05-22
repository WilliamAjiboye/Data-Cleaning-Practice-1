import time
import requests
from dotenv import load_dotenv
import os
import pandas as pd
from tqdm import tqdm

# Load API key
load_dotenv('secrets.env')
key = os.getenv('API_KEY')

# Base URLs
BASE_URL_MOVIE = "https://api.themoviedb.org/3/movie"
BASE_URL_TV = "https://api.themoviedb.org/3/tv"
SEARCH_URL_MOVIE = f"{BASE_URL_MOVIE}/search/movie"
SEARCH_URL_TV = f"{BASE_URL_TV}/search/tv"

# Caches to avoid redundant API calls
movie_id_cache = {}
series_id_cache = {}

def get_id(title, type_):
    if type_ == 'Movie':
        if title in movie_id_cache:
            return movie_id_cache[title]
        url = SEARCH_URL_MOVIE
    else:
        if title in series_id_cache:
            return series_id_cache[title]
        url = SEARCH_URL_TV

    try:
        response = requests.get(url, params={'api_key': key, 'query': title})
        response.raise_for_status()
        results = response.json().get('results', [])
        result_id = results[0].get('id', 'Not Available') if results else 'Not Available'
        if type_ == 'Movie':
            movie_id_cache[title] = result_id
        else:
            series_id_cache[title] = result_id
        return result_id
    except requests.RequestException:
        return 'Error'
    finally:
        time.sleep(0.25)

def get_credits(id_, type_):
    if id_ in ('Not Available', 'Error', None):
        return 'Not Available', 'Not Available'
    try:
        id_ = int(id_)
    except (ValueError, TypeError):
        return 'Not Available', 'Not Available'

    url = f"{BASE_URL_MOVIE}/{id_}/credits" if type_ == 'Movie' else f"{BASE_URL_TV}/{id_}/season/1/credits"

    try:
        response = requests.get(url, params={'api_key': key})
        response.raise_for_status()
        data = response.json()
        crew = data.get('crew', [])
        cast = data.get('cast', [])

        directors = [member['name'] for member in crew if 'director' in member.get('job', '').lower()]
        cast_names = [member['name'] for member in cast if member.get('name')]

        return ', '.join(cast_names) or 'Not Available', ', '.join(directors) or 'Not Available'
    except requests.RequestException:
        return 'Error', 'Error'
    finally:
        time.sleep(0.25)

def enrich_dataframe(dataframe):
    df = dataframe[dataframe.isnull().any(axis=1)].copy()
    mask = df['cast'].isna() | df['director'].isna()
    rows_to_process = df[mask]

    for index, row in tqdm(rows_to_process.iterrows(), total=rows_to_process.shape[0]):
        title = row.get('title')
        content_type = row.get('type')

        if pd.isna(title) or pd.isna(content_type):
            continue

        tmdb_id = get_id(title, content_type)
        cast, director = get_credits(tmdb_id, content_type)

        if pd.isna(row.get('cast')) and cast not in ('Not Available', 'Error'):
            df.at[index, 'cast'] = cast

        if pd.isna(row.get('director')) and director not in ('Not Available', 'Error'):
            df.at[index, 'director'] = director

    dataframe.loc[df.index, ['cast', 'director']] = df[['cast', 'director']]
    return dataframe
