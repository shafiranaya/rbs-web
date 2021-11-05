from os import popen
from experta import *

class LipsProductRecommendation(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        # TODO initialnya di set lip_product = ""
        global lip_product
        yield Fact(initial="yes")
        # yield Fact(product="not done")
        lip_product = ""
    
    # TODO urusin initial
    # @Rule(
    #     Fact(initial="yes"),
    #     NOT(Fact(product="done"))
    # )
    # def Initial(self):
    #     lip_product = ""
    ### WARDAH

    @Rule(
        Fact(brand="wardah"),
        Fact(type="lipstick"),
        Fact(powdery="yes"),
        Fact(lightweight="yes"),
        Fact(layered="yes")
    )
    def WardahColorfitUltralightMatteLipstickKoreaEdition(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Wardah​​ Colorfit Ultralight Matte Lipstick Korea Edition"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="lipstick"),
        Fact(powdery="yes"),
        Fact(matte="yes"),
        Fact(lightweight="yes"),
        Fact(smooth="yes"),
        Fact(moisturizing="yes"),
        Fact(dailyuse="yes"),
        Fact(layered="yes")
    )
    def ColorfitUltralightMatteLipstick(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Colorfit Ultralight Matte Lipstick"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="lipstick"),
        Fact(longlasting="yes"),
        Fact(smooth="yes"),
        Fact(moisturizing="yes")
    )
    def WardahLongLastingLipstick(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Wardah Long Lasting Lipstick"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="lipstick"),
        Fact(matte="yes"),
        Fact(smooth="yes")
    )
    def ExclusiveMatteLipstick(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Exclusive Matte Lipstick"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="lipstick"),
        Fact(moisturizing="yes")
    )
    def ExclusiveMoistLipstick(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Exclusive Moist Lipstick"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="lipstick"),
        Fact(matte="yes"),
        Fact(moisturizing="yes"),
        Fact(smooth="yes"),
        Fact(creamy="yes")
    )
    def IntenseMatteLipstick(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Intense Matte Lipstick"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="wardah"),
        Fact(type="lipcream"),
        Fact(matte="yes"),
        Fact(creamy="yes")
    )
    def WardahExclusiveMatteLipCream(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Wardah Exclusive Matte Lip Cream"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="lipcream"),
        Fact(mousse="yes"),
        Fact(smooth="yes"),
        Fact(moisturizing="yes"),
        Fact(matte="yes"),
        Fact(longlasting="yes"),
        Fact(transferproof="yes")
    )
    def ColorfitVelvetMatteLipMousse(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Colorfit Velvet Matte Lip Mousse"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="lipcream"),
        Fact(creamy="yes"),
        Fact(longlasting="yes"),
        Fact(transferproof="yes")
    )
    def WardahColorfitLastAllDayLipPaint(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Wardah Colorfit Last All Day Lip Paint"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="lipcream"),
        Fact(matte="yes"),
        Fact(watery="yes")
    )
    def ColorfitFreshMatteLipInk(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Colorfit Fresh Matte Lip Ink"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="liptint"),
        Fact(moisturizing="yes")
    )
    def WardahEverydayCheekAndLiptint(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Wardah Everyday Cheek And Liptint"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="liptint"),
        Fact(uvprotection="yes"),
        Fact(moisturizing="yes"),
        Fact(creamy="yes"),
        Fact(nonsticky="yes"),
        Fact(longlasting="yes")
    )
    def WardahLipBalmPicnicLimitedEdition(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Wardah Lip Balm Picnic Limited Edition"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="liptint"),
        Fact(moisturizing="yes"),
        Fact(creamy="yes"),
        Fact(nonsticky="yes"),
        Fact(longlasting="yes")
    )
    def EverydayMoistureLipNutrition(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Everyday Moisture Lip Nutrition"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="liptint"),
        Fact(moisturizing="yes"),
        Fact(creamy="yes"),
        Fact(nonsticky="yes"),
        Fact(longlasting="yes")
    )
    def EverydayFruitySheerLipBalm(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Everyday Fruity Sheer Lip Balm"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="liptint"),
        Fact(smooth="yes"),
        Fact(moisturizing="yes"),
        Fact(dailyuse="yes")
    )
    def WardahHydrogloss(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Wardah Hydrogloss"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="wardah"),
        Fact(type="liptint"),
        Fact(moisturizing="yes"),
        Fact(glossy="yes"),
        Fact(smooth="yes"),
        Fact(dailyuse="yes"),
        Fact(layered="yes")
    )
    def WardahLipgloss(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Wardah Lipgloss"
        self.declare(Fact(product="done"))
    
    ### MAKE OVER
    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipstick"),
        Fact(creamy="yes"),
        Fact(matte="yes")
    )
    def MakeOverCreamyLustLipstick(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Creamy Lust Lipstick"
        self.declare(Fact(product="done"))
        
    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipstick"),
        Fact(intense="yes"),
        Fact(longlasting="yes")
    )
    def MakeOverUltraHimatteLipstick(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Ultra Hi-Matte Lipstick"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipstick"),
        Fact(smooth="yes"),
        Fact(glossy="yes")
    )
    def MakeOverUltraShineLipstick(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Ultra Shine Lipstick"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipstick"),
        Fact(smooth="yes"),
        Fact(moisturizing="yes"),
        Fact(intense="yes"),
        Fact(lightweight="yes"),
        Fact(nonsticky="yes"),
        Fact(crayon="yes")
    )
    def MakeOverColorStickGlossCrayon(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Color Stick Gloss Crayon"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipstick"),
        Fact(matte="yes"),
        Fact(intense="yes"),
        Fact(lightweight="yes"),
        Fact(nonsticky="yes"),
        Fact(creamy="yes")
    )
    def MakeOverColorHypnoseCreamyLipmatte(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Color Hypnose Creamy Lipmatte"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipstick"),
        Fact(matte="yes"),
        Fact(clickpen="yes")
    )
    def MakeOverCliquematteLipStylo(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Cliquematte Lip Stylo"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipstick"),
        Fact(crayon="yes"),
        Fact(smooth="yes"),
        Fact(matte="yes"),
        Fact(transferproof="yes"),
        Fact(intense="yes"),
    )
    def MakeOverColorStickMatteCrayon(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Color Stick Matte Crayon"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipcream"),
        Fact(transferproof="yes"),
        Fact(matte="yes"),
        Fact(longlasting="yes")
    )
    def MakeOverPowerstayTransferproofMatteLipCream(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Powerstay Transferproof Matte Lip Cream"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipcream"),
        Fact(cream="yes"),
        Fact(matte="yes"),
        Fact(intense="yes"),
        Fact(powdery="yes")
    )
    def MakeOverHydrastaySmoothLipWhip(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Hydrastay Smooth Lip Whip"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipcream"),
        Fact(matte="yes"),
        Fact(intense="yes"),
        Fact(longlasting="yes")
    )
    def MakeOverIntenseMatteLipCream(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Intense Matte Lip Cream"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipcream"),
        Fact(intense="yes"),
        Fact(creamy="yes")
    )
    def MakeOverIntenseMetallicLipCream(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Intense Metallic Lip Cream"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipcream"),
        Fact(intense="yes"),
        Fact(lightweight="yes"),
        Fact(longlasting="yes")
    )
    def MakeOverPowerstayVividWaterlineLipStain(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Powerstay Vivid Waterline Lip Stain"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipcream"),
        Fact(soft="yes"),
        Fact(moisturizing="yes"),
        Fact(longlasting="yes")
    )
    def MakeOverLiquidLipColor(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Liquid Lip Color"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="makeover"),
        Fact(type="lippencil"),
        Fact(layered="yes"),
        Fact(matte="yes"),
        Fact(lightweight="yes")
    )
    def MakeOverLipAmplifyContourLiner(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Lip Amplify Contour Liner"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipgloss"),
        Fact(creamy="yes"),
        Fact(moisturizing="yes")
    )
    def MakeOverCreamyLipGloss(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Creamy Lip Gloss"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipgloss"),
        Fact(layered="yes"),
        Fact(glossy="yes"),
        Fact(nonsticky="yes"),
        Fact(lightweight="yes")
    )
    def MakeOverPowerstayGlossyLipTopCoat(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Powerstay Glossy Lip Top Coat"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="makeover"),
        Fact(type="lipbalm"),
        Fact(moisturizing="yes"),
        Fact(dailyuse="yes"),
        Fact(uvprotection="yes")
    )
    def MakeOverLipBalmLipNutrition(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Make Over Lip Balm Lip Nutrition"
        self.declare(Fact(product="done"))

    ### EMINA 
    
    @Rule(
        Fact(brand="emina"),
        Fact(type="lipmatte"),
        Fact(creamy="yes"),
        Fact(matte="yes"),
        Fact(longlasting="yes"),
        Fact(nonsticky="yes")
    )
    def PoppinMatteLipCream(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Emina Poppin Matte Lip Cream"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="emina"),
        Fact(type="lipmatte"),
        Fact(lightweight="yes"),
        Fact(smooth="yes"),
        Fact(moisturizing="yes")
    )
    def SqueezeMeUpLipMatte(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Squeeze Me Up Lip Matte"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="emina"),
        Fact(type="lipgloss"),
        Fact(glossy="yes"),
        Fact(lightweight="yes"),
        Fact(nonsticky="yes"),
        Fact(moisturizing="yes")
    )
    def SqueezeMeUpLipGlass(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Squeeze Me Up Lip Glass"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="emina"),
        Fact(type="lipgloss"),
        Fact(glossy="yes"),
        Fact(dailyuse="yes"),
        Fact(moisturizing="yes")
    )
    def SqueezeMeUpLipShine(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Squeeze Me Up Lip Shine"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="emina"),
        Fact(type="lipstick"),
        Fact(moisturizing="yes")
    )
    def OhSoKissableTintedBalmStick(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Oh So Kissable Tinted Balm Stick"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="emina"),
        Fact(type="lipstick"),
        Fact(matte="yes"),
        Fact(intense="yes"),
        Fact(moisturizing="yes")
    )
    def Soulmatte(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Emina Soulmatte"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="emina"),
        Fact(type="lipstick"),
        Fact(creamy="yes"),
        Fact(intense="yes"),
        Fact(glossy="yes"),
        Fact(moisturizing="yes")
    )
    def SugarRush(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Emina Sugar Rush"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="emina"),
        Fact(type="liquidlipstick"),
        Fact(fresh="yes"),
        Fact(matte="yes"),
        Fact(intense="yes"),
        Fact(lightweight="yes")
    )
    def LipCushion(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Emina Lip Cushion"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="emina"),
        Fact(type="liquidlipstick"),
        Fact(soft="yes"),
        Fact(velvety="yes"),
        Fact(matte="yes")
    )
    def CreamatteMetallicEdition(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Emina Creamatte Metallic Edition"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="emina"),
        Fact(type="liquidlipstick"),
        Fact(matte="yes"),
        Fact(soft="yes"),
        Fact(velvety="yes"),
        Fact(moisturizing="yes")
    )
    def Creamatte(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Emina Creamatte"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="emina"),
        Fact(type="liptint"),
        Fact(watery="yes"),
        Fact(semimatte="yes"),
        Fact(dailyuse="yes")
    )
    def MagicPotion(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Emina Magic Potion"
        self.declare(Fact(product="done"))

    @Rule(
        Fact(brand="emina"),
        Fact(type="liptint"),
        Fact(glossy="yes"),
        Fact(moisturizing="yes"),
        Fact(lightweight="yes")
    )
    def GlossyTint(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Emina Glossy Tint"
        self.declare(Fact(product="done"))
    
    @Rule(
        Fact(brand="emina"),
        Fact(type="liptint"),
        Fact(smooth="yes"),
        Fact(intense="yes"),
        Fact(longlasting="yes"),
        Fact(lightweight="yes"),
        Fact(moisturizing="yes"),
        Fact(nonsticky="yes")
    )
    def CreamyTint(self):
        global lip_product
        # self.modify(engine.facts[0], product="done")
        # self.retract(0)
        lip_product = "Emina Creamy Tint"
        self.declare(Fact(product="done"))
    
    # If product not found
    @Rule(
        NOT(Fact(product="done"))
    )
    def ProductNotFound(self):
        global lip_product
        lip_product = ""
        # lip_product = "Tidak ada produk yang sesuai dengan preferensimu"

# (defrule None
# 	(declare (salience -100))
# (not (product done))
# 	=>
# 	(printout t"Mohon maaf, tidak ada produk yang sesuai preferensimu" crlf)

# )
def get_product(
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
):
    global lip_product
    lip_product = ""
    engine = LipsProductRecommendation()
    engine.reset()
    engine.declare(
        Fact(brand=brand_input),
        Fact(type=type_input),
        Fact(dailyuse=dailyuse_input),
        Fact(lightweight=lightweight_input),
        Fact(powdery=powdery_input),
        Fact(smooth=smooth_input),
        Fact(creamy=creamy_input),
        Fact(moisturizing=moisturizing_input),
        Fact(longlasting=longlasting_input),
        Fact(transferproof=transferproof_input),
        Fact(glossy=glossy_input),
        Fact(intense=intense_input),
        Fact(watery=watery_input),
        Fact(nonsticky=nonsticky_input),
        Fact(mousse=mousse_input),
        Fact(uvprotection=uvprotection_input),
        Fact(crayon=crayon_input),
        Fact(clickpen=clickpen_input),
        Fact(velvety=velvety_input),
        Fact(matte=matte_input),
        Fact(semimatte=semimatte_input)
    )
    engine.run()
    # if (lip_product != ""):
    #     submitted = True
    # else:
    #     submitted = False
    return lip_product

def get_recommendation(brand_input,type_input,powdery_input,lightweight_input,layered_input):
    global lip_product
    lip_product =""
    engine = LipsProductRecommendation()
    engine.reset()
    engine.declare(
        Fact(brand=brand_input),
        Fact(type=type_input),
        Fact(powdery=powdery_input),
        Fact(lightweight=lightweight_input),
        Fact(layered=layered_input)
    )
    engine.run()
    print(lip_product)
    print(engine.facts)

    return lip_product

# hasil = get_recommendation()
hasil = get_recommendation("wardah","lipstick","yes","yes","yes")
print("HASIL: ",hasil)