# Brief créatif — « Mythe ou science ? » ép. 2 : craquer ses doigts, ça donne de l'arthrose ?

Agent 16 (directeur de création « monde ») · 18/10/2026 (pour publication 19/10) · mode RAPIDE · Statut : **BRIEF PRÉPARÉ** (rien n'est rendu, rien n'est testé).
Entrées : `work-doigts/fiche-validee.md` (**seuls chiffres autorisés**) · `docs/veille-visuelle.md` (session du 18/10 soir) · `data/lecons.md` · briefs vitamine C et piéton (univers à **ne pas** refaire) · planches `exemples/*/planche-1ips.jpg` · couverture « 17 h éveillé ».
`work-doigts/script.md` n'existe pas encore : les textes ci-dessous sont des **emplacements** (gabarit, taille, nombre de mots). Le scénariste les remplit ; le directeur ne fixe aucun chiffre hors fiche.
Format : 1080×1920, 30 i/s, **24,0 s = 720 images** (plage autorisée 23-25 s). Moteur : `tools/motion-engine/capture.py` (`window.sceneReady`, `window.renderAt(t)`), SwiftShader. Partir du squelette `exemples/2026-10-18-pieton-2-secondes/index.html` (importmap, rendu interne 720×1280, utilitaires déterministes, signature PNG + reflet `#shine`) et **jeter toute la scène**.

---

## 0. Remise en question (sans complaisance)

**Ce que disent les chiffres** (`lecons.md`) : 60 % de vues > 3 s pour « 17 h éveillé » (texte néon 2D géant, centré) contre 23,5 % pour la vitamine C 3D. La 3D n'a pas « raté » : elle a **pris la place de l'accroche**.

**Ce qui fait « déjà vu » ou basique chez nous**
1. **Vitamine C** : l'objet 3D occupe le centre à l'image 0 et l'accroche est à 60 px de corps ; à 3 s l'image est **creuse** (nuage orange, zéro texte). Sarcelle unique pendant 20 s. Notre plus beau Reel est celui qui accroche le moins.
2. **Piéton** : l'accroche est en haut, petite (≈ 45 px de hauteur de lettre sur la planche), mangée par la scène ; trop de petites mentions grises (3 niveaux de texte par plan). Le « 2 s » néon est trop petit pour la vignette 395 px.
3. **Les deux 3D** : le texte reste un bloc « posé » au-dessus de la scène ; il ne fait jamais partie de l'action.
4. **Les compteurs rouleau + anneaux + avion en papier** reviennent d'un Reel à l'autre : c'est devenu notre propre gabarit.
5. **Aucune raison de s'abonner visible** dans la vidéo (leçon du 18/10 soir) : l'ép. 1 annonçait l'ép. 2 sur une carte floue à 24 s, que personne n'a vue.
6. **Le « 17 h éveillé »** gagne, mais son décor (étoiles, croix « + », sol quadrillé, halo large) est déjà daté : on garde **sa hiérarchie** (texte géant centré, dégradé cyan → violet), pas son décor.

