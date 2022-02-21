import threading
import time
from statistics import mean, median
import requests

rbc_url = 'https://www.dav-rbc.de/072/185829.php'
PARALLEL_REQUESTS = 5
RUNS = 5

_c1, _c = 6, 21

print(f'{"Run".ljust(_c1)} | {"T to Headers".ljust(_c+1)} | {"T to complete Request".ljust(_c+2)}')
print(f'{"-"* (_c1 + 1)}+{"-"* (_c + 3)}+{"-" * (_c + 2)}')
t1s, t2s = [], []
for run in range(1, RUNS+1):
    # run all PARALLEL_REQUESTS except one in a background thread to simulate multiple users requesting the site
    for p in range(PARALLEL_REQUESTS - 1):
        threading.Thread(target=lambda: requests.get(rbc_url), daemon=True)
    # use the only other request to measure time
    start = time.time()
    t1 = requests.get(rbc_url).elapsed.total_seconds()
    t2 = time.time() - start
    print(f'{str(run).rjust(_c1)} | {str(round(t1, 3)).rjust(_c)}s | {str(round(t2, 3)).rjust(_c)}s')
    t1s.append(t1)
    t2s.append(t2)

if RUNS > 1:
    print(f'{"-"* (_c1 + 1)}+{"-"* (_c + 3)}+{"-" * (_c + 2)}')
    print(f'{"MIN".rjust(_c1)} | {str(round(min(t1s), 3)).rjust(_c)}s | {str(round(min(t2s), 3)).rjust(_c)}s')
    print(f'{"MEDIAN".rjust(_c1)} | {str(round(median(t1s), 3)).rjust(_c)}s | {str(round(median(t2s), 3)).rjust(_c)}s')
    print(f'{"AVG".rjust(_c1)} | {str(round(mean(t1s), 3)).rjust(_c)}s | {str(round(mean(t2s), 3)).rjust(_c)}s')
    print(f'{"MAX".rjust(_c1)} | {str(round(max(t1s), 3)).rjust(_c)}s | {str(round(max(t2s), 3)).rjust(_c)}s')

print("\nDanke")
