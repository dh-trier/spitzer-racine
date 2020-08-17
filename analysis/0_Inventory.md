L'effet de sourdine revisité: les motifs définis par Spitzer
============================================================

##  A Die Entindividualisierung (S. 136-XXX) / La "désindividualisation" (209)

### A1 "Die Entindividualisierung durch den unbestimmten Artikel (bzw. im Plural durch des)" (S. 136-142) / l'article indéfini (209)

Beispiele (Spitzer)

* "À de moindres faveurs des malheureux prétendent, / Seigneur ; c'est un exil que mes pleurs vous demandent" (Andromaque)

Queries

* A1a ([word="de"][word="les"]|[word="un.?"])[pos="noun"]
* A1b [word="de"][word="les"][pos="noun"]

Anmerkungen

* Nicht gut modelliert, weil das natürlich nur in ganz bestimmten Kontexten dem entspricht, was Spitzer hier meint. 


### A2 "Plural statt Singular", auch "des + (pluralisches) Substantiv + Relativsatz (S. 142) le pluriel au lieu du singulier / "des + substantif (pluriel) + proposition relative" (212) // "des + pluralisches Substantiv + Relativsatz (142)

Beispiele (Spitzer)

* "Je révoque des lois dont j'ai plaint la rigueur"
* "Modérez des bontés dont l'excès m'embarrasse"

Queries

* A2 [pos="det.*" & form="de"][pos="det.*"][pos="noun.*"][tag="PR.*"]

Anmerkungen

* Recht gut modelliert


### A3 "unpersönliche Ausdrucksweisen" (S. 143) "expressions impersonnelles" avec "on" (213) / unpersönliche Ausdrücke mit on

Beispiele (Spitzer)

* (viele)

Queries

* A3: [lemma="on"] (approximation)

Anmerkungen

* Nicht mehr bei Racine, sondern sogar deutlich weniger. Aber das sind natürlich nur die rohen "on"-counts. 
* Insgesamt nicht gut modelliert. 


##  B "Dämpfend, das Unmittelbare des Empfindens abschwächend wirkt auch..." (S. 144) / Affaiblissement de l'expression directe du sentiment (214)

### B1 der "distanzierend[e] Gebrauch des Demonstrativs" (S. 144) / "le démonstratif de distance" (au lieu du possessif) (214)

Beispiele (Spitzer)

* "ce fils"
* "ce fruit de sa vieillesse"
* "cette reine"

Queries

* B1 [pos="det" & lemma="ce"] [pos="noun"]

Anmerkungen

* Racine 7.7, Proches 6.5, rrf 1.17 zugunsten Racine (leicht überrepräsentiert); aber mit p-value von 0.07 nicht signifikant.


### B2 "Das umschreibende "en ces lieux" statt "ici und "ce jour" statt "aujourd'hui" (S. 147) [S05] / "les périphrases" locatives / lokative Periphrasen 

Beispiele (Spitzer)

* B2 "(en) ces lieux" / "sur ces bords" (pour "ici")

Queries

* B2a ([word="en"][word="ces"][word="lieux"]|[word="sur"][word="ces"][word="bords"])
* B2b [word="ce"][word="jour"]
* zum Vergleich [word="ici"]
* (fw) [word="en"][word="ces"][word="lieux"] 
* (fw) [word="sur"][word="ces"][word="bords"] 
* (fw) [word="ce"][word="jour"] 

* B2c [word="en|sur"][word="ce|ces"][word="lieux|bords|jour|rivages"]



Anmerkungen

* Racine verwendet "en ces lieux" und "sur ces bords" deutlich häufiger als die anderen (rrf 1,36!), das ist aber nicht statistisch signifikant. Auch bei den Proches ist eine breite Verteilung da.
* Außerdem fällt auf, dass Racine auch "ici" deutlich mehr verwendet, also gerade nicht seltener, wie von Spitzer angedeutet
* Spitzer schreibt, "ici" sei bei Racine selten; also umgekehrte Erwartung!

 
## C "hat etwas Kühl-Abgeschwächtes" (S. 150) / Affaiblissement (paradoxal) de l'expression (219)


### C1 "das beteuernde si und tant (S. 150) / "le SI d'affirmation forte": "substantif + si + adjectif" / "si + adjectif + substantif" (219)

Exemples (Spitzer)

* "des transports si charmants"
* "une si douce erreur"
* "une mort si juste"
* "des dépouilles si chères"

Queries

* C1a ([pos="noun" & type="common"][word="si" & pos="adverb"][pos="adj.*"]|[word="si" & pos="adverb"][pos="adj.*"][pos="noun" & type="common"])
* C1b [frpos="Nc.*"][word="si"][frpos="Ag|Ga"]: Racine 1.13, Proches 1.00, Autres 0.70


Anmerkungen

* Lässt sich gut modellieren.
* Hier ist nun wirklich nicht klar, inwiefern das was mit "Dämpfung" zu tun hat...


