#@imports


from flask import Flask,url_for
from flask import render_templates

#@app logics goes here

#@Home page....

@app.route('/Home')
def Home():
   return render_templates('index.html')

#@Blog page ...


@app.route('/Blogs')
def Blogs():
   return render_templates('blogs.html')
#@Services page ...

@app.route('/Services')
def Services():
   return render_templates('services.html')
#@project page ...


@app.route('/Projects')
def Projects():
   return render_templates('projects.html')


#@end ...

if _name_=="_name_":
