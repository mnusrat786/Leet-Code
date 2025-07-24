class Solution(object):
    def defangIPaddr(self, address):

        output = address.replace(".","[.]")
        return output
        """
        :type address: str
        :rtype: str
        """
        