# Playbook Lifestyles — règles communes à tous les agents

Version 2 — 17/10/2026. **Chaque agent lit ce fichier avant de travailler.** En cas de conflit, ce playbook prime sur les habitudes ; la décision explicite la plus récente d'Anthony prime sur le playbook.

## 1. L'objectif
Un Reel réussi = **arrêter le pouce** (0-2 s) → **garder jusqu'au bout** (rétention ≥ 60 %) → **déclencher un envoi en message privé** (partage) → **donner une raison de s'abonner** (série, promesse de suite).
Les partages sont la métrique n°1 : c'est elle qui pousse Instagram à montrer la vidéo à des non-abonnés. Aujourd'hui : 1 partage sur 7 jours. C'est le levier principal.

## 2. Les 4 critères d'un sujet qui marche (tous obligatoires)
1. **Contre-intuitif** : contredit une croyance répandue ou révèle un chiffre que personne ne connaît.
2. **Personnel** : le spectateur se reconnaît en moins de 2 s (« tu », sa journée, son corps, sa maison, sa voiture).
3. **Vérifiable** : source primaire solide, chiffre exact.
4. **Envoyable** : on pense immédiatement à **une personne précise** à qui l'envoyer.

## 3. Formules d'accroche (choisir, adapter, ne pas copier mot à mot)
| Formule | Modèle | Exemple |
|---|---|---|
| Croyance cassée | « Tu crois X ? En fait Y. » | « Tu vises 10 000 pas ? 7 000, c'est déjà beaucoup. » |
| Chiffre choc personnel | « [situation banale] = [conséquence chiffrée] » | « Debout depuis 17 h ? Ton cerveau roule à 0,5 g/L. » |
| Erreur quotidienne | « Tu fais ça tous les jours. C'est une erreur. » | « Tu rinces tes pâtes ? Tu jettes la meilleure partie. » |
| Révélation cachée | « Personne ne te dit que… » | « Ton éponge contient plus de bactéries que… » |
| Test immédiat | « Fais ce test maintenant. » | « Pose ta main sur ton ventre et respire. » |
| Compte à rebours | « Dans X secondes tu sauras si… » | « Dans 20 s tu sauras si tu dors assez. » |

Règles : ≤ 10 mots, un chiffre ou une contradiction, tutoiement, **lisible sans le son**, visible dès l'image 0.

## 4. Les 7 règles de rétention
1. **Boucle ouverte** dans les 3 premières secondes (« et le pire, c'est la fin »), refermée à la fin.
2. **Changement visuel toutes les 1,5 à 2,5 s** : nouveau texte, zoom, compteur, coupe, couleur.
3. **Jamais d'écran vide**, jamais plus de 12 mots à l'écran.
4. **Un seul fil** : un sujet, une idée, une conséquence.
5. **La révélation personnelle** arrive aux deux tiers (« Le piège : réveillé à 7 h, tu y es à minuit »).
6. **Durée 18-28 s**. Couper tout ce qui ne sert pas l'accroche.
7. **Fin qui relance** : la dernière image renvoie à l'accroche, pour que la boucle reparte.

## 5. Les leviers de partage (au moins 2 par Reel)
- **Ciblage nommé** : « Envoie ça à quelqu'un qui… » + profil précis et drôle ou bienveillant.
- **Utilité immédiate** : une action réalisable aujourd'hui en moins de 2 minutes.
- **Argument de débat** : un chiffre qu'on a envie de ressortir en famille.
- **Protection** : « ça peut éviter un accident ou une erreur à quelqu'un que tu aimes ».
- **Identité** : « les sportifs qui… », « les parents qui… ».

## 6. Plus réel : règles visuelles
- **Mélanger du réel et du néon.** Fond = vraie image ou vraie vidéo (rush d'Anthony, photo fournie, plan OpenArt photoréaliste) assombrie de 55-70 %. Par-dessus : textes et graphiques néon Lifestyles.
- **Ressources réelles** : dossier `assets/broll/` du dépôt, classé par thème (`sport/`, `cuisine/`, `nature/`, `nuit/`, `route/`, `corps/`). Si rien ne colle, l'agent producteur **le signale et demande un rush** au lieu de livrer du texte seul.
- Un objet physique filmé vaut mieux qu'une icône : un vrai téléphone, une vraie montre, une vraie route de nuit.
- Visages : jamais de personne identifiable sans accord ; silhouette d'Anthony de dos ou de 3/4 autorisée.
- IA photoréaliste : provenance notée dans le journal, et `isAiGenerated: true` à la publication si un plan réaliste est généré par IA.

## 7. Seuils de qualité (sinon on refait)
| Étape | Seuil |
|---|---|
| Sujet | ≥ 21/25 et les 4 critères obligatoires validés |
| Accroche | 3 versions écrites, la meilleure notée ≥ 8/10 par le scénariste **et** le contrôleur |
| Faits | 100 % des chiffres avec source primaire ou organisme officiel, verdict VALIDÉ |
| Vidéo | planche relue, 0 chevauchement, 0 écran vide, accroche visible image 0 |
| Gate | 10/10 points ✅, sinon NO-GO |

## 8. Boucle d'apprentissage
- Chaque publication → une ligne dans `data/journal-publications.md` (sujet, formule d'accroche, levier de partage, style, réel ou motion, heure).
- Chaque soir → l'analyste met à jour `data/lecons.md` : ce qui marche se renforce, ce qui échoue deux fois est abandonné.
- Tests A/B : **une seule variable** à la fois (accroche OU style OU durée), sur deux jours différents.

## 9. Objectifs de croissance (suivis par l'agent growth)
| Indicateur | Point de départ (17/10) | Objectif 30 jours |
|---|---|---|
| Vues médianes par Reel | 27 | 300 |
| Partages / 1 000 vues | ≈ 0 | 10 |
| Enregistrements / 1 000 vues | ≈ 0 | 15 |
| Abonnements / 1 000 vues | n.d. | 5 |
| Abonnés | 2 310 | 3 000 |

## 10. Contrôle visuel automatique
Toute vidéo passe par `tools/qa/check_reel.py` (format, durée, son audible, images vides, plans figés, rythme, luminosité, zone sûre, contraste de l'accroche). Score ≥ 90 et aucun ÉCHEC avant publication.

## 11. Règles absolues
Vérité (programmé ≠ publié), zéro dépense, signature officielle jamais redessinée, un sujet = un Reel, anti-répétition 3 mois, pas de promesse santé, secrets jamais dans le dépôt.
