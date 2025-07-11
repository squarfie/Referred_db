from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import EmailValidator


# Create your models here.

class Referred_Data(models.Model):
    Common_Choices = (
        ('n/a',''),
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    Common_pheno = (
        ('n/a',''),
        ('(+)','(+)'),
        ('(-)', '(-)'),
        ('NT', 'NT'),
    )
    SexatbirthChoice=(
        ('n/a',''),
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    ServiceTypeChoice=(
        ('n/a',''),
        ('In','In'),
        ('Out','Out')
        
    )
    ReasonChoices=(
        ('n/a',''),
        ('a & d','a & d'),
        ('confirmation of org and ast','a'),
        ('for ast only','b'),
        ('difficult to ID','c'),
        ('for serotyping','d'),
        ('for research','e'),
        ('Others','o')
    )

 
   
    # Batch Data
    Hide=models.BooleanField(default=False)
    Copy_data=models.BooleanField(default=False)
    Batch_Name=models.CharField(max_length=255, blank=True,)
    Date_of_Entry =models.DateTimeField(auto_now_add=True)
    RefNo=models.IntegerField(null=True, blank=True) #
    BatchNo=models.CharField(max_length=255, blank=True,)
    AccessionNo=models.CharField(max_length=255, blank=True,)
    AccessionNoGen=models.CharField(max_length=100, blank=True)
    Default_Year=models.DateField(null=True, blank=True)
    SiteCode=models.CharField(max_length=255, blank=True,) #
    Site_Name=models.CharField(max_length=255, blank=True,) #
    Referral_Date=models.DateField(null=True, blank=True)
    #Patient Information
    Patient_ID=models.CharField(max_length=255, blank=True,)
    First_Name=models.CharField(max_length=255, blank=True,)
    Mid_Name=models.CharField(max_length=255, blank=True,)
    Last_Name=models.CharField(max_length=255, blank=True,)
    Date_Birth=models.DateField(null=True, blank=True)
    Age=models.CharField(max_length=255, blank=True,)
    Age_Verification=models.CharField(max_length=255, blank=True,)
    Sex=models.CharField(max_length=255, blank=True,)
    Date_Admis=models.DateField(null=True, blank=True)
    Nosocomial=models.CharField(max_length=255, choices=Common_Choices, default="")
    Diagnosis=models.CharField(max_length=255, blank=True,)
    Diagnosis_ICD10=models.CharField(max_length=255, blank=True,)
    Ward=models.CharField(max_length=255, blank=True,)
    Service_Type=models.CharField(max_length=255, choices=ServiceTypeChoice, default="")
    #Isolate Information
    Spec_Num=models.CharField(max_length=255, blank=True,)
    Spec_Date=models.DateField(null=True, blank=True)
    Spec_Type=models.CharField(max_length=255, blank=True, null=True)
    Reason=models.TextField(max_length=255, choices=ReasonChoices, default="")
    Growth=models.CharField(max_length=255, blank=True,)
    Urine_ColCt=models.CharField(max_length=255, blank=True,)
    #Phenotypic Results
    ampC=models.CharField(max_length=255, choices=Common_pheno, default="")
    ESBL=models.CharField(max_length=255, choices=Common_pheno, default="")
    CARB=models.CharField(max_length=255, choices=Common_pheno, default="")
    MBL=models.CharField(max_length=255, choices=Common_pheno, default="")
    BL=models.CharField(max_length=255, choices=Common_pheno, default="")
    MR=models.CharField(max_length=255, choices=Common_pheno, default="")
    mecA=models.CharField(max_length=255, choices=Common_pheno, default="")
    ICR=models.CharField(max_length=255, choices=Common_pheno, default="")
    OtherResMech=models.CharField(max_length=255, blank=True)
    #Organism Result
    Site_Pre=models.CharField(max_length=255, blank=True,)
    Site_Org=models.CharField(max_length=255, blank=True,)
    Site_Pos=models.CharField(max_length=255, blank=True,)
    OrganismCode=models.CharField(max_length=255, blank=True,)
    Comments=models.TextField(blank=True, null=True)
    
    #ARSRL Sty Results
    ars_ampC=models.CharField(max_length=255, choices=Common_pheno, default="")
    ars_ESBL=models.CharField(max_length=255, choices=Common_pheno, default="")
    ars_CARB=models.CharField(max_length=255, choices=Common_pheno, default="")
    ars_ECIM=models.CharField(max_length=255, choices=Common_pheno, default="")
    ars_MCIM=models.CharField(max_length=255, choices=Common_pheno, default="")
    ars_EC_MCIM=models.CharField(max_length=255, choices=Common_pheno, default="")
    ars_MBL=models.CharField(max_length=255, choices=Common_pheno, default="")
    ars_BL=models.CharField(max_length=255, choices=Common_pheno, default="")
    ars_MR=models.CharField(max_length=255, choices=Common_pheno, default="")
    ars_mecA=models.CharField(max_length=255, choices=Common_pheno, default="")
    ars_ICR=models.CharField(max_length=255, choices=Common_pheno, default="")
    ars_Pre=models.CharField( max_length=255, blank=True,)
    ars_Post=models.CharField(max_length=255, blank=True,)
    ars_OrgCode=models.CharField(max_length=255, blank=True,)
    ars_OrgName=models.CharField(max_length=255, blank=True,)
    ars_ct_ctl=models.CharField(max_length=255, blank=True,)
    ars_tz_tzl=models.CharField(max_length=255, blank=True,)
    ars_cn_cni=models.CharField(max_length=255, blank=True,)
    ars_ip_ipi=models.CharField(max_length=255, blank=True,)
    ars_reco_Code=models.CharField(max_length=255, blank=True,)
    ars_reco=models.TextField(blank=True, null=True)
    
    #Batch Table Data
    SiteName=models.CharField(max_length=255, blank=True,)
    Month_Date=models.DateField(null=True, blank=True)
    Day_Date=models.DateField(null=True, blank=True)
    Year_Date=models.DateField(null=True, blank=True)
    RefDate=models.DateField(null=True, blank=True)
    Start_AccNo=models.IntegerField(null=True, blank=True)
    End_AccNo=models.IntegerField(null=True, blank=True)
    No_Isolates=models.IntegerField(null=True, blank=True)
    BatchNumber=models.IntegerField(null=True, blank=True)
    TotalBatchNumber=models.IntegerField(null=True, blank=True)
    Encoded_by=models.CharField(max_length=255, blank=True,)
    Encoded_by_Initials=models.CharField(max_length=255, blank=True,)
    Edited_by=models.CharField(max_length=255, blank=True,)
    Edited_by_Initials=models.CharField(max_length=255, blank=True,)
    Checked_by=models.CharField(max_length=255, blank=True,)
    Checked_by_Initials=models.CharField(max_length=255, blank=True,)
    Verified_by_Senior=models.CharField(max_length=255, blank=True,)
    Verified_by_Senior_Initials=models.CharField(max_length=255, blank=True,)
    Verified_by_LabManager=models.CharField(max_length=255, blank=True,)
    Verified_by_LabManager_Initials=models.CharField(max_length=255, blank=True,)
    Noted_by=models.CharField(max_length=255, blank=True,)
    Noted_by_Initials=models.CharField(max_length=255, blank=True,)
    Concordance_Check=models.CharField(max_length=255, blank=True,)
    Concordance_by=models.CharField(max_length=255, blank=True,)
    Concordance_by_Initials=models.CharField(max_length=255, blank=True,)
    abx_code=models.CharField(max_length=25, blank=True, default="")
    
    #laboratory personnel
    Laboratory_Staff = models.CharField(max_length=100,blank=True, default='', null=True)
    Date_Accomplished_ARSP=models.DateField(blank=True, null=True)
    ars_notes = models.TextField(blank=True, null=True)
    ars_contact = PhoneNumberField(blank=True, null=True)
    ars_email = models.EmailField(blank=True, null=True, validators=[EmailValidator()])

    def __str__(self):
        return self.AccessionNo
    
    
class Meta:
    db_table ="Referred_Data"

  
# for final edit table
class Final_Data(models.Model):
    f_Common_Choices = (
        ('n/a',''),
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    f_Common_pheno = (
        ('n/a',''),
        ('(+)','(+)'),
        ('(-)', '(-)'),
        ('NT', 'NT'),
    )
    f_SexatbirthChoice=(
        ('n/a',''),
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    f_ServiceTypeChoice=(
        ('n/a',''),
        ('In','In'),
        ('Out','Out')
        
    )
    f_ReasonChoices=(
        ('n/a',''),
        ('a & d','a & d'),
        ('confirmation of org and ast','a'),
        ('for ast only','b'),
        ('difficult to ID','c'),
        ('for serotyping','d'),
        ('for research','e'),
        ('Others','o')
    )

 
   
    # Batch Data
    f_Hide=models.BooleanField(default=False)
    f_Batch_Code=models.CharField(max_length=255, blank=True,)
    f_Date_of_Entry =models.DateTimeField(auto_now_add=True)
    f_RefNo=models.IntegerField(null=True, blank=True) #
    f_BatchNo=models.CharField(max_length=255, blank=True,)
    f_AccessionNo=models.CharField(max_length=255, blank=True,)
    f_AccessionNoGen=models.CharField(max_length=100, blank=True)
    f_Default_Year=models.DateField(null=True, blank=True)
    f_SiteCode=models.CharField(max_length=255, blank=True,) #
    f_Site_Name=models.CharField(max_length=255, blank=True,) #
    f_Referral_Date=models.DateField(null=True, blank=True)
    #Patient Information
    f_Patient_ID=models.CharField(max_length=255, blank=True,)
    f_First_Name=models.CharField(max_length=255, blank=True,)
    f_Mid_Name=models.CharField(max_length=255, blank=True,)
    f_Last_Name = models.CharField(max_length=255, blank=True)
    f_Date_Birth = models.DateField(null=True, blank=True)
    f_Age = models.CharField(max_length=255, blank=True)
    f_Age_Verification = models.CharField(max_length=255, blank=True)
    f_Sex = models.CharField(max_length=255, blank=True)
    f_Date_Admis = models.DateField(null=True, blank=True)
    f_Nosocomial = models.CharField(max_length=255, choices=f_Common_Choices, default="")
    f_Diagnosis = models.CharField(max_length=255, blank=True)
    f_Diagnosis_ICD10 = models.CharField(max_length=255, blank=True)
    f_Ward = models.CharField(max_length=255, blank=True)
    f_Service_Type = models.CharField(max_length=255, choices=f_ServiceTypeChoice, default="")

    #Isolate Information
    f_Spec_Num=models.CharField(max_length=255, blank=True,)
    f_Spec_Date = models.DateField(null=True, blank=True)
    f_Spec_Type = models.CharField(max_length=255, blank=True, null=True)
    f_Reason = models.TextField(max_length=255, choices=f_ReasonChoices, default="")
    f_Growth = models.CharField(max_length=255, blank=True)
    f_Urine_ColCt = models.CharField(max_length=255, blank=True)

    # Phenotypic Results
    f_ampC = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_ESBL = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_CARB = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_MBL = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_BL = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_MR = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_mecA = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_ICR = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_OtherResMech = models.CharField(max_length=255, blank=True)

    # Organism Result
    f_Site_Pre = models.CharField(max_length=255, blank=True)
    f_Site_Org = models.CharField(max_length=255, blank=True)
    f_Site_Pos = models.CharField(max_length=255, blank=True)
    f_OrganismCode = models.CharField(max_length=255, blank=True)
    f_Comments = models.TextField(blank=True, null=True)

    # ARSRL Sty Results
    f_ars_ampC = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_ars_ESBL = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_ars_CARB = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_ars_ECIM = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_ars_MCIM = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_ars_EC_MCIM = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_ars_MBL = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_ars_BL = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_ars_MR = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_ars_mecA = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_ars_ICR = models.CharField(max_length=255, choices=f_Common_pheno, default="")
    f_ars_Pre = models.CharField(max_length=255, blank=True)
    f_ars_Post = models.CharField(max_length=255, blank=True)
    f_ars_OrgCode = models.CharField(max_length=255, blank=True)
    f_ars_OrgName = models.CharField(max_length=255, blank=True)
    f_ars_ct_ctl = models.CharField(max_length=255, blank=True)
    f_ars_tz_tzl = models.CharField(max_length=255, blank=True)
    f_ars_cn_cni = models.CharField(max_length=255, blank=True)
    f_ars_ip_ipi = models.CharField(max_length=255, blank=True)
    f_ars_reco_Code = models.CharField(max_length=255, blank=True)
    f_ars_reco = models.TextField(blank=True, null=True)

    # Batch Table Data
    f_SiteName = models.CharField(max_length=255, blank=True)
    f_Month_Date = models.DateField(null=True, blank=True)
    f_Day_Date = models.DateField(null=True, blank=True)
    f_Year_Date = models.DateField(null=True, blank=True)
    f_RefDate = models.DateField(null=True, blank=True)
    f_Start_AccNo = models.IntegerField(null=True, blank=True)
    f_End_AccNo = models.IntegerField(null=True, blank=True)
    f_No_Isolates = models.IntegerField(null=True, blank=True)
    f_BatchNumber = models.IntegerField(null=True, blank=True)
    f_TotalBatchNumber = models.IntegerField(null=True, blank=True)
    f_Encoded_by = models.CharField(max_length=255, blank=True)
    f_Encoded_by_Initials = models.CharField(max_length=255, blank=True)
    f_Edited_by = models.CharField(max_length=255, blank=True)
    f_Edited_by_Initials = models.CharField(max_length=255, blank=True)
    f_Checked_by = models.CharField(max_length=255, blank=True)
    f_Checked_by_Initials = models.CharField(max_length=255, blank=True)
    f_Verified_by_Senior = models.CharField(max_length=255, blank=True)
    f_Verified_by_Senior_Initials = models.CharField(max_length=255, blank=True)
    f_Verified_by_LabManager = models.CharField(max_length=255, blank=True)
    f_Verified_by_LabManager_Initials = models.CharField(max_length=255, blank=True)
    f_Noted_by = models.CharField(max_length=255, blank=True)
    f_Noted_by_Initials = models.CharField(max_length=255, blank=True)
    f_Concordance_Check = models.CharField(max_length=255, blank=True)
    f_Concordance_by = models.CharField(max_length=255, blank=True)
    f_Concordance_by_Initials = models.CharField(max_length=255, blank=True)
    f_abx_code = models.CharField(max_length=25, blank=True, default="")

    # Laboratory Personnel
    f_Laboratory_Staff = models.CharField(max_length=100, blank=True, default='', null=True)
    f_Date_Accomplished_ARSP = models.DateField(blank=True, null=True)
    f_ars_notes = models.TextField(blank=True, null=True)
    f_ars_contact = PhoneNumberField(blank=True, null=True)
    f_ars_email = models.EmailField(blank=True, null=True, validators=[EmailValidator()])


    def __str__(self):
        return self.f_AccessionNo
    
    
class Meta:
    db_table ="Final_Data"

# for specific indexing use this
    # indexes = [
    #             models.Index(fields=['Egasp_Id']),  # Index for field1
    #             models.Index(fields=['Uic_Ptid']),  # Index for field2
    #             models.Index(fields=['First_Name']),  # Index for field3
    #             models.Index(fields=['Last_Name']),  # Index for field4
    #             # add more indexes as needed
    #         ]


class SiteData(models.Model):
    SiteCode=models.CharField(max_length=3, blank=True)
    SiteName=models.CharField(max_length=155, blank=True)
    def __str__(self):
        return self.SiteCode 
    
class Meta:
    db_table ="SiteData"



class BreakpointsTable(models.Model):
    TestMethodChoices =(
        ('DISK', 'DISK'),
        ('MIC','MIC'),
    )
    
    GuidelineChoices = (
        ('CLSI', 'CLSI'),        
    )

    Guidelines = models.CharField(max_length=100, choices=GuidelineChoices, blank=True, default='')
    Test_Method = models.CharField(max_length=20, choices=TestMethodChoices, blank=True, default='')
    Potency = models.CharField(max_length=5, blank=True, default='')
    Abx_code = models.CharField(max_length=15, blank=True, default='')
    Tier = models.CharField(max_length=10, blank=True, default='')
    Show = models.BooleanField(default=True)
    Retest = models.BooleanField(default=False)
    Antibiotic = models.CharField(max_length=100, blank=True, default='')
    Whonet_Abx = models.CharField(max_length=100, blank=True, default='')
    Disk_Abx = models.BooleanField(default=False)
    R_val = models.CharField(max_length=30, blank=True, default='')
    I_val = models.CharField(max_length=30, blank=True, default='')
    SDD_val = models.CharField(max_length=30, blank=True, default='')
    S_val = models.CharField(max_length=30, blank=True, default='')
    Alert_val = models.CharField(max_length=30, blank=True, default='')
    Date_Modified = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Abx_code 

class Meta:
    db_table ="BreakpointsTable"


class Breakpoint_upload(models.Model):
    File_uploadBP = models.FileField(upload_to='uploads/breakpoints/', null=True, blank=True)

class Meta:
    db_table = "Breakpoint_upload"

    
#for antibiotic test entries
class AntibioticEntry(models.Model):
#  links to main and breakpoints table
    ab_idNum_referred = models.ForeignKey(Referred_Data, on_delete=models.CASCADE, null=True, related_name='antibiotic_entries')
    ab_AccessionNo= models.CharField(max_length=100, blank=True, null=True)
    ab_RefNo = models.CharField(max_length=100, blank=True, null=True)
    ab_breakpoints_id = models.ManyToManyField(BreakpointsTable, max_length=6)
    
    ab_Antibiotic = models.CharField(max_length=100, blank=True, null=True)
    ab_Abx_code= models.CharField(max_length=100, blank=True, null=True)
    ab_Abx=models.CharField(max_length=100, blank=True, null=True)

    #sentinel site results
    ab_Disk_value = models.IntegerField(blank=True, null=True)
    ab_Disk_RIS = models.CharField(max_length=4, blank=True)
    ab_MIC_operand=models.CharField(max_length=4, blank=True, null=True, default='')
    ab_MIC_value = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    ab_MIC_RIS = models.CharField(max_length=4, blank=True)
    ab_AlertMIC = models.BooleanField(default=False)
    ab_Alert_val = models.CharField(max_length=30, blank=True, null=True, default='')

    ab_R_breakpoint = models.CharField(max_length=10, blank=True, null=True)
    ab_I_breakpoint = models.CharField(max_length=10, blank=True, null=True)
    ab_SDD_breakpoint = models.CharField(max_length=10, blank=True, null=True)  
    ab_S_breakpoint = models.CharField(max_length=10, blank=True, null=True)
    
    #arsrl results
    ab_Retest_Antibiotic = models.CharField(max_length=100, blank=True, null=True)
    ab_Retest_Abx_code = models.CharField(max_length=100, blank=True, null=True)
    ab_Retest_Abx = models.CharField(max_length=100, blank=True, null=True)
    ab_Retest_DiskValue = models.IntegerField(blank=True, null=True)
    ab_Retest_Disk_RIS = models.CharField(max_length=4, blank=True)
    ab_Retest_MIC_operand=models.CharField(max_length=4, blank=True, null=True, default='')
    ab_Retest_MICValue = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    ab_Retest_MIC_RIS = models.CharField(max_length=4, blank=True)
    ab_Retest_AlertMIC = models.BooleanField(default=False)
    ab_Retest_Alert_val = models.CharField(max_length=30, blank=True, null=True, default='')
    ab_Ret_R_breakpoint = models.CharField(max_length=10, blank=True, null=True)
    ab_Ret_I_breakpoint = models.CharField(max_length=10, blank=True, null=True)
    ab_Ret_SDD_breakpoint = models.CharField(max_length=10, blank=True, null=True)
    ab_Ret_S_breakpoint = models.CharField(max_length=10, blank=True, null=True)    

    ab_MICJoined = models.CharField(max_length=7, blank=True, null=True)
    def __str__(self):
        return ", ".join([abx.Whonet_Abx for abx in self.ab_breakpoints_id.all()]) 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the instance first
        

    class Meta:
        db_table = "AntibioticEntry"


class SpecimenTypeModel(models.Model):
    Specimen_name = models.CharField(max_length=100, blank=True, null=True)
    Specimen_code = models.CharField(max_length=4, blank=True, null=True)
    def __str__(self):
        return self.Specimen_code 

class Meta:
    db_table = "SpecimenTypeTable"


#Address Book
class Lab_Staff_Details(models.Model):
    LabStaff_Name = models.CharField(max_length=100, blank=True, null=True)
    LabStaff_Designation= models.CharField(max_length=100, blank=True, null=True)
    LabStaff_Telnum= PhoneNumberField(blank=True, region="PH", null=True)
    LabStaff_EmailAdd = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.LabStaff_Name if self.LabStaff_Name else "Unnamed Staff"

class Recommendation(models.Model):
    Reco_Code = models.CharField(max_length=100, blank=True, null=True)
    Reco_Details = models.TextField(blank=True, null=True)

    def __str__(self):
            return self.Reco_Code 