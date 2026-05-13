import pandas as pd
def monthly_train_type_delay_summary(input_data):
    selections = ["source_month", "train_type"] #Grouping using these from tableau.
    total_records = input_data.groupby(selections).size().reset_index(name="total_records")
    average = input_data.groupby(selections)["delay_in_min"].mean().reset_index(name="average_minutes")
    maximumDelay = input_data.groupby(selections)["delay_in_min"].max().reset_index(name="maximumDelay_minutes")
    cancelled = input_data.groupby(selections)["is_canceled"].sum().reset_index(name="cancelled")
    finalTable = total_records.merge(average, on=selections)
    finalTable = finalTable.merge(maximumDelay, on=selections)
    finalTable = finalTable.merge(cancelled, on=selections)
    finalTable["cancellation_rate_percent"] = (finalTable["cancelled"] / finalTable["total_records"]) * 100
    finalTable["average_minutes"] = finalTable["average_minutes"].round(2)
    finalTable["cancellation_rate_percent"] = finalTable["cancellation_rate_percent"].round(2)
    finalTable = finalTable.sort_values(by=["source_month", "average_minutes"],ascending=[True, False])
    return finalTable