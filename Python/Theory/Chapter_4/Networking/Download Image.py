import urllib.request

# Image no URL
image_url = "https://www.example.com/sample.jpg"

# Local file name jema image save karvu che
save_as = "downloaded_image.jpg"

# Download kari ne save karvo
urllib.request.urlretrieve(image_url, save_as)

print("Image successfully downloaded!")
