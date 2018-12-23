from flask import Flask, render_template
from vsearch import search4letters

app = Flask(__name__)

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to the search4letters website!')

app.run()
