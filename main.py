from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('Accueil.html')
@app.route("/Bulbasaur")
def Bulbasaur():
    return render_template("/pokedex/Bulbasaur.html")

@app.route("/Ivysaur")
def Ivysaur():
    return render_template("/pokedex/Ivysaur.html")

@app.route("/Venusaur")
def Venusaur():
    return render_template("/pokedex/Venusaur.html")

@app.route("/VenusaurMega")
def VenusaurMega():
    return render_template("/pokedex/VenusaurMega.html")

@app.route("/VenusaurGigantamax")
def VenusaurGigantamax():
    return render_template("/pokedex/VenusaurGigantamax.html")

@app.route("/Charmander")
def Charmander():
    return render_template("/pokedex/Charmander.html")

@app.route("/Charmeleon")
def Charmeleon():
    return render_template("/pokedex/Charmeleon.html")

@app.route("/Charizard")
def Charizard():
    return render_template("/pokedex/Charizard.html")

@app.route("/CharizardMegaX")
def CharizardMegaX():
    return render_template("/pokedex/CharizardMegaX.html")

@app.route("/CharizardMegaY")
def CharizardMegaY():
    return render_template("/pokedex/CharizardMegaY.html")

@app.route("/CharizardGigantamax")
def CharizardGigantamax():
    return render_template("/pokedex/CharizardGigantamax.html")

@app.route("/Squirtle")
def Squirtle():
    return render_template("/pokedex/Squirtle.html")

@app.route("/Wartortle")
def Wartortle():
    return render_template("/pokedex/Wartortle.html")

@app.route("/Blastoise")
def Blastoise():
    return render_template("/pokedex/Blastoise.html")

@app.route("/BlastoiseMega")
def BlastoiseMega():
    return render_template("/pokedex/BlastoiseMega.html")

@app.route("/BlastoiseGigantamax")
def BlastoiseGigantamax():
    return render_template("/pokedex/BlastoiseGigantamax.html")

@app.route("/Caterpie")
def Caterpie():
    return render_template("/pokedex/Caterpie.html")

@app.route("/Metapod")
def Metapod():
    return render_template("/pokedex/Metapod.html")

@app.route("/Butterfree")
def Butterfree():
    return render_template("/pokedex/Butterfree.html")

@app.route("/ButterfreeGigantamax")
def ButterfreeGigantamax():
    return render_template("/pokedex/ButterfreeGigantamax.html")

@app.route("/Weedle")
def Weedle():
    return render_template("/pokedex/Weedle.html")

@app.route("/Kakuna")
def Kakuna():
    return render_template("/pokedex/Kakuna.html")

@app.route("/Beedrill")
def Beedrill():
    return render_template("/pokedex/Beedrill.html")

@app.route("/BeedrillMega")
def BeedrillMega():
    return render_template("/pokedex/BeedrillMega.html")

@app.route("/Pidgey")
def Pidgey():
    return render_template("/pokedex/Pidgey.html")

@app.route("/Pidgeotto")
def Pidgeotto():
    return render_template("/pokedex/Pidgeotto.html")

@app.route("/Pidgeot")
def Pidgeot():
    return render_template("/pokedex/Pidgeot.html")

@app.route("/PidgeotMega")
def PidgeotMega():
    return render_template("/pokedex/PidgeotMega.html")

@app.route("/Rattata")
def Rattata():
    return render_template("/pokedex/Rattata.html")

@app.route("/RattataAlola")
def RattataAlola():
    return render_template("/pokedex/RattataAlola.html")

@app.route("/Raticate")
def Raticate():
    return render_template("/pokedex/Raticate.html")

@app.route("/RaticateAlola")
def RaticateAlola():
    return render_template("/pokedex/RaticateAlola.html")

@app.route("/Spearow")
def Spearow():
    return render_template("/pokedex/Spearow.html")

@app.route("/Fearow")
def Fearow():
    return render_template("/pokedex/Fearow.html")

@app.route("/Ekans")
def Ekans():
    return render_template("/pokedex/Ekans.html")

@app.route("/Arbok")
def Arbok():
    return render_template("/pokedex/Arbok.html")

@app.route("/Pikachu")
def Pikachu():
    return render_template("/pokedex/Pikachu.html")

@app.route("/PikachuGigantamax")
def PikachuGigantamax():
    return render_template("/pokedex/PikachuGigantamax.html")

@app.route("/PikachuStarter")
def PikachuStarter():
    return render_template("/pokedex/PikachuStarter.html")

@app.route("/Raichu")
def Raichu():
    return render_template("/pokedex/Raichu.html")

@app.route("/RaichuAlola")
def RaichuAlola():
    return render_template("/pokedex/RaichuAlola.html")

@app.route("/Sandshrew")
def Sandshrew():
    return render_template("/pokedex/Sandshrew.html")

@app.route("/SandshrewAlola")
def SandshrewAlola():
    return render_template("/pokedex/SandshrewAlola.html")

@app.route("/Sandslash")
def Sandslash():
    return render_template("/pokedex/Sandslash.html")

@app.route("/SandslashAlola")
def SandslashAlola():
    return render_template("/pokedex/SandslashAlola.html")

@app.route("/Nidoran_Female")
def Nidoran_Female():
    return render_template("/pokedex/Nidoran_Female.html")

@app.route("/Nidorina")
def Nidorina():
    return render_template("/pokedex/Nidorina.html")

@app.route("/Nidoqueen")
def Nidoqueen():
    return render_template("/pokedex/Nidoqueen.html")

@app.route("/Nidoran_Male")
def Nidoran_Male():
    return render_template("/pokedex/Nidoran_Male.html")

@app.route("/Nidorino")
def Nidorino():
    return render_template("/pokedex/Nidorino.html")

@app.route("/Nidoking")
def Nidoking():
    return render_template("/pokedex/Nidoking.html")

@app.route("/Clefairy")
def Clefairy():
    return render_template("/pokedex/Clefairy.html")

@app.route("/Clefable")
def Clefable():
    return render_template("/pokedex/Clefable.html")

@app.route("/Vulpix")
def Vulpix():
    return render_template("/pokedex/Vulpix.html")

@app.route("/VulpixAlola")
def VulpixAlola():
    return render_template("/pokedex/VulpixAlola.html")

@app.route("/Ninetales")
def Ninetales():
    return render_template("/pokedex/Ninetales.html")

@app.route("/NinetalesAlola")
def NinetalesAlola():
    return render_template("/pokedex/NinetalesAlola.html")

@app.route("/Jigglypuff")
def Jigglypuff():
    return render_template("/pokedex/Jigglypuff.html")

@app.route("/Wigglytuff")
def Wigglytuff():
    return render_template("/pokedex/Wigglytuff.html")

@app.route("/Zubat")
def Zubat():
    return render_template("/pokedex/Zubat.html")

@app.route("/Golbat")
def Golbat():
    return render_template("/pokedex/Golbat.html")

@app.route("/Oddish")
def Oddish():
    return render_template("/pokedex/Oddish.html")

@app.route("/Gloom")
def Gloom():
    return render_template("/pokedex/Gloom.html")

@app.route("/Vileplume")
def Vileplume():
    return render_template("/pokedex/Vileplume.html")

@app.route("/Paras")
def Paras():
    return render_template("/pokedex/Paras.html")

@app.route("/Parasect")
def Parasect():
    return render_template("/pokedex/Parasect.html")

@app.route("/Venonat")
def Venonat():
    return render_template("/pokedex/Venonat.html")

@app.route("/Venomoth")
def Venomoth():
    return render_template("/pokedex/Venomoth.html")

@app.route("/Diglett")
def Diglett():
    return render_template("/pokedex/Diglett.html")

@app.route("/DiglettAlola")
def DiglettAlola():
    return render_template("/pokedex/DiglettAlola.html")

@app.route("/DugtrioAlola")
def DugtrioAlola():
    return render_template("/pokedex/DugtrioAlola.html")

@app.route("/Dugtrio")
def Dugtrio():
    return render_template("/pokedex/Dugtrio.html")

@app.route("/Meowth")
def Meowth():
    return render_template("/pokedex/Meowth.html")

@app.route("/MeowthAlola")
def MeowthAlola():
    return render_template("/pokedex/MeowthAlola.html")

@app.route("/MeowthGalar")
def MeowthGalar():
    return render_template("/pokedex/MeowthGalar.html")

@app.route("/MeowthGigantamax")
def MeowthGigantamax():
    return render_template("/pokedex/MeowthGigantamax.html")

@app.route("/Persian")
def Persian():
    return render_template("/pokedex/Persian.html")

@app.route("/PersianAlola")
def PersianAlola():
    return render_template("/pokedex/PersianAlola.html")

@app.route("/Psyduck")
def Psyduck():
    return render_template("/pokedex/Psyduck.html")

@app.route("/Golduck")
def Golduck():
    return render_template("/pokedex/Golduck.html")

@app.route("/Mankey")
def Mankey():
    return render_template("/pokedex/Mankey.html")

@app.route("/Primeape")
def Primeape():
    return render_template("/pokedex/Primeape.html")

@app.route("/Growlithe")
def Growlithe():
    return render_template("/pokedex/Growlithe.html")

@app.route("/GrowlitheHisui")
def GrowlitheHisui():
    return render_template("/pokedex/GrowlitheHisui.html")

@app.route("/Arcanine")
def Arcanine():
    return render_template("/pokedex/Arcanine.html")

@app.route("/ArcanineHisui")
def ArcanineHisui():
    return render_template("/pokedex/ArcanineHisui.html")

@app.route("/Poliwag")
def Poliwag():
    return render_template("/pokedex/Poliwag.html")

@app.route("/Poliwhirl")
def Poliwhirl():
    return render_template("/pokedex/Poliwhirl.html")

@app.route("/Poliwrath")
def Poliwrath():
    return render_template("/pokedex/Poliwrath.html")

@app.route("/Abra")
def Abra():
    return render_template("/pokedex/Abra.html")

@app.route("/Kadabra")
def Kadabra():
    return render_template("/pokedex/Kadabra.html")

@app.route("/Alakazam")
def Alakazam():
    return render_template("/pokedex/Alakazam.html")

@app.route("/AlakazamMega")
def AlakazamMega():
    return render_template("/pokedex/AlakazamMega.html")

@app.route("/Machop")
def Machop():
    return render_template("/pokedex/Machop.html")

@app.route("/Machoke")
def Machoke():
    return render_template("/pokedex/Machoke.html")

@app.route("/Machamp")
def Machamp():
    return render_template("/pokedex/Machamp.html")

@app.route("/MachampGigantamax")
def MachampGigantamax():
    return render_template("/pokedex/MachampGigantamax.html")

@app.route("/Bellsprout")
def Bellsprout():
    return render_template("/pokedex/Bellsprout.html")

@app.route("/Weepinbell")
def Weepinbell():
    return render_template("/pokedex/Weepinbell.html")

@app.route("/Victreebel")
def Victreebel():
    return render_template("/pokedex/Victreebel.html")

@app.route("/Tentacool")
def Tentacool():
    return render_template("/pokedex/Tentacool.html")

@app.route("/Tentacruel")
def Tentacruel():
    return render_template("/pokedex/Tentacruel.html")

@app.route("/Geodude")
def Geodude():
    return render_template("/pokedex/Geodude.html")

@app.route("/GeodudeAlola")
def GeodudeAlola():
    return render_template("/pokedex/GeodudeAlola.html")

@app.route("/GravelerAlola")
def GravelerAlola():
    return render_template("/pokedex/GravelerAlola.html")

@app.route("/Graveler")
def Graveler():
    return render_template("/pokedex/Graveler.html")

@app.route("/Golem")
def Golem():
    return render_template("/pokedex/Golem.html")

@app.route("/GolemAlola")
def GolemAlola():
    return render_template("/pokedex/GolemAlola.html")

@app.route("/PonytaGalar")
def PonytaGalar():
    return render_template("/pokedex/PonytaGalar.html")

@app.route("/Ponyta")
def Ponyta():
    return render_template("/pokedex/Ponyta.html")

@app.route("/Rapidash")
def Rapidash():
    return render_template("/pokedex/Rapidash.html")

@app.route("/RapidashGalar")
def RapidashGalar():
    return render_template("/pokedex/RapidashGalar.html")

@app.route("/SlowpokeGalar")
def SlowpokeGalar():
    return render_template("/pokedex/SlowpokeGalar.html")

@app.route("/Slowpoke")
def Slowpoke():
    return render_template("/pokedex/Slowpoke.html")

@app.route("/SlowbroMega")
def SlowbroMega():
    return render_template("/pokedex/SlowbroMega.html")

@app.route("/SlowbroGalar")
def SlowbroGalar():
    return render_template("/pokedex/SlowbroGalar.html")

@app.route("/Slowbro")
def Slowbro():
    return render_template("/pokedex/Slowbro.html")

@app.route("/Magnemite")
def Magnemite():
    return render_template("/pokedex/Magnemite.html")

@app.route("/Magneton")
def Magneton():
    return render_template("/pokedex/Magneton.html")

@app.route("/Farfetchd")
def Farfetchd():
    return render_template("/pokedex/Farfetchd.html")

@app.route("/FarfetchdGalar")
def FarfetchdGalar():
    return render_template("/pokedex/FarfetchdGalar.html")

@app.route("/Doduo")
def Doduo():
    return render_template("/pokedex/Doduo.html")

@app.route("/Dodrio")
def Dodrio():
    return render_template("/pokedex/Dodrio.html")

@app.route("/Seel")
def Seel():
    return render_template("/pokedex/Seel.html")

@app.route("/Dewgong")
def Dewgong():
    return render_template("/pokedex/Dewgong.html")

@app.route("/Grimer")
def Grimer():
    return render_template("/pokedex/Grimer.html")

@app.route("/GrimerAlola")
def GrimerAlola():
    return render_template("/pokedex/GrimerAlola.html")

@app.route("/MukAlola")
def MukAlola():
    return render_template("/pokedex/MukAlola.html")

@app.route("/Muk")
def Muk():
    return render_template("/pokedex/Muk.html")

@app.route("/Shellder")
def Shellder():
    return render_template("/pokedex/Shellder.html")

@app.route("/Cloyster")
def Cloyster():
    return render_template("/pokedex/Cloyster.html")

@app.route("/Gastly")
def Gastly():
    return render_template("/pokedex/Gastly.html")

@app.route("/Haunter")
def Haunter():
    return render_template("/pokedex/Haunter.html")

@app.route("/Gengar")
def Gengar():
    return render_template("/pokedex/Gengar.html")

@app.route("/GengarGigantamax")
def GengarGigantamax():
    return render_template("/pokedex/GengarGigantamax.html")

@app.route("/GengarMega")
def GengarMega():
    return render_template("/pokedex/GengarMega.html")

@app.route("/Onix")
def Onix():
    return render_template("/pokedex/Onix.html")

@app.route("/Drowzee")
def Drowzee():
    return render_template("/pokedex/Drowzee.html")

@app.route("/Hypno")
def Hypno():
    return render_template("/pokedex/Hypno.html")

@app.route("/Krabby")
def Krabby():
    return render_template("/pokedex/Krabby.html")

@app.route("/Kingler")
def Kingler():
    return render_template("/pokedex/Kingler.html")

@app.route("/KinglerGigantamax")
def KinglerGigantamax():
    return render_template("/pokedex/KinglerGigantamax.html")

@app.route("/Voltorb")
def Voltorb():
    return render_template("/pokedex/Voltorb.html")

@app.route("/VoltorbHisui")
def VoltorbHisui():
    return render_template("/pokedex/VoltorbHisui.html")

@app.route("/Electrode")
def Electrode():
    return render_template("/pokedex/Electrode.html")

@app.route("/ElectrodeHisui")
def ElectrodeHisui():
    return render_template("/pokedex/ElectrodeHisui.html")

@app.route("/Exeggcute")
def Exeggcute():
    return render_template("/pokedex/Exeggcute.html")

@app.route("/Exeggutor")
def Exeggutor():
    return render_template("/pokedex/Exeggutor.html")

@app.route("/ExeggutorAlola")
def ExeggutorAlola():
    return render_template("/pokedex/ExeggutorAlola.html")

@app.route("/Cubone")
def Cubone():
    return render_template("/pokedex/Cubone.html")

@app.route("/Marowak")
def Marowak():
    return render_template("/pokedex/Marowak.html")

@app.route("/MarowakAlola")
def MarowakAlola():
    return render_template("/pokedex/MarowakAlola.html")

@app.route("/Hitmonlee")
def Hitmonlee():
    return render_template("/pokedex/Hitmonlee.html")

@app.route("/Hitmonchan")
def Hitmonchan():
    return render_template("/pokedex/Hitmonchan.html")

@app.route("/Lickitung")
def Lickitung():
    return render_template("/pokedex/Lickitung.html")

@app.route("/Koffing")
def Koffing():
    return render_template("/pokedex/Koffing.html")

@app.route("/Weezing")
def Weezing():
    return render_template("/pokedex/Weezing.html")

@app.route("/WeezingGalar")
def WeezingGalar():
    return render_template("/pokedex/WeezingGalar.html")

@app.route("/Rhyhorn")
def Rhyhorn():
    return render_template("/pokedex/Rhyhorn.html")

@app.route("/Rhydon")
def Rhydon():
    return render_template("/pokedex/Rhydon.html")

@app.route("/Chansey")
def Chansey():
    return render_template("/pokedex/Chansey.html")

@app.route("/Tangela")
def Tangela():
    return render_template("/pokedex/Tangela.html")

@app.route("/Kangaskhan")
def Kangaskhan():
    return render_template("/pokedex/Kangaskhan.html")

@app.route("/KangaskhanMega")
def KangaskhanMega():
    return render_template("/pokedex/KangaskhanMega.html")

@app.route("/Horsea")
def Horsea():
    return render_template("/pokedex/Horsea.html")

@app.route("/Seadra")
def Seadra():
    return render_template("/pokedex/Seadra.html")

@app.route("/Goldeen")
def Goldeen():
    return render_template("/pokedex/Goldeen.html")

@app.route("/Seaking")
def Seaking():
    return render_template("/pokedex/Seaking.html")

