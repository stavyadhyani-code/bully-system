from collections import defaultdict

class BullyGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_relationship(self, bully, victim):
        self.graph[bully].append(victim)

    def display_graph(self):
        for bully, victims in self.graph.items():
            print(f"{bully} → {', '.join(victims)}")

    def get_victims(self, bully):
        return self.graph.get(bully, [])

    def find_conflict_patterns(self):
        print("\nConflict patterns:")
        for bully, victims in self.graph.items():
            if len(victims) > 1:
                print(f"{bully} has targeted multiple victims: {', '.join(victims)}")
