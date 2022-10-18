import time


class BPMCounter:
    """
    BPM = 1 min / beat duration
    """

    durations = []

    def count(self, duration):
        self.durations.append(duration)
        return duration

    def average_array(self, durations):
        if not durations or type(durations) != list or type(durations[0]) != float:
            raise TypeError
        return sum(durations) / len(durations)

    def reset(self):
        self.durations = []

    def get_bpm(self):
        bpm = 60 / self.average_array(self.durations)
        return bpm


def main():
    bpm_counter = BPMCounter()
    print("Hit enter in time with the beat to find bpm")
    while True:
        start = time.perf_counter()
        input()
        end = time.perf_counter()
        bpm_counter.count(end - start)
        if len(bpm_counter.durations) > 5:
            bpm_counter.durations.pop(0)
        print(bpm_counter.get_bpm())


if __name__ == "__main__":
    main()
