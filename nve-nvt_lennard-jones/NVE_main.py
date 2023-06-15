import argparse
from NVE_lj import VV_mdlj
parser = argparse.ArgumentParser()
parser.add_argument("--kt",type=float,default=0.694,help='The temperature of the system.', required=False)
parser.add_argument("--nstep",type=int,default=1000,help='Total number of timesteps to run the simulation for.', required=False)
parser.add_argument("--mode",type=int,default=0,help='Initialization mode (see notes).'  , required=False)
parser.add_argument("--dt",type=float,default=0.005,help='Size of timestep to use.'  , required=False)
args = parser.parse_args()

kt=args.kt
nstep=args.nstep
mode=args.mode
dt=args.dt
VV_mdlj(mode=mode,nstep=nstep,dt=dt,freq=10,kt=kt)