#### C2 "tant + de + substantif" (220) / das beteuernde tant

Beispiele (Spitzer)

* "entre tant de beautés" 

Queries:

* C2a [word="tant_de"][pos="noun" & type="common"] 
* C2b [word="tant_de"] [word="beauté.?"] 
* C2d [word="tant_de"][pos="noun.*"] 

Anmerkungen

* Lässt sich gut modellieren.


## D "Racine sorgt dafür, dass das Ich sich nicht zu sehr aussinge" (S. 151) / "Refrèner le chant lyrique du Moi" (221)

### D1 "Ein objektivierendes Er (Sie) [...], das mit dem Ich abwechselt" (S. 151) / il/elle objectivant (221) - alternance de moi et non-moi

* nicht modellierbar 


### D2 (war: D1a) utiliser le nom au lieu d'un pronom

Auch: "das Absehen vom empirischen Ich" (S. 154)
"sich selbst mit dem ebenso teilnahmslosen, objektiven Eigennamen nennt" (S. 154)

Beispiele (Spitzer)

* Joas: Joas ne cessera jamais de vous aimer.

Query

* nicht gut modellierbar
* Teilweise (wie im Beispiel oben) hängt das damit zusammen, dass der Sprecher von sich selbst in der dritten Person spricht, sodass man erfassen müsste, ob ein Sprecher seinen eigenen Namen nennt. In der aktuellen Annotation nicht möglich, aber eigentlich nicht schwierig. 

Anmerkungen

* Man könnte theoretisch einfach einmal schauen, ob Racine insgesamt mehr Eigennamen verwendet als die anderen. Aber das ist erstens kein sehr präziser Query, und zweitens ist die Freeling-Annotation für NP (proper nouns) unglaublich schlecht, mit vielen Funktionswörtern am Versanfang, die als NP erkannt wurden (Et, Je, etc.). Das müsste man erst optimieren, bevor das sinnvoll ist. 


### D3 (war: D2) montrer / présenter

Anmerkungen

* Das ist sehr schwierig zu identifizieren! 


##  E "[Die] Unpersönlich[keit] der Rede" (S. 157), auch beschrieben als "Das Abrücken vom Persönlichen zum Prinzipiellen hin" (S. 160)  / Dépersonnalisation du discours / De l'individuel à l'universel

### E1 "Plural majestatis" (S. 157) / pluriel de majesté (225) 

Beispiele (Spitzer)

* "Tu veux que je le fuie? Eh bien! rien ne m'arrête: / Allons, n'envions plus son indigne conquête... / Fuyons..." (Andromaque)

Queries

* [pos="verb.*" & form=".*ons"] 
* [tag="VMM01P0"]

Anmerkungen

* Nicht gut modellierbar, da precision schwierig. 
* Die beiden Queries sind nicht identisch. Und es werden natürlich alle Formen gefunden, nicht nur diejenigen, die tatsächlich ein "pluralis majestatis" enthalten. 

### E2 "terra majestatis" (S. 158) / pays de majesté

Beispiele (Spitzer)

* "L'ÉPIRE sauvera ce que Troie a sauvé" (Andromaque)

Queries

* E2a: 

Anmerkungen

* Mit der aktuellen Annotation nicht sinnvoll zu machen, außer über die konkreten Beispiele. 
* Eventuell könnte man über NEs: Länder gehen und dann ein aktives Verb im Anschluss suchen; aber die Annotation ist zu schlecht dafür. 


### E3 "Die Personifikation der Abstrakta, die an die Stelle der Personen tritt" (S. 160) / La personnification des abstraits (227) substantif abstrait + verbe subjectif ou d'action

Beispiele (Spitzer)

* "ce reste de fierté qui craint d'être importune"
* "dédaigner l'inconstance", "fléchir sa rigueur"
* "des soupirs qui craignaient"
* "désordre éternel règne"
* "chagrin inquiet l'arrache"

* Substantive: fierté, inconstance, rigueur, soupirs, désordre, chagrin, douleur, puissance, voeux, désirs, inimité, 
* Verben: craindre, dédaigner, fléchir, regner, arracher, ordonner, pousser, accorder, vouloir, 

Queries

* E3a [wnlex="noun.attribute|noun.cognition|noun.feeling|noun.communication"][word!=",|!|:|\."]{0,2}[wnlex="verb.motion"]
* E3b [lemma="fierté|inconstance|rigueur|soupirs|désordre|chagrin|douleur|puissance|voeux|désirs|inimité"][]{0,4}[lemma="craindre|dédaigner|fléchir|regner|arracher|ordonner|pousser|accorder|vouloir"]  

* Verben: craindre, dédaigner, fléchir, regner, arracher, ordonner, pousser, accorder, vouloir, 
* (fw) [lxn="[noun.attribute|noun.cognition]"][]{0,2}[lxn="verb.motion"] 
* (fw) [pos="noun*"][]{0,2}[form="qui"][]{0,2}[pos="verb"] 


