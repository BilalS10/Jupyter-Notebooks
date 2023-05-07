import sys
import json
dict_of_arguments = json.loads(sys.argv[1])
print(dict_of_arguments['altergoProgramTaskId'])
print(dict_of_arguments['altergoUserApiKey'])
print(dict_of_arguments['altergoFactoryApi'])
print(dict_of_arguments['altergoIotApi'])
