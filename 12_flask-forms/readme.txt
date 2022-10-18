Flying Karate Masters: Matthew Yee, Kevin Li, Joseph Wu
SoftDev
K12 -- Flask Forms + GET vs POST
2022-10-17
time spent: 0.5 hours

app.py notes:

request.args is used for GET requests, and request.form is used for POST requests. They are mutually exclusive
request.method can be used to determine what kind of request is being used.

login.html notes:

method is a perameter that can be used to specify a request type.


GET vs. POST:
POST excludes extra data from the URL, whereas GET does not.
