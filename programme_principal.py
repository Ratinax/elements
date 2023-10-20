import pygame
from pygame.locals import*
pygame.init()  # on initialise pygame
ecran_utilise = pygame.display.Info()   # pour connaitre les dimensions de l'ecran de l'utilisateur
fen_x = ecran_utilise.current_w  #ecran_utilise.current_w # récupère la largeur de l'écran de l'utilisateur
fen_y = int(9/16*fen_x) # met l'épaisseur en fonction de la largeur de l'écran
fenetre = pygame.display.set_mode((fen_x,fen_y),FULLSCREEN)
continuer=True
continuer2=True
fenetre.fill((100,100,100))
##images
image_feu=pygame.image.load("images/feu.jpg").convert()
image_feu=pygame.transform.scale(image_feu,(int(0.03*fen_x),int(0.03*fen_x)))
image_eau=pygame.image.load("images/eau.jpg").convert()
image_eau=pygame.transform.scale(image_eau,(int(0.03*fen_x),int(0.03*fen_x)))
image_air=pygame.image.load("images/air.jpg").convert()
image_air=pygame.transform.scale(image_air,(int(0.03*fen_x),int(0.03*fen_x)))
image_terre=pygame.image.load("images/terre.jpg").convert()
image_terre=pygame.transform.scale(image_terre,(int(0.03*fen_x),int(0.03*fen_x)))
image_retour=pygame.image.load("images/retour.png").convert()
image_retour.set_colorkey((255,255,255))
image_retour=pygame.transform.scale(image_retour,(int(0.03*fen_x),int(0.03*fen_x)))
image_retour2=pygame.image.load("images/retour2.png").convert()
image_retour2.set_colorkey((255,255,255))
image_retour2=pygame.transform.scale(image_retour2,(int(0.03*fen_x),int(0.03*fen_x)))
image_menu=pygame.image.load("images/menu_elements.jpg").convert()
image_menu.set_colorkey((255,255,255))
image_menu=pygame.transform.scale(image_menu,(int(0.03*fen_x),int(0.03*fen_x)))
image_menu2=pygame.image.load("images/menu_elements2.jpg").convert()
image_menu2.set_colorkey((255,255,255))
image_menu2=pygame.transform.scale(image_menu2,(int(0.03*fen_x),int(0.03*fen_x)))
image_poubelle=pygame.image.load("images/poubelle3.png").convert()
image_poubelle.set_colorkey((255,255,255))
image_poubelle=pygame.transform.scale(image_poubelle,(int(0.03*fen_x),int(0.03*fen_x)))
image_poubelle_ouverte=pygame.image.load("images/poubelle_ouverte.jpg").convert()
image_poubelle_ouverte.set_colorkey((255,255,255))
image_poubelle_ouverte=pygame.transform.scale(image_poubelle_ouverte,(int(0.03*fen_x),int(0.03*fen_x)))
image_lave=pygame.image.load("images/lave.jpg").convert()
image_lave.set_colorkey((255,255,255))
image_lave=pygame.transform.scale(image_lave,(int(0.03*fen_x),int(0.03*fen_x)))
image_vapeur=pygame.image.load("images/vapeur.jpg").convert()
image_vapeur=pygame.transform.scale(image_vapeur,(int(0.03*fen_x),int(0.03*fen_x)))
image_caillou=pygame.image.load("images/caillou.jpg").convert()
image_caillou=pygame.transform.scale(image_caillou,(int(0.03*fen_x),int(0.03*fen_x)))
image_sable=pygame.image.load("images/sable.jpg").convert()
image_sable=pygame.transform.scale(image_sable,(int(0.03*fen_x),int(0.03*fen_x)))
image_plage=pygame.image.load("images/plage.jpg").convert()
image_plage=pygame.transform.scale(image_plage,(int(0.03*fen_x),int(0.03*fen_x)))
image_mer=pygame.image.load("images/mer.jpg").convert()
image_mer=pygame.transform.scale(image_mer,(int(0.03*fen_x),int(0.03*fen_x)))
image_verre=pygame.image.load("images/verre.jpg").convert()
image_verre=pygame.transform.scale(image_verre,(int(0.03*fen_x),int(0.03*fen_x)))
image_boue=pygame.image.load("images/boue.jpg").convert()
image_boue=pygame.transform.scale(image_boue,(int(0.03*fen_x),int(0.03*fen_x)))
image_sel=pygame.image.load("images/sel.jpg").convert()
image_sel=pygame.transform.scale(image_sel,(int(0.03*fen_x),int(0.03*fen_x)))
image_verre_d_eau=pygame.image.load("images/verre_d_eau.jpg").convert()
image_verre_d_eau=pygame.transform.scale(image_verre_d_eau,(int(0.03*fen_x),int(0.03*fen_x)))
image_bocal_sable=pygame.image.load("images/bocal_sable.jpg").convert()
image_bocal_sable=pygame.transform.scale(image_bocal_sable,(int(0.03*fen_x),int(0.03*fen_x)))
image_vapeur=pygame.image.load("images/vapeur.jpg").convert()
image_vapeur=pygame.transform.scale(image_vapeur,(int(0.03*fen_x),int(0.03*fen_x)))
image_nuage=pygame.image.load("images/nuage.jpg").convert()
image_nuage=pygame.transform.scale(image_nuage,(int(0.03*fen_x),int(0.03*fen_x)))
image_pluie=pygame.image.load("images/pluie.jpg").convert()
image_pluie=pygame.transform.scale(image_pluie,(int(0.03*fen_x),int(0.03*fen_x)))
image_orage=pygame.image.load("images/orage.jpg").convert()
image_orage=pygame.transform.scale(image_orage,(int(0.03*fen_x),int(0.03*fen_x)))
image_metal=pygame.image.load("images/metal.jpg").convert()
image_metal=pygame.transform.scale(image_metal,(int(0.03*fen_x),int(0.03*fen_x)))
image_electricite=pygame.image.load("images/electricite.jpg").convert()
image_electricite=pygame.transform.scale(image_electricite,(int(0.03*fen_x),int(0.03*fen_x)))
image_poterie=pygame.image.load("images/poterie.jpg").convert()
image_poterie=pygame.transform.scale(image_poterie,(int(0.03*fen_x),int(0.03*fen_x)))
image_vie=pygame.image.load("images/vie.jpg").convert()
image_vie=pygame.transform.scale(image_vie,(int(0.03*fen_x),int(0.03*fen_x)))
image_poisson=pygame.image.load("images/poisson.jpg").convert()
image_poisson=pygame.transform.scale(image_poisson,(int(0.03*fen_x),int(0.03*fen_x)))
image_esprit_de_feu=pygame.image.load("images/esprit_de_feu.jpg").convert()
image_esprit_de_feu=pygame.transform.scale(image_esprit_de_feu,(int(0.03*fen_x),int(0.03*fen_x)))
image_poisson_qui_marche_sur_terre=pygame.image.load("images/poisson_qui_marche_sur_terre.jpg").convert()
image_poisson_qui_marche_sur_terre=pygame.transform.scale(image_poisson_qui_marche_sur_terre,(int(0.03*fen_x),int(0.03*fen_x)))
image_arbre=pygame.image.load("images/arbre.jpg").convert()
image_arbre=pygame.transform.scale(image_arbre,(int(0.03*fen_x),int(0.03*fen_x)))
image_singe=pygame.image.load("images/singe.jpg").convert()
image_singe=pygame.transform.scale(image_singe,(int(0.03*fen_x),int(0.03*fen_x)))
image_homme_des_cavernes=pygame.image.load("images/homme_des_cavernes.jpg").convert()
image_homme_des_cavernes=pygame.transform.scale(image_homme_des_cavernes,(int(0.03*fen_x),int(0.03*fen_x)))
image_homme_antiquite=pygame.image.load("images/homme_antiquite.jpg").convert()
image_homme_antiquite=pygame.transform.scale(image_homme_antiquite,(int(0.03*fen_x),int(0.03*fen_x)))
image_combat=pygame.image.load("images/combat.jpg").convert()
image_combat=pygame.transform.scale(image_combat,(int(0.03*fen_x),int(0.03*fen_x)))
image_oiseau=pygame.image.load("images/oiseau.jpg").convert()
image_oiseau=pygame.transform.scale(image_oiseau,(int(0.03*fen_x),int(0.03*fen_x)))
image_phenix=pygame.image.load("images/phenix.jpg").convert()
image_phenix=pygame.transform.scale(image_phenix,(int(0.03*fen_x),int(0.03*fen_x)))
image_epee=pygame.image.load("images/epee.jpg").convert()
image_epee=pygame.transform.scale(image_epee,(int(0.03*fen_x),int(0.03*fen_x)))
image_arme_a_feu=pygame.image.load("images/arme_a_feu.jpg").convert()
image_arme_a_feu=pygame.transform.scale(image_arme_a_feu,(int(0.03*fen_x),int(0.03*fen_x)))
image_homme=pygame.image.load("images/homme.jpg").convert()
image_homme=pygame.transform.scale(image_homme,(int(0.03*fen_x),int(0.03*fen_x)))
image_kfc=pygame.image.load("images/kfc.jpg").convert()
image_kfc=pygame.transform.scale(image_kfc,(int(0.03*fen_x),int(0.03*fen_x)))
image_poisson_pane=pygame.image.load("images/poisson_pane.jpg").convert()
image_poisson_pane=pygame.transform.scale(image_poisson_pane,(int(0.03*fen_x),int(0.03*fen_x)))
image_croustibat=pygame.image.load("images/croustibat.jpg").convert()
image_croustibat=pygame.transform.scale(image_croustibat,(int(0.03*fen_x),int(0.03*fen_x)))
image_poisson_dans_un_bocal=pygame.image.load("images/poisson_dans_un_bocal.jpg").convert()
image_poisson_dans_un_bocal=pygame.transform.scale(image_poisson_dans_un_bocal,(int(0.03*fen_x),int(0.03*fen_x)))
image_sirene=pygame.image.load("images/sirene.jpg").convert()
image_sirene=pygame.transform.scale(image_sirene,(int(0.03*fen_x),int(0.03*fen_x)))
image_foret=pygame.image.load("images/foret.jpg").convert()
image_foret=pygame.transform.scale(image_foret,(int(0.03*fen_x),int(0.03*fen_x)))
image_incendi=pygame.image.load("images/incendi.jpg").convert()
image_incendi=pygame.transform.scale(image_incendi,(int(0.03*fen_x),int(0.03*fen_x)))
image_foret_apres_incendi=pygame.image.load("images/foret_apres_incendi.jpg").convert()
image_foret_apres_incendi=pygame.transform.scale(image_foret_apres_incendi,(int(0.03*fen_x),int(0.03*fen_x)))
image_zeus=pygame.image.load("images/zeus.jpg").convert()
image_zeus=pygame.transform.scale(image_zeus,(int(0.03*fen_x),int(0.03*fen_x)))
image_poseidon=pygame.image.load("images/poseidon.jpg").convert()
image_poseidon=pygame.transform.scale(image_poseidon,(int(0.03*fen_x),int(0.03*fen_x)))
image_hades=pygame.image.load("images/hades.jpg").convert()
image_hades=pygame.transform.scale(image_hades,(int(0.03*fen_x),int(0.03*fen_x)))
image_tele=pygame.image.load("images/tele.jpg").convert()
image_tele=pygame.transform.scale(image_tele,(int(0.03*fen_x),int(0.03*fen_x)))
image_publicite=pygame.image.load("images/publicite.jpg").convert()
image_publicite=pygame.transform.scale(image_publicite,(int(0.03*fen_x),int(0.03*fen_x)))
image_publicite=pygame.image.load("images/publicite.jpg").convert()
image_publicite=pygame.transform.scale(image_publicite,(int(0.03*fen_x),int(0.03*fen_x)))
image_disney=pygame.image.load("images/disney.jpg").convert()
image_disney=pygame.transform.scale(image_disney,(int(0.03*fen_x),int(0.03*fen_x)))
image_zazu=pygame.image.load("images/zazu.jpg").convert()
image_zazu=pygame.transform.scale(image_zazu,(int(0.03*fen_x),int(0.03*fen_x)))
image_nemo=pygame.image.load("images/nemo.jpg").convert()
image_nemo=pygame.transform.scale(image_nemo,(int(0.03*fen_x),int(0.03*fen_x)))
image_rafiki=pygame.image.load("images/rafiki.jpg").convert()
image_rafiki=pygame.transform.scale(image_rafiki,(int(0.03*fen_x),int(0.03*fen_x)))
image_papier=pygame.image.load("images/papier.jpg").convert()
image_papier=pygame.transform.scale(image_papier,(int(0.03*fen_x),int(0.03*fen_x)))
image_livre=pygame.image.load("images/livre.jpg").convert()
image_livre=pygame.transform.scale(image_livre,(int(0.03*fen_x),int(0.03*fen_x)))
image_cinema=pygame.image.load("images/cinema.jpg").convert()
image_cinema=pygame.transform.scale(image_cinema,(int(0.03*fen_x),int(0.03*fen_x)))
image_disney=pygame.image.load("images/disney.jpg").convert()
image_disney=pygame.transform.scale(image_disney,(int(0.03*fen_x),int(0.03*fen_x)))
image_kirikou=pygame.image.load("images/kirikou.jpg").convert()
image_kirikou=pygame.transform.scale(image_kirikou,(int(0.03*fen_x),int(0.03*fen_x)))
image_street_fighter=pygame.image.load("images/street_fighter.jpg").convert()
image_street_fighter=pygame.transform.scale(image_street_fighter,(int(0.03*fen_x),int(0.03*fen_x)))
image_roi_lion=pygame.image.load("images/roi_lion.jpg").convert()
image_roi_lion=pygame.transform.scale(image_roi_lion,(int(0.03*fen_x),int(0.03*fen_x)))
image_aang=pygame.image.load("images/aang.jpg").convert()
image_aang=pygame.transform.scale(image_aang,(int(0.03*fen_x),int(0.03*fen_x)))
image_gangster=pygame.image.load("images/gangster.jpg").convert()
image_gangster=pygame.transform.scale(image_gangster,(int(0.03*fen_x),int(0.03*fen_x)))
image_prison=pygame.image.load("images/prison.jpg").convert()
image_prison=pygame.transform.scale(image_prison,(int(0.03*fen_x),int(0.03*fen_x)))
image_shrek=pygame.image.load("images/shrek.jpg").convert()
image_shrek=pygame.transform.scale(image_shrek,(int(0.03*fen_x),int(0.03*fen_x)))
image_bob_l_eponge=pygame.image.load("images/bob_l_eponge.jpg").convert()
image_bob_l_eponge=pygame.transform.scale(image_bob_l_eponge,(int(0.03*fen_x),int(0.03*fen_x)))

