from dataclasses import dataclass, asdict, replace
import json

@dataclass(frozen=True, slots=True, order=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    def __post_init__(self):
        if not (0 <= self.note <= 10):
            raise ValueError(f"Note invalide : {self.note}, doit être entre 0 et 10")

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def est_classique(self):
        return self.annee < 2000

    @staticmethod
    def from_json(json_str: str):
        data = json.loads(json_str)
        return Film(**data)