@app.route("/Staryu")
def Staryu():
    return render_template("/pokedex/Staryu.html")

@app.route("/Starmie")
def Starmie():
    return render_template("/pokedex/Starmie.html")

@app.route("/MrMime")
def MrMime():
    return render_template("/pokedex/MrMime.html")

@app.route("/MrMimeGalar")
def MrMimeGalar():
    return render_template("/pokedex/MrMimeGalar.html")

@app.route("/Scyther")
def Scyther():
    return render_template("/pokedex/Scyther.html")

@app.route("/Jynx")
def Jynx():
    return render_template("/pokedex/Jynx.html")

@app.route("/Electabuzz")
def Electabuzz():
    return render_template("/pokedex/Electabuzz.html")

@app.route("/Magmar")
def Magmar():
    return render_template("/pokedex/Magmar.html")

@app.route("/Pinsir")
def Pinsir():
    return render_template("/pokedex/Pinsir.html")

@app.route("/PinsirMega")
def PinsirMega():
    return render_template("/pokedex/PinsirMega.html")

@app.route("/Tauros")
def Tauros():
    return render_template("/pokedex/Tauros.html")

@app.route("/TaurosPaldeanCombatBreed")
def TaurosPaldeanCombatBreed():
    return render_template("/pokedex/TaurosPaldeanCombatBreed.html")

@app.route("/TaurosPaldeanBlazeBreed")
def TaurosPaldeanBlazeBreed():
    return render_template("/pokedex/TaurosPaldeanBlazeBreed.html")

@app.route("/TaurosPaldeanAquaBreed")
def TaurosPaldeanAquaBreed():
    return render_template("/pokedex/TaurosPaldeanAquaBreed.html")

@app.route("/Magikarp")
def Magikarp():
    return render_template("/pokedex/Magikarp.html")

@app.route("/Gyarados")
def Gyarados():
    return render_template("/pokedex/Gyarados.html")

@app.route("/GyaradosMega")
def GyaradosMega():
    return render_template("/pokedex/GyaradosMega.html")

@app.route("/Lapras")
def Lapras():
    return render_template("/pokedex/Lapras.html")

@app.route("/LaprasGigantamax")
def LaprasGigantamax():
    return render_template("/pokedex/LaprasGigantamax.html")

@app.route("/Ditto")
def Ditto():
    return render_template("/pokedex/Ditto.html")

@app.route("/Eevee")
def Eevee():
    return render_template("/pokedex/Eevee.html")

@app.route("/EeveeGigantamax")
def EeveeGigantamax():
    return render_template("/pokedex/EeveeGigantamax.html")

@app.route("/EeveeStarter")
def EeveeStarter():
    return render_template("/pokedex/EeveeStarter.html")

@app.route("/Vaporeon")
def Vaporeon():
    return render_template("/pokedex/Vaporeon.html")

@app.route("/Jolteon")
def Jolteon():
    return render_template("/pokedex/Jolteon.html")

@app.route("/Flareon")
def Flareon():
    return render_template("/pokedex/Flareon.html")

@app.route("/Porygon")
def Porygon():
    return render_template("/pokedex/Porygon.html")

@app.route("/Omanyte")
def Omanyte():
    return render_template("/pokedex/Omanyte.html")

@app.route("/Omastar")
def Omastar():
    return render_template("/pokedex/Omastar.html")

@app.route("/Kabuto")
def Kabuto():
    return render_template("/pokedex/Kabuto.html")

@app.route("/Kabutops")
def Kabutops():
    return render_template("/pokedex/Kabutops.html")

@app.route("/Aerodactyl")
def Aerodactyl():
    return render_template("/pokedex/Aerodactyl.html")

@app.route("/AerodactylMega")
def AerodactylMega():
    return render_template("/pokedex/AerodactylMega.html")

@app.route("/Snorlax")
def Snorlax():
    return render_template("/pokedex/Snorlax.html")

@app.route("/SnorlaxGigantamax")
def SnorlaxGigantamax():
    return render_template("/pokedex/SnorlaxGigantamax.html")

@app.route("/Articuno")
def Articuno():
    return render_template("/pokedex/Articuno.html")

@app.route("/ArticunoGalar")
def ArticunoGalar():
    return render_template("/pokedex/ArticunoGalar.html")

@app.route("/Zapdos")
def Zapdos():
    return render_template("/pokedex/Zapdos.html")

@app.route("/ZapdosGalar")
def ZapdosGalar():
    return render_template("/pokedex/ZapdosGalar.html")

@app.route("/Moltres")
def Moltres():
    return render_template("/pokedex/Moltres.html")

@app.route("/MoltresGalar")
def MoltresGalar():
    return render_template("/pokedex/MoltresGalar.html")

@app.route("/Dratini")
def Dratini():
    return render_template("/pokedex/Dratini.html")

@app.route("/Dragonair")
def Dragonair():
    return render_template("/pokedex/Dragonair.html")

@app.route("/Dragonite")
def Dragonite():
    return render_template("/pokedex/Dragonite.html")

@app.route("/Mewtwo")
def Mewtwo():
    return render_template("/pokedex/Mewtwo.html")

@app.route("/MewtwoMegaX")
def MewtwoMegaX():
    return render_template("/pokedex/MewtwoMegaX.html")

@app.route("/MewtwoMegaY")
def MewtwoMegaY():
    return render_template("/pokedex/MewtwoMegaY.html")

@app.route("/Mew")
def Mew():
    return render_template("/pokedex/Mew.html")

@app.route("/Chikorita")
def Chikorita():
    return render_template("/pokedex/Chikorita.html")

@app.route("/Bayleef")
def Bayleef():
    return render_template("/pokedex/Bayleef.html")

@app.route("/Meganium")
def Meganium():
    return render_template("/pokedex/Meganium.html")

@app.route("/Cyndaquil")
def Cyndaquil():
    return render_template("/pokedex/Cyndaquil.html")

@app.route("/Quilava")
def Quilava():
    return render_template("/pokedex/Quilava.html")

@app.route("/Typhlosion")
def Typhlosion():
    return render_template("/pokedex/Typhlosion.html")

@app.route("/TyphlosionHisui")
def TyphlosionHisui():
    return render_template("/pokedex/TyphlosionHisui.html")

@app.route("/Totodile")
def Totodile():
    return render_template("/pokedex/Totodile.html")

@app.route("/Croconaw")
def Croconaw():
    return render_template("/pokedex/Croconaw.html")

@app.route("/Feraligatr")
def Feraligatr():
    return render_template("/pokedex/Feraligatr.html")

@app.route("/Sentret")
def Sentret():
    return render_template("/pokedex/Sentret.html")

@app.route("/Furret")
def Furret():
    return render_template("/pokedex/Furret.html")

@app.route("/Hoothoot")
def Hoothoot():
    return render_template("/pokedex/Hoothoot.html")

@app.route("/Noctowl")
def Noctowl():
    return render_template("/pokedex/Noctowl.html")

@app.route("/Ledyba")
def Ledyba():
    return render_template("/pokedex/Ledyba.html")

@app.route("/Ledian")
def Ledian():
    return render_template("/pokedex/Ledian.html")

@app.route("/Spinarak")
def Spinarak():
    return render_template("/pokedex/Spinarak.html")

@app.route("/Ariados")
def Ariados():
    return render_template("/pokedex/Ariados.html")

@app.route("/Crobat")
def Crobat():
    return render_template("/pokedex/Crobat.html")

@app.route("/Chinchou")
def Chinchou():
    return render_template("/pokedex/Chinchou.html")

@app.route("/Lanturn")
def Lanturn():
    return render_template("/pokedex/Lanturn.html")

@app.route("/Pichu")
def Pichu():
    return render_template("/pokedex/Pichu.html")

@app.route("/Cleffa")
def Cleffa():
    return render_template("/pokedex/Cleffa.html")

@app.route("/Igglybuff")
def Igglybuff():
    return render_template("/pokedex/Igglybuff.html")

@app.route("/Togepi")
def Togepi():
    return render_template("/pokedex/Togepi.html")

@app.route("/Togetic")
def Togetic():
    return render_template("/pokedex/Togetic.html")

@app.route("/Natu")
def Natu():
    return render_template("/pokedex/Natu.html")

@app.route("/Xatu")
def Xatu():
    return render_template("/pokedex/Xatu.html")

@app.route("/Mareep")
def Mareep():
    return render_template("/pokedex/Mareep.html")

@app.route("/Flaaffy")
def Flaaffy():
    return render_template("/pokedex/Flaaffy.html")

@app.route("/Ampharos")
def Ampharos():
    return render_template("/pokedex/Ampharos.html")

@app.route("/AmpharosMega")
def AmpharosMega():
    return render_template("/pokedex/AmpharosMega.html")

@app.route("/Bellossom")
def Bellossom():
    return render_template("/pokedex/Bellossom.html")

@app.route("/Marill")
def Marill():
    return render_template("/pokedex/Marill.html")

@app.route("/Azumarill")
def Azumarill():
    return render_template("/pokedex/Azumarill.html")

@app.route("/Sudowoodo")
def Sudowoodo():
    return render_template("/pokedex/Sudowoodo.html")

@app.route("/Politoed")
def Politoed():
    return render_template("/pokedex/Politoed.html")

@app.route("/Hoppip")
def Hoppip():
    return render_template("/pokedex/Hoppip.html")

@app.route("/Skiploom")
def Skiploom():
    return render_template("/pokedex/Skiploom.html")

@app.route("/Jumpluff")
def Jumpluff():
    return render_template("/pokedex/Jumpluff.html")

@app.route("/Aipom")
def Aipom():
    return render_template("/pokedex/Aipom.html")

@app.route("/Sunkern")
def Sunkern():
    return render_template("/pokedex/Sunkern.html")

@app.route("/Sunflora")
def Sunflora():
    return render_template("/pokedex/Sunflora.html")

@app.route("/Yanma")
def Yanma():
    return render_template("/pokedex/Yanma.html")

@app.route("/Wooper")
def Wooper():
    return render_template("/pokedex/Wooper.html")

@app.route("/WooperPaldea")
def WooperPaldea():
    return render_template("/pokedex/WooperPaldea.html")

@app.route("/Quagsire")
def Quagsire():
    return render_template("/pokedex/Quagsire.html")

@app.route("/Espeon")
def Espeon():
    return render_template("/pokedex/Espeon.html")

@app.route("/Umbreon")
def Umbreon():
    return render_template("/pokedex/Umbreon.html")

@app.route("/Murkrow")
def Murkrow():
    return render_template("/pokedex/Murkrow.html")

@app.route("/Slowking")
def Slowking():
    return render_template("/pokedex/Slowking.html")

@app.route("/SlowkingGalar")
def SlowkingGalar():
    return render_template("/pokedex/SlowkingGalar.html")

@app.route("/Misdreavus")
def Misdreavus():
    return render_template("/pokedex/Misdreavus.html")

@app.route("/Unown")
def Unown():
    return render_template("/pokedex/Unown.html")

@app.route("/UnownA")
def UnownA():
    return render_template("/pokedex/UnownA.html")

@app.route("/UnownB")
def UnownB():
    return render_template("/pokedex/UnownB.html")

@app.route("/UnownC")
def UnownC():
    return render_template("/pokedex/UnownC.html")

@app.route("/UnownD")
def UnownD():
    return render_template("/pokedex/UnownD.html")

@app.route("/UnownE")
def UnownE():
    return render_template("/pokedex/UnownE.html")

@app.route("/UnownG")
def UnownG():
    return render_template("/pokedex/UnownG.html")

@app.route("/UnownH")
def UnownH():
    return render_template("/pokedex/UnownH.html")

@app.route("/UnownI")
def UnownI():
    return render_template("/pokedex/UnownI.html")

@app.route("/UnownJ")
def UnownJ():
    return render_template("/pokedex/UnownJ.html")

@app.route("/UnownK")
def UnownK():
    return render_template("/pokedex/UnownK.html")

@app.route("/UnownL")
def UnownL():
    return render_template("/pokedex/UnownL.html")

@app.route("/UnownM")
def UnownM():
    return render_template("/pokedex/UnownM.html")

@app.route("/UnownN")
def UnownN():
    return render_template("/pokedex/UnownN.html")

@app.route("/UnownO")
def UnownO():
    return render_template("/pokedex/UnownO.html")

@app.route("/UnownP")
def UnownP():
    return render_template("/pokedex/UnownP.html")

@app.route("/UnownQ")
def UnownQ():
    return render_template("/pokedex/UnownQ.html")

@app.route("/UnownR")
def UnownR():
    return render_template("/pokedex/UnownR.html")

@app.route("/UnownS")
def UnownS():
    return render_template("/pokedex/UnownS.html")

@app.route("/UnownT")
def UnownT():
    return render_template("/pokedex/UnownT.html")

@app.route("/UnownU")
def UnownU():
    return render_template("/pokedex/UnownU.html")

@app.route("/UnownV")
def UnownV():
    return render_template("/pokedex/UnownV.html")

@app.route("/UnownW")
def UnownW():
    return render_template("/pokedex/UnownW.html")

@app.route("/UnownX")
def UnownX():
    return render_template("/pokedex/UnownX.html")

@app.route("/UnownY")
def UnownY():
    return render_template("/pokedex/UnownY.html")

@app.route("/UnownZ")
def UnownZ():
    return render_template("/pokedex/UnownZ.html")

@app.route("/UnownExclamation_Mark")
def UnownExclamation_Mark():
    return render_template("/pokedex/UnownExclamation_Mark.html")

@app.route("/UnownQuestion_Mark")
def UnownQuestion_Mark():
    return render_template("/pokedex/UnownQuestion_Mark.html")

@app.route("/Wobbuffet")
def Wobbuffet():
    return render_template("/pokedex/Wobbuffet.html")

@app.route("/Girafarig")
def Girafarig():
    return render_template("/pokedex/Girafarig.html")

@app.route("/Pineco")
def Pineco():
    return render_template("/pokedex/Pineco.html")

@app.route("/Forretress")
def Forretress():
    return render_template("/pokedex/Forretress.html")

@app.route("/Dunsparce")
def Dunsparce():
    return render_template("/pokedex/Dunsparce.html")

@app.route("/Gligar")
def Gligar():
    return render_template("/pokedex/Gligar.html")

@app.route("/Steelix")
def Steelix():
    return render_template("/pokedex/Steelix.html")

@app.route("/SteelixMega")
def SteelixMega():
    return render_template("/pokedex/SteelixMega.html")

@app.route("/Snubbull")
def Snubbull():
    return render_template("/pokedex/Snubbull.html")

@app.route("/Granbull")
def Granbull():
    return render_template("/pokedex/Granbull.html")

@app.route("/Qwilfish")
def Qwilfish():
    return render_template("/pokedex/Qwilfish.html")

@app.route("/QwilfishHisui")
def QwilfishHisui():
    return render_template("/pokedex/QwilfishHisui.html")

@app.route("/Scizor")
def Scizor():
    return render_template("/pokedex/Scizor.html")

@app.route("/ScizorMega")
def ScizorMega():
    return render_template("/pokedex/ScizorMega.html")

@app.route("/Shuckle")
def Shuckle():
    return render_template("/pokedex/Shuckle.html")

@app.route("/Heracross")
def Heracross():
    return render_template("/pokedex/Heracross.html")

@app.route("/HeracrossMega")
def HeracrossMega():
    return render_template("/pokedex/HeracrossMega.html")

@app.route("/Sneasel")
def Sneasel():
    return render_template("/pokedex/Sneasel.html")

@app.route("/SneaselHisui")
def SneaselHisui():
    return render_template("/pokedex/SneaselHisui.html")

@app.route("/Teddiursa")
def Teddiursa():
    return render_template("/pokedex/Teddiursa.html")

@app.route("/Ursaring")
def Ursaring():
    return render_template("/pokedex/Ursaring.html")

@app.route("/Slugma")
def Slugma():
    return render_template("/pokedex/Slugma.html")

@app.route("/Magcargo")
def Magcargo():
    return render_template("/pokedex/Magcargo.html")

@app.route("/Swinub")
def Swinub():
    return render_template("/pokedex/Swinub.html")

@app.route("/Piloswine")
def Piloswine():
    return render_template("/pokedex/Piloswine.html")

@app.route("/Corsola")
def Corsola():
    return render_template("/pokedex/Corsola.html")

@app.route("/CorsolaGalar")
def CorsolaGalar():
    return render_template("/pokedex/CorsolaGalar.html")

@app.route("/Remoraid")
def Remoraid():
    return render_template("/pokedex/Remoraid.html")

@app.route("/Octillery")
def Octillery():
    return render_template("/pokedex/Octillery.html")

@app.route("/Delibird")
def Delibird():
    return render_template("/pokedex/Delibird.html")

@app.route("/Mantine")
def Mantine():
    return render_template("/pokedex/Mantine.html")

@app.route("/Skarmory")
def Skarmory():
    return render_template("/pokedex/Skarmory.html")

@app.route("/Houndour")
def Houndour():
    return render_template("/pokedex/Houndour.html")

@app.route("/Houndoom")
def Houndoom():
    return render_template("/pokedex/Houndoom.html")

@app.route("/HoundoomMega")
def HoundoomMega():
    return render_template("/pokedex/HoundoomMega.html")

@app.route("/Kingdra")
def Kingdra():
    return render_template("/pokedex/Kingdra.html")

@app.route("/Phanpy")
def Phanpy():
    return render_template("/pokedex/Phanpy.html")

@app.route("/Donphan")
def Donphan():
    return render_template("/pokedex/Donphan.html")

@app.route("/Porygon2")
def Porygon2():
    return render_template("/pokedex/Porygon2.html")

@app.route("/Stantler")
def Stantler():
    return render_template("/pokedex/Stantler.html")

@app.route("/Smeargle")
def Smeargle():
    return render_template("/pokedex/Smeargle.html")

@app.route("/Tyrogue")
def Tyrogue():
    return render_template("/pokedex/Tyrogue.html")

@app.route("/Hitmontop")
def Hitmontop():
    return render_template("/pokedex/Hitmontop.html")

