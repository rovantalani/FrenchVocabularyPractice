def glosor(ordlista2):
    skippadeord= {}
    ordet=''
    for key in ordlista2:
        while ordet!= ordlista2[key]:
            print key
            ordet= raw_input()
           
            if ordet ==ordlista2[key]:
                print 'right'
            elif ordet== 'ss':
                ordet=ordlista2[key]
                print "ordet var: " + ordet
                skippadeord[key]= ordet        
            else:
                print 'try again'        
    print 'ord du inte kunde: '
    for key in skippadeord:
        print key + ' betyder: ' + skippadeord[key]
    return skippadeord

sara={'v�lkommen(m)': 'bienvenu', 'till': 'en', 'Frankrike': 'France', 'anl�nda': 'arrive', 'p� t�gstationen': '� la gare',
      'urs�kta mig': 'excusez-moi', 'det �r': "c'est", 'ni �r': 'vous �tes', 'fr�n sverige': 'de Su�de', 'jag �r': 'je suis',
      'trevligt att tr�ffas(m)': 'enchant�', 'inte s�': 'pas trop', 'tr�tt(m)': 'fatigu�', 'lite grann': 'un peu', 'men': 'mais',
      'ert bagage(m pl)': 'vous bagages', 'h�r �r': 'voici', 'min ryggs�ck': 'mon sac � dos', 'd�(s�)': 'alors', 'd� g�r vi': 'on y va'}
Lebau= {'allihopa': 'tout le monde', 'hos': 'chez', 'godkv�ll': 'bonsoir', 'ungdomar (m pl)': 'les junes', 'alla': 'tous', 'hon kommer': 'elle vient',
        'en gitarr': 'une guitare', 'toppen (m)': 'g�nial', 'jag �lskar': "j'adore", 'ja kommer': 'je viens', 'ocks�': 'aussi', 'jag gillar': "j'aime",
        'jag gillar mycket': "j'aime bien", 'du kommer': 'tu viens', 'va, hu sa?': 'comment', 'just det s� �r det': "c'est c,a",
        'jag f�redrar': 'je pr�f�re', 'London': 'Londres', 'svenskorna': 'les Su�doises', 'du �r': 'tu es', 'om�jligt': 'impossible', 'jaha': 'eh ben',
        'okej': "d'accord", 'musiken': 'la musique', 'flickorna': 'les filles', 'jag bor': "j'habite", 'i': '�', 'K�penhamn': 'Copenhague',
        'framf�r allt': 'surtout', 'sj�lvklart': 'bien s�r', 'klassisk musik': 'la musique classique', 'jag l�mnar er': 'je vous laisse',
        'godnatt': 'bonne nuit', 'nejd�': 'mais non'}
etre= {'vara': '�tre', 'jag �r': 'je suis', 'du �r': 'tu es', 'han �r': 'il est', 'hon �r': 'elle est', 'man �r/vi �r': 'on est', 'vi �r': 'nous sommes',
       'ni �r': 'vous �tes', 'de �r(m)': 'ils sont', 'de �r(f)': 'elles sont'}

unune= {'en balkong': 'un balcon', 'en te': 'un th�', 'ett garage': 'un garage', 'en banan': 'une banane', 'en gitarr': 'une guitare',
        'ett bibliotek':  'une biblioth�que'}
chanson= {'20': 'vingt', '21': 'vingt et un', '22': 'vingt-deux', '23': 'vingt-trois', '24': 'vingt-quatre', '30': 'trente', '31': 'trente et un',
          '40': 'quarante', '50': 'cinquante', '60': 'soixante', '70': 'soixante-dix', '71': 'soixante et onze', '72': 'soixante-douze',
          '73': 'soixante-treize', '74': 'soixante-quatorze', '75': 'soixante-quinze', '76': 'soixante-seize', '77': 'soixante-dix-sept',
          '78': 'soixante-dix-huit', '79' : 'soixante-dix-neuf', '80': 'quatre-vingts', '81': 'quatre-vingt-un', '90': 'quatre-vingt-dix',
          '91' : 'quatre-vingt-onze', '100': 'cent', '200': 'deux cent', '1000': 'mille'}
cafe= {'vad?': "qu'est-ce que", 'vad ska vi ta': "qu'est-ce qu'on prend", 'en kompis(m)': 'un copain', 'en kompis(f)': 'une copine',
       'hennes/hans/sina kompisar': 'ses copains', 'p� cafe': 'au caf�', 'jag tar': 'je prends', 'en saft med mintsmak':'un diablo menthe',
       'jag har': "j'ai", 'jag �r t�rstig': "j'ai soif", 'jag vet inte': 'je ne sais pas', 'jag �r inte t�rstig': "je n'ai pas soif",
       'egentligen': 'vraiment', 'kanske': 'peut-�tre', 'du tar': 'tu prends', 'en apelsinl�sk': 'un Orangina', 'please': "s'il vous pla�t",
       'servit�ren': 'le garc,on' , 'ni tar': 'vous prenez', 'senare': 'plus tard', 'Hur mycket blir det': 'c,a fait combien', 'en euro': 'un euro',
       'vars�god': 'voil�', 'damer och herrar': 'messieurs-dames', 'en fat�l': 'un demi'}
prendre= {'ta': 'prendre', 'jag tar': 'je prends', 'du tar': 'tu prends', 'han tar': 'il prend', 'hon tar':'elle prend', 'man/vi tar': 'on prend',
          'vi tar': 'nous prenons', 'ni tar': 'vous prenez', 'de tar(m)': 'ils prennent', 'de tar (f)': 'elles prennent'}
boire={'ska vi': 'on va', 'dricka':'boire', 'ett glas': 'un verre', 'okej': "d'accord", 'en espresso med varm mj�lk': 'un caf� cr�me',
       'en grop/h�la': 'un creux', 'jag �r sugen p� n�got': "j'ai un petit creux", 'jag �r hungrig': "j'ai faim",
       'jag �r inte hungrig': "je n'ai pas faim", 'inte alls': 'pas du tout', 'mina damer': 'mesdames', 'till er': 'pour vous', 'svart': 'noir',
       'en espresso': 'un caf�'}
pont= {'p�': 'sur', 'bron': 'le pont', 'd�r dansar man': 'on y danse', 'i ring': 'en rond', 'de vackra': 'les beaux', 'herrarna': 'messieurs',
       'g�r': 'font', 's� h�r': 'comme c,a', 'sedan': 'puis', 'igen': 'encore', 'de vackra damerna': 'les belles dames', 'musikerna': 'les musiciens',
       'soldaterna': 'les militaires', 'hos sig': 'chez lui', 'de andra': 'les autres'}
#kapitel 3
presente= {'jag presenterar mig': 'je me pr�sente', 'en kvinna': 'une femme', 'jag �r 17 �r': "j'ai 17 ans", 'livet': 'la vie', 'jag g�r': 'je vais',
           'p� gymnasiet': 'au lyc�e', 'tv�an i gymnasiet': 'en premi�re', 'naturprogrammet': 'option scientifique', 'min familj': 'ma famille',
           'min pappa': 'mon p�re', 'min mamma': 'ma m�re', 'en bror': 'un fr�re', 'en syster': 'une soeur', 'en hund': 'un chien',
           'j�tte gullig (f)': 'super mignonne', 'killarna': 'les mecs', 'mina kompisar': 'mes copains', 'shoppa': 'faire du shopping',
           'festa': 'faire la f�te', 'g� p� bio': 'aller au cin�', 'l�sa': 'lire', 'lyssna p� musik': '�couter de la musique', 'sjunga': 'chanter',
           'spela gitarr': 'jouer de la guitare', 'rock': 'du rock', 'min dator': 'mon ordi', 'en hemsida': 'une page web', 'chatta': 'tchatter',
           'p�': 'sur', 'v�nner': 'des amis', '�verallt': 'partout', 'alltid': 'toujours', 'l�gnare': 'les menteurs'}
avoir= {'ha': 'avoir', 'jag har': "j'ai", 'du har': 'tu as', 'han har': 'il a', 'hon har': 'elle a', 'man har': 'on a', 'vi har': 'nous avons',
        'ni har': 'vous avez', 'de har(m)': 'ils ont', 'de har(f)': 'elles ont', 'kom ih�g binda vi, ni, de(f), de(m)(ok)': 'ok'}
extra={'gymnasieklass 1': 'seconde', 'gymnasieklass 2':'premi�re', '�rskurs 3': 'terminale', 'telefonnummer': 'le num�ro de t�l�phone',
       'det �r': "c'est le", 'idag': "aujourd'hui", 'jag fick 20': "j'ai eu 20", 'vilket �mne': 'quelle mati�re', 'du skojar': 'sans blague',
       'en katt':'un chat', 'en bebis': 'un b�b�'}
#redo extra
jesuis= {'en taxichauff�r': 'un chauffeur de taxi', 'gift(m)': 'mari�', 'en kvinna/fru': 'une femme', 'en kass�r(m)': 'un caissier',
         'en kass�rska(f)': 'une caissi�re', 'hon jobbar': 'elle travaille', 'ett barn(m/f)': 'un enfant', 'hon g�r': 'elle va',
         'p� h�gstadiet': 'au coll�ge', 'en s�ngare(m)': 'un chanteur', 'en s�ngerska(f)': 'une chanteuse', 'en sk�despelare(m)': 'un acteur',
         'en sk�despelerska(f)': 'une actrice', 'en sambo(m)':'un compagnon', 'en sambo(f)':'une compagne', 'en dotter': 'une fille',
         'f�dd(m)': 'n�', 'f�dd (f)': 'n�e', 'en son': 'un fils'}
metier={'yrke': 'm�tier', 'advokat(m) + advokat(f)': 'avocat avocate', 'gymnasiestudent(m)+(f)': 'lyc�en lyc�enne', 'tandl�kare': 'dentiste',
        'arkitekt': 'architecte', 'journalist': 'journaliste', 'l�kare': 'm�decin', 'sjuksk�terska(m) + (f)' : 'infirmier infirmi�re',
        'student (m) + (f)': '�tudiant �tudiante', 'industriarbetare(m)+ (f)': 'ouvrier ouvri�re', 'professor': 'professeur',
        'l�rare l�gstadie (m)+ (f)': 'instituteur institutrice', 'cock(m) + (f)': 'cuisinier cuisini�re', 'ingenj�r': 'ing�nieur',
        'programmerere': 'programmeur', 'kass�r(m)+(f)': 'caissier caissi�re', 'taxichauff�r': 'chauffeur de taxi', 'polis': 'agent de police',
        'arbetsl�s': 'au ch�mage'}
#kapitel 4
hexagone= {'ljuv, behaglig (2 s�tt)': 'doux douxe', 'sexh�rningen': "l'hexagone", 'det finns': 'il y a', 'en inv�nare': 'un habitant',
           'huvudstaden': 'la capitale', 'den andra': 'la deuxi�me', 'en stad': 'une ville', 'den n�st st�rsta staden': 'la deuxi�me ville',
           'den tredje': 'la troisi�me', 'medlem i': 'membre de', 'stor(m)+(f)': 'grand grande', 'ett land': 'un pays',
           'industri(m) + (f)': 'industriel industrielle', 'bilarna': 'les voitures', 'franska': 'franc,aises', 'landskapet': 'le paysage',
           'Frankrikes': 'de la France', 'varierat': 'vari�', 'berg':'des montagnes', 'alperna': 'les alpes', 'stora': 'grands',
           'floder': 'fleuves', 'm�nga': 'beaucoup', 'vackra': 'belles', 'str�nder': 'plages', 'p�': 'sur', 'Franska Riverian': "la C�te d'Azur",
           'ungef�r': 'environ', 'n�stan': 'presque', 'en turist (m)': 'un touriste', 'de(m) bes�ker': 'ils visitent', 'varje': 'chaque',
           'ett �r': 'une ann�e', 'l�nderna': 'les pays', 'grann': 'voisins', 'i norr': 'au nord', 'i �ster': "� l'est", 
           'i s�der':'au sud', 'stora': 'grandes', 'hav(pl)': 'mers', 'i v�ster': "� l'ouest"}
lander= {'belgien': 'la belgique', 'luxemburg': 'le luxembourg','tyskland': "l'allemagne", 'schweiz': 'La suisse', 'italien': "l'italie",
         'spanien':"l'espagne",'medelhavet': 'la m�diterran�e', 'Atlanten': "l'atlantique"}
questions={'fr�gor': 'des questions', 'hur mycket (f�re substantiv': 'combien de', 'hur mycket/hur m�nga': 'combien', 'vad, hur': 'comment',
           '�r det s� att': 'est-ce que', 'vem': 'qui', 'vilken/vilket (m)+(f)': 'quel quelle', 'vilka(m pl) + (f pl)': 'quels quelles',
           'var': 'o�', 'vad': "qu'est-ce que", 'vad �r det': "qu'est-ce que c'est"}
parle= {'vi pratar': 'on parle', 'du pratar': 'tu parles', 'vilket spr�k': 'quelle langue', 'dina kompisar': 'tes copains', 'hur gammal': 'quel �ge',
        'h�r': 'ici', 'dagstidningarna': 'les journaux','en skola': 'une �cole', 'p� franska': 'en franc,ais', 'tv': 'la t�l�', 'valutan': 'la monnaie',
        'singel': 'c�libataire', 'ett sjukhus': 'un h�pital', 'd�r': 'o�', 'hemma': '� la maison', 'p� jobbet': 'au travail', 'du g�r': 'tu fais',
        'jag studerar ekonomi': "je fais des �tudes d'�conomie", 'p� universitetet': "� l'universit�", 'ensam': 'seul', 'mina f�r�ldrar': 'mes parents',
        'mor och farf�rldrar': 'grands-parents', 'vi pratar': 'vous parlez', 'vi blandar': 'on m�lange', 'tv�spr�kig': 'bilingue', 'ert namn': 'votre nom',
        'vad g�r ni i livet': "qu'est-ce que vous faites dans la vie", 'min man': 'mon mari', 'vi pratar': 'nous parlons', 'de pratar(m)': 'ils parlent',
        'deras kompisar': 'leurs copains'}

parler= {'prata': 'parler', 'jag pratar': 'je parle', 'du pratar': 'tu parles', 'han pratar': 'il parle', 'hon pratar': 'elle parle',
         'man pratar': 'on parle', 'vi pratar': 'nous parlons', 'ni pratar': 'vous parlez', 'de(m) pratar': 'ils parlent', 'de pratar(f)' : 'elles parlent'}
