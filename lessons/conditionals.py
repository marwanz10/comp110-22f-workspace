"""Example implementing a list utility function."""

# Function name: contains
# We will have 2 paramters: needle (str), haystack (list[str])
# Return type bool
def contains(needle: str, haystack: list[str]) -> bool:
     # Gameplan:
    # 1. Start iwth the first index
    i: int = 0
    # 2. Loop through every index
    while i < len(haystack):
        #   2.A Test if item at index equal to needle
        if haystack[i] == needle:
            #  We found it! No more work to do!
                return True
        i += 1      
    # 3. Return False
    # We tried searching each item and came up short!
    return False