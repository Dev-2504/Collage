import urllib.request

# URL of the web page
url = "https://www.example.com"

# Local file name to save
file_name = "downloaded_page.html"

# Download and save
urllib.request.urlretrieve(url, file_name)

print("Web page successfully downloaded and saved as", file_name)
