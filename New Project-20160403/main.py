import urllib
import json
response = urllib.urlopen("https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22YHOO%22%2C%22AAPL%22%2C%22GOOG%22%2C%22MSFT%22)%0A%09%09&format=json&diagnostics=true&env=http%3A%2F%2Fdatatables.org%2Falltables.env&callback=")
json1 = json.load( response)
#print json1
print type(json1)
#print json1.keys()
#print type(json1["query"])
#print json1["query"].keys()
print type(json1["query"]["results"])
print json1["query"]["results"].keys()
print type(json1["query"]["results"]["quote"])
print type(json1["query"]["results"]["quote"][0])
print json1["query"]["results"]["quote"][0].keys
print json1["query"]["results"]["quote"][0]["Name"]