### E4 Lieu comme auteur d'une action (230): lieu + verbe (230)

Beispiele (Spitzer)

* "Qui l'eût dit, qu'un rivage à mes yeux si funeste / Présenterait d'abord Pylade aux yeux d'Oreste?" (Andromaque)

Queries

* E4a [lemma="terre|monde|mer|abîme|rivage|astre|forêt|gouffre|rocher|île|fleuve|précipice|ruisseau|pente|ferme|butte|bois|rivière|seine|vallée|col|champ|étang|marais|massif|roche|endroit|lieu"][]{0,4}[wnlex="verb.motion"]

Anmerkungen

* Spitzer nennt nur ein Beispiel!
* WordNet kennt relevante Kategorien: "wnlex=noun.object" beinhaltet ein Reihe von Ortsbezeichnungen, aber auch vieles andere.
* E4a ist viel zu unpräzise, weil keine syntaktische Abhängigkeit modelliert wird 

    
### E5: Jour auteur d'une action: jour + verbe (230)

Beispiele (Spitzer)

* "Le jour qui de leurs rois vit éteindre la race / Eteignit tout le feu de leur antique audace." (Athalie)

Queries

* E5a [lemma="jour"]
* E5b [lemma="jour"], Auswahl nach Kontext

Anmerkungen

* E5a: Das bleibt natürlich sehr vage, die meisten Treffer sind "false positives".
* E5b:
* Es mangelt hier klar an einem syntaktischen Parsing und einer besseren semantischen Annotation, wie so oft. Dann könnte man "jour" in Subjektposition suchen, das passende Verb unabhängig von der Nähe dazu identifizieren und prüfen, ob es ein Handlungsverb ist.


## F - Die "Konturverwischung" (S. 163, 168) / Estomper les contours, abolir les limites (230/233)

### F1 "pluriels qui estompent les contours" (230) / konturverwischende Plurale

Beispiele (Spitzer)

* amours, fureurs, flammes, soupirs, désirs, alarmes, refus, soins

Queries

* F1a [word="amours|fureurs|flammes|soupirs|désirs|alarmes|refus|soins|mépris|retardements|attraits|vengeances|alarmes|amours|caprices|contentements|craintes|dégoûts|ennuis|haines|ingratitudes|remerciements|respects|ressentiments|souhaits|sympathies|timidités|volontés"%c]
* F1b [word="amours|fureurs|flammes|soupirs|désirs|alarmes|refus|soins|mépris|retardements|vengeances|charmes|attraits"]
* [wnlex="noun.feeling" & num="plural"]
 
Anmerkungen 

* Die Unterschiede zwischen den beiden Queries und ihren Ergebnissen sind interessant. Obwohl der zweite Query eigentlich weniger bestimmt ist als der erste, gibt es für den ersten wesentlich mehr Treffer. Das liegt daran, dass die WordNet-Annotation mal wieder wenig Abdeckung hat und unter den "noun.feeling" zwar mehr Begriffe fallen (16 statt nur 8), aber eben einige der von Spitzer erwähnten Begriffe fehlen (fureurs, flammes, soupirs, désirs, refus, soins). 
* G1 bildet die gemeinsame Liste der beiden anderen Queries ab. 


### F2 "les mots qui estompent les contours" (233) / konturverwischende Begriffe

Pas seulement expression plus noble, mais plus floue.

Beispiele (Spitzer)

* sein (pour ventre), flanc (pour ventre), lit (pour mariage), hymen (pour mariage), courroux (pour colère)

Queries

* F2a 
[word="sein|flanc|lit|lien|noeud|hymen|courroux|lien"%c] # alle von Spitzer erwähnten Wörter
* F2b [lemma="sein|flanc|lit|lien|noeud|hymen|courroux|lien"%c] # same, aber als Lemma
* F2c [word="sein|flanc|hymen|courroux"] # nur die eindeutigen Wörter
* F2d [word="lit|lien"] # nur die beiden nicht eindeutigen Wörter, und wörtliche Verwendungen händisch gelöscht; da ergibt sich ein massiver Unterschied zugunsten Racines.
   
Anmerkungen

* Das hier ist ein interessanter Fall, weil es ein Musterbeispiel für die Abweichungsstilistik ist. Jedes der Worte wird erst dadurch zum "Treffer", dass es an dieser Stelle für ein anderes stehen könnte bzw. dass eben auch das andere dort stehen könnte. Das ist schwer abzufragen. Hier gehe ich einfach davon aus, dass diese Wörter immer Treffer sind und nehme in Kauf, auch ein paar wörtliche Treffer mitzunehmen. 
   

### F3 "le neutre ce que" (233) / das neutrale ce que

Beispiele (Spitzer)

