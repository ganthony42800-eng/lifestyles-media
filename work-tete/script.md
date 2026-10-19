# Script — Mythe ou science ? · ÉP. 3 : on perd la moitié de sa chaleur par la tête ? (verdict NUANCE)

Publication : mardi 20/10/2026 12:00. Durée : **25,8 s** (774 images à 30 i/s). Sans voix off.
**90 mots** en texte principal (≤ 0,25 s/mot respecté écran par écran ; seul l'écran 12, raccord de boucle, reprend l'accroche déjà lue). Petits textes courts (sources, ≤ 10 mots).
Chiffres : **uniquement** `work-tete/fiche-validee.md` (40-45 % = mythe seulement, ≈ 7 %, ≈ 10 %, 19 %). +42 % non utilisé (voir § Choix).
Plan réel : `assets/broll/` vide → tout en 3D three.js. Aucun visage : silhouette de dos uniquement, bébé = silhouette de verre sans traits.

## 0. Protocole de remise en question (§ 0 du playbook)
- **Recherche externe** : je n'ai pas d'outil web dans cette tâche (lecture/écriture de fichiers seulement). Étape non réalisée, je le signale ; je me suis appuyé sur les stats internes (`data/lecons.md`, consignes du 19/10).
- **Comparaison sans complaisance avec l'ép. 2** : l'image 0 de l'ép. 2 montrait un objet abstrait (doigt-radio). Or le taux > 3 s décide de tout (piéton POV 70 %, vitamine C 3D abstraite 23,6 %).
- **Nouveautés de l'ép. 3** :
  1. **Image 0 = lieu vécu en POV + situation humaine** : on marche derrière quelqu'un dans une rue froide, la nuit, vu par une **caméra thermique**. La tête nue « brille ». La 3D sert un lieu, pas un objet abstrait.
  2. **Palette thermique « néon Lifestyles »** comme signature de la série hiver : le froid en bleu-violet, le chaud en magenta → orange → blanc. La caméra thermique rend la donnée visible sans lire.
  3. **Accroche visuellement piégée** : l'image 0 montre exactement le cas « vrai » (corps couvert, tête nue = tête brûlante). Aux 2/3 on revient au même plan et le spectateur comprend ce qu'il regardait depuis le début. Boucle refermée par l'image elle-même.
  4. **Partage avec retournement** : « Envoie ça à celle qui crie “Mets ton bonnet !” » + « Elle a raison… à moitié. » On l'envoie pour taquiner ET pour donner raison (pas de conflit, donc plus d'envois).

## 1. Les 3 accroches (3 formules différentes)

| | Formule | Accroche (≤ 10 mots) | Arrêt du pouce | Clarté sans le son | Exactitude | Personnel | **Note /10** |
|---|---|---|---|---|---|---|---|
| **A (retenue)** | Croyance cassée | « **Ta tête perd la moitié de ta chaleur ?** » puis à 1,6 s « **Non… sauf un cas.** » | 9 | 10 | 9 (le « cas » = nuance validée) | 9 | **9/10** |
| B (réserve A/B) | Erreur quotidienne | « Bonnet sur la tête, blouson ouvert ? Mauvaise fuite. » | 8 | 7 | 8 | 9 | **7,5/10** |
| C (réserve A/B) | Compte à rebours | « Dans 20 s, tu sauras si ton bonnet sert. » | 7 | 9 | 9 | 8 | **7,5/10** |

