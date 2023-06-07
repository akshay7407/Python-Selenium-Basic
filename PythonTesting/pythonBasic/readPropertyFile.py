
from PythonTesting.utilities.config import *


addBookUrl = getConfig()['API']['endpoint']
sqlPAss = getConfig()['SQL']['password']
dataBase = getConfig()['SQL']['database']
print(addBookUrl)
print(sqlPAss)
print(dataBase)