* "L'Épire sauvera ce que Troie a sauvé." (Andromaque)
* "Épouser ce qu'il hait et perdre ce qu'il aime." (Andromaque)

Queries

* F3a [word="ce_que"%c]
* F3b [][]  [][]
* F3c ([pos="verb"][]{0,1}[word="ce_que"%c]|[word="ce_que"%c][]{0,1}[pos="verb"])

Anmerkungen

* F3a: Der Type ist bei den Proches wesentlich häufiger als bei Racine! Und für ein Mal ist das auch signifikant. 
* F3b: Beschränkung auf einen Verb-Kontext vorher und nachher. Außerdem Auswahl der Beispiele von Hand. 
* F3c: Beschränkung auf einen Verb-Kontext vorher und nachher ohne Auswahl der Beispiele.
* Spitzer sagt weder genau, warum hier ein "effet de sourdine" zu verzeichnen ist, noch sagt er, wie die vielen Instanzen von "ce que" dahingehend beschrieben werden können, ob so ein Effekt erkennbar ist oder nicht. Das macht die Entscheidung schwierig, ob und wie unter den Treffern noch ausgewählt werden sollte. Eine Strategie ist, jeweils ein Verb vorher und nachher zu verlangen, weil das in allen Spitzer-beispielen so ist. 


### F4 Das "entgrenzende *où* 'wo'" (S. 168)

fr: "le relatif "où" placé après des abstraits" (234)

Beispiele (Spitzer)

* "avec des yeux où règnait la douceur"
* "pour avancer cette mort où je cours"
* l'hymen où je me suis rangée"
* la honte où je suis descendue."

Queries

* F4a 
[wnlex="noun.feeling"|lemma="coeur|honte|pudeur|mélancolie|déplaisir|penchant|chagrin|oeil|mort|hymen"][word=","]{0,1}[word="où"%c] 
[wnlex="noun.feeling"][word=","]{0,1}[word="où"%c]
[wnlex="noun.feeling"|wnlex="noun.attribute"|wnlex="noun.cognition"|wnlex="noun.communication"|lemma="coeur|honte|pudeur|mélancolie|honte|pudeur|déplaisir|penchant|chagrin|oeil|mort|hymen"][word=","]{0,1}[word="où"%c]

* F4b (neu)  
[wnlex="noun.feeling"|lemma="coeur|honte|pudeur|mélancolie|déplaisir|penchant|chagrin|mort|hymen|trouble|mal|désespoir|malheurs|joie|bonheur|malheur| ennui|horreur|douleur|erreur|noeud|peine|rage|sacrifice|transport|colère|courroux|crainte|hyménée"][word=","]{0,1}[word="où"%c][]{0,10}[pos="verb"]

Anmerkungen

* En réalité, Spitzer renvoie ici presque exclusivement à des émotions et quelques noms assez concrets. Liste complète de Spitzer: "coeur|honte|pudeur|mélancolie|honte|pudeur|déplaisir|penchant|chagrin|yeux|mort|hymen"


### F5 les verbes phraséologiques (236): daigner, vouloir, oser, savoir / phraseologische Verben

Beispiele (Spitzer)

Queries

* F5: [lemma="daigner|oser|prétendre"][]{0,4}[pos="verb"] 

Anmerkungen

* Gut zu modellieren.


## F6 périphrase avec voir: PronomPers. + (AUX) + VOIR (241) / Periphrasen mit voir

Exemples / variantes (Spitzer)

* a "tu vis + VER"
* b "j'ai vu + VER"
* c "il m'a vu + VER (faire qqch)"
* d "tu m'as vu + VER"

Queries: 

* F6a [tag="PP.*"]{1,2}[tag="VA.*"]{0,1}[lemma="voir"][tag="VMN.*"]
* F6b [frpos="Pp.*"][frpos="Vu.*"][frlemma="VOIR"][frpos="V.*"]
* F6c [frpos="Pp.*"][frpos="Pp.*"]{0,1}[frpos="Vu.*"][frlemma="VOIR"][frpos="V.*"]
* F6d [tag="PP.*"]{1,2}[tag="VA.*"]{0,1}[lemma="voir"][tag="VM.*"]

Anmerkungen

* tt1: "j'ai vu couler" uvm.; Racine: 0.16, Proches 0.07, Autres 0.08 => plus fréquent chez Racine!
* tt2: "je vous ai vu préférer..." etc. Racine: 0.06, Proches 0.02, Autres 0.03 => plus fréquent chez Racine!
* F6c: Recht gute Abbildung des Phänomens; häufiger bei Racine, aber nicht massiv und nicht signifikant.
* F6d: Etwas bessere Abbildung des Phänomens, weil nur infinitive; häufiger bei Racine, aber nicht massiv und nicht signifikant.


### F7 expression périphrastique du verbe / umschreibender Ausdruck des Verbs

Beispiele (Spitzer)

