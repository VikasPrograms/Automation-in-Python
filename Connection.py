
# ===================
#
# Imports
#
# ===================

from urllib.request import urlopen

try:
        urlopen('http://www.google.com', timeout = 1)
        print("\nSuccessfully Connected To Internet...")
except:
        print("\nERROR : Please Check Your Internet Connection, Unable To Send Mail!")

# ==============================
#
# Check Connection
#
# ==============================

def Check_Connection():

    try:
        urlopen('http://www.google.com', timeout = 1)
        return True
    except:
        return False