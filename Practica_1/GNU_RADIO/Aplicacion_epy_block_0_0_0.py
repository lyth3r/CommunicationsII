import numpy as np
from gnuradio import gr
class blk(gr.sync_block):
    def __init__ ( self ) : # only default arguments here
        gr. sync_block . __init__ (
            self ,
            name ="Diferenciador", # will show up in GRC
            in_sig =[np.float32],
            out_sig =[np.float32])
        self.last_sample=0
        
    def work (self , input_items , output_items ):
        x = input_items[0] # Senial de entrada .
        y = output_items[0] # Senial acumulada diferencial
        N = len(x)
        y[0] = x[0] - self.last_sample
        y[1:] = np.diff(x)
        self.last_sample = x[-1]
        
        return len(x)