@app.route("/Smoochum")
def Smoochum():
    return render_template("/pokedex/Smoochum.html")

@app.route("/Elekid")
def Elekid():
    return render_template("/pokedex/Elekid.html")

@app.route("/Magby")
def Magby():
    return render_template("/pokedex/Magby.html")

@app.route("/Miltank")
def Miltank():
    return render_template("/pokedex/Miltank.html")

@app.route("/Blissey")
def Blissey():
    return render_template("/pokedex/Blissey.html")

@app.route("/Raikou")
def Raikou():
    return render_template("/pokedex/Raikou.html")

@app.route("/Entei")
def Entei():
    return render_template("/pokedex/Entei.html")

@app.route("/Suicune")
def Suicune():
    return render_template("/pokedex/Suicune.html")

@app.route("/Larvitar")
def Larvitar():
    return render_template("/pokedex/Larvitar.html")

@app.route("/Pupitar")
def Pupitar():
    return render_template("/pokedex/Pupitar.html")

@app.route("/Tyranitar")
def Tyranitar():
    return render_template("/pokedex/Tyranitar.html")

@app.route("/TyranitarMega")
def TyranitarMega():
    return render_template("/pokedex/TyranitarMega.html")

@app.route("/Lugia")
def Lugia():
    return render_template("/pokedex/Lugia.html")

@app.route("/HoOh")
def HoOh():
    return render_template("/pokedex/HoOh.html")

@app.route("/Celebi")
def Celebi():
    return render_template("/pokedex/Celebi.html")

@app.route("/Treecko")
def Treecko():
    return render_template("/pokedex/Treecko.html")

@app.route("/Grovyle")
def Grovyle():
    return render_template("/pokedex/Grovyle.html")

@app.route("/Sceptile")
def Sceptile():
    return render_template("/pokedex/Sceptile.html")

@app.route("/SceptileMega")
def SceptileMega():
    return render_template("/pokedex/SceptileMega.html")

@app.route("/Torchic")
def Torchic():
    return render_template("/pokedex/Torchic.html")

@app.route("/Combusken")
def Combusken():
    return render_template("/pokedex/Combusken.html")

@app.route("/Blaziken")
def Blaziken():
    return render_template("/pokedex/Blaziken.html")

@app.route("/BlazikenMega")
def BlazikenMega():
    return render_template("/pokedex/BlazikenMega.html")

@app.route("/Mudkip")
def Mudkip():
    return render_template("/pokedex/Mudkip.html")

@app.route("/Marshtomp")
def Marshtomp():
    return render_template("/pokedex/Marshtomp.html")

@app.route("/Swampert")
def Swampert():
    return render_template("/pokedex/Swampert.html")

@app.route("/SwampertMega")
def SwampertMega():
    return render_template("/pokedex/SwampertMega.html")

@app.route("/Poochyena")
def Poochyena():
    return render_template("/pokedex/Poochyena.html")

@app.route("/Mightyena")
def Mightyena():
    return render_template("/pokedex/Mightyena.html")

@app.route("/Zigzagoon")
def Zigzagoon():
    return render_template("/pokedex/Zigzagoon.html")

@app.route("/ZigzagoonGalar")
def ZigzagoonGalar():
    return render_template("/pokedex/ZigzagoonGalar.html")

@app.route("/Linoone")
def Linoone():
    return render_template("/pokedex/Linoone.html")

@app.route("/LinooneGalar")
def LinooneGalar():
    return render_template("/pokedex/LinooneGalar.html")

@app.route("/Wurmple")
def Wurmple():
    return render_template("/pokedex/Wurmple.html")

@app.route("/Silcoon")
def Silcoon():
    return render_template("/pokedex/Silcoon.html")

@app.route("/Beautifly")
def Beautifly():
    return render_template("/pokedex/Beautifly.html")

@app.route("/Cascoon")
def Cascoon():
    return render_template("/pokedex/Cascoon.html")

@app.route("/Dustox")
def Dustox():
    return render_template("/pokedex/Dustox.html")

@app.route("/Lotad")
def Lotad():
    return render_template("/pokedex/Lotad.html")

@app.route("/Lombre")
def Lombre():
    return render_template("/pokedex/Lombre.html")

@app.route("/Ludicolo")
def Ludicolo():
    return render_template("/pokedex/Ludicolo.html")

@app.route("/Seedot")
def Seedot():
    return render_template("/pokedex/Seedot.html")

@app.route("/Nuzleaf")
def Nuzleaf():
    return render_template("/pokedex/Nuzleaf.html")

@app.route("/Shiftry")
def Shiftry():
    return render_template("/pokedex/Shiftry.html")

@app.route("/Taillow")
def Taillow():
    return render_template("/pokedex/Taillow.html")

@app.route("/Swellow")
def Swellow():
    return render_template("/pokedex/Swellow.html")

@app.route("/Wingull")
def Wingull():
    return render_template("/pokedex/Wingull.html")

@app.route("/Pelipper")
def Pelipper():
    return render_template("/pokedex/Pelipper.html")

@app.route("/Ralts")
def Ralts():
    return render_template("/pokedex/Ralts.html")

@app.route("/Kirlia")
def Kirlia():
    return render_template("/pokedex/Kirlia.html")

@app.route("/Gardevoir")
def Gardevoir():
    return render_template("/pokedex/Gardevoir.html")

@app.route("/GardevoirMega")
def GardevoirMega():
    return render_template("/pokedex/GardevoirMega.html")

@app.route("/Surskit")
def Surskit():
    return render_template("/pokedex/Surskit.html")

@app.route("/Masquerain")
def Masquerain():
    return render_template("/pokedex/Masquerain.html")

@app.route("/Shroomish")
def Shroomish():
    return render_template("/pokedex/Shroomish.html")

@app.route("/Breloom")
def Breloom():
    return render_template("/pokedex/Breloom.html")

@app.route("/Slakoth")
def Slakoth():
    return render_template("/pokedex/Slakoth.html")

@app.route("/Vigoroth")
def Vigoroth():
    return render_template("/pokedex/Vigoroth.html")

@app.route("/Slaking")
def Slaking():
    return render_template("/pokedex/Slaking.html")

@app.route("/Nincada")
def Nincada():
    return render_template("/pokedex/Nincada.html")

@app.route("/Ninjask")
def Ninjask():
    return render_template("/pokedex/Ninjask.html")

@app.route("/Shedinja")
def Shedinja():
    return render_template("/pokedex/Shedinja.html")

@app.route("/Whismur")
def Whismur():
    return render_template("/pokedex/Whismur.html")

@app.route("/Loudred")
def Loudred():
    return render_template("/pokedex/Loudred.html")

@app.route("/Exploud")
def Exploud():
    return render_template("/pokedex/Exploud.html")

@app.route("/Makuhita")
def Makuhita():
    return render_template("/pokedex/Makuhita.html")

@app.route("/Hariyama")
def Hariyama():
    return render_template("/pokedex/Hariyama.html")

@app.route("/Azurill")
def Azurill():
    return render_template("/pokedex/Azurill.html")

@app.route("/Nosepass")
def Nosepass():
    return render_template("/pokedex/Nosepass.html")

@app.route("/Skitty")
def Skitty():
    return render_template("/pokedex/Skitty.html")

@app.route("/Delcatty")
def Delcatty():
    return render_template("/pokedex/Delcatty.html")

@app.route("/Sableye")
def Sableye():
    return render_template("/pokedex/Sableye.html")

@app.route("/SableyeMega")
def SableyeMega():
    return render_template("/pokedex/SableyeMega.html")

@app.route("/Mawile")
def Mawile():
    return render_template("/pokedex/Mawile.html")

@app.route("/MawileMega")
def MawileMega():
    return render_template("/pokedex/MawileMega.html")

@app.route("/Aron")
def Aron():
    return render_template("/pokedex/Aron.html")

@app.route("/Lairon")
def Lairon():
    return render_template("/pokedex/Lairon.html")

@app.route("/Aggron")
def Aggron():
    return render_template("/pokedex/Aggron.html")

@app.route("/AggronMega")
def AggronMega():
    return render_template("/pokedex/AggronMega.html")

@app.route("/Meditite")
def Meditite():
    return render_template("/pokedex/Meditite.html")

@app.route("/Medicham")
def Medicham():
    return render_template("/pokedex/Medicham.html")

@app.route("/MedichamMega")
def MedichamMega():
    return render_template("/pokedex/MedichamMega.html")

@app.route("/Electrike")
def Electrike():
    return render_template("/pokedex/Electrike.html")

@app.route("/Manectric")
def Manectric():
    return render_template("/pokedex/Manectric.html")

@app.route("/ManectricMega")
def ManectricMega():
    return render_template("/pokedex/ManectricMega.html")

@app.route("/Plusle")
def Plusle():
    return render_template("/pokedex/Plusle.html")

@app.route("/Minun")
def Minun():
    return render_template("/pokedex/Minun.html")

@app.route("/Volbeat")
def Volbeat():
    return render_template("/pokedex/Volbeat.html")

@app.route("/Illumise")
def Illumise():
    return render_template("/pokedex/Illumise.html")

@app.route("/Roselia")
def Roselia():
    return render_template("/pokedex/Roselia.html")

@app.route("/Gulpin")
def Gulpin():
    return render_template("/pokedex/Gulpin.html")

@app.route("/Swalot")
def Swalot():
    return render_template("/pokedex/Swalot.html")

@app.route("/Carvanha")
def Carvanha():
    return render_template("/pokedex/Carvanha.html")

@app.route("/Sharpedo")
def Sharpedo():
    return render_template("/pokedex/Sharpedo.html")

@app.route("/SharpedoMega")
def SharpedoMega():
    return render_template("/pokedex/SharpedoMega.html")

@app.route("/Wailmer")
def Wailmer():
    return render_template("/pokedex/Wailmer.html")

@app.route("/Wailord")
def Wailord():
    return render_template("/pokedex/Wailord.html")

@app.route("/Numel")
def Numel():
    return render_template("/pokedex/Numel.html")

@app.route("/Camerupt")
def Camerupt():
    return render_template("/pokedex/Camerupt.html")

@app.route("/CameruptMega")
def CameruptMega():
    return render_template("/pokedex/CameruptMega.html")

@app.route("/Torkoal")
def Torkoal():
    return render_template("/pokedex/Torkoal.html")

@app.route("/Spoink")
def Spoink():
    return render_template("/pokedex/Spoink.html")

@app.route("/Grumpig")
def Grumpig():
    return render_template("/pokedex/Grumpig.html")

@app.route("/Spinda")
def Spinda():
    return render_template("/pokedex/Spinda.html")

@app.route("/Trapinch")
def Trapinch():
    return render_template("/pokedex/Trapinch.html")

@app.route("/Vibrava")
def Vibrava():
    return render_template("/pokedex/Vibrava.html")

@app.route("/Flygon")
def Flygon():
    return render_template("/pokedex/Flygon.html")

@app.route("/Cacnea")
def Cacnea():
    return render_template("/pokedex/Cacnea.html")

@app.route("/Cacturne")
def Cacturne():
    return render_template("/pokedex/Cacturne.html")

@app.route("/Swablu")
def Swablu():
    return render_template("/pokedex/Swablu.html")

@app.route("/Altaria")
def Altaria():
    return render_template("/pokedex/Altaria.html")

@app.route("/AltariaMega")
def AltariaMega():
    return render_template("/pokedex/AltariaMega.html")

@app.route("/Zangoose")
def Zangoose():
    return render_template("/pokedex/Zangoose.html")

@app.route("/Seviper")
def Seviper():
    return render_template("/pokedex/Seviper.html")

@app.route("/Lunatone")
def Lunatone():
    return render_template("/pokedex/Lunatone.html")

@app.route("/Solrock")
def Solrock():
    return render_template("/pokedex/Solrock.html")

@app.route("/Barboach")
def Barboach():
    return render_template("/pokedex/Barboach.html")

@app.route("/Whiscash")
def Whiscash():
    return render_template("/pokedex/Whiscash.html")

@app.route("/Corphish")
def Corphish():
    return render_template("/pokedex/Corphish.html")

@app.route("/Crawdaunt")
def Crawdaunt():
    return render_template("/pokedex/Crawdaunt.html")

@app.route("/Baltoy")
def Baltoy():
    return render_template("/pokedex/Baltoy.html")

@app.route("/Claydol")
def Claydol():
    return render_template("/pokedex/Claydol.html")

@app.route("/Lileep")
def Lileep():
    return render_template("/pokedex/Lileep.html")

@app.route("/Cradily")
def Cradily():
    return render_template("/pokedex/Cradily.html")

@app.route("/Anorith")
def Anorith():
    return render_template("/pokedex/Anorith.html")

@app.route("/Armaldo")
def Armaldo():
    return render_template("/pokedex/Armaldo.html")

@app.route("/Feebas")
def Feebas():
    return render_template("/pokedex/Feebas.html")

@app.route("/Milotic")
def Milotic():
    return render_template("/pokedex/Milotic.html")

@app.route("/Castform")
def Castform():
    return render_template("/pokedex/Castform.html")

@app.route("/CastformSunny")
def CastformSunny():
    return render_template("/pokedex/CastformSunny.html")

@app.route("/CastformRainy")
def CastformRainy():
    return render_template("/pokedex/CastformRainy.html")

@app.route("/CastformSnowy")
def CastformSnowy():
    return render_template("/pokedex/CastformSnowy.html")

@app.route("/Kecleon")
def Kecleon():
    return render_template("/pokedex/Kecleon.html")

@app.route("/Shuppet")
def Shuppet():
    return render_template("/pokedex/Shuppet.html")

@app.route("/Banette")
def Banette():
    return render_template("/pokedex/Banette.html")

@app.route("/BanetteMega")
def BanetteMega():
    return render_template("/pokedex/BanetteMega.html")

@app.route("/Duskull")
def Duskull():
    return render_template("/pokedex/Duskull.html")

@app.route("/Dusclops")
def Dusclops():
    return render_template("/pokedex/Dusclops.html")

@app.route("/Tropius")
def Tropius():
    return render_template("/pokedex/Tropius.html")

@app.route("/Chimecho")
def Chimecho():
    return render_template("/pokedex/Chimecho.html")

@app.route("/Absol")
def Absol():
    return render_template("/pokedex/Absol.html")

@app.route("/AbsolMega")
def AbsolMega():
    return render_template("/pokedex/AbsolMega.html")

@app.route("/Wynaut")
def Wynaut():
    return render_template("/pokedex/Wynaut.html")

@app.route("/Snorunt")
def Snorunt():
    return render_template("/pokedex/Snorunt.html")

@app.route("/Glalie")
def Glalie():
    return render_template("/pokedex/Glalie.html")

@app.route("/GlalieMega")
def GlalieMega():
    return render_template("/pokedex/GlalieMega.html")

@app.route("/Spheal")
def Spheal():
    return render_template("/pokedex/Spheal.html")

@app.route("/Sealeo")
def Sealeo():
    return render_template("/pokedex/Sealeo.html")

@app.route("/Walrein")
def Walrein():
    return render_template("/pokedex/Walrein.html")

@app.route("/Clamperl")
def Clamperl():
    return render_template("/pokedex/Clamperl.html")

@app.route("/Huntail")
def Huntail():
    return render_template("/pokedex/Huntail.html")

@app.route("/Gorebyss")
def Gorebyss():
    return render_template("/pokedex/Gorebyss.html")

@app.route("/Relicanth")
def Relicanth():
    return render_template("/pokedex/Relicanth.html")

@app.route("/Luvdisc")
def Luvdisc():
    return render_template("/pokedex/Luvdisc.html")

@app.route("/Bagon")
def Bagon():
    return render_template("/pokedex/Bagon.html")

@app.route("/Shelgon")
def Shelgon():
    return render_template("/pokedex/Shelgon.html")

@app.route("/Salamence")
def Salamence():
    return render_template("/pokedex/Salamence.html")

@app.route("/SalamenceMega")
def SalamenceMega():
    return render_template("/pokedex/SalamenceMega.html")

@app.route("/Beldum")
def Beldum():
    return render_template("/pokedex/Beldum.html")

@app.route("/Metang")
def Metang():
    return render_template("/pokedex/Metang.html")

@app.route("/Metagross")
def Metagross():
    return render_template("/pokedex/Metagross.html")

@app.route("/MetagrossMega")
def MetagrossMega():
    return render_template("/pokedex/MetagrossMega.html")

@app.route("/Regirock")
def Regirock():
    return render_template("/pokedex/Regirock.html")

@app.route("/Regice")
def Regice():
    return render_template("/pokedex/Regice.html")

@app.route("/Registeel")
def Registeel():
    return render_template("/pokedex/Registeel.html")

@app.route("/Latias")
def Latias():
    return render_template("/pokedex/Latias.html")

@app.route("/LatiasMega")
def LatiasMega():
    return render_template("/pokedex/LatiasMega.html")

@app.route("/Latios")
def Latios():
    return render_template("/pokedex/Latios.html")

@app.route("/LatiosMega")
def LatiosMega():
    return render_template("/pokedex/LatiosMega.html")

@app.route("/Kyogre")
def Kyogre():
    return render_template("/pokedex/Kyogre.html")

@app.route("/KyogrePrimal")
def KyogrePrimal():
    return render_template("/pokedex/KyogrePrimal.html")

@app.route("/Groudon")
def Groudon():
    return render_template("/pokedex/Groudon.html")

@app.route("/GroudonPrimal")
def GroudonPrimal():
    return render_template("/pokedex/GroudonPrimal.html")

@app.route("/Rayquaza")
def Rayquaza():
    return render_template("/pokedex/Rayquaza.html")

@app.route("/RayquazaMega")
def RayquazaMega():
    return render_template("/pokedex/RayquazaMega.html")

@app.route("/Jirachi")
def Jirachi():
    return render_template("/pokedex/Jirachi.html")

@app.route("/Deoxys")
def Deoxys():
    return render_template("/pokedex/Deoxys.html")

@app.route("/DeoxysAttack")
def DeoxysAttack():
    return render_template("/pokedex/DeoxysAttack.html")

@app.route("/DeoxysDefense")
def DeoxysDefense():
    return render_template("/pokedex/DeoxysDefense.html")

