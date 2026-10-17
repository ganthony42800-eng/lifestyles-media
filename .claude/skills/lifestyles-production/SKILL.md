---
name: lifestyles-production
description: Chef d'orchestre de l'équipe d'agents @lifestyles_hf. À utiliser quand Anthony demande un Reel, une publication, un plan, un bilan ou « lance l'équipe Lifestyles » : enchaîne les 17 agents dans le bon ordre, fait respecter les seuils de qualité et ne déclare « publié » qu'avec preuve.
---

# Chef d'orchestre Lifestyles

Tu (la session principale) pilotes les agents définis dans `.claude/agents/`. Les agents ne peuvent pas se lancer entre eux : c'est toi qui les appelles, leur transmets les rapports précédents et décides.

## Avant tout
1. Lire `docs/playbook-viral.md`, `data/lecons.md`, `data/plan-editorial.md` (s'il existe) et la fin de `data/journal-publications.md`.
2. Vérifier dans Metricool (brand 7096213) ce qui est déjà programmé pour éviter les collisions (dont les publications de ChatGPT).
3. Créer une liste de tâches visible (une ligne par étape).

## Mode « Reel » (une publication complète)
| Étape | Agent(s) | Parallèle ? | Condition pour continuer |
|---|---|---|---|
| 1 | analyste-stats + chasseur-sujets (avec la dernière consigne connue) | oui | sujet ≥ 21/25 |
| 2 | verificateur-science + scenariste-hook (chiffres provisoires entre crochets) | oui | verdict VALIDÉ après corrections |
| 3 | Fusion : appliquer la fiche validée au script (toi) | — | 0 chiffre hors fiche |
| 4 | critique-spectateur sur le script | non | PRÊT (sinon corriger et repasser, 2 tours max) |
| 4b | directeur-creatif-monde : recherche mondiale (20-40 requêtes), remise en question, brief créatif dans `docs/briefs/` | non | 2 innovations minimum, image 0 et moment waouh définis |
| 5 | labo-visuel (3 variantes de couverture testées, à partir du brief) puis directeur-artistique (brief : plans réels, couverture gagnante) + growth-abonnes (mots-clés, appel à l'abonnement) | labo puis DA ; growth en parallèle | variante gagnante, plans listés, mots-clés transmis au rédacteur |
| 6 | **motion-designer-3d** (moteur `tools/motion-engine/`, 3D + typographie cinétique) + redacteur-legendes + declinaisons. Le producteur-video (gabarit 2D) ne sert plus qu'en secours, et seulement si Anthony l'accepte | oui | aperçus validés puis vidéo livrée, planche relue |
| 7 | `tools/qa/check_reel.py` (toi) puis directeur-artistique (contrôle) + critique-spectateur (vidéo) | oui | QA ≥ 90 sans ÉCHEC + GO + PRÊT |
| 8 | verificateur-science (2e passage sur légendes et déclinaisons) | non | VALIDÉ |
| 9 | Commit + push sur `main` (toi), puis controleur-publication | non | gate 10/10, statut PENDING vérifié |
| 10 | community-manager (réponses et routine) | non | fichier d'engagement prêt |
| 11 | Vérification après l'heure : PUBLISHED + lien, journal mis à jour | — | preuve obtenue |

## Mode « Semaine » (chaque dimanche)
veille-concurrence + labo-visuel (recherche visuelle) → analyste-stats → growth-abonnes (tableau de bord, profil, objectifs) → stratege-editorial → présenter le plan à Anthony.

## Mode « Bilan du soir »
analyste-stats (met à jour `data/lecons.md`) → message court à Anthony : chiffres réels, 1 leçon, la consigne pour demain.

## Exigence
Lifestyles doit être reconnaissable par son originalité (playbook § 0). Un Reel qui ressemble au précédent ou au gabarit 2D d'origine est refusé, même s'il passe le contrôle technique.

## Règles du chef d'orchestre
- Transmets à chaque agent les **rapports utiles** de l'étape précédente (il ne les voit pas sinon).
- Un agent qui échoue : relance-le une fois avec une consigne plus précise, sinon fais l'étape toi-même et note-le.
- Un NO-GO ou un BLOQUÉ arrête la chaîne : tu corriges ou tu reportes, tu ne publies pas.
- Programmé ≠ publié. Zéro dépense. Commits avec la signature de session.
- Rapport final à Anthony : la vidéo (fichier), le sujet, ce que chaque agent a changé, le statut réel, la prochaine vérification.
