# ADJ In The House!
* Joseph Wu
* Anna Fang
* Diana Akhmedova

<br>

# DISCO:
## Predictions:
* We believe that this will not work because it doesn't request the argument before printing; might return memory address.
* args is from Flask.
* headers is from HTML.
* The webserver will return "Waaaa hooo HAAAH" when a form is submitted.

## Observations:
* A request object is the location of the Flask app.
    * ex: http://127.0.0.1:5000/auth?username=ADJ+In+The+House%21&sub1=Submit+Query
* The request argument is a ImmutableMultiDict([]), which stores the username and the submit button once inputted.
    * The username and sub1 are keys named from the HTML files.
    * The user inputs and "Submit Query" are the values.
    * request.args outputs the user's input for the username after the user submits it.
* The request headers include:
    * Host: 127.0.0.1:5000
    * User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0
    * Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
    * Accept-Language: en-US,en;q=0.5
    * Accept-Encoding: gzip, deflate, br
    * Connection: keep-alive
    * Referer: http://127.0.0.1:5000/
    * Upgrade-Insecure-Requests: 1
    * Sec-Fetch-Dest: document
    * Sec-Fetch-Mode: navigate
    * Sec-Fetch-Site: same-origin
    * Sec-Fetch-User: ?1
* GET retrieves information from the webserver.
* POST puts the HTML information on the webserver.

<br>

# QCC:
* Where did the "Submit Query" name come from that is displayed in the terminal and on the webserver?
* Are there any other type of methods besides GET and POST?
* Why does running the webserver still work without the GET and POST methods?
* What does "Upgrade-Insecure-Requests: 1" mean?
