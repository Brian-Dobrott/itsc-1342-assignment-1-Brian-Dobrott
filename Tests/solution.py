# [Brian Dobrott] - Assignment 1


# If username or password are wrong the login fails. 
# clearance level will also give different results
def verify_access(username, password, clearance_level):
    if username != "soc_admin" or password != "S3cur3_P@ss":
        return "INTRUSION_DETECTED"

    # This is the highest clearance level
    elif clearance_level >= 5:
        return "ROOT_ACCESS_GRANTED"

    # This is the lower clearance levels
    elif clearance_level == 3 or clearance_level == 4:
        return "ANALYST_ACCESS_GRANTED"

    # This is where you don't have clearance
    # Even with the correct username & password
    else:
        return "INSUFFICIENT_CLEARANCE"
