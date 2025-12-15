from bmondata import Server

SENSOR_ID = 'mtn_dhw_circ_state'

def dhw_circ_pump_runtime():
    svr = Server('https://bmon.analysisnorth.com')
    df = svr.sensor_readings(
        SENSOR_ID,
        averaging = '1W'
    )
    ax = df.plot(figsize=(10, 5))
    return ax.get_figure()
