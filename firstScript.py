from slmpy import ModularityOptimzer

edges = [
         [0, 1],
         [0, 2],
         [0, 3],
         [1, 2],
         [1, 3],
         [2, 3],
         [3, 4],
         [4, 5],
         [4, 6],
         [5, 6],
         [7, 8],
        ]

mo = ModularityOptimzer(edges)
mo.n_iterations = 1
mo.fixed_nodes = [0, 4]  # This fixes nodes 0 and 4 to be in different communities
communities = mo(algorithm='smart_local_moving')

# Check answer
assert((communities == [0, 0, 0, 0, 1, 1, 1]).all())
