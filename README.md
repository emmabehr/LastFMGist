# My Weekly Top Stats

A python script to fetch music stats from LastFM.

Currently gets my weekly top tracks played and updates a gist

app.config is used to store config data and should look like this:
{
    "api_key": "<LastFM api key here>",
    "api_user": "<LastFM username here>",
    "api_result_limit": "<Number of results to return>",
    "github_token": "<your github token here>",
    "gist_id": "<id of the gist to update>"
}

Python script can be run as a cron job or called manually

Inspired by [https://github.com/jacc/music-box]