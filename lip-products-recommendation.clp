	;;; WARDAH ada 16

(defrule Wardah​​ColorfitUltralightMatteLipstickKoreaEdition
	(brand wardah)
	(type lipstick)
	(powdery yes)
	(lightweight yes)
	(layered yes)
	=>
	(assert (product done))
	(printout t "Wardah​​ Colorfit Ultralight Matte Lipstick Korea Edition" crlf)
)

(defrule ColorfitUltralightMatteLipstick
	(brand wardah)
	(type lipstick)
(powdery yes)
	(matte yes)
	(lightweight yes)
	(smooth yes)
	(moisturizing yes)
	(dailyuse yes)	
	(layered yes)
	=>
	(assert (product done))
	(printout t "Colorfit Ultralight Matte Lipstick" crlf)
)

(defrule WardahLongLastingLipstick
	(brand wardah)
	(type lipstick)
(longlasting yes)
	(smooth yes)
	(moisturizing yes)
	=>
	(assert (product done))
	(printout t "Wardah Long Lasting Lipstick" crlf)
)

(defrule ExclusiveMatteLipstick
	(brand wardah)
	(type lipstick)
(matte yes)
	(smooth yes)
	=>
	(assert (product done))
	(printout t "Exclusive Matte Lipstick" crlf)
)
(defrule ExclusiveMoistLipstick
	(brand wardah)
	(type lipstick)
	(moisturizing yes)
	=>
	(assert (product done))
	(printout t "Exclusive Moist Lipstick" crlf)
)

(defrule IntenseMatteLipstick
	(brand wardah)
	(type lipstick)
	(matte yes)
	(moisturizing yes)
	(smooth yes)
	(creamy yes)
	=>
	(assert (product done))
	(printout t "Intense Matte Lipstick" crlf)
)

(defrule WardahExclusiveMatteLipCream
	(brand wardah)
	(type lipcream)
	(matte yes)
	(creamy yes)
	=>
	(assert (product done))
	(printout t "Wardah Exclusive Matte Lip Cream" crlf)
)

(defrule ColorfitVelvetMatteLipMousse
	(brand wardah)
	(type lipcream)
	(mousse yes)
	(smooth yes)
	(moisturizing yes)
	(matte yes)
	(longlasting yes)
	(transferproof yes)
	=>
	(assert (product done))
	(printout t "Colorfit Velvet Matte Lip Mousse" crlf)
)

(defrule WardahColorfitLastAllDayLipPaint
	(brand wardah)
	(type lipcream)
	(creamy yes)
	(transferproof yes)
	(longlasting yes)
	=>
	(assert (product done))
	(printout t "Wardah Colorfit Last All Day Lip Paint" crlf)
)

(defrule ColorfitFreshMatteLipInk
	(brand wardah)
	(type lipcream)
	(matte yes)
	(watery yes)
	=>
	(assert (product done))
	(printout t "Colorfit Fresh Matte Lip Ink" crlf)
)

(defrule WardahEverydayCheekAndLiptint
	(brand wardah)
	(type liptint)
	(moisturizing yes)
	=>
	(assert (product done))
	(printout t "Wardah Everyday Cheek & Liptint" crlf)
)

(defrule WardahLipBalmPicnicLimitedEdition
	(brand wardah)
	(type lipbalm)
	(uvprotection yes)
	(moisturizing yes)
	(creamy yes)
	(nonsticky yes)
	(longlasting yes)
	=>
	(assert (product done))
	(printout t "Wardah Lip Balm Picnic Limited Edition" crlf)
)

(defrule EverydayMoistureLipNutrition
	(brand wardah)
	(type lipbalm)
	(moisturizing yes)
	(creamy yes)
	(nonsticky yes)
	(longlasting yes)
	=>
	(assert (product done))
	(printout t "Everyday Moisture Lip Nutrition" crlf)
)