@app.route("/DeoxysSpeed")
def DeoxysSpeed():
    return render_template("/pokedex/DeoxysSpeed.html")

@app.route("/Turtwig")
def Turtwig():
    return render_template("/pokedex/Turtwig.html")

@app.route("/Grotle")
def Grotle():
    return render_template("/pokedex/Grotle.html")

@app.route("/Torterra")
def Torterra():
    return render_template("/pokedex/Torterra.html")

@app.route("/Chimchar")
def Chimchar():
    return render_template("/pokedex/Chimchar.html")

@app.route("/Monferno")
def Monferno():
    return render_template("/pokedex/Monferno.html")

@app.route("/Infernape")
def Infernape():
    return render_template("/pokedex/Infernape.html")

@app.route("/Piplup")
def Piplup():
    return render_template("/pokedex/Piplup.html")

@app.route("/Prinplup")
def Prinplup():
    return render_template("/pokedex/Prinplup.html")

@app.route("/Empoleon")
def Empoleon():
    return render_template("/pokedex/Empoleon.html")

@app.route("/Starly")
def Starly():
    return render_template("/pokedex/Starly.html")

@app.route("/Staravia")
def Staravia():
    return render_template("/pokedex/Staravia.html")

@app.route("/Staraptor")
def Staraptor():
    return render_template("/pokedex/Staraptor.html")

@app.route("/Bidoof")
def Bidoof():
    return render_template("/pokedex/Bidoof.html")

@app.route("/Bibarel")
def Bibarel():
    return render_template("/pokedex/Bibarel.html")

@app.route("/Kricketot")
def Kricketot():
    return render_template("/pokedex/Kricketot.html")

@app.route("/Kricketune")
def Kricketune():
    return render_template("/pokedex/Kricketune.html")

@app.route("/Shinx")
def Shinx():
    return render_template("/pokedex/Shinx.html")

@app.route("/Luxio")
def Luxio():
    return render_template("/pokedex/Luxio.html")

@app.route("/Luxray")
def Luxray():
    return render_template("/pokedex/Luxray.html")

@app.route("/Budew")
def Budew():
    return render_template("/pokedex/Budew.html")

@app.route("/Roserade")
def Roserade():
    return render_template("/pokedex/Roserade.html")

@app.route("/Cranidos")
def Cranidos():
    return render_template("/pokedex/Cranidos.html")

@app.route("/Rampardos")
def Rampardos():
    return render_template("/pokedex/Rampardos.html")

@app.route("/Shieldon")
def Shieldon():
    return render_template("/pokedex/Shieldon.html")

@app.route("/Bastiodon")
def Bastiodon():
    return render_template("/pokedex/Bastiodon.html")

@app.route("/Burmy")
def Burmy():
    return render_template("/pokedex/Burmy.html")

@app.route("/BurmySandy")
def BurmySandy():
    return render_template("/pokedex/BurmySandy.html")

@app.route("/BurmyTrash")
def BurmyTrash():
    return render_template("/pokedex/BurmyTrash.html")

@app.route("/Wormadam")
def Wormadam():
    return render_template("/pokedex/Wormadam.html")

@app.route("/WormadamSandy")
def WormadamSandy():
    return render_template("/pokedex/WormadamSandy.html")

@app.route("/WormadamTrash")
def WormadamTrash():
    return render_template("/pokedex/WormadamTrash.html")

@app.route("/Mothim")
def Mothim():
    return render_template("/pokedex/Mothim.html")

@app.route("/Combee")
def Combee():
    return render_template("/pokedex/Combee.html")

@app.route("/Vespiquen")
def Vespiquen():
    return render_template("/pokedex/Vespiquen.html")

@app.route("/Pachirisu")
def Pachirisu():
    return render_template("/pokedex/Pachirisu.html")

@app.route("/Buizel")
def Buizel():
    return render_template("/pokedex/Buizel.html")

@app.route("/Floatzel")
def Floatzel():
    return render_template("/pokedex/Floatzel.html")

@app.route("/Cherubi")
def Cherubi():
    return render_template("/pokedex/Cherubi.html")

@app.route("/Cherrim")
def Cherrim():
    return render_template("/pokedex/Cherrim.html")

@app.route("/Shellos")
def Shellos():
    return render_template("/pokedex/Shellos.html")

@app.route("/ShellosEastSea")
def ShellosEastSea():
    return render_template("/pokedex/ShellosEastSea.html")

@app.route("/Gastrodon")
def Gastrodon():
    return render_template("/pokedex/Gastrodon.html")

@app.route("/GastrodonEastSea")
def GastrodonEastSea():
    return render_template("/pokedex/GastrodonEastSea.html")

@app.route("/Ambipom")
def Ambipom():
    return render_template("/pokedex/Ambipom.html")

@app.route("/Drifloon")
def Drifloon():
    return render_template("/pokedex/Drifloon.html")

@app.route("/Drifblim")
def Drifblim():
    return render_template("/pokedex/Drifblim.html")

@app.route("/Buneary")
def Buneary():
    return render_template("/pokedex/Buneary.html")

@app.route("/Lopunny")
def Lopunny():
    return render_template("/pokedex/Lopunny.html")

@app.route("/LopunnyMega")
def LopunnyMega():
    return render_template("/pokedex/LopunnyMega.html")

@app.route("/Mismagius")
def Mismagius():
    return render_template("/pokedex/Mismagius.html")

@app.route("/Honchkrow")
def Honchkrow():
    return render_template("/pokedex/Honchkrow.html")

@app.route("/Glameow")
def Glameow():
    return render_template("/pokedex/Glameow.html")

@app.route("/Purugly")
def Purugly():
    return render_template("/pokedex/Purugly.html")

@app.route("/Chingling")
def Chingling():
    return render_template("/pokedex/Chingling.html")

@app.route("/Stunky")
def Stunky():
    return render_template("/pokedex/Stunky.html")

@app.route("/Skuntank")
def Skuntank():
    return render_template("/pokedex/Skuntank.html")

@app.route("/Bronzor")
def Bronzor():
    return render_template("/pokedex/Bronzor.html")

@app.route("/Bronzong")
def Bronzong():
    return render_template("/pokedex/Bronzong.html")

@app.route("/Bonsly")
def Bonsly():
    return render_template("/pokedex/Bonsly.html")

@app.route("/MimeJr")
def MimeJr():
    return render_template("/pokedex/MimeJr.html")

@app.route("/Happiny")
def Happiny():
    return render_template("/pokedex/Happiny.html")

@app.route("/Chatot")
def Chatot():
    return render_template("/pokedex/Chatot.html")

@app.route("/Spiritomb")
def Spiritomb():
    return render_template("/pokedex/Spiritomb.html")

@app.route("/Gible")
def Gible():
    return render_template("/pokedex/Gible.html")

@app.route("/Gabite")
def Gabite():
    return render_template("/pokedex/Gabite.html")

@app.route("/Garchomp")
def Garchomp():
    return render_template("/pokedex/Garchomp.html")

@app.route("/GarchompMega")
def GarchompMega():
    return render_template("/pokedex/GarchompMega.html")

@app.route("/Munchlax")
def Munchlax():
    return render_template("/pokedex/Munchlax.html")

@app.route("/Riolu")
def Riolu():
    return render_template("/pokedex/Riolu.html")

@app.route("/Lucario")
def Lucario():
    return render_template("/pokedex/Lucario.html")

@app.route("/LucarioMega")
def LucarioMega():
    return render_template("/pokedex/LucarioMega.html")

@app.route("/Hippopotas")
def Hippopotas():
    return render_template("/pokedex/Hippopotas.html")

@app.route("/Hippowdon")
def Hippowdon():
    return render_template("/pokedex/Hippowdon.html")

@app.route("/Skorupi")
def Skorupi():
    return render_template("/pokedex/Skorupi.html")

@app.route("/Drapion")
def Drapion():
    return render_template("/pokedex/Drapion.html")

@app.route("/Croagunk")
def Croagunk():
    return render_template("/pokedex/Croagunk.html")

@app.route("/Toxicroak")
def Toxicroak():
    return render_template("/pokedex/Toxicroak.html")

@app.route("/Carnivine")
def Carnivine():
    return render_template("/pokedex/Carnivine.html")

@app.route("/Finneon")
def Finneon():
    return render_template("/pokedex/Finneon.html")

@app.route("/Lumineon")
def Lumineon():
    return render_template("/pokedex/Lumineon.html")

@app.route("/Mantyke")
def Mantyke():
    return render_template("/pokedex/Mantyke.html")

@app.route("/Snover")
def Snover():
    return render_template("/pokedex/Snover.html")

@app.route("/Abomasnow")
def Abomasnow():
    return render_template("/pokedex/Abomasnow.html")

@app.route("/AbomasnowMega")
def AbomasnowMega():
    return render_template("/pokedex/AbomasnowMega.html")

@app.route("/Weavile")
def Weavile():
    return render_template("/pokedex/Weavile.html")

@app.route("/Magnezone")
def Magnezone():
    return render_template("/pokedex/Magnezone.html")

@app.route("/Lickilicky")
def Lickilicky():
    return render_template("/pokedex/Lickilicky.html")

@app.route("/Rhyperior")
def Rhyperior():
    return render_template("/pokedex/Rhyperior.html")

@app.route("/Tangrowth")
def Tangrowth():
    return render_template("/pokedex/Tangrowth.html")

@app.route("/Electivire")
def Electivire():
    return render_template("/pokedex/Electivire.html")

@app.route("/Magmortar")
def Magmortar():
    return render_template("/pokedex/Magmortar.html")

@app.route("/Togekiss")
def Togekiss():
    return render_template("/pokedex/Togekiss.html")

@app.route("/Yanmega")
def Yanmega():
    return render_template("/pokedex/Yanmega.html")

@app.route("/Leafeon")
def Leafeon():
    return render_template("/pokedex/Leafeon.html")

@app.route("/Glaceon")
def Glaceon():
    return render_template("/pokedex/Glaceon.html")

@app.route("/Gliscor")
def Gliscor():
    return render_template("/pokedex/Gliscor.html")

@app.route("/Mamoswine")
def Mamoswine():
    return render_template("/pokedex/Mamoswine.html")

@app.route("/PorygonZ")
def PorygonZ():
    return render_template("/pokedex/PorygonZ.html")

@app.route("/Gallade")
def Gallade():
    return render_template("/pokedex/Gallade.html")

@app.route("/GalladeMega")
def GalladeMega():
    return render_template("/pokedex/GalladeMega.html")

@app.route("/Probopass")
def Probopass():
    return render_template("/pokedex/Probopass.html")

@app.route("/Dusknoir")
def Dusknoir():
    return render_template("/pokedex/Dusknoir.html")

@app.route("/Froslass")
def Froslass():
    return render_template("/pokedex/Froslass.html")

@app.route("/Rotom")
def Rotom():
    return render_template("/pokedex/Rotom.html")

@app.route("/RotomMow")
def RotomMow():
    return render_template("/pokedex/RotomMow.html")

@app.route("/RotomHeat")
def RotomHeat():
    return render_template("/pokedex/RotomHeat.html")

@app.route("/RotomWash")
def RotomWash():
    return render_template("/pokedex/RotomWash.html")

@app.route("/RotomFrost")
def RotomFrost():
    return render_template("/pokedex/RotomFrost.html")

@app.route("/RotomFan")
def RotomFan():
    return render_template("/pokedex/RotomFan.html")

@app.route("/Uxie")
def Uxie():
    return render_template("/pokedex/Uxie.html")

@app.route("/Mesprit")
def Mesprit():
    return render_template("/pokedex/Mesprit.html")

@app.route("/Azelf")
def Azelf():
    return render_template("/pokedex/Azelf.html")

@app.route("/Dialga")
def Dialga():
    return render_template("/pokedex/Dialga.html")

@app.route("/DialgaOrigin")
def DialgaOrigin():
    return render_template("/pokedex/DialgaOrigin.html")

@app.route("/Palkia")
def Palkia():
    return render_template("/pokedex/Palkia.html")

@app.route("/PalkiaOrigin")
def PalkiaOrigin():
    return render_template("/pokedex/PalkiaOrigin.html")

@app.route("/Heatran")
def Heatran():
    return render_template("/pokedex/Heatran.html")

@app.route("/Regigigas")
def Regigigas():
    return render_template("/pokedex/Regigigas.html")

@app.route("/Giratina")
def Giratina():
    return render_template("/pokedex/Giratina.html")

@app.route("/GiratinaOrigin")
def GiratinaOrigin():
    return render_template("/pokedex/GiratinaOrigin.html")

@app.route("/Cresselia")
def Cresselia():
    return render_template("/pokedex/Cresselia.html")

@app.route("/Phione")
def Phione():
    return render_template("/pokedex/Phione.html")

@app.route("/Manaphy")
def Manaphy():
    return render_template("/pokedex/Manaphy.html")

@app.route("/Darkrai")
def Darkrai():
    return render_template("/pokedex/Darkrai.html")

@app.route("/Shaymin")
def Shaymin():
    return render_template("/pokedex/Shaymin.html")

@app.route("/ShayminSky")
def ShayminSky():
    return render_template("/pokedex/ShayminSky.html")

@app.route("/Arceus")
def Arceus():
    return render_template("/pokedex/Arceus.html")

@app.route("/Victini")
def Victini():
    return render_template("/pokedex/Victini.html")

@app.route("/Snivy")
def Snivy():
    return render_template("/pokedex/Snivy.html")

@app.route("/Servine")
def Servine():
    return render_template("/pokedex/Servine.html")

@app.route("/Serperior")
def Serperior():
    return render_template("/pokedex/Serperior.html")

@app.route("/Tepig")
def Tepig():
    return render_template("/pokedex/Tepig.html")

@app.route("/Pignite")
def Pignite():
    return render_template("/pokedex/Pignite.html")

@app.route("/Emboar")
def Emboar():
    return render_template("/pokedex/Emboar.html")

@app.route("/Oshawott")
def Oshawott():
    return render_template("/pokedex/Oshawott.html")

@app.route("/Dewott")
def Dewott():
    return render_template("/pokedex/Dewott.html")

@app.route("/Samurott")
def Samurott():
    return render_template("/pokedex/Samurott.html")

@app.route("/SamurottHisui")
def SamurottHisui():
    return render_template("/pokedex/SamurottHisui.html")

@app.route("/Patrat")
def Patrat():
    return render_template("/pokedex/Patrat.html")

@app.route("/Watchog")
def Watchog():
    return render_template("/pokedex/Watchog.html")

@app.route("/Lillipup")
def Lillipup():
    return render_template("/pokedex/Lillipup.html")

@app.route("/Herdier")
def Herdier():
    return render_template("/pokedex/Herdier.html")

@app.route("/Stoutland")
def Stoutland():
    return render_template("/pokedex/Stoutland.html")

@app.route("/Purrloin")
def Purrloin():
    return render_template("/pokedex/Purrloin.html")

@app.route("/Liepard")
def Liepard():
    return render_template("/pokedex/Liepard.html")

@app.route("/Pansage")
def Pansage():
    return render_template("/pokedex/Pansage.html")

@app.route("/Simisage")
def Simisage():
    return render_template("/pokedex/Simisage.html")

@app.route("/Pansear")
def Pansear():
    return render_template("/pokedex/Pansear.html")

@app.route("/Simisear")
def Simisear():
    return render_template("/pokedex/Simisear.html")

@app.route("/Panpour")
def Panpour():
    return render_template("/pokedex/Panpour.html")

@app.route("/Simipour")
def Simipour():
    return render_template("/pokedex/Simipour.html")

@app.route("/Munna")
def Munna():
    return render_template("/pokedex/Munna.html")

@app.route("/Musharna")
def Musharna():
    return render_template("/pokedex/Musharna.html")

@app.route("/Pidove")
def Pidove():
    return render_template("/pokedex/Pidove.html")

@app.route("/Tranquill")
def Tranquill():
    return render_template("/pokedex/Tranquill.html")

@app.route("/Unfezant")
def Unfezant():
    return render_template("/pokedex/Unfezant.html")

@app.route("/Blitzle")
def Blitzle():
    return render_template("/pokedex/Blitzle.html")

@app.route("/Zebstrika")
def Zebstrika():
    return render_template("/pokedex/Zebstrika.html")

@app.route("/Roggenrola")
def Roggenrola():
    return render_template("/pokedex/Roggenrola.html")

@app.route("/Boldore")
def Boldore():
    return render_template("/pokedex/Boldore.html")

@app.route("/Gigalith")
def Gigalith():
    return render_template("/pokedex/Gigalith.html")

@app.route("/Woobat")
def Woobat():
    return render_template("/pokedex/Woobat.html")

@app.route("/Swoobat")
def Swoobat():
    return render_template("/pokedex/Swoobat.html")

@app.route("/Drilbur")
def Drilbur():
    return render_template("/pokedex/Drilbur.html")

@app.route("/Excadrill")
def Excadrill():
    return render_template("/pokedex/Excadrill.html")

@app.route("/Audino")
def Audino():
    return render_template("/pokedex/Audino.html")

@app.route("/AudinoMega")
def AudinoMega():
    return render_template("/pokedex/AudinoMega.html")

@app.route("/Timburr")
def Timburr():
    return render_template("/pokedex/Timburr.html")

@app.route("/Gurdurr")
def Gurdurr():
    return render_template("/pokedex/Gurdurr.html")

@app.route("/Conkeldurr")
def Conkeldurr():
    return render_template("/pokedex/Conkeldurr.html")

@app.route("/Tympole")
def Tympole():
    return render_template("/pokedex/Tympole.html")

@app.route("/Palpitoad")
def Palpitoad():
    return render_template("/pokedex/Palpitoad.html")

@app.route("/Seismitoad")
def Seismitoad():
    return render_template("/pokedex/Seismitoad.html")

@app.route("/Throh")
def Throh():
    return render_template("/pokedex/Throh.html")

@app.route("/Sawk")
def Sawk():
    return render_template("/pokedex/Sawk.html")

@app.route("/Sewaddle")
def Sewaddle():
    return render_template("/pokedex/Sewaddle.html")

