from simulation.universe import Universe

def run_simulation():
    universe = Universe("Universo Principal")
    universe.create_entity("Entidad Inicial")
    universe.simulate()

if __name__ == "__main__":
    run_simulation()