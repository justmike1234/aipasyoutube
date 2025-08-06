import json
from google_auth_oauthlib.flow import InstalledAppFlow

# YouTube API scope
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json',
        scopes=SCOPES
    )
    creds = flow.run_local_server(port=8080, prompt='consent', authorization_prompt_message="")
    
    token_data = {
        "token": creds.token,
        "refresh_token": creds.refresh_token,
        "token_uri": creds.token_uri,
        "client_id": creds.client_id,
        "client_secret": creds.client_secret,
        "scopes": creds.scopes
    }

    with open('youtube_token.json', 'w') as token_file:
        json.dump(token_data, token_file, indent=4)
    
    print("\n✅ Refresh token saved to youtube_token.json")

if __name__ == '__main__':
    main()
