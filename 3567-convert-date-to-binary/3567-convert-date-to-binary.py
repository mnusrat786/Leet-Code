class Solution(object):
    def convertDateToBinary(self, date):
        year, month, day = date.split("-")
        #conversion,typecasting
        year_bin = bin(int(year))[2:]
        month_bin = bin(int(month))[2:]
        day_bin = bin(int(day))[2:]
        
        return f"{year_bin}-{month_bin}-{day_bin}"