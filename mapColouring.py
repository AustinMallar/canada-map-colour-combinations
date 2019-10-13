# List of provinces
provinces = ["BC",
             "AB",
             "SK",
             "MB",
             "YK",
             "NWT",
             "NV",
             "ON",
             "QBC",
             "NFL",
             "NB",
             "NS",
             "PEI", ]

# Constraints assigned to each province. If province is in the tuple, it can't be the same colour.
neighbouring_provinces = {
    "BC": ("AB", "YK", "NWT"),
    "AB": ("BC", "NWT", "SK"),
    "SK": ("AB", "MB", "NWT"),
    "MB": ("SK", "ON", "NV"),
    "YK": ("BC", "NWT"),
    "NWT": ("BC", "YK", "AB", "SK", "NV"),
    "NV": ("NWT", "MB"),
    "ON": ("MB", "QBC"),
    "QBC": ("ON", "NB", "NFL"),
    "NFL": ("QBC",),
    "NB": ("QBC", "NS"),
    "NS": ("NB",),
    "PEI": ()
}

# Dictionary containing colour (number) assigned to each province. (0 means no colour assigned)
x = {
    "BC": 0,
    "AB": 0,
    "SK": 0,
    "MB": 0,
    "YK": 0,
    "NWT": 0,
    "NV": 0,
    "ON": 0,
    "QBC": 0,
    "NB": 0,
    "NS": 0,
    "PEI": 0,
}

# Global variable that keeps track of number of valid combinations
num_combinations = 0

# Main recursive function for assigning colours to each province


def colourMap(k):
    global num_combinations
    for colour in range(1, num_colours+1):
        if(isValid(k, colour)):
            # Get the name of the province from provinces list using index k
            province = provinces[k]
            # assign colour to province in the province dictionary
            x[province] = colour
            if(k+1 < len(provinces)):
                # Call colourMap function with the next province
                colourMap(k+1)
            else:
                # Found valid colour combination for all provinces
                print(x)
                num_combinations += 1
                return


def isValid(k, colour):
    province = provinces[k]
    # Iterate through provinces
    for i in x:
        # If the province in current iteration neighbours the province we are validating AND has the same colour, return FALSE
        if(i in neighbouring_provinces[province] and colour == x[i]):
            return False
    return True


num_colours = int(input("Enter the number of colours to use: "))

# Start at the first index of the provinces list (BC)
colourMap(0)
print("Found {} combinations".format(num_combinations))
