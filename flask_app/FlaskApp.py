from flask import Flask, jsonify, request



# name - имя текущ. модуля (проекта с кодом) питона


app = Flask(__name__)

client = app.test_client()

# GET
# POST
# PUT
# DELETE

@app.route('/', methods=['GET'])
def get_MainPage():
    return "Main page!"


@app.route('/hello', methods=['GET'])
def get_HelloWorld():
    return "Hello World"


movieList = [
    {
        'title': "The Lighthouse",
        'description': "The Lighthouse 2019 - best movie ever"
    },
    {
        'title': "Avengers",
        'description': "Avengers 2000-something - fine i guess"
    }
]


#
# @app.route('/', methods=['GET'])
# def get_HelloWordMain():
#     return "Main page!"


@app.route('/getlist', methods=['GET'])
def get_movieList():
    # return movieList[0]['title']
    return jsonify(movieList)



@app.route('/postlist', methods=['POST'])
def update_list():
    newMovie = request.json
    movieList.append(newMovie)
    print(movieList)
    return jsonify(movieList)
#
#
#
# http://127.0.0.1:5000/getWord?var=someWord



@app.route('/getText', methods=['GET'])
def get_Text():
    nameStr = request.args.get('name','not listed')

    age = request.args.get('age','not listed')
    return "Your name is: " + nameStr + " and your age: " + age



# @app.route('/getWord', methods=['GET'])
# def get_Word():
#     word = request.args.get('word','default word')
#     desc = request.args.get('desc','default description')
#     age = request.args.get('age','60')
#     return "Your word is: " + word + " and also: " + desc + " and age is: " + age
#
#
@app.route('/getAge', methods=['GET'])
def get_Age():
    age = int(request.args.get('age','0'))
    age +=20
    return "Через 20 лет вам будет: " + str(age)





if __name__ == '__main__':
    # app.run()
    # app.run(port=1111)
    app.run(port=5000)