(defrule EverydayFruitySheerLipBalm
	(brand wardah)
	(type lipbalm)
	(moisturizing yes)
	(creamy yes)
	(nonsticky yes)
	(longlasting yes)
	=>
	(assert (product done))
	(printout t "Everyday Fruity Sheer Lip Balm" crlf)
)

(defrule WardahHydrogloss
	(brand wardah)
	(type lipbalm)
	(smooth yes)
	(moisturizing yes)
	(dailyuse yes)
	=>
	(assert (product done))
	(printout t "Wardah Hydrogloss" crlf)
)

(defrule WardahLipgloss
	(brand wardah)
	(type lipbalm)
	(moisturizing yes)
	(glossy yes)
	(smooth yes)
	(dailyuse yes)
	(layered yes)
	=>
	(assert (product done))
	(printout t "Wardah Lipgloss" crlf)
)


;;; MAKEOVER ada 17
(defrule MakeOverCreamyLustLipstick
	(brand makeover)
	(type lipstick)
	(creamy yes)
	(matte yes)
	=>
	(assert (product done))
	(printout t "Make Over Creamy Lust Lipstick" crlf)
)

(defrule MakeOverUltraHimatteLipstick
	(brand makeover)
	(type lipstick)
	(intense yes)
	(longlasting yes)
	=>
	(assert (product done))
	(printout t "Make Over Ultra Hi-Matte Lipstick" crlf)
)

(defrule MakeOverUltraShineLipstick
	(brand makeover)
	(type lipstick)
	(smooth yes)
	(glossy yes)
	=>
	(assert (product done))
	(printout t "Make Over Ultra Shine Lipstick" crlf)
)

(defrule MakeOverColorStickGlossCrayon
	(brand makeover)
	(type lipstick)
	(smooth yes)
	(moisturizing yes)
	(intense yes)
	(lightweight yes)
	(nonsticky yes)
	(crayon yes)
	=>
	(assert (product done))
	(printout t "Make Over Color Stick Gloss Crayon" crlf)
)






(defrule MakeOverColorHypnoseCreamyLipmatte
	(brand makeover)
	(type lipstick)
	(matte yes)
	(intense yes)
	(lightweight yes)
	(nonsticky yes)
	(creamy yes)
	=>
	(assert (product done))
	(printout t "Make Over Color Hypnose Creamy Lipmatte" crlf)
)

(defrule MakeOverCliquematteLipStylo
	(brand makeover)
	(type lipstick)
	(matte yes)
	(clickpen yes)
	=>
	(assert (product done))
	(printout t "Make Over Cliquematte Lip Stylo" crlf)
)

(defrule MakeOverColorStickMatteCrayon
	(brand makeover)
	(type lipstick)
	(crayon yes)
	(smooth yes)
	(matte yes)
	(transferproof yes)
	(intense yes)
	=>
	(assert (product done))
	(printout t "Make Over Color Stick Matte Crayon" crlf)
)

(defrule MakeOverPowerstayTransferproofMatteLipCream
	(brand makeover)
	(type lipcream)
	(transferproof yes)
	(matte yes)
	(longlasting yes)
	=>
	(assert (product done))
	(printout t "Make Over Powerstay Transferproof Matte Lip Cream" crlf)
)


(defrule MakeOverHydrastaySmoothLipWhip
	(brand makeover)
	(type lipcream)
	(cream yes)
	(matte yes)
	(intense yes)
	(powdery yes)
	=>
	(assert (product done))
	(printout t "Make Over Hydrastay Smooth Lip Whip" crlf)
)

(defrule MakeOverIntenseMatteLipCream
	(brand makeover)
	(type lipcream)
	(matte yes)
	(intense yes)
	(longlasting yes)
	=>
	(assert (product done))
	(printout t "Make Over Intense Matte Lip Cream" crlf)
)

