from flask import Flask, render_template

app = Flask(__name__, static_folder="./images")

products =[
     {'nombre':'playera de jojo', 'talla':'mediana','costo':349,'img':'./images/jojo.jpg','discounted':True, 'cantidad_descuento':50},
     {'nombre':'playera de jojo eyes of heaven', 'talla':'grande','costo':500,'img':'./images/j2.jpg','discounted':True, 'cantidad_descuento':200},
     {'nombre':'playera de saint seiya', 'talla':'grande','costo':450,'img':'./images/ss.jpg','discounted':True, 'cantidad_descuento':100},
     {'nombre':'playera indie', 'talla':'chica','costo':260,'img':'./images/bn.jpg','discounted':False}   
]

popular_products =[
    {'nombre':'playera de jojo', 'talla':'mediana','costo':349,'img':'./images/jojo.jpg','discounted':True, 'cantidad_descuento':50},
    {'nombre':'playera de jojo eyes of heaven', 'talla':'grande','costo':500,'img':'./images/j2.jpg','discounted':True, 'cantidad_descuento':200},
     {'nombre':'playera de saint seiya', 'talla':'grande','costo':450,'img':'./images/ss.jpg','discounted':True, 'cantidad_descuento':100}
]


@app.route('/')
def inicio():
    return render_template('index.html',products = products)

@app.route('/contenido')
def contenido():
    return render_template('contenido.html',popular_products = popular_products)

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')      

if __name__ == '__main__':
    app.run(debug=True, port=5069)       