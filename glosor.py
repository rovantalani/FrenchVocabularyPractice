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

sara={'välkommen(m)': 'bienvenu', 'till': 'en', 'Frankrike': 'France', 'anlända': 'arrive', 'på tågstationen': 'à la gare',
      'ursäkta mig': 'excusez-moi', 'det är': "c'est", 'ni är': 'vous êtes', 'från sverige': 'de Suède', 'jag är': 'je suis',
      'trevligt att träffas(m)': 'enchanté', 'inte så': 'pas trop', 'trött(m)': 'fatigué', 'lite grann': 'un peu', 'men': 'mais',
      'ert bagage(m pl)': 'vous bagages', 'här är': 'voici', 'min ryggsäck': 'mon sac à dos', 'då(så)': 'alors', 'då går vi': 'on y va'}
Lebau= {'allihopa': 'tout le monde', 'hos': 'chez', 'godkväll': 'bonsoir', 'ungdomar (m pl)': 'les junes', 'alla': 'tous', 'hon kommer': 'elle vient',
        'en gitarr': 'une guitare', 'toppen (m)': 'génial', 'jag älskar': "j'adore", 'ja kommer': 'je viens', 'också': 'aussi', 'jag gillar': "j'aime",
        'jag gillar mycket': "j'aime bien", 'du kommer': 'tu viens', 'va, hu sa?': 'comment', 'just det så är det': "c'est c,a",
        'jag föredrar': 'je préfère', 'London': 'Londres', 'svenskorna': 'les Suédoises', 'du är': 'tu es', 'omöjligt': 'impossible', 'jaha': 'eh ben',
        'okej': "d'accord", 'musiken': 'la musique', 'flickorna': 'les filles', 'jag bor': "j'habite", 'i': 'à', 'Köpenhamn': 'Copenhague',
        'framför allt': 'surtout', 'självklart': 'bien sûr', 'klassisk musik': 'la musique classique', 'jag lämnar er': 'je vous laisse',
        'godnatt': 'bonne nuit', 'nejdå': 'mais non'}
etre= {'vara': 'être', 'jag är': 'je suis', 'du är': 'tu es', 'han är': 'il est', 'hon är': 'elle est', 'man är/vi är': 'on est', 'vi är': 'nous sommes',
       'ni är': 'vous êtes', 'de är(m)': 'ils sont', 'de är(f)': 'elles sont'}

unune= {'en balkong': 'un balcon', 'en te': 'un thé', 'ett garage': 'un garage', 'en banan': 'une banane', 'en gitarr': 'une guitare',
        'ett bibliotek':  'une bibliothèque'}
chanson= {'20': 'vingt', '21': 'vingt et un', '22': 'vingt-deux', '23': 'vingt-trois', '24': 'vingt-quatre', '30': 'trente', '31': 'trente et un',
          '40': 'quarante', '50': 'cinquante', '60': 'soixante', '70': 'soixante-dix', '71': 'soixante et onze', '72': 'soixante-douze',
          '73': 'soixante-treize', '74': 'soixante-quatorze', '75': 'soixante-quinze', '76': 'soixante-seize', '77': 'soixante-dix-sept',
          '78': 'soixante-dix-huit', '79' : 'soixante-dix-neuf', '80': 'quatre-vingts', '81': 'quatre-vingt-un', '90': 'quatre-vingt-dix',
          '91' : 'quatre-vingt-onze', '100': 'cent', '200': 'deux cent', '1000': 'mille'}
cafe= {'vad?': "qu'est-ce que", 'vad ska vi ta': "qu'est-ce qu'on prend", 'en kompis(m)': 'un copain', 'en kompis(f)': 'une copine',
       'hennes/hans/sina kompisar': 'ses copains', 'på cafe': 'au café', 'jag tar': 'je prends', 'en saft med mintsmak':'un diablo menthe',
       'jag har': "j'ai", 'jag är törstig': "j'ai soif", 'jag vet inte': 'je ne sais pas', 'jag är inte törstig': "je n'ai pas soif",
       'egentligen': 'vraiment', 'kanske': 'peut-être', 'du tar': 'tu prends', 'en apelsinläsk': 'un Orangina', 'please': "s'il vous plaît",
       'servitören': 'le garc,on' , 'ni tar': 'vous prenez', 'senare': 'plus tard', 'Hur mycket blir det': 'c,a fait combien', 'en euro': 'un euro',
       'varsågod': 'voilà', 'damer och herrar': 'messieurs-dames', 'en fatöl': 'un demi'}
prendre= {'ta': 'prendre', 'jag tar': 'je prends', 'du tar': 'tu prends', 'han tar': 'il prend', 'hon tar':'elle prend', 'man/vi tar': 'on prend',
          'vi tar': 'nous prenons', 'ni tar': 'vous prenez', 'de tar(m)': 'ils prennent', 'de tar (f)': 'elles prennent'}
boire={'ska vi': 'on va', 'dricka':'boire', 'ett glas': 'un verre', 'okej': "d'accord", 'en espresso med varm mjölk': 'un café crème',
       'en grop/håla': 'un creux', 'jag är sugen på något': "j'ai un petit creux", 'jag är hungrig': "j'ai faim",
       'jag är inte hungrig': "je n'ai pas faim", 'inte alls': 'pas du tout', 'mina damer': 'mesdames', 'till er': 'pour vous', 'svart': 'noir',
       'en espresso': 'un café'}
pont= {'på': 'sur', 'bron': 'le pont', 'där dansar man': 'on y danse', 'i ring': 'en rond', 'de vackra': 'les beaux', 'herrarna': 'messieurs',
       'gör': 'font', 'så här': 'comme c,a', 'sedan': 'puis', 'igen': 'encore', 'de vackra damerna': 'les belles dames', 'musikerna': 'les musiciens',
       'soldaterna': 'les militaires', 'hos sig': 'chez lui', 'de andra': 'les autres'}
#kapitel 3
presente= {'jag presenterar mig': 'je me présente', 'en kvinna': 'une femme', 'jag är 17 år': "j'ai 17 ans", 'livet': 'la vie', 'jag går': 'je vais',
           'på gymnasiet': 'au lycée', 'tvåan i gymnasiet': 'en première', 'naturprogrammet': 'option scientifique', 'min familj': 'ma famille',
           'min pappa': 'mon père', 'min mamma': 'ma mère', 'en bror': 'un frère', 'en syster': 'une soeur', 'en hund': 'un chien',
           'jätte gullig (f)': 'super mignonne', 'killarna': 'les mecs', 'mina kompisar': 'mes copains', 'shoppa': 'faire du shopping',
           'festa': 'faire la fête', 'gå på bio': 'aller au ciné', 'läsa': 'lire', 'lyssna på musik': 'écouter de la musique', 'sjunga': 'chanter',
           'spela gitarr': 'jouer de la guitare', 'rock': 'du rock', 'min dator': 'mon ordi', 'en hemsida': 'une page web', 'chatta': 'tchatter',
           'på': 'sur', 'vänner': 'des amis', 'överallt': 'partout', 'alltid': 'toujours', 'lögnare': 'les menteurs'}
avoir= {'ha': 'avoir', 'jag har': "j'ai", 'du har': 'tu as', 'han har': 'il a', 'hon har': 'elle a', 'man har': 'on a', 'vi har': 'nous avons',
        'ni har': 'vous avez', 'de har(m)': 'ils ont', 'de har(f)': 'elles ont', 'kom ihåg binda vi, ni, de(f), de(m)(ok)': 'ok'}
extra={'gymnasieklass 1': 'seconde', 'gymnasieklass 2':'première', 'årskurs 3': 'terminale', 'telefonnummer': 'le numéro de téléphone',
       'det är': "c'est le", 'idag': "aujourd'hui", 'jag fick 20': "j'ai eu 20", 'vilket ämne': 'quelle matière', 'du skojar': 'sans blague',
       'en katt':'un chat', 'en bebis': 'un bébé'}
#redo extra
jesuis= {'en taxichaufför': 'un chauffeur de taxi', 'gift(m)': 'marié', 'en kvinna/fru': 'une femme', 'en kassör(m)': 'un caissier',
         'en kassörska(f)': 'une caissière', 'hon jobbar': 'elle travaille', 'ett barn(m/f)': 'un enfant', 'hon går': 'elle va',
         'på högstadiet': 'au collège', 'en sångare(m)': 'un chanteur', 'en sångerska(f)': 'une chanteuse', 'en skådespelare(m)': 'un acteur',
         'en skådespelerska(f)': 'une actrice', 'en sambo(m)':'un compagnon', 'en sambo(f)':'une compagne', 'en dotter': 'une fille',
         'född(m)': 'né', 'född (f)': 'née', 'en son': 'un fils'}
metier={'yrke': 'métier', 'advokat(m) + advokat(f)': 'avocat avocate', 'gymnasiestudent(m)+(f)': 'lycéen lycéenne', 'tandläkare': 'dentiste',
        'arkitekt': 'architecte', 'journalist': 'journaliste', 'läkare': 'médecin', 'sjuksköterska(m) + (f)' : 'infirmier infirmière',
        'student (m) + (f)': 'étudiant étudiante', 'industriarbetare(m)+ (f)': 'ouvrier ouvrière', 'professor': 'professeur',
        'lärare lågstadie (m)+ (f)': 'instituteur institutrice', 'cock(m) + (f)': 'cuisinier cuisinière', 'ingenjör': 'ingénieur',
        'programmerere': 'programmeur', 'kassör(m)+(f)': 'caissier caissière', 'taxichaufför': 'chauffeur de taxi', 'polis': 'agent de police',
        'arbetslös': 'au chômage'}
#kapitel 4
hexagone= {'ljuv, behaglig (2 sätt)': 'doux douxe', 'sexhörningen': "l'hexagone", 'det finns': 'il y a', 'en invånare': 'un habitant',
           'huvudstaden': 'la capitale', 'den andra': 'la deuxième', 'en stad': 'une ville', 'den näst största staden': 'la deuxième ville',
           'den tredje': 'la troisième', 'medlem i': 'membre de', 'stor(m)+(f)': 'grand grande', 'ett land': 'un pays',
           'industri(m) + (f)': 'industriel industrielle', 'bilarna': 'les voitures', 'franska': 'franc,aises', 'landskapet': 'le paysage',
           'Frankrikes': 'de la France', 'varierat': 'variè', 'berg':'des montagnes', 'alperna': 'les alpes', 'stora': 'grands',
           'floder': 'fleuves', 'många': 'beaucoup', 'vackra': 'belles', 'stränder': 'plages', 'på': 'sur', 'Franska Riverian': "la Côte d'Azur",
           'ungefär': 'environ', 'nästan': 'presque', 'en turist (m)': 'un touriste', 'de(m) besöker': 'ils visitent', 'varje': 'chaque',
           'ett år': 'une année', 'länderna': 'les pays', 'grann': 'voisins', 'i norr': 'au nord', 'i öster': "à l'est", 
           'i söder':'au sud', 'stora': 'grandes', 'hav(pl)': 'mers', 'i väster': "à l'ouest"}
lander= {'belgien': 'la belgique', 'luxemburg': 'le luxembourg','tyskland': "l'allemagne", 'schweiz': 'La suisse', 'italien': "l'italie",
         'spanien':"l'espagne",'medelhavet': 'la méditerranée', 'Atlanten': "l'atlantique"}
questions={'frågor': 'des questions', 'hur mycket (före substantiv': 'combien de', 'hur mycket/hur många': 'combien', 'vad, hur': 'comment',
           'är det så att': 'est-ce que', 'vem': 'qui', 'vilken/vilket (m)+(f)': 'quel quelle', 'vilka(m pl) + (f pl)': 'quels quelles',
           'var': 'où', 'vad': "qu'est-ce que", 'vad är det': "qu'est-ce que c'est"}
parle= {'vi pratar': 'on parle', 'du pratar': 'tu parles', 'vilket språk': 'quelle langue', 'dina kompisar': 'tes copains', 'hur gammal': 'quel âge',
        'här': 'ici', 'dagstidningarna': 'les journaux','en skola': 'une école', 'på franska': 'en franc,ais', 'tv': 'la télé', 'valutan': 'la monnaie',
        'singel': 'célibataire', 'ett sjukhus': 'un hôpital', 'där': 'où', 'hemma': 'à la maison', 'på jobbet': 'au travail', 'du gör': 'tu fais',
        'jag studerar ekonomi': "je fais des études d'économie", 'på universitetet': "à l'université", 'ensam': 'seul', 'mina föräldrar': 'mes parents',
        'mor och farförldrar': 'grands-parents', 'vi pratar': 'vous parlez', 'vi blandar': 'on mélange', 'tvåspråkig': 'bilingue', 'ert namn': 'votre nom',
        'vad gör ni i livet': "qu'est-ce que vous faites dans la vie", 'min man': 'mon mari', 'vi pratar': 'nous parlons', 'de pratar(m)': 'ils parlent',
        'deras kompisar': 'leurs copains'}

parler= {'prata': 'parler', 'jag pratar': 'je parle', 'du pratar': 'tu parles', 'han pratar': 'il parle', 'hon pratar': 'elle parle',
         'man pratar': 'on parle', 'vi pratar': 'nous parlons', 'ni pratar': 'vous parlez', 'de(m) pratar': 'ils parlent', 'de pratar(f)' : 'elles parlent'}