(defrule MakeOverIntenseMetallicLipCream
	(brand makeover)
	(type lipcream)
	(intense yes)
	(creamy yes)
	=>
	(assert (product done))
	(printout t "Make Over Intense Metallic Lip Cream" crlf)
)

(defrule MakeOverPowerstayVividWaterlineLipStain
	(brand makeover)
	(type lipcream)
	(intense yes)
	(lightweight yes)
	(longlasting yes)
	=>
	(assert (product done))
	(printout t "Make Over Powerstay Vivid Waterline Lip Stain" crlf)
)






(defrule MakeOverLiquidLipColor
	(brand makeover)
	(type lipcream)
	(soft yes)
	(moisturizing yes)
	(longlasting yes)
	=>
	(assert (product done))
	(printout t "Make Over Liquid Lip Color" crlf)
)

(defrule MakeOverLipAmplifyContourLiner
	(brand makeover)
	(type lippencil)
	(layered yes)
	(matte yes)
	(lightweight yes)
	=>
	(assert (product done))
	(printout t "Make Over Lip Amplify Contour Liner" crlf)
)

(defrule MakeOverCreamyLipGloss
	(brand makeover)
	(type lipgloss)
	(creamy yes)
	(moisturizing yes)
	=>
	(assert (product done))
	(printout t "Make Over Creamy Lip Gloss" crlf)
)

(defrule MakeOverPowerstayGlossyLipTopCoat
	(brand makeover)
	(type lipgloss)
	(glossy yes)
	(layered yes)
	(nonsticky yes)
	(lightweight yes)
	=>
	(assert (product done))
	(printout t "Make Over Powerstay Glossy Lip Top Coat" crlf)
)



(defrule MakeOverPowerstayGlossyLipTopCoat
	(brand makeover)
	(type lipbalm)
	(moisturizing yes)
	(dailyuse yes)
	(uvprotection yes)
	=>
	(assert (product done))
	(printout t "Make Over Powerstay Glossy Lip Top Coat" crlf)
)
;;; EMINA ada 14
(defrule PoppinMatteLipCream
	(brand emina)
	(type lipmatte)
	(creamy yes)
	(matte yes)
	(longlasting yes)
	(nonsticky yes)
	=>
	(assert (product done))
	(printout t "Emina Poppin Matte Lip Cream" crlf)
)

(defrule SqueezeMeUpLipMatte
	(brand emina)
	(type lipmatte)
	(lightweight yes)
	(smooth yes)
	(moisturizing yes)
	=>
	(assert (product done))
	(printout t "Emina Squeeze Me Up Lip Matte" crlf)
)

(defrule SqueezeMeUpLipMatte
	(brand emina)
	(type lipmatte)
	(lightweight yes)
	(smooth yes)
	(moisturizing yes)
	=>
	(assert (product done))
	(printout t "Emina Squeeze Me Up Lip Matte" crlf)
)

(defrule SqueezeMeUpLipGlass
	(brand emina)
	(type lipgloss)
	(glossy yes)
	(lightweight yes)
	(nonsticky yes)
	(moisturizing yes)
	=>
	(assert (product done))
	(printout t "Emina Squeeze Me Up Lip Glass" crlf)
)

(defrule SqueezeMeUpLipMatte
	(brand emina)
	(type lipgloss)
	(glossy yes)
	(dailyuse yes)
	(moisturizing yes)
	=>
	(assert (product done))
	(printout t "Emina Liquid Lip Shine" crlf)
)

(defrule OhSoKissableTintedBalmStick
	(brand emina)
	(type lipstick)
	(moisturizing yes)
	=>
	(assert (product done))
	(printout t "Emina Oh So Kissable Tinted Balm Stick" crlf)
)

(defrule Soulmatte
	(brand emina)
	(type lipstick)
	(matte yes)
	(intense yes)
	(moisturizing yes)
	=>
	(assert (product done))
	(printout t "Emina Soulmatte" crlf)
)