@app.route("/Swadloon")
def Swadloon():
    return render_template("/pokedex/Swadloon.html")

@app.route("/Leavanny")
def Leavanny():
    return render_template("/pokedex/Leavanny.html")

@app.route("/Venipede")
def Venipede():
    return render_template("/pokedex/Venipede.html")

@app.route("/Whirlipede")
def Whirlipede():
    return render_template("/pokedex/Whirlipede.html")

@app.route("/Scolipede")
def Scolipede():
    return render_template("/pokedex/Scolipede.html")

@app.route("/Cottonee")
def Cottonee():
    return render_template("/pokedex/Cottonee.html")

@app.route("/Whimsicott")
def Whimsicott():
    return render_template("/pokedex/Whimsicott.html")

@app.route("/Petilil")
def Petilil():
    return render_template("/pokedex/Petilil.html")

@app.route("/Lilligant")
def Lilligant():
    return render_template("/pokedex/Lilligant.html")

@app.route("/LilligantHisui")
def LilligantHisui():
    return render_template("/pokedex/LilligantHisui.html")

@app.route("/Basculin")
def Basculin():
    return render_template("/pokedex/Basculin.html")

@app.route("/BasculinWhiteStriped")
def BasculinWhiteStriped():
    return render_template("/pokedex/BasculinWhiteStriped.html")

@app.route("/BasculinBlueStriped")
def BasculinBlueStriped():
    return render_template("/pokedex/BasculinBlueStriped.html")

@app.route("/Sandile")
def Sandile():
    return render_template("/pokedex/Sandile.html")

@app.route("/Krokorok")
def Krokorok():
    return render_template("/pokedex/Krokorok.html")

@app.route("/Krookodile")
def Krookodile():
    return render_template("/pokedex/Krookodile.html")

@app.route("/Darumaka")
def Darumaka():
    return render_template("/pokedex/Darumaka.html")

@app.route("/DarumakaGalar")
def DarumakaGalar():
    return render_template("/pokedex/DarumakaGalar.html")

@app.route("/Darmanitan")
def Darmanitan():
    return render_template("/pokedex/Darmanitan.html")

@app.route("/DarmanitanZen")
def DarmanitanZen():
    return render_template("/pokedex/DarmanitanZen.html")

@app.route("/DarmanitanGalar")
def DarmanitanGalar():
    return render_template("/pokedex/DarmanitanGalar.html")

@app.route("/DarmanitanGalarZen")
def DarmanitanGalarZen():
    return render_template("/pokedex/DarmanitanGalarZen.html")

@app.route("/Maractus")
def Maractus():
    return render_template("/pokedex/Maractus.html")

@app.route("/Dwebble")
def Dwebble():
    return render_template("/pokedex/Dwebble.html")

@app.route("/Crustle")
def Crustle():
    return render_template("/pokedex/Crustle.html")

@app.route("/Scraggy")
def Scraggy():
    return render_template("/pokedex/Scraggy.html")

@app.route("/Scrafty")
def Scrafty():
    return render_template("/pokedex/Scrafty.html")

@app.route("/Sigilyph")
def Sigilyph():
    return render_template("/pokedex/Sigilyph.html")

@app.route("/Yamask")
def Yamask():
    return render_template("/pokedex/Yamask.html")

@app.route("/YamaskGalar")
def YamaskGalar():
    return render_template("/pokedex/YamaskGalar.html")

@app.route("/Cofagrigus")
def Cofagrigus():
    return render_template("/pokedex/Cofagrigus.html")

@app.route("/Tirtouga")
def Tirtouga():
    return render_template("/pokedex/Tirtouga.html")

@app.route("/Carracosta")
def Carracosta():
    return render_template("/pokedex/Carracosta.html")

@app.route("/Archen")
def Archen():
    return render_template("/pokedex/Archen.html")

@app.route("/Archeops")
def Archeops():
    return render_template("/pokedex/Archeops.html")

@app.route("/Trubbish")
def Trubbish():
    return render_template("/pokedex/Trubbish.html")

@app.route("/Garbodor")
def Garbodor():
    return render_template("/pokedex/Garbodor.html")

@app.route("/GarbodorGigantamax")
def GarbodorGigantamax():
    return render_template("/pokedex/GarbodorGigantamax.html")

@app.route("/Zorua")
def Zorua():
    return render_template("/pokedex/Zorua.html")

@app.route("/ZoruaHisui")
def ZoruaHisui():
    return render_template("/pokedex/ZoruaHisui.html")

@app.route("/Zoroark")
def Zoroark():
    return render_template("/pokedex/Zoroark.html")

@app.route("/ZoroarkHisui")
def ZoroarkHisui():
    return render_template("/pokedex/ZoroarkHisui.html")

@app.route("/Minccino")
def Minccino():
    return render_template("/pokedex/Minccino.html")

@app.route("/Cinccino")
def Cinccino():
    return render_template("/pokedex/Cinccino.html")

@app.route("/Gothita")
def Gothita():
    return render_template("/pokedex/Gothita.html")

@app.route("/Gothorita")
def Gothorita():
    return render_template("/pokedex/Gothorita.html")

@app.route("/Gothitelle")
def Gothitelle():
    return render_template("/pokedex/Gothitelle.html")

@app.route("/Solosis")
def Solosis():
    return render_template("/pokedex/Solosis.html")

@app.route("/Duosion")
def Duosion():
    return render_template("/pokedex/Duosion.html")

@app.route("/Reuniclus")
def Reuniclus():
    return render_template("/pokedex/Reuniclus.html")

@app.route("/Ducklett")
def Ducklett():
    return render_template("/pokedex/Ducklett.html")

@app.route("/Swanna")
def Swanna():
    return render_template("/pokedex/Swanna.html")

@app.route("/Vanillite")
def Vanillite():
    return render_template("/pokedex/Vanillite.html")

@app.route("/Vanillish")
def Vanillish():
    return render_template("/pokedex/Vanillish.html")

@app.route("/Vanilluxe")
def Vanilluxe():
    return render_template("/pokedex/Vanilluxe.html")

@app.route("/Deerling")
def Deerling():
    return render_template("/pokedex/Deerling.html")

@app.route("/DeerlingSummer")
def DeerlingSummer():
    return render_template("/pokedex/DeerlingSummer.html")

@app.route("/DeerlingAutumn")
def DeerlingAutumn():
    return render_template("/pokedex/DeerlingAutumn.html")

@app.route("/DeerlingWinter")
def DeerlingWinter():
    return render_template("/pokedex/DeerlingWinter.html")

@app.route("/Sawsbuck")
def Sawsbuck():
    return render_template("/pokedex/Sawsbuck.html")

@app.route("/SawsbuckSummer")
def SawsbuckSummer():
    return render_template("/pokedex/SawsbuckSummer.html")

@app.route("/SawsbuckAutumn")
def SawsbuckAutumn():
    return render_template("/pokedex/SawsbuckAutumn.html")

@app.route("/SawsbuckWinter")
def SawsbuckWinter():
    return render_template("/pokedex/SawsbuckWinter.html")

@app.route("/Emolga")
def Emolga():
    return render_template("/pokedex/Emolga.html")

@app.route("/Karrablast")
def Karrablast():
    return render_template("/pokedex/Karrablast.html")

@app.route("/Escavalier")
def Escavalier():
    return render_template("/pokedex/Escavalier.html")

@app.route("/Foongus")
def Foongus():
    return render_template("/pokedex/Foongus.html")

@app.route("/Amoonguss")
def Amoonguss():
    return render_template("/pokedex/Amoonguss.html")

@app.route("/Frillish")
def Frillish():
    return render_template("/pokedex/Frillish.html")

@app.route("/Jellicent")
def Jellicent():
    return render_template("/pokedex/Jellicent.html")

@app.route("/Alomomola")
def Alomomola():
    return render_template("/pokedex/Alomomola.html")

@app.route("/Joltik")
def Joltik():
    return render_template("/pokedex/Joltik.html")

@app.route("/Galvantula")
def Galvantula():
    return render_template("/pokedex/Galvantula.html")

@app.route("/Ferroseed")
def Ferroseed():
    return render_template("/pokedex/Ferroseed.html")

@app.route("/Ferrothorn")
def Ferrothorn():
    return render_template("/pokedex/Ferrothorn.html")

@app.route("/Klink")
def Klink():
    return render_template("/pokedex/Klink.html")

@app.route("/Klang")
def Klang():
    return render_template("/pokedex/Klang.html")

@app.route("/Klinklang")
def Klinklang():
    return render_template("/pokedex/Klinklang.html")

@app.route("/Tynamo")
def Tynamo():
    return render_template("/pokedex/Tynamo.html")

@app.route("/Eelektrik")
def Eelektrik():
    return render_template("/pokedex/Eelektrik.html")

@app.route("/Eelektross")
def Eelektross():
    return render_template("/pokedex/Eelektross.html")

@app.route("/Elgyem")
def Elgyem():
    return render_template("/pokedex/Elgyem.html")

@app.route("/Beheeyem")
def Beheeyem():
    return render_template("/pokedex/Beheeyem.html")

@app.route("/Litwick")
def Litwick():
    return render_template("/pokedex/Litwick.html")

@app.route("/Lampent")
def Lampent():
    return render_template("/pokedex/Lampent.html")

@app.route("/Chandelure")
def Chandelure():
    return render_template("/pokedex/Chandelure.html")

@app.route("/Axew")
def Axew():
    return render_template("/pokedex/Axew.html")

@app.route("/Fraxure")
def Fraxure():
    return render_template("/pokedex/Fraxure.html")

@app.route("/Haxorus")
def Haxorus():
    return render_template("/pokedex/Haxorus.html")

@app.route("/Cubchoo")
def Cubchoo():
    return render_template("/pokedex/Cubchoo.html")

@app.route("/Beartic")
def Beartic():
    return render_template("/pokedex/Beartic.html")

@app.route("/Cryogonal")
def Cryogonal():
    return render_template("/pokedex/Cryogonal.html")

@app.route("/Shelmet")
def Shelmet():
    return render_template("/pokedex/Shelmet.html")

@app.route("/Accelgor")
def Accelgor():
    return render_template("/pokedex/Accelgor.html")

@app.route("/Stunfisk")
def Stunfisk():
    return render_template("/pokedex/Stunfisk.html")

@app.route("/StunfiskGalar")
def StunfiskGalar():
    return render_template("/pokedex/StunfiskGalar.html")

@app.route("/Mienfoo")
def Mienfoo():
    return render_template("/pokedex/Mienfoo.html")

@app.route("/Mienshao")
def Mienshao():
    return render_template("/pokedex/Mienshao.html")

@app.route("/Druddigon")
def Druddigon():
    return render_template("/pokedex/Druddigon.html")

@app.route("/Golett")
def Golett():
    return render_template("/pokedex/Golett.html")

@app.route("/Golurk")
def Golurk():
    return render_template("/pokedex/Golurk.html")

@app.route("/Pawniard")
def Pawniard():
    return render_template("/pokedex/Pawniard.html")

@app.route("/Bisharp")
def Bisharp():
    return render_template("/pokedex/Bisharp.html")

@app.route("/Bouffalant")
def Bouffalant():
    return render_template("/pokedex/Bouffalant.html")

@app.route("/Rufflet")
def Rufflet():
    return render_template("/pokedex/Rufflet.html")

@app.route("/Braviary")
def Braviary():
    return render_template("/pokedex/Braviary.html")

@app.route("/BraviaryHisui")
def BraviaryHisui():
    return render_template("/pokedex/BraviaryHisui.html")

@app.route("/Vullaby")
def Vullaby():
    return render_template("/pokedex/Vullaby.html")

@app.route("/Mandibuzz")
def Mandibuzz():
    return render_template("/pokedex/Mandibuzz.html")

@app.route("/Heatmor")
def Heatmor():
    return render_template("/pokedex/Heatmor.html")

@app.route("/Durant")
def Durant():
    return render_template("/pokedex/Durant.html")

@app.route("/Deino")
def Deino():
    return render_template("/pokedex/Deino.html")

@app.route("/Zweilous")
def Zweilous():
    return render_template("/pokedex/Zweilous.html")

@app.route("/Hydreigon")
def Hydreigon():
    return render_template("/pokedex/Hydreigon.html")

@app.route("/Larvesta")
def Larvesta():
    return render_template("/pokedex/Larvesta.html")

@app.route("/Volcarona")
def Volcarona():
    return render_template("/pokedex/Volcarona.html")

@app.route("/Cobalion")
def Cobalion():
    return render_template("/pokedex/Cobalion.html")

@app.route("/Terrakion")
def Terrakion():
    return render_template("/pokedex/Terrakion.html")

@app.route("/Virizion")
def Virizion():
    return render_template("/pokedex/Virizion.html")

@app.route("/Tornadus")
def Tornadus():
    return render_template("/pokedex/Tornadus.html")

@app.route("/TornadusTherian")
def TornadusTherian():
    return render_template("/pokedex/TornadusTherian.html")

@app.route("/Thundurus")
def Thundurus():
    return render_template("/pokedex/Thundurus.html")

@app.route("/ThundurusTherian")
def ThundurusTherian():
    return render_template("/pokedex/ThundurusTherian.html")

@app.route("/Reshiram")
def Reshiram():
    return render_template("/pokedex/Reshiram.html")

@app.route("/Zekrom")
def Zekrom():
    return render_template("/pokedex/Zekrom.html")

@app.route("/Landorus")
def Landorus():
    return render_template("/pokedex/Landorus.html")

@app.route("/LandorusTherian")
def LandorusTherian():
    return render_template("/pokedex/LandorusTherian.html")

@app.route("/Kyurem")
def Kyurem():
    return render_template("/pokedex/Kyurem.html")

@app.route("/KyuremWhite")
def KyuremWhite():
    return render_template("/pokedex/KyuremWhite.html")

@app.route("/KyuremBlack")
def KyuremBlack():
    return render_template("/pokedex/KyuremBlack.html")

@app.route("/Keldeo")
def Keldeo():
    return render_template("/pokedex/Keldeo.html")

@app.route("/KeldeoResolute")
def KeldeoResolute():
    return render_template("/pokedex/KeldeoResolute.html")

@app.route("/Meloetta")
def Meloetta():
    return render_template("/pokedex/Meloetta.html")

@app.route("/MeloettaPirouette")
def MeloettaPirouette():
    return render_template("/pokedex/MeloettaPirouette.html")

@app.route("/Genesect")
def Genesect():
    return render_template("/pokedex/Genesect.html")

@app.route("/Chespin")
def Chespin():
    return render_template("/pokedex/Chespin.html")

@app.route("/Quilladin")
def Quilladin():
    return render_template("/pokedex/Quilladin.html")

@app.route("/Chesnaught")
def Chesnaught():
    return render_template("/pokedex/Chesnaught.html")

@app.route("/Fennekin")
def Fennekin():
    return render_template("/pokedex/Fennekin.html")

@app.route("/Braixen")
def Braixen():
    return render_template("/pokedex/Braixen.html")

@app.route("/Delphox")
def Delphox():
    return render_template("/pokedex/Delphox.html")

@app.route("/Froakie")
def Froakie():
    return render_template("/pokedex/Froakie.html")

@app.route("/Frogadier")
def Frogadier():
    return render_template("/pokedex/Frogadier.html")

@app.route("/Greninja")
def Greninja():
    return render_template("/pokedex/Greninja.html")

@app.route("/GreninjaAsh")
def GreninjaAsh():
    return render_template("/pokedex/GreninjaAsh.html")

@app.route("/Bunnelby")
def Bunnelby():
    return render_template("/pokedex/Bunnelby.html")

@app.route("/Diggersby")
def Diggersby():
    return render_template("/pokedex/Diggersby.html")

@app.route("/Fletchling")
def Fletchling():
    return render_template("/pokedex/Fletchling.html")

@app.route("/Fletchinder")
def Fletchinder():
    return render_template("/pokedex/Fletchinder.html")

@app.route("/Talonflame")
def Talonflame():
    return render_template("/pokedex/Talonflame.html")

@app.route("/Scatterbug")
def Scatterbug():
    return render_template("/pokedex/Scatterbug.html")

@app.route("/Spewpa")
def Spewpa():
    return render_template("/pokedex/Spewpa.html")

@app.route("/Vivillon")
def Vivillon():
    return render_template("/pokedex/Vivillon.html")

@app.route("/VivillonPolarPattern")
def VivillonPolarPattern():
    return render_template("/pokedex/VivillonPolarPattern.html")

@app.route("/VivillonTundraPattern")
def VivillonTundraPattern():
    return render_template("/pokedex/VivillonTundraPattern.html")

@app.route("/VivillonContinentalPattern")
def VivillonContinentalPattern():
    return render_template("/pokedex/VivillonContinentalPattern.html")

@app.route("/VivillonGardenPattern")
def VivillonGardenPattern():
    return render_template("/pokedex/VivillonGardenPattern.html")

@app.route("/VivillonElegantPattern")
def VivillonElegantPattern():
    return render_template("/pokedex/VivillonElegantPattern.html")

@app.route("/VivillonIcySnowPattern")
def VivillonIcySnowPattern():
    return render_template("/pokedex/VivillonIcySnowPattern.html")

@app.route("/VivillonModernPattern")
def VivillonModernPattern():
    return render_template("/pokedex/VivillonModernPattern.html")

@app.route("/VivillonMarinePattern")
def VivillonMarinePattern():
    return render_template("/pokedex/VivillonMarinePattern.html")

@app.route("/VivillonArchipelagoPattern")
def VivillonArchipelagoPattern():
    return render_template("/pokedex/VivillonArchipelagoPattern.html")

@app.route("/VivillonHighPlainsPattern")
def VivillonHighPlainsPattern():
    return render_template("/pokedex/VivillonHighPlainsPattern.html")

@app.route("/VivillonSandstormPattern")
def VivillonSandstormPattern():
    return render_template("/pokedex/VivillonSandstormPattern.html")

@app.route("/VivillonRiverPattern")
def VivillonRiverPattern():
    return render_template("/pokedex/VivillonRiverPattern.html")