* "porter ses pas" / "guider ses pas" (244), aber er bringt kein Racine-Beispiel!!! 
* "alla porter la terreur"

Queries

* F7a [lemma="porter|guider"][][lemma="pas"]
* F7b [tag="VM.*"][tag="DP.*"][lemma="pas" & pos="noun"]
* F7c [tag="VM.*" & lemma!="accompagner|suivre"][tag="DP.*"][lemma="pas" & pos="noun"]
* F7d ([lemma="arrêter|conduire|détourner|guider|hâter|porter|précipiter|redoubler|tourner"][][lemma="pas" & pos="noun"]|[lemma="aller"][pos="verb"])

Anmerkungen

* Beispiel: tc0649 "Au trône de Cyrus lui fit porter ses pas"
* weitere Beispiele: détourne ses pas, précipitez ses pas, retenu ses pas, suivre ses pas
* Es gibt mit porter/guider tatsächlich nur ein Beispiel bei Racine! Kein Wunder, dass Spitzer nichts zitiert.
* Mit anderen Verben noch einige relevante Treffer: 27 Treffer bei Racine
* Und: bei den Proches kaum treffer, und häufig 0 in einem Stück; Median 0! 
* Klar überrepräsentiert bei Racine, sogar deutlich signifikant.


## G Effet refroidissant, atténuant (245)

###  G1 adjectifs d'appréciation + NOM / wertenden Adjektiva und Adverbien (ger:178)

Beispiele (Spitzer)

* "votre juste crainte"
* "une juste terreur"

Queries

* (tt) [frlemma="JUSTE"][frpos="Nc.*"] 
* (tt) [frlemma="JUSTE"][frlemma="CRAINTE|COLÈRE|COURROUX|FUREUR|VENGEANCE|DOULEUR|CHÂTIMENT|ALARMES|EFFROI|DÉSESPOIR|HORREUR|SUPPLICE|DÉSIR|REMORDS|TERREUR|HAINE|AGRESSEUR|AMBITION|AMOUR|AUTORITÉ|AVERSION|DÉPIT|DEVOIR|ERREUR|EXCÈS|FERMETÉ|FIERTÉ|FRAYEUR|HAINE|HOMICIDE|IGNOMINIE|IMPATIENCE|INDIGNATION|JALOUSIE|MENACE|MÉPRIS|ORGUEIL|PEINE|PLAINTE|PUISSANCE|PUNITION|RAGE|RIGUEUR|SACRIFICE|ARRÊTS|FLAMMES|RIGUEUR"]
* Ergebnis: Racine 0.24, Proches 0.19, Autres 0.15 => häufiger bei Racine!
* G1x [lemma="juste"][wnlex="noun.attribute|noun.state|noun.feeling|noun.time|noun.cognition" & form!="ciel|cris|effets"]
* G1y [lemma="juste|oisif|utile|heureux|indigne|extrême|importun|triste|sombre|infortuné|noble|zélé|redoutable|détestable|funeste"][wnlex="noun.attribute|noun.state|noun.feeling|noun.time|noun.cognition" & form!="ciel|cris|effets"] 
* G1z [pos="adj.*"][wnlex="noun.attribute|noun.state|noun.feeling|noun.time|noun.cognition" & form!="ciel|cris|effets"] 
* G1c [pos="adj.*" & lemma!="même|autre|seul|3|capable|commun|nouveau|propre|grand|long|mutuel|moindre|jeune|premier|vieux|entier"][wnlex="noun.attribute|noun.state|noun.feeling|noun.time|noun.cognition" & lemma!="ciel|cri|effet|vie|jour|heure|de|amant|fait|voix|moment|paix|vue|couleur|moment|lien|secret|clarté|avantage|avis|climat|instant|journée|avantage|qualité|obstacle|apparence|vieillesse|caractère|choix|exploit|sujet|gloire"] 

Anmerkungen

* Problem ist, dass von LS nur diejenigen Konstruktionen gemeint sind (oder sein können), in denen das Substantiv als semantische Komponente einen Exzess oder zumindest eine große Intensität impliziert, was formal nicht so leicht zu definieren ist; allenfalls mit einer Liste.
* Auch beim Adjektiv gibt es ein Modellierungsproblem, weil Spitzer eine lange Liste an Adjektiven nennt, die alle in irgendeiner Form evaluierend / axiologisch sind. Das wiederum ist aber von Wordnet nicht erfasst, das nur "adj.all kennt oder keine Annotation. Einfach alle Adjektive zu nehmen, ist aber wiederum auch nicht zielführend.
* G11y: Nur die Adjektive, die Spitzer für Racine nennt; und nur die Wordnet-relevanten Nouns. Dann ist aber ein pro-Racine bias schon eingebaut.
* G1c: Alle Adjektive und alle Wordnet-relevanten Nouns, aber mit einer Ausschlussliste. So fasst man den Query breit, ohne allzu viele false Positives mitzubekommen, aber auch ohne Racine-Bias. 