(defrule SugarRush
	(brand emina)
	(type lipstick)
	(creamy yes)
	(intense yes)
	(glossy yes)
	(moisturizing yes)
	=>
	(assert (product done))
	(printout t "Emina Sugar Rush" crlf)
)

(defrule LipCushion
	(brand emina)
	(type liquidlipstick)
	(fresh yes)
	(matte yes)
	(intense yes)
	(lightweight yes)
	=>
	(assert (product done))
	(printout t "Emina Lip Cushion" crlf)
)
(defrule CreamatteMetallicEdition
	(brand emina)
	(type liquidlipstick)
	(soft yes)
	(velvety yes)
	(matte yes)
	=>
	(assert (product done))
	(printout t "Emina Creamatte Metallic Edition" crlf)
)
(defrule Creamatte
	(brand emina)
	(type liquidlipstick)
	(matte yes)
	(intense yes)
	(soft yes)
	(velvety yes)
	(moisturizing yes)
	=>
	(assert (product done))
	(printout t "Emina Creamatte" crlf)
)

(defrule MagicPotion
	(brand emina)
	(type liptint)
	(watery yes)
	(semimatte yes)
	(dailyuse yes)
	=>
	(assert (product done))
	(printout t "Emina Magic Potion" crlf)
)
(defrule GlossyTint
	(brand emina)
	(type liptint)
	(glossy yes)
	(lightweight yes)
	(moisturizing yes)
	=>
	(assert (product done))
	(printout t "Emina Glossy Tint" crlf)
)

(defrule CreamyTint
	(brand emina)
	(type liptint)
	(smooth yes)
	(intense yes)
	(longlasting yes)
(lightweight yes)
	(moisturizing yes)
	(nonsticky yes)
	=>
	(assert (product done))
	(printout t "Emina Creamy Tint" crlf)
)

;;; INPUT
(defrule GetBrand
	(declare (salience 500))
	(not (product done))
=>
(printout t "Brand apa yang diinginkan?(wardah/makeover/emina): ")
(bind ?response (read))
(assert (brand ?response))
)

(defrule GetTypeWardah
	(declare (salience 300))
	(brand wardah)
	(not (product done))
=>
(printout t "Jenis produk apa yang diinginkan?(lipstick/lipcream/lipbalm/liptint): ")
(bind ?response (read))
(assert (type ?response))
)

(defrule GetTypeMakeover
	(declare (salience 300))
	(brand makeover)
	(not (product done))
=>
(printout t "Jenis produk apa yang diinginkan?(lipstick/lipcream/lipbalm/lippencil/lipgloss): ")
(bind ?response (read))
(assert (type ?response))
)

(defrule GetTypeEmina
	(declare (salience 300))
	(brand emina)
	(not (product done))
=>
(printout t "Jenis produk apa yang diinginkan?(lipstick/lipmatte/lipgloss/liptint/liquidlispstick): ")
(bind ?response (read))
(assert (type ?response))
)

(defrule GetDailyUse
	(not (product done))
=>
(printout t "Apakah Anda membutuhkan produk Daily Use?(yes/no): ")
(bind ?response (read))
(assert (dailyuse ?response))
)

(defrule GetLightweight
	(not (product done))
=>
(printout t "Apakah Anda membutuhkan produk yang ringan?(yes/no): ")
(bind ?response (read))
(assert (lightweight ?response))
)

(defrule GetPowdery
	(not (product done))
=>
(printout t "Apakah kamu menginginkan produk yang powdery?(yes/no): ")
(bind ?response (read))
(assert (powdery ?response))
)

(defrule GetLayered
	(not (product done))
=>
(printout t "Apakah membutuhkan produk yang dapat digunakan dengan produk lain?(yes/no): ")
(bind ?response (read))
(assert (layered ?response))
)

(defrule GetSmooth
	(not (product done))
=>
(printout t "Apakah membutuhkan produk yang halus dan lembut? (yes/no): ")
(bind ?response (read))
(assert (smooth ?response))
)

