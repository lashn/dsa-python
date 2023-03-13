'''
The input of the problem is an array of tuples.
 The output of the problem is an array with the memory ids inside of cache memory.

 Tuple
 The time, in seconds, when the memory was accessed. | The id of the memory accessed.

 Time [INT] | Memory id [INT]
 1 | 2

 Rules:
 - Every memory hit adds priority +2.
 - Every second without access subtracts priority -1.
 - Every memory id with priority > 5 should be relocated to the cache memory.
 - Every memory id with priority < 3 should be removed to the cache memory.
 - Priority could not be negative.

 Example:

 Given an array of tuples:

 logs: [ (1,2), (2,4), (2,2), (3, 2) ]


 Iteration 1:

 Memory
 Id | Priority
 -------------
 2 | 0 + 2 = 2

 Iteration 2:

 Memory
 Id | Priority
 -------------
 2 | 2 + 2 = 4
 4 | 0 + 2 = 2

 Iteration 3:

 Memory
 Id | Priority
 -------------
 2 | 4 + 2 = 6
 4 | 2 - 1 = 1

 Memory cache
 Id | Priority
 -------------
 2 | 6

 Program output : [2]

'''