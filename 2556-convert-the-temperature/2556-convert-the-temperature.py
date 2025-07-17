class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = float(celsius) + 273.15
        fahrenheit = (float(celsius* 1.80)) + 32
        ans = [kelvin,fahrenheit]
        return ans


 
        