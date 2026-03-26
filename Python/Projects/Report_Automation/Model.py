from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional
from datetime import date, datetime
import re


class Finding(BaseModel):
    FINDING_ID: int
    FINDING_NAME: str
    FINDING_DESCRIPTION: str
    FINDING_IMPACT: str
    FINDING_REMEDIATION: str
    FINDING_SEVERITY: str
    FINDING_CVSS: Optional[float]
    FINDING_CATEGORY: str
    FINDING_CATEGORY_URL: str
    FINDING_OWASP_REF: str


class Format(BaseModel):

    # Colors
    HighSeverityColor: Optional[str] = '#E60000'
    MediumSeverityColor: Optional[str] = '#F79646'
    LowSeverityColor: Optional[str] = '#9BBB59' 
    TableTopRowColor: Optional[str] = '#595959'
    TableBackColor1: Optional[str] = '#F4EFE0'
    TableBackColor2: Optional[str] = '#E8DDBB'
    FontSize: Optional[int] = 12
    FontName: Optional[str] = 'Arial(Body)'


class Application(BaseModel):
    
    APP_ID: str = 'ABC'
    APP_NAME: str = "Test Application"
    APP_NETWORK: str = 'External'
    APP_STARTDATE: date = None
    APP_ENDDATE: date = None
    APP_URL: str = 'https://testapp.xyz.com'
    APP_ASSESMENTID: int = Field(
        ...,
        ge=1,
        le=9999,
        description='Assessment Id',
        examples=1234
    )
    


    @field_validator('APP_URL')
    def ApplicationURL(cls,url):
        pattern = r"^(http|https):\/\/\w+.\w+.\w+"
        if not re.fullmatch(pattern, url):
            raise ValueError('App URL is not proper')
        return url 
    
    @model_validator(mode='after')
    def validate_model(cls, values):
        if values.APP_STARTDATE > values.APP_ENDDATE:
            raise ValueError('Start date cant be greater than End date')


    # @computed_field
    # @property
    # def total_findings_count(self) -> int:
    #     return self.APP_HIGH_COUNT + self.APP_MEDIUM_COUNT + self.APP_LOW_COUNT


    @classmethod
    def get_parameters(cls):
        return 


    @staticmethod
    def welcome_message():
        return "Welcome to Report Automation!!"


 
class Report():
    
    def __init__(
            self,
            Application, 
            Finding, 
            Format,
            detailed_report_path: str = './Templates/Detailed_Report.docx',
            output_detailed_report_path: str = './Output/Detailed_report.docx'):
        
        self.app_data = Application
        self.findngs = Finding
        self.format = Format    
        self.detailed_report_template_path = detailed_report_path
        self.output_detailed_report_path = output_detailed_report_path
        pass


