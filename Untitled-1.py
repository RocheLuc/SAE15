import csv




caractere=["IP"]#texte à rechercher
entetes=[
         u'HEURES',
         u'MINUTES',
         u'SECONDES',
         u'IP SOURCE',
         u'IP DESTINATION',
         u'FLAG',
         u'SEQUENCE',
         ]   




with open("Fichier_a_traiter.txt", 'r') as fichier, open("fichiertraiter.csv","w")as oui: #ouverture du fichier ainsi que du second fichier
    lignes = fichier.readlines()
    f=open("oui.csv" , "w")
    ligneEntete=";".join(entetes) + "\n"
    oui.write(ligneEntete)


    
    
    


    for ligne in lignes:
        for caracteres in caractere:
            if caracteres in ligne:
                 
                     
                     
                     
                     oui.write(ligne.replace('IP',';').replace('>',';').replace(',',';').replace(':',';'))# Cette ligne permet de remplacer le mot IP par ";" et de le coller dans un autre fichier avec que les lignes interessante
oui.close() #Fermer le fichier creer 
  
f=open("oui.csv" , "w")
ligneEntete=";".join(entetes) + "\n"
f.write(ligneEntete)
print("Le fichier a bien été créer")
f.close

with open("fichiertraiter.csv","r") as files:
    with open("fichiertraiter2.csv","w") as fichiersortie:
        with open("fichieratraiter.txt","w")as fichierdesortie:
            with open ("fichieripsource.txt","w")as fichieripsource:
                with open ("fichieripdestination.txt","w")as fichieripdestination:
                    my_reader = csv.reader(files, delimiter = ";")
                    csv_reader = csv.reader(fichiersortie)
                    for ligne in my_reader:
                        fichiersortie.write(ligne[3] )
                        fichiersortie.write(';')
                        fichiersortie.write(ligne[4] + ';')
                        fichiersortie.write(ligne[5] + '\n')
                        fichierdesortie.write(ligne[5] + '\n')
                        fichieripsource.write(ligne[3] + '\n')
                        fichieripdestination.write(ligne[4] + '\n')
                
        