@app.route("/VivillonMonsoonPattern")
def VivillonMonsoonPattern():
    return render_template("/pokedex/VivillonMonsoonPattern.html")

@app.route("/VivillonSavannaPattern")
def VivillonSavannaPattern():
    return render_template("/pokedex/VivillonSavannaPattern.html")

@app.route("/VivillonSunPattern")
def VivillonSunPattern():
    return render_template("/pokedex/VivillonSunPattern.html")

@app.route("/VivillonOceanPattern")
def VivillonOceanPattern():
    return render_template("/pokedex/VivillonOceanPattern.html")

@app.route("/VivillonJunglePattern")
def VivillonJunglePattern():
    return render_template("/pokedex/VivillonJunglePattern.html")

@app.route("/VivillonFancyPattern")
def VivillonFancyPattern():
    return render_template("/pokedex/VivillonFancyPattern.html")

@app.route("/VivillonPokeBallPattern")
def VivillonPokeBallPattern():
    return render_template("/pokedex/VivillonPokeBallPattern.html")

@app.route("/Litleo")
def Litleo():
    return render_template("/pokedex/Litleo.html")

@app.route("/Pyroar")
def Pyroar():
    return render_template("/pokedex/Pyroar.html")

@app.route("/Flabebe")
def Flabebe():
    return render_template("/pokedex/Flabebe.html")

@app.route("/FlabebeYellowFlower")
def FlabebeYellowFlower():
    return render_template("/pokedex/FlabebeYellowFlower.html")

@app.route("/FlabebeOrangeFlower")
def FlabebeOrangeFlower():
    return render_template("/pokedex/FlabebeOrangeFlower.html")

@app.route("/FlabebeBlueFlower")
def FlabebeBlueFlower():
    return render_template("/pokedex/FlabebeBlueFlower.html")

@app.route("/FlabebeWhiteFlower")
def FlabebeWhiteFlower():
    return render_template("/pokedex/FlabebeWhiteFlower.html")

@app.route("/Floette")
def Floette():
    return render_template("/pokedex/Floette.html")

@app.route("/FloetteYellowFlower")
def FloetteYellowFlower():
    return render_template("/pokedex/FloetteYellowFlower.html")

@app.route("/FloetteOrangeFlower")
def FloetteOrangeFlower():
    return render_template("/pokedex/FloetteOrangeFlower.html")

@app.route("/FloetteBlueFlower")
def FloetteBlueFlower():
    return render_template("/pokedex/FloetteBlueFlower.html")

@app.route("/FloetteWhiteFlower")
def FloetteWhiteFlower():
    return render_template("/pokedex/FloetteWhiteFlower.html")

@app.route("/Florges")
def Florges():
    return render_template("/pokedex/Florges.html")

@app.route("/FlorgesYellowFlower")
def FlorgesYellowFlower():
    return render_template("/pokedex/FlorgesYellowFlower.html")

@app.route("/FlorgesOrangeFlower")
def FlorgesOrangeFlower():
    return render_template("/pokedex/FlorgesOrangeFlower.html")

@app.route("/FlorgesBlueFlower")
def FlorgesBlueFlower():
    return render_template("/pokedex/FlorgesBlueFlower.html")

@app.route("/FlorgesWhiteFlower")
def FlorgesWhiteFlower():
    return render_template("/pokedex/FlorgesWhiteFlower.html")

@app.route("/Skiddo")
def Skiddo():
    return render_template("/pokedex/Skiddo.html")

@app.route("/Gogoat")
def Gogoat():
    return render_template("/pokedex/Gogoat.html")

@app.route("/Pancham")
def Pancham():
    return render_template("/pokedex/Pancham.html")

@app.route("/Pangoro")
def Pangoro():
    return render_template("/pokedex/Pangoro.html")

@app.route("/Furfrou")
def Furfrou():
    return render_template("/pokedex/Furfrou.html")

@app.route("/FurfrouHeartTrim")
def FurfrouHeartTrim():
    return render_template("/pokedex/FurfrouHeartTrim.html")

@app.route("/FurfrouStarTrim")
def FurfrouStarTrim():
    return render_template("/pokedex/FurfrouStarTrim.html")

@app.route("/FurfrouDiamondTrim")
def FurfrouDiamondTrim():
    return render_template("/pokedex/FurfrouDiamondTrim.html")

@app.route("/FurfrouDebutanteTrim")
def FurfrouDebutanteTrim():
    return render_template("/pokedex/FurfrouDebutanteTrim.html")

@app.route("/FurfrouMatronTrim")
def FurfrouMatronTrim():
    return render_template("/pokedex/FurfrouMatronTrim.html")

@app.route("/FurfrouDandyTrim")
def FurfrouDandyTrim():
    return render_template("/pokedex/FurfrouDandyTrim.html")

@app.route("/FurfrouLaReineTrim")
def FurfrouLaReineTrim():
    return render_template("/pokedex/FurfrouLaReineTrim.html")

@app.route("/FurfrouKabukiTrim")
def FurfrouKabukiTrim():
    return render_template("/pokedex/FurfrouKabukiTrim.html")

@app.route("/FurfrouPharaohTrim")
def FurfrouPharaohTrim():
    return render_template("/pokedex/FurfrouPharaohTrim.html")

@app.route("/Espurr")
def Espurr():
    return render_template("/pokedex/Espurr.html")

@app.route("/Meowstic")
def Meowstic():
    return render_template("/pokedex/Meowstic.html")

@app.route("/MeowsticFemale")
def MeowsticFemale():
    return render_template("/pokedex/MeowsticFemale.html")

@app.route("/Honedge")
def Honedge():
    return render_template("/pokedex/Honedge.html")

@app.route("/Doublade")
def Doublade():
    return render_template("/pokedex/Doublade.html")

@app.route("/Aegislash")
def Aegislash():
    return render_template("/pokedex/Aegislash.html")

@app.route("/AegislashBlade")
def AegislashBlade():
    return render_template("/pokedex/AegislashBlade.html")

@app.route("/Spritzee")
def Spritzee():
    return render_template("/pokedex/Spritzee.html")

@app.route("/Aromatisse")
def Aromatisse():
    return render_template("/pokedex/Aromatisse.html")

@app.route("/Swirlix")
def Swirlix():
    return render_template("/pokedex/Swirlix.html")

@app.route("/Slurpuff")
def Slurpuff():
    return render_template("/pokedex/Slurpuff.html")

@app.route("/Inkay")
def Inkay():
    return render_template("/pokedex/Inkay.html")

@app.route("/Malamar")
def Malamar():
    return render_template("/pokedex/Malamar.html")

@app.route("/Binacle")
def Binacle():
    return render_template("/pokedex/Binacle.html")

@app.route("/Barbaracle")
def Barbaracle():
    return render_template("/pokedex/Barbaracle.html")

@app.route("/Skrelp")
def Skrelp():
    return render_template("/pokedex/Skrelp.html")

@app.route("/Dragalge")
def Dragalge():
    return render_template("/pokedex/Dragalge.html")

@app.route("/Clauncher")
def Clauncher():
    return render_template("/pokedex/Clauncher.html")

@app.route("/Clawitzer")
def Clawitzer():
    return render_template("/pokedex/Clawitzer.html")

@app.route("/Helioptile")
def Helioptile():
    return render_template("/pokedex/Helioptile.html")

@app.route("/Heliolisk")
def Heliolisk():
    return render_template("/pokedex/Heliolisk.html")

@app.route("/Tyrunt")
def Tyrunt():
    return render_template("/pokedex/Tyrunt.html")

@app.route("/Tyrantrum")
def Tyrantrum():
    return render_template("/pokedex/Tyrantrum.html")

@app.route("/Amaura")
def Amaura():
    return render_template("/pokedex/Amaura.html")

@app.route("/Aurorus")
def Aurorus():
    return render_template("/pokedex/Aurorus.html")

@app.route("/Sylveon")
def Sylveon():
    return render_template("/pokedex/Sylveon.html")

@app.route("/Hawlucha")
def Hawlucha():
    return render_template("/pokedex/Hawlucha.html")

@app.route("/Dedenne")
def Dedenne():
    return render_template("/pokedex/Dedenne.html")

@app.route("/Carbink")
def Carbink():
    return render_template("/pokedex/Carbink.html")

@app.route("/Goomy")
def Goomy():
    return render_template("/pokedex/Goomy.html")

@app.route("/Sliggoo")
def Sliggoo():
    return render_template("/pokedex/Sliggoo.html")

@app.route("/SliggooHisui")
def SliggooHisui():
    return render_template("/pokedex/SliggooHisui.html")

@app.route("/Goodra")
def Goodra():
    return render_template("/pokedex/Goodra.html")

@app.route("/GoodraHisui")
def GoodraHisui():
    return render_template("/pokedex/GoodraHisui.html")

@app.route("/Klefki")
def Klefki():
    return render_template("/pokedex/Klefki.html")

@app.route("/Phantump")
def Phantump():
    return render_template("/pokedex/Phantump.html")

@app.route("/Trevenant")
def Trevenant():
    return render_template("/pokedex/Trevenant.html")

@app.route("/Pumpkaboo")
def Pumpkaboo():
    return render_template("/pokedex/Pumpkaboo.html")

@app.route("/PumpkabooSmallSize")
def PumpkabooSmallSize():
    return render_template("/pokedex/PumpkabooSmallSize.html")

@app.route("/PumpkabooLargeSize")
def PumpkabooLargeSize():
    return render_template("/pokedex/PumpkabooLargeSize.html")

@app.route("/PumpkabooSuperSize")
def PumpkabooSuperSize():
    return render_template("/pokedex/PumpkabooSuperSize.html")

@app.route("/Gourgeist")
def Gourgeist():
    return render_template("/pokedex/Gourgeist.html")

@app.route("/GourgeistSmallSize")
def GourgeistSmallSize():
    return render_template("/pokedex/GourgeistSmallSize.html")

@app.route("/GourgeistLargeSize")
def GourgeistLargeSize():
    return render_template("/pokedex/GourgeistLargeSize.html")

@app.route("/GourgeistSuperSize")
def GourgeistSuperSize():
    return render_template("/pokedex/GourgeistSuperSize.html")

@app.route("/Bergmite")
def Bergmite():
    return render_template("/pokedex/Bergmite.html")

@app.route("/AvaluggHisui")
def AvaluggHisui():
    return render_template("/pokedex/AvaluggHisui.html")

@app.route("/Avalugg")
def Avalugg():
    return render_template("/pokedex/Avalugg.html")

@app.route("/Noibat")
def Noibat():
    return render_template("/pokedex/Noibat.html")

@app.route("/Noivern")
def Noivern():
    return render_template("/pokedex/Noivern.html")

@app.route("/Xerneas")
def Xerneas():
    return render_template("/pokedex/Xerneas.html")

@app.route("/Yveltal")
def Yveltal():
    return render_template("/pokedex/Yveltal.html")

@app.route("/Zygarde")
def Zygarde():
    return render_template("/pokedex/Zygarde.html")

@app.route("/Zygarde10Pct")
def Zygarde10Pct():
    return render_template("/pokedex/Zygarde10Pct.html")

@app.route("/ZygardeComplete")
def ZygardeComplete():
    return render_template("/pokedex/ZygardeComplete.html")

@app.route("/DiancieMega")
def DiancieMega():
    return render_template("/pokedex/DiancieMega.html")

@app.route("/Diancie")
def Diancie():
    return render_template("/pokedex/Diancie.html")

@app.route("/Hoopa")
def Hoopa():
    return render_template("/pokedex/Hoopa.html")

@app.route("/HoopaUnbound")
def HoopaUnbound():
    return render_template("/pokedex/HoopaUnbound.html")

@app.route("/Volcanion")
def Volcanion():
    return render_template("/pokedex/Volcanion.html")

@app.route("/Rowlet")
def Rowlet():
    return render_template("/pokedex/Rowlet.html")

@app.route("/Dartrix")
def Dartrix():
    return render_template("/pokedex/Dartrix.html")

@app.route("/Decidueye")
def Decidueye():
    return render_template("/pokedex/Decidueye.html")

@app.route("/DecidueyeHisui")
def DecidueyeHisui():
    return render_template("/pokedex/DecidueyeHisui.html")

@app.route("/Litten")
def Litten():
    return render_template("/pokedex/Litten.html")

@app.route("/Torracat")
def Torracat():
    return render_template("/pokedex/Torracat.html")

@app.route("/Incineroar")
def Incineroar():
    return render_template("/pokedex/Incineroar.html")

@app.route("/Popplio")
def Popplio():
    return render_template("/pokedex/Popplio.html")

@app.route("/Brionne")
def Brionne():
    return render_template("/pokedex/Brionne.html")

@app.route("/Primarina")
def Primarina():
    return render_template("/pokedex/Primarina.html")

@app.route("/Pikipek")
def Pikipek():
    return render_template("/pokedex/Pikipek.html")

@app.route("/Trumbeak")
def Trumbeak():
    return render_template("/pokedex/Trumbeak.html")

@app.route("/Toucannon")
def Toucannon():
    return render_template("/pokedex/Toucannon.html")

@app.route("/Yungoos")
def Yungoos():
    return render_template("/pokedex/Yungoos.html")

@app.route("/Gumshoos")
def Gumshoos():
    return render_template("/pokedex/Gumshoos.html")

@app.route("/Grubbin")
def Grubbin():
    return render_template("/pokedex/Grubbin.html")

@app.route("/Charjabug")
def Charjabug():
    return render_template("/pokedex/Charjabug.html")

@app.route("/Vikavolt")
def Vikavolt():
    return render_template("/pokedex/Vikavolt.html")

@app.route("/Crabrawler")
def Crabrawler():
    return render_template("/pokedex/Crabrawler.html")

@app.route("/Crabominable")
def Crabominable():
    return render_template("/pokedex/Crabominable.html")

@app.route("/Oricorio")
def Oricorio():
    return render_template("/pokedex/Oricorio.html")

@app.route("/OricorioPomPom")
def OricorioPomPom():
    return render_template("/pokedex/OricorioPomPom.html")

@app.route("/OricorioPau")
def OricorioPau():
    return render_template("/pokedex/OricorioPau.html")

@app.route("/OricorioSensu")
def OricorioSensu():
    return render_template("/pokedex/OricorioSensu.html")

@app.route("/Cutiefly")
def Cutiefly():
    return render_template("/pokedex/Cutiefly.html")

@app.route("/Ribombee")
def Ribombee():
    return render_template("/pokedex/Ribombee.html")

@app.route("/Rockruff")
def Rockruff():
    return render_template("/pokedex/Rockruff.html")

@app.route("/Lycanroc")
def Lycanroc():
    return render_template("/pokedex/Lycanroc.html")

@app.route("/LycanrocMidnight")
def LycanrocMidnight():
    return render_template("/pokedex/LycanrocMidnight.html")

@app.route("/LycanrocDusk")
def LycanrocDusk():
    return render_template("/pokedex/LycanrocDusk.html")

@app.route("/Wishiwashi")
def Wishiwashi():
    return render_template("/pokedex/Wishiwashi.html")

@app.route("/WishiwashiSchool")
def WishiwashiSchool():
    return render_template("/pokedex/WishiwashiSchool.html")

@app.route("/Mareanie")
def Mareanie():
    return render_template("/pokedex/Mareanie.html")

@app.route("/Toxapex")
def Toxapex():
    return render_template("/pokedex/Toxapex.html")

@app.route("/Mudbray")
def Mudbray():
    return render_template("/pokedex/Mudbray.html")

@app.route("/Mudsdale")
def Mudsdale():
    return render_template("/pokedex/Mudsdale.html")

@app.route("/Dewpider")
def Dewpider():
    return render_template("/pokedex/Dewpider.html")

@app.route("/Araquanid")
def Araquanid():
    return render_template("/pokedex/Araquanid.html")

@app.route("/Fomantis")
def Fomantis():
    return render_template("/pokedex/Fomantis.html")

@app.route("/Lurantis")
def Lurantis():
    return render_template("/pokedex/Lurantis.html")

@app.route("/Morelull")
def Morelull():
    return render_template("/pokedex/Morelull.html")

@app.route("/Shiinotic")
def Shiinotic():
    return render_template("/pokedex/Shiinotic.html")

@app.route("/Salandit")
def Salandit():
    return render_template("/pokedex/Salandit.html")

@app.route("/Salazzle")
def Salazzle():
    return render_template("/pokedex/Salazzle.html")

@app.route("/Stufful")
def Stufful():
    return render_template("/pokedex/Stufful.html")

@app.route("/Bewear")
def Bewear():
    return render_template("/pokedex/Bewear.html")

@app.route("/Bounsweet")
def Bounsweet():
    return render_template("/pokedex/Bounsweet.html")

@app.route("/Steenee")
def Steenee():
    return render_template("/pokedex/Steenee.html")

@app.route("/Tsareena")
def Tsareena():
    return render_template("/pokedex/Tsareena.html")

@app.route("/Comfey")
def Comfey():
    return render_template("/pokedex/Comfey.html")

@app.route("/Oranguru")
def Oranguru():
    return render_template("/pokedex/Oranguru.html")

@app.route("/Passimian")
def Passimian():
    return render_template("/pokedex/Passimian.html")

@app.route("/Wimpod")
def Wimpod():
    return render_template("/pokedex/Wimpod.html")

@app.route("/Golisopod")
def Golisopod():
    return render_template("/pokedex/Golisopod.html")

@app.route("/Sandygast")
def Sandygast():
    return render_template("/pokedex/Sandygast.html")

@app.route("/Palossand")
def Palossand():
    return render_template("/pokedex/Palossand.html")

@app.route("/Pyukumuku")
def Pyukumuku():
    return render_template("/pokedex/Pyukumuku.html")

@app.route("/TypeNull")
def TypeNull():
    return render_template("/pokedex/TypeNull.html")

@app.route("/Silvally")
def Silvally():
    return render_template("/pokedex/Silvally.html")

@app.route("/Minior")
def Minior():
    return render_template("/pokedex/Minior.html")

@app.route("/MiniorRedCore")
def MiniorRedCore():
    return render_template("/pokedex/MiniorRedCore.html")

