import argparse
from NVT_lj import NH_mdlj
parser = argparse.ArgumentParser()
parser.add_argument("--kt",type=float,default=0.694,help='The temperature of the system.', required=False)
parser.add_argument("--tausq",type=float,default=1.0,help='tau**2 parameter for N-H thermostat.', required=False)
parser.add_argument("--kt_init",type=float,default=1.0,help='Initial temperature for the system.', required=False)
parser.add_argument("--kt_targ",type=float,default=1.0,help='Target temperature for the system.', required=False)
parser.add_argument("--nstep",type=int,default=1000,help='Total number of timesteps to run the simulation for.', required=False)
parser.add_argument("--mode",type=int,default=0,help='Initialization mode (see notes).'  , required=False)
parser.add_argument("--dt",type=float,default=0.005,help='Size of timestep to use.'  , required=False)
args = parser.parse_args()

kt_init=args.kt_init
nstep=args.nstep
mode=args.mode
dt=args.dt
tausq=args.tausq
kt_targ=args.kt_targ

NH_mdlj(mode=0,nstep=4000,kt_init=.5,kt_targ=1.,tausq=1.,freq=20)
