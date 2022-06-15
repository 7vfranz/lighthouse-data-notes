# Notes for Week 1 Day 3

### API - Readings
* application programming interface 
* dedicated URL that returns pure data rather than GUI 
* application - piece of software can be separated from environment
* e.g. log-in with account, paypal, weather, twitter bots, travel booking
* more e.g. automotive, web apps, streaming, retail giants, financial instutions
* useful for aggregating data

### XML - Readings
* extensive markup language - similar to html
* creates information formats and share structured data, currently being replaced by JSON
* sender, receiver, heading and message body - but does not anything, just info wrapped in tags
* simply carries data 
* no predifined tags - everything is made by the author of the doc 
* changing is easy with newer versions of xml
* all plain text format

### JSON
* JavaScript Object Notation, i.e. subset of JavaScript
* values are labeled - more readable
* often nested - and can be parsed by other languages
* unlike XML - has tag name at beginning of element, can have arrays
* very similar to a dict
* can just be an object {} or an array []

``` JSON
{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}
```

### Accessing APIs
#### Browser
* https://api.github.com/users/<your_user_name>
#### Postman
* See compass - straight forward gui
#### Terminal 
* curl https://api.github.com/users/<your_user_name>
``` bash
curl --request GET --url "https://api.foursquare.com/v3/places/search?ll=45.6387,-122.6615&radius=100" --header 'Accept: application/json' --header 'Authorization: '"$FOURSQUARE_API"''
```

#### Through Python
* Sample:
``` python
import os
import requests as re
api_key = os.environ.get('FOURSQUARE_API')
location = 'Toronto,Canada'
url = "https://api.foursquare.com/v3/places/search?near="+location
headers = {"Accept": "application/json"}
headers['Authorization'] = api_key
response = re.get(url,headers=headers)
print(response)
print(response.json())
```

### Types of API
* most important type is REST 
* [APItypes](https://www.decipherzone.com/blog-detail/Types-of-APIs)

##### Ownership types:
* open - no restriction, aka Public API 
* partner - requires specific rights or licenses to access, usually paid
* internal - aka Private API, used in internal systems
* composite - combines different data and service 

##### Communication levels:
* high-level - typically used in REST form - only performs in limited function
* low-level - more detailed, for sending real-time video or media 

##### Webservice APIs
* SOAP - uses xml, more security
* XML-RPC - older than SOAP - minimum bandwidth. RPC - remote procedure calls 
* JSON-RPC - json format
* REST - representational state transfer. more data driven. browser compatible
    * can use different data formats - plaintext, html, xml, json
    * single uniform interface
    * fewer security requirements, browser compatible, discoverable, scalable
    * doesn't store any state about client session on the server-side 'stateless'


### HTTP Requests
* [httpRequests](https://www.codecademy.com/article/http-requests)
* HyperText Transfer Protocol
* structures requests and responses over the internet
* transfers happen using TCP (transmission control protocol) 
* your computer is the 'client' requesting address to server via URL (Uniform Resource Locator)
* if get requests is ok - usually has 200 OK .. if not found 404 
* https - secured version allows encrypted data
* Analogy - http is language used to make a request from a client to a service/business. returns a product i.e. website

### More on REST and API 
* REST = design pattern for APIs, way to represent requests in a universal way. 
* when RESTful API is called - server transfers to the client (you) a representation of the state of the requested resource
* separate client-server, stateless, and cacheable
* can be in JSON, XML, HTML format of the web service 
* what you get from request depends on:
    * the URL, in otherwords the identifier, aka endpoint
    * the operation - in the form of HTTP method - common methods are GET (i.e. read), POST (i.e. update), PUT, DELETE

### Python Requests
* [requests](https://realpython.com/python-requests/)

* Difference between params and headers:
    * Parameters are actual data, Headers have 'meta info' 
    * HTTP auto decodes parameters
    * headers usually need to be manually encoded
    * headers are hidden, but parameters can be seen by end-users in the URL.

* some require authorization, must be specified with auth=

* Customizing Requests:
    * headers, authentication, query strings, message bodies 

* SSL certificate verification - for more security 

* For making code more efficient/resilient, add to get requests
    * Timeout - can be set up to timeout- timeout=1 - stops after 1 second 
    * session Object - useful for making multiple reuests with the same authentication 
    * Max Retries - can retry connection before reaising a ConnectioNErro 
--------------------------------

## Lecture 

### API
* application programming interface 
* dedicated URL that returns pure data rather than GUI 
* programmer-friendly version of websites
* better for extracting data 
* e.g. [translinkAPI](https://www.translink.ca/about-us/doing-business-with-translink/app-developer-resources/rtti#stops)

* will enter a URL with given API key
* usually prefer to extract with JSON 

#### From command line 
* use curl <link>
* usually gets in JSON

#### Using postman 
* stores your API key
* specifies keys and values
* saves past api calls 

#### Using python
* import requests
* import os
* apikey = os.environ.get('API_KEY')
* response = requests.get(api_endpoint_url,params = {}, header=)

