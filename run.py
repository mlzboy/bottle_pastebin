#!/usr/bin/env python
#encoding=utf-8

from bottle import route, run,redirect,request
t=""
html="""
<html>
<title>life is tough,use python~</title>
<body>
<form name="form1" action="/" method="post">
<textarea name="t" cols="80" rows="25">%s</textarea>
<input type="submit" name="sub" value="save" />
</form>
</body>
</html>
"""
#@route('/',method=["POST","GET"])
@route('/',method=["POST"])
def index():
    global t,html
    t=request.POST.get("t")
    print t

    
    return html%t

@route('/')
def index():
    global t,html
    print t
    
    return html%t

run(host='localhost', port=8084)