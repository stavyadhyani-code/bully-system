class RepeatOffenders:
    def __init__(self):
        self.offender_count = {}

    def record_offense(self, bully_name):
        self.offender_count[bully_name] = self.offender_count.get(bully_name, 0) + 1

    def get_offense_count(self, bully_name):
        return self.offender_count.get(bully_name, 0)

    def get_repeat_offenders(self):
        return {k: v for k, v in self.offender_count.items() if v > 1}

    def display_all(self):
        for bully, count in self.offender_count.items():
            print(f"{bully}: {count} complaints")
