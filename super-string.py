def levenshtein_distance(a, b):
    """Return the Levenshtein edit distance between two strings *a* and *b*."""
    if a == b:
        return 0
    if len(a) < len(b):
        a, b = b, a
    if not a:
        return len(b)
    previous_row = range(len(b) + 1)
    for i, column1 in enumerate(a):
        current_row = [i + 1]
        for j, column2 in enumerate(b):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (column1 != column2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1] 

class SuperString(str):
    
    def __init__(self, string):
        self.index = 0
        self.string = string
        
    def distinct_len(self):
        return len(set(self))
    
    def levenstein_distance(self, string2):
        return levenshtein_distance(self.string, string2)
    
#     def __iter__(self):
#         print("start iteration")
#         self.index = 0
#         return self
    
#     def __next__(self):
#         try:
#             result = self.string[self.index]
#         except IndexError:
#             raise StopIteration
#         self.index += 1
#         return result
