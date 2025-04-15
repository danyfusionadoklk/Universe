import time
from simulation.entity import Entity

class Universe:
    def __init__(self, name, depth=1):
        self.name = name
        self.entities = []
        self.child_universe = None
        self.depth = depth

    def create_entity(self, entity_name):
        self.entities.append(Entity(entity_name))

    def simulate(self, steps=5):
        for step in range(steps):
            print(f"\n[{self.name}] Paso {step + 1}")
            for entity in self.entities:
                entity.act()
                if entity.conscious and not self.child_universe:
                    self.spawn_child_universe(entity.name)
            time.sleep(0.5)
            if self.child_universe:
                self.child_universe.simulate(steps=steps - 1)

    def spawn_child_universe(self, creator_name):
        child_name = f"{self.name} - Sim por {creator_name}"
        print(f"{creator_name} ha creado una sub-simulación: {child_name}")
        self.child_universe = Universe(child_name, self.depth + 1)
        self.child_universe.create_entity(f"Entidad de {creator_name}")
