liste=[]
liste_fusion=False

nouvel_element=str(input("nom nouvel element: "))
element_pere=str(input("element pere: "))
element_mere=str(input("element mere: "))

fichier=open("programme_principal.py","r")
for ligne in fichier:
    ligne=ligne.replace("\n","")

    if liste_fusion==True:
        ligne=ligne.replace("]","")
        ligne=ligne+f',"{element_pere}{element_mere}","{element_mere}{element_pere}"]'
        liste_fusion=False





    if ligne=="#nouvelle_image":
        liste.append(f'image_{nouvel_element}=pygame.image.load("images/{nouvel_element}.jpg").convert()')
        liste.append(f'image_{nouvel_element}=pygame.transform.scale(image_{nouvel_element},(int(0.03*fen_x),int(0.03*fen_x)))')
    elif ligne=="#liste_fusion":
        liste_fusion=True
    elif ligne=="    #resultat_fusion":
        liste.append(f'    if text_fusion=="{element_pere}{element_mere}" or text_fusion=="{element_mere}{element_pere}":')
        liste.append(f'        if not "{nouvel_element}" in liste_elements:')
        liste.append(f'            liste_elements_menu.append((image_{nouvel_element},"{nouvel_element}",nouvelle_coordoneex,nouvelle_coordoneey))')
        liste.append(f'            liste_elements.append("{nouvel_element}")')
        liste.append(f'        return(image_{nouvel_element},"{nouvel_element}")')



    liste.append(ligne)




liste.append("")
fichier.close()

fichier=open("programme_principal.py","w")
for element in liste:
    fichier.write(element+'\n')
fichier.close()
