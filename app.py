from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters from the request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week
    current_day = datetime.datetime.now().strftime("%A")

    # Get the current UTC time with validation of +/-2 minutes
    utc_time = datetime.datetime.now(pytz.UTC)
    utc_time_str = utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Construct GitHub URLs based on your repository and file names
    github_repo_url = "https://github.com/username/repo"
    github_file_url = f"{github_repo_url}/blob/main/file_name.ext"

    # Create the response JSON
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time_str,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
