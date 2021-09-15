import requests
sources = {"LegitimateURLShortener.txt":"https://raw.githubusercontent.com/DandelionSprout/adfilt/master/LegitimateURLShortener.txt"}
for s in sources:
   req = requests.get(sources[s])
   f = open(s,"w")
   f.write(req.text)
   f.close()
