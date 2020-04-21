from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from whocalledme import db
from whocalledme.models import *

main = Blueprint('main', __name__)

@main.route('/')
def search_input():
    extensions= Extension.query.all()
    return render_template('input.html', extensions=extensions)