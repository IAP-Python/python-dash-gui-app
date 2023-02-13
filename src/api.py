"""
API of the app where data manipulation nstuff  happens idk
"""

from nptdms import TdmsFile
import timeit
import numpy as np
import argparse
import sys
import pandas as pd
from scipy import signal
# import pyyaml


from math import log10,floor,copysign,sqrt,factorial # Import mathematical functions

# TODO Finish Query implementation of groups
    
options = {
    "window": np.array(["hanning", "flattop", "tukey", "exponential"]), # Window Type
    "filtertype": np.array(["running-average", "savitzky-golay", "wavelets"]), # Filter technique
    "window_len": 4,
    "norm-technique": np.array(["min-max", "z-score"]),
}

#%% --------------------------DATA MANIPULATION-------------------------------
def data_smoothing(data: pd.Series, filtertype:str="rolling-average", **kwargs) -> pd.Series:
    """
        Data Smoothing (pandas)
        ----------
        Returns a smoothed pandas Series based on the specified
        statistical technique. In escence, this function is just
        a wrapper function of different filtering and smoothing 
        techniques implemented in scipy, numpy or pandas packed
        together with default parameters that better suits our
        needs.

        Parameters
        ----------
        data : A 1D pandas Series whose elements are integers or floats.
        filtertype : Options => "rolling-average" (default), "savitzky-golay", "FFT" (fast fourier transform), "SMA" (simple median average)
        kwargs : Additional arguments based on the filter selected

        Returns
        -------
        pandas.Series : A Copy of the input data but smoothed
    """
    args = kwargs.keys()
    try:
        filtertype = filtertype.lower()
        if not filtertype in options["filtertype"]:
            raise ValueError("Valid Filter Type's are:", options["filtertype"])
    except:
        print("Using default option: rolling-average")
        filtertype = "rolling-average"

    # Global options for all statistical smoothing techniques
    window = 4 if "win-length" not in args else kwargs["win-length"]

    if filtertype == "savitzky-golay":
        order = 2 if  "order" not in args else kwargs["order"]
        return signal.savgol_filter(x=data, window_length=window, polyorder=order)

    # TODO Investigate best wavelet technique for part testing
    elif filtertype == "wavelets":
        pass

    else: # running average
        return signal.convolve(x, np.ones(window), 'valid') / window



def norm_data(data: pd.Series, nominal: int, scale:int=100, technique="min-max") -> pd.Series:
    """
        Normalization of Data (pandas)
        ------------------------------
        Normalized Waveform with Respect to a Nominal Value and rescale to match non-normalized data scale

        Parameters
        _____
        data   : A 1D pandas Series whose elements are integers or floats
        normal : An integer value to be used and the base for the normalization.
        scale  : (optional) default is 100. An integer scalar in which the normalized data is scaled to
        technique : (optional) default is "min-max". Specifies the normalization technique to be used.
        Available techniques are: "min-max" and "z-score"

        Returns
        -------
        pandas.Series => A normalized copy of data
    """
    try:
        if technique not in options["norm-technique"]:
            pass
    except:
        print("Using default option: min-max")


    pass

def plotter():
    # go to data at SEL_21_01_10
    pass

def __group_name__(n):
    # return np.char.split(n.name, '_')
    return n.name.split('_')

def main():
    parser = argparse.ArgumentParser(
        prog="duco-fire",
        description="The CLI version of the app. Here you can do something similar to the web gui but on the terminal"
        )
    
    parser.add_argument("--file", help="File can either be TDMS or CSV. Else DucoFire gets angry", type=TdmsFile.open)
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        exit()

    if args.file:
        groups = np.asarray(args.file.groups(), dtype=object) # Pull up all the groups plz
        
        # Note: using lambda functions may be more convenient, however
        # I found some visible performance loss compared to just creating
        # a "private" function
        group_names = np.vectorize(__group_name__) # Group names
        
        get_group_names = group_names(groups)
        a = get_group_names
        # print(args.file["Beam1_SCOPE3-5172_69"].channel)
        
        # print(a)
        
        # Filtering
        # filter(get_group_names, )
        
        

if __name__ == '__main__':
    pass
    # main()