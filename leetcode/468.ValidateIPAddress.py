class Solution:
    def validIPAddress(self, IP: str) -> str:

        # Check if a given segment of a IP4 address meets the validation requirements
        def isIP4(chunk):
            try: return str(int(chunk)) == chunk and 0 <= int(chunk) <= 255
            except ValueError: return False
        
        # Check if a given segment of a IP6 address meets the validation requirements
        def isIP6(chunk):
            try: return int(chunk, 16) >= 0 and len(chunk) <= 4
            except ValueError: return False

        # If the IP address has 3 '.' (aka 4 parts) and all its segments are valid then it is IP4
        if IP.count(".") == 3 and all(isIP4(chunk) for chunk in IP.split('.')):
            return "IPv4"
        
        # If the IP address has 7 ':' (aka 6 parts) and all its segments are valid then it is IP6
        elif IP.count(":") == 7 and all(isIP6(chunk) for chunk in IP.split(':')):
            return "IPv6"
        
        # Otherwise it is neither type
        return "Neither"