image_ace=pygame.image.load("images/ace.jpg").convert()
image_ace=pygame.transform.scale(image_ace,(int(0.03*fen_x),int(0.03*fen_x)))
image_gaz=pygame.image.load("images/gaz.jpg").convert()
image_gaz=pygame.transform.scale(image_gaz,(int(0.03*fen_x),int(0.03*fen_x)))
image_etoile=pygame.image.load("images/etoile.jpg").convert()
image_etoile=pygame.transform.scale(image_etoile,(int(0.03*fen_x),int(0.03*fen_x)))
image_systeme_solaire=pygame.image.load("images/systeme_solaire.jpg").convert()
image_systeme_solaire=pygame.transform.scale(image_systeme_solaire,(int(0.03*fen_x),int(0.03*fen_x)))
image_patrick=pygame.image.load("images/patrick.jpg").convert()
image_patrick=pygame.transform.scale(image_patrick,(int(0.03*fen_x),int(0.03*fen_x)))
image_outils=pygame.image.load("images/outils.jpg").convert()
image_outils=pygame.transform.scale(image_outils,(int(0.03*fen_x),int(0.03*fen_x)))
image_bois=pygame.image.load("images/bois.jpg").convert()
image_bois=pygame.transform.scale(image_bois,(int(0.03*fen_x),int(0.03*fen_x)))
image_coquillage=pygame.image.load("images/coquillage.jpg").convert()
image_coquillage=pygame.transform.scale(image_coquillage,(int(0.03*fen_x),int(0.03*fen_x)))
image_petrole=pygame.image.load("images/petrole.jpg").convert()
image_petrole=pygame.transform.scale(image_petrole,(int(0.03*fen_x),int(0.03*fen_x)))
image_essence=pygame.image.load("images/essence.jpg").convert()
image_essence=pygame.transform.scale(image_essence,(int(0.03*fen_x),int(0.03*fen_x)))
image_voiture=pygame.image.load("images/voiture.jpg").convert()
image_voiture=pygame.transform.scale(image_voiture,(int(0.03*fen_x),int(0.03*fen_x)))
image_voiture_electrique=pygame.image.load("images/voiture_electrique.jpg").convert()
image_voiture_electrique=pygame.transform.scale(image_voiture_electrique,(int(0.03*fen_x),int(0.03*fen_x)))
image_avion=pygame.image.load("images/avion.jpg").convert()
image_avion=pygame.transform.scale(image_avion,(int(0.03*fen_x),int(0.03*fen_x)))
image_fusee=pygame.image.load("images/fusee.jpg").convert()
image_fusee=pygame.transform.scale(image_fusee,(int(0.03*fen_x),int(0.03*fen_x)))
#nouvelle_image
page="menu"
liste_element_menu_principal=[[image_feu,int(0.1*fen_x),int(0.1*fen_x),False,"feu"],[image_eau,int(0.131*fen_x),int(0.1*fen_x),False,"eau"],[image_air,int(0.1*fen_x),int(0.131*fen_x),False,"air"],[image_terre,int(0.131*fen_x),int(0.131*fen_x),False,"terre"]]
#liste_fusion
liste_fusions=["terrefeu","feuterre","eaufeu","feueau","laveeau","eaulave","cailloueau","eaucaillou","sableeau","eausable","plageeau","eauplage","sablefeu","feusable","terreeau","eauterre","merfeu","feumer","verreeau","eauverre","verresable","sableverre","vapeur","vapeur","vapeurvapeur","nuageeau","eaunuage","nuagenuage","cailloufeu","feucaillou","oragemetal","metalorage","feuboue","bouefeu","eauair","aireau","vieeau","eauvie","lavevie","vielave","poissonterre","terrepoisson","vieterre","terrevie","","","poisson_qui_marche_sur_terrearbre","arbrepoisson_qui_marche_sur_terre","singefeu","feusinge","homme_des_cavernesmetal","metalhomme_des_cavernes","hommehomme","hommehomme","airvie","vieair","feuoiseau","oiseaufeu","combatmetal","metalcombat","epeefeu","feuepee","homme_antiquiteelectricite","electricitehomme_antiquite","oiseauhomme","hommeoiseau","poissonfeu","feupoisson","poisson_panehomme","hommepoisson_pane","poissonverre","verrepoisson","poissonhomme","hommepoisson","arbrearbre","arbrearbre","foretfeu","feuforet","incendieau","eauincendi","incendipluie","pluieincendi","oragehomme_antiquite","homme_antiquiteorage","homme_antiquitemer","merhomme_antiquite","homme_antiquitelave","lavehomme_antiquite","verreelectricite","electriciteverre","telecroustibat","croustibattele","telekfc","kfctele","hadessirene","sirenehades","disneyoiseau","oiseaudisney","disneypoisson","poissondisney","disneysinge","singedisney","arbrefeu","feuarbre","papierhomme_antiquite","homme_antiquitepapier","livretele","telelivre","telehades","hadestele","cinemapoterie","poteriecinema","hommecaillou","caillouhomme","telecombat","combattele","zazurafiki","rafikizazu","","","hommeair","airhomme","hommeair","airhomme","hommehades","hadeshomme","hommearme_a_feu","arme_a_feuhomme","gangstermetal","metalgangster","hommeboue","bouehomme","homme_des_cavernesboue","bouehomme_des_cavernes","mervie","viemer","feuhomme","hommefeu","boueair","airboue","gazfeu","feugaz","etoileterre","terreetoile","etoilemer","meretoile","etoilebob_l_eponge","bob_l_epongeetoile","epeemetal","metalepee","outilsarbre","arbreoutils","outilsforet","foretoutils","vieplage","plagevie","gazeau","eaugaz","petrolecoquillage","coquillagepetrole","essencemetal","metalessence","voitureelectricite","electricitevoiture","oiseaumetal","metaloiseau","voitureair","airvoiture","voitureoiseau","oiseauvoiture","avionfeu","feuavion"]
liste_elements=["feu","eau","air","terre"]
liste_elements_menu=[(image_feu,"feu",int(0.1*fen_x),int(0.1*fen_x)),(image_eau,"eau",int(0.131*fen_x),int(0.1*fen_x)),(image_air,"air",int(0.162*fen_x),int(0.1*fen_x)),(image_terre,"terre",int(0.193*fen_x),int(0.1*fen_x))]
def position_carre(x1,x2,y1,y2):
    positionX_souris = pygame.mouse.get_pos()[0]
    positionY_souris = pygame.mouse.get_pos()[1]
    if positionX_souris>int(x1) and positionX_souris<int(x2) and positionY_souris>int(y1) and positionY_souris<int(y2):
        return True
