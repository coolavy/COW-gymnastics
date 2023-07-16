import sys

sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')
# what is K --- number of exams .......x
# what is N --- number of students ......

K, N = [int(y) for y in input().split()]
print (K)
print (N)

answer = 0

all_values = []
for x in range(K):
	all_values.append([int(x) for x in input().split()])
print(all_values)

# student_rank_map = {}
# for i in range(K):
#   print(" Marking period number "+str(i))
#   for j in range(N):
#     student_rank_map = {i:all_values[i][j]}
#     student_rank_base = {i:all_values[i][0]}
#     print(student_rank_map)
#     print("______________+__)_+")
#     print("")

for i in range(N):
  base = all_values[0][i]
  print(base)
  print("++++")
  for j in range(i + 1, N):
    print(base, j)