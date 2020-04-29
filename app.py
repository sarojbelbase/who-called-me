from whocalledme import create_app, db, whooshee
from whocalledme.models import Extension, Company

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db,'whooshee':whooshee,'Extension':Extension,'Company':Company}


if __name__ == '__main__':
    app.run(debug=True)