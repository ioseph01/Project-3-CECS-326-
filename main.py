
class Banker:
    
    def __init__(self):
        self.p = 5
        self.r = 3
        self.available = [3,3,2]
        self.MAX = [
            [7,5,3],
            [3,2,2],
            [9,0,2],
            [2,2,2],
            [4,3,3]
        ]
        self.ALLOCATION = [
            [0,1,0],
            [2,0,0],
            [3,0,2],
            [2,1,1],
            [0,0,2]    
        ]
        
    @property
    def NEED(self):
        return [[self.MAX[i][j] - self.ALLOCATION[i][j] for j in range(len(self.ALLOCATION[0]))] for i in range(len(self.ALLOCATION))]

    def resource_less_than_or_equal(self, r1, r2):
        if len(r1) != len(r2):
            raise ValueError
            
        for idx in range(len(r1)):
            if r1[idx] > r2[idx]:
                return False
        return True

    def safety_check(self):
        """ Return (is_safe: bool, safe_sequence: list) """
        sequence = []
        available = [r for r in self.available]
        finished = set()
    
        for _ in range(self.p):
            for process_idx, need in enumerate(self.NEED):
                if process_idx in finished:
                    continue
    
                if self.resource_less_than_or_equal(need, available):
                    for idx, alloc in enumerate(self.ALLOCATION[process_idx]):
                        available[idx] += alloc
                    sequence.append(process_idx)
                    finished.add(process_idx)
                    break
    
            else:
                print("Unsafe state.")
                return (False, [])
    
        return (True, sequence)

        
    
    def request_resources(self, process_number, request):
        ''' Start at process 0 ''' 
        if len(request) == self.r:
            need = self.NEED
            if self.resource_less_than_or_equal(need[process_number], self.available) and self.resource_less_than_or_equal(request, self.MAX[process_number]):
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

print("Test case 1: Run safe test:\n Expected: System is in a safe state. Safe Sequence: [1, 3, 4, 0, 2]")
print(b.safety_check())

print("-----------------------------------\nTest case 2: # Process 1 requests resources [1, 0, 2]")
request = [1, 0, 2]

print("Expected Output: System is in a safe state. Resources allocated to process 1.")
if b.request_resources(1, request):
    print("Resources allocated to process 1")
else:
    print("Request failed")
    
print("---------------------------------\nTest case 3: Process 4 requests resources [3, 3, 1]")
request = [3, 3, 1] # Process 4's resource request
print("Expected output: Error: Not enough resources available.")
if b.request_resources(4, request):
    print("Resources allocated to process 4")
else:
    print("Request failed to process 4")



