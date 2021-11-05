from flask import Flask, render_template, request
from main import *
app = Flask(__name__)

# app.config['SECRET_KEY'] = 'shafira'

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def index():
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
    dailyuse_input = request.form.get("dailyuse")
    lightweight_input = request.form.get("lightweight")
    powdery_input = request.form.get("powdery")
    layered_input = request.form.get("layered")
    smooth_input = request.form.get("smooth")
    creamy_input = request.form.get("creamy")
    moisturizing_input = request.form.get("moisturizing")
    longlasting_input = request.form.get("longlasting")
    transferproof_input = request.form.get("transferproof")
    glossy_input = request.form.get("glossy")
    intense_input = request.form.get("intense")
    watery_input = request.form.get("watery")
    nonsticky_input = request.form.get("nonsticky")
    mousse_input = request.form.get("mousse")
    uvprotection_input = request.form.get("uvprotection")
    
    # TODO kalo sempet bisa dijadiin satu get aja misal bentuk
    crayon_input = request.form.get("crayon")
    clickpen_input = request.form.get("clickpen")

    velvety_input = request.form.get("velvety")

    # TODO kalo sempet bisa dijadiin satu get aja misal finish
    matte_input = request.form.get("matte")
    semimatte_input = request.form.get("semimatte")

    global lip_product
    lip_product = get_product(
            brand_input,
            type_input,
            dailyuse_input,
            lightweight_input,
            powdery_input,
            smooth_input,
            creamy_input,
            moisturizing_input,
            longlasting_input,
            transferproof_input,
            glossy_input,
            intense_input,
            watery_input,
            nonsticky_input,
            mousse_input,
            uvprotection_input,
            crayon_input,
            clickpen_input,
            velvety_input,
            matte_input,
            semimatte_input
    )
    if request.method == 'POST':
        submitted = True
    else:
        submitted = False
    # lip_product = get_recommendation(brand_input,type_input,powdery_input,lightweight_input,layered_input)
    return render_template('index.html',result=lip_product, submitted=submitted)

# @app.route("/get")
# # fungsi untuk mendapatkan response dari bot
# def get_bot_response():
#     userText = request.args.get('msg')
#     return detect_fitur.get_bot_response(userText)

if __name__ == "__main__":
    app.run(debug=True)