from classes import Relation

a = [1, 2, 3]
r = [
    [1,2],
    [2,3]
]

R = Relation('R', a, r)

# print(R.transitive)

# print(R.symmetrical)
# print(R.reflective)

print(R.report())