@app.route("/MiniorOrangeCore")
def MiniorOrangeCore():
    return render_template("/pokedex/MiniorOrangeCore.html")

@app.route("/MiniorYellowCore")
def MiniorYellowCore():
    return render_template("/pokedex/MiniorYellowCore.html")

@app.route("/MiniorGreenCore")
def MiniorGreenCore():
    return render_template("/pokedex/MiniorGreenCore.html")

@app.route("/MiniorBlueCore")
def MiniorBlueCore():
    return render_template("/pokedex/MiniorBlueCore.html")

@app.route("/MiniorIndigoCore")
def MiniorIndigoCore():
    return render_template("/pokedex/MiniorIndigoCore.html")

@app.route("/MiniorVioletCore")
def MiniorVioletCore():
    return render_template("/pokedex/MiniorVioletCore.html")

@app.route("/Komala")
def Komala():
    return render_template("/pokedex/Komala.html")

@app.route("/Turtonator")
def Turtonator():
    return render_template("/pokedex/Turtonator.html")

@app.route("/Togedemaru")
def Togedemaru():
    return render_template("/pokedex/Togedemaru.html")

@app.route("/Mimikyu")
def Mimikyu():
    return render_template("/pokedex/Mimikyu.html")

@app.route("/Bruxish")
def Bruxish():
    return render_template("/pokedex/Bruxish.html")

@app.route("/Drampa")
def Drampa():
    return render_template("/pokedex/Drampa.html")

@app.route("/Dhelmise")
def Dhelmise():
    return render_template("/pokedex/Dhelmise.html")

@app.route("/Jangmoo")
def Jangmoo():
    return render_template("/pokedex/Jangmoo.html")

@app.route("/Hakamoo")
def Hakamoo():
    return render_template("/pokedex/Hakamoo.html")

@app.route("/Kommoo")
def Kommoo():
    return render_template("/pokedex/Kommoo.html")

@app.route("/TapuKoko")
def TapuKoko():
    return render_template("/pokedex/TapuKoko.html")

@app.route("/TapuLele")
def TapuLele():
    return render_template("/pokedex/TapuLele.html")

@app.route("/TapuBulu")
def TapuBulu():
    return render_template("/pokedex/TapuBulu.html")

@app.route("/TapuFini")
def TapuFini():
    return render_template("/pokedex/TapuFini.html")

@app.route("/Cosmog")
def Cosmog():
    return render_template("/pokedex/Cosmog.html")

@app.route("/Cosmoem")
def Cosmoem():
    return render_template("/pokedex/Cosmoem.html")

@app.route("/Solgaleo")
def Solgaleo():
    return render_template("/pokedex/Solgaleo.html")

@app.route("/Lunala")
def Lunala():
    return render_template("/pokedex/Lunala.html")

@app.route("/Nihilego")
def Nihilego():
    return render_template("/pokedex/Nihilego.html")

@app.route("/Buzzwole")
def Buzzwole():
    return render_template("/pokedex/Buzzwole.html")

@app.route("/Pheromosa")
def Pheromosa():
    return render_template("/pokedex/Pheromosa.html")

@app.route("/Xurkitree")
def Xurkitree():
    return render_template("/pokedex/Xurkitree.html")

@app.route("/Celesteela")
def Celesteela():
    return render_template("/pokedex/Celesteela.html")

@app.route("/Kartana")
def Kartana():
    return render_template("/pokedex/Kartana.html")

@app.route("/Guzzlord")
def Guzzlord():
    return render_template("/pokedex/Guzzlord.html")

@app.route("/NecrozmaDuskMane")
def NecrozmaDuskMane():
    return render_template("/pokedex/NecrozmaDuskMane.html")

@app.route("/NecrozmaDawnWings")
def NecrozmaDawnWings():
    return render_template("/pokedex/NecrozmaDawnWings.html")

@app.route("/NecrozmaUltra")
def NecrozmaUltra():
    return render_template("/pokedex/NecrozmaUltra.html")

@app.route("/Necrozma")
def Necrozma():
    return render_template("/pokedex/Necrozma.html")

@app.route("/Magearna")
def Magearna():
    return render_template("/pokedex/Magearna.html")

@app.route("/MagearnaOriginalColor")
def MagearnaOriginalColor():
    return render_template("/pokedex/MagearnaOriginalColor.html")

@app.route("/Marshadow")
def Marshadow():
    return render_template("/pokedex/Marshadow.html")

@app.route("/Poipole")
def Poipole():
    return render_template("/pokedex/Poipole.html")

@app.route("/Naganadel")
def Naganadel():
    return render_template("/pokedex/Naganadel.html")

@app.route("/Stakataka")
def Stakataka():
    return render_template("/pokedex/Stakataka.html")

@app.route("/Blacephalon")
def Blacephalon():
    return render_template("/pokedex/Blacephalon.html")

@app.route("/Zeraora")
def Zeraora():
    return render_template("/pokedex/Zeraora.html")

@app.route("/Meltan")
def Meltan():
    return render_template("/pokedex/Meltan.html")

@app.route("/Melmetal")
def Melmetal():
    return render_template("/pokedex/Melmetal.html")

@app.route("/MelmetalGigantamax")
def MelmetalGigantamax():
    return render_template("/pokedex/MelmetalGigantamax.html")

@app.route("/Grookey")
def Grookey():
    return render_template("/pokedex/Grookey.html")

@app.route("/Thwackey")
def Thwackey():
    return render_template("/pokedex/Thwackey.html")

@app.route("/Rillaboom")
def Rillaboom():
    return render_template("/pokedex/Rillaboom.html")

@app.route("/RillaboomGigantamax")
def RillaboomGigantamax():
    return render_template("/pokedex/RillaboomGigantamax.html")

@app.route("/Scorbunny")
def Scorbunny():
    return render_template("/pokedex/Scorbunny.html")

@app.route("/Raboot")
def Raboot():
    return render_template("/pokedex/Raboot.html")

@app.route("/Cinderace")
def Cinderace():
    return render_template("/pokedex/Cinderace.html")

@app.route("/CinderaceGigantamax")
def CinderaceGigantamax():
    return render_template("/pokedex/CinderaceGigantamax.html")

@app.route("/Sobble")
def Sobble():
    return render_template("/pokedex/Sobble.html")

@app.route("/Drizzile")
def Drizzile():
    return render_template("/pokedex/Drizzile.html")

@app.route("/Inteleon")
def Inteleon():
    return render_template("/pokedex/Inteleon.html")

@app.route("/InteleonGigantamax")
def InteleonGigantamax():
    return render_template("/pokedex/InteleonGigantamax.html")

@app.route("/Skwovet")
def Skwovet():
    return render_template("/pokedex/Skwovet.html")

@app.route("/Greedent")
def Greedent():
    return render_template("/pokedex/Greedent.html")

@app.route("/Rookidee")
def Rookidee():
    return render_template("/pokedex/Rookidee.html")

@app.route("/Corvisquire")
def Corvisquire():
    return render_template("/pokedex/Corvisquire.html")

@app.route("/Corviknight")
def Corviknight():
    return render_template("/pokedex/Corviknight.html")

@app.route("/CorviknightGigantamax")
def CorviknightGigantamax():
    return render_template("/pokedex/CorviknightGigantamax.html")

@app.route("/Blipbug")
def Blipbug():
    return render_template("/pokedex/Blipbug.html")

@app.route("/Dottler")
def Dottler():
    return render_template("/pokedex/Dottler.html")

@app.route("/Orbeetle")
def Orbeetle():
    return render_template("/pokedex/Orbeetle.html")

@app.route("/OrbeetleGigantamax")
def OrbeetleGigantamax():
    return render_template("/pokedex/OrbeetleGigantamax.html")

@app.route("/Nickit")
def Nickit():
    return render_template("/pokedex/Nickit.html")

@app.route("/Thievul")
def Thievul():
    return render_template("/pokedex/Thievul.html")

@app.route("/Gossifleur")
def Gossifleur():
    return render_template("/pokedex/Gossifleur.html")

@app.route("/Eldegoss")
def Eldegoss():
    return render_template("/pokedex/Eldegoss.html")

@app.route("/Wooloo")
def Wooloo():
    return render_template("/pokedex/Wooloo.html")

@app.route("/Dubwool")
def Dubwool():
    return render_template("/pokedex/Dubwool.html")

@app.route("/Chewtle")
def Chewtle():
    return render_template("/pokedex/Chewtle.html")

@app.route("/Drednaw")
def Drednaw():
    return render_template("/pokedex/Drednaw.html")

@app.route("/DrednawGigantamax")
def DrednawGigantamax():
    return render_template("/pokedex/DrednawGigantamax.html")

@app.route("/Yamper")
def Yamper():
    return render_template("/pokedex/Yamper.html")

@app.route("/Boltund")
def Boltund():
    return render_template("/pokedex/Boltund.html")

@app.route("/Rolycoly")
def Rolycoly():
    return render_template("/pokedex/Rolycoly.html")

@app.route("/Carkol")
def Carkol():
    return render_template("/pokedex/Carkol.html")

@app.route("/Coalossal")
def Coalossal():
    return render_template("/pokedex/Coalossal.html")

@app.route("/CoalossalGigantamax")
def CoalossalGigantamax():
    return render_template("/pokedex/CoalossalGigantamax.html")

@app.route("/Applin")
def Applin():
    return render_template("/pokedex/Applin.html")

@app.route("/Flapple")
def Flapple():
    return render_template("/pokedex/Flapple.html")

@app.route("/FlappleGigantamax")
def FlappleGigantamax():
    return render_template("/pokedex/FlappleGigantamax.html")

@app.route("/AppletunGigantamax")
def AppletunGigantamax():
    return render_template("/pokedex/AppletunGigantamax.html")

@app.route("/Appletun")
def Appletun():
    return render_template("/pokedex/Appletun.html")

@app.route("/Silicobra")
def Silicobra():
    return render_template("/pokedex/Silicobra.html")

@app.route("/Sandaconda")
def Sandaconda():
    return render_template("/pokedex/Sandaconda.html")

@app.route("/SandacondaGigantamax")
def SandacondaGigantamax():
    return render_template("/pokedex/SandacondaGigantamax.html")

@app.route("/Cramorant")
def Cramorant():
    return render_template("/pokedex/Cramorant.html")

@app.route("/Arrokuda")
def Arrokuda():
    return render_template("/pokedex/Arrokuda.html")

@app.route("/Barraskewda")
def Barraskewda():
    return render_template("/pokedex/Barraskewda.html")

@app.route("/Toxel")
def Toxel():
    return render_template("/pokedex/Toxel.html")

@app.route("/Toxtricity")
def Toxtricity():
    return render_template("/pokedex/Toxtricity.html")

@app.route("/ToxtricityLowKey")
def ToxtricityLowKey():
    return render_template("/pokedex/ToxtricityLowKey.html")

@app.route("/ToxtricityGigantamax")
def ToxtricityGigantamax():
    return render_template("/pokedex/ToxtricityGigantamax.html")

@app.route("/ToxtricityLowKeyGigantamax")
def ToxtricityLowKeyGigantamax():
    return render_template("/pokedex/ToxtricityLowKeyGigantamax.html")

@app.route("/Sizzlipede")
def Sizzlipede():
    return render_template("/pokedex/Sizzlipede.html")

@app.route("/Centiskorch")
def Centiskorch():
    return render_template("/pokedex/Centiskorch.html")

@app.route("/CentiskorchGigantamax")
def CentiskorchGigantamax():
    return render_template("/pokedex/CentiskorchGigantamax.html")

@app.route("/Clobbopus")
def Clobbopus():
    return render_template("/pokedex/Clobbopus.html")

@app.route("/Grapploct")
def Grapploct():
    return render_template("/pokedex/Grapploct.html")

@app.route("/Sinistea")
def Sinistea():
    return render_template("/pokedex/Sinistea.html")

@app.route("/SinisteaAntique")
def SinisteaAntique():
    return render_template("/pokedex/SinisteaAntique.html")

@app.route("/PolteageistAntique")
def PolteageistAntique():
    return render_template("/pokedex/PolteageistAntique.html")

@app.route("/Polteageist")
def Polteageist():
    return render_template("/pokedex/Polteageist.html")

@app.route("/Hatenna")
def Hatenna():
    return render_template("/pokedex/Hatenna.html")

@app.route("/Hattrem")
def Hattrem():
    return render_template("/pokedex/Hattrem.html")

@app.route("/Hatterene")
def Hatterene():
    return render_template("/pokedex/Hatterene.html")

@app.route("/HattereneGigantamax")
def HattereneGigantamax():
    return render_template("/pokedex/HattereneGigantamax.html")

@app.route("/Impidimp")
def Impidimp():
    return render_template("/pokedex/Impidimp.html")

@app.route("/Morgrem")
def Morgrem():
    return render_template("/pokedex/Morgrem.html")

@app.route("/Grimmsnarl")
def Grimmsnarl():
    return render_template("/pokedex/Grimmsnarl.html")

@app.route("/GrimmsnarlGigantamax")
def GrimmsnarlGigantamax():
    return render_template("/pokedex/GrimmsnarlGigantamax.html")

@app.route("/Obstagoon")
def Obstagoon():
    return render_template("/pokedex/Obstagoon.html")

@app.route("/Perrserker")
def Perrserker():
    return render_template("/pokedex/Perrserker.html")

@app.route("/Cursola")
def Cursola():
    return render_template("/pokedex/Cursola.html")

@app.route("/Sirfetchd")
def Sirfetchd():
    return render_template("/pokedex/Sirfetchd.html")

@app.route("/MrRime")
def MrRime():
    return render_template("/pokedex/MrRime.html")

@app.route("/Runerigus")
def Runerigus():
    return render_template("/pokedex/Runerigus.html")

@app.route("/Milcery")
def Milcery():
    return render_template("/pokedex/Milcery.html")

@app.route("/Alcremie")
def Alcremie():
    return render_template("/pokedex/Alcremie.html")

@app.route("/AlcremieRubyCream")
def AlcremieRubyCream():
    return render_template("/pokedex/AlcremieRubyCream.html")

@app.route("/AlcremieMatchaCream")
def AlcremieMatchaCream():
    return render_template("/pokedex/AlcremieMatchaCream.html")

@app.route("/AlcremieMintCream")
def AlcremieMintCream():
    return render_template("/pokedex/AlcremieMintCream.html")

@app.route("/AlcremieLemonCream")
def AlcremieLemonCream():
    return render_template("/pokedex/AlcremieLemonCream.html")

@app.route("/AlcremieSaltedCream")
def AlcremieSaltedCream():
    return render_template("/pokedex/AlcremieSaltedCream.html")

@app.route("/AlcremieRubySwirl")
def AlcremieRubySwirl():
    return render_template("/pokedex/AlcremieRubySwirl.html")

@app.route("/AlcremieCaramelSwirl")
def AlcremieCaramelSwirl():
    return render_template("/pokedex/AlcremieCaramelSwirl.html")

@app.route("/AlcremieRainbowSwirl")
def AlcremieRainbowSwirl():
    return render_template("/pokedex/AlcremieRainbowSwirl.html")

@app.route("/AlcremieGigantamax")
def AlcremieGigantamax():
    return render_template("/pokedex/AlcremieGigantamax.html")

@app.route("/Falinks")
def Falinks():
    return render_template("/pokedex/Falinks.html")

@app.route("/Pincurchin")
def Pincurchin():
    return render_template("/pokedex/Pincurchin.html")

@app.route("/Snom")
def Snom():
    return render_template("/pokedex/Snom.html")

@app.route("/Frosmoth")
def Frosmoth():
    return render_template("/pokedex/Frosmoth.html")

@app.route("/Stonjourner")
def Stonjourner():
    return render_template("/pokedex/Stonjourner.html")

@app.route("/Eiscue")
def Eiscue():
    return render_template("/pokedex/Eiscue.html")

@app.route("/EiscueNoice")
def EiscueNoice():
    return render_template("/pokedex/EiscueNoice.html")

@app.route("/Indeedee")
def Indeedee():
    return render_template("/pokedex/Indeedee.html")

@app.route("/IndeedeeFemale")
def IndeedeeFemale():
    return render_template("/pokedex/IndeedeeFemale.html")

@app.route("/Morpeko")
def Morpeko():
    return render_template("/pokedex/Morpeko.html")

@app.route("/Cufant")
def Cufant():
    return render_template("/pokedex/Cufant.html")

@app.route("/Copperajah")
def Copperajah():
    return render_template("/pokedex/Copperajah.html")

@app.route("/CopperajahGigantamax")
def CopperajahGigantamax():
    return render_template("/pokedex/CopperajahGigantamax.html")

@app.route("/Dracozolt")
def Dracozolt():
    return render_template("/pokedex/Dracozolt.html")

@app.route("/Arctozolt")
def Arctozolt():
    return render_template("/pokedex/Arctozolt.html")

@app.route("/Dracovish")
def Dracovish():
    return render_template("/pokedex/Dracovish.html")

@app.route("/Arctovish")
def Arctovish():
    return render_template("/pokedex/Arctovish.html")

@app.route("/Duraludon")
def Duraludon():
    return render_template("/pokedex/Duraludon.html")

@app.route("/DuraludonGigantamax")
def DuraludonGigantamax():
    return render_template("/pokedex/DuraludonGigantamax.html")

@app.route("/Dreepy")
def Dreepy():
    return render_template("/pokedex/Dreepy.html")

@app.route("/Drakloak")
def Drakloak():
    return render_template("/pokedex/Drakloak.html")

@app.route("/Dragapult")
def Dragapult():
    return render_template("/pokedex/Dragapult.html")

@app.route("/Zacian")
def Zacian():
    return render_template("/pokedex/Zacian.html")

@app.route("/ZacianCrowned")
def ZacianCrowned():
    return render_template("/pokedex/ZacianCrowned.html")

@app.route("/Zamazenta")
def Zamazenta():
    return render_template("/pokedex/Zamazenta.html")

@app.route("/ZamazentaCrowned")
def ZamazentaCrowned():
    return render_template("/pokedex/ZamazentaCrowned.html")

