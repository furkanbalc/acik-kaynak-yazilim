import requests 

url = "https://passwordinator.onrender.com/?len={lenght}"

response = requests.get(url)
data = response.get(url)
println(data)
