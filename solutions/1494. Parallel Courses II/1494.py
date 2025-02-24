class Solution:
  def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
    # dp[i] := min # Of semesters to take all courses in mask i.
    dp = [n] * (1 << n)
    # prereq[i] := bit mask of all dependencies of course i.
    prereq = [0] * n

    for prevCourse, nextCourse in relations:
      prereq[nextCourse - 1] |= 1 << prevCourse - 1

    dp[0] = 0  # No need time to finish 0 course.

    for i in range(1 << n):
      # Bit mask of all the courses can be taken.
      coursesCanBeTaken = 0
      # Can take course j if i contains all j's prerequisites.
      for j in range(n):
        if (i & prereq[j]) == prereq[j]:
          coursesCanBeTaken |= 1 << j
      # Don't take any course which is already taken.
      # (i represents set of courses that are already taken)
      coursesCanBeTaken &= ~i
      # Enumerate all bit subset of `coursesCanBeTaken`.
      s = coursesCanBeTaken
      while s:
        if bin(s).count('1') <= k:
          # Any combination of courses (if <= k) can be taken now.
          # i | s := combining courses taken with courses can be taken.
          dp[i | s] = min(dp[i | s], dp[i] + 1)
        s = (s - 1) & coursesCanBeTaken

    return dp[-1]
