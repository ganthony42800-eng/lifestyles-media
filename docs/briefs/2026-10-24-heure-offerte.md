# Brief créatif — « Le chiffre qui pique · ép. 2 » : l'heure « offerte » (33 min, pas 60)

Agent 16 (directeur de création « monde ») · 23/10/2026 · mode RAPIDE · Statut : **BRIEF PRÉPARÉ** (rien n'est rendu, rien n'est testé).
Publication : samedi 24/10/2026 ~07:00 (veille du passage à l'heure d'hiver, 25/10, 3 h → 2 h).
Entrées : `work-heure/script-valide.md` (**textes, minutage et chiffres non modifiables** ; ce brief n'ajoute aucun chiffre) · `work-heure/fiche-validee.md` · `data/lecons.md` · `docs/veille-visuelle.md` (session du 23/10 en tête) · brief de référence `2026-10-18-pieton-2-secondes.md` (meilleur Reel : 70,1 % > 3 s).
Format : rendu **720×1280** à 30 i/s, upscalé en 1080×1920 ; **26,0 s = 780 images**. Moteur : `tools/motion-engine/capture.py` (`window.sceneReady`, `window.renderAt(t)`), three.js r187 (vendor), Chromium headless SwiftShader. Partir du squelette `exemples/2026-10-18-pieton-2-secondes/index.html` (importmap, composer, bloom, grain, signature PNG) et **jeter toute la scène**.
**Toutes les coordonnées écran ci-dessous sont en repère 1080×1920** (pour le rendu 720×1280 : multiplier par 2/3).

---

## 0. Remise en question (sans complaisance)

Regardé : couvertures piéton, craquer doigts, chaleur tête (scan), pétrichor, doigts fripés, dette de sommeil v2 ; planche `exemples/2026-10-18-pieton-2-secondes/planche-1ips.jpg`.

**Ce qui fait « déjà vu » chez nous**
1. **Même couverture six fois** : bloc de texte centré dans le tiers haut, Inter blanc + un mot en couleur, fond nuit bleu-violet, petite pastille. Reconnaissable, oui ; mais c'est devenu un gabarit. Le texte porte tout, l'image ne dit rien seule (sauf le piéton).
2. **La pluie partout** (piéton, pétrichor, doigts fripés) et les **étoiles + sol quadrillé** (dette de sommeil) : nos « nuits » se ressemblent. Ici : **zéro pluie, zéro étoile, zéro grille**.
3. **Le piéton a déjà montré « on recule d'1 h »** : horloge analogique + rembobinage sonore à 11,3 s. Refaire une horloge à aiguilles serait une redite exacte. Ici : **horloge numérique de téléphone** et c'est **la lumière de la chambre** qui rembobine (innovation 1).
4. **Les humains en capsules font mannequin** dès qu'on s'approche (planche piéton, scènes 6-7). Ici : aucun corps, seulement un **poignet sous une manche de pyjama**, en partie hors champ et dans le flou.
5. **La 3D abstraite échoue** (vitamine C 23,6 % > 3 s : objet translucide sur fond nuit). La jauge en verre imposée par le script est exactement ce risque. Parade : la jauge **est le verre d'eau de la table de nuit**, posée sur du bois, éclairée par le téléphone, dans une chambre qu'on reconnaît en 0,5 s. Jamais seule dans le vide.
6. **Nos chiffres restent du HTML collé à l'écran** sauf dans le piéton. Ici, chaque chiffre clé a un **double physique** : 60 = trait gravé, 33 = niveau de liquide, 3 = ce qui reste au fond.

**Ce que les meilleurs font et que nous ne faisons pas encore** : le POV « depuis le lit », format qui a fait 23 à 49 M de vues par variante ([Know Your Meme](https://knowyourmeme.com/memes/alright-bro-goodnight-i-forgot-to-get-my-water)) ; de **vraies interfaces** plutôt que des widgets inventés ; la lumière de fenêtre projetée (« gobo ») comme narration ; le **son qui raconte la physique** (le verre qui se remplit monte en hauteur) ; une transition **du point de vue du corps** (clignement des paupières).

---

## 1. Idée maîtresse

> **« Tu es couché, la tête sur l'oreiller, à 02:59. Ton téléphone passe à 03:00, puis rembobine jusqu'à 02:00, et toute la chambre recule avec lui. Sur la table de nuit, le verre d'eau devient la jauge de ton heure "offerte" : on te promet 60 minutes, il n'en reste que 33 au fond du verre. »**

Un seul décor, une seule nuit, une caméra qui ne coupe jamais (sauf le clignement de 0,3 s imposé, qui *est* un plan POV). Le spectateur reconnaît **sa** table de nuit : téléphone sur son support, câble de charge, verre d'eau, lampe éteinte, rai de lune sur le mur.

## 2. Innovations retenues (jamais faites chez nous)

| # | Innovation | En quoi c'est nouveau chez nous | Principe source |
|---|---|---|---|
| **1** ★ | **La lumière de la chambre est une horloge** : le rectangle de lune projeté sur le mur (« gobo » de fenêtre avec croisillon et bord de rideau) **glisse en arrière** au moment où 03:00 redevient 02:00 (le rai de lune remonte le temps), puis vire à l'**aube** en scène 8 et revient à la nuit pour la boucle. Le temps se *voit* sans aiguilles. | Piéton : horloge à aiguilles. Ici : aucune horloge analogique ; c'est l'ombre portée qui raconte l'heure, comme un cadran solaire inversé. | Gobos / « light cookies » de fenêtre ([Superhive, 2026](https://superhivemarket.com/products/50-cinematic-gobo-light-alphas-vol1)) ; projection de texture ([three.js forum](https://discourse.threejs.org/t/what-does-the-textures-map-do-for-a-spotlight-and-do-i-need-one/44357/4)) |
| **2** ★ | **Le « liquide fantôme »** : dans le même verre, le **promis** (60) et le **réel** (33) coexistent. Les 27 min manquantes sont un volume *fantôme* (contour rouge hachuré, sans matière) qui clignote, puis lundi le vrai liquide s'écoule jusqu'à ≈ 3 sous le fantôme. Nouvelle façon de montrer un écart : **deux états dans le même objet**, pas deux barres. | Jusqu'ici : un compteur, ou deux lignes au sol (piéton). Ici, l'écart a un volume et une matière (ou une absence de matière). | Jauges liquides devenues widgets génériques ([Framer](https://www.framer.com/marketplace/components/dynamic-liquid-gauge/), [Power BI](https://powerbi.microsoft.com/blog/visual-awesomeness-unlocked-liquid-fill-gauge/)) : on garde la lecture instantanée, on la rend **physique** ; « transformation split » ([BlitzCut, 03/09/2026](https://blitzcutai.com/blog/visual-hooks-instagram-reels)) |
| 3 | **Typographie « mise au point »** : chaque phrase arrive floue et légèrement trop grande, puis devient nette, **synchronisée avec le changement de mise au point de la caméra** (on se réveille, l'œil fait le point). Sorties : flou + dérive vers le haut. Fini le balayage de faisceau et l'essuie-glace du piéton. | Le texte et la caméra partagent la même « optique ». | Typo cinétique qui porte le récit en muet ([autoae, 2026](https://autoae.online/blog/motion-graphics-trends-2026)) |
| 4 | **Le clignement des paupières** (15,0-15,3 s) : deux paupières courbes (haut et bas), bord flou, se ferment et se rouvrent sur lundi 06:30. La seule « coupe » du Reel est un geste du corps du spectateur. | Piéton : fondu au noir. | POV corporel, format « depuis le lit » ([Know Your Meme](https://knowyourmeme.com/memes/alright-bro-goodnight-i-forgot-to-get-my-water)) |
| 5 | **L'interface qui sort de l'écran** (12,6 s) : la notification « Dimanche · réveil désactivé » se détache du téléphone en carte de **verre liquide** (réfraction de bord, reflet spéculaire qui suit le mouvement) et vient vers la caméra, bouton d'envoi qui pulse. | Piéton : avion en papier néon (à ne pas refaire). | Liquid Glass ([STRV](https://strv.com/blog/liquid-glass-and-the-future-of-design)) ; vraies interfaces (veille 19/10) |

1 et 2 sont les deux innovations obligatoires. 3, 4, 5 sont gratuites en coût de rendu (HTML/CSS ou plans simples).

## 3. Image 0, couverture et moments forts

### Image 0 (ce qui arrête le pouce) = couverture = dernière image
POV oreiller, nuit. Tête posée, **roulis −5°** (on est couché), regard à hauteur du plateau de la table de nuit.
- **Bas (y 1670-1920, zone interdite au texte)** : bord d'oreiller en lin très flou, blanc bleuté `#C8D0E8` à 35 % de luminosité, qui occupe le bas de l'image (profondeur, et ça masque la zone d'interface Instagram).
- **Centre (y 860-1420)** : le **téléphone debout sur son support**, écran de verrouillage en mode nuit : **« 02:59 »** en très grand (chiffres Inter Display Light, ambre chaud `#FFB547`, hauteur ≈ 120 px à l'écran), deux-points qui clignotent à 1 Hz. Il éclaire le bois et le verre d'une lueur ambre. Câble de charge qui part du bas et tombe du plateau.
- **À droite du téléphone** : le **verre d'eau gradué vide** (traits fins gravés, trait « 60 » plus épais et lumineux), un filet de lune sur son bord.
- **Fond** : mur bleu nuit, **rectangle de lune avec croisillon** projeté en biais (haut droit vers centre gauche), poussière en suspension dans le rai ; à gauche, silhouette d'une lampe de chevet éteinte (profondeur).
- **Texte (y 300-640)** : « Cette nuit, tu dors 1 h de plus ? » (voir §6).
- **Pastille (y 150-205)** : « LE CHIFFRE QUI PIQUE · ÉP. 2 ».
- **Ce qui n'y est pas** : aucun « 33 », aucune réponse.

**Pourquoi ça arrête** : objet familier (un téléphone qui affiche 02:59 = « je connais cette heure-là »), question personnelle, et la veille du changement d'heure : tout le monde a le sujet en tête ([débat « extra hour in bed », IBTimes 19/10/2026](https://www.ibtimes.co.uk/uk-clocks-change-social-media-debate-winter-darkness-1826496)).

**Couverture** : image 0 exacte. Contrôle de recadrage : tout le sens (accroche + écran 02:59) tient dans le rectangle **y 240-1680** (grille profil 3:4) **et** dans le carré central 1080 × 1080 (y 420-1500) pour les vues qui recadrent en carré ([Krumzi 2026](https://www.krumzi.com/blog/instagram-reels-cover)) : l'accroche reste lisible en vignette 395 px ; si le carré coupe la 1re ligne, descendre le bloc texte de 60 px uniquement sur la couverture. La couverture a un effet marginal selon Mosseri ([Lindsey Gamble](https://www.lindseygamble.com/blog/cover-photos-for-reels-have-minimal-impact-according-to-instagram-head-adam-mosseri)) : **c'est l'image 0 qui compte**, elle est donc soignée comme une affiche.
TikTok (leçon du 19/10) : texte de couverture propre, avec mots-clés : « Changement d'heure : 1 h de sommeil en plus ? ».

### Moments forts
| Temps | Moment | Ce qui se passe |
|---|---|---|
| **1,40 → 1,75 s** ★ **WAOUH d'accroche** | Le rembobinage | 1,40 : « 03:00 » (déclic). 1,50 : **glitch** (séparation RVB 6 px, lignes de balayage, 2 images figées), les chiffres **défilent à l'envers** en rouleau flou (03:00 → 02:00 en 7 images). Au même instant, **le rectangle de lune glisse de 22 cm vers la gauche sur le mur** et la poussière remonte au lieu de descendre (temps inversé). 1,75 : « 02:00 » net, la pièce se stabilise. « Pas vraiment. » arrive à 1,5 s. |
| **9,8 s** | Le niveau se bloque | Le liquide violet s'arrête net à 33 : micro-onde en anneau à la surface, 30 gouttelettes, ding de verre, bloom 0,6 → 1,1 → 0,6. |
| **10,2 s** ★ **WAOUH de donnée** | Le liquide fantôme | Recul rapide (6 images) : on voit tout le verre. Entre 33 et 60, le **volume fantôme rouge** s'allume et clignote ; « +33 min » géant se remplit de liquide. |
| **15,0-15,3 s** | Clignement | Paupières, silence total, puis sonnerie. |
| **25,2-26,0 s** | Boucle | Retour exact à l'image 0. |

## 4. Palette (deux dominantes par plan, maximum)

| Rôle | Hex | Usage |
|---|---|---|
| Nuit (fond) | `#05071A` (ombres) → `#0B1030` (mur) → `#161C4A` (zones éclairées par la lune) | Jamais de noir pur |
| Lune (froid) | `#8FA8FF` cœur du gobo, `#5E74D9` bords, poussière `#C9D4FF` | Mur, bord du verre, liseré de l'oreiller |
| Écran mode nuit (chaud) | `#FFB547` chiffres, halo `#FF9A3C` à 25 % | Téléphone, lueur sur le bois et le verre : **le contraste chaud / froid de chaque plan** |
| Liquide de mesure (marque) | `#7B5CFF` fond → `#B49CFF` surface, cœur émissif | Le « temps dormi » (leçon : bleu-violet bat vert/or) |
| Promis / fantôme | contour `#FF4D6A`, hachures à 18 % | Uniquement 33-60 (scènes 5-7) |
| Aube | ciel `#3D5BD9` → `#9DB4FF`, liseré `#FFC46B` sur le bord du gobo | Scènes 8-10 ; le liseré or annonce la signature |
| Bois de la table | `#2A1C14`, veinage `#3A281C` | Plateau |
| Texte | `#F4F4FF` · secondaire `#AAB0D6` · mots clés lavande `#B49CFF` · alerte `#FF4D6A` | Calque HTML |
| Signature | PNG officiel (or + trèfle) | Jamais redessinée ; **aucun vert ailleurs** dans le Reel |

## 5. Décor 3D, matières et éclairage

**Unités** : 1 unité = 1 m. Origine = œil du dormeur. Le plateau de la table de nuit est à y −0,07 (légèrement sous l'œil), centré en (0,02, −0,07, −0,74). Mur à z −1,05. Fenêtre hors champ à droite (x +1,4, z −0,2), elle n'est jamais vue, seulement sa lumière.

| Objet | Géométrie (simple, crédible) | Matière |
|---|---|---|
| **Table de nuit** | `RoundedBoxGeometry` 0,46 × 0,05 (plateau) + caisson 0,44 × 0,5 × 0,38 ; tiroir suggéré par une rainure | `MeshStandardMaterial` bois `#2A1C14`, roughness 0,5, veinage = texture canvas seedée (1024), légère `normalMap` de veinage ; arête du plateau qui accroche la lune |
| **Téléphone** | `RoundedBoxGeometry` 0,072 × 0,150 × 0,008 (rayon 0,009), incliné de 18° en arrière sur un **support** (prisme biseauté) | Châssis métal sombre `#1B1D24` metalness 0,85 roughness 0,28 ; écran = plan texture **canvas redessinée à chaque image** (heure, notification, réveils, SNOOZE), matériau `MeshBasicMaterial` (émissif pur), verre d'écran = 2e plan à 0,5 mm avec reflet spéculaire en bande |
| **Câble de charge** | `TubeGeometry` r 0,0018 sur une courbe Catmull-Rom (du bas du téléphone au bord du plateau, puis chute) | Blanc cassé `#D9DCE6` roughness 0,6 |
| **Verre-jauge** | Cylindre ouvert r 0,034 × 0,15 m, fond épais (disque 0,008) ; **pas de `transmission`** (trop cher) | Verre = `MeshStandardMaterial` transparent opacité 0,10 + **shader Fresnel additif** sur les bords (`#C9D4FF`, puissance 3) + 2 bandes spéculaires verticales (plans fins additifs) qui glissent quand la caméra bouge. **Graduations** : cylindre r 0,0345, texture canvas (traits tous les 5 « min », trait **« 60 »** plus épais émissif blanc, étiquette gravée « 60 » ; pas d'autres nombres gravés pour ne rien ajouter au script) |
| **Liquide** | Cylindre r 0,031, hauteur = niveau (échelle Y animée) + disque de surface avec **ménisque** (anneau légèrement relevé) et ondulation sinusoïdale amortie | `ShaderMaterial` : dégradé vertical `#7B5CFF` → `#B49CFF`, émissif 1,4 (le bloom fait le cœur lumineux), bulles minuscules = 12 points qui montent pendant le remplissage ; caustique violette au pied du verre (disque additif sur le bois) |
| **Liquide fantôme** | Même cylindre, de 33 à 60 | Shader : contour (Fresnel) `#FF4D6A` + hachures diagonales 18 %, opacité clignotante ; aucun volume rempli |
| **Lampe de chevet** (éteinte) | Pied cylindre + abat-jour cône tronqué, arrière-gauche (−0,22, −0,07, −0,9) | Tissu `#1A1E33` roughness 1 ; ne s'allume jamais (silhouette de profondeur) |
| **Livre fermé** (option, si budget) | Box 0,13 × 0,02 × 0,19 sous le téléphone | Couverture `#23283F`, tranche crème |
| **Mur** | Plan 3 × 2 m | Plâtre `#0B1030` roughness 0,95, bruit fin |
| **Gobo de lune** (innovation 1) | **Plan collé au mur** (et un 2e sur le plateau) avec texture canvas : fenêtre 4 carreaux + croisillon + bord de rideau ondulé, bords flous ; **pas de `SpotLight.map`** (exige une ombre calculée) | Additif `#8FA8FF`, opacité 0,55 ; position/inclinaison = fonction de t (glisse à 1,5 s, teinte aube en scène 8) |
| **Rai de lune volumétrique** | 1 boîte allongée de la fenêtre au mur, shader additif (atténuation douce, bruit lent) + **220 poussières** (`InstancedMesh` de points) | `#C9D4FF` à 6 % ; poussière qui descend lentement (remonte pendant le rembobinage) |
| **Rideau** | 3 plans déformés (sinus) au bord droit, hors mise au point | `#141A3D`, liseré lune |
| **Oreiller (premier plan)** | **Billboard** avec texture canvas pré-floutée (forme de coussin en lin, couture floue) à 0,12 m de la caméra, bas de l'image | Lin `#C8D0E8` à 35 %, liseré lune côté droit |
| **Poignet + capteur** (scène 3) | Manche de pyjama = cylindre déformé (tricot, plis par `normalMap`) qui entre par le bas droite ; poignet = court tronc de cône **à moitié caché par la manche et le flou** ; **pas de main nette, pas de doigts**. Capteur = petit boîtier noir 0,023 × 0,032 × 0,009 sur bracelet lisse : **pas d'écran** (les participants UK Biobank portaient un accéléromètre sans affichage) ; une **LED** latérale | Manche `#20264A` roughness 0,95 ; peau en ombre `#8C6B5E` (on ne la voit presque pas) ; capteur `#0E0F14` roughness 0,35 ; LED `#B49CFF` qui pulse |

**Lumières (total)** : 1 `DirectionalLight` lune `#8FA8FF` intensité 0,5 depuis la fenêtre (sans ombre) · 1 `PointLight` « écran » ambre `#FFB547` (distance 0,6, intensité liée à la luminosité de l'écran : plus forte quand la notification ou la sonnerie s'affiche) · 1 `HemisphereLight` `#161C4A` / `#05071A` intensité 0,2. **Zéro ombre calculée** ; ombres de contact = disques flous sous le téléphone et le verre.

**Post-traitement** : `UnrealBloomPass` demi-résolution { 0,6 ; 0,45 ; seuil 0,8 } · vignette 0,45 · grain 3 % seedé · **passe glitch** (séparation RVB + lignes) active seulement 1,50-1,75 s · **flou directionnel horizontal** seulement pendant le panoramique filé de 12,6 s · **pas de BokehPass** : la profondeur de champ est simulée par des billboards pré-floutés (oreiller, rideau) et par un petit flou CSS du canvas 3D pendant les changements de mise au point (scènes 3 et 4), à tester en aperçu.

**Caméra** : `PerspectiveCamera` FOV 40° (POV), courbes Catmull-Rom position + cible, interpolation `cubic-bezier(0.65, 0, 0.35, 1)`, **respiration du dormeur** : bascule verticale 3 mm à 0,23 Hz pendant tout le Reel (signe POV quasi invisible mais vivant), roulis −5° (sauf mention). Jamais d'arrêt total (dérive ≥ 0,01 m/s).

**Budget** : ≤ 60 000 triangles, 3 lumières, 0 ombre, 1 canvas d'écran redessiné par image, bloom demi-résolution. Objectif ≤ 1,6 s/image en 720×1280 → **≈ 21 min de capture**. Si > 2,5 s/image : retirer le livre, réduire la poussière à 120, supprimer la caustique.

**Déterminisme** : tout dépend de t (poussière, bulles, gouttelettes, grain = seeds fixes).

## 6. Calque texte (HTML/CSS), typographie cinétique, zones sûres

**Zones (repère 1080×1920)**
| Zone | y | Contenu |
|---|---|---|
| Haut interdit | 0-220 | **Seulement la pastille** « LE CHIFFRE QUI PIQUE · ÉP. 2 » (y 150-205, centrée, Inter Display Bold 26, majuscules espacées, contour 1,5 px `#B49CFF`, fond `rgba(5,7,26,.55)`) |
| Mention | 232-262 | « Simulation 3D » Inter Medium 22, `#AAB0D6` à 70 %, alignée à droite (x 940) |
| **Texte principal** | **290-760** | Phrases du script ; largeur x 90-940 (rien à droite de x 950 : boutons Instagram) |
| Petit texte | sous le bloc principal, au plus bas y 840 | « PROMIS », « en moyenne · vs le dimanche d'avant », « lun.-ven. · non significatif », source |
| Action 3D | 860-1500 | Téléphone, verre, poignet : aucun texte important ici (sauf les doubles 3D des chiffres) |
| Nuance permanente | 1530-1565 | Dès 4,6 s : « Étude UK Biobank · sommeil estimé par bracelet » Inter Medium 26 `#AAB0D6`, centrée |
| Signature | 1585-1660 | `brand/signature-officielle.png` **PNG tel quel**, largeur 240 px, centrée, opacité 0,85 (présente tout le Reel, comme demandé par le script) |
| Bas interdit | 1670-1920 | Rien d'important : oreiller flou uniquement |

**Polices** (dans `fonts/`) : Inter Display Black (chiffres, mots clés), Inter Display SemiBold (phrases), Inter Medium (mentions), Inter Display Light (heure de l'écran). Chiffres tabulaires.

**Mouvement du texte (innovation 3)**
- **Entrée « mise au point »** (10 images) : `filter: blur(14px) → 0`, `scale 1.06 → 1`, `letter-spacing +0.04em → 0`, opacité 0 → 1 sur les 4 premières images. Synchronisée avec le changement de mise au point de la caméra quand il y en a un.
- **Sortie** (6 images) : flou 0 → 10 px, dérive −14 px vers le haut, opacité → 0.
- **Lisibilité** : pas de halo sur les phrases ; ombre `0 4px 24px rgba(5,7,26,.9)` ; voile sombre radial sans bord derrière le bloc (`rgba(5,7,26,.5)` → 0) car le gobo de lune passe parfois derrière le texte.
- **Chiffres** : rouleau vertical (comme un réveil), flou de mouvement 6 px pendant le défilement, décélération finale.
- **Densité** : le script est déjà conforme (≤ 12 mots/écran) ; rien n'est ajouté.

## 7. Découpage plan par plan (textes exacts du script validé)

Notation : caméra position (x, y, z) → cible (x, y, z), en mètres.

### Plan 1 — 0,0 à 2,6 s · « Cette nuit, tu dors 1 h de plus ? » puis (1,5 s) « Pas vraiment. » ★ waouh d'accroche
- **Caméra** : (−0,03, 0, 0) → (−0,01, 0, −0,04), cible (0,02, −0,05, −0,74) ; poussée imperceptible + respiration. Roulis −5°.
- **Écran** : 02:59, deux-points à 1 Hz ; **1,40 s « 03:00 »** ; **1,50-1,75 s** glitch + rouleau arrière jusqu'à **« 02:00 »** (cf. §3). Petite ligne d'écran sous l'heure (Inter Medium, ambre à 60 %) : « sam. 24 oct. » à 0-1,4 s puis « dim. 25 oct. » (date du changement, issue de la fiche) — **à valider par le vérificateur ; sinon ne rien écrire sous l'heure**.
- **Lumière** : à 1,50 s, le gobo glisse de 22 cm vers la gauche sur le mur en 8 images (courbe ease-out), la poussière inverse son mouvement 1,50-1,75 s puis reprend sa chute.
- **Texte** : « Cette nuit, tu dors » SemiBold 64 blanc / « 1 h de plus ? » Black 104 lavande `#B49CFF` (y 300-560). **1,5 s** : la question remonte et se réduit (SemiBold 52, y 300-380) ; « Pas vraiment. » Black 112 blanc entre en mise au point (y 420-540), un trait rouge `#FF4D6A` passe sous « vraiment » en 6 images.
- **Son** : tic-tac doux (pendule d'une autre pièce) dès 0,0 ; respiration lente du dormeur à −34 dB ; **1,40 déclic** sec ; **1,50 rembobinage** (bande à l'envers 0,25 s + craquement numérique) ; 1,75 retour du tic-tac.

### Plan 2 — 2,6 à 4,6 s · « Devine : combien, en vrai ? » · petit « PROMIS »
- **Caméra** : **travelling latéral + poussée** du téléphone vers le verre : (−0,01, 0, −0,04) → (0,07, −0,01, −0,46), cible (0,09, −0,02, −0,74) ; FOV 40 → 32° (effet macro). Roulis −5 → −2°. Le téléphone passe en flou au premier plan gauche (sa lueur ambre reste sur le verre).
- **Verre vide** : à 3,1 s, le **trait « 60 » s'allume** de gauche à droite autour du cylindre (anneau émissif blanc, 8 images) ; le mot **« PROMIS »** apparaît **aussi** comme étiquette gravée lumineuse à côté du trait (double 3D du petit texte HTML).
- **Texte** : « Devine : combien, en vrai ? » SemiBold 66 (« combien » Black lavande) ; petit « PROMIS » Inter Display Bold 28 espacé, `#AAB0D6`.
- **Son** : nappe grave qui s'ouvre ; reflet sonore cristallin léger quand le trait 60 s'allume.

### Plan 3 — 4,6 à 7,8 s · « 7 211 Britanniques, 43-78 ans. » (« 43-78 ans » à 6,4 s) · nuance permanente apparaît
- **Caméra** : **panoramique vers le bas et la droite + recul** jusqu'au bord du lit : (0,07, −0,01, −0,46) → (0,14, −0,06, −0,30), cible (0,16, −0,13, −0,46). Le poignet (manche + capteur) est posé sur la couette au bord du matelas, **le verre reste visible flou en haut du cadre** (continuité). Mise au point sur le capteur (le texte entre en même temps : innovation 3).
- **Capteur** : LED lavande qui **pulse à 1 Hz** ; à chaque pulsation, une fine onde (anneau additif) part du capteur sur les plis de la couette.
- **5,6 s (données vivantes)** : la 3e onde s'étend sur toute la couette et allume **7 211 points** minuscules (`InstancedMesh`, 1 px à l'écran, lavande à 50 %) répartis dans les plis, comme une constellation de bracelets : un point par participant. Ils s'éteignent en 0,6 s. (Aucun nouveau chiffre : c'est le 7 211 du script.)
- **6,4 s** : « 43-78 ans » entre en mise au point.
- **Texte** : « 7 211 Britanniques, » Black 84 (« 7 211 » lavande) puis « 43-78 ans. » SemiBold 64. Nuance permanente en bas (y 1530-1565) dès 4,6 s, jusqu'à la fin.
- **Son** : **bip capteur** discret (sinus 2 kHz, 60 ms) à chaque pulsation ; « shimmer » doux à 5,6 s.

### Plan 4 — 7,8 à 10,2 s · « Le dimanche du changement, ils ont dormi… » · compteur 0 → 33 bloqué à 9,8 s
- **Caméra** : **remontée en grue + mise au point arrière** vers le verre : (0,14, −0,06, −0,30) → (0,10, −0,03, −0,56), cible (0,09, −0,02, −0,74), FOV 32 → 30°. Le poignet sort par le bas en flou.
- **Liquide** : monte de 0 à 33 (sur l'échelle 0-60 du verre) entre 8,0 et 9,8 s, **ease-out**, surface qui ondule, bulles qui montent, caustique violette qui grandit sur le bois. Les graduations s'allument une à une au passage. **9,8 s : arrêt net**, anneau d'onde + 30 gouttelettes, bloom en pointe.
- **Compteur** (HTML, rouleau) : 0 → 33 de 8,0 à 9,8 s, Black 150 lavande, au-dessus de la phrase ; se fige à 9,8 s.
- **Texte** : « Le dimanche du changement, » SemiBold 60 / « ils ont dormi… » SemiBold 60.
- **Son** : **remplissage dont la hauteur monte** (comme un vrai verre qu'on remplit : la résonance monte, 8,0-9,8 s) ; **ding** de verre à 9,8 s.

### Plan 5 — 10,2 à 12,6 s · « +33 min. Pas 60. » · petit « en moyenne · vs le dimanche d'avant » ★ waouh de donnée
- **Caméra** : **recul punch** (6 images, ease-out) : (0,10, −0,03, −0,56) → (0,08, −0,02, −0,45), cible (0,09, −0,015, −0,74) : tout le verre, trait 60 compris, est cadré ; roulis 0°. Micro-tremblé 1 image à l'impact.
- **Liquide fantôme** (innovation 2) : 10,2 s, le volume 33-60 s'allume en contour rouge hachuré ; **clignote 3 fois** (période 0,4 s) puis reste à 40 %.
- **Texte** : « +33 min. » Black 200 (les chiffres **se remplissent de liquide violet** de bas en haut en 0,4 s, masque CSS avec vague) ; « Pas 60. » Black 112 rouge `#FF4D6A` à 10,8 s ; petit « en moyenne · vs le dimanche d'avant » Medium 28 `#AAB0D6`.
- **Son** : **impact** grave (sub 45 Hz, 350 ms) à 10,2 ; trois petits « tics » électriques sur les clignotements.

### Plan 6 — 12,6 à 15,0 s · « Envoie ça à celui qui prévoit sa grasse mat'. » (levier de partage)
- **Caméra** : **panoramique filé** (8 images, flou directionnel) du verre vers le téléphone : → (0,00, −0,01, −0,40), cible (−0,06, −0,03, −0,74). Le verre (33 + fantôme) reste en flou à droite.
- **Écran** : notification « **Dimanche · réveil désactivé** » descend du haut de l'écran (12,7 s) ; à 13,0 s elle **se détache en carte de verre liquide** 3D (plan arrondi, réfraction simulée par décalage du fond flouté, reflet spéculaire qui glisse) et avance de 6 cm vers la caméra (innovation 5) ; une **icône d'envoi** (flèche « partager » du système, dessinée simplement, pas un avion en papier) pulse 2 fois à droite de la carte.
- **Texte** : « Envoie ça à celui qui » SemiBold 60 / « prévoit sa grasse mat'. » Black 84 lavande.
- **Son** : **swoosh** de notification (synthé maison, pas un son de marque) à 12,7 ; souffle doux quand la carte sort.

### Plan 7 — 15,0 à 18,2 s · « Et lundi ? L'écart retombe à ≈ 3 min. » · petit « lun.-ven. · non significatif »
- **15,0-15,3 s : clignement** (innovation 4) : paupière haute et basse (formes courbes noires, bord flou 30 px, légère teinte peau très sombre `#120C10` au bord), fermeture 4 images, noir 1 image, ouverture 4 images. Pendant le noir, le décor passe à **lundi** (gobo plus pâle, pré-aube encore sombre).
- **Caméra** (rouverte) : cadrage large téléphone + verre : (0,02, 0, −0,30), cible (0,04, −0,04, −0,74), roulis −5°.
- **Écran** : « **LUN 06:30** » qui sonne : l'écran pulse (luminosité 0,8 ↔ 1), le téléphone **vibre** sur son support (±0,6 mm, 25 Hz) ; ondes concentriques ambrées très légères autour.
- **Verre** : 15,6-17,4 s, le liquide **s'écoule de 33 à ≈ 3** (petit tourbillon à la surface, ease-in-out) ; le fantôme rouge s'étend donc de 3 à 60.
- **Texte** : « Et lundi ? » Black 96 / « L'écart retombe à ≈ 3 min. » SemiBold 60 (« ≈ 3 min » Black lavande) ; petit « lun.-ven. · non significatif » Medium 28.
- **Son** : **silence total** 15,0-15,3 ; **sonnerie** (mélodie synthé originale, 2 notes) à 15,3 ; **glouglou** d'écoulement 15,6-17,4.

### Plan 8 — 18,2 à 20,6 s · « Des horaires réguliers aident le sommeil (INSV). »
- **Caméra** : lent recul en grue (0,02, 0, −0,30) → (0,00, 0,03, −0,10), cible (0,03, −0,05, −0,74) : la table entière, le mur.
- **Aube** (innovation 1, suite) : le gobo vire au bleu aube `#9DB4FF` avec **liseré or** `#FFC46B` sur son bord haut, il glisse lentement dans le sens normal du temps ; la poussière devient dorée.
- **Écran** : écran « Réveils » : une ligne **« 06:30 »** avec interrupteur activé (le même réglage tous les jours, sans libellé de jours pour ne rien ajouter).
- **Gouttes en particules** : 7 gouttelettes violettes s'élèvent du verre et s'alignent en **une rangée régulière** au-dessus de la table (même hauteur, même espacement) : la régularité devient une image. Elles restent jusqu'à 20,6 s puis retombent dans le verre.
- **Texte** : « Des horaires réguliers » Black 76 / « aident le sommeil (INSV). » SemiBold 60.
- **Son** : nappe qui descend et s'éclaire ; **un seul** chant d'oiseau lointain à 18,6 s (CC0, discret).

### Plan 9 — 20,6 à 23,0 s · « Enregistre-le pour le ressortir dimanche. » · petit « de Lange et al. · J Sleep Res · 2024 »
- **Caméra** : poussée douce vers le verre (0,00, 0,03, −0,10) → (0,06, 0, −0,42), cible (0,09, −0,02, −0,74).
- **Marque-page néon** : le contour de l'icône « enregistrer » (ruban à encoche, trait néon lavande 3 px) **se dessine** (animation de tracé, 10 images) puis **se clipse sur le bord du verre** comme un marque-page (léger rebond). 
- **Texte** : « Enregistre-le pour le » SemiBold 60 / « ressortir dimanche. » Black 84 ; petit « de Lange et al. · J Sleep Res · 2024 » Medium 24 `#AAB0D6`.
- **Son** : **pop** feutré au clip.

### Plan 10 — 23,0 à 25,2 s · « Ép. 3 : le snooze, ça aide ? Abonne-toi »
- **Caméra** : retour vers le téléphone, (0,06, 0, −0,42) → (−0,02, 0, −0,20), cible (−0,04, −0,04, −0,74).
- **Écran** : gros bouton **SNOOZE** (pilule, ambre) qui pulse 3 fois (échelle 1 → 1,06) ; à 23,6 s la **pastille du haut bascule « ÉP. 2 » → « ÉP. 3 »** (rotation X de la pastille, 8 images, comme un chiffre de réveil à palettes).
- **Texte** : « Ép. 3 : le snooze, ça aide ? » SemiBold 62 (« le snooze » Black lavande) / « Abonne-toi » Black 84 blanc, soulignement lavande qui se trace.
- **Son** : **sonnerie courte** (les mêmes 2 notes, une fois) à 23,0.
- **Préparer la boucle** dès 24,4 s : l'aube redescend vers la nuit (gobo bleu nuit), l'écran s'assombrit.

### Plan 11 — 25,2 à 26,0 s · « Cette nuit, tu dors 1 h de plus ? »
- **Caméra** : arrive à **la pose exacte de l'image 0** à 25,5 s (même FOV 40°, même roulis −5°, même cible) et y reste (respiration seule).
- **Décor** : nuit, gobo à sa position de départ, verre **vide** (le liquide et le fantôme s'éteignent 25,2-25,4 s), écran 02:59, pastille de nouveau « ÉP. 2 ».
- **Texte** : « Cette nuit, tu dors 1 h de plus ? » identique à l'image 0.
- **Son** : tic-tac calé pour se raccorder au tic de 0,0 s.
- **Dernière image (26,0 s) = image 0** : la boucle repart sans saut.

## 8. Son (récapitulatif)

| Couche | Description | Niveau |
|---|---|---|
| Ambiance | Silence de chambre (bruit de pièce très bas), respiration lente du dormeur (pas de voix), tic-tac lointain : **le fil rouge** du début et de la fin | −24 LUFS court terme |
| Ponctuations | déclic 1,40 · rembobinage + craquement numérique 1,50 · bip capteur · shimmer 5,6 · remplissage qui monte · ding 9,8 · impact 10,2 · swoosh 12,7 · **silence 15,0-15,3** · sonnerie 15,3 · glouglou · oiseau · pop · sonnerie courte 23,0 · tic-tac 25,2 | crêtes −1 dBTP |
| Nappe | Accord grave tenu, s'éclaire à l'aube (seul moment lumineux) | −26 |
| Mixage | Intégré −14 LUFS ; **vérifier que la piste n'est pas muette** (`tools/qa/check_reel.py`) | — |

Sources : synthèse dans `audio.py` (squelette du piéton) + banques **CC0** ; aucune sonnerie de marque (pas de sonnerie iPhone). Zéro dépense.

## 9. Points de vigilance (à trancher avant rendu)
1. **Date sous l'heure** (« sam. 24 oct. » → « dim. 25 oct. ») : vient de la fiche (25/10), mais c'est un texte de plus à l'écran. Le vérificateur décide ; par défaut, **rien sous l'heure**.
2. **Échelle du verre** : 0 à 60 « min » ; seul le trait « 60 » est étiqueté. Le niveau 33 et ≈ 3 doivent être **exacts** sur cette échelle (33/60 = 55 % de la hauteur utile ; 3/60 = 5 %).
3. **Capteur sans écran** : ne pas dessiner une montre connectée avec cadran (exactitude UK Biobank : accéléromètre au poignet, porté 2013-2015). La LED est une liberté graphique minimale.
4. **7 211 points** : un point par participant, sans légende supplémentaire ; s'ils rendent mal en SwiftShader (scintillement), remplacer par 7 211 points sur une seule texture précalculée.
5. **« Simulation 3D »** visible du début à la fin (y 232-262), jamais masquée par la pastille qui bascule.
6. **Planche de contrôle avant capture complète** : `capture.py --apercu 0,1.45,1.6,1.8,3.2,5.7,6.5,9.8,10.4,13.2,15.15,16.5,19.5,21.5,23.7,25.6,26.0` → 0 chevauchement, image 0 lisible en vignette 395 px, gobo visible mais derrière le texte jamais plus clair que `#2A3470`, niveaux 33 et ≈ 3 justes, 26,0 = 0,0.

## 10. Faisabilité

| Élément | Moteur maison | Plan réel d'Anthony | OpenArt (via ChatGPT) |
|---|---|---|---|
| Chambre, table, téléphone, verre, liquide, fantôme, gobo, poussière, capteur, manche | **Oui** (géométries simples, canvas, additifs ; aucun asset externe) | — | — |
| Écran du téléphone (heure, notification, réveils, SNOOZE) | **Oui** (canvas redessiné à chaque image) | — | — |
| Clignement, typo « mise au point », carte en verre liquide | **Oui** (CSS + un plan 3D) | — | — |
| Sons | **Oui** (`audio.py` + CC0) | Option : tic-tac d'une vraie pendule, eau versée dans un verre (30 s chacun) | — |
| Image 0 photoréaliste | Pas nécessaire | — | Option seulement si l'aperçu de l'image 0 est jugé pauvre ; alors `isAiGenerated: true` |

**Temps** : écriture de la scène 2 h 30, aperçus 15 min, capture ≈ 21 min (780 × 1,6 s), audio 30 min. **Plan B** si retard : supprimer le livre, les 7 211 points, la carte en verre (notification restant dans l'écran), garder gobo + fantôme + clignement.

### Prompt OpenArt (option image 0 uniquement)
> Ultra-realistic cinematic photograph, vertical 9:16, 1080x1920, first-person view of someone lying in bed at night, head on the pillow, camera slightly tilted. Out-of-focus white linen pillow edge filling the bottom of the frame. On a dark walnut nightstand at eye level: a modern smartphone standing on a small stand, night-mode lock screen showing large warm amber digits "02:59", a thin white charging cable, and an empty tall clear drinking glass with fine engraved graduation lines, lit by the phone's warm amber glow. Behind, a deep navy bedroom wall with a cold blue moonlight window pattern (four panes and a cross frame) projected diagonally, faint dust in the moonbeam, a switched-off bedside lamp in silhouette on the left. Top 35% of the frame is clean dark negative space for text. 35mm lens, f/1.8, shallow depth of field, premium sleep-tech commercial look. No people, no hands, no text other than the phone clock, no logo, no stars, no rain, no oversaturation.

Négatif : `cartoon, illustration, watermark, logo, person, face, hands, rain, stars, neon grid, bright room, daylight, oversaturated, analog clock`.

## 11. Références par choix

| Choix | Références |
|---|---|
| POV depuis le lit, lieu vécu | [Know Your Meme — « Alright bro goodnight » (23 à 49 M vues par variante, 2021)](https://knowyourmeme.com/memes/alright-bro-goodnight-i-forgot-to-get-my-water) · leçon 19/10 (piéton 70,1 % > 3 s) · [Bustle — POV « you walk into my room »](https://www.bustle.com/life/pov-you-walk-into-my-room-tiktok-trend-rodger-cleye) |
| Lumière de fenêtre comme narration (gobo) | [Superhive — 50 gobo alphas (2026)](https://superhivemarket.com/products/50-cinematic-gobo-light-alphas-vol1) · [three.js forum — texture projetée](https://discourse.threejs.org/t/what-does-the-textures-map-do-for-a-spotlight-and-do-i-need-one/44357/4) · [Videobolt — volumetric lighting](https://videobolt.net/motion-graphics-glossary/volumetric-lighting) |
| Jauge liquide rendue physique, deux états dans un objet | [Framer — dynamic liquid gauge](https://www.framer.com/marketplace/components/dynamic-liquid-gauge/) · [Power BI — liquid fill gauge](https://powerbi.microsoft.com/blog/visual-awesomeness-unlocked-liquid-fill-gauge/) · [BlitzCut — transformation split, 03/09/2026](https://blitzcutai.com/blog/visual-hooks-instagram-reels) |
| Carte en verre liquide, vraie interface | [STRV — Liquid Glass](https://strv.com/blog/liquid-glass-and-the-future-of-design) · [Wikipedia — Liquid Glass](https://en.wikipedia.org/wiki/Liquid_Glass) · [Instrument — Oura app (couleur sémantique, lecture en un coup d'œil)](https://www.instrument.com/work/oura-app) |
| Typo cinétique, glitch numérique mesuré | [autoae — tendances 2026](https://autoae.online/blog/motion-graphics-trends-2026) · [Motionographer — prédictions](https://motionographer.com/2025/01/02/25-for-2025-the-motionographers-crystal-ball-motion-design-predictions-part-2/) · [Linearity — kinetic typography](https://www.linearity.io/blog/kinetic-typography/) |
| Angle « l'heure en plus n'est pas du sommeil en plus » (débat) | [Axios 30/10/2025 — illustration plate d'un réveil : la presse reste en 2D](https://www.axios.com/2025/10/30/time-change-fall-back-2025) · [IBTimes 19/10/2026 — « give me the damn extra hour in bed »](https://www.ibtimes.co.uk/uk-clocks-change-social-media-debate-winter-darkness-1826496) |

## 12. Prédiction (à comparer avec l'analyste à J+1 et J+3)
- **> 3 s : 60-70 %** (POV lieu vécu + objet familier 02:59 + glitch à 1,5 s ; famille sommeil, la plus forte). Sous 50 % : l'image 0 est en cause (téléphone trop petit ou trop sombre), pas le sujet.
- **Partages** : ciblage nommé à 12,6 s + argument de débat 33 / 60 / 3 + timing (veille du changement). Objectif ≥ 5 / 1 000 vues (le compte est à ≈ 0).
- **Enregistrements** : demande datée (« pour le ressortir dimanche ») + marque-page visuel ; objectif ≥ 5 / 1 000.
- **Signal à lire en commentaires** : « 33 min ?! » ou « moi c'est 0 » = l'argument de débat fonctionne.
- **Biais** : publication samedi 07:00 (créneau nouveau) ; ne pas comparer directement aux Reels du soir.
