# Brief créatif — « Mythe ou science ? » ép. 3 : on perd la moitié de sa chaleur par la tête ?

Agent 16 (directeur de création « monde ») · 19/10/2026 (pour publication 20/10) · mode RAPIDE · Statut : **BRIEF PRÉPARÉ** (rien n'est rendu, rien n'est testé).
Entrées : `work-tete/fiche-validee.md` (**seuls chiffres autorisés** : 40-45 % = le mythe · ≈ 7 % · 19 % · ≈ 10 % · +42 %) · `docs/veille-visuelle.md` (session du 19/10) · `data/lecons.md` · briefs vitamine C, piéton, doigts · couvertures piéton et doigts.
`work-tete/script.md` n'existait pas à la fin de la recherche : les textes ci-dessous sont des **emplacements** (taille, nombre de mots). Le scénariste les remplit ; le directeur ne fixe aucun chiffre hors fiche. **Aucune température en °C à l'écran** (le viseur n'affiche aucun nombre : voir §6).
Format : 1080×1920, 30 i/s, **24,0 s = 720 images** (23-25 s autorisé). Moteur : `tools/motion-engine/capture.py` (`window.sceneReady`, `window.renderAt(t)`), three.js r187 (vendor), SwiftShader. Partir du squelette `exemples/2026-10-19-mythe-craquer-doigts/index.html` (importmap, utilitaires déterministes, signature PNG + `#shine`, pastille de série) et **jeter toute la scène**.

---

## 0. Remise en question (sans complaisance)

**Ce que disent les chiffres** : le seul Reel 3D qui tient à 3 s (piéton, 70 %) montre **un lieu crédible et une situation humaine vue en POV** ; la 3D abstraite (vitamine C, 23,5 %) n'accroche pas. L'image 0 doit être comprise comme une **image du monde réel**, pas comme une illustration.

**Ce qui fait « déjà vu » chez nous**
1. **Trois épisodes, trois fonds bleu-violet sombres avec un objet translucide au centre** (verre, os radio). Le doigt radio de l'ép. 2 et le verre de l'ép. 1 sont la même idée : « objet fantôme qui luit sur fond nuit ». Ép. 3 doit casser ce gabarit.
2. **Le texte reste un calque blanc posé sur la scène** (ép. 2 a fait vivre le mot ARTHROSE, mais le reste du texte est resté du blanc standard). La couleur du texte ne dit rien.
3. **La donnée est toujours un objet ajouté** (jauge de bulles, jauges-os, compteurs) au lieu d'être **lue dans l'image elle-même**.
4. **Nos caméras glissent toutes de la même façon** (Catmull-Rom douce, orbite lente). Aucune caméra « de terrain » avec son caractère propre.
5. **Le piéton a déjà fait la rue de nuit** : une rue d'hiver sombre avec immeubles, réverbères et pluie serait une redite. La rue de l'ép. 3 n'existe **qu'en thermique** : pas de réverbère, pas de pluie, pas de phares, pas de marquage au sol.
6. **Mise en garde** : l'esthétique thermique est en train de devenir un **préréglage** (Remotion propose `thermalVision()` en un appel, [doc](https://remotion.dev/docs/effects/thermal-vision)). Un simple filtre « fer » sur une scène serait déjà banal. Notre différence doit venir de **ce que la caméra thermique raconte**, pas du filtre.

**Ce que les meilleurs font et que nous ne faisons pas encore**
- Utiliser un **appareil réel comme langage** (la caméra thermique, ses bruits, ses défauts, son viseur) : BBC Earth Unplugged, l'homme qui se déshabille dans la neige filmé en thermique, repris en 2016 puis encore en 11/2025 ([VICE](https://vice.com/en/article/two-long-shirtless-minutes-in-the-snow-through-the-lens-of-an-infrared-camera), [TVOvermind](https://tvovermind.com/?p=1305327)).
- **« Tout est révélé par la chaleur, pas par la lumière »** (Hiro Murai, clip « Grief », [Dezeen](https://www.dezeen.com/2015/04/04/grief-earl-sweatshirt-music-video-hiro-murai-thermal-camera/)) : un monde où ce qui est froid disparaît.
- **Le balayage qui révèle** une couche cachée ([Codrops, scan sur carte de profondeur](https://tympanus.net/codrops/?p=90674)).
- **Le son comme preuve de crédibilité** : chaque événement visible a son son ([tendances motion 10/2026](https://blog.mean.ceo/?p=10938)).

**Univers interdits** : eau, bulles, verre, sarcelle (ép. 1) · réverbères, pluie, phares, faisceau, HUD au sol (piéton) · négatoscope, os radio, fente dans le mot (ép. 2) · étoiles, croix, sol quadrillé · compteur rouleau, anneau-minuteur, avion en papier.

---

## 1. Idée maîtresse

> **« Tu regardes quelqu'un de dos à travers une caméra thermique : sa tête nue brille comme un phare, le mythe semble vrai… puis un balayage rend son manteau transparent et tout son corps s'allume : la tête n'était brillante que parce que c'était la seule partie nue. »**

C'est **l'image qui crée le mythe** (les photos thermiques d'hiver montrent toujours une tête blanche sur un manteau violet) et **la même image qui le casse**. La nuance (corps couvert + tête nue = la tête compte) découle naturellement : on rhabille, la tête redevient la seule fuite, le bonnet tombe et **éteint** la tache.

## 2. Innovations retenues (jamais faites chez nous)

| # | Innovation | En quoi c'est neuf | Principe source |
|---|---|---|---|
| 1 ★ | **Rendu « champ de température »** : la scène 3D n'est pas colorée, elle écrit une **température** (0-1) dans une image en niveaux de gris à basse résolution, floutée, puis une seule passe la transforme en couleurs par une table (palette fer). Avec tout le **langage d'une vraie caméra** : bruit de capteur, flou thermique, **déclic d'étalonnage** (NUC : image figée 2 images + clic), **zoom numérique par paliers** (×1 → ×2, sans glissé), **changement de palette** comme transition. Le flou thermique **cache les primitives** : une silhouette en capsules lissées paraît réelle. | Ép. 1-2 : objets « fantômes » éclairés. Ici : **une caméra de terrain**, un POV humain crédible (on tient l'appareil), et une donnée physique réelle (la chaleur) qui produit l'image. | Murai / BBC Earth (veille §1-2) · [Remotion thermalVision](https://remotion.dev/docs/effects/thermal-vision) (même principe luminance → palette, mais nous l'appliquons à un champ calculé, pas à une vidéo) |
| 2 ★ | **Le balayage qui déshabille** (moment waouh) : une ligne de scan horizontale descend sur la silhouette ; au-dessus d'elle, le manteau devient thermiquement transparent et tout le corps s'allume. La « tache chaude » de la tête se **noie** dans un corps entier aussi chaud. | Première fois que **l'image elle-même réfute l'image** (même plan, avant / après). | [Codrops — scan révélateur](https://tympanus.net/codrops/?p=90674) · BBC Earth (veste retirée = corps qui s'allume) |
| 3 | **La barre de palette devient le graphique** : la légende verticale de couleurs à droite du viseur (présente sur toutes les caméras thermiques) se transforme en **barre de surface du corps** ; le segment « tête » mesure 7 %, puis grandit à 19 % pour le bébé. Aucun objet graphique ajouté : la donnée sort de l'interface de l'appareil. | Fin des jauges ajoutées (bulles, os, compteurs). | Interfaces FLIR (veille §5) · [tendances 10/2026 : de vraies interfaces plutôt que des tableaux de bord fictifs](https://blog.mean.ceo/?p=10938) |
| 4 | **Typographie thermique** : les mots **chauffent** pour entrer (indigo → magenta → orange → blanc, même table que l'image, flou de chaleur 10 px → 0) et **refroidissent** pour sortir (retour indigo + bruit de capteur). Le mot du mythe refroidit et se dissout ; le chiffre vrai reste chaud. | La couleur du texte **dit** quelque chose (vrai = chaud, faux = froid). | [Centric — typo héroïne 2026](https://www.centricdxb.com/insights/social-media-design-trends) · veille 18/10 : faire bouger le texte selon la physique du sujet |
| 5 | **Palette « armée » pour le mythe** : la phrase « un vieux manuel de survie de l'armée américaine » passe en **blanc-chaud militaire** (niveaux de gris, réticule), puis retour en fer pour la science. La palette raconte la source. | Changement de palette comme transition narrative. | Clip « Grief » en niveaux de gris ([Dezeen](https://www.dezeen.com/2015/04/04/grief-earl-sweatshirt-music-video-hiro-murai-thermal-camera/)) |

Obligatoires : **1, 2, 3**. 4 et 5 ne coûtent presque rien (CSS et une seconde table de couleurs).

## 3. Image 0 et moments forts

**Image 0 (arrête le pouce ; lisible en vignette 395 px et dans la grille 3:4 y 240-1680)**
- Plein cadre : **vue de caméra thermique**, palette fer. Une personne **de dos**, cadrée de la taille au-dessus de la tête, au centre-bas : **tête nue blanc-jaune éclatant** (haut du crâne à y ≈ 1060, nuque à y ≈ 1270), épaules et manteau **violet-magenta**, fond de rue **indigo presque noir** avec deux fenêtres floues orange (chaleur des intérieurs) à gauche, et des **flocons qui tombent en points sombres** (la neige est froide : elle apparaît noire, comme dans la vidéo BBC).
- Viseur discret (blanc 70 %, traits 2 px) : réticule centré **sur la tête**, petite étiquette « POINT CHAUD » accrochée au réticule, barre de palette verticale à droite (x 990-1010, y 520-1240), mention « IRONBOW » en haut à droite. **Aucun chiffre de température.**
- En haut (y 70) : signature officielle 240 px, opacité 0,85 ; dessous (y 190) **pastille « MYTHE OU SCIENCE ? · ÉP. 3 »** (gabarit ép. 2, contour passé en `#FF8A3D` pour la saison thermique).
- **Ligne 1** (emplacement, ≤ 6 mots, ex. « Tu perds la moitié de ta chaleur ») : Inter Display SemiBold **78 px**, blanc `#FFF6EC`, centrée, lignes de base y 560 et 650.
- **Ligne 2** (emplacement, ≤ 3 mots, ex. « PAR LA TÊTE ? ») : Inter Display Black, taille ajustée pour **900 px de large** (≈ 150-170 px), capitales, centrée sur **y 800**, remplissage dégradé **chaud** vertical `#FFF8E1` → `#FFC24A` → `#FF6A2B` (= le haut de la palette fer : le mot a **la même couleur que la tête**). Lueur serrée `0 0 16px rgba(255,140,60,.5)` + ombre portée sombre `0 6px 30px rgba(10,4,30,.7)`.
- **Ligne 3** (boucle ouverte, entre à 2,0 s seulement) : Inter Display Medium 40, `#E9D9FF`, y 930, ex. « La caméra thermique a l'air d'accord… »
- Voile sombre sans bord derrière L1-L2 (radial `rgba(10,4,30,.55)` → 0) : écart de luminance texte / fond ≥ 120. La tête brillante reste **sous** le texte, jamais derrière.
→ **Couverture = image 0** (avec L3).

**Pourquoi elle arrête le pouce** : l'image thermique est un code connu de tous (et si fascinant qu'on la falsifie : la fausse vidéo « pets en thermique » a fait > 9 M de vues, [Gizmodo](https://gizmodo.com/that-video-of-farts-captured-by-thermal-cameras-looking-1841442780)) ; elle **semble confirmer** la question : tension immédiate.

**Événement avant 1 s : 0,90 s (image 27)** — **déclic d'étalonnage** : clic mécanique, image figée 2 images, léger saut de luminance, puis la palette se **ré-étale** et la tête passe du jaune au **blanc saturé** ; le réticule se verrouille (2 coins qui se resserrent). On ne donne pas la réponse : on renforce le mythe.

**Moment waouh : 6,20 s (image 186)** — **le balayage** (innovation 2). Préparé par 250 ms de silence.
**Second pic : 17,40 s (image 522)** — **le bonnet tombe et éteint la tache** (blanc → violet en 12 images), son de laine + souffle grave descendant.
**Révélation personnelle aux deux tiers : 15,6 s** — « Mais… » (manteau remis, tête nue = seule fuite).

## 4. Palette

| Rôle | Hex | Usage |
|---|---|---|
| Table « fer » (ironbow), 7 arrêts | `#05030F` (0,00) · `#1C0B4A` (0,15) · `#4B1590` (0,32) · `#A0228F` (0,50) · `#E8473A` (0,66) · `#FF9A1F` (0,80) · `#FFE27A` (0,92) · `#FFFBEA` (1,00) | **Toute l'image 3D** passe par cette table. Le froid tombe dans **notre bleu-violet** (style gagnant, `lecons.md`), le chaud dans **l'or** (rime avec la signature). |
| Table « armée » (scène 2 seulement) | `#0A0A0A` → `#FFFFFF` (blanc = chaud) | Le mythe, 2,5 s |
| Texte principal | `#FFF6EC` · secondaire `#E9D9FF` | Calque HTML |
| Texte « vrai » (chiffres de la fiche) | dégradé chaud `#FFF8E1` → `#FFC24A` → `#FF6A2B` | ≈ 7 %, ≈ 10 %, 19 %, verdict |
| Texte « mythe » | `#7A5CC8` puis dissolution | 40 à 45 % (refroidit et s'efface) |
| Viseur | `#FFFFFF` à 70 % | Réticule, coins, barre de palette |
| Signature | PNG officiel (or + trèfle `#5DBB4A`) | **Jamais redessinée, jamais recolorée.** Aucun vert ailleurs (la palette fer n'en contient pas : on évite les palettes « arc-en-ciel » thermiques). |

Deux dominantes par plan : violet froid + or chaud. Pas de cyan, pas de sarcelle.

## 5. Scène 3D (sobre : objectif ≤ 1,5 s / image en SwiftShader)

**Principe de rendu (le cœur de l'innovation 1)**
1. Tous les objets utilisent **un seul `ShaderMaterial` « température »** qui écrit une valeur scalaire `T` dans le canal rouge : `T = uTemp × mix(0.78, 1.0, pow(max(dot(N,V),0.),0.5)) + bruit_lent × 0.02` (les bords rasants paraissent plus froids, comme en vrai). Pas de lumières, pas d'ombres, pas de transmission.
2. Rendu dans une `WebGLRenderTarget` **270 × 480** (quart de résolution : vraie basse définition de capteur, coût minime).
3. **Une** `ShaderPass` finale en 720 × 1280 : flou gaussien 9 échantillons (rayon 1,5 px capteur) → table de couleurs (texture 256×1 ou fonction à 8 arrêts, `uPalette` 0 = fer / 1 = armée, fondu entre les deux) → bruit de capteur seedé 2,5 % + léger motif de colonnes fixes 1 % → vignette 0,3 → `uFreeze` (NUC) et `uStep` (zoom numérique par paliers : on agrandit le centre de l'image capteur, pixels plus gros visibles 3 images puis lissés).
4. Pas de bloom (la palette fait la lueur). Pas de Bokeh.

**Unités** : 1 unité = 1 cm. Personne debout, de dos, pieds en y = 0, hauteur 175.

| Objet | Géométrie | `uTemp` (0-1) |
|---|---|---|
| Tête | Sphère 32×24, échelle (9, 11,5, 10), centre y 163 | **0,95** (nue) → 0,30 sous bonnet |
| Oreilles | 2 sphères aplaties (2,2 × 3,2 × 1) | 0,80 |
| Cou / nuque | Cylindre r 5,5, h 9 | 0,88 (col du manteau le cache à moitié) |
| Torse (corps) | `LatheGeometry` 40 segments, profil lissé (hanches r 16 → taille r 14 → poitrine r 17 → épaules r 19 → base du cou r 6), y 95 → 152, échelle z 0,62 | 0,82 (visible seulement sous le scan) |
| Bras, jambes | `CapsuleGeometry` (r 5,5 / 7,5) | 0,80 (bras) · 0,78 (jambes) |
| Mains | Capsules courtes | 0,60 (gants : 0,32) |
| **Manteau** | Coque Lathe r +3 autour du torse, manches capsules r +2,5, col roulé (tore) ; descend à y 70 | **0,30** ; `uScanY` : fragments au-dessus de la ligne de scan → `discard` (manteau thermiquement transparent) |
| Pantalon | Capsules r +1,5 | 0,34, même `uScanY` |
| **Bonnet** | Demi-sphère r 10,5 + tore (rebord roulé) + pompon (sphère r 3) | 0,28 ; animé en y : 205 → 166 (chute avec rebond 4 % en 9 images) |
| Souffle | 3 sprites ronds additifs (dans le champ de température : `T` = 0,5 → 0), devant le visage, débordent sur les côtés de la tête | Un nuage toutes les 3,2 s, monte et s'éteint en 1,4 s : **la personne est vivante** |
| Rue | 3 plans : façade (T 0,14 + bruit de briques très doux), trottoir (0,10), ciel (0,04) ; 2 fenêtres (rectangles T 0,55, très floues) à gauche, une porte entrouverte (0,45) à droite | Aucun réverbère, aucune pluie |
| Flocons | `Points` 400, taille 2-5 px capteur, **T 0,02 (plus froids que tout : points sombres)**, chute lente seedée | Signature visuelle de la scène |

**Variantes de forme (scènes 3 et 7)**
- **Mythe 40-45 %** : `uMythY` dans le shader du manteau et de la peau : tout fragment au-dessus de `uMythY` prend `T = 0,95`. `uMythY` descend du sommet du crâne jusqu'à la hauteur où ≈ 45 % de la surface visible de la silhouette est « chaude » (à mesurer une fois dans l'aperçu : environ le milieu du dos). Ridicule et clair : « si c'était vrai, ça ressemblerait à ça ».
- **Bébé 19 %** : la silhouette se **transforme** (1,0 s, `eio`) en proportions de bébé emmailloté : groupe corps échelle y 0,38, tête échelle ×0,62 (donc **proportionnellement** énorme), jambes rentrées sous la coque, le tout recentré au même point du cadre. Tête nue blanche. Pas de visage, de dos, sans détail.

**Caméra (« caméra de terrain », innovation 1)** : `PerspectiveCamera` FOV 34°, position (0, 140, 210) → cible (0, 135, 0) (légèrement plongeante, de dos, 3/4 très léger : 6°). **Bougé à la main** : bruit de Perlin seedé, amplitude 0,25° en rotation, 0,3 cm en position, fréquence 0,6 Hz ; jamais immobile.
**Pas de glissé Catmull-Rom** : les changements de cadrage se font par **paliers de zoom numérique** (×1 → ×1,6 → ×1 en 1 image chacun, avec 3 images de gros pixels) et par **une seule** vraie translation (la caméra recule de 30 cm pendant le scan pour que le corps entier entre). C'est le caractère du Reel.

**Budget** : ≤ 25 000 triangles, 0 lumière, 0 ombre, 0 objet transparent réel (tout est opaque dans la cible de température, sauf 3 sprites de souffle), 1 cible de rendu quart de résolution + 1 passe. Mesurer les 30 premières images : au-delà de 1,5 s / image, réduire les flocons à 200.

**Déterminisme** : tout dépend de `t = frame / 30` ; graines fixes ; aucune horloge, aucune physique.

## 6. Typographie cinétique et viseur (calque HTML)

- **Polices** : `InterDisplay-Black.otf` (mot géant, chiffres, verdict), `InterDisplay-SemiBold.otf` (phrases), `InterDisplay-Medium.otf` (mentions, viseur), `InterDisplay-BlackItalic.otf` uniquement pour « Mais… ». Chiffres tabulaires.
- **Hiérarchie** : 2 niveaux de texte par plan maximum ; ≤ 8 mots par phrase ; mot ou chiffre clé ≥ 130 px ; **≤ 0,25 s par mot** (≈ 95 mots max au total, leçon ép. 2).
- **Position** : bloc principal y 480-980 (au-dessus de la tête), jamais sur la tête ni sur le visage ; mention permanente en bas y 1190-1230.
- **Entrée « chauffe »** (10 images) : `color` et `filter` animés le long de la table fer (indigo `#1C0B4A` → magenta `#A0228F` → orange `#FF9A1F` → couleur finale), `blur` 10 px → 0, `translateY` 8 px → 0 (la chaleur monte). Le chiffre « vrai » reste dans le dégradé chaud.
- **Sortie « refroidit »** (8 images) : retour vers `#1C0B4A`, opacité → 0, petit grain (masque bruit CSS).
- **Le mythe « 40 à 45 % »** : entre en blanc-chaud militaire (palette armée : Inter Display Black, interlettrage 0,04 em, blanc pur), puis **refroidit sur place** jusqu'à disparaître quand la palette repasse en fer.
- **Viseur** : réticule (deux crochets 60 px), étiquette « POINT CHAUD » (Medium 26, interlettrage 0,12 em), barre de palette (20 × 720 px, la table fer en dégradé vertical), libellé « IRONBOW » / « WHITE HOT » (Medium 24). **Aucun nombre** : ni °C, ni pourcentage de batterie, ni heure.
- **Barre-graphique (innovation 3)** : à 9,0 s la barre de palette quitte le bord (x 1000 → 930) et s'élargit (20 → 56 px) ; ses couleurs s'effacent au profit de **segments de surface** (tête en haut, puis tronc, bras, jambes, avec fins séparateurs 2 px). Seul le segment **tête** est étiqueté : « ≈ 7 % » (Black 64, dégradé chaud) relié par un trait fin à la tête de la silhouette. À 19,0 s le segment grandit à **19 %** (bébé).

## 7. Découpage (emplacements ; chiffres = fiche uniquement)

| Scène | Temps | Image | Texte (emplacement) | Son |
|---|---|---|---|---|
| **1. Accroche** ★ | 0,0-3,0 | Image 0 (§3). Souffle à 0,4 s. **0,90 : déclic d'étalonnage** (figé 2 images, palette ré-étalée, tête plus blanche, réticule verrouillé). 2,0 : L3. | Pastille + L1 + L2 (+ L3) | Vent d'hiver filtré, pas sur la neige au loin ; **0,90 clic mécanique net** + léger sifflement électronique |
| 2. Le mythe | 3,0-6,0 | **Changement de palette → « WHITE HOT »** (fondu 6 images, bip court). `uMythY` descend : la zone chaude envahit le dos jusqu'à ≈ 45 % de la silhouette. Libellé viseur « WHITE HOT ». | « 40 à 45 % par la tête » (mythe, blanc) · petit « Source : un vieux manuel de survie de l'armée américaine » (≤ 10 mots) | Bip de palette ; nappe grave qui gonfle |
| **3. Le balayage** ★ waouh | 6,0-9,0 | 5,95-6,20 : silence. **6,20** : retour palette fer en 1 image + la ligne de scan (trait blanc 3 px + halo) descend du crâne aux genoux en 1,2 s ; au-dessus d'elle le manteau disparaît : **tout le corps s'allume**, la tête se fond dans un corps aussi chaud. La caméra recule de 30 cm. Le « 40 à 45 % » refroidit et s'efface. | « Sous le manteau, tout le corps chauffe » (≤ 7 mots, scénariste) | **Swoosh ascendant** synchronisé au scan + sub 50 Hz à l'arrivée ; le vent revient |
| 4. La part réelle | 9,0-12,5 | Palier de zoom ×1 → ×1,4 sur la tête puis retour. La barre de palette devient **barre de surface** (innovation 3), segment tête allumé. | « Ta tête ≈ 7 % de la surface de ton corps » (« ≈ 7 % » géant) | Tic sec à chaque segment (4 tics), clic de palier |
| 5. L'étude + verdict | 12,5-15,5 | À côté du segment « surface », un second segment « chaleur perdue » se remplit à **≈ 10 %**. Libellé discret « Pretorius 2006 · eau à 17 °C ». 14,2 : verdict entre en « chauffe ». | « Dans l'étude : ≈ 10 % de la chaleur perdue » · verdict (ex. « PLUTÔT MYTHE », Black ≥ 140, au choix du scénariste) · mention permanente en bas | 2 notes montantes ; « tampon » sourd au verdict |
| **6. Mais…** ★ | 15,5-18,6 | Le scan **remonte** : le manteau revient (le corps s'éteint en violet), il ne reste que **la tête blanche** : l'image 0 retrouvée, mais on sait désormais pourquoi. **17,10-17,40 silence** ; **17,40 le bonnet tombe** (rebond) et **éteint la tache** (blanc → violet en 12 images). Souffle visible juste après. | « **Mais…** » (BlackItalic 150, dégradé chaud) · « Corps couvert, tête nue : là, elle compte. » (nuance obligatoire, telle quelle) | Laine qui frotte + petit choc mat ; **filtre grave descendant** (la chaleur « s'éteint ») |
| 7. Bébé + partage | 18,6-21,6 | La silhouette se transforme en **bébé emmailloté** (tête nue énorme, blanche). Le segment tête de la barre passe de 7 % à **19 %**. 20,4 : mini-bonnet. | « Chez un bébé : 19 % » · ligne de partage (emplacement, ≤ 10 mots, ex. « Envoie ça à [la personne qui te dit de mettre ton bonnet] ») | Tic de barre étiré ; laine douce |
| 8. Fin + boucle | 21,6-24,0 | Signature grande (gabarit `#sigB` + `#shine`) ; « @lifestyles_hf » ; **« Ép. 4 : [sujet] → abonne-toi »** SemiBold 52 ; sources Medium 24. 23,0 : retour à l'adulte, le bonnet **se soulève** et la tête se rallume ; **dernière image = image 0 exacte** (sans L3). | Fin | Vent ; à 23,9 le clic d'étalonnage **commence** (rejoue à 0,9 s dans la boucle) |

Légende (pas à l'écran) : précaution de la fiche (« Par grand froid, couvre tout, tête comprise. Bébé ou signes d'hypothermie : demande conseil à un professionnel de santé. Ceci n'est pas un avis médical. »). **Mention écran obligatoire** (bas, scène 1 à 8, Medium 22, 60 %) : « Simulation · couleurs indicatives » (honnêteté : ce n'est pas une vraie prise thermique).
Interdits (fiche) : « 0 % par la tête », « le bonnet ne sert à rien », « 50 % à −4 °C », « manuel de 1970 », « années 1950 », « 10 % » sans « ≈ » ou présenté comme mesuré dans l'air. Le +42 % est autorisé mais **déconseillé à l'écran** (troisième chiffre de l'étude, alourdit ; le garder pour la légende).

## 8. Son

| Couche | Description | Niveau |
|---|---|---|
| Fil rouge | **Le clic d'étalonnage** de la caméra (0,9 s, 9,0 s palier, 23,9 s boucle) | crêtes −1 dBTP, précédé de 150 ms de vide |
| Ambiance | Vent d'hiver filtré passe-bas, pas lointains dans la neige, aucune voiture | −26 LUFS court terme |
| Nappe | Accord grave froid ; s'ouvre vers le chaud au verdict, se referme au bonnet | −22 |
| Événements | Bip de palette (3,0 et 6,2), swoosh de scan (6,2), 4 tics de barre, tampon (14,2), laine + choc + filtre descendant (17,4) | synchronisés à l'image près |
| Mixage | Intégré −14 LUFS ; **piste non muette vérifiée** par `tools/qa/check_reel.py` | — |

Sources : banque **CC0** (clic d'obturateur, vent, laine) ou **prise de son d'Anthony** (1 minute : frotter un bonnet en laine près du micro, poser un bonnet sur une table, clic d'un stylo à poussoir pour l'étalonnage). Zéro dépense.

## 9. Faisabilité

| Élément | Moteur maison | Plan réel d'Anthony | OpenArt |
|---|---|---|---|
| Silhouette, manteau, bonnet, rue, flocons, souffle | **Oui** (primitives + Lathe + Capsule, un seul matériau « température ») | — | — |
| Look thermique crédible | **Oui** (cible basse résolution + flou + table de couleurs + bruit) : c'est ce flou qui rend les primitives crédibles | — | — |
| Scan, mythe 45 %, bébé | **Oui** (uniformes `uScanY`, `uMythY`, échelles de groupe) | — | — |
| Viseur, barre-graphique, typo thermique | **Oui** (HTML/CSS) | — | — |
| Sons | — | **Recommandé** (bonnet, 1 min) | — |
| Plan photoréaliste | **Non souhaité** : une fausse image thermique « réaliste » d'IA tromperait ; notre version stylisée, étiquetée « simulation », est plus honnête. | — | — |

Temps estimé : scène 2 h 30 ; aperçus 10 min ; capture 720 × ~1,2 s ≈ 15 min ; audio 30 min.
Planche de contrôle : `capture.py --apercu 0,0.9,1.0,2.5,4.5,6.2,6.8,7.6,10.5,13.5,15.8,17.2,17.8,19.5,22.5,23.97`. Contrôleur : accroche lisible à l'image 0 **et** en vignette 395 px ; tête blanche visible sous le texte sans chevauchement ; corps entier allumé à 7,6 s ; tache éteinte à 17,8 s ; aucun nombre dans le viseur ; dernière image = image 0.

**Point de vigilance** : si la silhouette en primitives paraît « bonhomme Michelin » malgré le flou, augmenter le flou (rayon 2,2 px capteur) et réduire le contraste du manteau ; le thermique réel est flou par nature.

## 10. Références par choix

| Choix | Références |
|---|---|
| Caméra thermique comme langage, neige en points sombres, corps qui s'allume sans manteau | [VICE — BBC Earth Unplugged, 2 min torse nu dans la neige](https://vice.com/en/article/two-long-shirtless-minutes-in-the-snow-through-the-lens-of-an-infrared-camera) · [TVOvermind 11/2025](https://tvovermind.com/?p=1305327) · [WILX — « Maman avait raison », manteau en thermique](https://www.wilx.com/2021/12/24/thermal-camera-shows-why-you-need-coat-michigan-winter) |
| Monde révélé par la chaleur, palette comme humeur (armée en niveaux de gris) | [Dezeen — Hiro Murai, « Grief »](https://www.dezeen.com/2015/04/04/grief-earl-sweatshirt-music-video-hiro-murai-thermal-camera/) · [FLIR — clip « Creepin' » en thermique](https://www.flir.com/discover/professional-tools/creepn-with-flir-the-weeknd-diddy-21-savage-and-metro-boomin-in-thermal-for-their-latest-music-video/) · [Remotion thermalVision](https://remotion.dev/docs/effects/thermal-vision) (principe luminance → table, et alerte « préréglage ») |
| Balayage révélateur | [Codrops — scan sur carte de profondeur](https://tympanus.net/codrops/?p=90674) · [Codrops — révélation par shader](https://tympanus.net/codrops/2024/12/02/how-to-code-a-shader-based-reveal-effect-with-react-three-fiber-glsl/) |
| Donnée tirée de l'interface réelle, son = crédibilité | [Tendances motion 10/2026](https://blog.mean.ceo/?p=10938) · [Centric — typo héroïne, authenticité 2026](https://www.centricdxb.com/insights/social-media-design-trends) |
| Argument de débat (le mythe circule encore) | [Xinhua 02/2026 : « un tiers à 15 °C, la moitié à 4 °C »](https://www.news.cn/20260202/b4e0910f95c04c7d83b03fb5861380e8/c.html) · [BBC Science Focus 03/2025](https://www.sciencefocus.com/science/the-great-cold-head-myth-where-you-really-lose-your-body-heat-from) |

## 11. Prédiction (à comparer avec l'analyste à J+1 et J+3)
- **Vues > 3 s ≥ 55 %** (hypothèse : image thermique d'un humain dans un lieu = POV crédible comme le piéton + accroche géante centrée). Sous 40 % : le thermique est lu comme « filtre » → test suivant = même accroche sur plan réel d'Anthony.
- **Partages ≥ 8 / 1 000** : la cible « la personne qui te dit de mettre ton bonnet » + argument de débat (« elle avait un peu raison ») + utilité (bébé).
- **Rétention au-delà de 6,2 s** : la courbe ne doit pas chuter avant le scan ; si chute à 3-5 s, la scène « mythe » est trop longue (passer à 2 s).
- Boucle : le bonnet qui se soulève à 23 s doit pousser au revisionnage (durée moyenne > 100 %).
