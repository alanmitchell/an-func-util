from func_to_web import run
from find_elsys import find_elsys_device
from dhw_runtime import dhw_circ_pump_runtime

run([find_elsys_device, dhw_circ_pump_runtime])