### G2 trop + ADJ (250) / trop + Adjektiv

Beispiele (Spitzer)

* "mon bras trop prompt à..."

Queries

* G2 [word="trop"][pos="adj.*"]

Anmerkungen

* Das ist schlicht, scheint aber recht gut zu funktionieren. Fast alle Adjektive, die in dieser Kombination vorkommen, drücken tatsächlich etwas Extremes aus. Hier sollte also kein Racine-Bias zu finden sein. Und die Konstruktion ist tatsächlich auch bei den Proches stark und signifikant überrepräsentiert.

### G3 Oxymoron (253)

Beispiele (Spitzer) 

* heureuse cruauté, innocent stratagème, fureur si belle, détestable fruit, honnête faussaire, pouvoir inutile, beau désespoir, dangereux adieux, funeste soin, tranquille fureur, orgeuilleuse faiblesse, heureuse rigueur, funeste plaisir, heureux larcin, fatal honneur, saintement homicides

Queries

* G3a (mit Racine-Bias): (zwei Listen)
([word="heureuse"][word="cruauté"]|[word="innocent"][word="stratagème"]|[word="fureur"][word="si"][word="belle"]|[word="détestable"][word="fruit"]|[word="honnête"][word="faussaire"]|[word="pouvoir"][word="inutile"]|[word="beau"][word="désespoir"]|[word="dangereux"][word="adieux"]|[word="funeste"][word="soin"]|[word="tranquille"][word="fureur"]|[word="orgueilleuse"][word="faiblesse"]|[word="heureuse"][word="rigueur"]|[word="funeste"][word="plaisir"]|[word="hereux"][word="larcin"]|[word="fatal"][word="honneur"]|[word="saintement"][word="homicide.*?"])
* (alle adj+noun, dann auswählen): [pos="adj.*"][pos="noun.*"]

### G4 Anithèse (257)

### G5 Chiasme (260)

### G6 Antithèse avec "perspective insoupconnée" (262)

### GX Stichotomies (rares chez Racine!) (264)

### GX Autocorrections / Selbstkorrektur (204)

### GX Juxtapositions asyndétiques (269)

### G7 Structure binaire / Zweigliedrigkeit (ger:206) 

Beispiele (Spitzer)

* A: "et la lettre et le seing"
* B: "et transir et brûler"
* C: "ni le frein ni la voix"
* D: (mit ou, keine Beispiele)
* E: (Auflockerung): "D'où te bannit ton sexe et ton impiété"

Queries

* G7a (Substantive, nur et): [word="et"%c][]?[pos="noun" & type="common"][word=","]?[word="et"%c][]?[pos="noun" & * H10B (Verben, alle Varianten): 
* G7b : [word="et|ou|ni"%c][]?[pos="verb"][word=","]?[word="et|ou|ni"%c][]?[pos="verb"]
type="common"]
* G7c (mit ni): [word="ni"%c][]?[pos="noun" & type="common"][word=","]?[word="ni"%c][]?[pos="noun" & type="common"]
* G7d (mit ou): [word="ou"%c][]?[pos="noun" & type="common"][word=","]?[word="ou"%c][]?[pos="noun" & type="common"]
* G7e (mit ou): [word="ou|ni|et"%c][]?[pos="noun" & type="common"][word=","]?[word="ou|ni|et"%c][]?[pos="noun" & type="common"]


Anmerkungen

* Die strengeren Fassung lassen sich gut identifizieren, aber die Auflockerungen bringen dann einfach zu viele false positives.

### G8 répétition de mots ou de radicaux (273) / Stamm(wort)wiederholung (ger:209)

Beispiele (Spitzer)

* "Mener en conquérant sa nouvelle conquête" 


### G9 Atténuation par le remplissage d'hémistisches: oppositions d'adjectifs ou de participes présents (275)

Beispiele (Spitzer)

* "soumis ou furieux"
* "invisible et présente"

Queries:

* (tt2) [frpos="ADJ.*|VER:pper"] [frpos="PUN"]{0,1} [frlemma="ou"] [frpos="ADJ.*"]
* G9 [pos="adj.*" | tag="VMP.*"][tag="F.*"]{0,1}[lemma="ou"|lemma="et"][pos="adj.*" | tag="VMP.*"] + händische Bearbeitung

Anmerkungen

* Gesamtkorpus: 70x; Racine: 15x, Andere: 55 (=12)
* Beispiele genauer anschauen, einige sind nicht korrekt.
* Hier wird einerseits ein Problem der quantitativen Stilistik klar: die abstrakte Struktur ADJ+(,)+ou+ADJ ist für den Computer einfach zu finden, aber ob die Adjektive semantisch in Opposition stehen, wäre nur mit weiteren Annotationen eventuell automatisch zu klären (Sentiment Analysis).
* Zugleich wird ein Problem der hermeneutischen Stilistik Spitzers deutlich: die Frage, ob hier wirklich eine "atténuation" vorliegt, ist kaum mit harten Argumenten zu entscheiden; da ist sein Blick schon sehr stark davon geprägt, was er sucht (top-down Wahrnehmung).
* Das gilt auch für die beiden folgenden Phänomene

