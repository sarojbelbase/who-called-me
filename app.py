from whocalledme import create_app
from whocalledme.models import *

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db}


if __name__ == '__main__':
    app.run()