class Banker:

    def __init__(self):
        self.p = 5
        self.r = 3
        self.available = [3, 3, 2]
        self.MAX = [
            [7, 5, 3],
            [3, 2, 2],
            [9, 0, 2],
            [2, 2, 2],
            [4, 3, 3]
        ]
        self.ALLOCATION = [
            [0, 1, 0],
            [2, 0, 0],
            [3, 0, 2],
            [2, 1, 1],
            [0, 0, 2]
        ]

    @property
    def need(self):
        return [[self.MAX[i][j] - self.ALLOCATION[i][j] for j in range(len(self.ALLOCATION[0]))] for i in
                range(len(self.ALLOCATION))]

    def resource_less_than_or_equal(self, r1, r2):
        if len(r1) != len(r2):
            raise ValueError

        for idx in range(len(r1)):
            if r1[idx] > r2[idx]:
                return False
        return True

    def safety_check(self):
        sequence = []
        available = [r for r in self.available]
        finished = [False] * self.p

        while len(sequence) < self.p:
            found = False
            for i in range(self.p):
                if not finished[i] and self.resource_less_than_or_equal(self.need[i], available):
                    # Allocate resources
                    for j in range(self.r):
                        available[j] += self.ALLOCATION[i][j]
                    sequence.append(i)
                    finished[i] = True
                    found = True
            if not found:
                print("Unsafe state.")
                return (False, [])

        return f"System is in a safe state.\nSafe Sequence: {sequence}"

    def request_resources(self, process_number, request):
        ''' Start at process 0 '''
        if len(request) == self.r:
            needs = self.need
            if self.resource_less_than_or_equal(needs[process_number],
                                                self.available) and self.resource_less_than_or_equal(request, self.MAX[
                process_number]):
                for i, amount in enumerate(request):
                    self.available[i] -= amount
                    self.ALLOCATION[process_number][i] += amount
                output = self.safety_check()
                print(output)
                if not output[0]:
                    self.available[i] += amount
                    self.ALLOCATION[process_number][i] -= amount
                else:
                    return True
        return False
        
b = Banker()

def main():
    user_input = input("Banker's Algorithm Test Menu:\n1. Check for safe sequence\n2. User-defined resource request\n"
                       "3. Exit\nEnter your choice (1-3): ")
    while user_input != "3":
        if user_input == "1":
            print("Test case 1: Run safe test:\nExpected: System is in a safe state. Safe Sequence: [1, 3, 4, 0, 2]")
            print(b.safety_check())

        elif user_input == "2":
            user_process = input("Enter the process ID (0 to 4): ")
            user_request = input(f"Enter the resources request for process {user_process} (format: r1 r2 r3): ")
            request = list(map(int, user_request.split()))
            print(f"Process {user_process} requests resources {request}")
            print(f"request_resouces({user_process}, {request})")
            print("Output:")
            if b.request_resources(int(user_process), request):
                print("System is in a safe state.")
                print(f"Resources allocated to process {user_process}.")
            else:
                print("ERROR!\nError: Request would lead to an unsafe state.")
        # Continue until user inputs "3".
        user_input = input(
            "\nBanker's Algorithm Test Menu:\n1. Check for safe sequence\n2. User-defined resource request\n"
            "3. Exit\nEnter your choice (1-3): ")
    # Exit program.
    print("Thank you for using the banker's algorithm.")
main()
