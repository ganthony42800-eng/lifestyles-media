# Équipe d'agents Lifestyles — v4 (17/10/2026)

15 agents spécialisés + 1 chef d'orchestre (`.claude/skills/lifestyles-production/SKILL.md`). Tous lisent d'abord `docs/playbook-viral.md` et `data/lecons.md`.

## Production
| # | Agent | Rôle | Livre |
|---|---|---|---|
| 1 | analyste-stats | Chiffres → décisions, ratios partages/enregistrements/abonnements | Consigne de la prochaine publication + `data/lecons.md` |
| 2 | chasseur-sujets | Sujets contre-intuitifs, personnels, vérifiables, envoyables | 6 idées notées /25 |
| 3 | verificateur-science | Source primaire, contre-vérification, accroche exacte | Fiche validée |
| 4 | scenariste-hook | 3 accroches notées, script à la seconde, plans réels | Script + épisode 2 |
| 5 | directeur-artistique | Brief réel + néon, contrôle image par image | GO / NO-GO |
| 6 | producteur-video | MP4 réel + néon, audio original | `reels/…mp4` |
| 7 | redacteur-legendes | Légendes, commentaire épinglé, story de relance | Blocs prêts |
| 8 | controleur-publication | Gate 10 points, programmation, preuve PUBLISHED | Statut + journal |

## Qualité et croissance
| # | Agent | Rôle | Livre |
|---|---|---|---|
| 9 | critique-spectateur | Crash test par 5 spectateurs types, prédiction de décrochage | PRÊT / À RETRAVAILLER |
| 10 | veille-concurrence | Principes des meilleurs comptes, sans copier | `docs/veille.md` |
| 11 | stratege-editorial | Plan 14 jours, séries, cadence, A/B | `data/plan-editorial.md` |
| 12 | declinaisons | Carrousel 4:5, stories 9:16, version TikTok | `posts/`, `stories/` |
| 13 | community-manager | Réponses types, routine 15 min, collaborations | `data/engagement/` |
| 14 | labo-visuel | Recherche visuelle, 3 variantes de couverture mesurées, amélioration du gabarit | Variante gagnante + `docs/style-visuel.md` |
| 15 | growth-abonnes | Abonnés, likes, vues : profil, mots-clés, Reels d'essai, collaborations, objectifs | Tableau de bord + 5 actions |

## Outil de contrôle
`tools/qa/check_reel.py` : score /100, GO / NO-GO automatique.

## Modes
- **Reel** : 1+2 → 3+4 → fusion → 9 → 14 → 5+15 → 6+7+12 → QA + 5+9 → 3 → 8 → 13 → vérification.
- **Semaine** (dimanche) : 10+14 → 1 → 15 → 11.
- **Bilan du soir** : 1.

## Utilisation
Dans une session Claude qui a ce dépôt : « Lance l'équipe Lifestyles » (mode Reel), « Plan de la semaine », « Bilan du soir ». ChatGPT peut lire les mêmes fiches sur GitHub.

## Fichiers partagés
`docs/playbook-viral.md` · `docs/series.md` · `docs/veille.md` · `data/lecons.md` · `data/journal-publications.md` · `data/plan-editorial.md` · `assets/broll/`
