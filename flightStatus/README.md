# DIY flight status

## Overview
This is a hack to locate your flight path in real-time while you are
flying with any airline carrier that has Gogo inflight wifi services.

## Requirements

You need to be on inflight wifi for the webpage to work.

## Running

```bash
# install Python requirements
pip install -r requirements.txt

# run flight status updater every 60 seconds
while true; do python gen_flight_status.py; sleep 60; done

# in another terminal, start a web server
python3 -m http.server
```

At this point go to http://localhost:8000 in a web browser to see your
live, real-time flight path.  The page refreshes every minute.