(defrule GetCreamy
	(not (product done))
=>
(printout t "Apakah membutuhkan produk dengan tekstur creamy? (yes/no): ")
(bind ?response (read))
(assert (creamy ?response))
)

(defrule GetMoisturizing
	(not (product done))
=>
(printout t "Apakah membutuhkan produk yang melembabkan bibir? (yes/no): ")
(bind ?response (read))
(assert (moisturizing ?response))
)

(defrule GetLonglasting
	(not (product done))
=>
(printout t "Apakah membutuhkan produk yang tahan lama?(yes/no): ")
(bind ?response (read))
(assert (longlasting ?response))
)

(defrule GetTransferproof
	(not (product done))
=>
(printout t "Apakah membutuhkan produk yang transferproof?(yes/no): ")
(bind ?response (read))
(assert (transferproof ?response))
)

(defrule GetGlossy
	(not (product done))
=>
(printout t "Apakah membutuhkan produk dengan hasil akhir glossy? (yes/no): ")
(bind ?response (read))
(assert (glossy ?response))
)

(defrule GetIntense
	(not (product done))
=>
(printout t "Apakah membutuhkan produk yang high pigmented? (yes/no): ")
(bind ?response (read))
(assert (intense ?response))
)

(defrule GetWatery
	(not (product done))

=>
(printout t "Apakah membutuhkan produk yang mengandung bahan dasar air? (yes/no): ")
(bind ?response (read))
(assert (watery ?response))

)

(defrule GetNonSticky
	(not (product done))
=>
(printout t "Apakah membutuhkan produk yang tidak lengket? (yes/no): ")
(bind ?response (read))
(assert (nonsticky ?response))
)

(defrule GetMousse
	(not (product done))
=>
(printout t "Apakah membutuhkan produk yang memberi hasil mousse? (yes/no): ")
(bind ?response (read))
(assert (mousse ?response))
)

(defrule GetUVProtection
	(type lipbalm)
	(not (product done))
=>
(printout t "Apakah membutuhkan produk yang mengandung UV Protection?(yes/no): ")
(bind ?response (read))
(assert (uvprotection ?response))
)


(defrule GetCrayon
	(brand makeover)
	(not (product done))
=>
(printout t "Apakah membutuhkan produk yang berbentuk crayon?(yes/no): ")
(bind ?response (read))
(assert (crayon ?response))
)

(defrule GetClickPen
	(declare (salience 100))
	(brand makeover)
	(type lipstick)
(not (product done))


=>
(printout t "Apakah membutuhkan produk yang berbentuk clickpen?: (yes/no)")
(bind ?response (read))
(assert (clickpen ?response))
)

(defrule GetVelvety
	(declare (salience 100))
	(brand emina)
	(not (product done))

=>
(printout t "Apakah membutuhkan produk dengan hasil akhir velvety? (yes/no): ")
(bind ?response (read))
(assert (velvety ?response))
)

(defrule GetSemiMatte
	(brand emina)
	(type liptint)
(not (product done))

=>
(printout t "Apakah membutuhkan produk memiliki finish yang semi matte?(yes/no): ")
(bind ?response (read))
(assert (semimatte ?response))
)

(defrule GetMatte
	(or (type lipstick) (type lipcream) (type lipmatte))
(not (product done))
=>
(printout t "Apakah membutuhkan produk memiliki finish yang matte?(yes/no): ")
(bind ?response (read))
(assert (matte ?response))
)

(defrule PrintGreetings
	(declare (salience 1000))
(not (product done))
	=>
	(printout t"Selamat datang di Paragon Lip Products Recommendation Rule Based System!" crlf)
(printout t""  crlf)
)


(defrule None
	(declare (salience -100))
(not (product done))
	=>
	(printout t"Mohon maaf, tidak ada produk yang sesuai preferensimu" crlf)

)

