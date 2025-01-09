from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('is_ghost', 'false', path='/')  # Ensure the path is set correctly
    return resp


@app.route('/treasure')
def treasure():
    if request.cookies.get('is_ghost') == 'true':
        return render_template('treasure.html')
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