# Kapitel 5
temp= {'det är vackert väder': 'il fait beau', 'det ät dåligt väder': 'il fait mauvais', 'det är varmt': 'il fait chaud', 'det är kallt': 'il fait froid',
       'det är grått': 'il fait gris', 'der är soligt': 'il fait du soleil', 'det blåser': 'il fait du vent', 'det regnar':'il pleut',
       'det snöar': 'il neige', 'det är ganska kallt': 'il fait assez froid', 'det är minus tio': 'il fait moins dix',
       'det är femton grader': 'il fait quinze degrés', 'vilket väder är det idag': "quel temps fait-il aujourd'hui", 'moln': 'nuage',
       'promenerar': 'se promènent', 'när': 'quand', 'plötsligt': 'tout à coup', 'stannar': "s'arrête", 'frågar honom': 'lui demande',
       'vad gör du': "que fais-tu"}
veckodag= {'veckogagar': 'les jours de la semaine', 'måndag': 'lundi', 'tisdag': 'mardi', 'onsdag': 'mercredi', 'torsdag': 'jeudi', 'fredag': 'vendredi',
           'lördag': 'samedi', 'söndag': 'dimanche'}
ramsa= {'vilken tur': 'quelle chance', 'ett paraply': 'un parapluie', 'en himmel': 'un ciel', 'äta': 'manger', 'en milion': 'un million',
        'ett lotteri': 'une loterie', 'dansa':'danser', 'hela natten': 'tout la nuit', 'i sängen': 'au lit', "till mitt på dagen": "jusqu'à midi",
        'lov/semester': 'vacances'}
heures={'klockan är tio': 'il est dix heures', 'kvart över': 'et quart', 'och halvtimme': 'et demie', 'kvart i': 'moins le quart', 'tjugo i': 'moins vingt',
        'hösten': "l'automne", 'vintern': "l'hiver", 'våren': 'le printemps', 'sommaren': "l'été"}
#Kapitel 6
hotel= {'ett hotell': 'un hôtel', 'jag skulle vilja': 'je voudrais', 'boka': 'réserver', 'ett sovrum': 'une chambre', 'för': 'pour', 'en natt': 'une nuit',
        'vänta': 'attandez', 'jag är ledsen/beklagar': 'je suis désolé', 'fullt': 'complet', 'det är synd': "c'est dommage", 'vi kan': 'on peut',
        'ringa': 'téléphoner', 'ledig': 'libre', 'en person': 'une personne', 'vad kostar det': "c'est combien", 'frukosten': 'la petit déjeuner',
        'inkluderad': 'compris', 'kostar två euro': 'est à deux euros', 'per person': 'par personne', 'jag bokar det': 'je la réserve',
        'i vilket namn': 'à quel nom', 'anlända till': 'arriver à', 'vi har bokat': 'nous avons réservé', 'en id hndling': "une pièce d'identité",
        'en nyckel': 'une clé', 'en hiss': 'un ascenseur'}
dejeuner= {'sockret': 'le sucre', 'sylt': 'la confiture', 'apelsinjuice': "le jus d'oragne", 'toastat bröd': 'le pain grillé', 'flingor': 'les céréales',
           'bröd': 'le pain', 'croissant': 'le croissant', 'te': 'le thé', 'grillat bröd macka': 'la tartine', 'smör': 'le beurre', 'en loppa': 'une puce',
           'de går ut': 'elles sortent', 'eller': 'ou', 'kyssa på kinden': 'faire la bise', 'vacker': 'beau', 'som jag': 'comme moi',
           'en träff': 'un rendez-vous', 'kram': 'gros bisous' }
train= {'med tåg': 'en train', 'leta': 'chercher', 'till': 'pour', 'tung': 'lourd', 'dödstrött': 'crevé', 'det är bra/stämmer': "c'est bon",
        'äntligen': 'enfin', 'jättesöta': 'trop mignons', 'jag': 'moi', 'den stan': 'cette ville', 'där': 'là', 'ett vandrarhem': 'une auberge de jeunesse',
        'dessutom': 'en plus', 'vi åker okmring i': 'on fait le tour de', 'åka tillbaka': 'rentrer', 'ellerhur': 'hein',
        'vi tycker det är häftigt': 'on est fan', 'för oss': 'pour nous', 'första(m+f)': 'premier première', 'sova': 'dormir',
        'nära' : 'près de', 'en gata': 'une rue', 'en tunnelbana': 'un métro', 'man måste': 'il faut', 'de tror jag': 'je crois',
        'det är mycket folk': 'il y a du monde', 'hörni, lyssna': 'écoutez', 'tillsammans': 'ensemble', 'en mobil': 'un portable'}
aller= {'gå': 'aller', 'jag går': 'je vais', 'du går': 'tu vas', 'han går': 'il va', 'hon går': 'elle va', 'man går': 'on va', 'vi går' : 'nous allons',
        'ni går': 'vous allez', 'de (m) går': 'ils vont', 'de (f) går)': 'elles vont'}
        


## DELKURS 2

#Kapitel 7
cartes= { "kram": 'grosses bises', 'ett vykort': 'une carte postale', 'kära(f)': 'chère', 'kära(m)': 'cher', 'mormor/farmor': 'mamie',
          'några rader': 'un petit mot', 'där': 'où', 'tillbringa': 'passer', 'en härlig semester': 'de bonnes vacances', 'semester': 'des vacances',
          'är beläget, ligger': 'est situé', 'en meter': 'un mètre', 'olyckligtvis': 'malheureusement', 'vattnet': "l'eau", 'skaldjur': 'des crustacés',
          'du mår': 'tu vas', 'kram': 'gros bisous', 'gata': 'boulevard', 'jag sänder dig': "je t'envoie", 'en liten jälsning': 'un petit bonjour',
          'korsika': 'la corse', 'toppen': 'superbe', 'en träff/möte': 'un rendez-vous', 'solen kikar fram': 'le soleil est au rendez-vous',
          'en strand': 'une plage', 'varje dag': 'tous les jours', 'äta': 'mange'}
faire= { 'göra': 'faire', 'jag gör': 'je fais', 'du gör': 'tu fais', 'han gör': 'il fait', 'hon gör': 'elle fait', 'man gör': 'on fait',
         'vi gör': 'nous faisons', 'ni gör': 'vous faites', 'de (m) gör': 'ils font', 'de gör(f)': 'elles font'}
tuesou= { 'har du hittat': 'tu as trouvé', 'du vet': 'tu sais', 'ibland': 'parfois', 'dåså, nåja, ok': 'bon', 'hur som helst': 'en tout cas',
          'då så!': 'ben voilà', 'jag måste': 'je dois', 'sluta': 'arrêter', 'tillslut': 'finalement',
          'thomas och jag har gjort slut': 'on a cassé avec thomas', 'jaså': 'ah oui', 'alltså': 'donc', 'ofta': 'souvent', 'jag förstår':"j'ai compris",
          'så är det': "c'est c,a", 'samtidigt': 'en même temps', 'det gör inget': "c'est pas grave", 'kär i (m)': 'amoureux de', 'kär i(f)': 'amoureuse de',
          'kom igen': 'allez', 'verkligen': 'tiens', 'komma för sent': 'être en retard', 'för mycket': 'trop', 'inte så värst': 'pas trop',
          'det skille vara toppen': 'c,a serait super', 'att hitta': 'trouver', 'att bryta': 'casser'}
#Kapitell8
HotelVille= {'trötta': 'fatigués', 'hitta': 'trouver', 'titta/titta på': 'regarde', 'en skylt': 'un panneau', 'vi frågar': 'on demande à',
             'en dam': 'une dame', 'ursäkta': 'pardon', 'hur kommer man till': 'pour aller à', 'lätt': 'facile', 'fortsätta': 'continuer',
             'rakt fram': 'tout droit', 'andra gatan': 'la deuxième rue', 'till vänster': 'à gauche', 'passera': 'passer', 'efter': 'après',
             'en kyrka': 'une église', 'sväng': 'tournez', 'till höger': 'à droite', 'där': 'là', 'skratta': 'rire', 'en borgmästare': 'un maire',
             'sedan': 'traverser', 'sedan': 'puis', 'ända till': "jusqu'à", 'torget': 'la place',
             'sedan': 'ensuite', 'dyr (m)': 'cher', 'dyr (f)': 'chère', 'billig': 'pas cher', 'mitt emot': 'en face de', 'brevid': 'à côté de'}
velib= {'turistbyrå': "l'office de tourisme", 'banken': 'la banque', 'en stadscykel': 'un vélib', 'en pojkvän': 'un petit ami', 'hon får':'elle rec,oit',
        'hennes/sin': 'sa', 'en kusin (m)': 'un cousin', 'en kusin(f)': 'une cousine', 'vem då': 'qui c,a', 'först':"d'abord", 'galen//tokig (m)': 'fou',
        'galen/tokig (f)' : 'folle', 'det är uppförsbacke': 'c,a monte', 'en gräsmatta': 'une pelouse', 'lite': 'un peu', 'en frukt': 'un fruit',
        'inget/ingen': 'pas de', 'en cykel': 'un vélo', 'cykla': 'faire du vélo', 'gå upp i': 'monter à', 'en trappa': 'un escalier',
        'billigare': 'moins cher', 'mindre, kortare': 'moins de', 'stanna kvar': 'rester', 'där nere': 'en bas', 'det kostar': 'c,a coûte',
        'det är inte klokt': "c'est dingue", 'känd': 'connu', 'ibland': 'des fois', 'man/vi vill': 'on veut', 'vilja': 'vouloir',
        'medan vi väntar': 'en attendant', 'köpa': 'acheter', 'skratta/skoja': 'rigoler', 'vi rör oss': 'on bouge', 'mot': 'vers',
        'till fots': 'à pied', 'tillslut': 'pour terminer', 'det räcker': "c,a suffit", 'sista': 'dernier', 'gillar du det': 'c,a te dit',
        'deras': 'leur', 'eller också': 'ou bien'}
#Kapitel9
amongout= { 'i min smak': 'à mon goût', 'en färg': 'une couleur', 'en fråga om': 'une question de', 'en smak': 'un goût', 'gå in/komma in': 'entrer',
            'lämna': 'quitter', 'livet i färg': 'la vie en couleurs', 'ibland': 'des fois', 'jag frågar mig själv': 'je me demande',
            'varför': 'pourquoi', 'en teve': 'une télé', 'däremot': 'par contre', 'en vägg': 'un mur', 'de andra':'les autres',
            'gardiner': 'des rideaux', 'en matta': 'un tapis', 'trikoloren(franska flaggan)': 'le drapeau tricolore', 'en säng': 'un lit',
            'en prydnadskudde': 'un coussin', 'i alla färger': 'de toutes les couleurs', 'en affisch': 'un poster', 'en målare': 'un peintre',
            'ett skrivbord': 'un bureau', 'en stol': 'une chaise', 'även om': 'même si', 'tycka/tänka': 'penser', 'var och en har sin smak':
            'à chacun son goût'}
lescouleurs= { 'blå': 'bleu bleue', 'grå': 'gris grise', 'grön': 'vert verte', 'vit': 'blanc blanche', 'gul': 'jaune', 'rosa': 'rose',
               'röd': 'rouge', 'svart': 'noir noire', 'lila': 'violet violette', 'beige': 'beige', 'brun': 'marron', 'orange': 'orange'}
sovrum= {'en soffa': 'un canapé', 'en fåtölj': 'un fauteuil', 'en tavla': 'une tableau', 'ett bord' : 'un table',
         'en stol': 'une chaise', 'en byrå': 'une commode', 'en spegel': 'un miroir', 'en skorsten': 'une cheminée',
         'en lampa':'une lampe', 'heltäckningsmatta': 'une moquette', 'en garderob': 'une armoire', 'på': 'sur',
         'till vänster om': 'à gauche de', 'till höger om': 'à droite de'}
studio= {'en etta med kokvrå': 'un studio', 'mellan': 'entre', 'ett fönster': 'une fenêtre', 'en stereo': 'une chaîne hi-fi',
         'en hylla': 'une étagère', 'ni ser': 'vous voyez', 'ett klädskåp': 'une armoire', 'i mörkt trä': 'en bois brun', 'kläderna': 'les vêtements',
         'bredvid': 'à côté de', 'ett nattduskbord': 'une table de nuit', 'en klockradio': 'un radio-réveil', 'ett kök': 'une cuisine',
         'lyons fotbollslag': "l'Olympique Lyonnais", 'ett vardagsrum' : 'une salle de séjour', 'behöva': 'avoir besoin de', 'en gasplatta':
         'un réchaud à gaz', 'en ugn': 'un four', 'ett kylskåp': 'un frigo', 'en diskbänk': 'un évier', 'diska': 'faire la vaisselle',
         'ett badrum': 'une salle de bains', 'ganska' : 'assez' }
#Studio gör om
#Genial 2
#Kapitel 1

CDG= { 'älskling':'chéri', 'fattar du' : 'tu te rends compte', 'inse, förstå': 'se rendre compte', 'vänta på': 'attendre', 'jag ska polisanmäla':
       'je vais porter plainte', 'vad är det': "qu'est-ce qu'il y a", 'ett flygplan': 'un avion', 'vara försenad': 'être en retard', 'de säger oss':
       'ils nous disent', 'bara': 'seulement', 'ingenting': 'ne ... rien', 'irritera' : 'énerver', 'ännu mer': 'encore plus', 'en chef': 'un patron',
       'nyss ha': 'venir de', 'behöva': 'avoir besoin de', 'sina läxor': 'ses devoirs', 'celine frågade mig': "celine m'a demandé", 'lägg på':
       'raccrocher', 'dricka': 'boire', 'där borta': 'là-bas', 'ombordsstigning (m)': 'embarquement', 'en gate': 'un porte', 'redan': 'déjà',
       'en flygning': 'un vol', 'nästa': 'prochain', 'bara': 'juste', 'olyckliggtvis': 'malheureusement', 'slå (ett nummer)': 'composer' }
