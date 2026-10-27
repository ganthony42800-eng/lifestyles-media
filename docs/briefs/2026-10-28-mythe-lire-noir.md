# Brief créatif — Mythe ou science ? ép. 6 : lire dans le noir abîme les yeux ? (28/10/2026)

Directeur de création (consignes du chef d'orchestre), complété par le motion designer 3D le 27/10.
Script : `work-noir/script-valide.md` (textes exacts) · fiche : `work-noir/fiche-validee.md`.

## Remise en question (protocole § 0)
- Ép. 3 thermique, ép. 4 télésiège (grand décor), ép. 5 goutte (macro, plongée dans une sphère) : l'ép. 6 ne plonge dans aucun objet et n'utilise ni pluie ni néon de rue. Le fil n'est plus un objet mais **une lumière** (le faisceau de la lampe torche), et le récit est un **passage de lumière** : nuit chaude sous la couette → jour froid.
- Leçon 19/10 : la 3D accroche en POV humain d'un lieu vécu → image 0 = TOI, à plat ventre sous la couette, le livre ouvert, la lampe dans la main droite.
- Leçons techniques 23-26/10 appliquées : fondus terminés avant le texte suivant, bloom au seuil > 2 sur les plans de jour, petits textes ≥ 30 px, audio plafonné −3,5 dBFS, signature basse remontée à y = 1396 (bas à 1474, test de la légende Instagram), contrôle ffprobe -count_frames.
- Veille externe (27/10) : faisceaux volumétriques en three.js (Codrops, rayons volumétriques), tests « cloth peel reveal » (révélation par tissu qui se soulève), BHVI : le temps dehors ajouté au calculateur de risque de myopie (mai 2026), presse « mythe lecture dans le noir » (Zeiss, CBC, WebMD) toujours illustrée par photos de banque d'images : personne ne montre la lumière elle-même comme preuve.

## Concept : « Le faisceau »
La lampe torche éclaire la page → se tourne vers toi (flare) → éclaire ton iris, qui se contracte, et tes paupières qui clignent moins → revient sous la couette, vacille, s'éteint (0,2 s de silence) → la couette s'arrache : le jour entre par la fenêtre → on sort par la fenêtre au-dessus de deux cours d'école → les élèves s'envolent et forment un globe → retour à la chambre → la couette retombe, la lampe se rallume : image 0.

## Image 0
POV sous une couette matelassée crème : plis éclairés par en dessous (rebond ambre de la page), faisceau volumétrique plein de poussière, livre ouvert (vraie page imprimée), lampe métal en bas à droite. Question en haut ≥ 90 px (« yeux » en ambre), pastille « MYTHE OU SCIENCE ? · ÉP. 6 » agrandie (32 px), signature officielle en petit.

## Innovations (vs ép. 5)
1. **Lumière volumétrique en marche de rayons** (raymarching plein écran, analytique) : un même shader rend le cône de la lampe la nuit et les rayons de la fenêtre le jour, avec l'ombre des croisillons dans la poussière.
2. **Œil macro anatomique** : globe + iris procédural (fibres, collerette, limbe), cornée à reflet de la lampe, pupille qui se contracte sous le faisceau, paupières découpées en amande sur une peau en relief avec cils en shader ; compteur 19,7 → 11,4 /min sans chiffre intermédiaire net.
3. **Moment waouh (8,45 s, après 0,2 s de silence)** : la couette (géométrie recalculée à chaque image) s'arrache depuis le pied du lit, le jour bleuté inonde la chambre.
4. **Données vivantes humaines** : 2 × 1 000 élèves en 3D vus d'en haut (effet tilt-shift « maquette »), 395 puis 304 s'allument (39,5 % / 30,4 % exacts), puis les élèves s'envolent et forment un globe de 4 000 personnes dont 2 000 s'allument (1 sur 2).
5. **Typo « à la lampe »** : chaque texte entre par un masque qui balaie de gauche à droite comme un faisceau.

## Palette
Ambre lampe (#FFC36B / #FFB347), cyan-blanc jour (#DDF3FF / #8FD3FF), corail Lifestyles (#FF6A55) pour l'alerte, nuit bleu Lifestyles (#060B1E). Jamais cartoon.

## Son (original, synthèse procédurale, sans voix)
Chambre la nuit étouffée (souffle sous la couette, froissement de tissu), nappe La majeur 9 chaude, clic de lampe, page tournée, souffle du flare, clignements (petits « tic » mouillés), roulement du compteur, grésillement de la lampe qui vacille, SILENCE 8,25-8,45, arrachement de la couette (whoosh) + accord clair du jour + oiseaux synthétisés, 395 puis 304 tics granulaires (gauche puis droite), envol vers le globe, 2 000 scintillements, tampon du verdict, scintillement de la signature, couette qui retombe + clic de la lampe (boucle).

## Couverture
Image à 1,2 s : couette + faisceau + question seule + pastille ÉP. 6 + signature.