# Kapitel 5
temp= {'det �r vackert v�der': 'il fait beau', 'det �t d�ligt v�der': 'il fait mauvais', 'det �r varmt': 'il fait chaud', 'det �r kallt': 'il fait froid',
       'det �r gr�tt': 'il fait gris', 'der �r soligt': 'il fait du soleil', 'det bl�ser': 'il fait du vent', 'det regnar':'il pleut',
       'det sn�ar': 'il neige', 'det �r ganska kallt': 'il fait assez froid', 'det �r minus tio': 'il fait moins dix',
       'det �r femton grader': 'il fait quinze degr�s', 'vilket v�der �r det idag': "quel temps fait-il aujourd'hui", 'moln': 'nuage',
       'promenerar': 'se prom�nent', 'n�r': 'quand', 'pl�tsligt': 'tout � coup', 'stannar': "s'arr�te", 'fr�gar honom': 'lui demande',
       'vad g�r du': "que fais-tu"}
veckodag= {'veckogagar': 'les jours de la semaine', 'm�ndag': 'lundi', 'tisdag': 'mardi', 'onsdag': 'mercredi', 'torsdag': 'jeudi', 'fredag': 'vendredi',
           'l�rdag': 'samedi', 's�ndag': 'dimanche'}
ramsa= {'vilken tur': 'quelle chance', 'ett paraply': 'un parapluie', 'en himmel': 'un ciel', '�ta': 'manger', 'en milion': 'un million',
        'ett lotteri': 'une loterie', 'dansa':'danser', 'hela natten': 'tout la nuit', 'i s�ngen': 'au lit', "till mitt p� dagen": "jusqu'� midi",
        'lov/semester': 'vacances'}
heures={'klockan �r tio': 'il est dix heures', 'kvart �ver': 'et quart', 'och halvtimme': 'et demie', 'kvart i': 'moins le quart', 'tjugo i': 'moins vingt',
        'h�sten': "l'automne", 'vintern': "l'hiver", 'v�ren': 'le printemps', 'sommaren': "l'�t�"}
#Kapitel 6
hotel= {'ett hotell': 'un h�tel', 'jag skulle vilja': 'je voudrais', 'boka': 'r�server', 'ett sovrum': 'une chambre', 'f�r': 'pour', 'en natt': 'une nuit',
        'v�nta': 'attandez', 'jag �r ledsen/beklagar': 'je suis d�sol�', 'fullt': 'complet', 'det �r synd': "c'est dommage", 'vi kan': 'on peut',
        'ringa': 't�l�phoner', 'ledig': 'libre', 'en person': 'une personne', 'vad kostar det': "c'est combien", 'frukosten': 'la petit d�jeuner',
        'inkluderad': 'compris', 'kostar tv� euro': 'est � deux euros', 'per person': 'par personne', 'jag bokar det': 'je la r�serve',
        'i vilket namn': '� quel nom', 'anl�nda till': 'arriver �', 'vi har bokat': 'nous avons r�serv�', 'en id hndling': "une pi�ce d'identit�",
        'en nyckel': 'une cl�', 'en hiss': 'un ascenseur'}
dejeuner= {'sockret': 'le sucre', 'sylt': 'la confiture', 'apelsinjuice': "le jus d'oragne", 'toastat br�d': 'le pain grill�', 'flingor': 'les c�r�ales',
           'br�d': 'le pain', 'croissant': 'le croissant', 'te': 'le th�', 'grillat br�d macka': 'la tartine', 'sm�r': 'le beurre', 'en loppa': 'une puce',
           'de g�r ut': 'elles sortent', 'eller': 'ou', 'kyssa p� kinden': 'faire la bise', 'vacker': 'beau', 'som jag': 'comme moi',
           'en tr�ff': 'un rendez-vous', 'kram': 'gros bisous' }
train= {'med t�g': 'en train', 'leta': 'chercher', 'till': 'pour', 'tung': 'lourd', 'd�dstr�tt': 'crev�', 'det �r bra/st�mmer': "c'est bon",
        '�ntligen': 'enfin', 'j�ttes�ta': 'trop mignons', 'jag': 'moi', 'den stan': 'cette ville', 'd�r': 'l�', 'ett vandrarhem': 'une auberge de jeunesse',
        'dessutom': 'en plus', 'vi �ker okmring i': 'on fait le tour de', '�ka tillbaka': 'rentrer', 'ellerhur': 'hein',
        'vi tycker det �r h�ftigt': 'on est fan', 'f�r oss': 'pour nous', 'f�rsta(m+f)': 'premier premi�re', 'sova': 'dormir',
        'n�ra' : 'pr�s de', 'en gata': 'une rue', 'en tunnelbana': 'un m�tro', 'man m�ste': 'il faut', 'de tror jag': 'je crois',
        'det �r mycket folk': 'il y a du monde', 'h�rni, lyssna': '�coutez', 'tillsammans': 'ensemble', 'en mobil': 'un portable'}
aller= {'g�': 'aller', 'jag g�r': 'je vais', 'du g�r': 'tu vas', 'han g�r': 'il va', 'hon g�r': 'elle va', 'man g�r': 'on va', 'vi g�r' : 'nous allons',
        'ni g�r': 'vous allez', 'de (m) g�r': 'ils vont', 'de (f) g�r)': 'elles vont'}
        


## DELKURS 2

#Kapitel 7
cartes= { "kram": 'grosses bises', 'ett vykort': 'une carte postale', 'k�ra(f)': 'ch�re', 'k�ra(m)': 'cher', 'mormor/farmor': 'mamie',
          'n�gra rader': 'un petit mot', 'd�r': 'o�', 'tillbringa': 'passer', 'en h�rlig semester': 'de bonnes vacances', 'semester': 'des vacances',
          '�r bel�get, ligger': 'est situ�', 'en meter': 'un m�tre', 'olyckligtvis': 'malheureusement', 'vattnet': "l'eau", 'skaldjur': 'des crustac�s',
          'du m�r': 'tu vas', 'kram': 'gros bisous', 'gata': 'boulevard', 'jag s�nder dig': "je t'envoie", 'en liten j�lsning': 'un petit bonjour',
          'korsika': 'la corse', 'toppen': 'superbe', 'en tr�ff/m�te': 'un rendez-vous', 'solen kikar fram': 'le soleil est au rendez-vous',
          'en strand': 'une plage', 'varje dag': 'tous les jours', '�ta': 'mange'}
faire= { 'g�ra': 'faire', 'jag g�r': 'je fais', 'du g�r': 'tu fais', 'han g�r': 'il fait', 'hon g�r': 'elle fait', 'man g�r': 'on fait',
         'vi g�r': 'nous faisons', 'ni g�r': 'vous faites', 'de (m) g�r': 'ils font', 'de g�r(f)': 'elles font'}
tuesou= { 'har du hittat': 'tu as trouv�', 'du vet': 'tu sais', 'ibland': 'parfois', 'd�s�, n�ja, ok': 'bon', 'hur som helst': 'en tout cas',
          'd� s�!': 'ben voil�', 'jag m�ste': 'je dois', 'sluta': 'arr�ter', 'tillslut': 'finalement',
          'thomas och jag har gjort slut': 'on a cass� avec thomas', 'jas�': 'ah oui', 'allts�': 'donc', 'ofta': 'souvent', 'jag f�rst�r':"j'ai compris",
          's� �r det': "c'est c,a", 'samtidigt': 'en m�me temps', 'det g�r inget': "c'est pas grave", 'k�r i (m)': 'amoureux de', 'k�r i(f)': 'amoureuse de',
          'kom igen': 'allez', 'verkligen': 'tiens', 'komma f�r sent': '�tre en retard', 'f�r mycket': 'trop', 'inte s� v�rst': 'pas trop',
          'det skille vara toppen': 'c,a serait super', 'att hitta': 'trouver', 'att bryta': 'casser'}
#Kapitell8
HotelVille= {'tr�tta': 'fatigu�s', 'hitta': 'trouver', 'titta/titta p�': 'regarde', 'en skylt': 'un panneau', 'vi fr�gar': 'on demande �',
             'en dam': 'une dame', 'urs�kta': 'pardon', 'hur kommer man till': 'pour aller �', 'l�tt': 'facile', 'forts�tta': 'continuer',
             'rakt fram': 'tout droit', 'andra gatan': 'la deuxi�me rue', 'till v�nster': '� gauche', 'passera': 'passer', 'efter': 'apr�s',
             'en kyrka': 'une �glise', 'sv�ng': 'tournez', 'till h�ger': '� droite', 'd�r': 'l�', 'skratta': 'rire', 'en borgm�stare': 'un maire',
             'sedan': 'traverser', 'sedan': 'puis', '�nda till': "jusqu'�", 'torget': 'la place',
             'sedan': 'ensuite', 'dyr (m)': 'cher', 'dyr (f)': 'ch�re', 'billig': 'pas cher', 'mitt emot': 'en face de', 'brevid': '� c�t� de'}
velib= {'turistbyr�': "l'office de tourisme", 'banken': 'la banque', 'en stadscykel': 'un v�lib', 'en pojkv�n': 'un petit ami', 'hon f�r':'elle rec,oit',
        'hennes/sin': 'sa', 'en kusin (m)': 'un cousin', 'en kusin(f)': 'une cousine', 'vem d�': 'qui c,a', 'f�rst':"d'abord", 'galen//tokig (m)': 'fou',
        'galen/tokig (f)' : 'folle', 'det �r uppf�rsbacke': 'c,a monte', 'en gr�smatta': 'une pelouse', 'lite': 'un peu', 'en frukt': 'un fruit',
        'inget/ingen': 'pas de', 'en cykel': 'un v�lo', 'cykla': 'faire du v�lo', 'g� upp i': 'monter �', 'en trappa': 'un escalier',
        'billigare': 'moins cher', 'mindre, kortare': 'moins de', 'stanna kvar': 'rester', 'd�r nere': 'en bas', 'det kostar': 'c,a co�te',
        'det �r inte klokt': "c'est dingue", 'k�nd': 'connu', 'ibland': 'des fois', 'man/vi vill': 'on veut', 'vilja': 'vouloir',
        'medan vi v�ntar': 'en attendant', 'k�pa': 'acheter', 'skratta/skoja': 'rigoler', 'vi r�r oss': 'on bouge', 'mot': 'vers',
        'till fots': '� pied', 'tillslut': 'pour terminer', 'det r�cker': "c,a suffit", 'sista': 'dernier', 'gillar du det': 'c,a te dit',
        'deras': 'leur', 'eller ocks�': 'ou bien'}
#Kapitel9
amongout= { 'i min smak': '� mon go�t', 'en f�rg': 'une couleur', 'en fr�ga om': 'une question de', 'en smak': 'un go�t', 'g� in/komma in': 'entrer',
            'l�mna': 'quitter', 'livet i f�rg': 'la vie en couleurs', 'ibland': 'des fois', 'jag fr�gar mig sj�lv': 'je me demande',
            'varf�r': 'pourquoi', 'en teve': 'une t�l�', 'd�remot': 'par contre', 'en v�gg': 'un mur', 'de andra':'les autres',
            'gardiner': 'des rideaux', 'en matta': 'un tapis', 'trikoloren(franska flaggan)': 'le drapeau tricolore', 'en s�ng': 'un lit',
            'en prydnadskudde': 'un coussin', 'i alla f�rger': 'de toutes les couleurs', 'en affisch': 'un poster', 'en m�lare': 'un peintre',
            'ett skrivbord': 'un bureau', 'en stol': 'une chaise', '�ven om': 'm�me si', 'tycka/t�nka': 'penser', 'var och en har sin smak':
            '� chacun son go�t'}
lescouleurs= { 'bl�': 'bleu bleue', 'gr�': 'gris grise', 'gr�n': 'vert verte', 'vit': 'blanc blanche', 'gul': 'jaune', 'rosa': 'rose',
               'r�d': 'rouge', 'svart': 'noir noire', 'lila': 'violet violette', 'beige': 'beige', 'brun': 'marron', 'orange': 'orange'}
sovrum= {'en soffa': 'un canap�', 'en f�t�lj': 'un fauteuil', 'en tavla': 'une tableau', 'ett bord' : 'un table',
         'en stol': 'une chaise', 'en byr�': 'une commode', 'en spegel': 'un miroir', 'en skorsten': 'une chemin�e',
         'en lampa':'une lampe', 'helt�ckningsmatta': 'une moquette', 'en garderob': 'une armoire', 'p�': 'sur',
         'till v�nster om': '� gauche de', 'till h�ger om': '� droite de'}
studio= {'en etta med kokvr�': 'un studio', 'mellan': 'entre', 'ett f�nster': 'une fen�tre', 'en stereo': 'une cha�ne hi-fi',
         'en hylla': 'une �tag�re', 'ni ser': 'vous voyez', 'ett kl�dsk�p': 'une armoire', 'i m�rkt tr�': 'en bois brun', 'kl�derna': 'les v�tements',
         'bredvid': '� c�t� de', 'ett nattduskbord': 'une table de nuit', 'en klockradio': 'un radio-r�veil', 'ett k�k': 'une cuisine',
         'lyons fotbollslag': "l'Olympique Lyonnais", 'ett vardagsrum' : 'une salle de s�jour', 'beh�va': 'avoir besoin de', 'en gasplatta':
         'un r�chaud � gaz', 'en ugn': 'un four', 'ett kylsk�p': 'un frigo', 'en diskb�nk': 'un �vier', 'diska': 'faire la vaisselle',
         'ett badrum': 'une salle de bains', 'ganska' : 'assez' }
#Studio g�r om
#Genial 2
#Kapitel 1

CDG= { '�lskling':'ch�ri', 'fattar du' : 'tu te rends compte', 'inse, f�rst�': 'se rendre compte', 'v�nta p�': 'attendre', 'jag ska polisanm�la':
       'je vais porter plainte', 'vad �r det': "qu'est-ce qu'il y a", 'ett flygplan': 'un avion', 'vara f�rsenad': '�tre en retard', 'de s�ger oss':
       'ils nous disent', 'bara': 'seulement', 'ingenting': 'ne ... rien', 'irritera' : '�nerver', '�nnu mer': 'encore plus', 'en chef': 'un patron',
       'nyss ha': 'venir de', 'beh�va': 'avoir besoin de', 'sina l�xor': 'ses devoirs', 'celine fr�gade mig': "celine m'a demand�", 'l�gg p�':
       'raccrocher', 'dricka': 'boire', 'd�r borta': 'l�-bas', 'ombordsstigning (m)': 'embarquement', 'en gate': 'un porte', 'redan': 'd�j�',
       'en flygning': 'un vol', 'n�sta': 'prochain', 'bara': 'juste', 'olyckliggtvis': 'malheureusement', 'sl� (ett nummer)': 'composer' }