europe= {'USA' : 'les Etats-Unis', 'på en vecka': 'en huit jours', 'en vistelse': 'un séjour', 'ha det så trevligt' : 'bon séjour',
         'midnattssolen': 'le soleil de minuit', 'München': 'Munich', 'en korv' : 'une sauciesse', 'innan/före': 'avant', 'innan han går över':
         'avant de traverser', 'en present': 'un cadeau', 'ett armbandsur': 'une montre', 'Genevesjön': 'le lac Léman', 'en mussla': 'une moule',
         'pommes frites': 'des frites', 'musslor med pommes frites': 'des moules frites', 'en kanal': 'un canal', 'kanaler': 'des canaux',
         'hyra': 'louer', 'nederländerna': 'les Pays-Bas', 'en skärgård': 'un archipel', 'himlen':'le ciel', 'vilken semester': 'quelles vacances',
         'alltför': 'trop', 'röra på sig': 'bouger', 'en tårta': 'un gâteau', 'ett slott': 'un château', 'utmattad, dödstrött': 'crevé',
         'gårdagen': 'la veille', 'han tar på sig': 'il met', 'solglasögon': 'des lunettes de soleil', 'han solar': 'il bronze', 'simma': 'nager',
         'inte mer/ inte längre': 'ne ... plus', 'han har inga pengar kvar': "il n'a plus d'argent", 'pengarna': "l'argent", 'en kurs': 'un stage'}
partir= {'resa/ ge sig av': 'partir', 'jag reser': 'je pars', 'du reser': 'tu pars', 'han reser': 'il part', 'hon reser': 'elle part', 'vi reser':
         'on part', 'vi reser': 'nous partons', 'ni reser': 'vous partez', 'De (f) reser': 'elles partent', 'De (m) reser': 'ils partent'}
famille= {'föräldrar': 'parents', 'man/make': 'mari', 'fru': 'femme', 'sambo': 'compagnon', 'sambo yngre (m)': 'copain ami', 'sambo yngre (f)':
          'copine amie','tvilling (m)': 'jumeau', 'tvilling (f)': 'jumelle', 'tvillingar (m osen f)': 'jumeaux jumelles', 'barnbarn(f)': 'petite-fille',
          'barnbarb(m)':'petit-fils', 'morbror/farbror': 'oncle', 'moster/faster': 'tante', 'kusin m' : 'cousin', 'kusin f': 'cousine',
          'bror/systerson': 'neveu', 'bror/systerdotter': 'nièce', 'svärfar': 'beau-père', 'svärmor': 'belle-mère', 'svåger': 'beau-frère',
          'svägerska': 'belle-soeur', 'gift(m)': 'marié', 'separerad (m)': 'séparé','skild m': 'divorcé', 'singel m': 'célibataire', 'död m': 'mort'}
# Kapitel 2
piquenique= {'gärna': 'avec plaisir', 'vid havet': 'au bord de la mer', 'tonfisk(m)': 'thon', 'en frukt': 'un fruit', 'några/lite': 'un peu de',
             'man måste': 'il faut', 'först': "d'abord", 'en marknad': 'un marché', 'handla': 'faire des courses', 'något annat?': 'et avec c,a',
             'jag behöver': 'il me faut', 'ett äpple': 'une pomme', 'det är bra så': "c'est bien comme c,a", 'ha en trevlig dag': 'bonne journée',
             'vatten': "de l'eau", 'precis, just det': 'justement', 'köpa': 'acheter', 'ska vi slå oss ner här': "on s'installe ici", 'perfekt': 'parfait',
             'en utsikt': 'une vue', 'över':'sur', 'fantastiskt': 'superbe', 'jag är hungrig': "j'ai faim", 'hungrig som en varg': 'une faim de loup',
             'jag är törstig': "j'ai soif", 'ett glas vatten': "un verre d'eau", 'genast': 'tout de suite', 'smaklig måltif': 'bon appétit'}
fruit= {'ett halvt kilo': 'une livre', 'mogen': 'mûr', 'totalt': 'au total', 'en citron': 'un citron', 'en melon': 'un melon', 'en annanas': 'un ananas',
        'en aprikos': 'un abricot', 'en kiwi':'un kiwi',
             'en grapefrukt': 'un pamplemousse', 'en vattenmelon': 'une pastèque', 'en apelsin': 'un orange', 'hallon' : 'des framboises',
             'en banan': 'une banane', 'ett äpple': 'une pomme', 'en persika': 'une pêche', 'ett plommon': 'une prune', 'ett päron': 'une poire',
             'körsbär': 'des cerises', 'vindruvor': 'du raisin', 'jordgubbar': 'des fraises'}
legumes= {'grönsaker': 'des légumes', 'majs': 'du maïs', 'en avokado': 'un avocat', 'en lök': 'un oignon', 'en gurka': 'un concombre',
          'en blomkål': 'un chou-fleur', 'en paprika': 'un poivron', 'en tomat': 'une tomate', 'en morot': 'une carotte', 'vitlök': "de l'ail",
          'potatisar': 'des pommes de terre', 'spenat': 'des épinards', 'svamp': 'des champignons', 'en zuccini': 'une courgette',
          'en aubergie': 'une aubergine', 'en sallad': 'une laitue'}
uttryck= {'ha lust att': 'avoir envie', 'frysa': 'avoir froid', 'vara varm': 'avoir chaud', 'ha rätt': 'avoir raison', 'ha fel': 'avoir tort',
          'vara rädd för': 'avoir peur de', 'skämmas för': 'avoir honte', 'behöva': 'avoir besoin de', 'vara sömnig': 'avoir sommeil' }
restaurant= {'resa': 'voyager', 'under om tid': 'pedant', 'där är de': 'les voilà', 'en meny': 'un menu', 'med kolsyra m f': 'gazeux gaseuse',
             'utan kolsyra m f': 'plat plate', 'har ni bestämt er': 'vous avez choisi', 'rekomenderar': 'recommander', 'alltför': 'trop',
             'en förrätt': 'une entrée', 'en gryta': 'un civet', 'en kanin': 'un lapin', 'en sås': 'une sauce', 'det är nödvängigt': 'il faut',
             'en ordbok': 'un dictionnaire', 'jag förstår': 'je comprends', 'en tupp i vin': 'un coq au vin', 'hur smakade det': 'c,a a été',
             'utsökt m f ': 'délicieux delicieuse', 'en efterätt': 'un dessert', 'en kula': 'une boule', 'det är bra så': 'c,a va bien comme c,a',
             'notan': "l'addition"}
mettreboire= {'sätta ställa lägga': 'mettre', 'jag lägger': 'je mets', 'du lägger': 'tu mets', 'han, (hon, man) lägger': 'il met', 'vi lägger':
              'nous mettons', 'ni lägger': 'vous mettez', 'de m (de f) lägger' : 'ils mettent', 'dricka': 'boire', 'jag dricker': 'je bois',
              'du dricker': 'tu bois', 'han (hon man) dricker': 'il boit', 'vi dricker': 'nous buvons', 'ni dricker': 'vous buvez',
              'de m (de f) dricker': 'ils boivent'}
chans= {'min svaghet': 'mon péché mignon', 'vaniljkräm': 'la crème anglaise', 'jag suger ur benen': 'je suce les os', 'torkade fikon': 'des figues sèches',
        'honungen': 'le miel', 'sockerkaka indränkt med rom': 'la baba au rhum', 'det är antecknat': "c'est noté", 'stör det?': 'c,a ne vous gêne pas',
        'tvärtom': 'au contraire'}

### Kurs 2 - A12

# Kapitel 3
tropcher= {'kläderna': 'les fringues', 'vad': 'quoi', 'ge' : 'offrir', 'i kväll': 'ce soir', 'ännu': 'encore', 'jag har inte haft tid att':
           "je n'ai pas eu le temps de", 'åt/ till honnom': 'lui', 'skämtar du eller': 'tu rigoles ou quoi', 'så': 'tellement',
           'jag blir': 'je deviens', 'galen m f': 'fou folle', 'jag lovar; verkligen': 'ma parole', 'jag följer med dig': "je t'accompagne",
           'skynda dig': 'dépêche-toi', 'avdelningen': 'le rayon', 'en tröja': 'un pull', 'du har rätt': 'tu as raison', 'inte direkt': 'pas tellement',
           'i alla fall/ ändå': 'quand même', 'tillräckligt med': 'assez de', 'pengar': 'du fric', 'det är sant': "c'est vrai", 'har du sett': "t'as vu",
           'kom': 'viens', 'en groda': 'une grenouille', 'du tycker': 'tu trouves', 'det är': 'c,a fait', 'sådär/ såhär': 'comme c,a', 'modernt':'tendance',
           'vilken storlek har han': 'il fait quelle taille', 'en klädstorlek': 'une taille', 'jag skulle säga': 'je dirais', 'han har L': 'il fait du L',
           'hjälpa': 'aider', 'ett ögonblick': 'un instant', 'jag tar den': 'je le prends', 'ett betalkort': 'une carte', 'knappa in': 'taper',
           'ett kvitto': 'un ticket'}
lesvetements= {'kläderna': 'les vêtements', 'en T-shirt': 'un T-shirt', 'en tröja': 'un pull', 'en tenniströja': 'un polo', 'en sweatshirt':'un sweat-shirt'
               , 'en kofta/väst': 'un gilet', 'en skjorta': 'une chemise', 'ett linne': 'un débardeur', 'byxor': 'un pantalon', 'jeans': 'un jean',
               'shorts': 'un short', 'en kavaj/ jacka': 'une veste', 'en rock/kappa': 'un manteau', 'en midjelång jacka': 'un blouson',
               'en kort skinnjacka':'un blouson en cuir', 'en dunjacka': 'une doudoune', 'en träningsoverall': 'un jogging', 'en lätt regnjacka':'un K-way',
               'en scarf': 'un foulard', 'en halsduk': 'une écharpe', 'en mössa': 'un bonnet', 'en keps': 'une casquette', 'en hatt': 'un chapeau',
               'strumpor': 'des chausettes', 'handskar': 'des gants', 'ett skärp': 'une ceinture', 'skor': 'des chaussures', 'sandaler': 'des sandales',
               'stövlar': 'des bottes', 'gymnastikskor': 'des baskets', 'för honom': 'pour lui', 'badbyxor': 'un maillot', 'en slips':'une cravate',
               'kalsonger': 'un slip', 'en kostym': 'un costume', 'för henne': 'pour elle', 'en blus': 'un chemisier', 'damsockor': 'des socquettes',
               'thights/legging': 'des leggings', 'en bikini/baddräckt': 'un bikini un maillot', 'en klänning': 'une robe', 'en kjol': 'une jupe',
               'en behå': 'un soutien-gorge un soutif', 'en trosa': 'une culotte un slip'}
acheter= {'köpa': 'acheter', 'jag köper': "j'achète", 'du köper': 'tu achètes', 'han köper': 'il achète', 'vi köper': 'nous achetons',
          'ni köper': 'vous achetez', 'de (m) köper': 'ils achètent'}
rire= {'en baby': 'un bébé', 'sova middag': 'faire la sieste', 'samma': 'même', 'lyfta': 'soulever', 'ett lakan': 'un drap', 'företa/göra': 'procéder à',
       'en undersökning': 'un examen', 'man har satt sig på' : "on t'as mis"}
balade= {'en promenad': 'une balade', 'det är riktigt hundväder': 'il fait un temps de chien', 'det är tydligt': "c'est clair",
         'vad händer': "qu'est-ce quise passe", 'sydfrankrike': 'le Midi', 'hemskt förskräckligt': 'épouvantable', 'man skulle kunna tro': 'on se croirait',
         'jag är ledsen': 'je suis désolé', 'iskall': 'glacial', 'en trätt': 'un rendez-vous', 'vid': 'vers', 'värma upp sig': 'se réchauffer',
         'i': 'par', 'det här vädret': 'ce temps', 'vi ses': 'a toute'}
plustard= { 'ny m f': 'neuf neuve', 'alldeles ny': 'tout neuf', 'kolla': 'tiens', 'känner du till': 'tu connais', 'en målare': 'un peintre',
            'favorit': 'préféré', 'hos mig': 'chez moi', 'helig': 'ste', 'en tavla': 'un tableau', 'rea': 'soldes', 'en affär': 'un magasin',
            'en täckjacka': 'un blouson matelassé', 'prova': 'essayer', 'prova den': "l'essayer", 'du kommer inte att frysa mer': "tu n'auras plus froid",
            'jättehäftig': 'trop top', 'svindyrt/superbilligt': 'un prix fou', 'en provhytt': 'une cabine', 'längst bort': 'au fond'}
meramer= {'kassan': 'la caisse', 'betala' : 'payer', 'ett plagg': 'une pièce', 'gammal m f': 'vieux vieille', 'hotell resturang programmet gymn':
          'un lycée hôtelier', 'en dräkt': 'un tailleur', 'en klädsel': 'une tenue', 'en ledig klädsel': 'une tenue décontractée', 'kan jag hjälpa dig':
          "je peux vous aider", 'längst il': 'au fond', 'enligt min åsikt': 'à mon avis'}
vendre= {'sälja': 'vendre', 'jag säljer': 'je vends', 'du säljer': 'tu vends', 'han säljer': 'il vend', 'vi säljer': 'nous vendons', 'ni säljer':
         'vous vendez', 'de (m) säljer': 'ils vendent'}
