# Brief créatif — « Le chiffre qui pique » : en noir à 18 h, le conducteur a 2 secondes

Agent 16 (directeur de création « monde ») · 18/10/2026, 7 h · mode RAPIDE · Statut : **BRIEF PRÉPARÉ** (rien n'est rendu, rien n'est testé).
Entrées : `work-pieton/script-valide.md` (**textes, temps et chiffres inchangés** : aucun chiffre ajouté à l'écran) · `docs/veille-visuelle.md` (sessions 17 et 18/10) · `data/lecons.md` · brief d'hier `2026-10-17-mythe-vitamine-c.md` (univers à **ne pas** refaire).
Format : 1080×1920, 30 i/s, **24,5 s = 735 images**. Moteur : `tools/motion-engine/capture.py` (scène `index.html` exposant `window.sceneReady` et `window.renderAt(t)`), Chromium headless en **SwiftShader (rendu processeur)** : ~2,4 s par image → **≈ 30 min de capture**. Partir du squelette `exemples/2026-10-17-mythe-vitamine-c/index.html` (importmap, composer, police) et jeter tout le reste.

---

## 0. Remise en question (sans complaisance)

Regardé : planche `exemples/2026-10-17-mythe-vitamine-c/planche-1ips.jpg`, couvertures vitamine C et 7 000 pas.

**Ce qui fait déjà « déjà vu » dans le Reel 3D d'hier**
1. **Un seul bleu-vert pendant 20 s.** De 3 s à 25 s, chaque image est le même aplat sarcelle avec des rayons : au pouce, toutes les images se ressemblent. Aucun contraste chaud / froid.
2. **Des objets qui flottent dans le vide.** Pas de sol, pas d'horizon, pas d'échelle : la 3D ne raconte pas un *lieu*. Le comprimé ressemble à un disque plat (texture faible, gravure brouillée).
3. **Caméra frontale et centrée** presque partout ; le « plan-séquence » se lit comme une suite de plans fixes.
4. **Image creuse à 3 s** (nuage orange illisible, aucun texte) : exactement au moment où notre audience décroche.
5. **Le texte reste un bloc centré en haut**, posé sur une plaque, scène après scène : on retrouve le gabarit, seulement en 3D.
6. **Aucun humain.** Les comptes qui explosent montrent une personne ou une situation vécue ; nous montrons des pictogrammes.
7. Le 7 000 pas d'aujourd'hui retombe dans l'ancien gabarit (étoiles, croix « + », sol quadrillé, halos) : la décision d'hier n'a pas été appliquée partout.

**Ce que les meilleurs font et que nous ne faisons pas encore** : un *lieu* crédible où le spectateur se projette (POV) · la lumière comme outil de révélation (on ne voit que ce que le faisceau touche) · les distances montrées **à l'échelle réelle**, dans l'espace · un contraste chaud / froid fort · un jeu de regard (« trouve le piéton ») qui pousse à revoir.

**Univers interdit (déjà fait hier)** : pas d'eau en volume, pas de bulles, pas de verre transparent réfractant, pas de sarcelle dominant. La pluie est traitée en **traits** (stries) et en **reflets au sol**, jamais en sphères.

---

## 1. Idée maîtresse

> **« Tu es au volant, de nuit, sous la pluie : ton pare-brise devient un affichage tête haute qui mesure, en vrais mètres sur la route, les 2 secondes qu'il te reste quand un piéton en noir sort de l'ombre. »**

Le spectateur est **le conducteur**. Toutes les données (2 s, 30 m, 50 m, 150 m, 26 m, 4 m) sont **projetées sur la route mouillée**, à leur vraie distance, comme un affichage tête haute en réalité augmentée de voiture récente. On *ressent* la distance au lieu de la lire.

## 2. Innovations retenues (jamais faites chez nous)

| # | Innovation | Ce qui change par rapport au Reel d'hier | Principe source |
|---|---|---|---|
| 1 | **Le pare-brise = affichage tête haute (HUD) en réalité augmentée.** Les chiffres sont des tubes néon et des marquages lumineux **posés dans le monde** (avec leur reflet dans la chaussée mouillée), à l'échelle 1 m = 1 m. | Hier : chiffres en HTML ou grilles flottant dans le vide. Aujourd'hui : chaque chiffre a une position, une distance et un reflet. | Data visualisation « dans l'espace » (veille 17/10 §B, hybride 2D / 3D) + HUD AR automobile ; [Borzendowski et al. via APS](https://psychologicalscience.org/?p=116122) : le piéton surestime sa visibilité, donc il faut montrer *ce que voit le conducteur* |
| 2 | **La lumière révèle, l'ombre cache.** Le piéton, la bande et certains mots n'existent que dans le cône des phares (masque lumineux). La bande rétroréfléchissante utilise un **vrai shader de rétroréflexion** (brillance maximale quand l'œil est aligné avec les phares). | Hier : tout éclairé uniformément. Aujourd'hui : 70 % de l'image dans le noir, l'œil va là où la lumière frappe. | [Volvo LifePaint](https://road.cc/content/news/147107-paint-yourself-visible-night-volvo-develops-new-life-paint-cyclists) (invisible jusqu'à ce que les phares le touchent, primé Cannes Lions) ; [Kennon et al. 2025 / QUT](https://research.qut.edu.au/mqcollab/wp-content/uploads/sites/471/2026/01/Visual-motion-perception-and-driving-hazard-visibility-at-night.pdf) : la nuit, le mouvement est l'indice le plus fort |
| 3 | **Temps figé, caméra libre (« bullet time »)** à 2,5 s : le monde s'arrête, la pluie reste suspendue en stries, la caméra sort par le pare-brise et monte en grue pour montrer la scène de haut. | Hier : la caméra suivait les objets. Aujourd'hui : on arrête le temps pour mesurer, puis on le relance (le crissement à 9 s). | Plans uniques et illusions qui retiennent (veille 17/10 §A-4) ; tendance « freeze-frame + move » |
| 4 | **« Trouve le piéton » dès l'image 0** : la silhouette sombre est *déjà là*, à peine perceptible entre deux lampadaires. Ceux qui la voient au 2e visionnage partagent. | Hier : image 0 = objet évident. Aujourd'hui : un jeu de regard qui provoque le revisionnage. | Mécanique de cherche-et-trouve / illusion (veille 17/10 §A-4, §A-5 FOOH) |
| 5 | **Typographie de marquage au sol** : les distances sont peintes sur l'asphalte en perspective anamorphique (comme « STOP » ou « BUS »), lisibles depuis le POV, et se relèvent à la verticale quand la caméra est en vue de dessus. | Hier : typo effervescente collée à l'écran. | [Visible Bag, GROSS / Uzum (Ouzbékistan, Or 2024-2025)](https://gross.uz/en/press_center/news/177) : le langage des signes routiers comme code visuel |

Le « HUD » (1) et la « lumière qui révèle » (2) sont les deux innovations obligatoires. 3, 4 et 5 se font dans le même moteur sans coût de rendu notable.

## 3. Image 0 et moments forts

**Image 0 (ce qui arrête le pouce)** : vue du conducteur, de nuit, sous la pluie. Bord du capot noir en bas (y 1700-1920), montants du pare-brise en ombre floue sur les bords. Rue mouillée qui file vers un point de fuite (y ≈ 980), **longues stries de reflets** chauds sous chaque lampadaire. Dans l'axe, à 30 m, le **« 2 s » géant en tube néon** (verre néon, cyan `#5EF2E0`, hauteur écran ≈ 420 px) flotte au-dessus de la chaussée **et se reflète dedans**. Juste sous le « 2 s », entre deux lampadaires, **la silhouette en noir est là, presque invisible** (contraste de luminance 6 à 8 % avec le fond : on la devine si on cherche). Gouttes sur le pare-brise. En haut : « En noir à 18 h ? » / « Le conducteur a 2 secondes. » + « à 50 km/h ».
→ Couverture = cette image, sans les gouttes au centre (lisibilité de la vignette 395 px).

**Moment waouh principal : 2,5 s** — le faisceau atteint la silhouette, elle **surgit** ; au même instant **tout se fige** (pluie suspendue, reflets immobiles), le « 2 s » tombe au sol et **se couche en ligne néon « 30 m »** au pied du piéton. Coup sourd.
**Second pic : 8,8 → 9,6 s** — vue de dessus : la ligne d'arrêt cyan glisse en freinant jusqu'à 26 m, s'immobilise **à 4 m du piéton**, la marge clignote rouge, flash rouge plein cadre (8 images) au crissement.
**Troisième pic : 18,4 s** — la bande du cartable, grise et terne, **s'allume d'un coup** dans les phares (bloom + traînée de reflet horizontale).
**Boucle** : la dernière image reprend le cadrage exact de l'image 0, mais le piéton porte maintenant la bande allumée : avant / après sans un mot.

## 4. Palette (deux couleurs dominantes par plan, maximum)

| Rôle | Hex | Usage |
|---|---|---|
| Nuit | `#04060F` (bas) → `#0A1230` (ciel) → `#1A1F4A` (halo urbain à l'horizon) | Fond. Jamais de noir pur. |
| Asphalte mouillé | base `#07090F`, rugosité 0,25, reflets = couleurs des sources | Chaussée |
| Phares (chaud) | `#FFE2B0` cœur, `#FFC877` bord du cône | Faisceaux volumétriques, sol éclairé |
| Lampadaires (sodium) | `#FF9E45` | 6 lampadaires, stries de reflets |
| HUD / mesure (néon marque) | `#5EF2E0` (cyan) | « 2 s », lignes 26 / 30 / 50 / 150 m, ligne d'arrêt |
| Secondaire marque | `#9682FF` (violet) | Ciel du crépuscule (scène 6), liserés, avion en papier (traînée) |
| Alerte | `#FF3B3B` (halo) · `#FFE6E0` (cœur) | Marge de 4 m, flash, feux arrière, « +34,9 % » |
| Bande rétroréfléchissante | éteinte `#5A5F6B` ; allumée `#F4FBFF` + bloom | Cartable, laisse, sac |
| Texte | `#F4F4FF` · secondaire `#AAACCD` | Calque HTML |
| Signature | PNG officiel (or + trèfle `#5DBB4A`) | Fin uniquement, jamais redessinée |

Règle : chaud (phares / sodium) contre froid (nuit / cyan) dans chaque plan ; le rouge n'apparaît **que** sur les moments de danger (scènes 4-5) ; aucune touche verte avant la signature.

## 5. Scène 3D de base

**Unités** : 1 unité = **1 mètre**. Repère « voiture figée » : à t = 2,5 s, l'avant de la voiture est en z = 0 ; la route part vers −z. Circulation à droite : voie de la voiture centrée x = +1,75 ; trottoir droit x 3,5 à 6 ; trottoir gauche x −3,5 à −6.

| Objet | Géométrie (simple et crédible) | Matière |
|---|---|---|
| **Chaussée** | Plan 9 × 400 m (z +40 à −360), 1 seul plan | `MeshStandardMaterial` { color `#07090F`, roughness 0,25 (0,55 dans les scènes 2-5, voir §9), metalness 0 } + normalMap de grain d'asphalte procédural (canvas 1024, bruit seedé, répété 1 × 40) |
| **Reflets mouillés (truc principal, pas cher)** | Pour chaque source lumineuse : un plan vertical-couché étiré (largeur 0,4-0,8 m, longueur 6-14 m) collé au sol sous la source, orienté vers la caméra | `ShaderMaterial` additif : dégradé de la couleur de la source, bruit qui casse la strie (flaques), opacité 0,35-0,6. **Pas de Reflector planaire** (doublerait le rendu) |
| **Marquages** | Ligne médiane pointillée blanche (`#C9CCD6`, emissive 0,15), bord de chaussée, passage piéton optionnel désactivé | Standard, roughness 0,4 |
| **Trottoirs + bordures** | `BoxGeometry` 2,5 × 0,15 × 400 de chaque côté | `#151823`, roughness 0,8 |
| **Lampadaires** | À droite (x +5,2) tous les 50 m : z −5, −55, −105, −155 (le piéton à z −30 est donc **au milieu de deux halos**, dans le noir) ; à gauche (x −5,2) décalés : z −32, −82, −132 (celui de z −32 porte l'horloge de la scène 5). Mât = cylindre r 0,08 × 7 m, crosse = tube, tête = `RoundedBoxGeometry` 0,6 × 0,12 × 0,25 | Mât `#1C1F2A` metalness 0,6 ; tête émissive `#FF9E45` intensité 4 ; **pas de vraie PointLight** : halo au sol = disque additif r 4 m |
| **Façades** | 2 rangées de `BoxGeometry` (hauteurs 6-14 m, profondeur 8) à x ±9, quelques fenêtres émissives tièdes (instances, 5 % allumées) | `#0B0E1A` roughness 0,9 ; perspective et parallaxe gratuites |
| **Phares (volumétriques)** | 2 `SpotLight` réels (angle 22°, pénombre 0,5, distance 70, intensité 40, **sans ombres**) + 2 cônes `ConeGeometry` ouverts (longueur 45 m) | Cône : `ShaderMaterial` additif, opacité qui décroît avec la distance et sur les bords (Fresnel inversé), bruit défilant (pluie dans le faisceau), `#FFE2B0` à 9 % |
| **Voiture** (vue seulement scènes 3-4) | Corps `RoundedBoxGeometry` 1,8 × 1,4 × 4,4 (rayon 0,25) + habitacle plus étroit, 4 cylindres roues ; **très sombre**, on ne lit que le liseré | `#0C0E16` metalness 0,7 roughness 0,3 ; feux arrière émissifs `#FF3B3B` + 2 stries de reflet rouges au sol |
| **Silhouette piéton** (premium, non cartoon) | Mannequin articulé de **capsules** (`CapsuleGeometry`) : tête r 0,11, cou, buste 0,5, bassin, bras 2 segments, jambes 2 segments, hauteur totale **1,72 m** ; proportions réalistes, pas de visage, pas de doigts. Marche procédurale (sin, cycle 1,1 s, rotation hanche ±22°, genou 0-35°, balancier bras ±18°, rebond 3 cm). Variantes : capuche (sphère tronquée), cartable (`RoundedBox` 0,3 × 0,4 × 0,15), sac de course, laisse (tube fin) + chien (5 capsules) | **Noir** : `#101218` roughness 0,95 (tissu mat). **Clair** : `#C9CDD8` roughness 0,9. Liseré de contre-jour par Fresnel `#FFC877` à 25 % uniquement dans le faisceau |
| **Bande rétroréfléchissante** | Bande 0,05 m de large sur bretelle / rabat de cartable / laisse (géométrie collée) | `ShaderMaterial` **rétroréflexion** : `I = pow(max(dot(normalize(camPos − P), normalize(headlightPos − P)), 0), 40) × éclairement du phare` ; base `#5A5F6B`, crête `#F4FBFF` × 6 (le bloom fait le reste). Phares et caméra étant presque alignés, elle brille ; vue de côté hors faisceau, elle redevient grise : c'est **physiquement juste** |
| **Pluie** | 1 `InstancedMesh` de 2 500 quads fins (0,01 × 0,5 m) dans une boîte qui suit la caméra | Additif, blanc bleuté `#BFD3FF` à 25 %, plus lumineux dans les cônes des phares (test « dans le cône ») ; position = fonction de t (seed), **figée** pendant le temps arrêté |
| **Pare-brise** (scènes 1, 2, 8) | Passe plein écran (`ShaderPass`) : 30 à 40 gouttes aplaties (pas des sphères) + traînées, carte de normales générée une fois (canvas, seed), déformation de l'image ≤ 12 px ; masque effacé par l'essuie-glace | — |
| **Essuie-glace** | Lame = `RoundedBox` 1,1 × 0,03 × 0,02 noire, attachée à la caméra, pivot bas gauche, balayage 0 → 95° → 0 en 0,5 s | `#050608` |
| **HUD néon** | « 2 s » et chiffres de distance : `TextGeometry` extrudé (police Inter Display Black convertie en typeface JSON, profondeur 0,08 m) ; **tube néon** = matière émissive `#5EF2E0` intensité 3 + liseré blanc au cœur | `MeshBasicMaterial` émissif + bloom ; leur **reflet dans la chaussée** = copie inversée en y, opacité 0,3, floutée (sprite) |
| **Lignes de distance** | Plans 0,12 × 7 m en travers de la chaussée à z −26, −30, −50, −150 ; étiquette « 30 m » etc. **peinte au sol** (plan texture canvas, anamorphose en vue POV) | Additif cyan (rouge pour la marge) |

**Lumières (au total)** : 2 `SpotLight` phares (sans ombre) · 1 `HemisphereLight` ciel `#1A1F4A` / sol `#04060F` intensité 0,25 · aucune autre lumière réelle (lampadaires, halos, reflets = faux additifs). **Zéro ombre portée calculée** (SwiftShader) ; une ombre de contact = disque flou sombre sous le piéton.

**Post-traitement (`EffectComposer`)**
1. `UnrealBloomPass` **demi-résolution** { strength 0,7, radius 0,5, threshold 0,78 } ; animé aux pics.
2. Passe pare-brise (gouttes) quand la caméra est derrière la vitre.
3. Traînée de reflet horizontale (« anamorphic streak ») : 1 passe flou horizontal sur la couche > 0,95 de luminance (phares, bande allumée). Discrète : 0,25.
4. Vignette 0,4 · grain 3 % seedé par numéro d'image · aberration chromatique 0,0012 sur les bords.
5. **Pas de BokehPass** (trop cher en SwiftShader) sauf scène 7 (gros plan bande) où l'arrière-plan est déjà flou par sprites.

**Caméra** : `PerspectiveCamera`. POV conducteur : position (1,35, 1,20, +1,6) relative à l'avant de la voiture (le conducteur est à gauche dans la voiture), FOV vertical **48°** (grand angle de pare-brise, pas macro). Courbes Catmull-Rom position + cible, interpolation `cubic-bezier(0.65, 0, 0.35, 1)`, la caméra ne s'arrête jamais (dérive 0,03 m/s minimum). Léger tremblé de route (bruit 2 mm, 3 Hz) **seulement** quand la voiture roule.

**Déterminisme** : tout dépend de `t` ; pluie, gouttes, grain et fenêtres allumées = seeds fixes ; aucune physique temps réel.

**Budget par image** (pour tenir ~2,4 s) : ≤ 150 000 triangles, 2 lumières réelles, 0 ombre, bloom demi-résolution, 1 passe de déformation max. Si l'aperçu dépasse 3 s / image : réduire la pluie à 1 500 instances puis supprimer les façades lointaines (z < −200).

---

## 6. Calque texte (HTML / CSS) et typographie cinétique

- **Polices** (déjà dans `fonts/`) : Inter Display Black (mots clés, chiffres), Inter Display SemiBold (phrases), Inter Medium (mentions). Chiffres tabulaires.
- **Zone sûre** : texte entre x 90 et 990, **y 200 et 760** (le ciel, au-dessus du point de fuite) ; la route en bas reste libre pour l'action. Nuance permanente du bas à **y 1420-1470**.
- **Lisibilité** : pas de halo, pas de dégradé sur les phrases. Ombre portée `0 4px 24px rgba(4,6,15,.85)`. Sous les blocs, voile sombre **sans bord** (dégradé radial `rgba(4,6,15,.55)` → 0) au lieu de la plaque de verre d'hier (on change de gabarit).
- **Entrée « balayage de faisceau »** (≈ 9 images) : chaque phrase est révélée par un masque lumineux qui balaie de gauche à droite comme un faisceau de phare (dégradé `#FFE2B0` → blanc sur le bord du masque, puis le texte se stabilise en blanc) ; flou de mouvement horizontal 10 px → 0.
- **Sortie « essuie-glace »** (≈ 6 images) : masque en arc de cercle (pivot bas gauche de l'écran) qui efface la phrase, synchronisé avec un balayage d'essuie-glace quand il y en a un (1,3 s ; 14,0 s ; 21,0 s), sinon simple balayage du masque.
- **Chiffres clés dans le monde** (innovation 5) : « 2 s », « 30 m », « 50 m », « 150 m », « 26 m », « 4 m », « +34,9 % » existent **aussi** en 3D (néon ou marquage au sol). Le HTML reste la version lisible ; la 3D est l'écho spatial. Ne jamais afficher un chiffre absent du script.
- **Compteur** : « +34,9 % » en rouleau (chiffres qui défilent avec flou 6 px), 0 → 34,9 en 1,0 s, décélération finale.
- **En-tête** : signature officielle `brand/signature-officielle.png`, largeur 260 px, y 48, opacité 0,85 ; **pas de pastille, pas de filet** (scènes 1-7). Grande signature en scène 8.
- **Nuance permanente** (Inter Medium 30, `#AAACCD`) de 2,5 à 11,0 s : « Selon la Prévention Routière · phares allumés, route sèche ».

---

## 7. Découpage scène par scène (textes exacts du script validé)

Notation caméra : position (x, y, z) → cible (x, y, z), en mètres, repère « voiture figée ».

### Scène 1 — 0,0 à 2,5 s · « En noir à 18 h ? » / « Le conducteur a 2 secondes. » + petit « à 50 km/h »
- **Monde** : la voiture roule à 13,9 m/s : la caméra POV avance de z = +36,35 + 1,6 à z = +1,6 (35 m en 2,5 s). Pluie qui tombe. Tremblé de route.
- **Caméra** : POV (1,35, 1,20, 37,95 → 1,6) → cible (1,6, 0,9, −60). Image 0 = t 0.
- **HUD « 2 s »** : en tube néon, **attaché à la voiture à 30 m devant elle** (il avance avec elle), hauteur réelle 2,2 m, base à 0,8 m au-dessus de la chaussée, reflet dans le sol. Il « respire » (intensité 2,6 ↔ 3,2, 1 cycle/s, en phase avec le tic).
- **Piéton noir** : placé à z = −30 (il sera exactement à 30 m à t 2,5), x = +3,2 (bord de chaussée, il s'apprête à traverser), en marche lente vers −x. Entre les lampadaires z −5 et −55 : dans la zone la plus sombre. Hors du cône des phares jusqu'à 2,3 s (le cône porte à ~30 m), donc presque invisible (contraste 6-8 %).
- **1,3 s** : **essuie-glace** (0,5 s) : les gouttes disparaissent dans son sillage ; la première phrase s'efface en arc, « Le conducteur a 2 secondes. » (Black 100) entre derrière la lame ; « à 50 km/h » (Medium 34, `#AAACCD`) + petit compteur de vitesse HUD « 50 » en bas à gauche du pare-brise (néon cyan, 60 px).
- **« En noir à 18 h ? »** : SemiBold 64 blanc, « en noir » souligné d'un trait gris foncé. **« 2 secondes »** dans la phrase en cyan `#5EF2E0`, le reste blanc.
- **Son** : pluie sur le toit et le pare-brise (constante), moteur bas, **tic de clignotant** à 1 Hz (le « tic » du script), « fwoump-squeak » de l'essuie-glace à 1,3 s.

### Scène 2 — 2,5 à 5,0 s · « En sombre : vu à 30 m. » · petit « Le remède prend 1 minute → fin » ★ MOMENT WAOUH
- **2,3 → 2,5 s** : le bord du faisceau touche les jambes puis le buste : la silhouette **surgit** (le liseré chaud s'allume sur l'épaule et la capuche). Elle tourne légèrement la tête vers la voiture (12°).
- **2,5 s : temps figé.** Voiture, pluie (stries suspendues), piéton (en appui, une jambe en avant) s'arrêtent. Le tremblé cesse. Le « 2 s » néon **bascule vers l'avant et se couche au sol** (rotation X 90° en 8 images) : il devient la **ligne néon « 30 m »** au pied du piéton (morph : les tubes du « 2 » et du « s » s'étirent latéralement en une ligne de 7 m), étiquette « 30 m » peinte au sol à côté (anamorphose lisible depuis le POV).
- **2,5 → 5,0 s** : caméra en poussée lente vers le piéton (z 1,6 → −3), mise au point visuelle par la lumière : le reste de la rue s'assombrit de 20 %.
- **Conditions de mesure (voir §9)** : de 2,7 à 3,2 s, un **balayage HUD** (plan cyan fin qui parcourt la scène de la voiture vers l'horizon) « nettoie » les stries de pluie suspendues sur son passage et fait passer la chaussée de mouillée à **satinée** (roughness 0,25 → 0,55, reflets ÷ 2). Lecture : on mesure en conditions standard.
- **Texte** : « En sombre : vu à 30 m. » (SemiBold 64 ; « 30 m » Black 96 cyan) ; petit « Le remède prend 1 minute → fin » (Medium 30, `#AAACCD`) en bas de bloc (boucle ouverte). Nuance permanente apparaît en bas.
- **Son** : whoosh inversé (aspiration) qui culmine à 2,5 s, **coup sourd** (sub 45 Hz, 400 ms) à 2,5 s, la pluie se coupe net (passe-bas en 3 images) : silence de temps figé avec une nappe grave tenue.

### Scène 3 — 5,0 à 7,5 s · « Clair : 50 m · Réfléchissant : plus de 150 m » · source « Prévention Routière · ONISR 2025 »
- **Caméra (le fil continu)** : **traverse le pare-brise** (5,0-5,3 s : les gouttes grossissent puis passent, 9 images de déformation), puis **grue arrière et montée** : (1,35, 1,2, −3) → (7, 10, 22), cible (1,5, 0, −70). On découvre la voiture figée de dos (feux arrière rouges), ses deux cônes de phares volumétriques sur la route, et la rue jusqu'à 150 m.
- **Silhouettes** : noire à 30 m (déjà là, ligne cyan). **5,8 s** : silhouette **claire** à z −50, x +3,0, ligne « 50 m » qui s'allume, ding. **6,6 s** : à z −150, une silhouette noire avec **bande réfléchissante** : seule la bande se voit (point blanc + traînée horizontale), ligne « 150 m », ding plus aigu. Les 3 silhouettes sont figées en pleine marche (biomouvement lisible même immobile).
- **Lignes** : 3 lignes cyan au sol avec étiquettes au sol ; vues de haut, les étiquettes **se relèvent à la verticale** (rotation X 90° en 10 images) pour rester lisibles depuis la grue.
- **Texte** : « Clair : 50 m » puis « · Réfléchissant : plus de 150 m » (SemiBold 58 ; chiffres Black 84 cyan) ; source « Prévention Routière · ONISR 2025 » Medium 24 `#AAACCD` sous le bloc.
- **Son** : riser (montée filtrée) 5,0 → 7,5 ; **ding** à 5,8 et 6,6 (verre fin, 2 hauteurs ; pas de son de bulle).

### Scène 4 — 7,5 à 11,0 s · « Pour s'arrêter à 50 km/h : au moins 26 m. » puis « En noir, il reste 4 m. » ★ SECOND PIC
- **Caméra** : poursuite de la grue jusqu'à la **vue de dessus** (route verticale à l'écran, format portrait idéal) : (1,75, 38, −8) → cible (1,75, 0, −17), roulis 0. Cadre ≈ 37 m de route : voiture en bas (z 0 → +4,4), piéton noir en haut (z −30). Les autres silhouettes sortent du cadre.
- **7,8 → 9,0 s** : une **ligne d'arrêt néon cyan** (largeur de voie, 3,5 m) part du pare-chocs et glisse vers le piéton en **décélérant** comme un freinage (courbe ease-out cubique), laissant derrière elle **deux traces de freinage** sombres et brillantes au sol (les pneus). Étiquette « 26 m » qui la suit. Elle s'immobilise à z −26.
- **9,0 → 11,0 s** : la bande entre −26 et −30 se remplit de **rouge** `#FF3B3B`, étiquette « 4 m » au sol ; clignote 3 fois (période 0,4 s). **9,6 s** : flash rouge plein cadre (opacité 0 → 0,35 → 0 en 8 images) + bloom 0,7 → 1,5 → 0,7.
- **Texte** : « Pour s'arrêter à 50 km/h : au moins 26 m. » (SemiBold 58, « au moins 26 m » Black 84 cyan) puis à 9,0 s « En noir, il reste 4 m. » (Black 104, « 4 m » rouge `#FF3B3B`).
- **Son** : la pluie et le moteur reviennent (le temps repart pour la simulation), **crissement de pneus** 7,8 → 9,0 qui s'arrête net à l'immobilisation, impact sourd + tic de clignotant seul pendant le clignotement.

### Scène 5 — 11,0 à 14,0 s · « 17 h-19 h : +34,9 % d'accidents » · petit « avec blessés, impliquant un piéton, après le changement d'heure (ONISR 2020-2024) »
- **Caméra** : de la vue de dessus, **bascule vers l'avant** et pivote vers le lampadaire de gauche en face du piéton (x −5,2, z −32) jusqu'à une **horloge de rue** fixée sur le mât à 4 m de haut : (−3,2, 4,2, −27) → cible (−5,0, 4,0, −32). Le piéton noir reste visible en flou dans le bas du cadre, de l'autre côté de la rue.
- **Horloge** (pas de verre transparent) : boîtier cylindre r 0,45 noir métal, cadran **émissif blanc chaud** `#FFF1DC`, aiguilles noires, index fins. Elle indique 18 h ; **11,3 → 12,3 s** les aiguilles **reculent d'1 h** (la grande aiguille fait un tour arrière, flou de mouvement par 3 copies en traînée).
- **Compteur** : **12,3 s** « +34,9 % » **jaillit du sol** sur la chaussée devant le mât : marquage au sol rouge qui se décolle et se dresse (extrusion 0 → 0,1 m puis rotation X 90°), compteur rouleau 0 → 34,9 en 1,0 s.
- **Texte** : « 17 h-19 h : » SemiBold 58 + « +34,9 % » Black 150 `#FF3B3B` + « d'accidents » SemiBold 58 ; petit texte en Medium 26 `#AAACCD` sur 2 lignes. Note : la nuance permanente a disparu à 11,0 s.
- **Son** : **rembobinage** (bande inversée, 1 s, sur le tour d'aiguille), **impact** grave à 12,3 s, tics du compteur (mécaniques, horlogers).

### Scène 6 — 14,0 à 17,5 s · « Dimanche 25/10 : on recule d'1 h. » puis « Lundi, ton retour de 18 h se fait à la nuit tombée. »
- **14,0 s** : essuie-glace « virtuel » (le masque en arc efface le texte précédent). La caméra recule de l'horloge et redescend à hauteur d'homme sur le trottoir : (4,5, 1,6, −18) → cible (3, 1,2, −40), vue de 3/4 le long de la rue.
- **Ciel accéléré** (14,0 → 15,7 s) : un dôme ciel (`SphereGeometry` inversée, shader dégradé) passe du **crépuscule** (horizon `#F08A5D` → `#9682FF` → `#1A1F4A`) à la **nuit** (`#0A1230`). Les **lampadaires s'allument en cascade** du plus proche au plus lointain (un toutes les 0,12 s, petit vacillement sodium). La pluie reprend, chaussée de nouveau mouillée (roughness 0,55 → 0,25).
- **15,7 → 16,0 s : 0,3 s de noir** (fondu en 2 images, pas plus).
- **16,0 → 17,5 s** : retour image : la silhouette marche vers nous dans le faisceau, et change de tenue en 3 temps par un **balayage lumineux vertical** (ligne cyan qui la parcourt de haut en bas, 6 images) : **cartable** (16,0) → **laisse + chien** (16,5) → **tenue de course** (17,0). Bandes encore éteintes.
- **Texte** : « Dimanche 25/10 : on recule d'1 h. » (SemiBold 58, « 25/10 » Black 84) puis à 16,0 « Lundi, ton retour de 18 h se fait à la nuit tombée. » (SemiBold 58, « à la nuit tombée » Black 72 blanc).
- **Son** : nappe qui descend, « clac » sourd à chaque lampadaire, **silence total 0,3 s** au noir, puis **basse** (sub 50 Hz) à 16,0 et pluie qui revient.

### Scène 7 — 17,5 à 21,0 s · « 1 minute : une bande réfléchissante sur le sac, le cartable, la laisse. » ★ TROISIÈME PIC
- **17,5 s** : un bruit de scratch : la main (simple capsule gantée, sombre) colle une bande sur la bretelle du cartable. Caméra **gros plan** : (2,9, 1,25, −28,9) → cible (3,0, 1,2, −29,6), FOV 30°, arrière-plan fait de sprites flous (halos sodium = bokeh rond, chaud).
- **17,9 → 18,4 s** : des phares approchent hors champ (la lumière chaude monte sur la bretelle) ; la bande grise **s'allume** d'un coup à 18,4 s (shader rétroréflexion, crête × 6, bloom 0,7 → 1,3, traînée horizontale).
- **18,4 → 19,0 s** : 2 micro-plans dans le même mouvement de caméra (panoramique latéral) : la bande sur le **sac**, puis sur la **laisse** (le chien), qui s'allument à leur tour au passage du faisceau.
- **19,2 → 20,8 s** : **recul ultra-rapide de 150 m** dans l'axe de la route (caméra de z −29 à z +120, cible fixe sur le piéton, FOV 30 → 18° pour garder la silhouette lisible : léger effet « vertigo »), à travers la pluie (stries étirées par le mouvement). À 150 m, il ne reste que **le point blanc de la bande** qui brille encore dans le noir.
- **Texte** : « 1 minute : » Black 96 cyan, puis « une bande réfléchissante sur le sac, le cartable, la laisse. » SemiBold 54 ; « le sac », « le cartable », « la laisse » passent en blanc plein au moment où chaque bande s'allume.
- **Son** : **scratch** (velcro réel), **carillon** cristallin à 18,4 (+ 2 notes plus douces pour sac et laisse), souffle de vitesse sur le recul.

### Scène 8 — 21,0 à 24,5 s · « Envoie ça au parent dont l'ado rentre à pied. » puis (23,0) grande signature + @lifestyles_hf + « Prévention Routière · ONISR 2025 »
- **21,0 → 22,0 s** : un **avion en papier néon** (géométrie pliée de 4 triangles, arêtes émissives cyan, traînée violette `#9682FF`) traverse la rue de droite à gauche au-dessus de la chaussée, se reflète dans le sol mouillé ; la caméra le suit et se replace **dans la voiture** (on repasse le pare-brise de l'extérieur vers l'intérieur, gouttes).
- **22,0 → 24,5 s** : retour au **cadrage exact de l'image 0** (POV, même FOV, même point de fuite) à 23,0 s, voiture qui roule de nouveau. À 30 m, sous l'emplacement du « 2 s », **la silhouette est là, bande allumée**, visible de loin.
- **Texte** : « Envoie ça au parent dont l'ado rentre à pied. » (SemiBold 56, « au parent dont l'ado rentre à pied » blanc plein, le reste `#AAACCD`). **23,0 s** : grande signature (largeur 720 px, centrée, y ≈ 520) révélée par **le balayage du faisceau** (même masque que les phrases, doré) ; « @lifestyles_hf » Medium 36 ; « Prévention Routière · ONISR 2025 » Medium 24 `#AAACCD`.
- **Dernière image (24,5 s)** : identique à l'image 0 sauf la bande allumée et le texte → la boucle se lit « avant / après ».
- **Son** : whoosh de l'avion (panoramique stéréo droite → gauche), pluie et moteur reviennent, **tic** de clignotant final calé pour se raccorder au tic de 0,0 s.

---

## 8. Son (récapitulatif)

| Couche | Description | Niveau |
|---|---|---|
| Ambiance | Pluie sur le toit / pare-brise (intérieur voiture), moteur bas ; coupée pendant le temps figé (2,5-7,8 s) | −22 LUFS court terme |
| Fil rouge | **Tic de clignotant** (1 Hz) : relie le début, la marge de 4 m et la fin (boucle sonore) | −20 |
| Ponctuations | Essuie-glace, whoosh inversé, coup sourd, dings, crissement, rembobinage, impact, clacs de lampadaires, silence 0,3 s, basse, scratch, carillon, whoosh avion | crêtes −1 dBTP |
| Nappe | Accord grave tenu, s'ouvre au carillon (seul moment « lumineux » de la musique) | −24 |
| Mixage | Intégré −14 LUFS ; **vérifier que la piste n'est pas muette** (`tools/qa/check_reel.py`, leçon du 17/10) | — |

Sources : banques **CC0** gratuites, ou prises de son d'Anthony **voiture à l'arrêt, moteur coupé ou au ralenti, sur un parking** : clignotant, essuie-glace, pluie sur le toit (30 s chacun). **Jamais en conduisant.** Zéro dépense.

---

## 9. Points de vigilance (à trancher par l'orchestrateur, avant rendu)

1. **Pluie à l'image / « route sèche » à l'écran** : le script affiche « route sèche » et la note interdit le chiffre pluie. Une image de pluie à côté de chiffres « route sèche » peut être lue comme trompeuse (« sous la pluie c'est encore pire, vous minimisez »). **Solution intégrée** : la pluie est **suspendue puis balayée** par le HUD pendant la mesure (2,7-11 s, chaussée satinée), et ne revient qu'à 14 s pour l'ambiance. Si le vérificateur préfère : chaussée humide **sans pluie qui tombe** dans tout le Reel (supprimer l'instancié pluie : gain de rendu). Je recommande la solution intégrée.
2. **Les distances à l'écran sont schématiques** : l'échelle est vraie en profondeur (1 m = 1 m), mais le faisceau réel des feux de croisement n'éclaire pas « exactement » jusqu'à 30 m. C'est une illustration de la donnée Prévention Routière, pas une simulation photométrique : aucune mention à ajouter, ne pas l'annoncer comme « simulation réaliste » dans la légende.
3. **Piéton qui traverse hors passage** : rester neutre (bord de chaussée, rue sans passage visible) ; ne pas culpabiliser l'ado, le ton reste « 1 minute de remède ».
4. **Aucun chiffre hors fiche validée** : le compteur de vitesse HUD affiche « 50 » (présent au script) ; ne pas afficher 13,9 m/s, 2,2 s, ni de distance pluie.
5. **Planche de contrôle** avant capture complète : `capture.py --apercu 0,1.3,2.5,3.5,6.6,9.6,12.5,16.2,18.4,20.8,23.0,24.4` → contrôleur : 0 chevauchement texte, accroche visible à l'image 0, silhouette **perceptible mais discrète** à l'image 0 (si personne ne la voit sur la planche, monter son contraste à 10 %).

## 10. Faisabilité

| Élément | Moteur maison | Plan réel d'Anthony | OpenArt (via ChatGPT) |
|---|---|---|---|
| Rue, lampadaires, façades, chaussée, reflets, pluie, phares volumétriques | **Oui** (géométries simples + additifs, aucun asset externe) | — | — |
| Silhouette articulée et marche | **Oui** (capsules + cycle procédural) ; rester stylisé « mannequin », pas de visage | — | — |
| Bande rétroréfléchissante | **Oui** (shader rétroréflexion) | — | — |
| HUD néon, marquages au sol, horloge, avion | **Oui** (`TextGeometry` : convertir InterDisplay-Black.otf en typeface JSON une fois, avec facetype.js hors ligne ou un script opentype) | — | — |
| Gouttes de pare-brise, essuie-glace | **Oui** (passe plein écran + mesh caméra) | — | — |
| Sons | — | **Recommandé** : clignotant, essuie-glace, pluie (voiture à l'arrêt) | — |
| Image 0 photoréaliste | Pas nécessaire en principe | — | Option seulement si le rendu de l'image 0 est jugé pauvre (prompt ci-dessous) ; alors `isAiGenerated: true` |

**Temps** : écriture de la scène 2 h 30 à 3 h, aperçus 15 min, capture ≈ 30 min (735 × 2,4 s), audio 30 min. **Tenable pour 12 h si on démarre avant 8 h** ; sinon, plan B : supprimer façades + traînée anamorphique + scène 7 « sac / laisse » (garder le cartable seul).

### Prompt OpenArt (option image 0 uniquement)
> Ultra-realistic cinematic photograph from the driver's seat, vertical 9:16, 1080x1920. Night, light rain, a wet European suburban street seen through a windshield with a few flattened raindrops, dark car hood at the bottom edge, blurred A-pillars at the sides. Long warm sodium streetlight reflections streaking on the glossy asphalt toward a vanishing point at mid-height. Warm halogen headlight beams (#FFE2B0) lighting the road up to about 30 metres, visible light shafts in the rain. Between two streetlights, at the edge of the beam, a pedestrian dressed entirely in black, hood up, barely distinguishable from the darkness, walking toward the road. Deep navy night sky (#0A1230), no stars. Upper 35% of the frame is clean dark negative space for text. Shallow depth of field, 24mm lens, f/2, high-end automotive safety commercial look. No text, no logo, no people other than the pedestrian, no cartoon, no illustration, no oversaturation.

Négatif : `cartoon, illustration, text, watermark, logo, bright pedestrian, reflective vest, daylight, oversaturated, bubbles, glass of water`.

## 11. Références par choix

| Choix | Références |
|---|---|
| Révélation par les phares (invisible → visible) | [Volvo LifePaint — road.cc](https://road.cc/content/news/147107-paint-yourself-visible-night-volvo-develops-new-life-paint-cyclists) · [LifePaint — Cannes Lions / The Work](https://www.lovethework.com/work-awards/campaigns/volvo-lifepaint-43705) · [BGR — LifePaint](https://bgr.com/2016/12/20/lifepaint-volvo-safety-spray/) |
| Montrer ce que voit le conducteur (écart de perception) | [APS — « Why Batman met a tragic death » (Borzendowski)](https://psychologicalscience.org/?p=116122) · [Police NRW — Safety through visibility](https://duisburg.polizei.nrw/en/article/safety-through-visibility-0) · [Derbyshire Police — vidéo vue conducteur](https://cdn.road.cc/content/news/212365-police-video-pushes-reflective-clothing-cyclists-rider-breaking-law-not-having?page=1) |
| Le mouvement révèle l'humain la nuit (marche, bande qui bouge) | [Kennon et al. 2025 / QUT](https://research.qut.edu.au/mqcollab/wp-content/uploads/sites/471/2026/01/Visual-motion-perception-and-driving-hazard-visibility-at-night.pdf) · [SWOV — biological motion et encombrement visuel](https://swov.nl/nl/publicatie/seeing-pedestrians-night-visual-clutter-does-not-mask-biological-motion) · [Wood — VTTI](https://vtti.whos.prod.es.cloud.vt.edu/PDFs/TRBVS_presentations/Wood_)VVTIvisimpwoodfinal2009.pdf) |
| Code des signes routiers sur objet du quotidien | [Visible Bag — GROSS](https://gross.uz/en/press_center/news/177) · [Toyota — campagne réflecteurs Japon](https://global.toyota/detail/52341) · [Kagawa — campagne 反射材 2026](https://www.pref.kagawa.lg.jp/kurashi/kaigi/tsc/080930.html) |
| Plan unique, illusion, temps figé | Veille 17/10 §A-4 ([Anijam](https://www.anijam.ai/blog/instagram-reels-trends/)) · [Splice — journey transitions](https://spliceapp.com/blog/journey-timelapse-transitions-instagram-reels-beginners/) · [FOOH Report 2026](https://fooh.com/resources/fooh-report-2026) |

## 12. Prédiction (à comparer avec l'analyste à J+1 et J+3)
- Rétention à 3 s **supérieure** au Reel vitamine C (hypothèse : POV vécu + silhouette cachée + surgissement à 2,5 s). Sujet hors famille sommeil : comparer surtout au vitamine C (3D) et au 7 000 pas (gabarit).
- Partages : levier « ciblage nommé » (parent d'ado) + saisonnalité forte (changement d'heure dans 7 jours) ; objectif playbook 10 / 1 000 vues.
- Signal à mesurer : commentaires « je ne l'avais pas vu » (preuve du jeu « trouve le piéton »).
- Publié un dimanche midi, créneau différent des 2 meilleurs Reels : noter le biais.
