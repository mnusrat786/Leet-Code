class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = float(celsius) + 273.15
        fahrenheit = (float(celsius* 1.80)) + 32.00
        return [kelvin,fahrenheit]
        # return ans


 
        