# Brief créatif — « Mythe ou science ? » ép. 4 : l'alcool réchauffe ?

Agent 16 (directeur de création « monde ») · 25/10/2026 (pour publication lundi 26/10) · mode RAPIDE · Statut : **BRIEF PRÉPARÉ** (rien n'est rendu, rien n'est testé).
Entrées : `docs/playbook-viral.md` · `data/lecons.md` · `docs/veille-visuelle.md` (session du 25/10, ajoutée) · briefs ép. 1-3 + piéton + heure offerte + snooze · couvertures des 5 derniers Reels · moteur `tools/motion-engine/` (exemples `2026-10-25-snooze`, `2026-10-20-mythe-chaleur-tete`).
**Message scientifique provisoire** (vérifié en parallèle). Les textes ci-dessous sont des **emplacements** : le scénariste les remplit, le vérificateur tranche. **Aucun chiffre de température à l'écran tant que la fiche n'est pas VALIDÉE.**
Format : 1080×1920, 30 i/s, **25,0 s = 750 images**. Moteur : `capture.py` (`window.sceneReady`, `window.renderAt(t)`), three.js (vendor), SwiftShader, rendu WebGL **720×1280** agrandi (comme snooze), texte HTML net en 1080×1920. Partir du squelette `exemples/2026-10-25-snooze/index.html` (importmap, utilitaires déterministes `mulberry32`, `canvasTex`, signature PNG + `#sigShine`, pastille de série) et **jeter toute la scène**.

---

## 0. Remise en question (sans complaisance)

**Ce que disent les chiffres.** Le seul Reel qui dépasse largement 50 % > 3 s en 3D est le piéton (70 %) : **un lieu vécu, en POV, avec une situation humaine**. L'ép. 3 publiée (tête en particules de dos, sur fond violet) fait 51,6 % : correct, pas plus. Les objets translucides sur fond nuit (ép. 1 : 23,5 %, ép. 2 : 48,9 %) n'accrochent pas.

