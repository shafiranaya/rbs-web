from flask import Flask, render_template, request
from main import *
app = Flask(__name__)

# app.config['SECRET_KEY'] = 'shafira'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['POST'])
def test():
    # global lip_product
    # lip_product ="ugh"
    # engine = LipsProductRecommendation()
    # engine.reset()
    # engine.declare(
    #     Fact(brand="wardah"),
    #     Fact(type="lipstick"),
    #     Fact(powdery="yes"),
    #     Fact(lightweight="yes"),
    #     Fact(layered="yes")
    # )
    # engine.run()
    # print("Lip product:",lip_product)
    # print("FACTS:\n",engine.facts)
    brand_input = request.form.get("brand")
    type_input = request.form.get("product_type")
    powdery_input = request.form.get("powdery")
    lightweight_input = request.form.get("lightweight")
    layered_input = request.form.get("layered")

    global lip_product
    lip_product = get_recommendation(brand_input,type_input,powdery_input,lightweight_input,layered_input)
    return render_template('index.html',result=lip_product)

# @app.route("/get")
# # fungsi untuk mendapatkan response dari bot
# def get_bot_response():
#     userText = request.args.get('msg')
#     return detect_fitur.get_bot_response(userText)

if __name__ == "__main__":
    app.run(debug=True)