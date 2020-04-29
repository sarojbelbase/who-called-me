from flask import render_template, request, Blueprint
from whocalledme.main.utils import try_searching

main = Blueprint('main', __name__)

@main.route('/')
def search_input():
    return render_template('input.html')


@main.route('/result', methods=['GET'])
def search_result():
    if request.method == 'GET':
        query= str(request.args.get('number'))
        if query and len(query) == 10 and query.startswith('9') :
            return try_searching(query, query[:4])
        elif query and query.startswith('0'):
            return try_searching(query, query[:3])
        return render_template('result.html', query=query, result=None)