cecescette= { 'i mrose': 'ce matin', 'i våras/i vår' :'ce printemps', 'i eftermiddags/i eftermiddag': 'cet après-midi',
              'i sommar/ i somras': 'cet été', 'i kväll': 'ce soir', 'i höst/i höstas': 'cet automne', 'i vinter/i vintras': 'cet hiver'}

attandre= {'vänta': 'attendre', 'jag väntar': "j'attends", 'du väntar': 'tu attends', 'han väntar': 'il attend',
           'vi väntar': 'nous attendons', 'ni väntar': 'vous attendez', 'de (m) vänar': 'ils attendent' }


repondre= {' jag svarar': 'je réponds', 'du svarar': 'tu réponds', 'han svarar': 'il répond', 'vi svarar': 'nous répondons',
           'ni svarar': 'vous répondez', 'de (m) svarar': 'ils répondent'}
#L'articel partitif + négation --> endast de används i negationer medans du, de la, des används annars
 


#Kapitel 4

catherine= {'som vanligt': "comme d'habitude", 'vi stiger upp': "nous nous levons", 'jag sminkar mig': "je me maquille", 'jag fixar håret': 'je me coiffe',
            'i allmänhet': 'en général', 'befinna sig, vara': 'se trouver', '(här)det tar mig': 'je mets', 'en knapp halvtimme': 'une petite demi-heure',
            'en landsväg': 'une route', 'varken ... eller': 'ni ... ni', 'trafik': 'circulation', 'halt väglag/halka': 'verglas',
            'en optiker (m)': 'un opticien', 'en optiker (f)': 'une opticienne', 'försäljning(f)': 'vente', 'ensam(m)': 'seul',
            'jag har inte tråkigt': "je ne m'ennuie pas", 'när det gäller': 'au niveau de', 'en arbetstid/ ett schema': 'un horaire', 'vilket': 'ce qui',
            'då/när': 'où', 'vara ivrig att': 'avoir hâte de', 'vila mig': 'me reposer', 'den som': 'celui qui', 'laga mat': 'faire à manger',
            'diska': 'faire la vaisselle', '(här) gå/sänds': 'passer', 'försöka': 'essayer', 'ett pass': 'une séance', 'streching': 'des étirements',
            'crunches/situps': 'des abdominaux', 'vi går och lägger oss': 'nous nous couchons', 'ett slut': 'une fin'}
olivier= {'årskurs ett': 'seconde', 'jag stiger upp': 'je me lève', 'jag tvättar mig': 'je me lave', 'ja gör mig i ordning': 'je me prépare',
          'jag måste': 'je dois', 'en lektion':'un cours', 'börja': 'commencer', 'en rast': 'une récréation', 'det vill säga': "c'est-à-dire",
          'putsa ut': 'souffler', 'ett förhör/prov': 'une interrogation', 'utnyttja/dra nytta av': 'profiter', 'repetera/läsa på': 'réviser',
          'fickpengar': 'argent de poche', 'en sötpotatis': 'une patate', 'van': 'habitué', 'hjälpa': 'aider', 'ved':'bois', 'en dunk': 'un bidon',
          'källvatten': 'eau de la source', 'en deg': 'une pâte', 'en läxa': 'un devoir', 'till och med': 'même', 'grejer': 'affaires',
          'kasta ut': 'jeter dehors', 'en surfplatta': 'une tablette', 'kyrkogård': 'cimetière', 'kissa': 'faire pipi', 'snäll': 'sage'}
Reflexiva_verb= {'tvätta sig': 'se laver', 'sminka sig': 'se maquiller', 'göra sig i ordning': 'se préparer', 'skynda sig': 'se dépêcher',
                 'gå o lägga sig': 'se coucher', 'klä på sig': "s'habiller", 'köpa sig': "s'acheter", 'jag lägger mig': 'je me couche',
                 'du lägger dig': 'tu te couches', 'han lägger sig': 'il se couche', 'vi lägger oss': 'nous nous couchons',
                 'ni lägger er': 'vous vous couchez', 'de lägger sig (m)': 'ils se couchent' }
#Reflexiva verb i passe compose använder etre. till exempel je me suis lavée --> jag tvättade mig
#Passe compose j'ai jouer --> vem + avoir + verb i passé copose
#Futurum (JAG SKA) jag vais --> vem + aller + verb i grundform (i vissa fall) I andra fall böjs det som nedan:
fururum= {'jag kommer att gå': "j'irai", 'du kommer att gå': 'tu iras', 'han kommer att gå': 'il ira', 'vi kommer att gå': 'nous irons',
          'ni kommer att gå': 'vous irez', 'de (m) kommer att gå': 'ils iront', 'jag kommer att vara': 'je serais',
          'du kommer att vara': 'tu seras', 'han kommer att vara': 'il sera', 'vi kommer att vara': 'nous serons',
          'ni kommer att vara': 'vous serez', 'de (m) kommer att vara': 'ils seront', 'gömma': 'cacher', 'jag kommer att gömma mig': 'je cacheras',
          'du kommer att gömma dig': 'tu cacheras', 'han komemr att gömma sig': 'il cachera', 'vi kommer att görra oss': 'nous cacherons',
          'ni kommer att gömma er': 'vous cacherez', 'de(m) kommer att gömma sig' : 'ils cacheront'}
          
unmatin= {'alla andra': 'tous les autres', 'visa, ange': 'indiquer', 'väckarklockan': 'le réveil', 'vard. ett jobb': 'un boulot',
          'för att ta sig dit': "pour s'y rendre", 'han gör kaffe åt sig': 'il se fait un café', 'hälla': 'verser', 'välta': 'renverser',
          'rengöra': 'nettoyer', 'skära': 'couper', 'en skiva': 'une tranche', 'fingret': 'le doigt', 'tusan också': 'zut', 'ett plåster':'un pansement',
          'raka sig': 'se raser', 'strunt samma': 'tant pis', 'starta': 'démarrer', 'gripas av panik': 'paniquer', 'ett företag': 'une entreprise',
          'dit, där': 'y', 'ingen är där': "personne n'est là", 'ingen': 'ne ... personne', 'antingen ... eller': 'ou ... ou', 'pasta': 'des pâtes',
          'ris': 'du riz', 'fixa käk': 'faire la bouffe', 'honung': 'du miel', 'vissla': 'siffler'}
devoir= { 'måste/ska': 'devoir', 'jag måste': 'je dois', 'du måste': 'tu dois', 'han måste':'il doit',
          'vi måste': 'nous devons', 'ni måste': 'vous devez', 'de måste': 'ils doivent'}
nene= {'dra nytta av': 'profiter de', 'långt ifrån': 'loin de', 'ingenting': 'ne ... rien',
       'inte förrän': 'ne ... que', 'det beror på': 'c,a dépend'}
apprendre= {'lära sig': 'apprendre', 'medan han tittar på': 'en regardant', 'ge sig iväg': 'se rendre', 'för sent': 'trop tard',
            'ingen': 'ne ... personne'}
finir= {'avslute/sluta':'finir', 'jag sluter': 'je finis', 'du slutar': 'tu finis', 'han slutar': 'il finit',
        'vi slutar': 'nous finissons', 'ni slutar': 'vous finissez', 'de (m) slutar': 'ils finissent',
        'välja': 'choisir', 'att lyckas': 'réussir', 'att reflektera': 'réfléchir'}


# kapitel 5

auvoleur= {'ta fast tjuven': 'au voleur', 'en tjuv': 'un voleur', 'sommarlover':'les grandes vacances', 'tågluffa': 'voyager avec interrail',
           'en kille': 'un mec', 'inte illa': 'pas mal', 'den, han, honom': 'celui', 'ögon, ögonen': 'les yeux', 'den andra': "l'autre",
           'ännu': 'encore', 'snyggare': 'plus beau', 'håret': 'les cheveux', 'krulligt, lockigt': 'bouclé', 'ett leefe': 'un sourire',
           'de kommer från': 'ils viennent de', 'sätta sig': "s'asseoir", 'varsågod/ ta för er': 'allez-y', 'sätt er': 'asseyez-vous', 'inte heller': 'non plus',
           'en accent': 'un accent', 'se, besöka': 'voir', 'trevlig': 'sympa', 'plötslig': "tout d'un coup", 'stanna': "s'arrêter", 'kom': 'viens',
           'vi måste': 'on doit',  'stiga av': 'descendre', 'vi ses!': 'à la prochaine', 'falla, ramla': 'tomber', 'armarna/ famnen': 'les bras', 'hjäpa hen': "l'aider",
           'vi ses': 'on se voit' , 'ett vandrarhem': 'une auberge de jeunesse', 'en plånbok': 'un portefeuille', 'en polisstation':'un commissariat de police',
           'arg(m)': 'fâché', 'gråta': 'pleurer'}
#un beau, un bel homme --> när det är un o vokal blir det bel, deux beaux hommes
#une belle, trois belles 
beau= { 'en snygg kille': 'un beau garc,on', 'en snygg man': 'un bel homme', 'två snygga killar': 'deux beaux hommes', 'en snygg tjej': 'une belle fille',
        'tre snygga tjejer': 'trois belles femmes', 'en gammal hund': 'un vieux chien' ,'en gammal vän (m)': 'un vieil ami', 'fyra gamla vänner(m)': 'quatre vieux amis',
        'en gammal vän(f)': 'une vielle ami', 'tre gamla vänner': 'trois vielles amies', 'en ny mobil': 'un nouveau portable', 'ett nytt hotell': 'un nouvel hôtel',
        'två nya hotell': 'deux nouveaux hôtels' , 'en ny skjorta': 'une nouvellle cheimise', 'tre nya skjortor': 'trois nouvelles chemises'}
extrakap5= {'en gågata': 'une rue piétonne', 'en musiker': 'un musicien', 'ett förhör': 'une interrogatoire', 'ett id kort': " une carte d'inentité",
            'färgat hår': 'les cheveux teints', 'man/vi sover': 'on dort', 'om ni vill': 'si vous voulez', 'jag hoppas ni ursäktar': 'vous permettez',
            'ett visa kort': 'une carte VISA', 'guld(m)': 'or', 'stoppar' : 'fait stopper', 'såg ni inte': "vous n'avez pas vu", 'rödljuset': 'le feu rouge',
            'en tändsticka': 'une allumette', 'tända': 'allumer', 'hel': 'entier', 'mörkret': 'la obscurité', 'minnas': 'rappeler', 'när jag håller dig': 'en te serrant' }
venir= {'jag kommer': 'je viens', 'du kommer' : 'tu viens', 'han kommer': 'il vient', 'vi kommer': 'nous venons', 'ni kommer': 'vous nenez',
        'de (m) kommer': 'ils viennent'}
lecorps= {'kroppen': 'le corps', 'ansiktet': 'le visage', 'håret': 'les cheveux', 'ett öga': 'un oeil', 'ögonen': 'les yeux', 'örat': "l'oreille",
           'näsan': 'le nez', 'läpparna': 'la bouche', 'nacken': 'le cou', 'halsen': 'la gorge', 'armen' :'le bras', 'handen': 'le main', 'benet': 'la jambe',
           'foten': 'le pied', 'knät': 'le genou', 'knäna': 'les genoux', 'rumpan': 'les fesses', 'magen': 'le ventre', 'ryggen': 'le dos', 'bröstet': 'la poitrine',
           'axeln': "l'épaule", 'skägget': 'la barbe', 'tänderna':  'les dents',  'huvudet': 'la tête', 'mustachen': 'la moustache', 'flintskallig': 'chauve',
           'hästsvans': 'une queue de cheval' , 'ginger': 'roux', 'kort hår': 'cheveux courts'}
police= {'en bostad, en hemort': 'un domicile', 'vad är det/ vads tår på': "qu'est-ce qu'il y a", 'höra': 'entendre', 'ett ljud,ett oljud': 'un bruit',
         'komma ut/gå ut': 'sortir', 'guldsmadjeaffären': 'la bijouterie', 'ett smycke': 'un bijou', 'han springer': 'il court', 'mot': 'vers', 'som': 'qui', 'vid ratten': 'au volant',
         'ge sig av': "s'en aller", 'hurdan var han': 'il était comment', 'typ, form': 'style', 'han hade på sig': 'il portait', 'en klack': 'un talon', 'med klackar': 'à talons',
         'hög': 'haut', 'hela tiden': 'tout le temps', 'skriva (en rapport': 'rédiger', 'en efterlysning': 'un avis de recherche', 'säker': 'sûr',
         'en beskrivning': 'une description', 'exakt': 'précis', 'en konstnär': 'un artiste-peintre', "jag är van": "j'ai l'habitude", '(här) noga': 'bien',
         'folket': 'les gens'}
jeter= {'att kasta': 'jeter', 'jag kastar': 'je jette', 'du kastar': 'tu jettes', 'han kastar': 'il jette', 'vi kastar': 'nous jetons', 'ni kastar': 'vous jetez', 'de kastar(m)': 'ils jettent'}
vouloir= {'vilja': 'vouloir', 'jag vill': 'je veux', 'du vill': 'tu veux', 'han vill': 'il veut', 'vi vill': 'nous voulons', 'ni vill': 'vous voulez', 'de(m) vill': 'ils veulent',
          'kunna': 'pouvoir', 'jag kan': 'je peux', 'du kan': 'tu peux', 'han kan': 'il peut', 'vi kan': 'nous pouvons', 'ni kan': 'vous pouvez', 'de(m) kan': 'ils peuvent'}
