from json import load as lod

def jsn_dat(loc):
    return lod(open(loc))

def cfg_clr(clr):
    return (int(clr[0]), int(clr[1]), int(clr[2]))