@app.route("/Eternatus")
def Eternatus():
    return render_template("/pokedex/Eternatus.html")

@app.route("/EternatusEternamax")
def EternatusEternamax():
    return render_template("/pokedex/EternatusEternamax.html")

@app.route("/Kubfu")
def Kubfu():
    return render_template("/pokedex/Kubfu.html")

@app.route("/Urshifu")
def Urshifu():
    return render_template("/pokedex/Urshifu.html")

@app.route("/UrshifuRapidStrike")
def UrshifuRapidStrike():
    return render_template("/pokedex/UrshifuRapidStrike.html")

@app.route("/UrshifuGigantamax")
def UrshifuGigantamax():
    return render_template("/pokedex/UrshifuGigantamax.html")

@app.route("/UrshifuRapidStrikeGigantamax")
def UrshifuRapidStrikeGigantamax():
    return render_template("/pokedex/UrshifuRapidStrikeGigantamax.html")

@app.route("/Zarude")
def Zarude():
    return render_template("/pokedex/Zarude.html")

@app.route("/ZarudeDada")
def ZarudeDada():
    return render_template("/pokedex/ZarudeDada.html")

@app.route("/Regieleki")
def Regieleki():
    return render_template("/pokedex/Regieleki.html")

@app.route("/Regidrago")
def Regidrago():
    return render_template("/pokedex/Regidrago.html")

@app.route("/Glastrier")
def Glastrier():
    return render_template("/pokedex/Glastrier.html")

@app.route("/Spectrier")
def Spectrier():
    return render_template("/pokedex/Spectrier.html")

@app.route("/Calyrex")
def Calyrex():
    return render_template("/pokedex/Calyrex.html")

@app.route("/CalyrexIceRider")
def CalyrexIceRider():
    return render_template("/pokedex/CalyrexIceRider.html")

@app.route("/CalyrexShadowRider")
def CalyrexShadowRider():
    return render_template("/pokedex/CalyrexShadowRider.html")

@app.route("/Wyrdeer")
def Wyrdeer():
    return render_template("/pokedex/Wyrdeer.html")

@app.route("/Kleavor")
def Kleavor():
    return render_template("/pokedex/Kleavor.html")

@app.route("/Ursaluna")
def Ursaluna():
    return render_template("/pokedex/Ursaluna.html")

@app.route("/UrsalunaBloodmoon")
def UrsalunaBloodmoon():
    return render_template("/pokedex/UrsalunaBloodmoon.html")

@app.route("/BasculegionFemale")
def BasculegionFemale():
    return render_template("/pokedex/BasculegionFemale.html")

@app.route("/Basculegion")
def Basculegion():
    return render_template("/pokedex/Basculegion.html")

@app.route("/Sneasler")
def Sneasler():
    return render_template("/pokedex/Sneasler.html")

@app.route("/Overqwil")
def Overqwil():
    return render_template("/pokedex/Overqwil.html")

@app.route("/Enamorus")
def Enamorus():
    return render_template("/pokedex/Enamorus.html")

@app.route("/EnamorusTherian")
def EnamorusTherian():
    return render_template("/pokedex/EnamorusTherian.html")

@app.route("/Sprigatito")
def Sprigatito():
    return render_template("/pokedex/Sprigatito.html")

@app.route("/Floragato")
def Floragato():
    return render_template("/pokedex/Floragato.html")

@app.route("/Meowscarada")
def Meowscarada():
    return render_template("/pokedex/Meowscarada.html")

@app.route("/Fuecoco")
def Fuecoco():
    return render_template("/pokedex/Fuecoco.html")

@app.route("/Crocalor")
def Crocalor():
    return render_template("/pokedex/Crocalor.html")

@app.route("/Skeledirge")
def Skeledirge():
    return render_template("/pokedex/Skeledirge.html")

@app.route("/Quaxly")
def Quaxly():
    return render_template("/pokedex/Quaxly.html")

@app.route("/Quaxwell")
def Quaxwell():
    return render_template("/pokedex/Quaxwell.html")

@app.route("/Quaquaval")
def Quaquaval():
    return render_template("/pokedex/Quaquaval.html")

@app.route("/Lechonk")
def Lechonk():
    return render_template("/pokedex/Lechonk.html")

@app.route("/Oinkologne")
def Oinkologne():
    return render_template("/pokedex/Oinkologne.html")

@app.route("/OinkologneFemale")
def OinkologneFemale():
    return render_template("/pokedex/OinkologneFemale.html")

@app.route("/Tarountula")
def Tarountula():
    return render_template("/pokedex/Tarountula.html")

@app.route("/Spidops")
def Spidops():
    return render_template("/pokedex/Spidops.html")

@app.route("/Nymble")
def Nymble():
    return render_template("/pokedex/Nymble.html")

@app.route("/Lokix")
def Lokix():
    return render_template("/pokedex/Lokix.html")

@app.route("/Pawmi")
def Pawmi():
    return render_template("/pokedex/Pawmi.html")

@app.route("/Pawmo")
def Pawmo():
    return render_template("/pokedex/Pawmo.html")

@app.route("/Pawmot")
def Pawmot():
    return render_template("/pokedex/Pawmot.html")

@app.route("/Tandemaus")
def Tandemaus():
    return render_template("/pokedex/Tandemaus.html")

@app.route("/Maushold")
def Maushold():
    return render_template("/pokedex/Maushold.html")

@app.route("/MausholdFamilyofThree")
def MausholdFamilyofThree():
    return render_template("/pokedex/MausholdFamilyofThree.html")

@app.route("/Fidough")
def Fidough():
    return render_template("/pokedex/Fidough.html")

@app.route("/Dachsbun")
def Dachsbun():
    return render_template("/pokedex/Dachsbun.html")

@app.route("/Smoliv")
def Smoliv():
    return render_template("/pokedex/Smoliv.html")

@app.route("/Dolliv")
def Dolliv():
    return render_template("/pokedex/Dolliv.html")

@app.route("/Arboliva")
def Arboliva():
    return render_template("/pokedex/Arboliva.html")

@app.route("/Squawkabilly")
def Squawkabilly():
    return render_template("/pokedex/Squawkabilly.html")

@app.route("/SquawkabillyBluePlumage")
def SquawkabillyBluePlumage():
    return render_template("/pokedex/SquawkabillyBluePlumage.html")

@app.route("/SquawkabillyYellowPlumage")
def SquawkabillyYellowPlumage():
    return render_template("/pokedex/SquawkabillyYellowPlumage.html")

@app.route("/SquawkabillyWhitePlumage")
def SquawkabillyWhitePlumage():
    return render_template("/pokedex/SquawkabillyWhitePlumage.html")

@app.route("/Nacli")
def Nacli():
    return render_template("/pokedex/Nacli.html")

@app.route("/Naclstack")
def Naclstack():
    return render_template("/pokedex/Naclstack.html")

@app.route("/Garganacl")
def Garganacl():
    return render_template("/pokedex/Garganacl.html")

@app.route("/Charcadet")
def Charcadet():
    return render_template("/pokedex/Charcadet.html")

@app.route("/Armarouge")
def Armarouge():
    return render_template("/pokedex/Armarouge.html")

@app.route("/Ceruledge")
def Ceruledge():
    return render_template("/pokedex/Ceruledge.html")

@app.route("/Tadbulb")
def Tadbulb():
    return render_template("/pokedex/Tadbulb.html")

@app.route("/Bellibolt")
def Bellibolt():
    return render_template("/pokedex/Bellibolt.html")

@app.route("/Wattrel")
def Wattrel():
    return render_template("/pokedex/Wattrel.html")

@app.route("/Kilowattrel")
def Kilowattrel():
    return render_template("/pokedex/Kilowattrel.html")

@app.route("/Maschiff")
def Maschiff():
    return render_template("/pokedex/Maschiff.html")

@app.route("/Mabosstiff")
def Mabosstiff():
    return render_template("/pokedex/Mabosstiff.html")

@app.route("/Shroodle")
def Shroodle():
    return render_template("/pokedex/Shroodle.html")

@app.route("/Grafaiai")
def Grafaiai():
    return render_template("/pokedex/Grafaiai.html")

@app.route("/Bramblin")
def Bramblin():
    return render_template("/pokedex/Bramblin.html")

@app.route("/Brambleghast")
def Brambleghast():
    return render_template("/pokedex/Brambleghast.html")

@app.route("/Toedscool")
def Toedscool():
    return render_template("/pokedex/Toedscool.html")

@app.route("/Toedscruel")
def Toedscruel():
    return render_template("/pokedex/Toedscruel.html")

@app.route("/Klawf")
def Klawf():
    return render_template("/pokedex/Klawf.html")

@app.route("/Capsakid")
def Capsakid():
    return render_template("/pokedex/Capsakid.html")

@app.route("/Scovillain")
def Scovillain():
    return render_template("/pokedex/Scovillain.html")

@app.route("/Rellor")
def Rellor():
    return render_template("/pokedex/Rellor.html")

@app.route("/Rabsca")
def Rabsca():
    return render_template("/pokedex/Rabsca.html")

@app.route("/Flittle")
def Flittle():
    return render_template("/pokedex/Flittle.html")

@app.route("/Espathra")
def Espathra():
    return render_template("/pokedex/Espathra.html")

@app.route("/Tinkatink")
def Tinkatink():
    return render_template("/pokedex/Tinkatink.html")

@app.route("/Tinkatuff")
def Tinkatuff():
    return render_template("/pokedex/Tinkatuff.html")

@app.route("/Tinkaton")
def Tinkaton():
    return render_template("/pokedex/Tinkaton.html")

@app.route("/Wiglett")
def Wiglett():
    return render_template("/pokedex/Wiglett.html")

@app.route("/Wugtrio")
def Wugtrio():
    return render_template("/pokedex/Wugtrio.html")

@app.route("/Bombirdier")
def Bombirdier():
    return render_template("/pokedex/Bombirdier.html")

@app.route("/Finizen")
def Finizen():
    return render_template("/pokedex/Finizen.html")

@app.route("/Palafin")
def Palafin():
    return render_template("/pokedex/Palafin.html")

@app.route("/PalafinHero")
def PalafinHero():
    return render_template("/pokedex/PalafinHero.html")

@app.route("/Varoom")
def Varoom():
    return render_template("/pokedex/Varoom.html")

@app.route("/Revavroom")
def Revavroom():
    return render_template("/pokedex/Revavroom.html")

@app.route("/Cyclizar")
def Cyclizar():
    return render_template("/pokedex/Cyclizar.html")

@app.route("/Orthworm")
def Orthworm():
    return render_template("/pokedex/Orthworm.html")

@app.route("/Glimmet")
def Glimmet():
    return render_template("/pokedex/Glimmet.html")

@app.route("/Glimmora")
def Glimmora():
    return render_template("/pokedex/Glimmora.html")

@app.route("/Greavard")
def Greavard():
    return render_template("/pokedex/Greavard.html")

@app.route("/Houndstone")
def Houndstone():
    return render_template("/pokedex/Houndstone.html")

@app.route("/Flamigo")
def Flamigo():
    return render_template("/pokedex/Flamigo.html")

@app.route("/Cetoddle")
def Cetoddle():
    return render_template("/pokedex/Cetoddle.html")

@app.route("/Cetitan")
def Cetitan():
    return render_template("/pokedex/Cetitan.html")

@app.route("/Veluza")
def Veluza():
    return render_template("/pokedex/Veluza.html")

@app.route("/Dondozo")
def Dondozo():
    return render_template("/pokedex/Dondozo.html")

@app.route("/Tatsugiri")
def Tatsugiri():
    return render_template("/pokedex/Tatsugiri.html")

@app.route("/TatsugiriDroppy")
def TatsugiriDroppy():
    return render_template("/pokedex/TatsugiriDroppy.html")

@app.route("/TatsugiriStretchy")
def TatsugiriStretchy():
    return render_template("/pokedex/TatsugiriStretchy.html")

@app.route("/Annihilape")
def Annihilape():
    return render_template("/pokedex/Annihilape.html")

@app.route("/Clodsire")
def Clodsire():
    return render_template("/pokedex/Clodsire.html")

@app.route("/Farigiraf")
def Farigiraf():
    return render_template("/pokedex/Farigiraf.html")

@app.route("/Dudunsparce")
def Dudunsparce():
    return render_template("/pokedex/Dudunsparce.html")

@app.route("/DudunsparceThreeSegment")
def DudunsparceThreeSegment():
    return render_template("/pokedex/DudunsparceThreeSegment.html")

@app.route("/Kingambit")
def Kingambit():
    return render_template("/pokedex/Kingambit.html")

@app.route("/GreatTusk")
def GreatTusk():
    return render_template("/pokedex/GreatTusk.html")

@app.route("/ScreamTail")
def ScreamTail():
    return render_template("/pokedex/ScreamTail.html")

@app.route("/BruteBonnet")
def BruteBonnet():
    return render_template("/pokedex/BruteBonnet.html")

@app.route("/FlutterMane")
def FlutterMane():
    return render_template("/pokedex/FlutterMane.html")

@app.route("/SlitherWing")
def SlitherWing():
    return render_template("/pokedex/SlitherWing.html")

@app.route("/SandyShocks")
def SandyShocks():
    return render_template("/pokedex/SandyShocks.html")

@app.route("/IronTreads")
def IronTreads():
    return render_template("/pokedex/IronTreads.html")

@app.route("/IronBundle")
def IronBundle():
    return render_template("/pokedex/IronBundle.html")

@app.route("/IronHands")
def IronHands():
    return render_template("/pokedex/IronHands.html")

@app.route("/IronJugulis")
def IronJugulis():
    return render_template("/pokedex/IronJugulis.html")

@app.route("/IronMoth")
def IronMoth():
    return render_template("/pokedex/IronMoth.html")

@app.route("/IronThorns")
def IronThorns():
    return render_template("/pokedex/IronThorns.html")

@app.route("/Frigibax")
def Frigibax():
    return render_template("/pokedex/Frigibax.html")

@app.route("/Arctibax")
def Arctibax():
    return render_template("/pokedex/Arctibax.html")

@app.route("/Baxcalibur")
def Baxcalibur():
    return render_template("/pokedex/Baxcalibur.html")

@app.route("/Gimmighoul")
def Gimmighoul():
    return render_template("/pokedex/Gimmighoul.html")

@app.route("/GimmighoulRoaming")
def GimmighoulRoaming():
    return render_template("/pokedex/GimmighoulRoaming.html")

@app.route("/Gholdengo")
def Gholdengo():
    return render_template("/pokedex/Gholdengo.html")

@app.route("/WoChien")
def WoChien():
    return render_template("/pokedex/WoChien.html")

@app.route("/ChienPao")
def ChienPao():
    return render_template("/pokedex/ChienPao.html")

@app.route("/TingLu")
def TingLu():
    return render_template("/pokedex/TingLu.html")

@app.route("/ChiYu")
def ChiYu():
    return render_template("/pokedex/ChiYu.html")

@app.route("/RoaringMoon")
def RoaringMoon():
    return render_template("/pokedex/RoaringMoon.html")

@app.route("/IronValiant")
def IronValiant():
    return render_template("/pokedex/IronValiant.html")

@app.route("/Koraidon")
def Koraidon():
    return render_template("/pokedex/Koraidon.html")

@app.route("/Miraidon")
def Miraidon():
    return render_template("/pokedex/Miraidon.html")

@app.route("/WalkingWake")
def WalkingWake():
    return render_template("/pokedex/WalkingWake.html")

@app.route("/IronLeaves")
def IronLeaves():
    return render_template("/pokedex/IronLeaves.html")

@app.route("/Dipplin")
def Dipplin():
    return render_template("/pokedex/Dipplin.html")

@app.route("/PoltchageistArtisan")
def PoltchageistArtisan():
    return render_template("/pokedex/PoltchageistArtisan.html")

@app.route("/Poltchageist")
def Poltchageist():
    return render_template("/pokedex/Poltchageist.html")

@app.route("/Sinistcha")
def Sinistcha():
    return render_template("/pokedex/Sinistcha.html")

@app.route("/SinistchaMasterpiece")
def SinistchaMasterpiece():
    return render_template("/pokedex/SinistchaMasterpiece.html")

@app.route("/Okidogi")
def Okidogi():
    return render_template("/pokedex/Okidogi.html")

@app.route("/Munkidori")
def Munkidori():
    return render_template("/pokedex/Munkidori.html")

@app.route("/Fezandipiti")
def Fezandipiti():
    return render_template("/pokedex/Fezandipiti.html")

@app.route("/Ogerpon")
def Ogerpon():
    return render_template("/pokedex/Ogerpon.html")

@app.route("/OgerponWellspringMask")
def OgerponWellspringMask():
    return render_template("/pokedex/OgerponWellspringMask.html")

@app.route("/OgerponHearthflameMask")
def OgerponHearthflameMask():
    return render_template("/pokedex/OgerponHearthflameMask.html")

@app.route("/OgerponCornerstoneMask")
def OgerponCornerstoneMask():
    return render_template("/pokedex/OgerponCornerstoneMask.html")

@app.route("/Archaludon")
def Archaludon():
    return render_template("/pokedex/Archaludon.html")

@app.route("/Hydrapple")
def Hydrapple():
    return render_template("/pokedex/Hydrapple.html")

@app.route("/GougingFire")
def GougingFire():
    return render_template("/pokedex/GougingFire.html")

@app.route("/RagingBolt")
def RagingBolt():
    return render_template("/pokedex/RagingBolt.html")

@app.route("/IronBoulder")
def IronBoulder():
    return render_template("/pokedex/IronBoulder.html")

@app.route("/IronCrown")
def IronCrown():
    return render_template("/pokedex/IronCrown.html")

@app.route("/TerapagosStellar")
def TerapagosStellar():
    return render_template("/pokedex/TerapagosStellar.html")

@app.route("/Terapagos")
def Terapagos():
    return render_template("/pokedex/Terapagos.html")

@app.route("/TerapagosTerastal")
def TerapagosTerastal():
    return render_template("/pokedex/TerapagosTerastal.html")

@app.route("/Pecharunt")
def Pecharunt():
    return render_template("/pokedex/Pecharunt.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