**Ce que les meilleurs font et que nous ne faisons pas encore** : la première image porte le sens **seule** et se décide en ≈ 1 s ([BlitzCut, 09/2026](https://blitzcutai.com/blog/what-makes-a-reel-hook-viral)) · la typo **est** le visuel principal ([Tangence 2026](https://www.tangence.com/blog/?p=1093)) · l'imagerie médicale réelle comme esthétique (radio animée, IRM en temps réel) · le mythbuster qui **garde une nuance surprenante** (Dr Karl : « pas d'arthrose, mais la poigne », > 350 000 vues, [greenMe](https://www.greenme.it/?p=859083)) · la fin qui relance la boucle par le son.

**Univers interdits** : eau, bulles, verre réfractant, sarcelle dominant (ép. 1) · nuit, pluie, phares, faisceau qui balaie, HUD au sol (piéton) · étoiles, croix, sol quadrillé (gabarit 2D) · « bulle qui explose » (interdit par la fiche) · compteur rouleau, anneau-minuteur, avion en papier (nos tics).

---

## 1. Idée maîtresse

> **« L'accroche est une articulation : au "crac", le mot ARTHROSE se fend en deux comme un doigt qu'on tire, une cavité sombre s'ouvre entre ses lettres, et la caméra entre dans cette fente pour arriver au cœur d'un doigt radiographié. »**

Le monde du Reel = **un négatoscope** (la boîte lumineuse des radiologues) : fond violet profond lumineux, un seul doigt en **os translucide « radio »**, lumière qui vient de derrière. Aucune autre matière.

## 2. Innovations retenues (jamais faites chez nous)

| # | Innovation | Ce qui change vs ép. 1 et piéton | Principe source |
|---|---|---|---|
| 1 | **Typo-articulation** : le mot géant de l'accroche est coupé à l'horizontale par la ligne d'articulation du doigt placé derrière. Au crac (0,9 s), la moitié haute des lettres se soulève (comme la phalange tirée), un **éclair blanc** de 2 images puis une **fente sombre** à liseré violet s'ouvre *dans* le mot, et elle **reste** (la cavité persiste, Kawchuk). Toute la suite du Reel réutilise ce geste : chaque mot clé entre en « pliant » sur sa ligne de base comme une phalange qui fléchit. | Ép. 1 : typo effervescente. Piéton : balayage de faisceau. Ici : **le texte vit la science** dès 0,9 s, sans quitter la taille géante qui fait 60 % à 3 s. | Typo comme visuel principal ([Tangence](https://www.tangence.com/blog/?p=1093), [Codrops — lettres animées par shader](https://tympanus.net/codrops/2025/03/24/animating-letters-with-shaders-interactive-text-effect-with-three-js-glsl/)) + IRM réelle : éclair puis cavité qui persiste ([The Limbic](https://thelimbic.com/?p=3732)) |
| 2 | **Jauges-os** : les 18,1 % et 21,5 % ne sont ni des barres ni des points : ce sont **deux doigts radio côte à côte** (« craquent » / « ne craquent pas ») dont l'os se **densifie de lumière** depuis la base, comme une radio qui « blanchit ». Le doigt des craqueurs s'arrête **plus bas** : le contre-intuitif se voit avant de se lire. | Ép. 1 : grilles de bulles + tubes. Piéton : lignes au sol. Ici : **le corps est le graphique** (miroir croyance / preuve). | Croyance face à la preuve en écran partagé ([AFP / Jordan News](https://www.jordannews.jo/Section-122/Health/TikTok-is-flooded-with-health-myths-these-creators-are-pushing-back-20853)) + radios animées en boucle ([Creative Bloq — Cameron Drake](https://creativebloq.com/animation/animated-x-rays-reveal-how-your-bones-move-81412674)) |
| 3 | **Boucle « période réfractaire »** : à la fin, le doigt se remet en tension, on entend le grincement qui monte… et **rien** (on ne peut recraquer qu'après ~20 min). La dernière image = l'image 0 exacte : le crac « manqué » se résout au début de la boucle suivante (0,9 s). | Ép. 1 et piéton : boucle visuelle seulement. Ici : **boucle sonore + scientifique**, qui pousse au revisionnage. | Fin qui relance (playbook §4.7) + Roston & Haines cité par Kawchuk (fiche) |
| 4 | **Épisode suivant à l'écran, lisible** : pastille de série en haut tout le long (« MYTHE OU SCIENCE ? · ÉP. 2 ») + à 22 s une ligne en grand « Ép. 3 : [sujet] → abonne-toi ». | Corrige la leçon « aucune raison de s'abonner visible ». | `lecons.md` 18/10 soir |

Obligatoires : **1 et 2**. 3 et 4 ne coûtent rien au rendu.

## 3. Image 0 et moments forts

**Image 0 (arrête le pouce, lisible en vignette 395 px et dans la grille 3:4)** — tout le sens tient dans le rectangle **x 65-1015, y 280-1250** (zone sûre Reels, [Hopper](https://www.hopperhq.com/blog/instagram-reel-size/)) et dans la zone grille 1080×1440 (y 240-1680).
- Fond négatoscope : dégradé radial `#2A1E6E` (centre, y ≈ 900) → `#120C38` → `#07061A` (bords). Grain de film radio 3 %.
- Derrière le texte, **un doigt radio vertical** (os translucides, voir §5), centré, articulation métacarpo-phalangienne exactement à **y 905** ; luminance de l'os **limitée à 30 %** pendant 0-3 s (le texte domine).
- En haut (y 70) : signature officielle 240 px, opacité 0,85 ; dessous (y 190) **pastille « MYTHE OU SCIENCE ? · ÉP. 2 »** : Inter Display SemiBold 30, interlettrage 0,14 em, texte `#F4F4FF`, fond `rgba(150,130,255,.16)`, bord 2 px `#9682FF`, coins 999 px, hauteur 64.
- **Ligne 1** (emplacement L1, ≤ 4 mots, ex. « Tu craques tes doigts ? ») : Inter Display SemiBold **84 px**, blanc `#F4F4FF`, centrée, ligne de base y 760.
- **Ligne 2** (emplacement L2, **un seul mot**, ex. « ARTHROSE ? ») : Inter Display Black, **taille ajustée pour remplir 900 px de large** (≈ 165-185 px de corps), capitales, centrée sur **y 905** (= la ligne d'articulation qui la coupera). Remplissage dégradé vertical `#6FF5E6` (haut) → `#A08CFF` (bas), cœur net, lueur serrée `0 0 14px rgba(140,150,255,.55)` + `0 4px 30px rgba(7,6,26,.8)` (pas le halo large de 2021).
- **Ligne 3** (emplacement L3, ≤ 6 mots, boucle ouverte, apparaît à 2,0 s, pas à l'image 0) : Inter Display Medium 40, `#C9C4FF`, y 1080, ex. « Réponse… et une vraie nuance ».
- Voile sombre sans bord derrière L1-L2 (dégradé radial `rgba(7,6,26,.55)` → 0) pour un écart de luminance texte / fond ≥ 120.
→ **Couverture = image 0** (avec L3), sans aucune autre modification.

**Moment waouh : 0,90 s (image 27)** — le crac. Voir scène 1. Placé avant la décision de 1 s.
**Second pic : 12,2 s** — les deux jauges-os se figent, celle des craqueurs **plus basse**, puis le verdict « MYTHE » entre en typo-articulation.
**Troisième pic (révélation aux deux tiers) : 15,6 s** — « Mais… » : seule apparition de la couleur chaude (ambre doré) dans tout le Reel.

## 4. Palette (deux dominantes par plan)

| Rôle | Hex | Usage |
|---|---|---|
| Négatoscope | `#2A1E6E` → `#120C38` → `#07061A` | Fond permanent. Jamais de noir pur. Remplace étoiles / sol quadrillé. |
| Os radio | cœur `#CFE2FF` à 25-60 %, liseré `#8FE9FF` | Phalanges, métacarpien |
| Cartilage | `#5EF2E0` (fin liseré émissif) | Surfaces articulaires |
| Cavité | cœur `#05040F`, liseré `#B49CFF` | La fente dans le mot et dans l'articulation |
| Éclair | `#FFFFFF` (2 images) | Juste avant la cavité |
| Accroche / marque | dégradé `#6FF5E6` → `#A08CFF` | L2, verdict, mots clés |
| Craqueurs | `#5EF2E0` | Jauge 18,1 % |
| Non-craqueurs | `#9682FF` | Jauge 21,5 % |
| **Nuance (poigne, gonflement)** | ambre doré `#F2C46B` | **Uniquement** scène 5 : seule touche chaude ; rime avec l'or de la signature |
| Texte | `#F4F4FF` · secondaire `#B7B3D9` | Calque HTML |
| Signature | PNG officiel (or + trèfle `#5DBB4A`) | Haut (petite) et fin (grande). **Jamais redessinée, jamais recolorée.** Aucun autre vert. |

## 5. Scène 3D (légère : objectif ≤ 1,2 s / image)

**Unités** : 1 unité = 1 cm. Doigt (index) vertical, base en y = 0, articulation MCP en y = 0 (repère centré sur elle).

| Objet | Géométrie | Matière (aucune transmission) |
|---|---|---|
| Métacarpien (bas) | `LatheGeometry` 48 segments : diaphyse r 0,45, tête sphérique r 0,62 en haut, longueur 6,5 | `ShaderMaterial` **« radio »** : `alpha = base 0,18 + fresnel^2,2 × 0,8` (bords plus denses, comme une vraie radio), couleur `#CFE2FF`, `uDensity` (0 → 1) qui ajoute un remplissage lumineux du bas vers le haut (sert aux jauges-os), additif, `depthWrite:false` |
| Phalange proximale | Lathe : base concave r 0,6, diaphyse r 0,38, longueur 4,4 | Idem |
| Phalanges moyenne et distale | Lathe, 2,6 et 1,9 | Idem (articulations IPP / IPD pour le pli de la scène 6) |
| Cartilage | 2 calottes sphériques fines (épaisseur 0,05) sur chaque surface de la MCP | `MeshBasicMaterial` `#5EF2E0`, opacité 0,6, additif |
| Liquide synovial | Lentille (sphère aplatie r 0,62 × 0,12) entre les calottes | Additif `#8FE9FF` à 10 % |
| **Cavité** | Ellipsoïde (sphère détail 32, échelle 0,55 × 0,28 × 0,55) au centre de l'interligne ; `uOpen` 0 → 1 en 3 images, puis **reste** à 0,85 | Shader : cœur opaque `#05040F` (soustrait la lumière de fond), liseré fresnel `#B49CFF` intensité 2 (bloom) ; **pas d'éclatement, pas de bulles** |
| Peau | Enveloppe : capsules lissées autour des os (r +0,35), une seule géométrie | Fresnel seul, `#9682FF` à 12 %, additif : silhouette de doigt sans visage ni ongle détaillé |
| Gonflement (scène 5) | même enveloppe, échelle radiale 1 → 1,07 autour des articulations | teinte → `#F2C46B` à 18 % |
| Poussière de lumière | `Points` 600, très lents, hors mise au point | `#B7B3D9` à 15 % |

**Lumières** : **aucune lumière réelle n'est nécessaire** (tout est non éclairé / fresnel). Si le motion designer veut une ombre : **une seule** `DirectionalLight` avec ombre 1024 px, sinon 0. **Zéro** RectAreaLight, PMREM, transmission.

**Post-traitement (une seule chaîne courte)**
1. `UnrealBloomPass` à **demi-résolution** (360×640) { strength 0,6, radius 0,45, threshold 0,7 }, animé aux pics.
2. **Une** `ShaderPass` finale qui fait tout : vignette 0,35 + grain 3 % seedé + **saut d'image au crac** (décalage 6 px vers le haut + séparation RVB 3 px pendant 3 images) + flash.
3. Pas de Bokeh, pas d'aberration permanente.

**Budget** : rendu interne 720×1280 puis mise à l'échelle (comme le piéton), ≤ 40 000 triangles, ≤ 8 objets transparents, 0-1 ombre. **Contrôle** : mesurer les 30 premières images en aperçu ; au-delà de 1,5 s / image, supprimer la poussière puis passer le bloom au quart de résolution.

**Caméra** : `PerspectiveCamera` FOV 30°. Courbes Catmull-Rom position + cible, `eio` entre clés, **jamais immobile** (dérive ≥ 0,02 cm/s). Trajet unique (le fil continu) :

| t (s) | Position → cible | Lecture |
|---|---|---|
| 0,0 | (0, 0, 32) → (0, 0, 0) | Face, doigt entier derrière le texte |
| 0,9 | +6 px de saut (passe finale) | Crac |
| 3,0 → 4,2 | (0, 0, 32) → (0,4, 0,1, 3,2) | **Plongée dans la fente** du mot / de l'articulation (le texte HTML s'écarte vers le haut et le bas, la fente 3D prend le relais) |
| 4,2 → 9,0 | orbite 0° → 35° autour de la MCP, rayon 3,2 → 4,5 | Macro 3/4 : la cavité en volume |
| 9,0 → 10,4 | recul (0, 1, 30), le doigt se **dédouble** en miroir (x −4 / +4) | Écran partagé, sans coupe |
| 10,4 → 15,4 | dérive verticale lente | Jauges-os |
| 15,4 → 19,4 | glissé vers le doigt gauche (−4, 1,5, 14) | Nuance |
| 19,4 → 22,0 | légère contre-plongée (0, −3, 22) | Le doigt se plie et « tape » l'icône d'envoi |
| 22,0 → 24,0 | retour à (0, 0, 32) → image 0 exacte à 23,97 s | Boucle |

**Déterminisme** : tout dépend de `t = frame / 30` ; graines fixes ; aucune horloge, aucune physique.

## 6. Typographie cinétique (calque HTML)

- **Polices** (`tools/motion-engine/fonts/`) : `InterDisplay-Black.otf` (mot géant, verdict, chiffres), `InterDisplay-SemiBold.otf` (phrases), `InterDisplay-Medium.otf` (mentions, pastille). Chiffres tabulaires. **Nouveau** : `InterDisplay-BlackItalic.otf` réservé au mot « Mais… » (scène 5), seul italique du Reel.
- **Hiérarchie** : 2 niveaux de texte par plan maximum (fin des 3 niveaux du piéton). Une phrase ≤ 8 mots, mot clé ≥ 120 px.
- **Position** : bloc principal centré verticalement **y 600-1150** (pas en haut) ; nuance permanente en bas à y 1190-1230 (au-dessus de la zone interface à 1250).
- **Entrée « phalange »** (8 images) : chaque ligne pivote depuis sa ligne de base (`rotateX` 70° → 0°, `transform-origin: 50% 100%`, perspective 900 px) avec un léger dépassement (−4°) puis retour : le mot **fléchit et se pose** comme un doigt. Flou de mouvement vertical 8 px → 0.
- **Sortie** (6 images) : la ligne se **fend** sur sa ligne médiane (deux masques haut / bas qui s'écartent de 30 px et s'effacent) : rappel discret du crac, sans son.
- **Fente de l'accroche (innovation 1)** : L2 est rendue **deux fois** (`clip-path` haut / bas sur y 905). Au crac : moitié haute `translateY(-34px)` en 3 images puis retour à −22 px (la cavité persiste) ; entre les deux, une bande `#05040F` à liseré `#B49CFF` 2 px ; éclair blanc pleine largeur de la fente aux images 26-27.
- **Chiffres des jauges** : **pas de rouleau** (déjà vu). Le chiffre « se développe » comme un film radio : flou 14 px → 0 et luminance 0 → 1 en 10 images, synchronisé au remplissage de l'os.

## 7. Découpage (emplacements de texte ; chiffres = fiche validée uniquement)

| Scène | Temps | Image | Texte (emplacement) | Son |
|---|---|---|---|---|
| **1. Accroche + crac** ★ | 0,0-3,0 | Image 0 (§3). 0,0-0,85 : le doigt se met en tension (la phalange s'éloigne de 0,08, grincement). **0,90** : éclair 2 images, cavité 3D + fente dans le mot, saut d'image, bloom 0,6 → 1,4 → 0,6. Le mot reste fendu. 2,0 : L3 entre. | L1 + L2 (+ L3 à 2,0) + pastille | 0,3-0,85 grincement tendu qui monte (filtre qui s'ouvre) ; **0,90 vrai crac de doigt** + sub 55 Hz 250 ms ; 80 ms de silence total ; 1,0 nappe grave violette |
| 2. Ce qu'est le crac | 3,0-6,5 | Plongée dans la fente → macro MCP. Le crac est **rejoué au ralenti** (×4) en 3D : éclair, puis cavité qui s'ouvre et **reste**. Libellé « ralenti ». | « Le crac = une cavité qui se forme » (≤ 7 mots, « cavité » Black 120 dégradé) ; petit « IRM en temps réel · Kawchuk 2015 · débat encore ouvert » | crac rejoué au ralenti (étiré, grave) ; « souffle » d'ouverture |
| 3. Pas une bulle | 6,5-9,0 | Orbite 3/4 : la cavité en volume, immobile ; le liquide synovial frémit à peine. Option : un fil lumineux part de la cavité et « compte » ~20 min (aiguille, pas d'anneau). | « Pas une bulle qui éclate » est **à reformuler** (la fiche interdit l'expression « une bulle qui explose » : le scénariste tranche ; proposition sûre : « Elle ne s'use pas : ~20 min pour recraquer ») | tic sourd unique |
| 4. Les radios ★ | 9,0-15,4 | Recul, dédoublement en 2 doigts. Libellés au-dessus : « Craquent » / « Ne craquent pas ». 10,8-12,2 : les os se **densifient** de bas en haut ; gauche s'arrête à 18,1 %, droite à 21,5 % (hauteur de remplissage proportionnelle). **12,2** : verdict « MYTHE » entre en « phalange » (Black, remplit 700 px). Nuance permanente en bas dès 10,4. | « 215 adultes, radios des mains » (9,2) · « 18,1 % » / « 21,5 % » (Black 110, couleurs §4) · « Écart non significatif » (Medium 36) · « MYTHE » · nuance obligatoire : **« Études petites, mais aucune ne montre plus d'arthrose. »** | montée douce pendant le remplissage (2 notes, une par doigt, la gauche s'arrête plus tôt) ; **12,2 crac + accord qui se résout** |
| 5. Mais… ★ | 15,4-19,4 | Glissé vers le doigt des craqueurs : l'enveloppe **gonfle** légèrement et vire à l'ambre ; un arc ambre au bout du doigt (la poigne) se referme **incomplètement**. Aucun chiffre (le 75 % est exclu). | « **Mais…** » (BlackItalic 150, ambre) · « Craqueurs habituels : mains plus gonflées, poigne plus faible » (≤ 9 mots) · petit « 1 étude d'observation, 300 patients, 1990 » | 0,3 s de silence avant « Mais… », puis basse chaude ; craquement sec plus mat |
| 6. Partage | 19,4-22,0 | Le doigt radio **se plie** (IPP 0 → 70°) et **tape** une icône « envoyer » (extrudée, liseré cyan) qui pulse 2 fois. | « Envoie ça à [la personne qui craque ses doigts en réunion] » (≤ 10 mots, la cible en blanc plein) | « tap » + 2 pulsations douces |
| 7. Fin + boucle | 22,0-24,0 | Grande signature PNG (largeur 720, y ≈ 560) révélée par le reflet doré `#shine` existant ; « @lifestyles_hf » Medium 40 ; **« Ép. 3 : [sujet] → abonne-toi »** SemiBold 52 ; sources Medium 24. 23,0 : le doigt se remet en tension, grincement… **pas de crac** (période réfractaire). Le texte de l'accroche se reforme intact ; **dernière image = image 0** (sans L3). | Sources : « deWeber 2011 · Castellanos 1990 · Kawchuk 2015 » | grincement qui monte et **s'arrête net** sur la dernière image → raccord avec le crac de 0,9 s |

Légende (pas à l'écran) : « Douleur, gonflement, raideur ou crac après un choc → médecin. » Interdits : « sans danger », « zéro risque », « bon pour tes articulations », « une bulle qui explose ».

## 8. Son

| Couche | Description | Niveau |
|---|---|---|
| Fil rouge | **Le crac** (prise réelle) : 0,9 s (net), 4,0 s (ralenti), 12,2 s (verdict), 16,5 s (mat) ; absent à 23,9 (boucle) | crêtes −1 dBTP, chaque crac précédé de 80-300 ms de silence |
| Tension | Grincement / étirement (cuir ou corde qui se tend, filtré) avant chaque crac | −24 |
| Nappe | Accord grave froid (violet) ; bascule en accord chaud à « Mais… » | −22 LUFS court terme |
| Ponctuations | sub 55 Hz au crac, souffle de plongée, 2 notes de jauge, tap, pulsations | — |
| Mixage | Intégré −14 LUFS ; **piste non muette vérifiée** par `tools/qa/check_reel.py` | — |

Sources : **prise de son d'Anthony** (craquer ses doigts près du micro du téléphone, pièce calme, 10 cracs : 1 minute suffit) sinon banque **CC0**. Zéro dépense.

## 9. Faisabilité

| Élément | Moteur maison | Plan réel d'Anthony | OpenArt |
|---|---|---|---|
| Doigt radio, cavité, jauges-os, gonflement, icône | **Oui** (Lathe + shaders fresnel, sans lumière) | — | — |
| Typo-articulation, entrée « phalange » | **Oui** (CSS `clip-path`, `rotateX`) | — | — |
| Son du crac | — | **Recommandé** (1 min) | — |
| Image 0 photoréaliste | **Non souhaitée** : l'image 0 doit rester typographique (leçon 60 % / 23 %) | — | — |

Temps estimé : scène 2 h, aperçus 10 min, capture 720 × ~1,2 s ≈ **15 min**, audio 30 min.
Planche de contrôle : `capture.py --apercu 0,0.9,1.0,2.5,4.0,7.5,11.0,12.4,15.8,17.5,20.5,22.8,23.97`. Contrôleur : accroche lisible à l'image 0 **et** sur la vignette 395 px, fente visible à 1,0 s, 0 chevauchement, dernière image = image 0.

## 10. Références par choix

| Choix | Références |
|---|---|
| Image 0 typographique, décision à 1 s / 3 s | [BlitzCut — hook 2026](https://blitzcutai.com/blog/what-makes-a-reel-hook-viral) · [Hopper — zones sûres et grille 3:4](https://www.hopperhq.com/blog/instagram-reel-size/) · `data/lecons.md` (60 % contre 23 %) |
| Typo-articulation | [Tangence — typographie au centre, 2026](https://www.tangence.com/blog/?p=1093) · [Codrops — lettres animées par shader](https://tympanus.net/codrops/2025/03/24/animating-letters-with-shaders-interactive-text-effect-with-three-js-glsl/) · contre-exemple saturé : [modèles « stomp »](https://videobolt.net/author/Goldenmotion/trendy-stomp) |
| Cavité, éclair, IRM | [The Limbic — éclair blanc et cavité](https://thelimbic.com/?p=3732) · [ScienceAlert — Kawchuk](https://www.sciencealert.com/researchers-have-finally-worked-out-what-happens-when-you-crack-your-knuckles) · [AuntMinnie — IRM des doigts](https://cdn.auntminnie.com/clinical-news/mri/article/15612128/researchers-use-mri-to-watch-finger-joints-crack) |
| Esthétique radio / négatoscope | [Creative Bloq — radios animées (Cameron Drake)](https://creativebloq.com/animation/animated-x-rays-reveal-how-your-bones-move-81412674) · veille 17/10 §D (3D médicale, rétroéclairage) · [Tangence — 2D + 3D légère](https://www.tangence.com/blog/?p=1093) |
| Mythe + nuance (poigne) | [greenMe — Dr Karl, > 350 000 vues](https://www.greenme.it/?p=859083) · [AFP / Jordan News — créateurs anti-mythes](https://www.jordannews.jo/Section-122/Health/TikTok-is-flooded-with-health-myths-these-creators-are-pushing-back-20853) · [The Week — fact check 10/2025](https://www.theweek.in/news/health/2025/10/13/fact-check-does-cracking-your-knuckles-every-day-cause-arthritis.amp.html) |

## 11. Prédiction (à comparer avec l'analyste à J+1 et J+3)
- **Vues > 3 s ≥ 50 %** (hypothèse : accroche géante néon centrée + événement physique à 0,9 s). Sous 40 % : le crac visuel n'aide pas → test suivant = même accroche sans 3D.
- Partages : ciblage nommé (scène 6) + argument de débat (« même un peu moins chez les craqueurs, écart non significatif ») ; objectif 10 / 1 000.
- Abonnements : la ligne « Ép. 3 → abonne-toi » à 22 s est la première promesse visible ; mesurer abonnés / 1 000 vues contre l'ép. 1.
- Revisionnages : la boucle « crac manqué » doit allonger la durée moyenne de visionnage au-delà de 100 % (à lire dans Instagram).