comparatif= {'längre än': 'plus grand que', 'kortare än': 'moins grand que', 'lika lång': 'aussi grand que',
             'längst (m)': 'le plus grand', 'lämgst(f)': 'la plus grande',  'dyraste(f)': 'la plus chère', 'dyrast(m)': 'le plus cher'}
savoir= {'kunna, veta': 'savoir', 'kan ni/ vet ni hur man': 'savez-vous', 'jag kan/vet': 'je sais', 'du an/vet': 'tu sais',
         'han kan/vet': 'il sait', 'vi kan/vet': 'nous savons', 'ni kan/vet': 'vous savez', 'de (m) kan/vet': 'ils savent', 'passé composé savvoir': "su",
         'jag kunde': "j'ai su", 'imperfekt jag savoir': 'je savais' , 'futurum jag savoir': 'je saurai'} 
#Passe compose: Generally speaking, the passé composé corresponds to the English simple past (did, worked, went …).
#It talks about completed, sequential or one-time actions that took place on a specific occasion.
#Passe compose är perfekt (har gjort) och ibland imperfekt (gjorde) 
#imparfait: is similar to the English past progressive (was doing, were working …) or the structures used to and would.
#It sets the scene, gives background description and expresses past actions that were repeated over time.
#Imperfekt  
etreimparf= {'jag var': "j'étais", 'du  var': 'tu étais', 'han var': 'il était', 'vi var': 'nous étions', 'ni var': 'vous étiez',
             'de var (m)': 'ils étaient', 'passe compose être': 'été', 'jag strosade': 'je me baladais',
             'jag hade lust': "j'avais envie", 'det räckte': 'il suffisait'}
#nedanstående sätts ihop med avoir för att bilda  passé composé, typ j'ai compris
passecomposeverb= {'arresterad': 'interpellé', 'stulen': 'dérobé', 'tagen': 'pris', 'upptäckt': 'découvert', 'var väpnad': 'armé', 'skickade': 'envoyé',
                   'was hospitalised' : 'hospitalisé', 'was hurt':'blessé', 'returned': 'rendu', 'flew':'volé', 'knew': 'connu', 'lämnade över': 'remis',
                   'var tvungen': 'dû', 'domiciled' :'domicilié', 'la': 'placé', 'hittade': 'trouvé', 'brutit': 'cassé',
                   'förstått': 'compris', 'ringde': 'téléphoné', 'reserveratt': 'réservé', 'jobbade': 'travaillè', 'slutat': 'fini', 'sålt': 'vendu'}
#verb som slutar på er blir oftast é i passé composé
#verb som slutar på ir blir oftast i passé composé
#verb som slutar på re blir otast u passé composé
#Infiitiv = verbets grundform

# Kapitel 6
enforme= {'i form': 'en forme', 'inget särskilt': 'rien de spécial', 'en artikel': 'un article', 'mannen': "l'homme", 'sakna något': 'manquer de quelque chose',
          'motion': 'exercice', 'missbruka': 'abuser de', 'hälsan': 'la santé', 'lida': 'souffrir', 'en sjukdom': 'une maladie', 'civilisationen': 'la civilisation',
          'välfärdssjukdom': 'les malades de civilisation', 'leda/ föra': 'mener', 'leva ett liv': 'mener une vie', 'överdriva': 'exagérer',
          'trivas bra med sig själv': 'être bien dans sa peau', 'nöjd': 'satisfait', 'inget/ ingen som helst': 'aucun', 'vad som helst': "n'importe quoi",
          'ha bråttom': 'être pressé', 'röka': 'fumer', 'hosta': 'tousser', 'oavbrutet': 'sans arrêt', 'zappa': 'zapper', 'simma': 'faire de la natation',
          'jag har köpt': "j'ai acheté", 'jag måste': 'je dois', 'kila, sticka': 'filer', 'pj då, det var värst': 'c,a alors', 'käk/ mat': 'de la bouffe', 'lätt/light': 'léger',
          'förmoda/anta': 'supposer', 'sluta!': 'arrête', 'åka ut en sväng': 'faire un tour', 'därefter/sedan': 'puis', 'lika ... som': 'aussi ... que',
          'i riskzonen': 'à risque', 'bättre förekomma än förekommas': 'mieux vaut pprévenir que guérir', 'du går mig på nerverna': "tu m'énerves", 'herråå': 'ciao'}
extra= {}
grandnord= {'ett äventyr': 'une aventure', 'långt uppe i norr': 'dans le grand nord', 'berätta': 'raconter', 'försöka': 'essayer', 'jaså?': 'ah bon', 'var då?': 'ou c,a',
            'fira': 'fêter', 'jätte liten': 'tout petit', 'en by': 'un village', 'lyckas': 'réussir', 'i alla fall': 'quand même', 'lära sig': 'apprendre',
            'det är inte självklart': "c'est pas évident", 'skratta': 'rigoler', 'nästa år': "l'année prochaine", 'vi skulle vilja': 'on voudrait', 'stormförtjust i': 'passionné de',
            'ett estetiskt program': 'une filière artistique', 'det förvånar mig': "c,a m'étonne", 'ett antal': 'un nombre', 'ett individuellt val': 'une option',
            'roa sig': "s'amuser", 'mer eller mindre': 'plus ou moins', 'en biljett': 'un billet', 'dyrare än (m pl) ': 'plus chers que', 'studentrabatt': 'tarif étudiant',
            'träffa kompisar': 'se retrouver entre amis', 'någon': "quelqu'un", 'en förfest': 'une pré-fête', 'innan man går': "avant d'aller", 'ett disco': 'une discothèque',
            'i centrum': 'au centre-ville', 'landet(inte pays)': 'la campagne', 'lägga märke till': 'remarquer', 'en bar med ett litet dansgolv': 'un bar dansant',
            'för övrigt': "d'ailleurs", 'ragga': 'draguer', 'det är färre som' : 'il y en a moins qui', 'snus': 'du tabac à chiquer', 'konstigt': 'bizarre'}
isomras= {'i lördags': 'samedi', 'igår': 'hier', 'i förrigår': 'avant-hier', 'i somras': 'cet été', 'i höstas': 'cet automne', 'i vintras': 'cet hiver', 'i våras': 'ce printemps',
          'i förra veckan': 'la semaine dernière', 'för en vecka sedan': 'il y a une semaine', 'för ett år sedan': 'il y a un an', 'för en månad sen': 'il y a un mois'}
voiretsoir= {'se': 'voir', 'jag ser': 'je vois', 'du ser': 'tu vois', 'han ser': 'il voit', 'vi ser': 'nous voyons', 'ni ser': 'vous voyez', 'de(m) ser': 'ils voient',
             'gå ut/ ta fram/ ta ut': 'sortir', 'jag går ut': 'je sors', 'du går ut': 'tu sors', 'han går ut': 'il sort', 'vi gåt ut': 'nous sortons', 'ni går ut': 'vous sortez',
             'de(m) går ut': 'ils sortent', 'förutse': 'prévoir', 'träffas': 'se voir', 'återseende': 'revoir', 'en utgång': 'une sortie',
             'sortir passe compsé, jag har gått ut': 'je suis sorti'}
#voir används också som besöka/hälsa på.
fritid= {'längdskidåkning': 'faire du ski de fond', 'gå och fiska': 'aller à la pêche', 'designa': 'dessiner', 'klättra': "faire de l'escalade", 'åka skridskor': 'faire du patinage',
         'vandra': 'faire de la randonnée', 'dyka': 'faire de la plongée', 'spela kort': 'jouer aux cartes', 'göra hantverk/bygga': 'faire du bricolage',
         'sjunga': 'chanter', 'simma': 'faire de la natation', 'spela ishockey': 'faire du hockey sur glace', 'spela fotboll': 'jouer au football', 'jogga': 'faire du jogging',
         'shoppa': 'faire les magasins', 'tjäna pengar': "faire de l'argent", 'skaffa barn': 'faire des enfents' }
extrakap6= {'har ni sportat lite': 'avez-vous fait un peu de sport', 'det är det minsta man kan säga!': 'et comment', 'häromdagen': "l'autre jour",
            'jag låg': "j'étais allongé", 'höll på att': 'en train', 'gled ur händerna på mig': "m'a échappé des mains", 'i stället för att': 'au lieu de',
            'jag böjde mig ner': 'je me suis baissé', 'jag plockade upp': "j'ai ramassé", 'hemsk': 'terrible', 'ensamheten' : 'la solitude', 'depressionen': 'la dépression',
            'stressen': 'le stress', 'en deckare': 'un roman policier', 'spänning': 'suspence'}
preps= {'à + le': 'au', 'à + la': 'à la',"à + l'": "à l'",  'à + les': 'aux', 'de + le': 'du', 'de la': 'de la', "de + l'": "de l'", 'de + les': 'des'}
    
# Kapitel 7
lalgerie= {'berätta': 'raconter', '(han) kom/anlände': 'est arrivé', 'besluta/bestämma':  'décider', 'lämna': 'quitter', 'algeriet': "l'Algérie", 'en anledning': 'une raison',
           'ekonoiskt': 'économique', 'han gifte sig': "il s'est marié", 'en städfirma': 'une enterprise de nettoyage', 'vara hemmafru': 'être femme au foyer',
           'arabiska': 'arabe', 'algerisk(m)': 'algérien', 'algerisk(f)': 'algérienne' , 'en dryck': 'un boisson', 'vi integreras': "on s'intègre", 'ett problem': 'un problème',
           'samhället': 'la société', 'främlingsfientligheten': 'la xénophobie', 'levnadsstandard': 'le niveau de vie', 'hög': 'élevé', 'säkert/naturligtvis': 'certainement',
           'som jag saknar': 'qui me manquent', 'de flesta av dem': "la plupart d'entre eux", '(här) när det gäller': 'question', 'bättre': 'mieux',
           'vart annat år': 'tous les deux ans', '(här) eftersom': 'comme', 'stor/tal rik m + f': 'nombreux nombreuse', 'en resa': 'un voyage', 'så mycket': 'tellement',
           'jag har rest': 'je suis allé', 'en morbror/farbror': 'un oncle', 'ett utbyte mellan skolor': 'un échange scolaire', 'en religion': 'une religion',
           'det viktigaste': 'le chose la plus importante', 'muslim(m)': 'musulman', 'en tro': 'une croyance', 'förlorad(m)': 'perdu', 'anklaga': 'reprocher',
           'han dog': 'il est mort'}
enalgerie= {'slutligen/tillslut': 'enfin', 'ett projekt om': 'un project sur', 'nyss (just) ha ...(+inf)': 'venir de ...', 'tillbringa': 'passer', 'ta sig tid att': 'prendre le temps de',
            'långdistanslöpning': 'endurance', 'spela tevespel': 'jouer à la console', 'ett tillfälle': 'une occasion', 'anordna/organisera': 'organiser',
            'en mottagning': 'une réception', 'bygga': 'construire', 'ha tråkigt': "s'ennuyer", 'faktiskt': 'en effet', 'de flesta': 'la plupart',
            'är inte direkt': "n'est pas tellement", 'prioritet': 'la priorité', 'vard, jobba': 'bosser', 'ett café med tobaksförsäljning': 'un bar tabac',
            'en stil/sort': 'un style', 'i allmänhet': 'en général', 'utanför/vid sidan om': 'en dehors de', 'en slöja': 'un voile', 'däremot': 'par contre',
            'en majoritet': 'une majorité', 'bättre': 'meilleur', 'helt enkelt': 'simplement', 'bekymra sig': "s'inquiéter", 'hoppas': 'espérer',
            'medans jag väntar': 'en attendant', 'hälsa till': 'passer le bonjour à' , 'kram': "je t'embrasse", 'en kopia': 'une copie', 'otålighet': 'impatience',
            'ett stipendiium': 'une bourse'}
#rörelseverb bildar passé comopsé med hjäpverbet être, t.ex aller, venir, arrier, partir, entrer, sortir, rentrer, monter, descendre,
#tomber, naître (födas), mourir (dö) 
passecompaller= {'jag gick/åkte/har gått/åkt': 'je suis allé(e)', 'du gick/åkte har gått/åkt': 'tu es allé(e)', 'han gick/åkte har gått/åkt': 'il est allé',
                 'hon gick/åkte har gått/åkt': 'elle est allée', 'man gick/åkte har gått/åkt': 'on est allé', 'vi (m) gick/åkte har gått/åkt': 'nous sommes allés',
                 'vi (f) gick/åkte har gått/åkt' : 'nous sommes allées', 'ni (m sing, f sing) gick/åkte har gått/åkt' : 'vous êtes allé allée',
                 'ni (m pl, f pl) gick/åkte har gått/åkt': 'vous êtes allés allées', 'de (m) gick/åkte har gått/åkt': 'ils sont allés',
                 'de (s) gick/åkte har gått/åkt': 'elles sont allées', 'han kom': 'il est venu', 'hon kom': 'elle est venue' }
#passé composé negation: ne ... pas placeras runt hjälpverbet avoir eller etre. t.ex ja n'ai pas rigolé
liredire= {'läsa': 'lire', 'jag läser': 'je lis', 'du läser': 'tu lis', 'han läser': 'il lit', 'vi läser': 'nous lisons', 'ni läser': 'vous lisez', 'de(m) läser': 'ils lisent',
           'säga': 'dire', 'jag säger': 'je dis', 'du säger': 'tu dis', 'han säger': 'il dit', 'vi säger': 'nous disons', 'ni säger': 'vous dites',  'de (m) säger': 'ils disent',
           'passe comp läsa, jag har läst': "j'ai lu", 'passe compose säga, jag har sagt': "j'ai dit" ,
           'läsa om': 'relire', 'välja': 'élire', 'väljare': 'électeur', 'förbjuda': 'interdire', 'man skulle kunna tro att': "on dirait qu'"}
