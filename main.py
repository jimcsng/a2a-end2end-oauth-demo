import os
import google_auth_oauthlib.flow

# --- OAuth 2.0 Configuration ---
# This variable specifies the name of a file that contains the OAuth 2.0
# client secret information for your application, including your client_id and
# client_secret. You can acquire this file by creating a new client ID for
# a "Desktop application" in the Google API Console.
CLIENT_SECRETS_FILE = "client_secret.json"

# This is the scope of access you are requesting.
# For this example, we are requesting read-only access to Google Drive.
# You should specify the scopes required for the APIs your application needs to access.
# A full list of scopes can be found at:
# https://developers.google.com/identity/protocols/oauth2/scopes
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']


def get_oauth_token():
    """Authenticates the user and returns an OAuth 2.0 token."""
    # Create a flow instance to manage the OAuth 2.0 Authorization Grant Flow.
    # The CLIENT_SECRETS_FILE is used to identify the application requesting
    # access.
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES)

    # The run_local_server() method starts a local web server to handle the
    # authorization redirect. It will open a new browser window for the
    # user to log in and authorize the application.
    try:
        credentials = flow.run_local_server(port=10010)
    except OSError as e:
        if e.errno == 98: # Address already in use
            print("Warning: A local server for OAuth is already running.")
            # If a server is already running, you might need to handle this
            # case based on your application's logic. For this example,
            # we will attempt to reuse the existing flow.
            credentials = flow.run_console()
        else:
            raise

    # The credentials object contains the access token and other OAuth 2.0 details.
    print("\nOAuth token received successfully!")
    print(f"Access Token: {credentials.token}")
    print(f"Refresh Token: {credentials.refresh_token}")

    return credentials

if __name__ == '__main__':
    # Ensure the client secrets file exists.
    if not os.path.exists(CLIENT_SECRETS_FILE):
        print(
            "Error: The client secrets file 'client_secret.json' was not found.\n"
            "Please download it from the Google API Console and place it in the same directory as this script."
        )
    else:
        get_oauth_token()