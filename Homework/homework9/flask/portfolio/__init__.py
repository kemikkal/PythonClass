from flask import Flask, render_template, request
app= Flask('portfolio')
from . import views
#creates a url
