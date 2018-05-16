import csv
import cProfile, pstats, io


import area_1
from input_areas import input_areas

# first atempt
pr = cProfile.Profile()
pr.enable()
al = area_1.AreaList()
al.batch_create(input_areas)
print(al.query(1.0, 1.0))
pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