europe= {'USA' : 'les Etats-Unis', 'p� en vecka': 'en huit jours', 'en vistelse': 'un s�jour', 'ha det s� trevligt' : 'bon s�jour',
         'midnattssolen': 'le soleil de minuit', 'M�nchen': 'Munich', 'en korv' : 'une sauciesse', 'innan/f�re': 'avant', 'innan han g�r �ver':
         'avant de traverser', 'en present': 'un cadeau', 'ett armbandsur': 'une montre', 'Genevesj�n': 'le lac L�man', 'en mussla': 'une moule',
         'pommes frites': 'des frites', 'musslor med pommes frites': 'des moules frites', 'en kanal': 'un canal', 'kanaler': 'des canaux',
         'hyra': 'louer', 'nederl�nderna': 'les Pays-Bas', 'en sk�rg�rd': 'un archipel', 'himlen':'le ciel', 'vilken semester': 'quelles vacances',
         'alltf�r': 'trop', 'r�ra p� sig': 'bouger', 'en t�rta': 'un g�teau', 'ett slott': 'un ch�teau', 'utmattad, d�dstr�tt': 'crev�',
         'g�rdagen': 'la veille', 'han tar p� sig': 'il met', 'solglas�gon': 'des lunettes de soleil', 'han solar': 'il bronze', 'simma': 'nager',
         'inte mer/ inte l�ngre': 'ne ... plus', 'han har inga pengar kvar': "il n'a plus d'argent", 'pengarna': "l'argent", 'en kurs': 'un stage'}
partir= {'resa/ ge sig av': 'partir', 'jag reser': 'je pars', 'du reser': 'tu pars', 'han reser': 'il part', 'hon reser': 'elle part', 'vi reser':
         'on part', 'vi reser': 'nous partons', 'ni reser': 'vous partez', 'De (f) reser': 'elles partent', 'De (m) reser': 'ils partent'}
famille= {'f�r�ldrar': 'parents', 'man/make': 'mari', 'fru': 'femme', 'sambo': 'compagnon', 'sambo yngre (m)': 'copain ami', 'sambo yngre (f)':
          'copine amie','tvilling (m)': 'jumeau', 'tvilling (f)': 'jumelle', 'tvillingar (m osen f)': 'jumeaux jumelles', 'barnbarn(f)': 'petite-fille',
          'barnbarb(m)':'petit-fils', 'morbror/farbror': 'oncle', 'moster/faster': 'tante', 'kusin m' : 'cousin', 'kusin f': 'cousine',
          'bror/systerson': 'neveu', 'bror/systerdotter': 'ni�ce', 'sv�rfar': 'beau-p�re', 'sv�rmor': 'belle-m�re', 'sv�ger': 'beau-fr�re',
          'sv�gerska': 'belle-soeur', 'gift(m)': 'mari�', 'separerad (m)': 's�par�','skild m': 'divorc�', 'singel m': 'c�libataire', 'd�d m': 'mort'}
# Kapitel 2
piquenique= {'g�rna': 'avec plaisir', 'vid havet': 'au bord de la mer', 'tonfisk(m)': 'thon', 'en frukt': 'un fruit', 'n�gra/lite': 'un peu de',
             'man m�ste': 'il faut', 'f�rst': "d'abord", 'en marknad': 'un march�', 'handla': 'faire des courses', 'n�got annat?': 'et avec c,a',
             'jag beh�ver': 'il me faut', 'ett �pple': 'une pomme', 'det �r bra s�': "c'est bien comme c,a", 'ha en trevlig dag': 'bonne journ�e',
             'vatten': "de l'eau", 'precis, just det': 'justement', 'k�pa': 'acheter', 'ska vi sl� oss ner h�r': "on s'installe ici", 'perfekt': 'parfait',
             'en utsikt': 'une vue', '�ver':'sur', 'fantastiskt': 'superbe', 'jag �r hungrig': "j'ai faim", 'hungrig som en varg': 'une faim de loup',
             'jag �r t�rstig': "j'ai soif", 'ett glas vatten': "un verre d'eau", 'genast': 'tout de suite', 'smaklig m�ltif': 'bon app�tit'}
fruit= {'ett halvt kilo': 'une livre', 'mogen': 'm�r', 'totalt': 'au total', 'en citron': 'un citron', 'en melon': 'un melon', 'en annanas': 'un ananas',
        'en aprikos': 'un abricot', 'en kiwi':'un kiwi',
             'en grapefrukt': 'un pamplemousse', 'en vattenmelon': 'une past�que', 'en apelsin': 'un orange', 'hallon' : 'des framboises',
             'en banan': 'une banane', 'ett �pple': 'une pomme', 'en persika': 'une p�che', 'ett plommon': 'une prune', 'ett p�ron': 'une poire',
             'k�rsb�r': 'des cerises', 'vindruvor': 'du raisin', 'jordgubbar': 'des fraises'}
legumes= {'gr�nsaker': 'des l�gumes', 'majs': 'du ma�s', 'en avokado': 'un avocat', 'en l�k': 'un oignon', 'en gurka': 'un concombre',
          'en blomk�l': 'un chou-fleur', 'en paprika': 'un poivron', 'en tomat': 'une tomate', 'en morot': 'une carotte', 'vitl�k': "de l'ail",
          'potatisar': 'des pommes de terre', 'spenat': 'des �pinards', 'svamp': 'des champignons', 'en zuccini': 'une courgette',
          'en aubergie': 'une aubergine', 'en sallad': 'une laitue'}
uttryck= {'ha lust att': 'avoir envie', 'frysa': 'avoir froid', 'vara varm': 'avoir chaud', 'ha r�tt': 'avoir raison', 'ha fel': 'avoir tort',
          'vara r�dd f�r': 'avoir peur de', 'sk�mmas f�r': 'avoir honte', 'beh�va': 'avoir besoin de', 'vara s�mnig': 'avoir sommeil' }
restaurant= {'resa': 'voyager', 'under om tid': 'pedant', 'd�r �r de': 'les voil�', 'en meny': 'un menu', 'med kolsyra m f': 'gazeux gaseuse',
             'utan kolsyra m f': 'plat plate', 'har ni best�mt er': 'vous avez choisi', 'rekomenderar': 'recommander', 'alltf�r': 'trop',
             'en f�rr�tt': 'une entr�e', 'en gryta': 'un civet', 'en kanin': 'un lapin', 'en s�s': 'une sauce', 'det �r n�dv�ngigt': 'il faut',
             'en ordbok': 'un dictionnaire', 'jag f�rst�r': 'je comprends', 'en tupp i vin': 'un coq au vin', 'hur smakade det': 'c,a a �t�',
             'uts�kt m f ': 'd�licieux delicieuse', 'en efter�tt': 'un dessert', 'en kula': 'une boule', 'det �r bra s�': 'c,a va bien comme c,a',
             'notan': "l'addition"}
mettreboire= {'s�tta st�lla l�gga': 'mettre', 'jag l�gger': 'je mets', 'du l�gger': 'tu mets', 'han, (hon, man) l�gger': 'il met', 'vi l�gger':
              'nous mettons', 'ni l�gger': 'vous mettez', 'de m (de f) l�gger' : 'ils mettent', 'dricka': 'boire', 'jag dricker': 'je bois',
              'du dricker': 'tu bois', 'han (hon man) dricker': 'il boit', 'vi dricker': 'nous buvons', 'ni dricker': 'vous buvez',
              'de m (de f) dricker': 'ils boivent'}
chans= {'min svaghet': 'mon p�ch� mignon', 'vaniljkr�m': 'la cr�me anglaise', 'jag suger ur benen': 'je suce les os', 'torkade fikon': 'des figues s�ches',
        'honungen': 'le miel', 'sockerkaka indr�nkt med rom': 'la baba au rhum', 'det �r antecknat': "c'est not�", 'st�r det?': 'c,a ne vous g�ne pas',
        'tv�rtom': 'au contraire'}

### Kurs 2 - A12

# Kapitel 3
tropcher= {'kl�derna': 'les fringues', 'vad': 'quoi', 'ge' : 'offrir', 'i kv�ll': 'ce soir', '�nnu': 'encore', 'jag har inte haft tid att':
           "je n'ai pas eu le temps de", '�t/ till honnom': 'lui', 'sk�mtar du eller': 'tu rigoles ou quoi', 's�': 'tellement',
           'jag blir': 'je deviens', 'galen m f': 'fou folle', 'jag lovar; verkligen': 'ma parole', 'jag f�ljer med dig': "je t'accompagne",
           'skynda dig': 'd�p�che-toi', 'avdelningen': 'le rayon', 'en tr�ja': 'un pull', 'du har r�tt': 'tu as raison', 'inte direkt': 'pas tellement',
           'i alla fall/ �nd�': 'quand m�me', 'tillr�ckligt med': 'assez de', 'pengar': 'du fric', 'det �r sant': "c'est vrai", 'har du sett': "t'as vu",
           'kom': 'viens', 'en groda': 'une grenouille', 'du tycker': 'tu trouves', 'det �r': 'c,a fait', 's�d�r/ s�h�r': 'comme c,a', 'modernt':'tendance',
           'vilken storlek har han': 'il fait quelle taille', 'en kl�dstorlek': 'une taille', 'jag skulle s�ga': 'je dirais', 'han har L': 'il fait du L',
           'hj�lpa': 'aider', 'ett �gonblick': 'un instant', 'jag tar den': 'je le prends', 'ett betalkort': 'une carte', 'knappa in': 'taper',
           'ett kvitto': 'un ticket'}
lesvetements= {'kl�derna': 'les v�tements', 'en T-shirt': 'un T-shirt', 'en tr�ja': 'un pull', 'en tennistr�ja': 'un polo', 'en sweatshirt':'un sweat-shirt'
               , 'en kofta/v�st': 'un gilet', 'en skjorta': 'une chemise', 'ett linne': 'un d�bardeur', 'byxor': 'un pantalon', 'jeans': 'un jean',
               'shorts': 'un short', 'en kavaj/ jacka': 'une veste', 'en rock/kappa': 'un manteau', 'en midjel�ng jacka': 'un blouson',
               'en kort skinnjacka':'un blouson en cuir', 'en dunjacka': 'une doudoune', 'en tr�ningsoverall': 'un jogging', 'en l�tt regnjacka':'un K-way',
               'en scarf': 'un foulard', 'en halsduk': 'une �charpe', 'en m�ssa': 'un bonnet', 'en keps': 'une casquette', 'en hatt': 'un chapeau',
               'strumpor': 'des chausettes', 'handskar': 'des gants', 'ett sk�rp': 'une ceinture', 'skor': 'des chaussures', 'sandaler': 'des sandales',
               'st�vlar': 'des bottes', 'gymnastikskor': 'des baskets', 'f�r honom': 'pour lui', 'badbyxor': 'un maillot', 'en slips':'une cravate',
               'kalsonger': 'un slip', 'en kostym': 'un costume', 'f�r henne': 'pour elle', 'en blus': 'un chemisier', 'damsockor': 'des socquettes',
               'thights/legging': 'des leggings', 'en bikini/baddr�ckt': 'un bikini un maillot', 'en kl�nning': 'une robe', 'en kjol': 'une jupe',
               'en beh�': 'un soutien-gorge un soutif', 'en trosa': 'une culotte un slip'}
acheter= {'k�pa': 'acheter', 'jag k�per': "j'ach�te", 'du k�per': 'tu ach�tes', 'han k�per': 'il ach�te', 'vi k�per': 'nous achetons',
          'ni k�per': 'vous achetez', 'de (m) k�per': 'ils ach�tent'}
rire= {'en baby': 'un b�b�', 'sova middag': 'faire la sieste', 'samma': 'm�me', 'lyfta': 'soulever', 'ett lakan': 'un drap', 'f�reta/g�ra': 'proc�der �',
       'en unders�kning': 'un examen', 'man har satt sig p�' : "on t'as mis"}
balade= {'en promenad': 'une balade', 'det �r riktigt hundv�der': 'il fait un temps de chien', 'det �r tydligt': "c'est clair",
         'vad h�nder': "qu'est-ce quise passe", 'sydfrankrike': 'le Midi', 'hemskt f�rskr�ckligt': '�pouvantable', 'man skulle kunna tro': 'on se croirait',
         'jag �r ledsen': 'je suis d�sol�', 'iskall': 'glacial', 'en tr�tt': 'un rendez-vous', 'vid': 'vers', 'v�rma upp sig': 'se r�chauffer',
         'i': 'par', 'det h�r v�dret': 'ce temps', 'vi ses': 'a toute'}
plustard= { 'ny m f': 'neuf neuve', 'alldeles ny': 'tout neuf', 'kolla': 'tiens', 'k�nner du till': 'tu connais', 'en m�lare': 'un peintre',
            'favorit': 'pr�f�r�', 'hos mig': 'chez moi', 'helig': 'ste', 'en tavla': 'un tableau', 'rea': 'soldes', 'en aff�r': 'un magasin',
            'en t�ckjacka': 'un blouson matelass�', 'prova': 'essayer', 'prova den': "l'essayer", 'du kommer inte att frysa mer': "tu n'auras plus froid",
            'j�tteh�ftig': 'trop top', 'svindyrt/superbilligt': 'un prix fou', 'en provhytt': 'une cabine', 'l�ngst bort': 'au fond'}
meramer= {'kassan': 'la caisse', 'betala' : 'payer', 'ett plagg': 'une pi�ce', 'gammal m f': 'vieux vieille', 'hotell resturang programmet gymn':
          'un lyc�e h�telier', 'en dr�kt': 'un tailleur', 'en kl�dsel': 'une tenue', 'en ledig kl�dsel': 'une tenue d�contract�e', 'kan jag hj�lpa dig':
          "je peux vous aider", 'l�ngst il': 'au fond', 'enligt min �sikt': '� mon avis'}
vendre= {'s�lja': 'vendre', 'jag s�ljer': 'je vends', 'du s�ljer': 'tu vends', 'han s�ljer': 'il vend', 'vi s�ljer': 'nous vendons', 'ni s�ljer':
         'vous vendez', 'de (m) s�ljer': 'ils vendent'}
