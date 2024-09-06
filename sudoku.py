# Fonction utilitaire pour afficher la grille Sudoku
def print_grid(arr):
    # Parcourt chaque ligne
    for i in range(9):
        # Parcourt chaque colonne
        for j in range(9):
            # Affiche chaque élément suivi d'un espace
            print(arr[i][j], end=" "),
        # Passe à la ligne suivante après chaque ligne
        print()

# Trouve une case vide (non assignée) dans la grille
# Renvoie True si trouvé, sinon False
def find_empty_location(arr, l):
    # Parcourt chaque ligne
    for row in range(9):
        # Parcourt chaque colonne
        for col in range(9):
            # Si la case est vide (0)
            if (arr[row][col] == 0):
                # Enregistre les coordonnées de la case vide
                l[0] = row
                l[1] = col
                return True
    # Renvoie False si aucune case vide n'est trouvée
    return False

# Vérifie si un nombre est déjà utilisé dans une ligne donnée
def used_in_row(arr, row, num):
    # Parcourt les colonnes de la ligne
    for i in range(9):
        # Si le nombre est trouvé dans la ligne
        if (arr[row][i] == num):
            return True
    # Renvoie False si le nombre n'est pas dans la ligne
    return False

# Vérifie si un nombre est déjà utilisé dans une colonne donnée
def used_in_col(arr, col, num):
    # Parcourt les lignes de la colonne
    for i in range(9):
        # Si le nombre est trouvé dans la colonne
        if (arr[i][col] == num):
            return True
    # Renvoie False si le nombre n'est pas dans la colonne
    return False

# Vérifie si un nombre est déjà utilisé dans une boîte 3x3
def used_in_box(arr, row, col, num):
    # Parcourt les cases de la boîte 3x3
    for i in range(3):
        for j in range(3):
            # Si le nombre est trouvé dans la boîte
            if (arr[i + row][j + col] == num):
                return True
    # Renvoie False si le nombre n'est pas dans la boîte
    return False

# Vérifie si il est sûr d'assigner un nombre à une position donnée
def check_location_is_safe(arr, row, col, num):
    # Vérifie si le nombre n'est pas dans la ligne, colonne et boîte 3x3
    return (not used_in_row(arr, row, num) and
            (not used_in_col(arr, col, num) and
             (not used_in_box(arr, row - row % 3,
                              col - col % 3, num))))

# Fonction principale qui résout le Sudoku en utilisant le backtracking
def solve_sudoku(arr):
    # Liste pour stocker les coordonnées de la case vide
    l = [0, 0]

    # Si aucune case vide n'est trouvée, le Sudoku est résolu
    if (not find_empty_location(arr, l)):
        return True

    # Récupère les coordonnées de la case vide
    row = l[0]
    col = l[1]

    # Tente d'assigner un nombre de 1 à 9
    for num in range(1, 10):
        # Vérifie si le nombre peut être placé à la position donnée
        if (check_location_is_safe(arr, row, col, num)):

            # Assigne temporairement le nombre
            arr[row][col] = num

            # Appelle récursivement solve_sudoku
            if (solve_sudoku(arr)):
                return True

            # Si l'assignation échoue, réinitialise la case (backtracking)
            arr[row][col] = 0

    # Si aucun nombre ne convient, déclenche le backtracking
    return False

# Fonction principale pour tester la solution
if __name__ == "__main__":

    # Création d'une grille Sudoku 9x9 avec des valeurs initiales
    grid = [[0 for x in range(9)]for y in range(9)]

    # Assignation des valeurs à la grille (les 0 représentent des cases vides)
    grid = [[8, 0, 9, 2, 0, 1, 0, 7, 4],
            [1, 2, 3, 7, 5, 0, 0, 6, 9],
            [5, 0, 4, 8, 6, 9, 3, 1, 0],
            [7, 4, 0, 1, 6, 9, 2, 0, 8],
            [0, 1, 0, 0, 8, 0, 7, 9, 0],
            [0, 0, 0, 0, 0, 7, 0, 0, 1],
            [0, 0, 0, 6, 7, 8, 9, 0, 3],
            [9, 0, 7, 3, 4, 2, 0, 5, 6],
            [2, 3, 0, 0, 0, 0, 4, 8, 7]]

    # Si le Sudoku est résolu, affiche la grille
    if (solve_sudoku(grid)):
        print_grid(grid)
    else:
        print("No solution exists")