Pourquoi A : c'est la croyance que tout le monde a entendue petit (débat immédiat), la question est lue seule pendant 1,6 s (règle « réponse à ≥ 1,5 s »), et « sauf un cas » ouvre la boucle dans les 3 s sans mentir (verdict NUANCE).
B : bonne idée de fond mais demande un temps de lecture ; « mauvaise fuite » est flou sans le son. C : clair mais froid, sans contradiction visible. B ou C pour un A/B ultérieur (une seule variable : l'accroche).

## 2. Script (scènes = décors 3D ; écrans = changements de texte)

Pastille permanente 0-25,8 s (visible dès l'image 0) : **MYTHE OU SCIENCE ? · ÉP. 3** en haut. Signature officielle (`brand/signature-officielle.png`) + trèfle + @lifestyles_hf en bas. Zone sûre respectée (texte principal au centre-haut, rien sur le bas 20 %).
HUD caméra thermique sur les scènes rue : coins de visée, point « REC », barre de couleur froid → chaud **sans aucune graduation chiffrée** (aucun chiffre hors fiche à l'écran).

| Scène | Écran | Début-fin (s) | Texte principal (exact) | Petit texte (exact) | Visuel (3D three.js) | Son |
|---|---|---|---|---|---|---|
| 1 · Rue thermique (POV) | 1 | 0,0-3,0 | **Ta tête perd la moitié de ta chaleur ?** puis à 1,6 s **Non… sauf un cas.** | — | **Image 0** : rue de nuit, pavés mouillés, réverbères, en vue thermique. Caméra à hauteur d'épaule qui suit une silhouette de dos (léger balancement de marche). Doudoune bleu-violet (froide), **tête nue blanc-orange qui « brille »**, buée qui s'échappe. Accroche déjà lisible, « LA MOITIÉ » en néon magenta. À 1,6 s : givre qui craque sur « LA MOITIÉ », le mot se fendille, « Non… sauf un cas. » apparaît, un viseur se pose et se verrouille sur la tête. | Vent d'hiver + pas sur pavé mouillé ; bip de caméra thermique à 0,0 ; craquement de glace à 1,6 s ; « tic » de verrouillage du viseur à 2,6 s |
| 2 · Le mythe | 2 | 3,0-5,2 | **Le mythe : « 40 à 45 % »** | Manuel de survie de l'armée US · cité par Vreeman & Carroll · BMJ · 2008 | Coupe : vieux manuel militaire en 3D (papier jauni, pochoir kaki) qui s'ouvre ; une jauge en verre sort de la page et grimpe à 40… 45 %. À 4,6 s, tampon néon rouge « MYTHE » qui s'écrase dessus. | Page qui tourne ; montée de compteur ; tampon sourd à 4,6 s |
| 3 · Mannequin de verre | 3 | 5,2-7,4 | **Ta tête ≈ 7 % de ta surface.** | adulte · Lund & Browder · 1944 | Transition : la silhouette de la rue devient un **mannequin de verre** (de dos, sans visage), surface pavée de petites tuiles. Seules les tuiles de la tête s'allument (cyan) ; compteur 0 → ≈ 7 %. | Whoosh de transition ; ticks cristallins à chaque tuile |
| 3 · Mannequin de verre | 4 | 7,4-9,8 | **Chaleur perdue par la tête : ≈ 10 %** | dans l'eau à 17 °C · Pretorius et al. · J Appl Physiol · 2006 | Le mannequin est immergé dans un bassin d'eau froide (bleu, réfraction, bulles). Des particules de chaleur quittent le corps ; celles de la tête sont colorées magenta. Jauge de verre à côté : ligne fantôme « 45 % » en pointillé, le liquide s'arrête à ≈ 10 %. | Plongeon étouffé ; sous l'eau ; « ding » grave à l'arrêt de la jauge |
| 3 · Mannequin de verre | 5 | 9,8-11,8 | **Sa part, à peu près. Pas la moitié.** | — | **Comparaison côte à côte** : 3 colonnes de verre, ≈ 7 % (surface, cyan), ≈ 10 % (pertes, magenta), 45 % (mythe, rouge) que barre un trait néon. | Deux « ding » + rayure néon sur la colonne mythe |
| 4 · Retour rue thermique (la nuance) | 6 | 11,8-14,2 | **Mais corps couvert, tête nue : là, elle compte.** | — | **Silence 0,3 s à 11,8.** Retour au plan exact de l'image 0 (même silhouette, même rue). Le viseur zoome : la doudoune passe au violet très sombre (bien isolée), la tête reste blanche. Le spectateur comprend ce qu'il regardait depuis 0 s. **Boucle « sauf un cas » refermée.** | Silence puis battement grave ; vent qui revient |
| 4 · Retour rue thermique | 7 | 14,2-16,2 | **Elle devient ta principale fuite.** | le cuir chevelu se resserre peu au froid · Pretorius 2006 | Un panache de chaleur monte de la tête comme une fumée (seule zone chaude de l'image) ; flèche néon « FUITE » qui pulse au-dessus. | Souffle qui s'échappe (son de fuite d'air), pulsation |
| 5 · Bébé de verre | 8 | 16,2-18,4 | **Chez un bébé : tête = 19 % du corps.** | surface · moins d'un an · Lund & Browder · 1944 | Côte à côte : silhouette de verre adulte (tête ≈ 7 %, cyan) et **silhouette de bébé de verre, sans traits** (tête 19 %, magenta). Les tuiles de la tête du bébé s'allument ; compteur 0 → 19 %. | Petite boîte à musique cristalline + ding à 19 % |
| 5 · Bébé de verre | 9 | 18,4-20,4 | **Par grand froid : couvre tout, tête comprise.** | geste du jour : pose le bonnet à côté des clés | Un bonnet en verre néon vient se poser sur la tête du bébé puis sur celle de l'adulte ; la chaleur cesse de s'échapper (le panache s'éteint). | Pop doux ×2, puis le vent se coupe |
| 6 · Partage | 10 | 20,4-22,8 | **Envoie ça à celle qui crie « Mets ton bonnet ! »** | Elle a raison… à moitié. | Icône envoi néon qui pulse ; derrière, le bonnet de verre qui tourne lentement. | Swoosh d'envoi ; rappel du craquement de glace |
| 7 · Série / abonnement | 11 | 22,8-25,0 | **Ép. 4 : le froid donne le rhume ? Abonne-toi** | Enregistre pour le premier jour de gel | Mouchoir en verre qui s'envole d'une boîte, givre sur les bords de l'écran ; bouton « S'abonner » néon + icône « Enregistrer ». Aucun chiffre. | Souffle froid ; petit éternuement stylisé (synthé, pas de voix humaine) ; pop |
| 1 · Rue thermique (raccord) | 12 | 25,0-25,8 | **Ta tête perd la moitié de ta chaleur ?** | — | Retour au cadrage exact de l'image 0 (même balancement, même HUD) : raccord de boucle invisible. | Vent + pas ; coupe nette sans craquement (le craquement arrive au replay à 1,6 s) |

Rythme : changement de texte ou de visuel au plus toutes les 2,4 s (écrans 1 et 2 ont un changement interne à 1,6 s et 4,6 s).
Source en une ligne avant 8 s : BMJ 2008 à 3,0 s, Lund & Browder à 5,2 s, **Pretorius et al. · J Appl Physiol · 2006 à 7,4 s**.
Révélation personnelle aux 2/3 : écrans 6-7 (11,8-16,2 s), phrase obligatoire de la fiche à l'écran mot pour mot.
Visualisations sans lecture : jauge 45 % qui s'écrase, tuiles qui s'allument (7 %), jauge avec ligne fantôme (≈ 10 % contre 45 %), 3 colonnes côte à côte, vue thermique (doudoune froide / tête brûlante), adulte et bébé côte à côte.

Contrôle densité (texte principal) : É1 12 mots / 3,0 s · É2 5 / 2,2 · É3 7 / 2,2 · É4 7 / 2,4 · É5 7 / 2,0 · É6 8 / 2,4 · É7 5 / 2,0 · É8 8 / 2,2 · É9 7 / 2,0 · É10 9 / 2,4 · É11 8 / 2,2 · É12 raccord (accroche déjà lue). Tous ≥ 0,25 s/mot.

## 3. Leviers de partage (4)
1. **Ciblage nommé** : « Envoie ça à celle qui crie “Mets ton bonnet !” » (mère, grand-mère, conjointe), adouci par « Elle a raison… à moitié. »
2. **Argument de débat** : 45 % (mythe) contre ≈ 7 % / ≈ 10 %, en colonnes côte à côte, un chiffre qu'on ressort à table.
3. **Protection** : bébé, tête = 19 % de la surface du corps → « couvre tout, tête comprise ».
4. **Utilité immédiate** : poser le bonnet à côté des clés (moins de 10 s) + « Enregistre pour le premier jour de gel ».
Raison de s'abonner visible : pastille ÉP. 3 en permanence + écran « Ép. 4 : le froid donne le rhume ? Abonne-toi ».

## 4. Question pour les commentaires (commentaire épinglé)
« Chez toi, qui crie “Mets ton bonnet !” : ta mère, ta grand-mère… ou toi ? »
(Variante débat pour la story sondage : « Tu sors tête nue l'hiver ? Oui / Jamais ».)

## 5. Légende (précaution obligatoire de la fiche)
Accroche + « Par grand froid, couvre tout, tête comprise. Bébé ou signes d'hypothermie : demande conseil à un professionnel de santé. Ceci n'est pas un avis médical. » + sources (Vreeman & Carroll, BMJ 2008 ; Pretorius et al., J Appl Physiol 2006 ; Lund & Browder 1944) + « Ép. 4 jeudi : le froid donne le rhume ? » (jour à confirmer par le planning ; promesse à tenir, cf. leçon 18/10).

## 6. Choix et points à faire vérifier
- **+42 % non utilisé à l'écran** : à côté de « ≈ 10 % », deux pourcentages de nature différente dans le même Reel brouillent le message (risque de lecture « 42 % par la tête = presque le mythe »). Réservé pour un commentaire de réponse ou un carrousel.
- « la moitié » n'est utilisée que dans la question (la croyance populaire) ; le chiffre du mythe à l'écran est celui de la fiche : 40 à 45 %.
- « Sa part, à peu près » reprend la conclusion de la fiche (« à peu près en proportion de sa surface »).
- « Elle devient ta principale fuite » reprend « la tête nue devient la principale fuite » (conclusion validée).
- **Écart avec la consigne** : « couvre d'abord le tronc » n'est pas dans la fiche ; remplacé par la formulation validée « Par grand froid : couvre tout, tête comprise. » À confirmer par le vérificateur si on veut l'ordre « tronc puis tête ».
- Écran 2 : « 40 à 45 % » est toujours encadré par « Le mythe » et le tampon MYTHE, jamais présenté comme un fait.
- Interdits de la fiche vérifiés : pas de « 0 % », pas de « le bonnet ne sert à rien », pas de « −4 °C », pas de « 1970 », pas de « années 1950 », « 10 % » toujours avec « ≈ » et « dans l'eau à 17 °C ».
- HUD thermique : aucune température chiffrée (sinon chiffre hors fiche).

## 7. Idée d'épisode 4
**« Le froid donne le rhume ? »** (promis à l'écran, sans chiffre). Fil probable : verdict NUANCE (ce sont les virus qui donnent le rhume ; la question est de savoir si le froid aide). Image 0 dans la même logique gagnante : POV, situation humaine, pieds dans une bassine d'eau froide ou sortie cheveux mouillés, vue thermique (continuité visuelle de la série hiver). Pistes de sources à faire lire en primaire par le vérificateur (rien à l'écran avant validation) : études d'exposition au froid et apparition de symptômes de rhume, travaux sur la température nasale et la réplication des rhinovirus. Partage visé : « Envoie ça à celui qui sort les cheveux mouillés ».