### G10 Atténuation par le remplissage d'hémistisches: atténuation par les adjectifs appréciatifs

Beispiele (Spitzer) 
* "un zèle imprudent"
* "victime obéissante"
* "indigne artifice"

Query
* (fw) [pos="noun"][pos="adj.*"|tag="VMP.*"]
* G10a: [pos="noun"][word="imprudent.*|obéissant.*|indigne.*|asservi.*|enchaîné.*|fatal|charmant|odieux|fier|fière|impuissant.*|souverain.*|magnanime.*|généreu.*|heureu.*|victorieu.*|timide.*|hautain.*|importuné.*|trompeu.*|"]
* G10b [pos="noun"][lemma="cruel|fatal|éternel|nouveau|secret|extrême|malheureux|odieux|infortuné|mortel|heureux|jaloux|fidèle|affreux|innocent|digne|criminel|furieux|suprême|sévére|ingrat|inhumain|perfide|sincère|importun|inutile|redoutable|victorieux|impuissant|obscur|timide|honteux|incertain|infidèle|farouche|généreux"]|[lemma="cruel|fatal|éternel|nouveau|secret|extrême|malheureux|odieux|infortuné|mortel|heureux|jaloux|fidèle|affreux|innocent|digne|criminel|furieux|suprême|sévére|ingrat|inhumain|perfide|sincère|importun|inutile|redoutable|victorieux|impuissant|obscur|timide|honteux|incertain|infidèle|farouche|généreux"][pos="noun"]


### G11 Atténuation par le remplissage d'hémistisches: appositions

Beispiele (Spitzer)

* "honteuse à ma mémoire"
* "promptes à me venger"


## H

### H1 Ordre de mots poétique de type latin (inversion); (278)

### H2 Ordre de mots enveloppée, synthétique (279)

## J Stilisierte Aufregung (ger:216)

### J1 Répétition solennelle (fre:280) / feierliche Wiederholung

Definition

* "da ist die feierliche Wiederholung von drohenden Prophezeiungen, mahnenden Imperativen, angsvollen Fragen, beteuernden Behauptungen" (ger:216) 

Beispiele (Spitzer)

* "Il peut, Seigneur, il peut, dans ce désordre extrême..."
* "Qui sait même, qui sait si le roi votre père..."  

Queries (RegEx)

* J1 ".* (\w{5,8}) .{0,25} \\1.*"
* ".* (\w{5,8}) .{0,15} \\1.*"
* ".* (\w{5,8}) .{0,50} \\1.*"

Anmerkungen

* Sowohl mit der engen Auslegung einer Wiederholung (L1x, wiederholte Wörter müssen nahe beieinander stehen) als auch mit einer erweiterten Auslegung (L1y) ergibt sich kein deutlicher, definitiv kein signifikanter Unterschied zwischen Racine und den Proches. Allerdings ist hier die reine Wiederholung modelliert, ohne inhaltliche Einschränkung auf die "mahnenden Imperative" etc. 


### J2 Asyndète de gradation / "das steigernde Asyndeton" (ger:217)

Beispiele (Spitzer)

* "Infortuné, proscrit, incertain de régner..."
* "Charmant, jeune, traînant tous les coeurs après soi..."
* "Muet, chargé de soins, et les larmes aux yeux..." 
* Le fer, le bandeau, la flamme est toute prête..." 

Queries

J2: Verben

* J2a [pos="verb" & lemma!="falloir|chercher|pouvoir|faire|être|avoir|devoir|dire" & word!="faut|suis|dit"][]{0,1}[word=","][pos="verb" & lemma!="falloir|chercher|pouvoir|faire|être|avoir|devoir|aller|dire" & word!="faut|suis|dit"][]{0,1}[word=","][pos="verb" & lemma!="falloir|chercher|pouvoir|faire|être|avoir|devoir|dire" & word!="faut|suis|dit"] 
* J2b ([pos="verb" & lemma!="falloir|chercher|pouvoir|faire|être|avoir|devoir|dire" & word!="faut|suis|dit"][]{0,1}[word=","][]{0,1}){3}

J3 (Substantive): 

* J3a: ([]{0,2}[pos="noun" & type="common"][word=","][]{0,1}){3}




Anmerkungen

