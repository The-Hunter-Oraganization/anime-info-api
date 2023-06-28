**Repository Name:** anime-info-api

**Description:**
The Anime Info API is a Flask-based web application that retrieves detailed information about anime from AniList using GraphQL. It provides endpoints to fetch anime information, including titles, descriptions, cover images, studio names, genres, episode details, start and end dates, and average scores. Additionally, it offers a JSON endpoint to directly access the anime data in JSON format. The API is designed to be easy to use and can be integrated into various applications or services that require anime-related data.

**Features:**
- Fetch detailed information about anime by ID
- Retrieve anime titles, descriptions, cover images, studio names, genres, episode details, start and end dates, and average scores
- JSON endpoint to directly access anime data in JSON format
- Error handling for failed API requests

**Usage:**
1. Clone the repository: `git clone https://github.com/soheru/anime-info-api.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the Flask application: `python app.py`
4. Access the API endpoints:
   - `/anime/info/<anime_id>`: Retrieve detailed information about a specific anime by ID.
   - `/json/info/<anime_id>`: Get the anime information in JSON format.
5. Integrate the API into your applications or services to fetch anime data programmatically.

**Contributing:**
Contributions to the Anime Info API are welcome! If you find any issues or have suggestions for improvements, please submit a pull request. Make sure to follow the contribution guidelines specified in the repository.

**License:**
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
