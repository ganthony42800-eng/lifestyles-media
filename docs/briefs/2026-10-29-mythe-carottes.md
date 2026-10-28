# Brief créatif : Mythe ou science ? ép. 7, les carottes font mieux voir ? (29/10/2026)

Directeur de création « monde » (agent 16), le 28/10. À appliquer par le motion designer 3D.
Script : `work-carottes/script-valide.md` (textes exacts, **ne pas les modifier**) · fiche : `work-carottes/fiche-validee.md` (liste fermée).
Format : 25,0 s · 1080×1920 · 30 i/s · une scène three.js procédurale (`tools/motion-engine/`, rendu interne 720×1280 comme l'ép. 6) · budget ≤ 2,5 s/image · aucune image externe.

---

## 1. Remise en question (protocole § 0)

**Les 5 dernières couvertures côte à côte** (heure offerte, snooze, alcool, cheveux, lire dans le noir) :
- **Gabarit identique 5 fois** : pastille en haut, question sur 2 lignes avec un seul mot coloré, objet héros au centre, signature centrée en bas. On reconnaît le gabarit, pas l'idée.
- **5 nuits d'affilée** (bleu nuit ou pénombre ambrée). Le compte devient « la chaîne sombre ».
- **Mêmes béquilles de matière** : bokeh (ép. 5), poussière dorée (ép. 6), particules, flare. Ces effets d'ambiance remplacent une idée visuelle.
- **Le chiffre arrive toujours en HTML par-dessus la 3D** (compteur centré). La 3D ne porte presque jamais la donnée elle-même. Seule exception : les élèves de l'ép. 6.
- **Les mains sont des cartes 2,5D** (une bonne solution technique, mais à garder hors du centre de l'image).

**Ce que les meilleurs font et que nous ne faisons pas encore** :
- **Le décor devient l'écran.** Hack Tetris du MIT sur les 153 fenêtres du Green Building (18/04/2026, viral sur Instagram et Reddit), Blinkenlights à Berlin (2001) : des fenêtres utilisées comme pixels. Chez nous, la donnée est toujours ajoutée par-dessus le décor.
- **La perception elle-même comme effet.** L'effet Purkinje (simulation ISLE de Hanover) : à la tombée de la nuit, le rouge et l'orange noircissent d'abord, le bleu tient. Personne, dans la presse sur ce mythe (Science Norway 25/05/2026, Daily Maverick 09/06/2026, McMaster, How It Works), ne le montre. Tous illustrent avec une photo de carottes ou l'affiche « Dig for Victory ».
- **Code d'époque par l'objet, pas par l'affiche.** Les rubans de papier gommé collés en croix sur les vitres en 1940 (1900s.org.uk) sont reconnaissables immédiatement, sans rien copier.
- **Le son de la matière comme ponctuation** (ASMR alimentaire) : nous mettons des « tics » génériques.

**Interdits rappelés (déjà faits)** : faisceau volumétrique en marche de rayons, couette, goutte en macro et plongée dans une sphère, télésiège, filtre thermique. **Nouveaux interdits pour cet épisode** : **zéro bokeh, zéro poussière en suspension, zéro flare de lampe.** La ville reste nette, en profondeur de champ longue.

---

## 2. Idée maîtresse

**« La fenêtre-données » : depuis ta table de cuisine, la ville d'en face devient l'écran. Ses fenêtres s'éteignent pour écrire 190 M, puis elle remonte à 1940.**
La lumière de la cuisine baisse et ta carotte perd son orange en premier (effet Purkinje). Elle ne le retrouve qu'au verdict.

## 3. Image 0 (ce qui arrête le pouce)

POV **assis à table, le soir**, caméra à hauteur d'yeux (≈ 1,15 m), légère plongée.
- **Bas du rectangle sûr (y ≈ 900-1250)** : assiette en céramique blanche émaillée (reflet de la suspension sur le bord). Rondelles de carotte **orange vif, brillantes** (beurre, reflet spéculaire mouillé), avec le cœur plus pâle et l'anneau du cambium visibles. Deux ou trois fanes vertes posées au bord (écho au trèfle de la signature).
- **Main d'adulte** (carte 2,5D, manche de pull) qui entre par le bas à gauche (y 1250-1600) et pousse l'assiette vers toi de 4 cm en 1,5 s. C'est le geste « finis tes carottes ».
- **Milieu (y ≈ 330-880)** : **fenêtre de cuisine** à croisillons. Derrière, une ville nette avec **toutes les fenêtres allumées** (chaudes #FFD38A, quelques froides #BFE6FF). Une **tour en face**, proche, à fenêtres en *interior mapping* (vraies pièces en parallaxe). C'est elle qui servira d'écran à 12,2 s. Reflet fantôme très léger de la suspension dans la vitre (indice de réalisme).
- **Haut (y 146-520)** : pastille « MYTHE OU SCIENCE ? · ÉP. 7 » (32 px), puis la question ≥ 90 px, « **mieux voir** » en orange carotte.
- Lumière : suspension chaude au-dessus de l'assiette (point + émissif), ville en contre-jour bleu nuit.
- **Rupture avec les 5 couvertures** : le héros n'est plus au centre. Composition en trois étages (question / ville / assiette), et l'**orange** domine pour la première fois.

## 4. Fil visuel continu (une seule caméra, aucune coupe)

| t (s) | Caméra | Ce qui se passe |
|---|---|---|
| 0-3,0 | Quasi fixe, micro-travelling avant de 3 cm (respiration) | Main qui pousse l'assiette, ville allumée. 1,5 s : « Pas toi. Mais leur vitamine sauve des yeux. » |
| 3,0-3,4 | Fixe | **Variateur** : la suspension baisse (clic + bourdonnement qui descend). **Bascule Purkinje** : la cuisine passe en vision de nuit gris-bleu, la carotte noircit en premier, le bleu de la ville tient, les fenêtres restent colorées. |
| 3,4-5,6 | Panoramique léger vers la droite | **Jauge = vrai objet** : un verre de jus de carotte déjà plein à ras bord (étiquette `lab` « stock vitamine A »). Trois rondelles tombent dedans, le jus **déborde en nappe** le long de la paroi (pas de goutte en gros plan) et s'étale sur la table : « Zéro bonus ». |
| 5,6-8,2 | Retour au centre | La main repousse l'assiette. Fenêtres de la ville **toujours allumées** (boucle ouverte). Écran de partage. |
| 8,2-12,2 | Lent travelling avant vers la vitre (de 0,6 m vers 0,35 m) | La cuisine plonge dans le noir, seules les fenêtres de la ville éclairent la scène. Compteur « ??? ». **Silence total 12,0-12,2.** |
| **12,2-15,4** | Fixe sur la tour en face, cadrée dans la vitre | **MOMENT WAOUH** (§ 5). |
| 15,4-18,4 | Dernier travelling avant : la vitre remplit le cadre | **Machine à remonter le temps** (§ 6) : la ville éteinte devient le black-out de 1940. |
| 18,4-21,6 | Travelling arrière rapide (0,5 s, ease-out) jusqu'à la table | Ruban décollé, tours qui remontent, **clic de la lampe** : la couleur revient en 0,35 s, l'orange en premier. Une seule carotte entière avec fanes dans l'assiette. Tampon MYTHE. Les fenêtres se rallument **en vague, du proche au lointain** (la boucle « sauve des yeux » se referme). |
| 21,6-24,4 | Fixe, léger flottement | Signature officielle collée (haut y = 1396, largeur 240, **bas ≤ 1474**), @lifestyles_hf, « Ép. 8 » + bouton Abonne-toi. |
| 24,4-25,0 | Retour à la pose d'image 0 | La carotte entière **se tranche en cascade** (les rondelles se séparent et tombent, un tic chacune). Image 25,0 = image 0. |

## 5. Moment waouh, 12,2 s : la façade-pixel

Après 0,2 s de silence, la ville **s'éteint par grappes en vague**, de l'horizon vers toi (grappes de 6 à 20 fenêtres, relais décalés). La **tour d'en face reste allumée**. Puis, de 12,35 à 12,9 s, **ses fenêtres s'éteignent pour écrire « 190 M »** en chiffres noirs sur la façade lumineuse.
- Grille de la façade ≈ 30 colonnes × 40 étages visibles. Glyphes 5×7 fenêtres, 1 colonne d'espace, centrés dans le rectangle sûr (x 140-940, y 560-900). Les fenêtres éteintes s'enchaînent trait par trait, dans le sens de l'écriture.
- Le chiffre HTML « 190 millions. » (script, sc. 5) entre **à 12,9 s, une fois l'écriture finie**. Le compteur « ??? » se fige **net**, sans valeur intermédiaire lisible.
- Couleur : fenêtres restantes plus chaudes, légère pulsation corail #FF6A55 sur le contour de la façade au mot « cécité ».
- **Pourquoi c'est fort** : la donnée n'est plus posée sur le décor, c'est le décor qui l'écrit. Et une fenêtre éteinte se lit comme « ne plus voir la nuit » sans aucune légende.
- Option, à faire valider par le vérificateur avant usage : la vague de la ville éteint **exactement 1 fenêtre sur 3** (fidèle aux 33,3 % de l'OMS 2009 figurant dans la fiche), **sans aucun texte** qui le dise. Si refus : grappes aléatoires.

## 6. Second temps fort, 15,4 s : la vitre remonte à 1940 (sans affiche)

- **15,4-15,8 s** : des **bandes de papier gommé brun** (≈ 7 cm, texture fibreuse procédurale) se posent **en croix d'un coin à l'autre** sur chaque carreau de NOTRE vitre, côté intérieur, avec un bruit de papier qu'on lisse.
- **15,6-16,6 s** : les tours modernes **s'abaissent** (échelle verticale des instances, ease-in-out) en rangées de maisons de 3 à 5 étages, à toits en pente et cheminées. Deux ou trois **ballons de barrage** argentés (ellipsoïde + 3 ailerons) montent. Toutes les fenêtres restent noires (le black-out).
- **Projecteurs SANS faisceau** : uniquement des **taches de lumière elliptiques qui glissent sur le plafond nuageux** (bruit fbm éclairé localement). On ne fait pas de cône volumétrique, interdit puisque déjà fait à l'ép. 6.
- **17,0-17,8 s** : un **bimoteur de nuit** en silhouette (géométrie simple, sans cocarde ni insigne) traverse une tache de lumière.
- Étalonnage : clair de lune **argent-vert froid** (#A9B8A6), pas de sépia.
- Rime narrative : le noir des fenêtres éteintes (carence) **devient** le noir du black-out. Même obscurité, autre histoire, sans coupe.

## 7. Les innovations retenues (nouvelles par rapport à l'ép. 6)

1. **Façade-pixel** : les fenêtres de la ville écrivent le chiffre clé (principe du hack Tetris du MIT 2026 et de Blinkenlights). La donnée vivante est le décor lui-même.
2. **Bascule Purkinje** : quand la lumière baisse, **l'orange meurt en premier**. La carotte, censée faire voir la nuit, est la première chose qu'on ne voit plus. Le texte suit la même physique : « mieux voir » passe de l'orange au gris-bleu à 3,0 s. Tout revient en couleur au verdict, à 18,4 s. Une vérité de perception rendue visible, sans chiffre ajouté.
3. **Machine à remonter le temps par l'objet** : papier gommé en croix et ville qui rajeunit, aucune affiche d'époque.
4. **Son : le tampon MYTHE est un croquement de carotte** (§ 10).

## 8. Palette (étincelante, sans surcharge)

| Rôle | Couleur |
|---|---|
| Héros, carotte | #FF7A1A (ombre #C24E0A, reflet #FFB070) |
| Fanes, écho au trèfle de la signature | #3FBF6A |
| Nuit de ville | #0A1430 → #060B1E (bleu Lifestyles) |
| Fenêtres | chaudes #FFD38A · froides #BFE6FF |
| Vision de nuit (Purkinje) | gris-bleu #8C9BB5, orange résiduel ≤ 25 % pour garder la jauge lisible |
| Alerte (190 millions, cécité) | corail #FF6A55 |
| 1940 | argent-vert #A9B8A6, papier gommé #8A6A44 |
| Signature | or officiel (image collée) |

Règle : **2 couleurs dominantes par plan au maximum** (orange + bleu nuit ; puis gris-bleu + fenêtres chaudes ; puis argent-vert seul).

## 9. Matières et lumière

- **Rondelles** : cylindres biseautés, shader dédié (dégradé radial : cœur pâle → cambium → cortex orange, stries radiales fines, spéculaire mouillé, légère translucidité en bord).
- **Assiette** : géométrie de révolution émaillée, reflet de l'environnement (RoomEnvironment faible).
- **Table** : bois procédural (veinage fbm), vernis satiné. La nappe de jus débordé = plan avec masque animé et spéculaire.
- **Verre de jus** : **faux verre en shader** (Fresnel + reflet + jus opaque à ménisque), sans `transmission` (économise une passe).
- **Vitre** : reflet fantôme de la suspension (≈ 6 %), croisillons en bois peint.
- **Ville** : ≈ 250 à 350 boîtes instanciées, fenêtres procédurales (identifiant de fenêtre par hachage, états fournis par une `DataTexture` qui pilote vagues, glyphes et rallumage). Tour d'en face en **interior mapping procédural** (pièces dessinées dans le shader, comme three-fenestra mais sans dépendance). Aucune texture externe.
- **Post-traitement** : passe Purkinje (luminance scotopique, approximation de Larson : V' ≈ 0,36·Z + 1,18·Y − 0,80·X, puis teinte gris-bleu, mélange piloté par `uScot`), bloom avec **seuil ≥ 1,7** (nuit), filtre NaN/Inf et plafond 6 avant le bloom (leçon du 27/10), grain 3 %, vignette légère.

## 10. Typographie cinétique : l'« allumage en fenêtres »

- **Entrée** : chaque bloc de texte est découpé par une grille de cellules rectangulaires (≈ 18 px). Les cellules s'allument dans un ordre aléatoire déterministe en **0,22 s**, avec un scintillement de néon sur 2 images, comme des fenêtres qui s'allument. **Sortie** : extinction inverse, **terminée avant l'entrée du texte suivant** (fenêtre [z − 0,24 ; z], leçon du 25/10).
- Le mot coloré **subit la bascule Purkinje** (orange → gris-bleu à 3,0 s, retour à 18,4 s).
- « 190 millions. » entre **sans** effet de cellules (la façade vient de le faire) : apparition nette, légère montée de 12 px.
- « MYTHE. » : tampon (échelle 1,25 → 1 avec léger dépassement), bordure orange carotte.
- Tailles : question et textes principaux ≥ 90 px · petits textes, sources et pastille **≥ 30 px** · étiquette `lab` 36 px.

## 11. Son (original, synthèse procédurale `audio.py`, sans voix, plafond −3,5 dBFS)

- **Lit** : cuisine le soir (frigo : 50 Hz + harmoniques, très bas), rumeur de ville filtrée passe-bas derrière la vitre.
- **Nappe** : Fa dièse mineur 11 (nouvelle tonalité), qui se résout en **Ré majeur 9 à 18,4 s**.
- 0,3-1,8 s : **assiette qui frotte sur le bois** (bruit de friction + 3 modes résonants céramiques).
- 3,0 s : **clic du variateur** + bourdonnement électrique qui descend en hauteur ; la nappe passe en filtre passe-bas (« l'oreille aussi passe en vision de nuit »).
- 3,6-5,4 s : 3 « plocs » de rondelles dans le jus, **débordement** (glouglou bref + filet).
- 8,2-12,0 s : les aigus de la nappe s'éteignent un à un. **Silence total 12,0-12,2.**
- 12,2-12,35 s : **vague de relais** (« toc » feutrés, panoramisés gauche/droite selon la position x de la grappe, hauteur selon l'étage).
- 12,35-12,9 s : chaque trait du « 190 M » = un « thunk » grave, plus un sub-boom sous le chiffre HTML.
- 15,4 s : **papier gommé** lissé sur le verre (4 frottements secs) ; vent froid ; **ronronnement de bimoteur** (deux dents de scie désaccordées ≈ 85/87 Hz, battement lent) qui passe de gauche à droite à 17,0-17,8 s.
- 18,4 s : papier qui se décolle (déchirure brève), **clic de la lampe**, l'accord s'ouvre, **tampon MYTHE = croquement de carotte** (rafale de craquements granulaires filtrés de 1,5 à 6 kHz + attaque sèche).
- 18,8-20,0 s : rallumage des fenêtres = arpège de petits tintements de verre, du proche au lointain.
- 21,6 s : scintillement de la signature. 24,4-25,0 s : rondelles qui tombent (6 tics de bois accordés), en raccord avec l'ambiance de 0 s pour la boucle.

## 12. Couverture

**Image à 1,0 s** (avant « Pas toi. ») : assiette orange brillante + main + ville toutes fenêtres allumées + question seule + pastille ÉP. 7 + signature. Tout le sens tient dans le carré central et le recadrage 4:5. Contrôle : la carotte doit rester **orange saturée** même en vignette (pas de voile du bloom).

## 13. Faisabilité (moteur maison, rien à commander)

- **100 % procédural dans `tools/motion-engine/`**, une seule scène three.js (cuisine + ville dans le même monde ; 1940 = morphing des mêmes instances). Aucun plan réel ni image OpenArt nécessaire. Pas de personnage connu, pas d'affiche d'époque.
- **Coût estimé** : ville instanciée + fenêtres en shader (très bon marché), faux verre sans transmission, ombres limitées à la suspension (une seule ombre, carte 1024), pas de marche de rayons. Cible **≈ 1,6-2,2 s/image** à 720×1280, sous le plafond de 2,5 s.
- **Signature** : `brand/signature-officielle.png` collée en `<img>` (jamais redessinée), haut y = 1396, largeur 240, **bas ≤ 1474** (test de la légende Instagram, à garder).
- **Contrôles obligatoires avant le rendu complet** : image 0 = image 25,0 (comparer les deux images avant de lancer le rendu, leçon du 27/10) ; carotte lisible en mode Purkinje ; glyphes « 190 M » lisibles à 50 % de taille ; `ffprobe -count_frames` = 750 ; `tools/qa/check_reel.py` ≥ 90.
- **Étiquette « Simulation 3D »** en coin pendant toute la vidéo (comme les épisodes précédents), y compris pendant la séquence 1940.

## 14. Références (3 par choix)

| Choix | Références |
|---|---|
| Façade-pixel (waouh) | [The Tech, Tetris sur le Green Building, 30/04/2026](https://thetech.com/2026/04/30/green-building-tetris-2026) · [Boston Globe, 21/04/2026](https://www.bostonglobe.com/2026/04/21/metro/mit-tetris-game-hack-returns-to-green-building/) · [Project Blinkenlights (Berlin, 2001)](https://en.wikipedia.org/wiki/Project_Blinkenlights) |
| Fenêtres vivantes, interior mapping | [three-fenestra (interior mapping three.js)](https://www.jsdelivr.com/package/npm/three-fenestra) · [Godot Shaders, interior mapping](https://godotshaders.com/shader/interior-mapping-shader/) · [Brevet « procedural window lighting »](https://patents.google.com/patent/US10380790) |
| Bascule Purkinje | [ISLE Hanover, simulation Purkinje](https://isle.hanover.edu/Ch03Eye/Ch03PurkinjieSim.html) · [ISLE, vision photopique / scotopique](https://isle.hanover.edu/Ch03Eye/Ch03PhotopicScotopic.html) · [ACEScentral, « All cats are grey at night » (rendu scotopique)](https://community.acescentral.com/t/all-cats-are-grey-at-night-render-theory-question/4511) |
| 1940 par l'objet (papier gommé, black-out) | [1900s.org.uk, vitres scotchées des années 1940](https://1900s.org.uk/1940s-taped-windows.htm) · [Wartime NI, faire respecter le black-out](https://archives.wartimeni.com/article/blackout-northern-ireland/) · [Science Norway, origine du mythe, 25/05/2026](https://www.sciencenorway.no/culture-food-and-health-war/where-the-carrot-myth-comes-from/2665915) |
| Ouverture : la presse n'illustre qu'en photo | [Daily Maverick, 09/06/2026](https://www.dailymaverick.co.za/article/2026-06-09-do-carrots-really-improve-your-night-vision-6-enduring-diet-myths-debunked.md) · [McMaster Health Sciences](https://healthsci.mcmaster.ca/?p=3929) · [How It Works](https://www.howitworksdaily.com/do-carrots-help-you-see-in-the-dark/) |
| Rythme et typo (un beat = une action, motion codée) | [mean.ceo, motion design octobre 2026](https://blog.mean.ceo/?p=10946) · [Videobolt, tendances 2026](https://blog.videobolt.net/post/top-motion-graphics-trends-2026) · [Tangence, tendances 2026](https://www.tangence.com/blog/?p=1093) |
| Format court du moment (plan unique, illusion) | [Anijam, tendances Reels (MAJ 10/10/2026)](https://www.anijam.ai/blog/instagram-reels-trends/) · [Buffer, Reels tendance 2026](https://buffer.com/resources/instagram-trending-reels/) · [Vaizle, tendances Reels](https://insights.vaizle.com/instagram-reel-trends/) |

## 15. Prédiction (à comparer après publication avec l'analyste)

- Taux > 3 s attendu **≥ 50 %** : lieu vécu en POV, souvenir d'enfance universel, couleur inédite sur le compte.
- Point de rétention critique : **12,2 s** (la façade-pixel doit faire remonter la courbe) ; deuxième point : 15,4 s (1940).
- Risque : la bascule Purkinje rend la jauge de jus moins lisible entre 3,4 et 5,6 s. Garder ≥ 25 % d'orange résiduel et un reflet spéculaire fort.
