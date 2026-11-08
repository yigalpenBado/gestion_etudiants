from dataclasses import dataclass
from datetime import date


@dataclass
class Etudiant:
    """Représente un étudiant."""
    matricule: str
    nom: str
    prenom: str
    date_naissance: date
    filiere: str


def afficher_etudiant(etudiant: Etudiant) -> None:
    """Affiche les informations d'un étudiant."""
    print("=" * 40)
    print(f"Nom               : {etudiant.nom}")
    print("=" * 40)


if __name__ == "__main__":
    etudiant = Etudiant(
        matricule="ESMT2026001",
        nom="OUEDRAOGO",
        prenom="Abdoulaye",
        date_naissance=date(2000, 1, 15),
        filiere="Génie Logiciel",
    )
    afficher_etudiant(etudiant)
