nSec = 52456

fullOurs = (nSec // 60 ** 2)
restSec = nSec - (fullOurs * 60 ** 2)

print(fullOurs, restSec)
