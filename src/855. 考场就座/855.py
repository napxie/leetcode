import bisect


class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = []


    def seat(self) -> int:
        if not self.students:
            student = 0
        else:
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    d = (s - prev) // 2
                    if d > dist:
                        dist, student = d, prev + d
            d = self.n - 1 - self.students[-1]
            if d > dist:
                student = self.n -1
        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)
        

    # def seat(self):
    #     # Let's determine student, the position of the next
    #     # student to sit down.
    #     if not self.students:
    #         student = 0
    #     else:
    #         # Tenatively, dist is the distance to the closest student,
    #         # which is achieved by sitting in the position 'student'.
    #         # We start by considering the left-most seat.
    #         dist, student = self.students[0], 0
    #         for i, s in enumerate(self.students):
    #             if i:
    #                 prev = self.students[i-1]
    #                 # For each pair of adjacent students in positions (prev, s),
    #                 # d is the distance to the closest student;
    #                 # achieved at position prev + d.
    #                 d = (s - prev) // 2
    #                 if d > dist:
    #                     dist, student = d, prev + d

    #         # Considering the right-most seat.
    #         d = self.N - 1 - self.students[-1]
    #         if d > dist:
    #             student = self.N - 1

    #     # Add the student to our sorted list of positions.
    #     bisect.insort(self.students, student)
    #     return student

    # def leave(self, p):
    #     self.students.remove(p)
        
if __name__ == "__main__":
    n = 10
    obj = ExamRoom(n)
    obj.seat()
    obj.seat()
    obj.seat()
    obj.seat()
    obj.seat()
    obj.leave(4)
    obj.seat()
    print(obj.students)

