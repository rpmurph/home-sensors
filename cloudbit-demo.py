from constants import DEVICE_ID         # replace this with your device id
from constants import ACCESS_TOKEN      # replace this with your access token

import partlycloudy as cloud
from datetime import datetime
from sys import argv, exit
from time import sleep

def get_date_time():
    ''' return the current date-time as a formatted string '''
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def parse_arguments(args):
    ''' return the current date-time as a formatted string '''

    #
    if len(args) == 1:
        return 5, False

    #
    elif len(args) == 2:
        return float(args[1]), False

    #
    elif len(args) == 3:
        if args[2].find('a') > 0 or args[2].find('A') > 0:
            return float(args[1]), True
        return float(args[1]), False

def main():
    ''' main function '''

    #
    delay, append_log = parse_arguments(argv)

    print
    print 'Confirming login credentials for:'
    print '\t' + 'device-id:\t' + DEVICE_ID
    print '\t' + 'token:\t\t' + ACCESS_TOKEN
    print

    # initialize variables
    bit = cloud.Bit(ACCESS_TOKEN, DEVICE_ID)

    # open file for logging
    f=open('temperature_log.csv', 'w')

    # initialize counter
    n = 0

    # open stream and begin logging;
    while True:
        for t in bit.stream():

            # print to screen just for fun
            dttm = get_date_time()
            val = str(t)
            print dttm + '\t' + val

            # log value to file
            f.write(dttm + ',' + val + '\n')

            # flush I/O buffer every 5 minutes
            if n == 60:
                f.flush()
                n = 0

            # built-in delay
            sleep(delay)
            n = n + 1

    #
    f.close()

if __name__ == '__main__':
    main()