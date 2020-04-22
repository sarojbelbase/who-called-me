from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from whocalledme import db
from whocalledme.models import Extension, Company

main = Blueprint('main', __name__)

@main.route('/')
def search_input():
    return render_template('input.html')


@main.route('/search', methods=['GET'])
def search_result():
    if request.method == 'GET':
        query= request.args.get('number')
        if query and len(query) == 10 and query.startswith('9'):
            stripthatdown = query[:4]
        elif query and query.startswith('0'):
            stripthatdown = query[:3]
        result = Extension.query.whooshee_search(stripthatdown, order_by_relevance=-1).first()
        return render_template('result.html', query=query, result=result)
    return render_template('input.html', query=query)