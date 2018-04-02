# home-sensors

This littleBits-powered home temperature sensor project was devleoped as a learning tool for an elementary school student to teach some fundamentsals of IoT devices, coding, and visualization of time series data. The core script makes use of an exisitng API wrapper for the libbleBits Cloud.

## Install Partly-Cloudy API
The CloudBit example script uses the Partly-Cloudy API wrapper which will first need to be installed.
```
>>> git clone https://github.com/rpmurph/home-sensors.git
>>> python setup.py sdist
>>> python setup.py install
```

## Update littleBits Cloud credentials
```
DEVICE_ID = <INSERT YOUR DEVICE ID>
ACCESS_TOKEN = <INSERT YOUR ACCESS TOKEN>
```

## Run the script
```
>>> python cloudbit-demo.py [Sample Frequency] [Append Log]
```

Where `Sample Frequency` is the time between subsequent API calls specificed in seconds, and `Append Log` will append the log file rather than overwrite by specifiying either `-a` or `-A`. Note the delay is important as the littleBits API is rate limited.
