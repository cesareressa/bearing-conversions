bearing_type_dict = {
    "BC": 6,
    "BL": "-",
    "BN": 7,
    "BA": 7,
    "BY": 7,
}

def get_afbma_bearing_type(skf_digit: int) -> str:
    """
    Use to get AFBMA bearing type from SKF int value. Returns
    key of bearing_type_dict based on value (e.g. 6 -> BC)
    """
    for afbma, skf in bearing_type_dict.items():
        if skf == skf_digit:
            return(afbma) 

def AFBMA_to_SKF(query: str) -> str:
    """
    Use to get SKF conversion
    """
   #split query
    query_list = [query[i:i+2] for i in range(0, 6, 2)]

    afbma_pars_dict = {
        "bore_diameter": int(query_list[0])/5,
        "bearing_type": query_list[1],
        "dimension_series" : query_list[2].replace("0",""),
    }

    bearing_type_SKF = bearing_type_dict[afbma_pars_dict["bearing_type"]]

    return str(bearing_type_SKF) + str(afbma_pars_dict["dimension_series"]) + str(afbma_pars_dict["bore_diameter"]).replace(".0", "")


def SKF_to_AFBMA(query: str) -> str:
    """
    Use to get SKF conversion
    """

    skf_pars_dict = {
        "bore_diameter": (int(query[-2:]))*5,
        "bearing_type": get_afbma_bearing_type(int(query[0])),
        "dimension_series" : query[1],
    }

    return str(skf_pars_dict["bore_diameter"]) +str(skf_pars_dict["bearing_type"]) + "0" + str(skf_pars_dict["dimension_series"])


# string = "65BY04"

# print(AFBMA_to_SKF(string))

# string = "6313"

# print(SKF_to_AFBMA(string))