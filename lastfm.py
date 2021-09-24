import requests
import json

API_BASE = "http://ws.audioscrobbler.com/2.0/"
APP_CONFIG = {  "api_key": "", 
                "api_user": "", 
                "api_result_limit": "10",
                "github_token": "",
                "gist_id": ""}

def getAppConfig():
    configuration = {"api_key": "", "api_user": "", "api_result_limit": "10"}
    #read from file
    try:
        config_file = open("app.config")
        configuration = json.load(config_file)
    except:
        print("Failed to read configuration")

    return configuration

def executeQuery(query):
    config = APP_CONFIG
    if config["api_user"] == "" or config["api_user"] == "":
        return {"error": True, "errorMessage": "Configuration Missing!\n Please ensure you update app.config" }

    try:
        query = API_BASE + query + f"&limit={config['api_result_limit']}&user={config['api_user']}&api_key={config['api_key']}"
        results = requests.get(query)
        return results.json()
    except:
        return {"error": True, "errorMessage": "There was a problem executing the query"}

def fetchTopTracks():
    query = "?method=user.gettoptracks&format=json&period=7day"
    results = executeQuery(query)
    if "error" in results and results["error"] == True:
        print(results["errorMessage"])
    else:
        tracks = []
        for track in results["toptracks"]["track"]:
            track_info = f"{track['name']} [{track['artist']['name']}] ({track['playcount']} plays)"
            tracks.append(track_info)
        content = "\n".join(tracks)
        writeToGist(content)

def writeToGist(content):
    headers = {"Authorization": f"token {APP_CONFIG['github_token']}"}
    try:
        request = requests.patch(f"https://api.github.com/gists/{APP_CONFIG['gist_id']}", data=json.dumps({"files":{"my weekly top tracks": {"content":content}}}),headers=headers) 
        print("Updated gist")
    except:
        print("Failed to update gist")

APP_CONFIG = getAppConfig()
fetchTopTracks()