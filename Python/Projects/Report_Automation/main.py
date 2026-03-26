from sample_input import *
from Model import *
from docx import *
from Utils import *
import os


# This should be coming from user input

report = Report(
    Application(**app_data),
    [Finding(**find) for find in findings_list],
    Format(),
     './Templates/Detailed_Report.docx',
     './Output/Detailed_report.docx'
)


# Report Generation Starts

detailed_report_document = Document(report.detailed_report_template_path)

    

# 1. Replace app details in word doc
print(dict(report.app_data))
replace_with_app_data(report,detailed_report_document)




try:
    if os.path.exists(report.output_detailed_report_path):
        os.remove(report.detailed_report_template_path)

    detailed_report_document.save(str(report.output_detailed_report_path))

except Exception as e:
    raise e


# High = [find for find in report.findings if find.FINDING_SEVERITY == 'High']


# print(report.detailed_report_template_path)
# print()



# report = Report(**app_data)

# print()
# print(report.__dict__)