extrakap7= {'sticka': 'faire du tricot', 'ett krig': 'une guerre', 'bli dödad': 'est tué', 'en kyrkogård': 'un cimetière', 'en frisör': 'un coiffeur',
            'en kille som raggar på tjejer': 'dragueur', 'en öppen spis': 'une cheminée', 'det är nog fint': 'c,a doit être beau', 'likadant': 'pareil',
            'vi hugger den': 'on le coupe', 'skogel': 'la forêt', 'en figur': 'un personnage', 'den heliga familjen': 'la sainte famille', 'klä ut sig': 'se déguiser',
            'enorm': 'copieux', 'en måltid': 'un repas', 'hobbyer': 'loisirs', 'jag saknar dig': 'tu me manques', 'de skulle vilja bosätta sig': 'ils voudraient venir habiter',
            'att tundervisa': 'enseigner', 'handikappade': 'les handicapés', 'att hantera': 'se débrouiller', 'utesluten': 'exclu',
            'att kopiera': 'copier', 'imponera på': 'impressionner', 'spontanitet': 'spontanéité',
            'öppen': 'ouverts', 'snäll': 'gentils', 'blyg': 'timides', 'ingen är': "personne n'est", 'fyrkant eller km2' : 'carré',
            'de (m) var (imperfekt': 'ils étaient', 'den enda som bar': 'les seuls à porter'}
#Ingen bildas av personne + ne vid verbet
mener= {'leda': 'mener', 'jag leder': 'je mène', 'du leder': 'tu mènes', 'han leder': 'il mène',
        'vi leder': 'nous menons', 'ni lever': 'vous menez', 'de (m) leder': 'ils mènent', 'överdriva': 'exagérer',
        'jag överdriver': "j'exagère", 'du överdriver' : 'tu exagères', 'han överdriver': 'il exagère',
        'vi överdriver': 'nous exagérons', 'ni överdriver': 'vous exagérez', 'de (m) överdriver': 'ils exagèrent'}
#aimer, détester, adorer, préférer följs av besä. form. tex. j'aime les chats, je déteste le café
#att vara född i: née en . Tex, je suis née en 2000

#Kapitel 1 genial 3
trespeople= {'mycket intresserad av kändisar': 'très people', 'skvallerpressen': 'la presse people', 'en frisör m': 'un coiffeur', 'känd': 'célèbre',
             'en skådespelare': 'un acteur', 'en skådespelerska': 'une actrice', 'en sångare': 'un chanteur', 'en sångerska': 'une chanteuse', 'född(m)': 'né',
             'en spelare (m)': 'un joueur', 'ett lag': 'une équipe', 'järn': 'fer', 'en regissör': 'un metteur en scène', 'har blivit': 'est devenu', 'kunglig': 'royal'}
kiffer= {'vard. gilla': 'kiffer', 'en grej': 'un truc', 'botten/värdelös(m)': 'nul', 'däremot': 'par contre', 'reklam': 'la publicité', 'bara' : 'ne ... rien',
         'ett program': 'une émission', 'vard. fånig': 'débile', 'dokusåpor': 'la télé réalité', 'jag blir': 'je deviens', 'vard. beroende': 'accro',
         'en tecknad serie': 'un dessin animé', 'vad spelar det för roll?': "qu'importe", 'tillbringa': 'passer', 'hel': 'entier', 'anse/tycka': 'trouver',
         'förnedrande': 'humiliant', 'en mening/åsikt': 'un avis', 'och sedan': 'et puis', 'dessutom': 'en plus', 'avbrytas av': 'être coupé par',
         'en gång i timmen': 'une fois par heure', 'döda': 'tuer', 'framför allt/ särskillt': 'surtout', 'ett spel/ en lek': 'un jeu', 'missa': 'rater',
         'inte någon, inte något': 'ne ... aucun', 'annars': 'sinon', 'det värsta': 'le pire', 'en idiot': 'un crétin', 'det är illa/alvarligt': "c'est grave",
         'verklig': 'réel', 'hur som helst/i varje fall': 'de toute fac,on', 'eller lixom': 'ou quoi', 'full av': 'plein de', 'förstöra': 'gâcher',
         'en stämning': 'une ambiance', 'och så är det bra': 'et puis voilà', 'den som': 'celui qui'}
extra31= {'jag struntar i det': "je m'en fous", 'tröttsamt': 'fatigant', 'en tonåring': 'un adolescent', 'oroandee': 'inquiétant', 'toppen': 'chouette',
          'skvaller': 'les potins', 'en förstasidesrubrik': 'une manchette', 'ett jobb': 'un boulot', 'var snälla': 'soyez sages', 'påslagen': 'allumé',
          'utom': 'sauf', 'kommunal musikskola': 'un conservatorie', 'dubbelvikt av skratt': 'écroulé de rire', 'simning': 'la natation',
          'friidrott': "l'athlétisme", 'det luktar': 'c,a sent', 'märkeskläder': 'les vêtements de marque'}
#Två former av futurum
# 1: le futur proche
# använder presens av aller som hjälpverb + infinitiv av verbet
# ex. Je vais rentrer demain
#används inm närliggande, planerad tid, jämförs med engelskans 'be going to'

#2: le futur simple
#infinitiv + ändelse
# ex. je rentrerai un jour

#Futurum av regelbundna verb:
futursimple= {'jag kommer prata': 'je parlerai', 'du kommer prata': 'tu parleras', 'han kommer prata': 'il parlera', 'vi kommer prata': 'nous parlerons',
              'ni kommer prata': 'vous parlerez', 'de (m) kommer prata': 'ils parleront', 'jag kommer att sluta': 'je finirai', 'du kommer att sluta': 'tu finiras',
              'han kommer att sluta': 'il finira', 'vi kommer att sluta': 'nous finirons', 'ni kommer att sluta': 'vous finirez', 'de (m) kommer att sluta': 'ils finiront',
              'jag kommer att sälja': 'je vendrai', 'du kommer att sälja': 'tu vendras', 'han kommer att sälja': 'il vendra', 'vi kommer att sälja': 'nous vendrons',
              'ni kommer att sälja': 'vous vendrez', 'de (m) kommer att sälja': 'ils venront'}
futursimple2= {'kommer ha -' : 'aur-', 'kommer veta/kunna': 'saur-', 'kommer vilja': 'voudr-', 'kommer komma': 'viendr-', 'kommer vara': 'ser-',
               'kommer kunna': 'devr-', 'kommer ta emot': 'recevr-', 'kommer skriva': 'écrir-',
               'kommer att bli': 'deviendr-', 'kommer göra': 'fer-', 'kommer kunna': 'pourr-',
               'kommer se': 'verr-', 'kommer ta': 'prendr-', 'kommer gå/åka': 'ir-',
               'je - ': 'ai', 'tu' : 'as', 'il': 'a', 'nous': 'ons', 'vous': 'ez', 'ils': 'ont', 'kommer behöva': 'devr-'}
vivredevoir= {'jag lever': 'je vis', 'du lever': 'tu vis', 'han lever': 'il vit', 'vi lever': 'nous vivons', 'ni lever': 'vous vivez', 'de (m) lever': 'ils vivent',
              'jag måste/ är tvungen att': 'je dois', 'du måste/ är tvungen att': 'tu dois', 'han måste/ är tvungen att': 'il doit', 'vi måste/ är tvungna att': 'nous devons',
              'ni måste/ är tvungna att': 'vous devez', 'de (m) måste/ är tvungna att': 'ils doivent', 'leva passe compose, jag har bott': "j'ai vécu",
              'futurum leva': 'je vivrai', ' måste passe compose, jag var tvungen': "j'ai dû", 'futurum behöva': 'je devrai'}
trestendence= {'några ungdomar går ut tsm': 'les sorties en bande', 'lektionerna': 'les cours', 'gärna': 'volontiers', 'ett bakverk': 'une pâtisserie',
               'en våffla': 'une geufre', 'en munk': 'un beignet', 'ett mellanmål': 'un goûter', 'vard. typ': 'quoi', 'stanna kvar': 'rester', 'skolmatsalen': 'la cantine',
               'en måltid': 'un repas', 'hur dags?': 'vers quelle heure', 'en fest': 'une soirée', 'först': "d'abord", 'gå hem': 'rentrer', 'lämna sina grejer': 'poser ses affaires',
               'jo': 'si', 'överkomlig, rimlig': 'abordable', 'sedan': 'ensuite', 'inte så värst': 'pas trop', 'ibland' : 'de temps en temps', 'sedan': 'ensuite',
               'utanför': 'en dehors de', 'innebära': 'poser', 'efter att ha druckit' : 'après avoir bu', 'stiga upp': 'se lever', 'här. hämta': 'chercher',
               'i så fall' : 'alors là', 'till': "jusqu'à", 'gryningen': 'le petit matin', 'erbjuda': 'offrir', 'åka hem till sig': 'rentrer chez eux', 'ett tidsfördriv': 'un passe-temps',
               'egentligen' : 'en effet', 'ladda ner': 'télécharger', 'rabatt(er)' : 'des réductions', 'en tonåring': 'un adolescent'}
passecomp= {'åkt': 'suis allé', 'hafrt': 'eu', 'druckit': 'bu', 'förstått': 'compris', 'sagt': 'dit', 'skrivit' : 'écrit', 'varit': 'été', 'ggjort': 'fait', 'lagt' : 'mis',
            'gett sig iväg': 'suis parti', 'kunnat': 'pu', 'tagit': 'pris', 'skrattat': 'ri', 'jobbat': 'travaillé', 'slutat': 'fini', 'sålt': 'vendu', 'levt': 'vécu', 'var tvungen': 'dû',
            'läst': 'lu', 'gått ut': 'sorti', 'sett': 'vu', 'kommit': 'venu', 'kunnat(kunskap)': 'su', 'lämnade tillbaka': 'revenu'}

# kap 2 genial 3
lafrancophinie= {'den fransktalande världen': 'la francophonie', 'schweiz': 'la Suisse', 'vansinnigt/förbaskat': 'vachement', 'vinna': 'ganger', 'en vistelse' : 'un séjour',
                 'en tävling': 'un concours', 'nöjd': 'content', 'långtråkig': 'ennuyeux', 'en klocka': 'une horlonge', 'en ko': 'une vache', 'i knäbyxor': 'en clouette',
                 'joddlande': 'faisant des tyroliennes', 'nåja nåväl': 'enfin', 'hel': 'entier', 'oförglömmelig': 'inoubliable', 'som har lärt mig': "qui m'ont appris",
                 'ett schema': 'un emploi du temps', 'fyllt, späckat': 'chargé', 'en vinnare' :'un gagnant', 'te med' : 'emmener', 'efter att ha lämnat vårt bagage':
                 'après avoir posé nos bagages', 'en linbana' :'un téléphérique', 'en vandring': 'une randonnée', 'ovanför': 'au-dessus de',
                 'ett moln': 'un nuage', 'en utsikt' : 'une vue', 'en flod': 'une rivière', 'jag svär/jag lovar dig': 'je te jure', 'på vägen/under resan': 'en route',
                 'till och med' : 'même', 'höra': 'entendre', 'slut/dödstrött' : 'crevé', 'få någon att tappa andan': 'couper le souffle à qn',
                 'snömannen i himalaya': 'le yeti', 'en lavin': 'une avalanche', 'en klyfta': 'une crevasse', 'falla' : 'tomber', 'en rysning': 'un frisson',
                 'pröva på/våga sig på': 'tenter', 'ett klot/en kula': 'une boule', 'jättejätte stor/gigantisk': 'géant', 'gå ner/åka ner': 'descendre',
                 'en kulle': 'une colline', 'berg och dahl bana': 'des montagnes russes', 'en favorit': 'un coup de coeur', 'starta/sätta igång': 'démarrer',
                 'man måste': 'il faut', 'där uppe': 'en haut', 'genom att använda': 'en utilisant', 'hoppa': 'sauter', 'dyka': 'plonger', 'en rutschbana': 'un toboggan',
                 'det bästa': 'le top', 'glida/halka': 'glisser', 'nere': 'en bas', 'en avfärd': 'un départ', 'ledsen/sorglig': 'triste',
                 'ingen': 'ne ... personne', 'ett verktyg': 'un outil', 'ett armbandsur': 'une montre'}
parleunpeu= {'spännande': 'passionnant', 'jättehäftigt': 'trop cool', 'underbart/toppen': 'sensass', 'livsfarligt' : 'mortel', 'förskräckligt/förfärligt': 'affreux',
             'skrämmande/hemskt': 'effrayant', 'ansträngande/påfrestande': 'épuisant', 'uttröttande': 'fatigant', 'kolla/ta reda på': 'se renseigner',
             'ett hörn': 'un coin', 'ett ställe' : 'un endroit', 'en älg': 'un élan', 'ett uteställe': 'une sortie', 'en secondhandbutik' : "un magasin d'occasion",
             'skicklighet': 'savoir-faire', 'vissla': 'siffler', 'åka vattenskidor': 'faire du ski nautique', 'köra': 'conduire' }
