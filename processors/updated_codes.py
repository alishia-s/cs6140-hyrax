import pandas as pd


if __name__ == "__main__":
    df = pd.read_csv("FY2021.csv")

# drop empty JOB_TITLE
    df['JOB_TITLE'].replace(" ", np.nan, inplace=True)
    df.dropna(subset=['JOB_TITLE'], inplace=True)
    df = df[df["FIRST_DECISION"] == "Approved"]
    df["SECTOR_CODE"] = df["NAICS_CODE"].apply(get_sector_code)
    df["SUBSECTOR_CODE"] = df["NAICS_CODE"].apply(get_subsector_code)
    df["INDUSTRY_GRP_CODE"] = df["NAICS_CODE"].apply(get_industry_group_code)
    df["SECTOR_DESCRIPTION"] = df["SECTOR_CODE"].apply(getSectorDescription)
    df.head()