import time
import math
from datetime import datetime
import partlycloudy as cloud

from constants import DEVICE_ID
from constants import ACCESS_TOKEN

def get_date_time():
    pass

def main():
    ''' Write something here. '''
    
    # Initialize variables.
    current_temp = []
    ref_date = datetime.now().date()
    ref_time = datetime.now().time()
    bit = cloud.Bit(ACCESS_TOKEN, DEVICE_ID)
    
    # Oper file for logging.
    f=open('temperature_log.csv', 'w')

    # Open stream and begin logging.
    for t in bit.stream():
        if datetime.now() == ref_time:
            current_temp.append(t)
        else:
            
            # Write output to file.
            if len(current_temp) > 0:
                one_line = time.strftime("%c") + ',' + str(float(len(current_temp))) + ',' + str(min(current_temp)) + ',' + str(max(current_temp)) + ',' + str(math.fsum(current_temp) / float(len(current_temp)))
                print one_line
                f.write(one_line)
                f.flush()
            
            #
            current_temp = []
            current_temp.append(t)
            ref_time = datetime.now()
        
if __name__ == '__main__':
    main()