connaitsavoir= {'känna/känna till': 'connaître', 'jag känner': 'je connais', 'du känner': 'tu connais', 'han känner': 'il connaît',
                'vi känner': 'nous connaissons', 'ni känner': 'vous connaissez', 'de (m) känner': 'ils connaissent' , 'passé composé connaître': "j'ai connu", 'futrum connaître': 'je connaîtrai',
                'kunna/veta': 'savoir', 'jag vet': 'je sais', 'du vet': 'tu sais', 'han vet': 'il sait', 'vi vet' : 'nous savons', 'ni vet' : 'vous savez', 'de (m) vet': 'ils savent',
                'passé composé savoir': "j'ai su", 'futurum savoir': 'je saurai', 'känna varandra': 'se connaître'}
idiotjesuis= {'åka igenom/via': 'passer par', 'på tillbakavägen': 'au retour', 'praktik/en kurs': 'un stage', 'lyckas med': 'réussie à' ,
              'jag skulle vilja': "j'amerais", 'skulle ni kunna': 'pourriez-vous', 'lätt': 'facile', 'långt ifrån': 'loin de', 'man måste': 'il faut',
              'varje': 'chaque', 'ett kvarter/ stadsdel': 'un quartier', 'ett turistkort/ turistbiljett': 'une carte touristique',
              'gälla': 'être valable', 'toppen': 'chouette', 'dröm': 'rêve', 'helt ensam': 'tout seul', 'bara': 'ne ... que', 'göra någon sällskap/ följa med': 'accompagner qn',
              'inte mycket': 'pas grand-chose', 'verka, se ut': "avoir l'air", 'sedan födsel': 'de naissance', 'montrealbo': 'Montréalais', 'till din tjänst': 'à ton service',
              'en massa': 'des tas de', 'förmodligen': 'probablement', 'minst/åtminstone': 'au moins', 'låt oss gå' : 'on y va', 'ett torn': 'une tour',
              'verkligen': 'vraiment', 'imponerande': 'impressionnant', 'otrolig': 'incroyable', 'avsluta': 'terminer', 'olympiska spelen': 'Les Jeux Olympiques',
              'det betyder' : 'c,a veut dire', 'ingen kunde se det': "personne n'a pu la voir" , 'antagligen/ nog': 'sans doute', 'det menar du inte!' : 'sans blague',
              'en hamn': 'un port', 'i allafall': 'quand même', 'som räknas': 'qui compte', 'dum': 'bête', 'missa': 'rater', 'lugna dig': 'calme-toi',
              'en teaterpjäs': 'une pièce de théâtre', 'pommes frites': 'des frites', 'en typ BBQ sås': 'une sauce style BBQ'}
extra32= {'skämt': 'farce', 'ren': 'caribou', 'rödluvan': 'le petit Chaperon rouge', 'en stjärna': 'une étoile', 'ett slott': 'un château', 'likna': 'ressembler',
          'före detta': 'ancien', 'en glasblåsare': 'un souffleur de verre', 'ett glasbruk': 'une verrerie', 'en glasfabrik' : 'une usine de verre',
          'moderlandet (frankrike)': 'métropole', 'blandspråk': 'créole', 'brådskande': 'urgent', 'bli sjuk': 'tomber malade', 'jag saknar det': 'c,a me manque',
          'klara sig (själv)' : 'de débrouiller', 'upptäcka': 'découvrir', 'en gummibåt' : 'un zodiac', 'ett mangroveträsk': 'un palétuvier',
          'köra': 'piloter', 'avkoppling' : 'détente', 'körkort': 'permis', 'jätte-': 'géant', 'sand': 'sable', 'att åka upp för en flod': "une remontée d'une rivière",
          'en björn': 'un ours'}

# Kapitel 3
pyrenees= { 'tack vare': 'grâce à', 'ett stipendium' : 'une bourse', 'hon skriver': 'elle écrit', 'före detta': 'ancien', 'en liten hälsning': 'un petit mot',
            "jag lär mig": "j'apprends", 'en sak': 'une chose', 'i början': 'au début', 'det var': "c'était", 'förstå' : 'comprendre', 'vara belägen' : 'être situé',
            'det händer att': 'il arrive que', 'försöka': 'essayer', 'klättra': 'grimper', 'en vägg': 'un mur', 'en skolvakt': 'un surveillant',
            'en ringsignal': 'une sonnerie', 'en sovsal': 'un dortoir', 'göra upprop': "faire l'appel", 'en rast': 'une récréation', 'börja om': 'recommencer',
            'jobbig/svår': 'dur', 'en energikaka': 'une barre de céréales', 'mer eller mindre': 'plus ou moins', 'en läxa': 'un devoir', 'lägga sig': 'se coucher',
            'föra oväsen': 'faire du bruit', 'fritid': 'les loisirs', 'på nedrevåningen': 'en bas', 'alltså': 'donc', 'sportig': 'sportif', 'flera, många': 'plusieurs',
            'längdskidåkning': 'le ski du fond', 'de var': 'ils étaient', 'en värdfamilj' : "une famille d'accueil", 'ofta': 'souvent', 'en anteckning': 'une note',
            'anteckna': 'prendre des notes', 'där': 'là', 'ett ämne': 'une matière', 'inte alls': 'pas du tout', 'en tanke': 'une pensée', 'toaletten': 'les toilettes',
            'komma försent': 'être en retard', 'skriven': 'écrit', 'alla helgons dag': 'la Toussaint', 'hälsa på': 'voir', 'utgöra en del av': 'faire partie de',
            'roa sig': "s'amuser", '(ung.) kram': 'je vous embrasse', 'en ledare m': 'un moniteur', 'en ledare f': 'une monitrice', 'förvåna sig': "s'étonner",
            'hos': 'auprès de', 'som tar emot': 'accueilllant', 'gruppera': 'grouper', 'på ett avstånd av': 'éloigné de', 'ett trettiotal': 'une trentaine de',
            'de kommer att ha lärt sig': 'ils auront appris'}
extra33= {'en latmask': 'un cancre', 'förhöra': 'questionner', 'sudda ut': 'effacer', 'en snara/fälla': 'un piège', 'ett hot': 'une menace', 'läraren': 'le maître',
          'en utvisslling/ burop': 'une huée', 'ett underbarn': 'un enfant prodige', 'en krita' : 'une craie', 'olycka': 'malheur', 'utantill': 'par coeur',
          'underteckna ett intyg om frånvaro': "signer un mot d'absence", 'en kamp': 'un combat', 'brasiliansk': 'brésilien', 'det tar bort stressen/ det lugnar mig':
          'c,a me déstresse', 'ta studenten': 'réussir son bac', 'en dagbok': 'un journal intime', 'törnrosa': 'la belle au bois dormant', 'stående': 'debout',
          'sova utomhus': 'dormir à la belle étoile', 'sova som en stock': 'dormir comme un loir', 'lång rund stenhård kudde': 'un traversin',
          'ha sovmorgon': 'faire la grasse matinée', 'älskling': 'chéri', 'korrekt klädsel': 'la tenue correcte', 'urringad': 'décolletée'}
faisgaffe= {'akta/ se upp': 'fais gaffe', 'köra': 'conduire', 'vid ratten': 'au volant', 'starta': 'démarrer', 'en gång': 'une fois', 'få motorstopp': 'caler',
            'efter, i slutet av': 'au bout de', 'växla': 'changer de vitesse', 'hastigheten/farten':  'la vitesse', 'några': 'quelques', 'en dumhet/tokighet': 'une bêtise',
            'förbli': 'rester', 'fungera': 'marcher', 'en hjärtattack': 'une crise cardiaque', 'en broms': 'un frein', 'en sten': 'une pierre' ,'slå emot/ kollidera med ngt':
            'heurter', 'ett däck': 'un pneu', 'insistera på att': 'insister pour', 'låta': 'laisser', 'bromsa': 'freiner', 'häftigt': 'brusquement', 'slå(emot)': 'frapper',
            'en vindruta': 'un pare-brise', 'övningskörning': 'la conduite accompagnée', 'vilken tur': 'quelle chance', 'lugnt': 'doucement', 'såra/skada': 'blesser',
            'backa': 'faire marche arrière', 'när jag gjorde det (eg. görande)': 'en le faisant', 'igen': 'de nouveau', 'mitt fel': 'de ma faute', 'skulle kunna': 'pourrait',
            'visa sig': 'se montrer', 'en vägkorsning': 'un carrefour', 'bli rasande': 'se mettre en colère', 'på samma gång': 'en même temps',
            'runt omkring': 'autour de', 'plötsligt': 'soudain', 'högerregeln': 'la priorité à droite', 'kopplingen': 'la embrayage'}
ecriredormir= {'skriva': 'écrire', 'jag skriver': "j'écris", 'du skriver': "tu écris", 'han skriver': 'il écrit', 'vi skriver': 'nous écrivons', 'ni skriver': 'vous écrivez',
               'de skriver m ': 'ils écrivent', 'sova': 'dormir', 'jag sover': 'je dors', 'du sover': 'tu dors', 'han sover': 'il dort', 'vi sover': 'nous dormons', 'ni sover': 'vous dormez',
               'de sover': 'ils dorment', 'passé composé skriva': "j'ai écrit", 'futurum skriva': "j'écrirai", 'passé composé sova': "j'ai dormi", 'futurum sova': 'je dormirai'}

#Kapitel 4
portesouverts= {'öppet hus': 'portes ouvertes', 'mycket nära': 'à deux pas', 'inom räckhåll': 'à portée de main', 'en affär': 'un commerce',
                'en köttaffär': 'une boucherie', 'en blomsterhandlare': 'un fleuriste', 'färsk m': 'frais', 'färsk f': 'fraîche', 'en alags bulle med bärlsocker': 'une choquette',
                'en doft/lukt': 'une odeur', 'överallt': 'partout', 'handla': 'faire les courses', 'varje lördagsmorgon': 'tous les samedis matins',
                'ett salutorg': 'un marché', 'vi tar fram': 'on sort', 'en shoppingvagn': 'un caddie', 'en restaurang/brasseri/cafe': 'une brasserie', 'en krog': 'un bistro',
                'en lindansare': 'un funambule', 'ha lust att': 'avoir envie de', 'eller också': 'ou bien', 'gå ut o gå': 'se balader', 'träffa' : 'rencontrer', 'nedanför': 'en bas de',
                'en fastighet': 'un immeuble', 'ett centrum': 'un foyer', 'nordafrikansk': 'maghrébin', 'sjunde': 'septième', 'en våning': 'un étage', 'en hiss': 'un ascenseur',
                'städa': 'faire le ménage', 'en bostad med subventionerad hyra': 'une HLM', 'för, ty': 'car', 'en hyra': 'un loyer', 'låg m f': 'bas basse', 'olyckligtvis':
                'malheureusement', 'ta emot': 'recevoir', 'hälsa på någon': "venir voir quelq'un", 'för det mesta': 'la plupart du temps', 'en bäddsoffa': 'un canapé clic-clac',
                'ett skrivbord': 'un bureau', 'i alla fall': 'quand même' ,'utrustad': 'equipé', 'en tvättmaskin': 'un lave-linge séchant', 'en diskmaskin': 'un lave-vaisselle',
                'slå sig ned': "s'installer", 'lugn': 'tranquille'}
extra34= {'ungdomsgården': 'la masion des jeunes', 'utnyttja': 'profiter de', 'vara pensionerad' : 'être à la retraite', 'adlig': 'noble', 'oumbärlig': 'indispensable',
          'värmebölja': 'canicule', 'flytta': 'déménager', 'ett radhus': 'une maison mitoyenne', 'trafik': 'circulation', 'man lever': 'on vit', 'ett kulturevenemang':
          'un événement culturel', 'en förstad med höghusområden': 'une cité', 'så snart som möjligt': 'dès que possible', 'bli irriterad': "s'énerver",
          'nöjen': 'distractions', 'en etta': 'un studio', 'jag går/ kör vilse': 'je me perds', 'ett trappsteg': 'une marche', 'ett palats': 'un palais', 'en skomakare':
          'un cordonnier', 'som hon föredrog': 'qui eut sa préférence', 'sätta på skor': 'chausser', 'friade': 'fit sa demande', 'vi skulle sova': 'nous dormirions',
          'en dubbelsäng': 'un grand lit', 'täckt': 'couvert', 'en pärla': 'une perle', 'vintergröna': 'pervenche', 'mitten': 'le mitant', 'skulle kunna': 'pourraient' ,
          'tankspridd': 'étourdi', 'vifta på svansen': 'remuer la queue'}
rire= {'skratta': 'rire', 'jag skrattar': 'je ris', 'du skrattar': 'tu ris', 'han skrattar': 'il rit', 'vi skratar': 'nous rions', 'ni skrattar': 'vous riez', 'de m skrattar': 'ils rient',
       'passé composé skratta': "j'ai ri", 'futurum skratta': 'je rirai'}
sdf= {'gå utför/ ramla utför': 'dégringoler', 'är jag' : 'me voici', 'tigga': 'faire la manche', 'hjärtlig': 'cordial', 'bland dem': 'parmi elles', 'människor/folk': 'des gens',
      'en egenskap': 'une qualité', 'idiotisk': 'con', 'spotta': 'cracher', 'ansiktet': 'la figure', 'komma över/besegra': 'surmonter', 'olycka': 'malheur', 'jag hade': "j'avais",
      'allt som behövs': "tout ce qu'il faut", 'jag arbetade': 'je travaillais', 'ett tryckeri': 'une imprimerie', 'för ... sedan' : 'il y a', 'avskeda': 'licencier', 'jag förlorade':
      "j'ai perdu", 'lämna': 'quitter', 'köra ut': 'foutre à la porte', 'nåja': 'bon, ben', 'erkänna': 'reconnaître', 'begränsa sig': 'se limiter', 'bli berusad': "s'enivrer",
      'hejda sig/stanna': "s'arrêter", 'dricka sig full': 'se soûler', 'en hemlös': 'un sans domicile fixe', 'se mörkt på': 'voir mal', 'dålig': 'mauvais',
      'ett hål': 'un trou', 'ingen': 'ne ... personne', 'hjälpa': 'aider', 'ta med sig': 'apporter', 'det viktigaste': 'le principal', 'tillåta': 'permettre', 'moralen': 'le moral',
      'hålla modet uppe': 'garder le moral'}
