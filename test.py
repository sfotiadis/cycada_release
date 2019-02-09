import time
import sys 
import logging

logging.basicConfig(format='%(message)s', level=logging.INFO)
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything

print ('before wait', file=sys.stderr)
time.sleep(5)
print ('after 5 sec', file=sys.stderr)
# Wait for 5 seconds
time.sleep(20)