cecescette= { 'i mrose': 'ce matin', 'i v�ras/i v�r' :'ce printemps', 'i eftermiddags/i eftermiddag': 'cet apr�s-midi',
              'i sommar/ i somras': 'cet �t�', 'i kv�ll': 'ce soir', 'i h�st/i h�stas': 'cet automne', 'i vinter/i vintras': 'cet hiver'}

attandre= {'v�nta': 'attendre', 'jag v�ntar': "j'attends", 'du v�ntar': 'tu attends', 'han v�ntar': 'il attend',
           'vi v�ntar': 'nous attendons', 'ni v�ntar': 'vous attendez', 'de (m) v�nar': 'ils attendent' }


repondre= {' jag svarar': 'je r�ponds', 'du svarar': 'tu r�ponds', 'han svarar': 'il r�pond', 'vi svarar': 'nous r�pondons',
           'ni svarar': 'vous r�pondez', 'de (m) svarar': 'ils r�pondent'}
#L'articel partitif + n�gation --> endast de anv�nds i negationer medans du, de la, des anv�nds annars
 


#Kapitel 4

catherine= {'som vanligt': "comme d'habitude", 'vi stiger upp': "nous nous levons", 'jag sminkar mig': "je me maquille", 'jag fixar h�ret': 'je me coiffe',
            'i allm�nhet': 'en g�n�ral', 'befinna sig, vara': 'se trouver', '(h�r)det tar mig': 'je mets', 'en knapp halvtimme': 'une petite demi-heure',
            'en landsv�g': 'une route', 'varken ... eller': 'ni ... ni', 'trafik': 'circulation', 'halt v�glag/halka': 'verglas',
            'en optiker (m)': 'un opticien', 'en optiker (f)': 'une opticienne', 'f�rs�ljning(f)': 'vente', 'ensam(m)': 'seul',
            'jag har inte tr�kigt': "je ne m'ennuie pas", 'n�r det g�ller': 'au niveau de', 'en arbetstid/ ett schema': 'un horaire', 'vilket': 'ce qui',
            'd�/n�r': 'o�', 'vara ivrig att': 'avoir h�te de', 'vila mig': 'me reposer', 'den som': 'celui qui', 'laga mat': 'faire � manger',
            'diska': 'faire la vaisselle', '(h�r) g�/s�nds': 'passer', 'f�rs�ka': 'essayer', 'ett pass': 'une s�ance', 'streching': 'des �tirements',
            'crunches/situps': 'des abdominaux', 'vi g�r och l�gger oss': 'nous nous couchons', 'ett slut': 'une fin'}
olivier= {'�rskurs ett': 'seconde', 'jag stiger upp': 'je me l�ve', 'jag tv�ttar mig': 'je me lave', 'ja g�r mig i ordning': 'je me pr�pare',
          'jag m�ste': 'je dois', 'en lektion':'un cours', 'b�rja': 'commencer', 'en rast': 'une r�cr�ation', 'det vill s�ga': "c'est-�-dire",
          'putsa ut': 'souffler', 'ett f�rh�r/prov': 'une interrogation', 'utnyttja/dra nytta av': 'profiter', 'repetera/l�sa p�': 'r�viser',
          'fickpengar': 'argent de poche', 'en s�tpotatis': 'une patate', 'van': 'habitu�', 'hj�lpa': 'aider', 'ved':'bois', 'en dunk': 'un bidon',
          'k�llvatten': 'eau de la source', 'en deg': 'une p�te', 'en l�xa': 'un devoir', 'till och med': 'm�me', 'grejer': 'affaires',
          'kasta ut': 'jeter dehors', 'en surfplatta': 'une tablette', 'kyrkog�rd': 'cimeti�re', 'kissa': 'faire pipi', 'sn�ll': 'sage'}
Reflexiva_verb= {'tv�tta sig': 'se laver', 'sminka sig': 'se maquiller', 'g�ra sig i ordning': 'se pr�parer', 'skynda sig': 'se d�p�cher',
                 'g� o l�gga sig': 'se coucher', 'kl� p� sig': "s'habiller", 'k�pa sig': "s'acheter", 'jag l�gger mig': 'je me couche',
                 'du l�gger dig': 'tu te couches', 'han l�gger sig': 'il se couche', 'vi l�gger oss': 'nous nous couchons',
                 'ni l�gger er': 'vous vous couchez', 'de l�gger sig (m)': 'ils se couchent' }
#Reflexiva verb i passe compose anv�nder etre. till exempel je me suis lav�e --> jag tv�ttade mig
#Passe compose j'ai jouer --> vem + avoir + verb i pass� copose
#Futurum (JAG SKA) jag vais --> vem + aller + verb i grundform (i vissa fall) I andra fall b�js det som nedan:
fururum= {'jag kommer att g�': "j'irai", 'du kommer att g�': 'tu iras', 'han kommer att g�': 'il ira', 'vi kommer att g�': 'nous irons',
          'ni kommer att g�': 'vous irez', 'de (m) kommer att g�': 'ils iront', 'jag kommer att vara': 'je serais',
          'du kommer att vara': 'tu seras', 'han kommer att vara': 'il sera', 'vi kommer att vara': 'nous serons',
          'ni kommer att vara': 'vous serez', 'de (m) kommer att vara': 'ils seront', 'g�mma': 'cacher', 'jag kommer att g�mma mig': 'je cacheras',
          'du kommer att g�mma dig': 'tu cacheras', 'han komemr att g�mma sig': 'il cachera', 'vi kommer att g�rra oss': 'nous cacherons',
          'ni kommer att g�mma er': 'vous cacherez', 'de(m) kommer att g�mma sig' : 'ils cacheront'}
          
unmatin= {'alla andra': 'tous les autres', 'visa, ange': 'indiquer', 'v�ckarklockan': 'le r�veil', 'vard. ett jobb': 'un boulot',
          'f�r att ta sig dit': "pour s'y rendre", 'han g�r kaffe �t sig': 'il se fait un caf�', 'h�lla': 'verser', 'v�lta': 'renverser',
          'reng�ra': 'nettoyer', 'sk�ra': 'couper', 'en skiva': 'une tranche', 'fingret': 'le doigt', 'tusan ocks�': 'zut', 'ett pl�ster':'un pansement',
          'raka sig': 'se raser', 'strunt samma': 'tant pis', 'starta': 'd�marrer', 'gripas av panik': 'paniquer', 'ett f�retag': 'une entreprise',
          'dit, d�r': 'y', 'ingen �r d�r': "personne n'est l�", 'ingen': 'ne ... personne', 'antingen ... eller': 'ou ... ou', 'pasta': 'des p�tes',
          'ris': 'du riz', 'fixa k�k': 'faire la bouffe', 'honung': 'du miel', 'vissla': 'siffler'}
devoir= { 'm�ste/ska': 'devoir', 'jag m�ste': 'je dois', 'du m�ste': 'tu dois', 'han m�ste':'il doit',
          'vi m�ste': 'nous devons', 'ni m�ste': 'vous devez', 'de m�ste': 'ils doivent'}
nene= {'dra nytta av': 'profiter de', 'l�ngt ifr�n': 'loin de', 'ingenting': 'ne ... rien',
       'inte f�rr�n': 'ne ... que', 'det beror p�': 'c,a d�pend'}
apprendre= {'l�ra sig': 'apprendre', 'medan han tittar p�': 'en regardant', 'ge sig iv�g': 'se rendre', 'f�r sent': 'trop tard',
            'ingen': 'ne ... personne'}
finir= {'avslute/sluta':'finir', 'jag sluter': 'je finis', 'du slutar': 'tu finis', 'han slutar': 'il finit',
        'vi slutar': 'nous finissons', 'ni slutar': 'vous finissez', 'de (m) slutar': 'ils finissent',
        'v�lja': 'choisir', 'att lyckas': 'r�ussir', 'att reflektera': 'r�fl�chir'}


# kapitel 5

auvoleur= {'ta fast tjuven': 'au voleur', 'en tjuv': 'un voleur', 'sommarlover':'les grandes vacances', 't�gluffa': 'voyager avec interrail',
           'en kille': 'un mec', 'inte illa': 'pas mal', 'den, han, honom': 'celui', '�gon, �gonen': 'les yeux', 'den andra': "l'autre",
           '�nnu': 'encore', 'snyggare': 'plus beau', 'h�ret': 'les cheveux', 'krulligt, lockigt': 'boucl�', 'ett leefe': 'un sourire',
           'de kommer fr�n': 'ils viennent de', 's�tta sig': "s'asseoir", 'vars�god/ ta f�r er': 'allez-y', 's�tt er': 'asseyez-vous', 'inte heller': 'non plus',
           'en accent': 'un accent', 'se, bes�ka': 'voir', 'trevlig': 'sympa', 'pl�tslig': "tout d'un coup", 'stanna': "s'arr�ter", 'kom': 'viens',
           'vi m�ste': 'on doit',  'stiga av': 'descendre', 'vi ses!': '� la prochaine', 'falla, ramla': 'tomber', 'armarna/ famnen': 'les bras', 'hj�pa hen': "l'aider",
           'vi ses': 'on se voit' , 'ett vandrarhem': 'une auberge de jeunesse', 'en pl�nbok': 'un portefeuille', 'en polisstation':'un commissariat de police',
           'arg(m)': 'f�ch�', 'gr�ta': 'pleurer'}
#un beau, un bel homme --> n�r det �r un o vokal blir det bel, deux beaux hommes
#une belle, trois belles 
beau= { 'en snygg kille': 'un beau garc,on', 'en snygg man': 'un bel homme', 'tv� snygga killar': 'deux beaux hommes', 'en snygg tjej': 'une belle fille',
        'tre snygga tjejer': 'trois belles femmes', 'en gammal hund': 'un vieux chien' ,'en gammal v�n (m)': 'un vieil ami', 'fyra gamla v�nner(m)': 'quatre vieux amis',
        'en gammal v�n(f)': 'une vielle ami', 'tre gamla v�nner': 'trois vielles amies', 'en ny mobil': 'un nouveau portable', 'ett nytt hotell': 'un nouvel h�tel',
        'tv� nya hotell': 'deux nouveaux h�tels' , 'en ny skjorta': 'une nouvellle cheimise', 'tre nya skjortor': 'trois nouvelles chemises'}
extrakap5= {'en g�gata': 'une rue pi�tonne', 'en musiker': 'un musicien', 'ett f�rh�r': 'une interrogatoire', 'ett id kort': " une carte d'inentit�",
            'f�rgat h�r': 'les cheveux teints', 'man/vi sover': 'on dort', 'om ni vill': 'si vous voulez', 'jag hoppas ni urs�ktar': 'vous permettez',
            'ett visa kort': 'une carte VISA', 'guld(m)': 'or', 'stoppar' : 'fait stopper', 's�g ni inte': "vous n'avez pas vu", 'r�dljuset': 'le feu rouge',
            'en t�ndsticka': 'une allumette', 't�nda': 'allumer', 'hel': 'entier', 'm�rkret': 'la obscurit�', 'minnas': 'rappeler', 'n�r jag h�ller dig': 'en te serrant' }
venir= {'jag kommer': 'je viens', 'du kommer' : 'tu viens', 'han kommer': 'il vient', 'vi kommer': 'nous venons', 'ni kommer': 'vous nenez',
        'de (m) kommer': 'ils viennent'}
lecorps= {'kroppen': 'le corps', 'ansiktet': 'le visage', 'h�ret': 'les cheveux', 'ett �ga': 'un oeil', '�gonen': 'les yeux', '�rat': "l'oreille",
           'n�san': 'le nez', 'l�pparna': 'la bouche', 'nacken': 'le cou', 'halsen': 'la gorge', 'armen' :'le bras', 'handen': 'le main', 'benet': 'la jambe',
           'foten': 'le pied', 'kn�t': 'le genou', 'kn�na': 'les genoux', 'rumpan': 'les fesses', 'magen': 'le ventre', 'ryggen': 'le dos', 'br�stet': 'la poitrine',
           'axeln': "l'�paule", 'sk�gget': 'la barbe', 't�nderna':  'les dents',  'huvudet': 'la t�te', 'mustachen': 'la moustache', 'flintskallig': 'chauve',
           'h�stsvans': 'une queue de cheval' , 'ginger': 'roux', 'kort h�r': 'cheveux courts'}
police= {'en bostad, en hemort': 'un domicile', 'vad �r det/ vads t�r p�': "qu'est-ce qu'il y a", 'h�ra': 'entendre', 'ett ljud,ett oljud': 'un bruit',
         'komma ut/g� ut': 'sortir', 'guldsmadjeaff�ren': 'la bijouterie', 'ett smycke': 'un bijou', 'han springer': 'il court', 'mot': 'vers', 'som': 'qui', 'vid ratten': 'au volant',
         'ge sig av': "s'en aller", 'hurdan var han': 'il �tait comment', 'typ, form': 'style', 'han hade p� sig': 'il portait', 'en klack': 'un talon', 'med klackar': '� talons',
         'h�g': 'haut', 'hela tiden': 'tout le temps', 'skriva (en rapport': 'r�diger', 'en efterlysning': 'un avis de recherche', 's�ker': 's�r',
         'en beskrivning': 'une description', 'exakt': 'pr�cis', 'en konstn�r': 'un artiste-peintre', "jag �r van": "j'ai l'habitude", '(h�r) noga': 'bien',
         'folket': 'les gens'}
jeter= {'att kasta': 'jeter', 'jag kastar': 'je jette', 'du kastar': 'tu jettes', 'han kastar': 'il jette', 'vi kastar': 'nous jetons', 'ni kastar': 'vous jetez', 'de kastar(m)': 'ils jettent'}
vouloir= {'vilja': 'vouloir', 'jag vill': 'je veux', 'du vill': 'tu veux', 'han vill': 'il veut', 'vi vill': 'nous voulons', 'ni vill': 'vous voulez', 'de(m) vill': 'ils veulent',
          'kunna': 'pouvoir', 'jag kan': 'je peux', 'du kan': 'tu peux', 'han kan': 'il peut', 'vi kan': 'nous pouvons', 'ni kan': 'vous pouvez', 'de(m) kan': 'ils peuvent'}
