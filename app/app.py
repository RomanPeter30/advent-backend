from . import create_app

app = create_app()


@app.route('/')
def index():  # put application's code here
    return "Hello World"

'''
@app.route('/createUser')
def index():  # put application's code here
    user = User(name='rpeter', point=0, tookPart=0)
    db.session.add(user)
    db.session.commit()
    return jsonify([{"id": user.id}])
'''

if __name__ == '__main__':
    app.run()