def resultat_fusion(text_fusion1,text_fusion2):   #fonction qui retourne la nouvelle image puis le nouveau nom d'une fusion
    text_fusion=text_fusion1+text_fusion2
    nouvelle_coordoneex=0.1*fen_x+float(len(liste_elements)%26*0.031*fen_x)
    nouvelle_coordoneey=0.1*fen_x+float(len(liste_elements)//26*0.031*fen_x)
    if text_fusion=="terrefeu" or text_fusion=="feuterre":
        if not "lave" in liste_elements:
            liste_elements_menu.append((image_lave,"lave",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("lave")
        return (image_lave,"lave")
    if text_fusion=="eaufeu" or text_fusion=="feueau":
        if not "vapeur" in liste_elements:
            liste_elements_menu.append((image_vapeur,"vapeur",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("vapeur")
        return(image_vapeur,"vapeur")
    if text_fusion=="laveeau" or text_fusion=="eaulave":
        if not "caillou" in liste_elements:
            liste_elements_menu.append((image_caillou,"caillou",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("caillou")
        return(image_caillou,"caillou")
    if text_fusion=="cailloueau" or text_fusion=="eaucaillou":
        if not "sable" in liste_elements:
            liste_elements_menu.append((image_sable,"sable",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("sable")
        return(image_sable,"sable")
    if text_fusion=="sableeau" or text_fusion=="eausable":
        if not "plage" in liste_elements:
            liste_elements_menu.append((image_plage,"plage",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("plage")
        return(image_plage,"plage")
    if text_fusion=="plageeau" or text_fusion=="eauplage":
        if not "mer" in liste_elements:
            liste_elements_menu.append((image_mer,"mer",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("mer")
        return(image_mer,"mer")
    if text_fusion=="feusable" or text_fusion=="sablefeu":
        if not "verre" in liste_elements:
            liste_elements_menu.append((image_verre,"verre",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("verre")
        return(image_verre,"verre")

    if text_fusion=="terreeau" or text_fusion=="eauterre":
        if not "boue" in liste_elements:
            liste_elements_menu.append((image_boue,"boue",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("boue")
        return(image_boue,"boue")
    if text_fusion=="merfeu" or text_fusion=="feumer":
        if not "sel" in liste_elements:
            liste_elements_menu.append((image_sel,"sel",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("sel")
        return(image_sel,"sel")
    if text_fusion=="verreeau" or text_fusion=="eauverre":
        if not "verre_d_eau" in liste_elements:
            liste_elements_menu.append((image_verre_d_eau,"verre_d_eau",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("verre_d_eau")
        return(image_verre_d_eau,"verre_d_eau")
    if text_fusion=="verresable" or text_fusion=="sableverre":
        if not "bocal_sable" in liste_elements:
            liste_elements_menu.append((image_bocal_sable,"bocal_sable",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("bocal_sable")
        return(image_bocal_sable,"bocal_sable")
    if text_fusion=="vapeur" or text_fusion=="vapeur":
        if not "vapeur" in liste_elements:
            liste_elements_menu.append((image_vapeur,"vapeur",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("vapeur")
        return(image_vapeur,"vapeur")
    if text_fusion=="vapeurvapeur":
        if not "nuage" in liste_elements:
            liste_elements_menu.append((image_nuage,"nuage",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("nuage")
        return(image_nuage,"nuage")
    if text_fusion=="nuageeau" or text_fusion=="eaunuage":
        if not "pluie" in liste_elements:
            liste_elements_menu.append((image_pluie,"pluie",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("pluie")
        return(image_pluie,"pluie")
    if text_fusion=="nuagenuage":
        if not "orage" in liste_elements:
            liste_elements_menu.append((image_orage,"orage",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("orage")
        return(image_orage,"orage")
    if text_fusion=="cailloufeu" or text_fusion=="feucaillou":
        if not "metal" in liste_elements:
            liste_elements_menu.append((image_metal,"metal",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("metal")
        return(image_metal,"metal")
    if text_fusion=="oragemetal" or text_fusion=="metalorage":
        if not "electricite" in liste_elements:
            liste_elements_menu.append((image_electricite,"electricite",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("electricite")
        return(image_electricite,"electricite")
    if text_fusion=="feuboue" or text_fusion=="bouefeu":
        if not "poterie" in liste_elements:
            liste_elements_menu.append((image_poterie,"poterie",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("poterie")
        return(image_poterie,"poterie")
    if text_fusion=="eauair" or text_fusion=="aireau":
        if not "vie" in liste_elements:
            liste_elements_menu.append((image_vie,"vie",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("vie")
        return(image_vie,"vie")
    if text_fusion=="vieeau" or text_fusion=="eauvie":
        if not "poisson" in liste_elements:
            liste_elements_menu.append((image_poisson,"poisson",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("poisson")
        return(image_poisson,"poisson")
    if text_fusion=="lavevie" or text_fusion=="vielave":
        if not "esprit_de_feu" in liste_elements:
            liste_elements_menu.append((image_esprit_de_feu,"esprit_de_feu",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("esprit_de_feu")
        return(image_esprit_de_feu,"esprit_de_feu")
    if text_fusion=="poissonterre" or text_fusion=="terrepoisson":
        if not "poisson_qui_marche_sur_terre" in liste_elements:
            liste_elements_menu.append((image_poisson_qui_marche_sur_terre,"poisson_qui_marche_sur_terre",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("poisson_qui_marche_sur_terre")
        return(image_poisson_qui_marche_sur_terre,"poisson_qui_marche_sur_terre")
    if text_fusion=="vieterre" or text_fusion=="terrevie":
        if not "arbre" in liste_elements:
            liste_elements_menu.append((image_arbre,"arbre",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("arbre")
        return(image_arbre,"arbre")
    if text_fusion=="poisson_qui_marche_sur_terrearbre" or text_fusion=="arbrepoisson_qui_marche_sur_terre":
        if not "singe" in liste_elements:
            liste_elements_menu.append((image_singe,"singe",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("singe")
        return(image_singe,"singe")
    if text_fusion=="singefeu" or text_fusion=="feusinge":
        if not "homme_des_cavernes" in liste_elements:
            liste_elements_menu.append((image_homme_des_cavernes,"homme_des_cavernes",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("homme_des_cavernes")
        return(image_homme_des_cavernes,"homme_des_cavernes")
    if text_fusion=="homme_des_cavernesmetal" or text_fusion=="metalhomme_des_cavernes":
        if not "homme_antiquite" in liste_elements:
            liste_elements_menu.append((image_homme_antiquite,"homme_antiquite",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("homme_antiquite")
        return(image_homme_antiquite,"homme_antiquite")
    if text_fusion=="hommehomme" or text_fusion=="hommehomme":
        if not "combat" in liste_elements:
            liste_elements_menu.append((image_combat,"combat",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("combat")
        return(image_combat,"combat")
    if text_fusion=="airvie" or text_fusion=="vieair":
        if not "oiseau" in liste_elements:
            liste_elements_menu.append((image_oiseau,"oiseau",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("oiseau")
        return(image_oiseau,"oiseau")
    if text_fusion=="feuoiseau" or text_fusion=="oiseaufeu":
        if not "phenix" in liste_elements:
            liste_elements_menu.append((image_phenix,"phenix",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("phenix")
        return(image_phenix,"phenix")
    if text_fusion=="combatmetal" or text_fusion=="metalcombat":
        if not "epee" in liste_elements:
            liste_elements_menu.append((image_epee,"epee",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("epee")
        return(image_epee,"epee")
    if text_fusion=="epeefeu" or text_fusion=="feuepee":
        if not "arme_a_feu" in liste_elements:
            liste_elements_menu.append((image_arme_a_feu,"arme_a_feu",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("arme_a_feu")
        return(image_arme_a_feu,"arme_a_feu")
    if text_fusion=="homme_antiquiteelectricite" or text_fusion=="electricitehomme_antiquite":
        if not "homme" in liste_elements:
            liste_elements_menu.append((image_homme,"homme",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("homme")
        return(image_homme,"homme")
    if text_fusion=="oiseauhomme" or text_fusion=="hommeoiseau":
        if not "kfc" in liste_elements:
            liste_elements_menu.append((image_kfc,"kfc",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("kfc")
        return(image_kfc,"kfc")
    if text_fusion=="poissonfeu" or text_fusion=="feupoisson":
        if not "poisson_pane" in liste_elements:
            liste_elements_menu.append((image_poisson_pane,"poisson_pane",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("poisson_pane")
        return(image_poisson_pane,"poisson_pane")
    if text_fusion=="poisson_panehomme" or text_fusion=="hommepoisson_pane":
        if not "croustibat" in liste_elements:
            liste_elements_menu.append((image_croustibat,"croustibat",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("croustibat")
        return(image_croustibat,"croustibat")
    if text_fusion=="poissonverre" or text_fusion=="verrepoisson":
        if not "poisson_dans_un_bocal" in liste_elements:
            liste_elements_menu.append((image_poisson_dans_un_bocal,"poisson_dans_un_bocal",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("poisson_dans_un_bocal")
        return(image_poisson_dans_un_bocal,"poisson_dans_un_bocal")
    if text_fusion=="poissonhomme" or text_fusion=="hommepoisson":
        if not "sirene" in liste_elements:
            liste_elements_menu.append((image_sirene,"sirene",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("sirene")
        return(image_sirene,"sirene")
    if text_fusion=="arbrearbre" or text_fusion=="arbrearbre":
        if not "foret" in liste_elements:
            liste_elements_menu.append((image_foret,"foret",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("foret")
        return(image_foret,"foret")
    if text_fusion=="foretfeu" or text_fusion=="feuforet":
        if not "incendi" in liste_elements:
            liste_elements_menu.append((image_incendi,"incendi",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("incendi")
        return(image_incendi,"incendi")
    if text_fusion=="incendieau" or text_fusion=="eauincendi":
        if not "foret_apres_incendi" in liste_elements:
            liste_elements_menu.append((image_foret_apres_incendi,"foret_apres_incendi",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("foret_apres_incendi")
        return(image_foret_apres_incendi,"foret_apres_incendi")
    if text_fusion=="incendipluie" or text_fusion=="pluieincendi":
        if not "foret_apres_incendi" in liste_elements:
            liste_elements_menu.append((image_foret_apres_incendi,"foret_apres_incendi",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("foret_apres_incendi")
        return(image_foret_apres_incendi,"foret_apres_incendi")
    if text_fusion=="oragehomme_antiquite" or text_fusion=="homme_antiquiteorage":
        if not "zeus" in liste_elements:
            liste_elements_menu.append((image_zeus,"zeus",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("zeus")
        return(image_zeus,"zeus")
    if text_fusion=="homme_antiquitemer" or text_fusion=="merhomme_antiquite":
        if not "poseidon" in liste_elements:
            liste_elements_menu.append((image_poseidon,"poseidon",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("poseidon")
        return(image_poseidon,"poseidon")
    if text_fusion=="homme_antiquitelave" or text_fusion=="lavehomme_antiquite":
        if not "hades" in liste_elements:
            liste_elements_menu.append((image_hades,"hades",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("hades")
        return(image_hades,"hades")
    if text_fusion=="verreelectricite" or text_fusion=="electriciteverre":
        if not "tele" in liste_elements:
            liste_elements_menu.append((image_tele,"tele",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("tele")
        return(image_tele,"tele")
    if text_fusion=="telecroustibat" or text_fusion=="croustibattele":
        if not "publicite" in liste_elements:
            liste_elements_menu.append((image_publicite,"publicite",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("publicite")
        return(image_publicite,"publicite")
    if text_fusion=="telekfc" or text_fusion=="kfctele":
        if not "publicite" in liste_elements:
            liste_elements_menu.append((image_publicite,"publicite",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("publicite")
        return(image_publicite,"publicite")
    if text_fusion=="hadessirene" or text_fusion=="sirenehades":
        if not "disney" in liste_elements:
            liste_elements_menu.append((image_disney,"disney",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("disney")
        return(image_disney,"disney")
    if text_fusion=="disneyoiseau" or text_fusion=="oiseaudisney":
        if not "zazu" in liste_elements:
            liste_elements_menu.append((image_zazu,"zazu",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("zazu")
        return(image_zazu,"zazu")
    if text_fusion=="disneypoisson" or text_fusion=="poissondisney":
        if not "nemo" in liste_elements:
            liste_elements_menu.append((image_nemo,"nemo",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("nemo")
        return(image_nemo,"nemo")
    if text_fusion=="disneysinge" or text_fusion=="singedisney":
        if not "rafiki" in liste_elements:
            liste_elements_menu.append((image_rafiki,"rafiki",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("rafiki")
        return(image_rafiki,"rafiki")
    if text_fusion=="arbrefeu" or text_fusion=="feuarbre":
        if not "papier" in liste_elements:
            liste_elements_menu.append((image_papier,"papier",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("papier")
        return(image_papier,"papier")
    if text_fusion=="papierhomme_antiquite" or text_fusion=="homme_antiquitepapier":
        if not "livre" in liste_elements:
            liste_elements_menu.append((image_livre,"livre",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("livre")
        return(image_livre,"livre")
    if text_fusion=="livretele" or text_fusion=="telelivre":
        if not "cinema" in liste_elements:
            liste_elements_menu.append((image_cinema,"cinema",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("cinema")
        return(image_cinema,"cinema")
    if text_fusion=="telehades" or text_fusion=="hadestele":
        if not "disney" in liste_elements:
            liste_elements_menu.append((image_disney,"disney",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("disney")
        return(image_disney,"disney")
    if text_fusion=="cinemapoterie" or text_fusion=="poteriecinema":
        if not "kirikou" in liste_elements:
            liste_elements_menu.append((image_kirikou,"kirikou",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("kirikou")
        return(image_kirikou,"kirikou")
    if text_fusion=="hommecaillou" or text_fusion=="caillouhomme":
        if not "homme_des_cavernes" in liste_elements:
            liste_elements_menu.append((image_homme_des_cavernes,"homme_des_cavernes",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("homme_des_cavernes")
        return(image_homme_des_cavernes,"homme_des_cavernes")
    if text_fusion=="telecombat" or text_fusion=="combattele":
        if not "street_fighter" in liste_elements:
            liste_elements_menu.append((image_street_fighter,"street_fighter",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("street_fighter")
        return(image_street_fighter,"street_fighter")
    if text_fusion=="zazurafiki" or text_fusion=="rafikizazu":
        if not "roi_lion" in liste_elements:
            liste_elements_menu.append((image_roi_lion,"roi_lion",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("roi_lion")
        return(image_roi_lion,"roi_lion")
    if text_fusion=="" or text_fusion=="":
        if not "homme" in liste_elements:
            liste_elements_menu.append((image_homme,"homme",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("homme")
        return(image_homme,"homme")
    if text_fusion=="hommeair" or text_fusion=="airhomme":
        if not "aang" in liste_elements:
            liste_elements_menu.append((image_aang,"aang",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("aang")
        return(image_aang,"aang")
    if text_fusion=="hommeair" or text_fusion=="airhomme":
        if not "aang" in liste_elements:
            liste_elements_menu.append((image_aang,"aang",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("aang")
        return(image_aang,"aang")
    if text_fusion=="hommehades" or text_fusion=="hadeshomme":
        if not "gangster" in liste_elements:
            liste_elements_menu.append((image_gangster,"gangster",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("gangster")
        return(image_gangster,"gangster")
    if text_fusion=="hommearme_a_feu" or text_fusion=="arme_a_feuhomme":
        if not "gangster" in liste_elements:
            liste_elements_menu.append((image_gangster,"gangster",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("gangster")
        return(image_gangster,"gangster")
    if text_fusion=="gangstermetal" or text_fusion=="metalgangster":
        if not "prison" in liste_elements:
            liste_elements_menu.append((image_prison,"prison",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("prison")
        return(image_prison,"prison")
    if text_fusion=="hommeboue" or text_fusion=="bouehomme":
        if not "shrek" in liste_elements:
            liste_elements_menu.append((image_shrek,"shrek",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("shrek")
        return(image_shrek,"shrek")
    if text_fusion=="homme_des_cavernesboue" or text_fusion=="bouehomme_des_cavernes":
        if not "shrek" in liste_elements:
            liste_elements_menu.append((image_shrek,"shrek",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("shrek")
        return(image_shrek,"shrek")
    if text_fusion=="mervie" or text_fusion=="viemer":
        if not "bob_l_eponge" in liste_elements:
            liste_elements_menu.append((image_bob_l_eponge,"bob_l_eponge",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("bob_l_eponge")
        return(image_bob_l_eponge,"bob_l_eponge")
    if text_fusion=="feuhomme" or text_fusion=="hommefeu":
        if not "ace" in liste_elements:
            liste_elements_menu.append((image_ace,"ace",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("ace")
        return(image_ace,"ace")
    if text_fusion=="boueair" or text_fusion=="airboue":
        if not "gaz" in liste_elements:
            liste_elements_menu.append((image_gaz,"gaz",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("gaz")
        return(image_gaz,"gaz")
    if text_fusion=="gazfeu" or text_fusion=="feugaz":
        if not "etoile" in liste_elements:
            liste_elements_menu.append((image_etoile,"etoile",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("etoile")
        return(image_etoile,"etoile")
    if text_fusion=="etoileterre" or text_fusion=="terreetoile":
        if not "systeme_solaire" in liste_elements:
            liste_elements_menu.append((image_systeme_solaire,"systeme_solaire",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("systeme_solaire")
        return(image_systeme_solaire,"systeme_solaire")
    if text_fusion=="etoilemer" or text_fusion=="meretoile":
        if not "patrick" in liste_elements:
            liste_elements_menu.append((image_patrick,"patrick",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("patrick")
        return(image_patrick,"patrick")
    if text_fusion=="etoilebob_l_eponge" or text_fusion=="bob_l_epongeetoile":
        if not "patrick" in liste_elements:
            liste_elements_menu.append((image_patrick,"patrick",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("patrick")
        return(image_patrick,"patrick")
    if text_fusion=="epeemetal" or text_fusion=="metalepee":
        if not "outils" in liste_elements:
            liste_elements_menu.append((image_outils,"outils",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("outils")
        return(image_outils,"outils")
    if text_fusion=="outilsarbre" or text_fusion=="arbreoutils":
        if not "bois" in liste_elements:
            liste_elements_menu.append((image_bois,"bois",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("bois")
        return(image_bois,"bois")
    if text_fusion=="outilsforet" or text_fusion=="foretoutils":
        if not "bois" in liste_elements:
            liste_elements_menu.append((image_bois,"bois",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("bois")
        return(image_bois,"bois")
    if text_fusion=="vieplage" or text_fusion=="plagevie":
        if not "coquillage" in liste_elements:
            liste_elements_menu.append((image_coquillage,"coquillage",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("coquillage")
        return(image_coquillage,"coquillage")
    if text_fusion=="gazeau" or text_fusion=="eaugaz":
        if not "petrole" in liste_elements:
            liste_elements_menu.append((image_petrole,"petrole",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("petrole")
        return(image_petrole,"petrole")
    if text_fusion=="petrolecoquillage" or text_fusion=="coquillagepetrole":
        if not "essence" in liste_elements:
            liste_elements_menu.append((image_essence,"essence",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("essence")
        return(image_essence,"essence")
    if text_fusion=="essencemetal" or text_fusion=="metalessence":
        if not "voiture" in liste_elements:
            liste_elements_menu.append((image_voiture,"voiture",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("voiture")
        return(image_voiture,"voiture")
    if text_fusion=="voitureelectricite" or text_fusion=="electricitevoiture":
        if not "voiture_electrique" in liste_elements:
            liste_elements_menu.append((image_voiture_electrique,"voiture_electrique",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("voiture_electrique")
        return(image_voiture_electrique,"voiture_electrique")
    if text_fusion=="oiseaumetal" or text_fusion=="metaloiseau":
        if not "avion" in liste_elements:
            liste_elements_menu.append((image_avion,"avion",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("avion")
        return(image_avion,"avion")
    if text_fusion=="voitureair" or text_fusion=="airvoiture":
        if not "avion" in liste_elements:
            liste_elements_menu.append((image_avion,"avion",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("avion")
        return(image_avion,"avion")
    if text_fusion=="voitureoiseau" or text_fusion=="oiseauvoiture":
        if not "avion" in liste_elements:
            liste_elements_menu.append((image_avion,"avion",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("avion")
        return(image_avion,"avion")
    if text_fusion=="avionfeu" or text_fusion=="feuavion":
        if not "fusee" in liste_elements:
            liste_elements_menu.append((image_fusee,"fusee",nouvelle_coordoneex,nouvelle_coordoneey))
            liste_elements.append("fusee")
        return(image_fusee,"fusee")
    #resultat_fusion
def do_fusion(liste):
    if len(liste)>0:
        for i in range(0,len(liste)):
            for j in range(1+i,len(liste)):
                if liste[i][1]==liste[j][1] and liste[i][2]==liste[j][2]:
                    if liste[i][4]+liste[j][4] in liste_fusions:
                        elem1=liste[i]
                        elem2=liste[j]
                        liste.append([resultat_fusion(liste[i][4],liste[j][4])[0],liste[i][1],liste[i][2],False,resultat_fusion(liste[i][4],liste[j][4])[1]])
                        liste.remove(elem1)
                        liste.remove(elem2)
                        break
texte_moyen = pygame.font.Font(None, int(fen_x/30)) # police moyenne
texte_petit = pygame.font.Font(None, int(fen_x/50)) # police petite
texte_intro = texte_moyen.render("Pour déplacer un élément cliquer dessus et glissez-le",True,(255,255,255))
texte_intro2 = texte_moyen.render("Pour fusionner 2 éléments faites cliques droits sur ces 2 derniers superposés",True,(255,255,255))
texte_intro3 = texte_moyen.render("Pour déplacer plusieurs éléments faites cliques droits dessus et glissez les",True,(255,255,255))
texte_intro4 = texte_moyen.render("Pour supprimer un élément, glissez le dans la corbeille",True,(255,255,255))
texte_intro5 = texte_moyen.render("Pour supprimer tous les éléments, clique droit sur la corbeille",True,(255,255,255))
texte_intro6 = texte_moyen.render("Pour récupérer des éléments cliquez dessus dans le menu en haut à gauche",True,(255,255,255))
texte_intro7 = texte_petit.render("Cliquez pour passer ;)",True,(255,255,255))
while continuer2==True:
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                continuer2=False
    fenetre.fill((200,200,200))
    fenetre.blit(texte_intro,(0,0))
    fenetre.blit(texte_intro2,(0,int(0.05*fen_x)))
    fenetre.blit(texte_intro3,(0,int(0.1*fen_x)))
    fenetre.blit(texte_intro4,(0,int(0.15*fen_x)))
    fenetre.blit(texte_intro5,(0,int(0.2*fen_x)))
    fenetre.blit(texte_intro6,(0,int(0.25*fen_x)))
    fenetre.blit(texte_intro7,(int(0.80*fen_x),int(0.50*fen_x)))
    pygame.display.flip()
while continuer==True:
    positionX_souris = pygame.mouse.get_pos()[0]
    positionY_souris = pygame.mouse.get_pos()[1]
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                continuer=False
        if event.type==MOUSEMOTION:
            if page=="menu":
                for i in range(len(liste_element_menu_principal)):
                    if liste_element_menu_principal[i][3]==True:
                        liste_element_menu_principal[i][1],liste_element_menu_principal[i][2]=positionX_souris-0.015*fen_x,positionY_souris-0.015*fen_x
        if event.type==MOUSEBUTTONDOWN:
            if page=="menu":
                if event.button==1:
                    oui=False
                    for i in range(len(liste_element_menu_principal)):
                        x1=liste_element_menu_principal[i][1]-2
                        x2=x1+0.03*fen_x
                        y1=liste_element_menu_principal[i][2]-2
                        y2=y1+0.03*fen_x
                        if oui!=True:
                            if position_carre(x1,x2,y1,y2)==True:
                                liste_element_menu_principal[i][3]=True
                                oui=True
                    for i in range(len(liste_element_menu_principal)):
                        if liste_element_menu_principal[i][3]==True:
                            liste_element_menu_principal[i][1],liste_element_menu_principal[i][2]=positionX_souris-0.015*fen_x,positionY_souris-0.015*fen_x
                elif event.button==3:
                    if position_carre(0.96*fen_x,0.99*fen_x,fen_y-0.04*fen_x,fen_y-0.01*fen_x):
                        for i in range(len(liste_element_menu_principal)):
                            liste_element_menu_principal.remove(liste_element_menu_principal[0])
                    for i in range(len(liste_element_menu_principal)):
                        x1=liste_element_menu_principal[i][1]-2
                        x2=x1+0.03*fen_x
                        y1=liste_element_menu_principal[i][2]-2
                        y2=y1+0.03*fen_x
                        if position_carre(x1,x2,y1,y2)==True:
                            liste_element_menu_principal[i][3]=True
                    for i in range(len(liste_element_menu_principal)):
                        if liste_element_menu_principal[i][3]==True:
                            liste_element_menu_principal[i][1],liste_element_menu_principal[i][2]=positionX_souris-0.015*fen_x,positionY_souris-0.015*fen_x
                    do_fusion(liste_element_menu_principal)
            elif page=="menu_elements":
                for i in range(len(liste_elements_menu)):
                    x1=liste_elements_menu[i][2]
                    x2=x1+0.03*fen_x
                    y1=liste_elements_menu[i][3]
                    y2=y1+0.03*fen_x
                    if position_carre(x1,x2,y1,y2)==True:
                        liste_element_menu_principal.append([liste_elements_menu[i][0],liste_elements_menu[i][2],liste_elements_menu[i][3],False,liste_elements_menu[i][1]])
        if event.type==MOUSEBUTTONUP:
            if page == "menu":
                if position_carre(0.96*fen_x,0.99*fen_x,fen_y-0.04*fen_x,fen_y-0.01*fen_x):
                    liste_a_enlever=[]
                    for i in range(len(liste_element_menu_principal)):
                        if liste_element_menu_principal[i][3]==True:
                            liste_a_enlever.append(liste_element_menu_principal[i])
                    for element in liste_a_enlever:
                        liste_element_menu_principal.remove(element)
                for i in range(len(liste_element_menu_principal)):    #quand souris relachée tous les éléments sont False: ils ne peuvent pas bouger
                    liste_element_menu_principal[i][3]=False
                if position_carre(0.03*fen_x,0.06*fen_x,0.03*fen_x,0.06*fen_x):
                    page="menu_elements"
            elif page=="menu_elements":
                if position_carre(0.03*fen_x,0.06*fen_x,0.03*fen_x,0.06*fen_x):
                    page="menu"
    if page=="menu":
        fenetre.fill((100,100,100))
        if position_carre(0.03*fen_x,0.06*fen_x,0.03*fen_x,0.06*fen_x):
            fenetre.blit(image_menu2,(int(0.03*fen_x),int(0.03*fen_x)))
        else:
            fenetre.blit(image_menu,(int(0.03*fen_x),int(0.03*fen_x)))
        # affichage des éléments
        for i in range(len(liste_element_menu_principal)-1,-1,-1):
            fenetre.blit(liste_element_menu_principal[i][0],(liste_element_menu_principal[i][1],liste_element_menu_principal[i][2])) #affiche chaque éléments un par un
        # affichage poubelle
        if position_carre(0.96*fen_x,0.99*fen_x,fen_y-0.04*fen_x,fen_y-0.01*fen_x):
            fenetre.blit(image_poubelle_ouverte,(0.96*fen_x,fen_y-0.04*fen_x))
        else:
            fenetre.blit(image_poubelle,(0.96*fen_x,fen_y-0.04*fen_x))
    elif page=="menu_elements":
        fenetre.fill((100,100,100))
        if position_carre(0.03*fen_x,0.06*fen_x,0.03*fen_x,0.06*fen_x):
            fenetre.blit(image_retour2,(int(0.03*fen_x),int(0.03*fen_x)))
        else:
            fenetre.blit(image_retour,(int(0.03*fen_x),int(0.03*fen_x)))
        for i in range(len(liste_elements_menu)):
            fenetre.blit(liste_elements_menu[i][0],(liste_elements_menu[i][2],liste_elements_menu[i][3]))
    pygame.display.flip()
pygame.quit()






