comparatif= {'l�ngre �n': 'plus grand que', 'kortare �n': 'moins grand que', 'lika l�ng': 'aussi grand que',
             'l�ngst (m)': 'le plus grand', 'l�mgst(f)': 'la plus grande',  'dyraste(f)': 'la plus ch�re', 'dyrast(m)': 'le plus cher'}
savoir= {'kunna, veta': 'savoir', 'kan ni/ vet ni hur man': 'savez-vous', 'jag kan/vet': 'je sais', 'du an/vet': 'tu sais',
         'han kan/vet': 'il sait', 'vi kan/vet': 'nous savons', 'ni kan/vet': 'vous savez', 'de (m) kan/vet': 'ils savent', 'pass� compos� savvoir': "su",
         'jag kunde': "j'ai su", 'imperfekt jag savoir': 'je savais' , 'futurum jag savoir': 'je saurai'} 
#Passe compose: Generally speaking, the pass� compos� corresponds to the English simple past (did, worked, went �).
#It talks about completed, sequential or one-time actions that took place on a specific occasion.
#Passe compose �r perfekt (har gjort) och ibland imperfekt (gjorde) 
#imparfait: is similar to the English past progressive (was doing, were working �) or the structures used to and would.
#It sets the scene, gives background description and expresses past actions that were repeated over time.
#Imperfekt  
etreimparf= {'jag var': "j'�tais", 'du  var': 'tu �tais', 'han var': 'il �tait', 'vi var': 'nous �tions', 'ni var': 'vous �tiez',
             'de var (m)': 'ils �taient', 'passe compose �tre': '�t�', 'jag strosade': 'je me baladais',
             'jag hade lust': "j'avais envie", 'det r�ckte': 'il suffisait'}
#nedanst�ende s�tts ihop med avoir f�r att bilda  pass� compos�, typ j'ai compris
passecomposeverb= {'arresterad': 'interpell�', 'stulen': 'd�rob�', 'tagen': 'pris', 'uppt�ckt': 'd�couvert', 'var v�pnad': 'arm�', 'skickade': 'envoy�',
                   'was hospitalised' : 'hospitalis�', 'was hurt':'bless�', 'returned': 'rendu', 'flew':'vol�', 'knew': 'connu', 'l�mnade �ver': 'remis',
                   'var tvungen': 'd�', 'domiciled' :'domicili�', 'la': 'plac�', 'hittade': 'trouv�', 'brutit': 'cass�',
                   'f�rst�tt': 'compris', 'ringde': 't�l�phon�', 'reserveratt': 'r�serv�', 'jobbade': 'travaill�', 'slutat': 'fini', 's�lt': 'vendu'}
#verb som slutar p� er blir oftast � i pass� compos�
#verb som slutar p� ir blir oftast i pass� compos�
#verb som slutar p� re blir otast u pass� compos�
#Infiitiv = verbets grundform

# Kapitel 6
enforme= {'i form': 'en forme', 'inget s�rskilt': 'rien de sp�cial', 'en artikel': 'un article', 'mannen': "l'homme", 'sakna n�got': 'manquer de quelque chose',
          'motion': 'exercice', 'missbruka': 'abuser de', 'h�lsan': 'la sant�', 'lida': 'souffrir', 'en sjukdom': 'une maladie', 'civilisationen': 'la civilisation',
          'v�lf�rdssjukdom': 'les malades de civilisation', 'leda/ f�ra': 'mener', 'leva ett liv': 'mener une vie', '�verdriva': 'exag�rer',
          'trivas bra med sig sj�lv': '�tre bien dans sa peau', 'n�jd': 'satisfait', 'inget/ ingen som helst': 'aucun', 'vad som helst': "n'importe quoi",
          'ha br�ttom': '�tre press�', 'r�ka': 'fumer', 'hosta': 'tousser', 'oavbrutet': 'sans arr�t', 'zappa': 'zapper', 'simma': 'faire de la natation',
          'jag har k�pt': "j'ai achet�", 'jag m�ste': 'je dois', 'kila, sticka': 'filer', 'pj d�, det var v�rst': 'c,a alors', 'k�k/ mat': 'de la bouffe', 'l�tt/light': 'l�ger',
          'f�rmoda/anta': 'supposer', 'sluta!': 'arr�te', '�ka ut en sv�ng': 'faire un tour', 'd�refter/sedan': 'puis', 'lika ... som': 'aussi ... que',
          'i riskzonen': '� risque', 'b�ttre f�rekomma �n f�rekommas': 'mieux vaut ppr�venir que gu�rir', 'du g�r mig p� nerverna': "tu m'�nerves", 'herr��': 'ciao'}
extra= {}
grandnord= {'ett �ventyr': 'une aventure', 'l�ngt uppe i norr': 'dans le grand nord', 'ber�tta': 'raconter', 'f�rs�ka': 'essayer', 'jas�?': 'ah bon', 'var d�?': 'ou c,a',
            'fira': 'f�ter', 'j�tte liten': 'tout petit', 'en by': 'un village', 'lyckas': 'r�ussir', 'i alla fall': 'quand m�me', 'l�ra sig': 'apprendre',
            'det �r inte sj�lvklart': "c'est pas �vident", 'skratta': 'rigoler', 'n�sta �r': "l'ann�e prochaine", 'vi skulle vilja': 'on voudrait', 'stormf�rtjust i': 'passionn� de',
            'ett estetiskt program': 'une fili�re artistique', 'det f�rv�nar mig': "c,a m'�tonne", 'ett antal': 'un nombre', 'ett individuellt val': 'une option',
            'roa sig': "s'amuser", 'mer eller mindre': 'plus ou moins', 'en biljett': 'un billet', 'dyrare �n (m pl) ': 'plus chers que', 'studentrabatt': 'tarif �tudiant',
            'tr�ffa kompisar': 'se retrouver entre amis', 'n�gon': "quelqu'un", 'en f�rfest': 'une pr�-f�te', 'innan man g�r': "avant d'aller", 'ett disco': 'une discoth�que',
            'i centrum': 'au centre-ville', 'landet(inte pays)': 'la campagne', 'l�gga m�rke till': 'remarquer', 'en bar med ett litet dansgolv': 'un bar dansant',
            'f�r �vrigt': "d'ailleurs", 'ragga': 'draguer', 'det �r f�rre som' : 'il y en a moins qui', 'snus': 'du tabac � chiquer', 'konstigt': 'bizarre'}
isomras= {'i l�rdags': 'samedi', 'ig�r': 'hier', 'i f�rrig�r': 'avant-hier', 'i somras': 'cet �t�', 'i h�stas': 'cet automne', 'i vintras': 'cet hiver', 'i v�ras': 'ce printemps',
          'i f�rra veckan': 'la semaine derni�re', 'f�r en vecka sedan': 'il y a une semaine', 'f�r ett �r sedan': 'il y a un an', 'f�r en m�nad sen': 'il y a un mois'}
voiretsoir= {'se': 'voir', 'jag ser': 'je vois', 'du ser': 'tu vois', 'han ser': 'il voit', 'vi ser': 'nous voyons', 'ni ser': 'vous voyez', 'de(m) ser': 'ils voient',
             'g� ut/ ta fram/ ta ut': 'sortir', 'jag g�r ut': 'je sors', 'du g�r ut': 'tu sors', 'han g�r ut': 'il sort', 'vi g�t ut': 'nous sortons', 'ni g�r ut': 'vous sortez',
             'de(m) g�r ut': 'ils sortent', 'f�rutse': 'pr�voir', 'tr�ffas': 'se voir', '�terseende': 'revoir', 'en utg�ng': 'une sortie',
             'sortir passe comps�, jag har g�tt ut': 'je suis sorti'}
#voir anv�nds ocks� som bes�ka/h�lsa p�.
fritid= {'l�ngdskid�kning': 'faire du ski de fond', 'g� och fiska': 'aller � la p�che', 'designa': 'dessiner', 'kl�ttra': "faire de l'escalade", '�ka skridskor': 'faire du patinage',
         'vandra': 'faire de la randonn�e', 'dyka': 'faire de la plong�e', 'spela kort': 'jouer aux cartes', 'g�ra hantverk/bygga': 'faire du bricolage',
         'sjunga': 'chanter', 'simma': 'faire de la natation', 'spela ishockey': 'faire du hockey sur glace', 'spela fotboll': 'jouer au football', 'jogga': 'faire du jogging',
         'shoppa': 'faire les magasins', 'tj�na pengar': "faire de l'argent", 'skaffa barn': 'faire des enfents' }
extrakap6= {'har ni sportat lite': 'avez-vous fait un peu de sport', 'det �r det minsta man kan s�ga!': 'et comment', 'h�romdagen': "l'autre jour",
            'jag l�g': "j'�tais allong�", 'h�ll p� att': 'en train', 'gled ur h�nderna p� mig': "m'a �chapp� des mains", 'i st�llet f�r att': 'au lieu de',
            'jag b�jde mig ner': 'je me suis baiss�', 'jag plockade upp': "j'ai ramass�", 'hemsk': 'terrible', 'ensamheten' : 'la solitude', 'depressionen': 'la d�pression',
            'stressen': 'le stress', 'en deckare': 'un roman policier', 'sp�nning': 'suspence'}
preps= {'� + le': 'au', '� + la': '� la',"� + l'": "� l'",  '� + les': 'aux', 'de + le': 'du', 'de la': 'de la', "de + l'": "de l'", 'de + les': 'des'}
    
# Kapitel 7
lalgerie= {'ber�tta': 'raconter', '(han) kom/anl�nde': 'est arriv�', 'besluta/best�mma':  'd�cider', 'l�mna': 'quitter', 'algeriet': "l'Alg�rie", 'en anledning': 'une raison',
           'ekonoiskt': '�conomique', 'han gifte sig': "il s'est mari�", 'en st�dfirma': 'une enterprise de nettoyage', 'vara hemmafru': '�tre femme au foyer',
           'arabiska': 'arabe', 'algerisk(m)': 'alg�rien', 'algerisk(f)': 'alg�rienne' , 'en dryck': 'un boisson', 'vi integreras': "on s'int�gre", 'ett problem': 'un probl�me',
           'samh�llet': 'la soci�t�', 'fr�mlingsfientligheten': 'la x�nophobie', 'levnadsstandard': 'le niveau de vie', 'h�g': '�lev�', 's�kert/naturligtvis': 'certainement',
           'som jag saknar': 'qui me manquent', 'de flesta av dem': "la plupart d'entre eux", '(h�r) n�r det g�ller': 'question', 'b�ttre': 'mieux',
           'vart annat �r': 'tous les deux ans', '(h�r) eftersom': 'comme', 'stor/tal rik m + f': 'nombreux nombreuse', 'en resa': 'un voyage', 's� mycket': 'tellement',
           'jag har rest': 'je suis all�', 'en morbror/farbror': 'un oncle', 'ett utbyte mellan skolor': 'un �change scolaire', 'en religion': 'une religion',
           'det viktigaste': 'le chose la plus importante', 'muslim(m)': 'musulman', 'en tro': 'une croyance', 'f�rlorad(m)': 'perdu', 'anklaga': 'reprocher',
           'han dog': 'il est mort'}
enalgerie= {'slutligen/tillslut': 'enfin', 'ett projekt om': 'un project sur', 'nyss (just) ha ...(+inf)': 'venir de ...', 'tillbringa': 'passer', 'ta sig tid att': 'prendre le temps de',
            'l�ngdistansl�pning': 'endurance', 'spela tevespel': 'jouer � la console', 'ett tillf�lle': 'une occasion', 'anordna/organisera': 'organiser',
            'en mottagning': 'une r�ception', 'bygga': 'construire', 'ha tr�kigt': "s'ennuyer", 'faktiskt': 'en effet', 'de flesta': 'la plupart',
            '�r inte direkt': "n'est pas tellement", 'prioritet': 'la priorit�', 'vard, jobba': 'bosser', 'ett caf� med tobaksf�rs�ljning': 'un bar tabac',
            'en stil/sort': 'un style', 'i allm�nhet': 'en g�n�ral', 'utanf�r/vid sidan om': 'en dehors de', 'en sl�ja': 'un voile', 'd�remot': 'par contre',
            'en majoritet': 'une majorit�', 'b�ttre': 'meilleur', 'helt enkelt': 'simplement', 'bekymra sig': "s'inqui�ter", 'hoppas': 'esp�rer',
            'medans jag v�ntar': 'en attendant', 'h�lsa till': 'passer le bonjour �' , 'kram': "je t'embrasse", 'en kopia': 'une copie', 'ot�lighet': 'impatience',
            'ett stipendiium': 'une bourse'}
#r�relseverb bildar pass� comops� med hj�pverbet �tre, t.ex aller, venir, arrier, partir, entrer, sortir, rentrer, monter, descendre,
#tomber, na�tre (f�das), mourir (d�) 
passecompaller= {'jag gick/�kte/har g�tt/�kt': 'je suis all�(e)', 'du gick/�kte har g�tt/�kt': 'tu es all�(e)', 'han gick/�kte har g�tt/�kt': 'il est all�',
                 'hon gick/�kte har g�tt/�kt': 'elle est all�e', 'man gick/�kte har g�tt/�kt': 'on est all�', 'vi (m) gick/�kte har g�tt/�kt': 'nous sommes all�s',
                 'vi (f) gick/�kte har g�tt/�kt' : 'nous sommes all�es', 'ni (m sing, f sing) gick/�kte har g�tt/�kt' : 'vous �tes all� all�e',
                 'ni (m pl, f pl) gick/�kte har g�tt/�kt': 'vous �tes all�s all�es', 'de (m) gick/�kte har g�tt/�kt': 'ils sont all�s',
                 'de (s) gick/�kte har g�tt/�kt': 'elles sont all�es', 'han kom': 'il est venu', 'hon kom': 'elle est venue' }
#pass� compos� negation: ne ... pas placeras runt hj�lpverbet avoir eller etre. t.ex ja n'ai pas rigol�
liredire= {'l�sa': 'lire', 'jag l�ser': 'je lis', 'du l�ser': 'tu lis', 'han l�ser': 'il lit', 'vi l�ser': 'nous lisons', 'ni l�ser': 'vous lisez', 'de(m) l�ser': 'ils lisent',
           's�ga': 'dire', 'jag s�ger': 'je dis', 'du s�ger': 'tu dis', 'han s�ger': 'il dit', 'vi s�ger': 'nous disons', 'ni s�ger': 'vous dites',  'de (m) s�ger': 'ils disent',
           'passe comp l�sa, jag har l�st': "j'ai lu", 'passe compose s�ga, jag har sagt': "j'ai dit" ,
           'l�sa om': 'relire', 'v�lja': '�lire', 'v�ljare': '�lecteur', 'f�rbjuda': 'interdire', 'man skulle kunna tro att': "on dirait qu'"}
