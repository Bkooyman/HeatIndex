import math

def calculate_HI(t , rh):
    """
    use the formula from the following webpage to calculat HI
    https://en.wikipedia.org/wiki/Heat_index
    this is confirmed the by the NWS here: https://www.wpc.ncep.noaa.gov/html/heatindex.shtml
    they include some adjustments https://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml

    
    """
    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -0.00683783
    c6 = -0.05481717
    c7 = 0.00122874
    c8 = 0.00085282
    c9 = -0.00000199

    if t > 79:
        hi = c1 + c2*t + c3*rh + c4*t*rh + c5*(t*t) + c6*(rh*rh) \
            + c7*(t*t)*rh + c8*t*(rh*rh) + c9*(t*t)*(rh*rh)
       
        # If the RH is less than 13% and the temperature is between 80 and 112 
        # degrees F, then the following adjustment is subtracted from HI: 
        if rh < 13 and t > 79 and t < 112:
            hi = hi - (13-rh)/4 * math.sqrt((17-abs(t-95))/17)
        
        # if the RH is greater than 85% and the temperature is between 
        # 80 and 87 degrees F, then the following adjustment is added to HI: 
        if rh > 85 and t > 79 and t < 88:
            hi = hi + (rh-85)/10 * (87-t)/5
    else: 
        hi = 0.5 * (t + 61.0 + ((t-68.0)*1.2) + (rh * 0.094))
    
    return math.floor(hi)

def get_risk_level(hi):
   
    if hi < 79:
        return "No Risk"
    elif hi > 78 and hi < 91:
        return "Minor"
    elif hi > 90 and hi < 103:
        return "Moderate"
    elif hi > 102 and hi < 125:
        return "Major"
    else: 
        return "Extreme"

# print(calculate_HI(80.0, 65.0))
# print(calculate_HI(90.0, 95.0))
# print(calculate_HI(90.0, 11.0))
# print(calculate_HI(82.0, 95.0))
