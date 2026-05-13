import pandas as pd
def station_performance_summary(input_data):
    selections = ["final_station_name"]
    total_records_for_each_stationPythonVariable = input_data.groupby(selections).size().reset_index(name="total_records_for_each_stationPythonVariable")
    average = input_data.groupby(selections)["delay_in_min"].mean().reset_index(name="average_minutes")
    maximumDelay = input_data.groupby(selections)["delay_in_min"].max().reset_index(name="maximumDelay_minutes")
    cancelled = input_data.groupby(selections)["is_canceled"].sum().reset_index(name="cancelled")
    finalTable = total_records_for_each_stationPythonVariable.merge(average, on=selections)
    finalTable = finalTable.merge(maximumDelay, on=selections)
    finalTable = finalTable.merge(cancelled, on=selections)
    finalTable["cancellation_rate_percent"] = (finalTable["cancelled"] / finalTable["total_records_for_each_stationPythonVariable"]) * 100
    finalTable["average_minutes"] = finalTable["average_minutes"].round(2)
    finalTable["cancellation_rate_percent"] = finalTable["cancellation_rate_percent"].round(2)
    finalTable = finalTable[finalTable["total_records_for_each_stationPythonVariable"] >= 100]
    finalTable = finalTable.rename(columns={"final_station_name": "station_name_for_analysis"})
    finalTable = finalTable.sort_values(by="average_minutes", ascending=False)
    return finalTable