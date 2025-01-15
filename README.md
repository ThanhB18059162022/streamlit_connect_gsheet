# ref

- https://youtu.be/_G5f7og_Dpo?si=14W85w3bh9zqjQ1r
- https://github.com/Sven-Bo/google-sheets-data-entry-form-with-streamlit.git
- https://docs.streamlit.io/get-started/installation
- https://github.com/streamlit/gsheets-connection

- Go to your spreadsheet and share it with a client_email from the step above. Just like you do with any other Google account. If you don’t do this, you’ll get a gspread.exceptions.SpreadsheetNotFound exception when trying to access this spreadsheet from your application or a script.
- Inside streamlit/secrets.toml place service_account configuration from downloaded JSON file, in the following format (where gsheets is your st.connection name)

# .streamlit/secrets.toml

[connections.gsheets]
spreadsheet = "<spreadsheet-name-or-url>"
worksheet = "<worksheet-gid-or-folder-id>" # worksheet GID is used when using Public Spreadsheet URL, when usign service_account it will be picked as folder_id
type = "" # leave empty when using Public Spreadsheet URL, when using service_account -> type = "service_account"
project_id = ""
private_key_id = ""
private_key = ""
client_email = ""
client_id = ""
auth_uri = ""
token_uri = ""
auth_provider_x509_cert_url = ""
client_x509_cert_url = ""
