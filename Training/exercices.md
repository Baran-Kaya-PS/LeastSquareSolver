```markdown
# Programme d’entraînement Python & NumPy (80 exercices)

Chaque exercice doit être codé en Python (et NumPy quand indiqué) ; l’objectif est de maîtriser toutes les briques pour implémenter ton solveur moindres carrés (Normal Eq + QR) « from-scratch ».

---

## Section A – Fondamentaux NumPy (10 exos)

1. **Créer et inspecter un array**  
   - **Mission** : Crée un vecteur `v = [0, 1, …, 119]`, reshape-le en matrice 12×10, affiche `shape`, `dtype`, `size`.  
   - **But** : Prise en main de la création et inspection d’`ndarray`.

2. **Matrices constantes**  
   - **Mission** : Construis via NumPy `zeros((8,8))`, `ones((5,3))`, `full((4,6), 7)`, puis affiche `itemsize`.  
   - **But** : Paramètres de construction et compréhension du stockage.

3. **Échelon inférieur sans diag**  
   - **Mission** : Génère la matrice échelon 5×5 (1 sur et en dessous de la diagonal, 0 ailleurs) sans `np.tril`.  
   - **But** : Indexation par masque et logique de matrice.

4. **Indexation simple**  
   - **Mission** : Depuis une matrice 6×6, extrais la 4ᵉ ligne et les 2 colonnes centrales.  
   - **But** : Maîtriser le slicing 2D basique.

5. **Masque booléen**  
   - **Mission** : Crée un vecteur aléatoire de taille 50 et filtre toutes les valeurs > moyenne.  
   - **But** : Masques booléens et filtrage.

6. **Concaténation**  
   - **Mission** : Concatène deux matrices 3×3 verticalement et horizontalement (`vstack`, `hstack`).  
   - **But** : Combiner des arrays de dimensions compatibles.

7. **Pretty print**  
   - **Mission** : Écris `pretty_print(A)` qui aligne joliment les colonnes d’une matrice interactive.  
   - **But** : Boucles Python et formatage de chaînes.

8. **Vectorisation vs boucle**  
   - **Mission** : Additionne deux matrices 500×500 par double boucle Python, puis avec `A + B`; compare temps.  
   - **But** : Notion de vectorisation et performance.

9. **I/O binaire**  
   - **Mission** : Sauve un array aléatoire en `.npy`, recharge-le, vérifie l’égalité bit-à-bit.  
   - **But** : Sauvegarde/chargement rapide et fiable.

10. **Transpose manuelle**  
    - **Mission** : Écris `transpose_list(M)` en pur Python (list of lists), compare à `A.T`.  
    - **But** : Comprendre la transposition et les vues vs copies.

---

## Section B – Indexation, broadcasting & statistiques (10 exos)

11. **Broadcast ligne**  
    - **Mission** : Ajoute un vecteur ligne `v` à chaque ligne d’une matrice 7×3 sans boucle.  
    - **But** : Règles de broadcasting horizontal.

12. **Broadcast colonne**  
    - **Mission** : Ajoute un vecteur colonne `w` à chaque colonne d’une matrice 7×3 sans boucle (`[:,None]`).  
    - **But** : Broadcasting vertical.

13. **Standardisation (z-score)**  
    - **Mission** : Calcule et applique `(x - μ)/σ` pour chaque colonne d’`A`.  
    - **But** : Statistiques élémentaires et normalisation.

14. **Masque complexe**  
    - **Mission** : Sur un vecteur `x`, crée le masque `(x > 0.2) & (x < 0.8) | (x < 0)`.  
    - **But** : Combiner opérations logiques.

15. **Gestion de NaN**  
    - **Mission** : Compte les `NaN` dans une matrice, remplace-les par la moyenne de leur colonne.  
    - **But** : Nettoyage de données.

16. **Histogramme 2D**  
    - **Mission** : Génère 100 000 points uniformes `(x,y)`, construit un histogramme 2D (ex. `np.histogram2d`).  
    - **But** : Manipuler de grands ensembles et visualiser répartitions.

17. **Produit scalaire manuel**  
    - **Mission** : Implemente `dot_py(u,v)` en boucle, compare résultat et temps à `np.dot`.  
    - **But** : Fondamentaux du produit scalaire.

18. **Normes multiples**  
    - **Mission** : Calcule L1, L2, et norme infinie d’un vecteur (boucle vs `np.linalg.norm`).  
    - **But** : Différents types de norme.

19. **Produit extérieur**  
    - **Mission** : Code `outer_py(u,v)` en double boucle, compare à `np.outer`.  
    - **But** : Produit extérieur et tailles d’array.

20. **Matrice Toeplitz**  
    - **Mission** : Génère une matrice Toeplitz 6×6 (valeurs dépendant de l’écart d’indices) sans SciPy.  
    - **But** : Indexation avancée.

---

## Section C – Opérations matricielles de base (10 exos)

21. **Multiplication naive**  
    - **Mission** : Code `matmul_loops(A,B)` (3 boucles), teste sur 50×50.  
    - **But** : Complexité O(n³) et implémentation brute.

22. **Optimisation légère**  
    - **Mission** : Réécris `matmul` en 2 boucles + list-comprehension, mesure l’amélioration.  
    - **But** : Micro-optimisation Python.

23. **Mat-vec en pur Python**  
    - **Mission** : Implemente `matvec_py(A,x)` sur listes, compare à `A @ x`.  
    - **But** : Fondamentaux du solveur.

24. **Assembler AᵀA**  
    - **Mission** : Calcule manuellement `AtA` et `Atb` via boucles, compare à NumPy.  
    - **But** : Préparation des équations normales.

25. **Symétrie d’AtA**  
    - **Mission** : Vérifie que `AtA.T` ≈ `AtA` (tolérance 1e-10).  
    - **But** : Propriété théorique.

26. **Élimination de Gauss (sans pivot)**  
    - **Mission** : Code `gauss_no_pivot(A,b)` pour un système 4×4.  
    - **But** : Algorithme de base des équations linéaires.

27. **Gauss avec pivot partiel**  
    - **Mission** : Ajoute pivot partiel à ton GE (choix de la ligne max).  
    - **But** : Améliorer la stabilité numérique.

28. **Validation GE**  
    - **Mission** : Teste ton GE vs `np.linalg.solve` sur 10 systèmes aléatoires, compare erreur relative.  
    - **But** : Assurance qualité.

29. **Profilage GE**  
    - **Mission** : Mesure temps de `gauss_pivot` vs `np.linalg.solve` pour n=200.  
    - **But** : Benchmark.

30. **Génération de jeu LS**  
    - **Mission** : Génère points bruités \(y = 3x+1+ϵ\) (n=100) et forme `A` (100×2), `b`.  
    - **But** : Créer un dataset de test.

---

## Section D – Préparation du solveur Least Squares (10 exos)

31. **solve_normal_eq**  
    - **Mission** : Implemente `solve_normal_eq(A,b)` via `AtA`, `Atb` et ton GE.  
    - **But** : Premier solveur OLS.

32. **Tracer droite**  
    - **Mission** : Trace les points et la droite de régression obtenue.  
    - **But** : Visualisation des résultats.

33. **Calculer résidu**  
    - **Mission** : Calcule \(\|Ax - b\|\) pour ta solution.  
    - **But** : Mesurer l’erreur.

34. **Condition number**  
    - **Mission** : Implemente `cond_number(A)` via `np.linalg.svd` (ou power-method simple).  
    - **But** : Indicateur de stabilité.

35. **Effet du bruit**  
    - **Mission** : Étudie l’impact d’un bruit croissant sur résidu et condition number.  
    - **But** : Analyse numérique.

36. **Weighted LS**  
    - **Mission** : Ajoute support `W` diag(random), résous \((√W A)x ≈ √W b\).  
    - **But** : Extension pondérée.

37. **Comparer pondéré vs non**  
    - **Mission** : Compare solutions et résidus pondéré vs non.  
    - **But** : Interprétation.

38. **Persistance JSON**  
    - **Mission** : Sauve coefficients, résidu, κ(A) dans un fichier JSON.  
    - **But** : Pipeline résultat.

39. **I/O CSV custom**  
    - **Mission** : Écris ton propre parser CSV (module `csv`) pour charger A/b.  
    - **But** : I/O “from scratch”.

40. **Cache NPZ**  
    - **Mission** : Implémente cache/rechargement `.npz` après preprocessing.  
    - **But** : Accélérer itérations.

---

## Section E – Décomposition QR & variantes (15 exos)

41. **Gram–Schmidt classique**  
    - **Mission** : Code `gram_schmidt(A)` pour m×n (m>n).  
    - **But** : Orthonormalisation de base.

42. **Validation QᵀQ = I**  
    - **Mission** : Vérifie `Q.T @ Q ≈ I` à tolérance 1e-10.  
    - **But** : Contrôle orthogonalité.

43. **Back-substitution**  
    - **Mission** : Implemente `back_sub(R,y)` pour triangulaire sup.  
    - **But** : Résolution triangulaire.

44. **solve_qr**  
    - **Mission** : Combine GS + back-sub pour `solve_qr(A,b)`.  
    - **But** : Deuxième solveur OLS.

45. **Comparer Normal vs QR**  
    - **Mission** : Sur matrices bien/mal conditionnées, compare résidus.  
    - **But** : Empiricité de la stabilité.

46. **Modified GS (MGS)**  
    - **Mission** : Refactorise GS en version modifiée, teste perte d’orthogonalité.  
    - **But** : Réduire erreurs numériques.

47. **Householder QR**  
    - **Mission** : Implémente `householder_qr(A)` (m≥n).  
    - **But** : Méthode pro.

48. **Benchmark QR**  
    - **Mission** : Compare GS, MGS, Householder sur m=200,n=50 (temps & précision).  
    - **But** : Choix d’algorithme.

49. **Visualiser orthogonalité**  
    - **Mission** : Trace \(\|QᵀQ - I\|\) selon chaque méthode.  
    - **But** : Analyse stabilité.

50. **CLI — choix QR**  
    - **Mission** : Ajoute `--qr_type` (gs|mgs|house) dans ton CLI.  
    - **But** : Interface utilisateur flexible.

51. **Test unitaire paramétré**  
    - **Mission** : Écris un test pytest qui vérifie `Q@R ≈ A` pour plusieurs tailles.  
    - **But** : Assurance qualité.

52. **Opérations flottantes estimées**  
    - **Mission** : Estime le nombre d’opérations pour GS vs chrono.  
    - **But** : Complexité pratique.

53. **QR sans NumPy**  
    - **Mission** : Ré-implémente GS sur listes natives, compare perf.  
    - **But** : Compréhension bas niveau.

54. **Givens rotations (bonus)**  
    - **Mission** : Implémente QR par rotations de Givens.  
    - **But** : Algorithme alternatif.

55. **Householder vs Givens**  
    - **Mission** : Sur matrice quasi-singulière, compare précision.  
    - **But** : Étude cas limite.

---

## Section F – Pipeline & packaging (10 exos)

56. **DataManager OOP**  
    - **Mission** : Crée `DataManager` (load, split, normalize, cache).  
    - **But** : Abstraction des données.

57. **Argparse avancé**  
    - **Mission** : Gère `--csv`, `--method`, `--weights`, `--normalize`, `--save-db`.  
    - **But** : Ergonomie CLI.

58. **Export JSON & CSV**  
    - **Mission** : Ajoute option pour sortir résultats en CSV ou JSON.  
    - **But** : Flexibilité.

59. **Tests bout-en-bout**  
    - **Mission** : Écris un test E2E (charger CSV → solve → fichier de sortie).  
    - **But** : Validation complète.

60. **Profilage intégré**  
    - **Mission** : Ajoute `--profile` pour afficher top 3 fonctions lentes (`cProfile`).  
    - **But** : Diagnostic de perf.

61. **Packaging pip**  
    - **Mission** : Crée `setup.cfg` / `pyproject.toml` pour `pip install -e .`.  
    - **But** : Distribution basique.

62. **Standalone exe**  
    - **Mission** : Génère un exécutable avec `pyinstaller`, teste sur machine sans Python.  
    - **But** : Déploiement.

63. **Documentation auto**  
    - **Mission** : Code un script qui génère un README.md résumé des méthodes et tests.  
    - **But** : Génération de docs.

64. **Notebook récap**  
    - **Mission** : Crée un Jupyter Notebook qui illustre chaque solveur sur un exemple.  
    - **But** : Démos interactives.

65. **Historique SQLite**  
    - **Mission** : Stocke chaque exécution (méthode, timestamp, résidu) dans une DB SQLite.  
    - **But** : Persistance structurée.

---

## Section G – Extensions numériques (10 exos)

66. **Conjugate Gradient**  
    - **Mission** : Implémente CG pour résoudre \(A^T A x = A^T b\).  
    - **But** : Méthode itérative OLS.

67. **CG vs direct**  
    - **Mission** : Compare CG vs QR sur n=1 000 (matrice dense) et matrice sparse simulée.  
    - **But** : Choix d’algorithme.

68. **Matrices sparses DIY**  
    - **Mission** : Génère une matrice sparse sous forme liste de triplets `(i,j,val)`.  
    - **But** : Représentation sparse.

69. **Produit sparse × dense**  
    - **Mission** : Code le produit matrice-sparse × vecteur dense.  
    - **But** : Calculs sur structure sparse.

70. **Power method**  
    - **Mission** : Implémente power-method pour approximer λ_max de \(A^T A\).  
    - **But** : Valeurs propres itératives.

71. **Inverse power method**  
    - **Mission** : Ajoute inverse power-method pour λ_min, calcule κ≈√(λ_max/λ_min).  
    - **But** : Condition number sans SVD.

72. **TLS via SVD**  
    - **Mission** : Implémente `solve_tls(A,b)` en appelant `np.linalg.svd` puis extraction de v_min.  
    - **But** : Total Least Squares pratique.

73. **Comparaison OLS vs TLS**  
    - **Mission** : Sur jeu où A et b sont bruités, compare résidus OLS vs TLS.  
    - **But** : Application du papier TLS.

74. **Surface résidu 2×2**  
    - **Mission** : Pour A 2×2, trace surface de résidu TLS et OLS en variant bruit.  
    - **But** : Visualisation comparative.

75. **Résumé PDF automatique**  
    - **Mission** : Génère un petit PDF (Markdown → PDF) listant formules et résumés des méthodes.  
    - **But** : Documentation technique.

---

## Section H – Challenges finaux (5 exos)

76. **Ré-implémenter GE+QR sans NumPy**  
    - **Mission** : Code GE et QR « from scratch » sur listes natives, compare perf.  
    - **But** : Maîtrise algorithme bas-niveau.

77. **QR par blocs**  
    - **Mission** : Implémente QR block-wise (blocs 32×32).  
    - **But** : Optimisation cache.

78. **Parallélisation simple**  
    - **Mission** : Compare execution QR block vs standard en multi-thread (`concurrent.futures`).  
    - **But** : Parallélisme de tâches.

79. **Micro-benchmark multi-méthodes**  
    - **Mission** : Écris un script qui compare ensemble des méthodes (Normal, QR, CG, TLS) sur matrices de tailles variées.  
    - **But** : Tableau de bord performance vs précision.

80. **Rédaction d’un white-paper**  
    - **Mission** : Rédige 2 pages (Markdown) comparant GE, QR, CG, TLS (algorithmes, stabilité, perf).  
    - **But** : Synthèse et communication technique.

---
```
