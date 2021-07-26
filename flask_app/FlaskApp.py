from flask import Flask, jsonify, request



# name - имя текущ. модуля (проекта с кодом) питона

app = Flask(__name__)

client = app.test_client()


movieList = [
    {
        'title': "The Lighthouse",
        'description': "Very important stuff"
    },
    {
        'title': "Avengers",
        'description': "Also very important stuff"
    }
]


@app.route('/getHelloWorld', methods=['GET'])
def get_HelloWord():
    return "Hello World!"

@app.route('/', methods=['GET'])
def get_HelloWordMain():
    return "Main page!"

@app.route('/getlist', methods=['GET'])
def get_list():
    return jsonify(movieList)


@app.route('/postlist', methods=['POST'])
def update_list():
    newMovie = request.json
    movieList.append(newMovie)
    return jsonify(movieList)


# http://127.0.0.1:5000/getWord?var=someWord

@app.route('/getWord', methods=['GET'])
def get_Word():
    var = request.args.get('word','default value')
    secondWord = request.args.get('desc','default value')
    secondWordWar = request.args.get('param','default value')
    # var = request.args.get('var', 'default value')
    return "Your word is: " + var + ", And also " + secondWord + " also " + secondWordWar


if __name__ == '__main__':
    app.run()
    # app.run(debug=True, port=5000)







