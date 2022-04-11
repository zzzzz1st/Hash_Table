if __name__ == '__main__':
    from linearHash import *
    from chainedHash import *
    from random import randint
    import time

    LOW = 10
    STANDARD = 100
    HIGH = 10000

    lhs = LinearHashTable(STANDARD)
    chs = ChainedHashTable(STANDARD)
    lhh = LinearHashTable(HIGH)
    chh = ChainedHashTable(HIGH)
    # INIZIO ESPERIMENTO HASH LINEARE
    linearBeforeStandardInsert = time.perf_counter_ns()
    for i in range(STANDARD):
        number = randint(0, STANDARD)
        lhs.insert(number, i)
    linearAfterStandardInsert = time.perf_counter_ns()
    linearBeforeBigInsert = time.perf_counter_ns()
    for i in range(STANDARD):
        number = randint(0, HIGH)
        lhh.insert(number, i)
    linearAfterBigInsert = time.perf_counter_ns()
number = randint(0, HIGH)
linearBeforeStandardSearch = time.perf_counter_ns()
val = lhs.get(number)
linearAfterStandardSearch = time.perf_counter_ns()
linearBeforeBigSearch = time.perf_counter_ns()
val2 = lhh.get(number)
linearAfterBigSearch = time.perf_counter_ns()
# FINE ESPERIMENTO HASH LINEARE
# INIZIO ESPERIMENTO HASH CONCATENATO
chainedBeforeStandardInsert = time.perf_counter_ns()
for i in range(STANDARD):
    number = randint(0, STANDARD)
    chs.insert(number, i)
chainedAfterStandardInsert = time.perf_counter_ns()
chainedBeforeBigInsert = time.perf_counter_ns()
for i in range(STANDARD):
    number = randint(0, HIGH)
    chh.insert(number, i)
chainedAfterBigInsert = time.perf_counter_ns()
number = randint(0, HIGH)
chainedBeforeStandardSearch = time.perf_counter_ns()
val = chs.get(number)
chainedAfterStandardSearch = time.perf_counter_ns()
chainedBeforeBigSearch = time.perf_counter_ns()
val2 = chh.get(number)
chainedAfterBigSearch = time.perf_counter_ns()
# FINE ESPERIMENTO HASH CONCATENATO
print(f'Linear Hash Table Standard con fattore di carico : {str(lhs.loadF())} '
      f'e n. collisioni : {str(lhs.collisions())}')
print(f'tempo di inserimento : {str(linearAfterStandardInsert - linearBeforeStandardInsert)}')
print(f'tempo di ricerca : {str(linearAfterStandardSearch - linearBeforeStandardSearch)}')
print(f'Linear Hash Table Grande con fattore di carico : {str(lhh.loadF())} '
      f'e n. collisioni : {str(lhh.collisions())}')
print(f'tempo di inserimento : {str(linearAfterBigInsert - linearBeforeBigInsert)}')
print(f'tempo di ricerca : {str(linearAfterBigSearch - linearBeforeBigSearch)}')
print("-----------------------------------------------------------------------")
print(f'Chained Hash Table Standard con fattore di carico : {str(chs.loadF())} '
      f'e n. collisioni : {str(chs.collisions())} ')
print(f'tempo di inserimento : {str(chainedAfterStandardInsert - chainedBeforeStandardInsert)}')
print(f'tempo di ricerca : {str(chainedAfterStandardSearch - chainedBeforeStandardSearch)}')
print(f'Chained Hash Table Grande con fattore di carico : {str(chh.loadF())} '
      f'e n. collisioni : {str(chh.collisions())}')
print(f'tempo di inserimento : {str(chainedAfterBigInsert - chainedBeforeBigInsert)}')
print(f'tempo di ricerca : {str(chainedAfterBigSearch - chainedBeforeBigSearch)}')
# Esperimento 2
print("########################################################################")
linear_result_ins = []
chained_result_ins = []
linear_result_ric = []
chained_result_ric = []
lhs_2 = LinearHashTable(LOW)
chs_2 = ChainedHashTable(LOW)
for i in range(STANDARD):
    loadF = lhs_2.loadF()
    linearBeforeStandardInsert = time.perf_counter_ns()
    lhs_2.insert(i, i)
    linearAfterStandardInsert = time.perf_counter_ns()
    linearBeforeStandardSearch = time.perf_counter_ns()
    val = lhs_2.get(i)
    linearAfterStandardSearch = time.perf_counter_ns()
    linear_result_ins.append((loadF, linearAfterStandardInsert - linearBeforeStandardInsert))
    linear_result_ric.append((loadF, linearAfterStandardSearch - linearBeforeStandardSearch))

for i in range(STANDARD):
    loadF = chs_2.loadF()
    chainedBeforeStandardInsert = time.perf_counter_ns()
    chs_2.insert(i, i)
    chainedAfterStandardInsert = time.perf_counter_ns()
    chainedBeforeStandardSearch = time.perf_counter_ns()
    val = chs_2.get(i)
    chainedAfterStandardSearch = time.perf_counter_ns()
    chained_result_ins.append((loadF, chainedAfterStandardInsert - chainedBeforeStandardInsert))
    chained_result_ric.append((loadF, chainedAfterStandardSearch - chainedBeforeStandardSearch))

print(linear_result_ins)
print(linear_result_ric)
print(chained_result_ins)
print(chained_result_ric)
