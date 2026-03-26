import urllib.request
import os

# Links to the official pre-trained model files
urls = {
    "deploy.prototxt": "https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/deploy.prototxt",
    "mobilenet_iter_73000.caffemodel": "https://github.com/chuanqi305/MobileNet-SSD/raw/master/mobilenet_iter_73000.caffemodel"
}

for filename, url in urls.items():
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print("Done!")
    else:
        print(f"{filename} already exists.")