* Hier beziehen sich die Beispiele immer auf die dreifache Wiederholung mehrerer unterschiedlicher Veben oder Substantive. Das lässt sich nocht recht gut mit CQP modellieren, allerdings ist natürlich die inhaltliche Steigerung nicht abbildbar.
* Spannend allerdings das Ergebnis: Die asyndetische Folge von Verben ist untypisch für Racine, während die asyndetische Folge von Substantiven tatsächlich bei Racine einen höheren Median hat, allerdings beides nicht signifikant. 



### J4 Asyndète avec condensation de différentes composantes (283) / "Ballung verschiedener Akzidentien oder Ingredientien zu einem einheitlichen Ganzen durch ein verschiedene Nomina (Infinitive, usw.) zusammenfassendes *tout*" (ger:219) 

Beispiele (Spitzer)

* (lange Passagen)

Queries

* J4: [word="tout"%c][word="cela"%c]

Anmerkungen

* J3x: Nur die Fälle mit "tout cela"
* 



### J5 Alignement de constructions nominales (284) / Aneinanderreihung von Nominalkonstruktionen

Beispiele (Spitzer) 

* Un seul exemple: "Soliman jouissait d'une pleine puissance : L'Égypte ramenée a son obéissance, Rhodes, des Ottomans ce redoutable écueil De tous ses défenseurs devenu le cercueil, Du_Danube asservi les rives désolées, De_l'_Empire_Persan les bornes reculées, Dans leurs climats brûlants les Africains domptés, Faisaient taire les lois devant ses volontés." (Bajazet)

Queries 

* J5 ([pos="noun"][tag="VMP.*"][]{0,8}){2,4} (also eine Sequenz von "Substantiv + Partizip + einige Worte, mehrfach)

Anmerkungen

* Treffer: "L'impie Achab détruit, et de son sang trempé Le champ que par le meurtre il avait usurpé ; Près_de ce champ fatal Jézabel immolée, Sous les pieds de les chevaux cette reine foulée ; Dans son sang inhumain les chiens désaltérés, Et de son corps hideux les membres déchirés ; Des prophètes menteurs la troupe confondue, Et la flamme de le ciel sur l'autel descendue ; Élie à les éléments parlant en souverain, Les cieux par lui fermés et devenus d'airain, Et la terre trois ans sans pluie et sans rosée ; Les morts se ranimant à la voix d'Élisée ;" (Athalie)

Notizen

* In der Tat erscheinen diese Sequenzen bei Racine sehr verbreitet zu sein. Im Vergleich der Mittelwerte zeigt sich das deutlich, mit 0.1/1000 Wörtern bei Racine, aber nur 0.05/1000 Wörtern bei den Anderen.

## K Übrige Phänomene

### K1 Aposiopèse (287) / "die Aposiopese, die Selbstunterbrechung der Rede" (ger:225)

Anmerkungen

* Schlicht markiert durch die drei Punkte "...",.

Queries

* K1: [word="\.\.\."]

### K2 "ganz einfache Verse oder Halbverse, die auf eine hochrhetorische Versreihe folgen" (ger:228)

Anmerkungen

* Das lässt sich nicht gut formal modellieren.

### K3 Nebensatzfolge (ger:232)

### K4 Abgeschwächte Interjektionen (ger: 232)

Beispiele (Spitzer)

* "Hélas ! un fils n'a rien qui ne soit à son père."
* "Ah, je l'ai trop aimé pour ne le point hair."

Queries

* K4a: [pos="interj"][word="!"]  
* K4b: [word="ah|hélas"%c] 
* K4c: [word="ah|hélas"%c][word="!"] 

Anmerkungen

* Spitzer sagt, Racine verwende sehr viele Interjektionen (und schwäche diese aber im Kontext ab). Die Ergebnisse zeigen, dass Racine gleich viele oder weniger Interjektionen als die Proches verwendet, allerdings bleibt unmodelliert, ob sie durch den Kontext jeweils abgeschwächt werden oder nicht. Das lässt sich nicht fassen. 

#### K5 Abgeschwächte Ausrufe

Beispiele (Spitzer)

* "Bajazet interdit ! Atalide étonnée !"
* "O soins tardifs et superflus !" 

Queries

* K5: [pos!="interj"][word="!"]

Anmerkungen

* Ganz einfacher Query, der nicht das Phänomen modelliert, sondern einen Indikator für das Phänomen. Die Ausrufezeichen nach Interjektionen sind ausgeschlossen, weil sie schon in M4A enthalten sind.


### K6 Apostrophen an höhere Mächte

### K7 "perseverierende Wortwiederholung" (ger:239)

Anmerkungen

* siehe hierzu weiter oben.


### K8 Rundzahlen

Beispiele (Spitzer)

* mille, cent

Queries

* K9 [word="mille|cent"%c]

Anmerkungen

* Interessant, dass diese Rundzahlen tatsächlich nur leicht überrepräsentiert sind bei Racine, allerdings sagt das wenig über ihre jeweilige Funktionalisierung und Kontextualisierung aus. 


### K10 Der Wechsel von "vous" und "toi"



