import pandas as pd
import numpy as np
import os



sector_dict = {
    11: "Agriculture, Forestry, Fishing and Hunting",
    21: "Mining, Quarrying, and Oil and Gas Extraction",
    22: "Utilities",
    23: "Construction",
    31: "Manufacturing",
    32: "Manufacturing",
    33: "Manufacturing",
    42: "Wholesale Trade",
    44: "Retail Trade",
    45: "Retail Trade",
    48: "Transportation and Warehousing",
    49: "Transportation and Warehousing",
    51: "Information",
    52: "Finance and Insurance",
    53: "Real Estate and Rental and Leasing",
    54: "Professional, Scientific, and Technical Services",
    55: "Management of Companies and Enterprises",
    56: "Administrative and Support and Waste Management and Remediation Services",
    61: "Educational Services",
    62: "Health Care and Social Assistance",
    71: "Arts, Entertainment, and Recreation",
    72: "Accommodation and Food Services",
    81: "Other Services",
    92: "Public Administration"
}

def get_sector_code(code): 
  if (len(code) <= 1):
    return None
  return code[:2]

def get_subsector_code(code): 
  if (len(code) <= 2):
    return None
  return code[:3]

def get_industry_group_code(code): 
  if (len(code) <= 4):
    return None
  return code[:4]

def get_sector_code(code): 
  if (len(code) <= 1):
    return code
  return code[:2]

def getSectorDescription(code):
  code = int(code)
  if code in sector_dict:
    return sector_dict[code]
  else:
    return None

def generateUpdated(filename, folder): 
    df = pd.read_csv(folder + "/" + filename, dtype=str)
    df['JOB_TITLE'].replace(" ", np.nan, inplace=True)
    df.dropna(subset=['JOB_TITLE'], inplace=True)
    df = df[df["FIRST_DECISION"] == "Approved"]
    df["SECTOR_CODE"] = df["NAICS_CODE"].apply(get_sector_code)
    df["SUBSECTOR_CODE"] = df["NAICS_CODE"].apply(get_subsector_code)
    df["INDUSTRY_GRP_CODE"] = df["NAICS_CODE"].apply(get_industry_group_code)
    df["SECTOR_DESCRIPTION"] = df["SECTOR_CODE"].apply(getSectorDescription)
    

    ignorePortion = "TRK_13139_"
    startPoint = len(ignorePortion)
    updatedName = "UPDATED_" + filename[startPoint:]
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, "..", "datasets", updatedName)
    df.to_csv(path)


if __name__ == "__main__":
    folder = "original_datasets"
    directory = os.fsencode(folder)
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".csv"): 
            generateUpdated(filename, folder)