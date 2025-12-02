from dataclasses import dataclass, asdict, replace
import json

@dataclass(frozen=True, slots=True, order=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def promo(self, prix_reduit: float):
        return replace(self, prix=prix_reduit)

    @staticmethod
    def from_json(json_str: str):
        data = json.loads(json_str)
        return Livre(**data)





livre1 = Livre("1984", "George Orwell", 1949, 9.90)
print("Livre original :", livre1.to_json())

livre2 = livre1.promo(7.90)
print("Livre avec promo :", livre2.to_json())

livre3 = Livre("Animal Farm", "George Orwell", 1945, 5.50)
livres = [livre1, livre2, livre3]
livres.sort()
print("Livres triés par prix :")
for l in livres:
    print(l.to_json())

json_str = '{"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "annee": 1943, "prix": 12.5}'
livre4 = Livre.from_json(json_str)
print("Livre reconstitué :", livre4.to_json())