croire= {'tro': 'croire', 'jag tror': 'je crois', 'du tror': 'tu crois', 'han tror': 'il croit', 'vi tror': 'nous croyons', 'ni tror': 'vous croyez', 'de m tror': 'ils croient',
         'passé composé tro': "j'ai cru", 'futurum tro': 'je crorai'}

# Kap 5

congo= {'ett inbördeskrig': 'une guerre civile', 'död': 'mort', 'freden': 'la paix', 'ett hörn': 'un coin', 'lidit': 'souffert', 'ett krig': 'une guerre', 'tegel': 'brique',
        'hälsa välkommen': 'souhaiter la bienvenue', 'skälla': 'aboyer', 'självklar': 'évident', 'föräldralös': 'orphelin', 'en jägare': 'un chasseur',
        'ett samvete' : 'une conscience', 'en höna': 'une poule', 'en deg': 'une pâte' , 'ett blad': 'une feuille', 'kandidat': 'licencié', 'juridik': 'le droit',
        'ta hand om': "s'occuper de", 'arbetslöshet': 'chômage', 'förlorade': 'a perdu', 'en strid': 'une lutte', 'rinnande vatten': "l'eau courante",
        'torr x2': 'sec sèche', 'en skugga': 'une ombre', 'vägkanten': 'le bord de la route', 'från vägkanten': 'du bord de la route', 'en träff': 'un rendez-vous',
        'en blus': 'un chemisier', 'förtjäna': 'mériter', 'jättetrevlig/jättesnäll': 'gentil, le comme tout', 'nyss ha gjort något': 'venir de faire quelque chose',
        'ha bråttom': 'être pressé', 'sopa': 'balayer', 'diska': 'faire la vaiselle', 'vila sig': 'se reposer' , 'tacksam': 'reconnaissant', 'jag skulle kunna': 'je pourrais',
        'skicka/sända' : 'envoyer', 'en hjältinna': 'une héroïne', 'här: göra': 'rendre', 'ensamhet': 'solitude'}
extra35= {'tröskeln': 'le pas de la porte', 'godmodighet': 'bonhomie', 'blomstrande/framgångsrik': 'prospère', 'sväva': 'flotter', 'sjuda': 'mijoter',
          'flyta förbi': "s'écouler", 'förflyta': 'se dérouler', 'själen f': "l'âme" , 'en träskomakare': 'un sabotier', 'en dödgrävare': 'un fossoyeur', 'tofflor': 'des pantoufles',
          'cider': 'du cidre', 'ett kar': 'un tonneau', 'en press': 'un pressoir', 'en kille': 'un mec', 'vända sig mot': 'se tourner vers', 'klara sig' : 'se débrouiller',
          'ett drag': 'un jeu', 'röra på/ vifta på': 'remuer', 'svansen': 'la queue', 'snäll, lydi': 'sage'}
        #verb med Ackusativ : écouter qn/qc, regarder qn/qc
          #verb med dativ: écrire à qn, parler à qn
          #de npersonen man gör något till kallas dativobjekt . Istället för preposition + substantiv kan man använda ett pronomen .
          #Obs! man får inte ha någon preposition (till, för, åt) när man använder sig av ett dativobjekt. Prepositionerna är redan inbakade i me, te, lui, nous, vous, leur.
voir= {'se': 'voir', 'jag ser': 'je vois', 'du ser': 'tu vois', 'han ser': 'il voit', 'vi ser': 'nous voyons', 'ni ser': 'vous voyez', 'de m ser': 'ils voient', 'passé compose se':
       "j'ai vu", 'futurum se': 'je verrai', 'få, erhålla': 'recevoir', 'jag får': 'je rec,ois', 'du får': 'tu rec,ois', 'han får': 'il rec,oit', 'vi får': 'nous recevons', 'ni får': 'vous recevez',
       'de m får': 'ils rec,oivent', 'passé composé få/erhålla': "j'ai rec,u", 'guturum få erhålla': 'je recevrai'}
barry= {'det var en gång': 'il etait une fois', 'en saga': 'un conte de fées', 'ett kloster': 'un monastère', 'ett bergspass': 'un col', 'en gräns': 'une frontière',
        'innehålla': 'contenir', 'en handling': 'un acte', 'en räddning': 'un sauvetage', 'genom': 'à travers', 'snön': 'la neige', 'dimman' : 'le brouillard', 'rädda': 'sauver',
        'mer än': 'plus de', 'döden': 'la mort', 'ana/ känna på sig': 'pressentir', 'snabbt': 'vite', 'ett ställe': 'un endroit', '(på) hjälp': 'au secours', 'den': 'celle',
        'befinna sig' :'se trouver', 'en spricka': 'une crevasse', 'återuppliva': 'ranimer', 'genom att slicka': 'en léchant', 'ett ansikte': 'un visage', 'resa sig upp igen':
        'se relever', 'kylan': 'le froid', 'ett ben': 'une jambe', 'gå/promenera': 'marcher', 'röra sig': 'bouger', 'lägga sig': 'se coucher', 'bredvid' : 'à côte de',
        'en rygg': 'un dos', 'helskinnad': 'sain et sauf', 'en kropp': 'un corps', 'stoppa upp djur': 'naturaliser', 'resa (ett monument/minnesmärke)': 'ériger'}
# Imperfekt: Beskrivande, målande tempus, Tilllstånd
    # Använder stammen plus ändelser -ais -ais -ait -ions -iez -aient
# Passé composé: Actiontempus, händelser
    #anänder hjälpverb avoir eller être

# Kapitel 6
labouffe= {'vard. mat': 'bouffe', 'ett stipendium': 'une bourse', 'överlycklig, förtjust': 'ravi', 'skaffa sig upplysningar, höra för': 'se reneigner', 'ett sätt': 'une fac,on',
           'ett varuhus': 'un grand magasin', 'smaka på/ avssmaka': 'dégusster', 'berömd': 'fameux','kött': 'viande', 'köttbullar': 'les boulette de viande',
           'ett lingon': 'une airelle', 'byta ut': 'remplacer', 'kokt potatis': 'pommes de terre vapeur', 'avdelning': 'un rayon', 'mat': 'alimentation', 'gillar du det':
           'c,a te dit', 'gärna': 'avec plaisir', 'inlagd sill': 'hareng mariné', 'dill': 'aneth', 'med dill': "à l'aneth", 'som huvudrätt': 'en plat principal', 'en älg': 'un élan',
           'pyttipanna': 'une poîlée suédoise', 'inte jag heller': 'moi non plus', 'verka/se ut': "avoir l'air", 'kaviar': 'des oeufs de poison', 'en smörgås': 'une tartine',
           'inte så mycket': 'pas grand chose', 'en skiva': 'une tranche', 'snarare, hellre': 'plutôt', 'enligt min åsikt': 'à mon avis', 'de är inte så mycket för desserter':
           "ils ne sont pas très dessert", 'en småkaka': 'un petit gâteau', 'en kanelbulle': 'une brioche à la cannelle', 'utanför': 'en dehors de', 'småäta' :'grignoter',
           'råg': 'seigle', 'en dryck': 'une boisson', 'dum': 'bête', 'ha rätt': 'avoir raison', 'surströmming': 'hareng fermenté', 'sluta upp': 'arrêter', 'skämta': 'plaisanter'}
extra36= {'stormarknader': 'les grandes surfaces', 'surdeg': 'levain', 'jäsa': 'fermenter', 'ånga': 'vapeur', 'knaprig': 'croustillant', 'klok/ förståndlig': 'raisonnable',
          'en botad': 'un logement' ,'dela': 'partager', 'en korridor': 'un couloir', 'vid slutet av': 'au bout de', 'en elplatta': 'un réchaud électrique',
          'skynda ssig': 'se dépêcher', 'en lukt/doft': 'une odeur', 'må illa': 'avoir mal au coeur', 'du har fel': 'tu as tort', 'en osthandlare': 'un fromager',
          'en ostaffär': 'une fromagerie', 'trogen': 'fidèle', 'provmaka': 'déguster', 'ekologiska ägg': 'de oeufs biologiques', 'getost': 'chèvre'}
repasinoubliable= {'oförglömlig': 'inoubliable', 'en semesterbostad på landet': 'un gîte', 'hyra': 'louer', 'åka bil': 'se promener en voiture',
                   'medans de lyssnade på': 'en écoutant', 'en utflykt/ åktur': 'une balade', 'inse/ fatta/ förtå': 'se rendre compte', 'erbjuda': 'proposer',
                   'en tävling': 'un concours', 'förklara': 'expliquer', 'varje gång': 'chaque fois', 'fin/ berömd': 'grand', 'klara sig': 'se débrouiller',
                   'en bechamelsås': 'une sauce béchamel', 'komma ihåg': 'se rappeller', 'en maträtt': 'un plat', 'vara van': "avoir l'habitude", 'gå bra': 'se passer bien',
                   'en sändning/ ett program': 'une émission', 'en kvarn': 'un moulin', 'belägen': 'situé', 'ett landskap': 'un paysage', 'ett vykort': 'une carte postale',
                   'slå sig ned': "s'installer", 'en flod': 'une rivière', 'en provsmakning': 'une dégustation', 'vattnas i munnen': "avoir l'eau à la bouche",
                   'njuta av': 'savourer', 'medan de njöt av': 'en savourant', 'en liten aptitretare': 'une amuse-bouche', 'frosseri': 'gourmandise',
                   'en finsmakare': 'un gourmet', 'hålla sig smal': 'garder la ligne', 'för en gångs sskull': 'pour une fois', 'mitt i': 'au milieu de', 'en sorbet': 'un sorbet',
                   'ett hål': 'un trou', 'en slags sorbet med alkohol': 'un trou normand', 'en storätare/läckergom': 'un gourmand', 'äta mycket och gärna': 'être très gourmand',
                   'smälta (maten)' : 'digérer', 'smakade det bra?': 'c,a a été', 'njuta/ smörja kråset': 'se régaler', 'lägga upp': 'présenter', 'tillägga': 'ajouter',
                   'ett konstverk': "une oeuvre d'art"}

                   
ffs= {'knaprig': 'croustillant', 'en bostad': 'un logement', 'skämta': 'plaisanter', 'byta ut': 'remplacer', 'överlycklig, förtjust': 'ravi', 'skaffa sig upplysningar för':
      'se reneigner', 'njuta av': 'savourer', 'medan de njöt av': 'en savourant', 'ett kloster': 'un monastère', 'återuppliva': 'ranimer', 'resa (ett monument/minnesmärke)':
      'ériger', 'en räddning ': 'un sauvetage', 'rädda': 'sauver', 'genom' : 'à travers', 'en saga': 'un conte de fées', 'ana/ känna på sig': 'pressentir',
      'en dödgrävare': 'un fossoyeur', 'flyta förbi': "s'écouler", 'tröskeln': 'le pas de la porte', 'en träskomakare': 'un sabotier', 'röra på/ vifta på': 'remuer',
      'förflyta': 'se dérouler', 'skälla': 'aboyer', 'en strid': 'une lutte', 'tacksam': 'reconnaissant', 'från vägkanten': 'du bord de la route', 'förtjäna': 'mériter',
      'bli berusad': "s'enivrer", 'idiotisk': 'con', 'ta med sig': 'apporter', 'ett tryckeri': 'une imprimerie', 'bland dem': 'parmi elles', 'jag hade': "j'avais",
      'går/ ramla utför': 'dégringoler'}
ffs2= {'ett kulturevenemang': 'un événement culturel', 'vara pensionerad': 'être à la retraite', 'en skomakare': 'un cordonnier', 'ett radhus': 'une maison mitoyenne',
       'oumbärlig': 'indispensable', 'flytta': 'déménager', 'tankspridd': 'étourdi', 'en tvättmaskin' : 'un lave-linge séchant', 'träffa' : 'rencontrer',
       'inom räckhåll': 'à portée de main', 'en lindansare': 'un funambule',
       'runt omkring': 'autour de', 'bli rasande': 'se mettre en colère', 'kopplingen': 'la embrayage', 'en vindruta': 'un pare-brise', 'visa sig': 'se montrer',
        'igen': 'de nouveau', 'efter, i slutet av': 'au bout de', 'övningskörning ': 'la conduite accompagnée', 'bromsa': 'freiner',
       'en ringsignal': 'une sonnerie', 'de kommer att ha lärt sig': 'ils auront appris', 'ett ämne': 'une matière', 'i början': 'au début',
 'på avstånd av': 'éloigné de', 'hos': 'auprès de', 'ett trettiotal': 'une trentaine de', 'som tar emot': 'accueilllant',
       'att åka upp för en flod': "une remontée d'une rivière", 'en glasfabrik': 'une usine de verre',
        'ett mangroveträsk': 'un palétuvier', 'ett glasbruk': 'une verrerie', 'moderlandet (frankrike)': 'métropole', 'ren': 'caribou'}
       

skippade= glosor(ffs)
