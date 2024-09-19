from sortedcontainers import SortedDict
import heapq


class ReceiverPerformance:
    def __init__(self):
        self.games_points = {}  # Game ID to points mapping
        self.total_points = 0
        self.games_played = 0

    def record_game(self, game_id, points):
        if game_id in self.games_points:
            self.total_points -= self.games_points[game_id]
        self.games_points[game_id] = points
        self.total_points += points
        self.games_played = len(self.games_points)

    def clear_game(self, game_id):
        if game_id in self.games_points:
            self.total_points -= self.games_points[game_id]
            del self.games_points[game_id]
            self.games_played = len(self.games_points)

    def get_average(self):
        return self.total_points / self.games_played if self.games_played else 0


class PerformanceTracker:
    def __init__(self):
        self.receivers = SortedDict()
        self.performance_heap = []

    def record(self, game_id, jersey_number, points):
        receiver = self.receivers.setdefault(jersey_number, ReceiverPerformance())
        receiver.record_game(game_id, points)
        heapq.heappush(self.performance_heap, (-receiver.get_average(), jersey_number))

    def clear(self, game_id, jersey_number):
        if jersey_number in self.receivers:
            receiver = self.receivers[jersey_number]
            receiver.clear_game(game_id)
            self.rebuild_heap()

    def rebuild_heap(self):
        self.performance_heap = []
        for jersey_number, receiver in self.receivers.items():
            heapq.heappush(self.performance_heap, (-receiver.get_average(), jersey_number))

    def ranked_receiver(self, k):
        temp_heap = self.performance_heap[:]
        top_k = []
        while k > 0 and temp_heap:
            top_k.append(heapq.heappop(temp_heap))
            k -= 1
        return top_k[-1][1] if top_k else None


# Example usage:
tracker = PerformanceTracker()
tracker.record(1, 10, 100)  # Game 1, Jersey 10, 100 points
tracker.record(2, 10, 150)  # Game 2, Jersey 10, 150 points
print(tracker.ranked_receiver(1))  # Get the top receiver
