Flying Karate Masters: Matthew Yee, Kevin Li, Joseph Wu
SoftDev
K19 -- Cookies
2022-11-03
time spent: 2 hours

DISCO
    - the methods parameter is ["GET"] by default
    - Forms have actions, which can be used to change the route
    - cookie will stay until you use session.pop on all data. 
        EX:
        session['username'] = request.form['username']
        session['password'] = request.form['password']

        session.pop('username')
        session.pop('password')
    - 'username' in session - returns a boolean of if username is in session
    - 'username' in request.form - returns a boolean of if username value is in forms
    - Accessing a page by just typing in the route counts as submitting a form with no arguments, via a GET request

QCC
    - A button without type="button" sends us back to the root page? 
        - Turns out that if specify type="button", it doesn't submit anything when pressed

    
        