**Ce qui fait « déjà vu » chez nous**
1. **Trois épisodes « Mythe ou science ? », trois fonds bleu-violet sombres avec un objet seul au centre** (verre, os, tête). La série a un gabarit, pas une identité.
2. **Deux mythes « chaleur » d'affilée** (ép. 3 tête, ép. 4 alcool). Si on refait une caméra thermique (palette fer, déjà prête dans la version « scan » non publiée de l'ép. 3) ou une silhouette de particules dorées, le public verra **le même Reel**. **Décision : pas de filtre thermique, pas de silhouette en particules.** La chaleur doit se voir autrement.
3. **Le spectateur n'a jamais de corps.** Même en POV (chambre, téléphone, pare-brise), personne ne voit **ses propres mains, ses genoux, sa veste**. Le snooze a même renoncé à la main (silhouette floue).
4. **Toutes nos caméras sont « posées »** : orbite lente, bougé à la main, glissé. Aucune n'est **transportée par quelque chose** (un véhicule, une remontée) qui donne seul le rythme.
5. **Sept Reels sur huit sont en intérieur ou en rue de nuit.** Aucun grand extérieur, aucune montagne, aucun ciel qui change.
6. **Le levier de partage arrive encore tard** (12,6 s heure offerte, 10,2 s snooze) et il est purement typographique : **rien ne se passe à l'image** quand on dit « envoie ça à… ».
7. **Le mythe est toujours dit en texte** (« un vieux manuel de l'armée ») : jamais montré comme une image, alors que le mythe de l'alcool a **une icône mondiale** (le Saint-Bernard et son tonnelet).

**Ce que les meilleurs font et que nous ne faisons pas encore**
- **Faire de la chaleur la matière même de l'image** : NOMINT pour WWF, « In Hot Water » (Graphite Pencil D&AD 2025, Gerety, Clio), maquettes chauffées une par une et filmées en thermique ([D&AD](https://www.dandad.org/work/d-ad-awards-archive/in-hot-water)). Nous en tirons le principe (« la chaleur raconte ») sans le filtre : la chaleur devient **de la lumière qui circule** dans le corps du spectateur.
- **Le réel prouve** : la recherche de Patras (2012) montre en thermique que le **nez se réchauffe** et le front refroidit après l'alcool, à cause des vaisseaux de la peau qui se dilatent ([ScienceDaily](https://www.sciencedaily.com/releases/2012/09/120904100137.htm)). La rougeur de surface est **un fait visible** : on la montre sur la main, sans visage.
- **Le sujet est partageable** : un Reel indien sur ce mythe (diététicien Bhawesh Gupta) : **≈ 285 000 vues, 11 700 j'aime, près de 4 000 partages** (déclaré par [The Week, 11/01/2026](https://www.theweek.in/news/health/2026/01/11/fact-check-does-alcohol-really-keep-you-warm-during-winters.amp.html)), soit ≈ 14 partages / 1 000 vues. C'est **au-dessus de notre objectif** (10 / 1 000) : le sujet porte le partage, à nous de ne pas le gâcher.
- **Le mythe est mondial et saisonnier** : Corée (« 혈관확장에 체온 뚝 », [Newsis 01/2025](https://www.newsis.com/view/NISX20250106_0003022427)), Allemagne (vin chaud du marché de Noël, [Utopia](https://utopia.de/ratgeber/gluehwein-zum-aufwaermen-warum-das-keine-gute-idee-ist/) ; « des cheveux mouillés au vin chaud : les plus grandes erreurs d'hiver », [Joyn](https://newstime.joyn.de/themen/panorama/von-nassen-haaren-bis-gluehwein-die-groessten-winter-irrtuemer-34599)), Brésil, Espagne, Chine. **Tous illustrent en photo de banque d'images** (gens emmitouflés, verre de vin chaud) : personne ne montre **le trajet de la chaleur** dans le corps.
- **Les interfaces réelles du lieu** : les masques de ski à affichage tête haute (Rekkie : vitesse, altitude, pente dans un coin du verre, [InTheSnow 2026](https://www.inthesnow.com/smart-goggles-and-airbag-vests-the-must-have-ski-tech-for-2026/)). On n'en fait pas l'interface principale (risque de gadget), mais **la petite étiquette de coin** (comme sur un vrai affichage de masque) sert de repère discret.

**Univers interdits (déjà faits ou hors ADN)** : palette fer / thermique plein cadre (ép. 3 scan) · silhouette en particules dorées, violet dominant (ép. 3) · verre, bulles, sarcelle (ép. 1) · os radio, négatoscope (ép. 2) · rue mouillée, pluie, réverbères, phares (piéton) · réveil, jauge liquide, rayons de lune (heure offerte) · fond clair de couette, cyan `#3FE0FF`, rouge `#FF3B5C` (snooze) · étoiles, sol quadrillé, gabarit « stomp ».

---

## 1. Idée maîtresse

> **« Tu es sur un télésiège à l'heure bleue. Une moufle te tend le bouchon d'une flasque. Tu bois : les vaisseaux de ta main s'allument en rouge, tu as chaud… puis le vent arrache cette chaleur de tes doigts, et la braise au centre de ton corps passe du doré au bleu glacier. »**

La chaleur est montrée comme **un circuit de lumière dans ton propre corps** : une braise au centre du corps → des filets lumineux dans la manche → le réseau des vaisseaux de la main qui s'élargit → des braises qui s'envolent dans le vent. Le mythe (« ça réchauffe ») et la vérité (« ça vide ») sont **le même mouvement de lumière** vu à deux moments. Pas de thermomètre, pas de chiffre nécessaire : **la couleur de la braise est la donnée**.

---

## 2. Innovations retenues (jamais faites chez nous)

| # | Innovation | En quoi c'est neuf chez nous | Principe source |
|---|---|---|---|
| 1 ★ | **La caméra est portée par un télésiège** : un seul plan continu de 25 s qui monte le long du câble (≈ 2,3 m/s, légère oscillation pendulaire de la chaise). **Le décor bat la mesure** : les chaises vides qui redescendent sur le câble d'en face croisent la caméra **toutes les 2,4 s** (changement visuel + « woosh » sonore), et deux pylônes passent au-dessus (0,8 s et 12,0 s : « clac-clac-clac » des galets). Le rythme de montage n'est plus un montage : c'est la remontée. | Toutes nos caméras étaient posées, en orbite ou tenues à la main. Ici, plan-séquence réel et métronome **diégétique** (il existe dans le lieu). | Plan-séquence sans coupe des tendances Reels ([Anijam 10/2026](https://www.anijam.ai/blog/instagram-reels-trends/)) · « le son calé sur chaque action visible » ([mean.ceo 10/2026](https://blog.mean.ceo/?p=10938)) · POV de lieu vécu (piéton, `lecons.md`) |
| 2 ★ | **Le spectateur a un corps, et la caméra est sa tête** : on voit **ses** genoux et ses skis qui pendent au-dessus du vide, **sa** moufle gauche sur le garde-corps, **sa** main droite nue qui prend le bouchon. La caméra **fait les gestes de la tête** : elle bascule vers le ciel pendant la gorgée (0,6 s), puis **baisse les yeux** vers la poitrine pour la révélation. | Première fois que « tu » n'est pas un mot mais **une image** : le spectateur se reconnaît en < 1 s. | POV « depuis le lit » (veille 23/10, Know Your Meme) · piéton POV conducteur |
| 3 ★ | **Le circuit de la chaleur** (donnée vivante sans chiffre) : la **braise du centre du corps** (sous la veste, révélée par la fermeture éclair qui s'ouvre seule) envoie des filets de lumière dans la manche ; dans la main, **un réseau de vaisseaux procédural s'allume puis s'épaissit** (la vasodilatation se voit : les traits grossissent) ; puis le vent arrache des braises des doigts. La braise passe **ambre → bleu glacier**, du givre pousse sur son contour. | Fini l'objet-jauge ajouté (bulles, verre gradué, barre de palette) : la donnée **est** le corps. | NOMINT « In Hot Water » (la chaleur comme langage, [D&AD](https://www.dandad.org/work/d-ad-awards-archive/in-hot-water)) · thermographie Patras : surface qui chauffe ([ScienceDaily](https://www.sciencedaily.com/releases/2012/09/120904100137.htm)) · codes de la 3D médicale : deux couleurs, chaude / froide (veille 17/10 § D) |
| 4 | **Le mythe dessiné à la lumière** : pendant 2,2 s, un **trait d'or au néon** dessine dans la neige, sous le télésiège, un Saint-Bernard et son tonnelet qui trottent (animation de tracé, style gravure), puis une rafale **souffle le dessin** en poussière de neige. Le mythe est un dessin (une légende), la science est de la matière. | Le mythe n'est plus une phrase : c'est une **image-icône** reconnue dans le monde entier. | Light painting / tracé de chemin (technique `stroke-dashoffset` / ligne shader) · origine picturale du tonnelet (Landseer, années 1820, [Mental Floss](https://www.mentalfloss.com/animals/dogs/10-big-facts-about-saint-bernards)) |
| 5 | **Le bord du cadre, c'est ta peau** : au moment de la gorgée, **les bords de l'image rougissent** (vignette corail douce, 60 px de flou, comme une joue qui chauffe) pendant que le centre, plus tard, **bleuit**. Deux températures dans le même cadre : ce que tu sens (bords) / ce qui se passe (centre). | La couleur du cadre raconte la sensation. | Dérivé de nos règles « deux dominantes par plan » + principe « split » de transformation (BlitzCut, veille 23/10) |
| 6 | **Arc de lumière sur 25 s** : l'heure bleue tombe en nuit pendant la montée (ciel `#1E3170` → `#070C22`, neige qui s'assombrit, lumières de la station en bas qui s'allument une à une). **Le froid gagne pendant que tu regardes.** | Première fois que la lumière du décor évolue avec le récit sur tout le Reel. | Gobos et lumière de fenêtre comme horloge (veille 23/10), étendu à un paysage |
| 7 | **Texte « de souffle »** : chaque nouvelle phrase naît d'une **bouffée de buée** (ton expiration, sprite blanc qui sort du bas du cadre) : le mot se forme dans la buée et reste net quand elle se dissipe. Les mots de vérité ont un **liseré de givre** (cristaux en CSS). | Le texte vient du corps et du lieu (le froid), pas d'un gabarit d'apparition. | Typo cinétique « selon la physique du sujet » (veille 18/10) · tendance typo 3D / dimensionnelle 2026 ([Design Monks](https://www.designmonks.co/blog/typography-trends-2026)) |

**Obligatoires : 1, 2, 3.** 4 et 5 coûtent peu (HTML/CSS + une ligne de shader). 6 et 7 : à garder si l'aperçu reste sous 6 s / image.

---

## 3. Image 0, couverture et moments forts

### Image 0 (arrête le pouce ; lisible en vignette 395 px et dans la grille 3:4, y 240-1680)
- **POV assis sur un télésiège, heure bleue, neige qui tombe doucement.** Cadrage légèrement plongeant (caméra inclinée de −18°).
- **Premier plan bas (y 1450-1920)** : le **garde-corps** du télésiège (tube métal gris-bleu, reflet du ciel) en travers ; dessus, **ta moufle gauche** (gris anthracite, matelassée) ; sous le garde-corps, **tes genoux** (pantalon de ski bleu nuit) et **les spatules de tes skis** qui pendent au-dessus du vide, en légère contre-plongée sur la pente.
- **Milieu (y 1050-1450)** : **depuis le bord droit, un bras de voisin** (manche de veste ardoise, **aucun visage, aucun corps au-delà de l'épaule**) tend **le bouchon-gobelet en métal brossé d'une flasque** (sans étiquette, sans marque, sans liquide visible : on voit le bord du gobelet, pas son contenu). C'est **« celui qui sort la flasque »** : la cible du partage est dans l'image 0.
- **Fond (y 600-1100)** : la pente de neige 8-10 m plus bas, qui défile ; des sapins sombres ; **le câble et les chaises qui montent devant** (silhouettes minuscules de skieurs de dos) ; plus loin, les crêtes en 3 couches de brume ; en bas à gauche, **quelques lumières chaudes de la station** (chalets).
- **Ciel (y 0-600)** : dégradé heure bleue.
- **Texte (y 300-640)** :
  - Pastille « MYTHE OU SCIENCE ? · ÉP. 4 » (y 150, gabarit habituel, **contour corail `#FF6A55`** pour cet épisode).
  - Petit « Simulation 3D » (y 243, à droite, comme snooze et heure offerte).
  - **L1 (≤ 4 mots, ex. « Un petit verre »)** : SemiBold 78, blanc `#F4F7FF`.
  - **L2 (≤ 3 mots, ex. « pour te réchauffer ? »)** : Black 128, blanc, **le mot « réchauffer » en corail `#FF6A55`** avec lueur chaude serrée. Accroche ≤ 10 mots au total, lisible à l'image 0.
  - **L3 (boucle ouverte, entre à 1,6 s seulement, ≤ 5 mots, ex. « Ta peau va te mentir. »)** : Medium 44, `#B9C6EE`, y 720.
- Voile sombre sans bord derrière L1-L2 (radial `rgba(7,12,34,.55)` → 0).
- **Signature** : PNG officiel, 240 px, en bas (y 1585, gabarit snooze) **au-dessus du garde-corps** (voile local sombre derrière pour le contraste, leçon du 24/10).

**Pourquoi elle arrête le pouce** : un lieu que tout skieur reconnaît en une demi-seconde (le garde-corps, les skis dans le vide) + **une situation humaine qui demande une réponse** (on te tend un verre : tu le prends ?) + une question qui touche une croyance que presque tout le monde a.

**Couverture** = image à **1,8 s** (image 0 + L3 « Ta peau va te mentir. »), identique à l'image 0 sinon. Tout le sens dans le carré central (y 420-1500).

### Événements
- **Avant 1 s : 0,80 s (image 24)** : un **pylône passe au-dessus** (ombre qui balaie l'image, « clac-clac-clac » des galets, **petite secousse** de la chaise de 0,4° et le bouchon tendu tremble). Rien n'est répondu : le lieu devient vivant.
- **Waouh 1 : 6,00 s (image 180) — « le flush »** : après la gorgée, en 0,5 s, **le réseau des vaisseaux de ta main s'allume en corail** du poignet au bout des doigts, et **les bords du cadre rougissent**. Battement de cœur grave.
- **Waouh 2 : 10,00 s (image 300) — « la fuite »** : 250 ms de silence (9,75-10,00), puis **rafale** : des centaines de braises corail **arrachées des doigts** filent vers l'arrière, traînées par le mouvement du télésiège ; en même temps **la braise de la poitrine vire au bleu glacier** et du givre pousse sur son contour (0,8 s).
- **Révélation personnelle (deux tiers) : 14,2 s** : « Tu as chaud… et tu refroidis. » sur l'image coupée en deux températures (bords corail, centre bleu).
- **Boucle : 24,4-25,0 s** : la moufle du voisin re-tend le bouchon, le pylône suivant approche : la dernière image **raccorde à l'image 0** (mêmes positions ; le ciel revient de la nuit à l'heure bleue en 12 images par un fondu « d'éblouissement » de la lumière de la station, justifié comme un passage de pylône qui masque le cadre 3 images).

---

## 4. Palette (deux dominantes par plan, maximum)

| Rôle | Hex | Usage |
|---|---|---|
| Ciel heure bleue | zénith `#0B1636` · milieu `#1E3170` · horizon `#5B6FB8` · bande `#8D8FD0` très fine | Décor 0-12 s ; glisse vers la nuit `#070C22` / horizon `#26346E` de 12 à 20 s |
| Neige | lumière `#C9DAF5` · ombres `#4A5F9E` · scintillement `#FFFFFF` (points) | Pente, toits, sapins poudrés |
| Silhouettes | `#0A1024` | Sapins, pylônes, câble, chaises |
| **Chaleur de surface (sensation)** | corail `#FF6A55` cœur · halo `#FF9C82` · ombre `#B8342B` | Vaisseaux de la main, bords du cadre, braises qui s'envolent, mot « réchauffer » |
| **Braise du centre du corps** | ambre `#FFB547` → or pâle `#FFE2A3` | La « vraie » réserve de chaleur ; rime avec l'or de la signature |
| **Vérité / froid du centre** | bleu glacier `#6FB6FF` · givre `#D8EEFF` | Braise refroidie, liseré de givre des mots vrais, verdict |
| Lumières de station | `#FFC36B` (points flous) | 6-10 points en bas à gauche |
| Matières | métal brossé `#9AA6C2` (garde-corps, flasque) · moufle `#2C3140` · veste du spectateur `#1B2A55` · manche voisin `#3A4258` · peau `#C99282` (lumière froide) | Corps et objets |
| Texte | `#F4F7FF` · secondaire `#B9C6EE` | Calque HTML |
| Signature | PNG officiel (or + trèfle) | **Jamais redessinée, jamais recolorée** ; aucun autre vert à l'image |

**Ce qui change par rapport aux ép. 1-3** : on quitte le violet dominant et le « fond nuit uni » pour un **paysage bleu glacier lumineux** (la neige renvoie le ciel), et le couple **corail / bleu glacier** remplace le couple violet / or. L'ADN néon reste : lueurs serrées, une couleur chaude qui brille sur du bleu.

---

## 5. Décor 3D, matières, éclairage (budget SwiftShader ≤ 6 s / image)

**Unités** : 1 unité = 1 m. Le câble monte en +z avec une pente de 22°. La caméra est à 0 m au-dessus de l'assise, tête à 0,75 m.

| Objet | Géométrie (procédurale) | Matériau / astuce |
|---|---|---|
| **Pente** | `PlaneGeometry` 60 × 140, 96 × 192 segments, déplacement par bruit fBm (bosses 0,4 m) + 2 traces de dameuse (sillons en sinus) | `ShaderMaterial` neige : lambert enveloppé + ciel en lumière ambiante + **scintillement** (hachage par cellule, 1 % des cellules flashent selon `t`) ; brouillard exponentiel couleur horizon |
| Sapins | `InstancedMesh` de 3 cônes empilés (12 côtés), **≤ 260 instances**, échelle 3-9 m, poudre de neige = 2e instance de cônes blancs plus petits décalés vers le haut | Couleur `#0A1024` → brouillard ; pas d'ombres |
| Crêtes lointaines | 3 plans avec contour par bruit (alpha) **peints une fois** dans un canvas 1024 × 512 | Couleurs de brume dégradées ; parallaxe lente |
| Ciel | Sphère inversée, dégradé dans le shader, `uNight` 0 → 1 | — |
| Câble montant / descendant | 2 × `TubeGeometry` r 0,025, chaînette légère | `#0A1024` + reflet fin |
| Pylônes | 2 instances (tube r 0,35, h 12 + traverse + 2 batteries de galets en cylindres) | Métal sombre |
| Chaises montantes (devant) | 6 instances : suspente (tube) + banc (box arrondie) + garde-corps ; 1 ou 2 silhouettes de dos assises (capsules), **à 15-60 m : aucun détail** | Silhouettes `#0A1024` |
| **Chaises descendantes (métronome)** | 3 instances qui boucle sur le câble d'en face à 4,5 m à gauche, **une passe toutes les 2,4 s** (vitesse relative 5,4 m/s) | Vides ; passage net en 0,5 s, flou de mouvement simulé par étirement de l'échelle en z (×1,6) |
| **Garde-corps + repose-skis** | Tubes (r 0,025) + coudes en tore | `MeshStandardMaterial` métal 0,8 / rugosité 0,35, carte d'environnement = PMREM d'une petite scène de ciel (calculée une fois) |
| **Tes jambes, tes skis** | 2 capsules (cuisses) vues du dessus + 2 boîtes arrondies 1,7 × 0,07 × 0,02 (skis) **qui pendent** (spatules en bas du cadre, légère rotation pendulaire ±2°) | Pantalon `#1B2A55` rugueux ; skis : dessus graphique **sans logo** (deux bandes corail / gris) |
| **Ta moufle gauche** | Capsule aplatie + capsule pouce, coutures = 2 tores fins | Tissu matelassé : normale procédurale en losanges dans le shader |
| **Ta main droite nue** (héroïne) | Paume = sphère aplatie (0,085 × 0,03 × 0,09) ; **4 doigts = 3 capsules chacun disposées en arc autour du gobelet** (rayon gobelet 0,024 m : les doigts « l'enveloppent » naturellement) ; pouce 2 capsules ; poignet capsule ; **manchette de veste** (cylindre côtelé) | `ShaderMaterial` peau : lambert enveloppé (lumière ciel bleue) + rétrodiffusion rouge sur les bords minces (`pow(1-NdotV,2)`) ; **`uFlush`** (0 → 1) : teinte vers `#E79A86` ; **`uVeins`** : réseau de vaisseaux = bruit « ridged » à domaine déformé en coordonnées objet, trait `1 - smoothstep(0, w, abs(n))`, **largeur `w` animée par `uDilate`** (0,02 → 0,055 : on voit les vaisseaux s'élargir), émissif corail additif. **Flou fort** sur l'arrière-plan derrière la main (voir post) pour cacher les primitives |
| **Bras du voisin + flasque** | Manche (capsule longue) + moufle ; flasque = boîte arrondie plate 0,09 × 0,14 × 0,025 ; bouchon-gobelet = cylindre ouvert r 0,024, h 0,035 | Métal brossé (rayures anisotropes simulées par bruit étiré) ; **aucune étiquette, aucun liquide visible, aucun reflet doré** |
| **Ta veste + fermeture éclair** (révélation, 7,6-14,4 s) | Quand la caméra baisse les yeux : plan de veste matelassée (2 panneaux) + glissière (petite boîte) qui descend ; **ouverture = `discard` dans une fente qui s'élargit** sur 0,6 s | Derrière la fente : **la braise** |
| **La braise du centre du corps** | Sphère r 0,09 + 2 coques additives (r 0,14 et 0,22) + 300 points scintillants dedans | Couleur `uCore` : ambre `#FFB547` → bleu glacier `#6FB6FF` ; **givre** = 40 aiguilles (petits cônes) qui poussent sur la coque externe quand `uCore` > 0,7 |
| **Filets de chaleur** (braise → main) | 3 `TubeGeometry` le long d'une courbe épaule-coude-poignet **sous** la manche, visibles par transparence additive (on « voit à travers » la manche seulement le filet, pas de radio) | Corail, lumière qui court (texture de bandes défilantes) |
| **Braises qui s'envolent** | `Points` **1 800**, nés sur la surface des doigts (positions pré-échantillonnées), vent + vitesse de la remontée → traînées vers l'arrière | Additif corail, taille 2-6 px, durée de vie 1,2 s |
| Neige qui tombe | `Points` 1 200, 3 profondeurs | Blanc, flou par la taille |
| Buée (souffle) | 4 sprites ronds additifs nés en bas du cadre (y 1700 écran) | Pour le texte « de souffle » |
| **Saint-Bernard au néon** (2,4-4,6 s) | **Pas en 3D** : chemin SVG (contour du chien + tonnelet, ≈ 12 tracés) dans le calque HTML, **projeté sur la neige** par une transformation CSS 3D (perspective qui suit la pente), tracé par `stroke-dashoffset` puis dispersé (masque bruité + translation vers la gauche) | Or `#FFD27A`, lueur `drop-shadow` serrée |

**Éclairage** : 1 `HemisphereLight` (ciel `#5B6FB8` / sol `#C9DAF5`) + 1 directionnelle faible froide ; **aucune ombre calculée** ; les seules lumières chaudes sont émissives (braise, vaisseaux, station). La braise **éclaire** la doublure de la veste par un terme ajouté dans le shader de la veste (distance à la braise), pas par une vraie lumière.

**Post-traitement** : `UnrealBloomPass` à **demi-résolution**, seuil 0,85 (seuls corail, ambre, lumières de station fleurissent) ; **faux flou de profondeur** : l'arrière-plan lointain (crêtes, ciel) est déjà flou dans son canvas, la pente reçoit un flou de 2 passes seulement dans les plans « macro » (scènes 4-5) par une `ShaderPass` qui lit la profondeur ; grain 3 % ; vignette. Pas de `BokehPass` (trop lourd en SwiftShader).

**Caméra (innovation 1 + 2)**
- Position = point du câble à `s(t) = 2,3 × t` m + oscillation pendulaire de la chaise (±0,6°, 0,35 Hz) + **secousse** au passage des pylônes (amortie, 0,4°).
- Regard par **gestes de tête** (courbes d'animation, pas de Catmull-Rom) : regard pente −18° (0-4,6 s) · **gorgée** : bascule vers le haut +25° en 0,35 s, tenue 0,3 s, retour 0,4 s (4,9-5,9 s) · regard main, léger rapprochement (macro) (6,0-9,4 s) · **baisser les yeux vers la poitrine** −55° (9,4-10,0 s) · retour à la pente avec la main au premier plan (14,2 s) · regard au loin vers les crêtes (19,4 s) · retour au cadrage de l'image 0 (24,0 s).
- FOV 58° (POV humain : grand-angle léger, on voit ses genoux et l'horizon).

**Déterminisme** : tout dépend de `t = frame / 30` ; graines fixes (`mulberry32`) ; braises et neige calculées par formule fermée de `t` (pas d'intégration pas à pas).

---

## 6. Calque texte (HTML/CSS), typographie cinétique, zones sûres

- **Polices** (déjà dans `fonts/`) : `InterDisplay-Black` (mot fort, verdict), `InterDisplay-SemiBold` (phrases), `InterDisplay-Medium` (mentions, source), `InterDisplay-BlackItalic` pour « Mais… » s'il est utilisé.
- **Densité** : ≤ 0,25 s par mot, **≤ 100 mots au total**, ≤ 8 mots par phrase, 2 niveaux de texte par plan au plus, jamais plus de 12 mots à l'écran.
- **Zone texte** : y 300-760 (au-dessus du paysage) ; mention permanente en bas y 1520-1560 au-dessus de la signature : « Simulation 3D ». Jamais de texte sur la main ou sur la braise.
- **Entrée « souffle »** (innovation 7, 12 images) : un sprite de buée monte depuis le bas du cadre jusqu'à la ligne ; le texte apparaît **dans la buée** (`filter: blur(14px) → 0`, `opacity 0 → 1`, `letter-spacing .08em → 0`) ; la buée se dissipe vers le haut et à gauche (vent).
- **Mots « chauds »** (sensation : réchauffer, chaud) : corail `#FF6A55` + `text-shadow: 0 0 14px rgba(255,106,85,.55)` + **ondulation de chaleur** très légère (filtre SVG `feTurbulence` + `feDisplacementMap`, échelle 2 px, seulement sur ce mot).
- **Mots « vrais »** (refroidit, hypothermie, verdict) : blanc + **liseré de givre** (`-webkit-text-stroke: 1.5px #D8EEFF` + masque de cristaux en dégradé conique répété) ; à l'entrée, le liseré **pousse** de gauche à droite (masque animé, 10 images).
- **Sortie** : le vent emporte le texte vers la gauche (`translateX −40 px`, `blur 0 → 8 px`, 8 images), dans le sens des braises.
- **Étiquette de coin** (facultative, Medium 24, blanc 60 %, coin haut droit sous « Simulation 3D ») : un repère d'altitude qui monte lentement (« 1 840 m » → « 1 905 m ») comme sur un affichage de masque de ski : **décor fictif, aucun chiffre scientifique**. À supprimer si l'écran paraît chargé.

---

## 7. Découpage plan par plan (emplacements ; changement visuel ≤ 2,5 s)

Un seul plan-séquence : les « plans » sont des temps du même trajet.

| Plan | Temps | Image | Texte (emplacement, à écrire par le scénariste) | Son |
|---|---|---|---|---|
| **1. Accroche** ★ | 0,0-2,4 | Image 0. **0,8 : pylône** (ombre, secousse, bouchon qui tremble). 1,6 : L3 entre (souffle). 2,0 : chaise descendante n° 1 croise à gauche. | L1 + L2 (≤ 10 mots, ex. « Un petit verre pour te réchauffer ? ») · 1,6 L3 (≤ 5 mots, ex. « Ta peau va te mentir. ») | Vent d'altitude, ronronnement du câble ; **0,8 clac-clac-clac** ; woosh 2,0 |
| 2. Le mythe | 2,4-4,6 | La caméra regarde la neige sous les skis : **le Saint-Bernard au néon d'or se dessine** et trotte (tracé 1,0 s, tonnelet en dernier, petit éclat). 4,2 : rafale, le dessin **s'envole en neige**. 4,4 : chaise n° 2. | ≤ 9 mots, ex. « Le Saint-Bernard, le vin chaud, la flasque du ski… » · facultatif petit (≤ 7 mots, si validé) : « (le tonnelet ? une invention de peintre) » | Petit carillon de traçage (notes ascendantes douces) ; souffle de rafale qui efface |
| 3. La gorgée + **waouh 1** ★ | 4,6-7,0 | 4,6 : ta main droite nue entre par le bas et prend le bouchon (le bras du voisin se retire). **4,9-5,9 : gorgée** (caméra vers le ciel et retour ; on ne voit pas le liquide). **6,0 : le flush** : vaisseaux corail de la main, bords du cadre qui rougissent. 6,8 : chaise n° 3. | ≤ 5 mots, ex. « Oui, ça chauffe. » (mot « chauffe » corail) | Clic du bouchon ; **pas de bruit de déglutition** ; 6,0 nappe chaude grave qui gonfle + **battement de cœur** (sous-grave 55 Hz) |
| 4. Les vaisseaux s'ouvrent | 7,0-9,4 | Rapprochement sur la main (macro, arrière-plan flou) : **les traits des vaisseaux s'élargissent** (innovation 3). 8,4 : les filets de chaleur apparaissent dans la manche et **remontent vers le corps** (on comprend que la chaleur vient d'ailleurs). 9,2 : chaise n° 4. | ≤ 8 mots, ex. « Les vaisseaux de ta peau s'ouvrent. » · 8,4 petit (≤ 7 mots) ex. « Le sang chaud monte en surface. » | Battement qui continue ; frottement doux de tissu |
| 5. La source + **waouh 2** ★ | 9,4-11,8 | 9,4 : **la caméra baisse les yeux** vers ta poitrine ; la fermeture éclair descend seule (9,5-10,0) et révèle **la braise ambre**, reliée à la main par les filets. **9,75-10,00 silence.** **10,0 : rafale** : braises arrachées des doigts, la braise de la poitrine **vire au bleu glacier**, givre. 11,6 : chaise n° 5. | ≤ 8 mots, ex. « Cette chaleur vient d'ici. » puis 10,4 (givre) ex. « Et elle s'envole. » | Zip (bruit filtré montant) ; **silence 250 ms** ; rafale + cristallisation (crépitements aigus) ; le battement ralentit |
| 6. **Partage** (avant 13 s) | 11,8-14,2 | **12,0 : 2e pylône** (secousse). La caméra revient à la pente ; **le bras du voisin réapparaît et, gêné, range la flasque dans sa poche** (petit geste comique, 0,8 s). | ≤ 10 mots, ex. « Envoie ça à celui qui sort la flasque au ski. » | 12,0 clac-clac-clac ; froissement de poche ; petite note « pouf » ironique |
| 7. **Révélation personnelle** ★ | 14,2-16,8 | Image à deux températures : **bords du cadre encore corail** (tu as chaud), **braise visible en incrustation douce au centre-bas, bleue** (tu refroidis). La nuit gagne, les lumières de la station s'allument une à une. 16,4 : chaise n° 6. | ≤ 6 mots, ex. « Tu as chaud… et tu refroidis. » (« chaud » corail, « refroidis » givre) | La nappe chaude se dérègle (désaccord léger), vent plus fort |
| 8. Le vrai risque + verdict | 16,8-19,4 | Neige plus dense, vent oblique, ciel presque nuit. **18,4 : verdict** qui entre avec le givre (Black ≥ 140). | ≤ 8 mots, ex. « Par grand froid : risque d'hypothermie. » · verdict (ex. « MYTHE », au choix du scénariste) · petit source (≤ 8 mots, fiche) | Rafale ; **tampon sourd** au verdict ; crépitement de givre |
| 9. Le geste utile | 19,4-21,8 | La caméra regarde au loin ; **le même bouchon**, tenu par ta main, **fume** maintenant (boisson chaude **sans alcool**, vapeur visible) ; les bords du cadre redeviennent neutres, la braise (incrustation) reprend un peu d'ambre. 19,0 et 21,4 : chaises. | ≤ 9 mots (à valider par le vérificateur), ex. « Pour te réchauffer : boisson chaude sans alcool, bouger. » | Nappe qui se résout (accord consonant) ; vapeur (souffle doux) |
| 10. Fin + ép. 5 | 21,8-24,4 | Grande signature (gabarit `#sig` + `#sigShine`) ; « @lifestyles_hf » ; **« Ép. 5 : [sujet] → abonne-toi »** SemiBold 52 ; sources Medium 24. La remontée approche de l'arrivée (lumières de la gare d'arrivée en haut du cadre). | ex. « Ép. 5 : sortir les cheveux mouillés rend malade ? Abonne-toi. » | Vent apaisé ; ronronnement du câble |
| 11. Boucle | 24,4-25,0 | Le bras du voisin **re-tend le bouchon** ; un pylône approche ; dernière image **= image 0** (L1 + L2, sans L3). | L1 + L2 | **24,8 : début du clac-clac** (raccorde au 0,8 s de la boucle) |

**Mots comptés (exemples)** : ≈ 85 mots sur 25 s (≤ 100). Le scénariste peut couper le petit texte du plan 2 en premier.

**Mention écran permanente** : « Simulation 3D » (en haut à droite). **Légende (pas à l'écran)** : précaution de la fiche (ex. « Par grand froid, pas d'alcool pour se réchauffer. Signes d'hypothermie : appelle le 15 ou le 112. Ceci n'est pas un avis médical. ») : texte exact par le vérificateur.

---

## 8. Son (original, synthétisé dans `audio.py`, zéro dépense)

| Couche | Description | Niveau |
|---|---|---|
| **Fil rouge : la remontée** | Ronronnement du câble (bruit rose filtré 60-120 Hz + légère modulation 0,35 Hz calée sur l'oscillation de la chaise) · **woosh des chaises descendantes** toutes les 2,4 s (bruit filtré passe-bande avec effet Doppler : fréquence qui descend pendant le croisement, panoramique gauche → arrière) | −24 LUFS court terme |
| **Pylônes** | « Clac-clac-clac » : 3 transitoires métalliques (impulsion + résonances 900 / 1 400 / 2 300 Hz, déclin 80 ms) espacés de 90 ms, à 0,8 s, 12,0 s et 24,8 s | crêtes −3 dBTP, précédées de 120 ms de vide |
| Ambiance | Vent d'altitude (bruit blanc passe-bas 400 Hz, rafales lentes), neige (aucun bruit propre) | −28 |
| **Chaleur** | 6,0 s : nappe chaude (accord majeur grave, attaque lente) + **battement de cœur** (2 impulsions sous-grave 55 Hz, 66 bpm) qui ralentit à partir de 10,0 s (56 bpm) puis s'arrête à 16,8 s | −20 |
| **Froid** | 10,0 s : rafale + **cristallisation** (crépitements aigus : courtes rafales de bruit filtré 6-9 kHz, densité croissante) ; repris à 18,4 s (verdict) | −22 |
| Gestes | Clic du bouchon (4,6) · zip (9,5) · froissement de poche (12,8) · vapeur (19,6) | −18 |
| Texte | Pas de son à chaque mot (gabarit) : seul le verdict a un tampon sourd | — |
| Mixage | Intégré −14 LUFS ; plafond −3,5 dBFS avant l'AAC (leçon du 24/10) ; **piste non muette vérifiée** par `tools/qa/check_reel.py` | — |

**Interdits sonores** : déglutition, glouglou, glaçons, trinquer (« santé ! »), rires de fête, musique de bar.

---

## 9. Ce qu'il faut éviter

1. **Glamour de l'alcool** : aucun liquide ambré en gros plan, aucun reflet doré sur la boisson, aucun versement au ralenti, aucun trinquage, aucune ambiance festive, aucune bouteille. La flasque est un objet banal en métal, vu de loin, puis **rangée** (plan 6).
2. **Marque** : aucune étiquette, aucun logo (flasque, skis, vestes, masque), aucun nom de station réelle.
3. **Visage identifiable** : le voisin n'existe que par une manche et une moufle ; les skieurs au loin sont des silhouettes de dos sans détail. Le spectateur n'a pas de visage (POV).
4. **Refaire l'ép. 3** : pas de filtre thermique plein cadre, pas de palette fer, pas de silhouette de particules dorées, pas de fond violet uni.
5. **Moralisme ou peur** : pas de tête de mort, pas de rouge « danger » clignotant, pas de corps allongé dans la neige. Le ton reste celui d'un ami qui sait.
6. **Chiffres non validés** : aucune température, aucun pourcentage, aucun « −X °C » à l'écran sans la fiche VALIDÉE. L'altitude décorative (facultative) n'est pas un chiffre scientifique.
7. **Surcharge** : un seul effet fort par temps (flush à 6,0, fuite à 10,0). Le Saint-Bernard ne revient pas. Le texte ne passe jamais sur la main.
8. **Contexte légal** : en France, la loi Évin encadre la publicité pour l'alcool ; ce Reel est de l'information santé **sans aucune incitation**. Ne jamais associer l'alcool à une image positive (sport réussi, sommet, coucher de soleil glorieux au moment de la gorgée). La gorgée a lieu sous un ciel neutre et l'effet positif est immédiatement contredit.

---

## 10. Points de vigilance scientifiques (à transmettre au vérificateur)

- **Nuance sur la température centrale** : une revue de portée de 2024, citée par [The Week (01/2026)](https://www.theweek.in/news/health/2026/01/11/fact-check-does-alcohol-really-keep-you-warm-during-winters.amp.html), trouve une baisse de la température centrale **dans la plupart des études**, avec des preuves limitées, et **pas d'altération nette chez de jeunes hommes en bonne santé** à certaines doses. Un petit essai en eau froide (8 hommes) donne ≈ −1,0 °C sous alcool contre ≈ −0,66 °C sous placebo. → La formulation écran la plus sûre est sans doute « **ton corps perd sa chaleur plus vite** » plutôt que « ta température chute ». La braise qui bleuit est une **image**, pas une mesure : garder « Simulation 3D ».
- **Le tonnelet du Saint-Bernard** : selon [Mental Floss](https://www.mentalfloss.com/animals/dogs/10-big-facts-about-saint-bernards) et l'[AKC](https://www.akc.org/expert-advice/dog-breeds/saint-bernard-history/), il viendrait d'un tableau d'Edwin Landseer (années 1820) et les chiens n'en auraient jamais porté. **À vérifier en source primaire** (Fondation Barry, Hospice du Grand-Saint-Bernard) avant d'afficher le petit texte du plan 2 ; sinon le supprimer (le dessin seul suffit).
- **Rougeur de surface** : la thermographie de Patras (2012 : nez plus chaud, front plus froid, [ScienceDaily](https://www.sciencedaily.com/releases/2012/09/120904100137.htm)) appuie l'image « la peau chauffe ». Ne pas montrer de visage : la main suffit.
- **Le geste utile** (plan 9) : formulation à valider (boisson chaude sans alcool, bouger, se couvrir, s'abriter) ; ne rien promettre.

---

## 11. Faisabilité et temps

| Élément | Moteur maison | Plan réel d'Anthony | OpenArt |
|---|---|---|---|
| Pente, sapins, crêtes, ciel qui tombe en nuit, câbles, pylônes, chaises | **Oui** (plans à bruit, instances, canvas peint une fois) | — | — |
| Garde-corps, genoux, skis, moufle, bras du voisin, flasque | **Oui** (tubes, capsules, boîtes arrondies, métal PMREM) | — | — |
| **Main nue autour du gobelet** | **Oui, point le plus risqué** : capsules en arc autour du cylindre + shader peau ; flou d'arrière-plan et cadrage partiel (pouce et 4 doigts, paume à moitié hors champ) pour éviter l'effet « main en saucisses » | Option : **photo de référence** (Anthony tient un gobelet de thermos devant une fenêtre, 2 min) pour caler les proportions | — |
| Vaisseaux, braise, filets, braises au vent, givre | **Oui** (shader + `Points` + petits cônes) | — | — |
| Saint-Bernard néon | **Oui** (SVG tracé dans le calque HTML, transformation 3D CSS) ; le contour se dessine à la main une fois (≈ 12 tracés) | — | — |
| Son | **Oui** (`audio.py`, synthèse) | Option : 30 s de prise réelle (clic d'un bouchon de thermos, zip de veste) | — |
| Plan photoréaliste | **Non retenu** : un télésiège photoréaliste d'IA avec flasque risque le « glamour » et la marque implicite ; notre 3D stylisée, étiquetée « Simulation 3D », est plus sûre | — | — |

**Budget de rendu (objectif ≤ 80 min)** : 750 images × ≤ 6 s = **≤ 75 min** sur 2 cœurs.
- Mesurer les images 0, 6,0, 10,2 et 18,4 en aperçu dès que la scène tourne. **Si > 6 s / image**, dans cet ordre : sapins 260 → 120 · braises 1 800 → 900 · neige 1 200 → 600 · bloom en quart de résolution · pente 96 × 192 → 64 × 128 · supprimer l'innovation 6 (garder le ciel fixe).
- Correction de texte après rendu : re-rendre seulement les segments touchés (leçon du 23/10).
- Vérifier le nombre d'images avec `ffprobe -count_frames` (capture.py peut en perdre 2 à la fin).

**Temps estimé** : scène 3 h (dont main 1 h) ; aperçus 15 min ; rendu ≤ 75 min ; audio 30 min.

**Planche de contrôle** : `capture.py --apercu 0,0.8,1.8,3.4,4.4,5.3,6.2,8.6,9.8,10.4,12.1,13.2,15.0,18.6,20.4,23.0,24.97`.
Contrôleur : accroche lisible à l'image 0 **et** en vignette 395 px · bras tendu et bouchon visibles sans chevauchement avec le texte · vaisseaux allumés à 6,2 · braise ambre à 9,8 puis bleue à 10,4 · flasque rangée à 13,2 · aucun liquide visible, aucune marque, aucun visage · dernière image = image 0.

---

## 12. Couverture

= image à **1,8 s** : POV télésiège heure bleue, garde-corps et skis au-dessus du vide, **la moufle du voisin qui tend le bouchon de flasque**, accroche L1 + L2 (« réchauffer » en corail) + L3 « Ta peau va te mentir. », pastille « MYTHE OU SCIENCE ? · ÉP. 4 » à contour corail, « Simulation 3D », signature en bas. Recadrages 4:5 et carré : tout le sens dans y 420-1500 (accroche + bouchon tendu). Titre TikTok dédié (leçon du 23/10), ex. « L'alcool réchauffe vraiment ? Mythe ou science ép. 4 #apprendresurtiktok #ski ».

---

## 13. Épisode 5 (proposition)

**« Sortir les cheveux mouillés, ça rend malade ? »** : même famille « mythes d'hiver » (la presse allemande les range ensemble : [Joyn](https://newstime.joyn.de/themen/panorama/von-nassen-haaren-bis-gluehwein-die-groessten-winter-irrtuemer-34599)), situation plus concrète et plus personnelle que « le froid donne le rhume ? » (POV devant la porte, cheveux qui gouttent), cible de partage évidente (« envoie ça à ta mère »). Garder « Le froid donne le rhume ? » pour l'ép. 6. Visuellement, l'ép. 5 devra encore changer de lieu (entrée d'immeuble au petit matin, pas de montagne, pas de braise).

---

## 14. Références par choix

| Choix | Références |
|---|---|
| La chaleur comme matière qui raconte (sans filtre thermique) | [D&AD — NOMINT / WWF « In Hot Water »](https://www.dandad.org/work/d-ad-awards-archive/in-hot-water) · [Gerety 2025](https://www.geretyawards.com/winners/2025/entry/186529/in-hot-water-wwf) · [ScienceDaily — thermographie Patras 2012](https://www.sciencedaily.com/releases/2012/09/120904100137.htm) |
| Plan-séquence porté, son calé sur l'action | [Anijam — tendances Reels 10/2026](https://www.anijam.ai/blog/instagram-reels-trends/) · [mean.ceo — tendances 10/2026](https://blog.mean.ceo/?p=10938) · [mean.ceo — format court 10/2026](https://blog.mean.ceo/?p=10995) |
| POV avec un corps, lieu vécu, interface de masque | `data/lecons.md` (piéton 70 % > 3 s) · [InTheSnow — masques à affichage 2026](https://www.inthesnow.com/smart-goggles-and-airbag-vests-the-must-have-ski-tech-for-2026/) · veille 23/10 (« POV depuis le lit ») |
| Le mythe en image (Saint-Bernard) | [Mental Floss](https://www.mentalfloss.com/animals/dogs/10-big-facts-about-saint-bernards) · [AKC](https://www.akc.org/expert-advice/dog-breeds/saint-bernard-history/) · [Woot — The Debunker](https://woot.com/blog/post/the-debunker-did-st-bernards-ever-carry-barrels-of-brandy-around-their-necks) |
| Typo cinétique selon la physique (souffle, givre, chaleur) | [Design Monks — typo 2026](https://www.designmonks.co/blog/typography-trends-2026) · [Videobolt 2026](https://blog.videobolt.net/post/top-motion-graphics-trends-2026) · veille 18/10 |
| Potentiel de partage du sujet | [The Week 01/2026 — Reel Bhawesh Gupta ≈ 4 000 partages](https://www.theweek.in/news/health/2026/01/11/fact-check-does-alcohol-really-keep-you-warm-during-winters.amp.html) · [Newsis (Corée)](https://www.newsis.com/view/NISX20250106_0003022427) · [Utopia (Allemagne)](https://utopia.de/ratgeber/gluehwein-zum-aufwaermen-warum-das-keine-gute-idee-ist/) |

---

## 15. Prédiction (à comparer avec l'analyste à J+1 et J+3)

- **Vues > 3 s ≥ 60 %** (hypothèse : lieu vécu en POV + geste humain qui appelle une réponse + corps du spectateur dans l'image). Sous 45 % : le paysage stylisé est lu comme « jeu vidéo » → test suivant : même accroche sur un plan réel d'Anthony (mains autour d'un gobelet dehors).
- **Partages ≥ 8 / 1 000** : la cible est **dans l'image 0** (la moufle qui tend la flasque) et nommée à 11,8 s ; le Reel indien du même sujet atteint ≈ 14 / 1 000 (déclaré).
- **Rétention** : pas de chute avant 6,0 s (flush) ; si chute entre 2,4 et 4,6 s, le Saint-Bernard est trop long → le réduire à 1,2 s.
- **Boucle** : le bras qui re-tend le bouchon à 24,4 s doit pousser au revisionnage (durée moyenne > 100 %).
