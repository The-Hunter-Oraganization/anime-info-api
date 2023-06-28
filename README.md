# Anime API

## Introduction
The Anime API is a RESTful web service built with Flask and Python. It allows users to retrieve information about anime using the AniList GraphQL API. The API provides endpoints to fetch anime details, such as title, synopsis, poster, genres, episodes, duration, start date, end date, and average score.

## Features
- Retrieve anime information by ID
- Fetch anime details including title, synopsis, poster, genres, episodes, duration, start date, end date, and average score

## Requirements
- Python 3.7 or above
- Flask
- Requests

## Installation
1. Clone the repository: `git clone https://github.com/soheru/anime-api.git`
2. Navigate to the project directory: `cd anime-api`
3. Install the dependencies: `pip install -r requirements.txt`

## Usage
1. Start the Flask server: `python app.py`
2. Access the API documentation at: [http://localhost:5000](http://localhost:5000)
3. Use the following endpoint to retrieve anime information:

   `GET /anime/info/{anime_id}`

   Replace `{anime_id}` with the ID of the anime you want to fetch.

## Example
To retrieve information about an anime with ID 123:

