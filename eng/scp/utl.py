from typing import Any
from scp.fnc import *

import pygame as pg

class txt_utl:
    def __init__(self, dat, suf):
        self.dat = jsn_dat(dat)
        self.suf = suf
    
    def drw(self, drw_txt, drw_xy, drw_clr, drw_siz=1):
        self.drw_txt = str(drw_txt)
        self.drw_xy = (int(drw_xy[0])), int(drw_xy[1])
        self.drw_clr = cfg_clr(drw_clr)
        self.drw_siz = int(drw_siz)
        self.drw_plc = 0

        for let in self.drw_txt:
            for y in range(len(self.dat[let])):
                for x in range(len(self.dat[let][0])):
                    if self.dat[let][y][x] == 1:
                        pg.draw.rect(self.suf, self.drw_clr, pg.FRect(self.drw_xy[0] + self.drw_plc + (x * self.drw_siz), self.drw_xy[1] + (y * self.drw_siz), 1, 1))
            
            self.drw_plc += len(self.dat[let][0]) * self.drw_siz + self.drw_siz