import webbrowser
import requests

rbc_url = 'https://www.dav-rbc.de/072/185829.php'
MAX_OPEN_WEBSITE = 5

# webbrowser.open(rbc_url)
i=0

while i <= 10:
    #Open Website in default browser MAX_OPEN_WEBSITE times
    j=1
    while j <= MAX_OPEN_WEBSITE:
        webbrowser.open(rbc_url)
        j=j+1
    #Send GET request and print time
    response = requests.get(rbc_url).elapsed.total_seconds()
    i=i+1
    print(response)

print ("Danke")