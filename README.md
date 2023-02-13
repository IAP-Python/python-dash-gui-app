# Rad Test Cruncher

## Introduction


Rad Test Cruncher is a Lab-View based BI designed in Dash by Plotly and uses numpy and pandas as the backbone to handle Texas Instruments' Radiation tests.

The instruments that are most commonly used are catergorized as:

- SMU

> A source measure unit (SMU) is an instrument that combines a sourcing function and a measurement function on the same pin or connector. It can source voltage or current and simultaneously measure voltage and/or current. It integrates the capabilities of a power supply or function generator, a digital multimeter (DMM) or oscilloscope, a current source, and an electronic load into a single, tightly synchronized instrument. 
<br /> <br /> 
from: https://www.analog.com/en/analog-dialogue/studentzone/studentzone-december-2017.html

- Power Supply Models

- DIO

# Info n stuff

1.  PXIe-4145 (4 channels, -6 to +6 -V, -500 to +500 -mA, 3 -W)
    - Current Available Cards : 1
    - Vendor: National Intruments
    - communication protocol: PXI
2. PXIe-4139 (1 channel,-60 to +60 -V, -3 to +3 -A, 20 -W)
     - Current Available Cards : 2
    - Vendor: National Intruments
    - communication protocol: PXI 


# Setup using Docker

```
docker-compose build
docker-compose up -d
```

### Stop and remove container
docker-compose stop

### Restart container
docker-compose restart

# Running the App


pip install dash-uploade