extrakap7= {'sticka': 'faire du tricot', 'ett krig': 'une guerre', 'bli d�dad': 'est tu�', 'en kyrkog�rd': 'un cimeti�re', 'en fris�r': 'un coiffeur',
            'en kille som raggar p� tjejer': 'dragueur', 'en �ppen spis': 'une chemin�e', 'det �r nog fint': 'c,a doit �tre beau', 'likadant': 'pareil',
            'vi hugger den': 'on le coupe', 'skogel': 'la for�t', 'en figur': 'un personnage', 'den heliga familjen': 'la sainte famille', 'kl� ut sig': 'se d�guiser',
            'enorm': 'copieux', 'en m�ltid': 'un repas', 'hobbyer': 'loisirs', 'jag saknar dig': 'tu me manques', 'de skulle vilja bos�tta sig': 'ils voudraient venir habiter',
            'att tundervisa': 'enseigner', 'handikappade': 'les handicap�s', 'att hantera': 'se d�brouiller', 'utesluten': 'exclu',
            'att kopiera': 'copier', 'imponera p�': 'impressionner', 'spontanitet': 'spontan�it�',
            '�ppen': 'ouverts', 'sn�ll': 'gentils', 'blyg': 'timides', 'ingen �r': "personne n'est", 'fyrkant eller km2' : 'carr�',
            'de (m) var (imperfekt': 'ils �taient', 'den enda som bar': 'les seuls � porter'}
#Ingen bildas av personne + ne vid verbet
mener= {'leda': 'mener', 'jag leder': 'je m�ne', 'du leder': 'tu m�nes', 'han leder': 'il m�ne',
        'vi leder': 'nous menons', 'ni lever': 'vous menez', 'de (m) leder': 'ils m�nent', '�verdriva': 'exag�rer',
        'jag �verdriver': "j'exag�re", 'du �verdriver' : 'tu exag�res', 'han �verdriver': 'il exag�re',
        'vi �verdriver': 'nous exag�rons', 'ni �verdriver': 'vous exag�rez', 'de (m) �verdriver': 'ils exag�rent'}
#aimer, d�tester, adorer, pr�f�rer f�ljs av bes�. form. tex. j'aime les chats, je d�teste le caf�
#att vara f�dd i: n�e en . Tex, je suis n�e en 2000

#Kapitel 1 genial 3
trespeople= {'mycket intresserad av k�ndisar': 'tr�s people', 'skvallerpressen': 'la presse people', 'en fris�r m': 'un coiffeur', 'k�nd': 'c�l�bre',
             'en sk�despelare': 'un acteur', 'en sk�despelerska': 'une actrice', 'en s�ngare': 'un chanteur', 'en s�ngerska': 'une chanteuse', 'f�dd(m)': 'n�',
             'en spelare (m)': 'un joueur', 'ett lag': 'une �quipe', 'j�rn': 'fer', 'en regiss�r': 'un metteur en sc�ne', 'har blivit': 'est devenu', 'kunglig': 'royal'}
kiffer= {'vard. gilla': 'kiffer', 'en grej': 'un truc', 'botten/v�rdel�s(m)': 'nul', 'd�remot': 'par contre', 'reklam': 'la publicit�', 'bara' : 'ne ... rien',
         'ett program': 'une �mission', 'vard. f�nig': 'd�bile', 'dokus�por': 'la t�l� r�alit�', 'jag blir': 'je deviens', 'vard. beroende': 'accro',
         'en tecknad serie': 'un dessin anim�', 'vad spelar det f�r roll?': "qu'importe", 'tillbringa': 'passer', 'hel': 'entier', 'anse/tycka': 'trouver',
         'f�rnedrande': 'humiliant', 'en mening/�sikt': 'un avis', 'och sedan': 'et puis', 'dessutom': 'en plus', 'avbrytas av': '�tre coup� par',
         'en g�ng i timmen': 'une fois par heure', 'd�da': 'tuer', 'framf�r allt/ s�rskillt': 'surtout', 'ett spel/ en lek': 'un jeu', 'missa': 'rater',
         'inte n�gon, inte n�got': 'ne ... aucun', 'annars': 'sinon', 'det v�rsta': 'le pire', 'en idiot': 'un cr�tin', 'det �r illa/alvarligt': "c'est grave",
         'verklig': 'r�el', 'hur som helst/i varje fall': 'de toute fac,on', 'eller lixom': 'ou quoi', 'full av': 'plein de', 'f�rst�ra': 'g�cher',
         'en st�mning': 'une ambiance', 'och s� �r det bra': 'et puis voil�', 'den som': 'celui qui'}
extra31= {'jag struntar i det': "je m'en fous", 'tr�ttsamt': 'fatigant', 'en ton�ring': 'un adolescent', 'oroandee': 'inqui�tant', 'toppen': 'chouette',
          'skvaller': 'les potins', 'en f�rstasidesrubrik': 'une manchette', 'ett jobb': 'un boulot', 'var sn�lla': 'soyez sages', 'p�slagen': 'allum�',
          'utom': 'sauf', 'kommunal musikskola': 'un conservatorie', 'dubbelvikt av skratt': '�croul� de rire', 'simning': 'la natation',
          'friidrott': "l'athl�tisme", 'det luktar': 'c,a sent', 'm�rkeskl�der': 'les v�tements de marque'}
#Tv� former av futurum
# 1: le futur proche
# anv�nder presens av aller som hj�lpverb + infinitiv av verbet
# ex. Je vais rentrer demain
#anv�nds inm n�rliggande, planerad tid, j�mf�rs med engelskans 'be going to'

#2: le futur simple
#infinitiv + �ndelse
# ex. je rentrerai un jour

#Futurum av regelbundna verb:
futursimple= {'jag kommer prata': 'je parlerai', 'du kommer prata': 'tu parleras', 'han kommer prata': 'il parlera', 'vi kommer prata': 'nous parlerons',
              'ni kommer prata': 'vous parlerez', 'de (m) kommer prata': 'ils parleront', 'jag kommer att sluta': 'je finirai', 'du kommer att sluta': 'tu finiras',
              'han kommer att sluta': 'il finira', 'vi kommer att sluta': 'nous finirons', 'ni kommer att sluta': 'vous finirez', 'de (m) kommer att sluta': 'ils finiront',
              'jag kommer att s�lja': 'je vendrai', 'du kommer att s�lja': 'tu vendras', 'han kommer att s�lja': 'il vendra', 'vi kommer att s�lja': 'nous vendrons',
              'ni kommer att s�lja': 'vous vendrez', 'de (m) kommer att s�lja': 'ils venront'}
futursimple2= {'kommer ha -' : 'aur-', 'kommer veta/kunna': 'saur-', 'kommer vilja': 'voudr-', 'kommer komma': 'viendr-', 'kommer vara': 'ser-',
               'kommer kunna': 'devr-', 'kommer ta emot': 'recevr-', 'kommer skriva': '�crir-',
               'kommer att bli': 'deviendr-', 'kommer g�ra': 'fer-', 'kommer kunna': 'pourr-',
               'kommer se': 'verr-', 'kommer ta': 'prendr-', 'kommer g�/�ka': 'ir-',
               'je - ': 'ai', 'tu' : 'as', 'il': 'a', 'nous': 'ons', 'vous': 'ez', 'ils': 'ont', 'kommer beh�va': 'devr-'}
vivredevoir= {'jag lever': 'je vis', 'du lever': 'tu vis', 'han lever': 'il vit', 'vi lever': 'nous vivons', 'ni lever': 'vous vivez', 'de (m) lever': 'ils vivent',
              'jag m�ste/ �r tvungen att': 'je dois', 'du m�ste/ �r tvungen att': 'tu dois', 'han m�ste/ �r tvungen att': 'il doit', 'vi m�ste/ �r tvungna att': 'nous devons',
              'ni m�ste/ �r tvungna att': 'vous devez', 'de (m) m�ste/ �r tvungna att': 'ils doivent', 'leva passe compose, jag har bott': "j'ai v�cu",
              'futurum leva': 'je vivrai', ' m�ste passe compose, jag var tvungen': "j'ai d�", 'futurum beh�va': 'je devrai'}
trestendence= {'n�gra ungdomar g�r ut tsm': 'les sorties en bande', 'lektionerna': 'les cours', 'g�rna': 'volontiers', 'ett bakverk': 'une p�tisserie',
               'en v�ffla': 'une geufre', 'en munk': 'un beignet', 'ett mellanm�l': 'un go�ter', 'vard. typ': 'quoi', 'stanna kvar': 'rester', 'skolmatsalen': 'la cantine',
               'en m�ltid': 'un repas', 'hur dags?': 'vers quelle heure', 'en fest': 'une soir�e', 'f�rst': "d'abord", 'g� hem': 'rentrer', 'l�mna sina grejer': 'poser ses affaires',
               'jo': 'si', '�verkomlig, rimlig': 'abordable', 'sedan': 'ensuite', 'inte s� v�rst': 'pas trop', 'ibland' : 'de temps en temps', 'sedan': 'ensuite',
               'utanf�r': 'en dehors de', 'inneb�ra': 'poser', 'efter att ha druckit' : 'apr�s avoir bu', 'stiga upp': 'se lever', 'h�r. h�mta': 'chercher',
               'i s� fall' : 'alors l�', 'till': "jusqu'�", 'gryningen': 'le petit matin', 'erbjuda': 'offrir', '�ka hem till sig': 'rentrer chez eux', 'ett tidsf�rdriv': 'un passe-temps',
               'egentligen' : 'en effet', 'ladda ner': 't�l�charger', 'rabatt(er)' : 'des r�ductions', 'en ton�ring': 'un adolescent'}
passecomp= {'�kt': 'suis all�', 'hafrt': 'eu', 'druckit': 'bu', 'f�rst�tt': 'compris', 'sagt': 'dit', 'skrivit' : '�crit', 'varit': '�t�', 'ggjort': 'fait', 'lagt' : 'mis',
            'gett sig iv�g': 'suis parti', 'kunnat': 'pu', 'tagit': 'pris', 'skrattat': 'ri', 'jobbat': 'travaill�', 'slutat': 'fini', 's�lt': 'vendu', 'levt': 'v�cu', 'var tvungen': 'd�',
            'l�st': 'lu', 'g�tt ut': 'sorti', 'sett': 'vu', 'kommit': 'venu', 'kunnat(kunskap)': 'su', 'l�mnade tillbaka': 'revenu'}

# kap 2 genial 3
lafrancophinie= {'den fransktalande v�rlden': 'la francophonie', 'schweiz': 'la Suisse', 'vansinnigt/f�rbaskat': 'vachement', 'vinna': 'ganger', 'en vistelse' : 'un s�jour',
                 'en t�vling': 'un concours', 'n�jd': 'content', 'l�ngtr�kig': 'ennuyeux', 'en klocka': 'une horlonge', 'en ko': 'une vache', 'i kn�byxor': 'en clouette',
                 'joddlande': 'faisant des tyroliennes', 'n�ja n�v�l': 'enfin', 'hel': 'entier', 'of�rgl�mmelig': 'inoubliable', 'som har l�rt mig': "qui m'ont appris",
                 'ett schema': 'un emploi du temps', 'fyllt, sp�ckat': 'charg�', 'en vinnare' :'un gagnant', 'te med' : 'emmener', 'efter att ha l�mnat v�rt bagage':
                 'apr�s avoir pos� nos bagages', 'en linbana' :'un t�l�ph�rique', 'en vandring': 'une randonn�e', 'ovanf�r': 'au-dessus de',
                 'ett moln': 'un nuage', 'en utsikt' : 'une vue', 'en flod': 'une rivi�re', 'jag sv�r/jag lovar dig': 'je te jure', 'p� v�gen/under resan': 'en route',
                 'till och med' : 'm�me', 'h�ra': 'entendre', 'slut/d�dstr�tt' : 'crev�', 'f� n�gon att tappa andan': 'couper le souffle � qn',
                 'sn�mannen i himalaya': 'le yeti', 'en lavin': 'une avalanche', 'en klyfta': 'une crevasse', 'falla' : 'tomber', 'en rysning': 'un frisson',
                 'pr�va p�/v�ga sig p�': 'tenter', 'ett klot/en kula': 'une boule', 'j�ttej�tte stor/gigantisk': 'g�ant', 'g� ner/�ka ner': 'descendre',
                 'en kulle': 'une colline', 'berg och dahl bana': 'des montagnes russes', 'en favorit': 'un coup de coeur', 'starta/s�tta ig�ng': 'd�marrer',
                 'man m�ste': 'il faut', 'd�r uppe': 'en haut', 'genom att anv�nda': 'en utilisant', 'hoppa': 'sauter', 'dyka': 'plonger', 'en rutschbana': 'un toboggan',
                 'det b�sta': 'le top', 'glida/halka': 'glisser', 'nere': 'en bas', 'en avf�rd': 'un d�part', 'ledsen/sorglig': 'triste',
                 'ingen': 'ne ... personne', 'ett verktyg': 'un outil', 'ett armbandsur': 'une montre'}
parleunpeu= {'sp�nnande': 'passionnant', 'j�tteh�ftigt': 'trop cool', 'underbart/toppen': 'sensass', 'livsfarligt' : 'mortel', 'f�rskr�ckligt/f�rf�rligt': 'affreux',
             'skr�mmande/hemskt': 'effrayant', 'anstr�ngande/p�frestande': '�puisant', 'uttr�ttande': 'fatigant', 'kolla/ta reda p�': 'se renseigner',
             'ett h�rn': 'un coin', 'ett st�lle' : 'un endroit', 'en �lg': 'un �lan', 'ett utest�lle': 'une sortie', 'en secondhandbutik' : "un magasin d'occasion",
             'skicklighet': 'savoir-faire', 'vissla': 'siffler', '�ka vattenskidor': 'faire du ski nautique', 'k�ra': 'conduire' }
