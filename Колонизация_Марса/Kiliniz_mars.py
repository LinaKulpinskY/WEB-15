from flask import Flask, url_for

app = Flask(__name__)




@app.route('/')
def index():
    return "<h1>Миссия Колонизация Марса<h1>"


@app.route('/index')
def index_2():
    return "<h1>И на Марсе будут яблони цвести!<h1>"


@app.route('/promotion')
def promotion():
    return (
        "<h1>Человечество вырастает из детства.<h1><h1>Человечеству мала одна планета.<h1><h1>Мы сделаем обитаемыми безжизненные пока планеты.<h1><h1>И начнем с Марса!<h1><h1>Присоединяйся!<h5>")


@app.route('/image_mars')
def image():
    return f'''<h1>Жди нас, Марс!<h1>
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" /><img src="{url_for('static', filename='img/mars.png')}" 
               alt="здесь должна была быть картинка, но не нашлась"><h2>вот она какая, красная планета<h2>'''

@app.route('/promotion_image')
def promotion_image():
    return f'''<h1>Жди нас, Марс!<h1>
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" /><img src="{url_for('static', filename='img/mars.png')}" 
               alt="здесь должна была быть картинка, но не нашлась"><h2>Человечество вырастает из детства.<h2><h2>Человечеству мала одна планета.<h2><h2>Мы сделаем обитаемыми безжизненные пока планеты.<h2><h2>И начнем с Марса!<h2><h2>Присоединяйся!<h2>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