connaitsavoir= {'k�nna/k�nna till': 'conna�tre', 'jag k�nner': 'je connais', 'du k�nner': 'tu connais', 'han k�nner': 'il conna�t',
                'vi k�nner': 'nous connaissons', 'ni k�nner': 'vous connaissez', 'de (m) k�nner': 'ils connaissent' , 'pass� compos� conna�tre': "j'ai connu", 'futrum conna�tre': 'je conna�trai',
                'kunna/veta': 'savoir', 'jag vet': 'je sais', 'du vet': 'tu sais', 'han vet': 'il sait', 'vi vet' : 'nous savons', 'ni vet' : 'vous savez', 'de (m) vet': 'ils savent',
                'pass� compos� savoir': "j'ai su", 'futurum savoir': 'je saurai', 'k�nna varandra': 'se conna�tre'}
idiotjesuis= {'�ka igenom/via': 'passer par', 'p� tillbakav�gen': 'au retour', 'praktik/en kurs': 'un stage', 'lyckas med': 'r�ussie �' ,
              'jag skulle vilja': "j'amerais", 'skulle ni kunna': 'pourriez-vous', 'l�tt': 'facile', 'l�ngt ifr�n': 'loin de', 'man m�ste': 'il faut',
              'varje': 'chaque', 'ett kvarter/ stadsdel': 'un quartier', 'ett turistkort/ turistbiljett': 'une carte touristique',
              'g�lla': '�tre valable', 'toppen': 'chouette', 'dr�m': 'r�ve', 'helt ensam': 'tout seul', 'bara': 'ne ... que', 'g�ra n�gon s�llskap/ f�lja med': 'accompagner qn',
              'inte mycket': 'pas grand-chose', 'verka, se ut': "avoir l'air", 'sedan f�dsel': 'de naissance', 'montrealbo': 'Montr�alais', 'till din tj�nst': '� ton service',
              'en massa': 'des tas de', 'f�rmodligen': 'probablement', 'minst/�tminstone': 'au moins', 'l�t oss g�' : 'on y va', 'ett torn': 'une tour',
              'verkligen': 'vraiment', 'imponerande': 'impressionnant', 'otrolig': 'incroyable', 'avsluta': 'terminer', 'olympiska spelen': 'Les Jeux Olympiques',
              'det betyder' : 'c,a veut dire', 'ingen kunde se det': "personne n'a pu la voir" , 'antagligen/ nog': 'sans doute', 'det menar du inte!' : 'sans blague',
              'en hamn': 'un port', 'i allafall': 'quand m�me', 'som r�knas': 'qui compte', 'dum': 'b�te', 'missa': 'rater', 'lugna dig': 'calme-toi',
              'en teaterpj�s': 'une pi�ce de th��tre', 'pommes frites': 'des frites', 'en typ BBQ s�s': 'une sauce style BBQ'}
extra32= {'sk�mt': 'farce', 'ren': 'caribou', 'r�dluvan': 'le petit Chaperon rouge', 'en stj�rna': 'une �toile', 'ett slott': 'un ch�teau', 'likna': 'ressembler',
          'f�re detta': 'ancien', 'en glasbl�sare': 'un souffleur de verre', 'ett glasbruk': 'une verrerie', 'en glasfabrik' : 'une usine de verre',
          'moderlandet (frankrike)': 'm�tropole', 'blandspr�k': 'cr�ole', 'br�dskande': 'urgent', 'bli sjuk': 'tomber malade', 'jag saknar det': 'c,a me manque',
          'klara sig (sj�lv)' : 'de d�brouiller', 'uppt�cka': 'd�couvrir', 'en gummib�t' : 'un zodiac', 'ett mangrovetr�sk': 'un pal�tuvier',
          'k�ra': 'piloter', 'avkoppling' : 'd�tente', 'k�rkort': 'permis', 'j�tte-': 'g�ant', 'sand': 'sable', 'att �ka upp f�r en flod': "une remont�e d'une rivi�re",
          'en bj�rn': 'un ours'}

# Kapitel 3
pyrenees= { 'tack vare': 'gr�ce �', 'ett stipendium' : 'une bourse', 'hon skriver': 'elle �crit', 'f�re detta': 'ancien', 'en liten h�lsning': 'un petit mot',
            "jag l�r mig": "j'apprends", 'en sak': 'une chose', 'i b�rjan': 'au d�but', 'det var': "c'�tait", 'f�rst�' : 'comprendre', 'vara bel�gen' : '�tre situ�',
            'det h�nder att': 'il arrive que', 'f�rs�ka': 'essayer', 'kl�ttra': 'grimper', 'en v�gg': 'un mur', 'en skolvakt': 'un surveillant',
            'en ringsignal': 'une sonnerie', 'en sovsal': 'un dortoir', 'g�ra upprop': "faire l'appel", 'en rast': 'une r�cr�ation', 'b�rja om': 'recommencer',
            'jobbig/sv�r': 'dur', 'en energikaka': 'une barre de c�r�ales', 'mer eller mindre': 'plus ou moins', 'en l�xa': 'un devoir', 'l�gga sig': 'se coucher',
            'f�ra ov�sen': 'faire du bruit', 'fritid': 'les loisirs', 'p� nedrev�ningen': 'en bas', 'allts�': 'donc', 'sportig': 'sportif', 'flera, m�nga': 'plusieurs',
            'l�ngdskid�kning': 'le ski du fond', 'de var': 'ils �taient', 'en v�rdfamilj' : "une famille d'accueil", 'ofta': 'souvent', 'en anteckning': 'une note',
            'anteckna': 'prendre des notes', 'd�r': 'l�', 'ett �mne': 'une mati�re', 'inte alls': 'pas du tout', 'en tanke': 'une pens�e', 'toaletten': 'les toilettes',
            'komma f�rsent': '�tre en retard', 'skriven': '�crit', 'alla helgons dag': 'la Toussaint', 'h�lsa p�': 'voir', 'utg�ra en del av': 'faire partie de',
            'roa sig': "s'amuser", '(ung.) kram': 'je vous embrasse', 'en ledare m': 'un moniteur', 'en ledare f': 'une monitrice', 'f�rv�na sig': "s'�tonner",
            'hos': 'aupr�s de', 'som tar emot': 'accueilllant', 'gruppera': 'grouper', 'p� ett avst�nd av': '�loign� de', 'ett trettiotal': 'une trentaine de',
            'de kommer att ha l�rt sig': 'ils auront appris'}
extra33= {'en latmask': 'un cancre', 'f�rh�ra': 'questionner', 'sudda ut': 'effacer', 'en snara/f�lla': 'un pi�ge', 'ett hot': 'une menace', 'l�raren': 'le ma�tre',
          'en utvisslling/ burop': 'une hu�e', 'ett underbarn': 'un enfant prodige', 'en krita' : 'une craie', 'olycka': 'malheur', 'utantill': 'par coeur',
          'underteckna ett intyg om fr�nvaro': "signer un mot d'absence", 'en kamp': 'un combat', 'brasiliansk': 'br�silien', 'det tar bort stressen/ det lugnar mig':
          'c,a me d�stresse', 'ta studenten': 'r�ussir son bac', 'en dagbok': 'un journal intime', 't�rnrosa': 'la belle au bois dormant', 'st�ende': 'debout',
          'sova utomhus': 'dormir � la belle �toile', 'sova som en stock': 'dormir comme un loir', 'l�ng rund stenh�rd kudde': 'un traversin',
          'ha sovmorgon': 'faire la grasse matin�e', '�lskling': 'ch�ri', 'korrekt kl�dsel': 'la tenue correcte', 'urringad': 'd�collet�e'}
faisgaffe= {'akta/ se upp': 'fais gaffe', 'k�ra': 'conduire', 'vid ratten': 'au volant', 'starta': 'd�marrer', 'en g�ng': 'une fois', 'f� motorstopp': 'caler',
            'efter, i slutet av': 'au bout de', 'v�xla': 'changer de vitesse', 'hastigheten/farten':  'la vitesse', 'n�gra': 'quelques', 'en dumhet/tokighet': 'une b�tise',
            'f�rbli': 'rester', 'fungera': 'marcher', 'en hj�rtattack': 'une crise cardiaque', 'en broms': 'un frein', 'en sten': 'une pierre' ,'sl� emot/ kollidera med ngt':
            'heurter', 'ett d�ck': 'un pneu', 'insistera p� att': 'insister pour', 'l�ta': 'laisser', 'bromsa': 'freiner', 'h�ftigt': 'brusquement', 'sl�(emot)': 'frapper',
            'en vindruta': 'un pare-brise', '�vningsk�rning': 'la conduite accompagn�e', 'vilken tur': 'quelle chance', 'lugnt': 'doucement', 's�ra/skada': 'blesser',
            'backa': 'faire marche arri�re', 'n�r jag gjorde det (eg. g�rande)': 'en le faisant', 'igen': 'de nouveau', 'mitt fel': 'de ma faute', 'skulle kunna': 'pourrait',
            'visa sig': 'se montrer', 'en v�gkorsning': 'un carrefour', 'bli rasande': 'se mettre en col�re', 'p� samma g�ng': 'en m�me temps',
            'runt omkring': 'autour de', 'pl�tsligt': 'soudain', 'h�gerregeln': 'la priorit� � droite', 'kopplingen': 'la embrayage'}
ecriredormir= {'skriva': '�crire', 'jag skriver': "j'�cris", 'du skriver': "tu �cris", 'han skriver': 'il �crit', 'vi skriver': 'nous �crivons', 'ni skriver': 'vous �crivez',
               'de skriver m ': 'ils �crivent', 'sova': 'dormir', 'jag sover': 'je dors', 'du sover': 'tu dors', 'han sover': 'il dort', 'vi sover': 'nous dormons', 'ni sover': 'vous dormez',
               'de sover': 'ils dorment', 'pass� compos� skriva': "j'ai �crit", 'futurum skriva': "j'�crirai", 'pass� compos� sova': "j'ai dormi", 'futurum sova': 'je dormirai'}

#Kapitel 4
portesouverts= {'�ppet hus': 'portes ouvertes', 'mycket n�ra': '� deux pas', 'inom r�ckh�ll': '� port�e de main', 'en aff�r': 'un commerce',
                'en k�ttaff�r': 'une boucherie', 'en blomsterhandlare': 'un fleuriste', 'f�rsk m': 'frais', 'f�rsk f': 'fra�che', 'en alags bulle med b�rlsocker': 'une choquette',
                'en doft/lukt': 'une odeur', '�verallt': 'partout', 'handla': 'faire les courses', 'varje l�rdagsmorgon': 'tous les samedis matins',
                'ett salutorg': 'un march�', 'vi tar fram': 'on sort', 'en shoppingvagn': 'un caddie', 'en restaurang/brasseri/cafe': 'une brasserie', 'en krog': 'un bistro',
                'en lindansare': 'un funambule', 'ha lust att': 'avoir envie de', 'eller ocks�': 'ou bien', 'g� ut o g�': 'se balader', 'tr�ffa' : 'rencontrer', 'nedanf�r': 'en bas de',
                'en fastighet': 'un immeuble', 'ett centrum': 'un foyer', 'nordafrikansk': 'maghr�bin', 'sjunde': 'septi�me', 'en v�ning': 'un �tage', 'en hiss': 'un ascenseur',
                'st�da': 'faire le m�nage', 'en bostad med subventionerad hyra': 'une HLM', 'f�r, ty': 'car', 'en hyra': 'un loyer', 'l�g m f': 'bas basse', 'olyckligtvis':
                'malheureusement', 'ta emot': 'recevoir', 'h�lsa p� n�gon': "venir voir quelq'un", 'f�r det mesta': 'la plupart du temps', 'en b�ddsoffa': 'un canap� clic-clac',
                'ett skrivbord': 'un bureau', 'i alla fall': 'quand m�me' ,'utrustad': 'equip�', 'en tv�ttmaskin': 'un lave-linge s�chant', 'en diskmaskin': 'un lave-vaisselle',
                'sl� sig ned': "s'installer", 'lugn': 'tranquille'}
extra34= {'ungdomsg�rden': 'la masion des jeunes', 'utnyttja': 'profiter de', 'vara pensionerad' : '�tre � la retraite', 'adlig': 'noble', 'oumb�rlig': 'indispensable',
          'v�rmeb�lja': 'canicule', 'flytta': 'd�m�nager', 'ett radhus': 'une maison mitoyenne', 'trafik': 'circulation', 'man lever': 'on vit', 'ett kulturevenemang':
          'un �v�nement culturel', 'en f�rstad med h�ghusomr�den': 'une cit�', 's� snart som m�jligt': 'd�s que possible', 'bli irriterad': "s'�nerver",
          'n�jen': 'distractions', 'en etta': 'un studio', 'jag g�r/ k�r vilse': 'je me perds', 'ett trappsteg': 'une marche', 'ett palats': 'un palais', 'en skomakare':
          'un cordonnier', 'som hon f�redrog': 'qui eut sa pr�f�rence', 's�tta p� skor': 'chausser', 'friade': 'fit sa demande', 'vi skulle sova': 'nous dormirions',
          'en dubbels�ng': 'un grand lit', 't�ckt': 'couvert', 'en p�rla': 'une perle', 'vintergr�na': 'pervenche', 'mitten': 'le mitant', 'skulle kunna': 'pourraient' ,
          'tankspridd': '�tourdi', 'vifta p� svansen': 'remuer la queue'}
rire= {'skratta': 'rire', 'jag skrattar': 'je ris', 'du skrattar': 'tu ris', 'han skrattar': 'il rit', 'vi skratar': 'nous rions', 'ni skrattar': 'vous riez', 'de m skrattar': 'ils rient',
       'pass� compos� skratta': "j'ai ri", 'futurum skratta': 'je rirai'}
sdf= {'g� utf�r/ ramla utf�r': 'd�gringoler', '�r jag' : 'me voici', 'tigga': 'faire la manche', 'hj�rtlig': 'cordial', 'bland dem': 'parmi elles', 'm�nniskor/folk': 'des gens',
      'en egenskap': 'une qualit�', 'idiotisk': 'con', 'spotta': 'cracher', 'ansiktet': 'la figure', 'komma �ver/besegra': 'surmonter', 'olycka': 'malheur', 'jag hade': "j'avais",
      'allt som beh�vs': "tout ce qu'il faut", 'jag arbetade': 'je travaillais', 'ett tryckeri': 'une imprimerie', 'f�r ... sedan' : 'il y a', 'avskeda': 'licencier', 'jag f�rlorade':
      "j'ai perdu", 'l�mna': 'quitter', 'k�ra ut': 'foutre � la porte', 'n�ja': 'bon, ben', 'erk�nna': 'reconna�tre', 'begr�nsa sig': 'se limiter', 'bli berusad': "s'enivrer",
      'hejda sig/stanna': "s'arr�ter", 'dricka sig full': 'se so�ler', 'en heml�s': 'un sans domicile fixe', 'se m�rkt p�': 'voir mal', 'd�lig': 'mauvais',
      'ett h�l': 'un trou', 'ingen': 'ne ... personne', 'hj�lpa': 'aider', 'ta med sig': 'apporter', 'det viktigaste': 'le principal', 'till�ta': 'permettre', 'moralen': 'le moral',
      'h�lla modet uppe': 'garder le moral'}
croire= {'tro': 'croire', 'jag tror': 'je crois', 'du tror': 'tu crois', 'han tror': 'il croit', 'vi tror': 'nous croyons', 'ni tror': 'vous croyez', 'de m tror': 'ils croient',
         'pass� compos� tro': "j'ai cru", 'futurum tro': 'je crorai'}

# Kap 5

congo= {'ett inb�rdeskrig': 'une guerre civile', 'd�d': 'mort', 'freden': 'la paix', 'ett h�rn': 'un coin', 'lidit': 'souffert', 'ett krig': 'une guerre', 'tegel': 'brique',
        'h�lsa v�lkommen': 'souhaiter la bienvenue', 'sk�lla': 'aboyer', 'sj�lvklar': '�vident', 'f�r�ldral�s': 'orphelin', 'en j�gare': 'un chasseur',
        'ett samvete' : 'une conscience', 'en h�na': 'une poule', 'en deg': 'une p�te' , 'ett blad': 'une feuille', 'kandidat': 'licenci�', 'juridik': 'le droit',
        'ta hand om': "s'occuper de", 'arbetsl�shet': 'ch�mage', 'f�rlorade': 'a perdu', 'en strid': 'une lutte', 'rinnande vatten': "l'eau courante",
        'torr x2': 'sec s�che', 'en skugga': 'une ombre', 'v�gkanten': 'le bord de la route', 'fr�n v�gkanten': 'du bord de la route', 'en tr�ff': 'un rendez-vous',
        'en blus': 'un chemisier', 'f�rtj�na': 'm�riter', 'j�ttetrevlig/j�ttesn�ll': 'gentil, le comme tout', 'nyss ha gjort n�got': 'venir de faire quelque chose',
        'ha br�ttom': '�tre press�', 'sopa': 'balayer', 'diska': 'faire la vaiselle', 'vila sig': 'se reposer' , 'tacksam': 'reconnaissant', 'jag skulle kunna': 'je pourrais',
        'skicka/s�nda' : 'envoyer', 'en hj�ltinna': 'une h�ro�ne', 'h�r: g�ra': 'rendre', 'ensamhet': 'solitude'}
extra35= {'tr�skeln': 'le pas de la porte', 'godmodighet': 'bonhomie', 'blomstrande/framg�ngsrik': 'prosp�re', 'sv�va': 'flotter', 'sjuda': 'mijoter',
          'flyta f�rbi': "s'�couler", 'f�rflyta': 'se d�rouler', 'sj�len f': "l'�me" , 'en tr�skomakare': 'un sabotier', 'en d�dgr�vare': 'un fossoyeur', 'tofflor': 'des pantoufles',
          'cider': 'du cidre', 'ett kar': 'un tonneau', 'en press': 'un pressoir', 'en kille': 'un mec', 'v�nda sig mot': 'se tourner vers', 'klara sig' : 'se d�brouiller',
          'ett drag': 'un jeu', 'r�ra p�/ vifta p�': 'remuer', 'svansen': 'la queue', 'sn�ll, lydi': 'sage'}
        #verb med Ackusativ : �couter qn/qc, regarder qn/qc
          #verb med dativ: �crire � qn, parler � qn
          #de npersonen man g�r n�got till kallas dativobjekt . Ist�llet f�r preposition + substantiv kan man anv�nda ett pronomen .
          #Obs! man f�r inte ha n�gon preposition (till, f�r, �t) n�r man anv�nder sig av ett dativobjekt. Prepositionerna �r redan inbakade i me, te, lui, nous, vous, leur.
voir= {'se': 'voir', 'jag ser': 'je vois', 'du ser': 'tu vois', 'han ser': 'il voit', 'vi ser': 'nous voyons', 'ni ser': 'vous voyez', 'de m ser': 'ils voient', 'pass� compose se':
       "j'ai vu", 'futurum se': 'je verrai', 'f�, erh�lla': 'recevoir', 'jag f�r': 'je rec,ois', 'du f�r': 'tu rec,ois', 'han f�r': 'il rec,oit', 'vi f�r': 'nous recevons', 'ni f�r': 'vous recevez',
       'de m f�r': 'ils rec,oivent', 'pass� compos� f�/erh�lla': "j'ai rec,u", 'guturum f� erh�lla': 'je recevrai'}
barry= {'det var en g�ng': 'il etait une fois', 'en saga': 'un conte de f�es', 'ett kloster': 'un monast�re', 'ett bergspass': 'un col', 'en gr�ns': 'une fronti�re',
        'inneh�lla': 'contenir', 'en handling': 'un acte', 'en r�ddning': 'un sauvetage', 'genom': '� travers', 'sn�n': 'la neige', 'dimman' : 'le brouillard', 'r�dda': 'sauver',
        'mer �n': 'plus de', 'd�den': 'la mort', 'ana/ k�nna p� sig': 'pressentir', 'snabbt': 'vite', 'ett st�lle': 'un endroit', '(p�) hj�lp': 'au secours', 'den': 'celle',
        'befinna sig' :'se trouver', 'en spricka': 'une crevasse', '�teruppliva': 'ranimer', 'genom att slicka': 'en l�chant', 'ett ansikte': 'un visage', 'resa sig upp igen':
        'se relever', 'kylan': 'le froid', 'ett ben': 'une jambe', 'g�/promenera': 'marcher', 'r�ra sig': 'bouger', 'l�gga sig': 'se coucher', 'bredvid' : '� c�te de',
        'en rygg': 'un dos', 'helskinnad': 'sain et sauf', 'en kropp': 'un corps', 'stoppa upp djur': 'naturaliser', 'resa (ett monument/minnesm�rke)': '�riger'}
# Imperfekt: Beskrivande, m�lande tempus, Tilllst�nd
    # Anv�nder stammen plus �ndelser -ais -ais -ait -ions -iez -aient
# Pass� compos�: Actiontempus, h�ndelser
    #an�nder hj�lpverb avoir eller �tre

# Kapitel 6
labouffe= {'vard. mat': 'bouffe', 'ett stipendium': 'une bourse', '�verlycklig, f�rtjust': 'ravi', 'skaffa sig upplysningar, h�ra f�r': 'se reneigner', 'ett s�tt': 'une fac,on',
           'ett varuhus': 'un grand magasin', 'smaka p�/ avssmaka': 'd�gusster', 'ber�md': 'fameux','k�tt': 'viande', 'k�ttbullar': 'les boulette de viande',
           'ett lingon': 'une airelle', 'byta ut': 'remplacer', 'kokt potatis': 'pommes de terre vapeur', 'avdelning': 'un rayon', 'mat': 'alimentation', 'gillar du det':
           'c,a te dit', 'g�rna': 'avec plaisir', 'inlagd sill': 'hareng marin�', 'dill': 'aneth', 'med dill': "� l'aneth", 'som huvudr�tt': 'en plat principal', 'en �lg': 'un �lan',
           'pyttipanna': 'une po�l�e su�doise', 'inte jag heller': 'moi non plus', 'verka/se ut': "avoir l'air", 'kaviar': 'des oeufs de poison', 'en sm�rg�s': 'une tartine',
           'inte s� mycket': 'pas grand chose', 'en skiva': 'une tranche', 'snarare, hellre': 'plut�t', 'enligt min �sikt': '� mon avis', 'de �r inte s� mycket f�r desserter':
           "ils ne sont pas tr�s dessert", 'en sm�kaka': 'un petit g�teau', 'en kanelbulle': 'une brioche � la cannelle', 'utanf�r': 'en dehors de', 'sm��ta' :'grignoter',
           'r�g': 'seigle', 'en dryck': 'une boisson', 'dum': 'b�te', 'ha r�tt': 'avoir raison', 'surstr�mming': 'hareng ferment�', 'sluta upp': 'arr�ter', 'sk�mta': 'plaisanter'}
extra36= {'stormarknader': 'les grandes surfaces', 'surdeg': 'levain', 'j�sa': 'fermenter', '�nga': 'vapeur', 'knaprig': 'croustillant', 'klok/ f�rst�ndlig': 'raisonnable',
          'en botad': 'un logement' ,'dela': 'partager', 'en korridor': 'un couloir', 'vid slutet av': 'au bout de', 'en elplatta': 'un r�chaud �lectrique',
          'skynda ssig': 'se d�p�cher', 'en lukt/doft': 'une odeur', 'm� illa': 'avoir mal au coeur', 'du har fel': 'tu as tort', 'en osthandlare': 'un fromager',
          'en ostaff�r': 'une fromagerie', 'trogen': 'fid�le', 'provmaka': 'd�guster', 'ekologiska �gg': 'de oeufs biologiques', 'getost': 'ch�vre'}
repasinoubliable= {'of�rgl�mlig': 'inoubliable', 'en semesterbostad p� landet': 'un g�te', 'hyra': 'louer', '�ka bil': 'se promener en voiture',
                   'medans de lyssnade p�': 'en �coutant', 'en utflykt/ �ktur': 'une balade', 'inse/ fatta/ f�rt�': 'se rendre compte', 'erbjuda': 'proposer',
                   'en t�vling': 'un concours', 'f�rklara': 'expliquer', 'varje g�ng': 'chaque fois', 'fin/ ber�md': 'grand', 'klara sig': 'se d�brouiller',
                   'en bechamels�s': 'une sauce b�chamel', 'komma ih�g': 'se rappeller', 'en matr�tt': 'un plat', 'vara van': "avoir l'habitude", 'g� bra': 'se passer bien',
                   'en s�ndning/ ett program': 'une �mission', 'en kvarn': 'un moulin', 'bel�gen': 'situ�', 'ett landskap': 'un paysage', 'ett vykort': 'une carte postale',
                   'sl� sig ned': "s'installer", 'en flod': 'une rivi�re', 'en provsmakning': 'une d�gustation', 'vattnas i munnen': "avoir l'eau � la bouche",
                   'njuta av': 'savourer', 'medan de nj�t av': 'en savourant', 'en liten aptitretare': 'une amuse-bouche', 'frosseri': 'gourmandise',
                   'en finsmakare': 'un gourmet', 'h�lla sig smal': 'garder la ligne', 'f�r en g�ngs sskull': 'pour une fois', 'mitt i': 'au milieu de', 'en sorbet': 'un sorbet',
                   'ett h�l': 'un trou', 'en slags sorbet med alkohol': 'un trou normand', 'en stor�tare/l�ckergom': 'un gourmand', '�ta mycket och g�rna': '�tre tr�s gourmand',
                   'sm�lta (maten)' : 'dig�rer', 'smakade det bra?': 'c,a a �t�', 'njuta/ sm�rja kr�set': 'se r�galer', 'l�gga upp': 'pr�senter', 'till�gga': 'ajouter',
                   'ett konstverk': "une oeuvre d'art"}

                   
ffs= {'knaprig': 'croustillant', 'en bostad': 'un logement', 'sk�mta': 'plaisanter', 'byta ut': 'remplacer', '�verlycklig, f�rtjust': 'ravi', 'skaffa sig upplysningar f�r':
      'se reneigner', 'njuta av': 'savourer', 'medan de nj�t av': 'en savourant', 'ett kloster': 'un monast�re', '�teruppliva': 'ranimer', 'resa (ett monument/minnesm�rke)':
      '�riger', 'en r�ddning ': 'un sauvetage', 'r�dda': 'sauver', 'genom' : '� travers', 'en saga': 'un conte de f�es', 'ana/ k�nna p� sig': 'pressentir',
      'en d�dgr�vare': 'un fossoyeur', 'flyta f�rbi': "s'�couler", 'tr�skeln': 'le pas de la porte', 'en tr�skomakare': 'un sabotier', 'r�ra p�/ vifta p�': 'remuer',
      'f�rflyta': 'se d�rouler', 'sk�lla': 'aboyer', 'en strid': 'une lutte', 'tacksam': 'reconnaissant', 'fr�n v�gkanten': 'du bord de la route', 'f�rtj�na': 'm�riter',
      'bli berusad': "s'enivrer", 'idiotisk': 'con', 'ta med sig': 'apporter', 'ett tryckeri': 'une imprimerie', 'bland dem': 'parmi elles', 'jag hade': "j'avais",
      'g�r/ ramla utf�r': 'd�gringoler'}
ffs2= {'ett kulturevenemang': 'un �v�nement culturel', 'vara pensionerad': '�tre � la retraite', 'en skomakare': 'un cordonnier', 'ett radhus': 'une maison mitoyenne',
       'oumb�rlig': 'indispensable', 'flytta': 'd�m�nager', 'tankspridd': '�tourdi', 'en tv�ttmaskin' : 'un lave-linge s�chant', 'tr�ffa' : 'rencontrer',
       'inom r�ckh�ll': '� port�e de main', 'en lindansare': 'un funambule',
       'runt omkring': 'autour de', 'bli rasande': 'se mettre en col�re', 'kopplingen': 'la embrayage', 'en vindruta': 'un pare-brise', 'visa sig': 'se montrer',
        'igen': 'de nouveau', 'efter, i slutet av': 'au bout de', '�vningsk�rning ': 'la conduite accompagn�e', 'bromsa': 'freiner',
       'en ringsignal': 'une sonnerie', 'de kommer att ha l�rt sig': 'ils auront appris', 'ett �mne': 'une mati�re', 'i b�rjan': 'au d�but',
 'p� avst�nd av': '�loign� de', 'hos': 'aupr�s de', 'ett trettiotal': 'une trentaine de', 'som tar emot': 'accueilllant',
       'att �ka upp f�r en flod': "une remont�e d'une rivi�re", 'en glasfabrik': 'une usine de verre',
        'ett mangrovetr�sk': 'un pal�tuvier', 'ett glasbruk': 'une verrerie', 'moderlandet (frankrike)': 'm�tropole', 'ren': 'caribou'}
       

skippade= glosor(ffs)
