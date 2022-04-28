# from fpdf import FPDF


# class PDF(FPDF):
#     def header(self):
#         # self.image("logo.png", 10, 10, 50)
#         self.set_font("times", "B", 16)
#         title1 = "DEPARTMENT OF RADIOLOGY AND IMAGING"
#         title2 = "CHEST X-RAY REPORT"
#         self.cell(0, 8, title1, ln=1, align="C")
#         self.cell(0, 8, title2, ln=1, align="C")

#     def footer(self):
#         self.set_y(-15)
#         self.set_font("helvetica", "I", 10)
#         self.multi_cell(
#             0,
#             5,
#             "*This report is NOT valid for medico-legal purposes. In case of any discrepancy, please get it rectificed immediately.",
#         )


# def create_pdf(parameters, label_pred):
#     pdf = PDF("P", "mm", "A4")
#     pdf.set_auto_page_break(auto=True, margin=15)

#     pdf.add_page()
#     pdf.set_font("times", "", 14)
#     age_sex = f"{parameters['age']}/{parameters['sex']}"
#     field_data = f"\n\
# {'Name :':15}{parameters['patient_name']:35}{'Procedure date :':20}{parameters['procedure_date']:35}\n\
# {'Age/Sex :':15}{age_sex:35}{'Requested by :':20}{parameters['doctor_name']:35}\n\
# {'Institution :':15}{parameters['institution']:35}{'Reported at :':20}{parameters['reported_time']:35}\n\n\n"

#     pdf.multi_cell(0, 8, field_data)
#     pdf.set_line_width(0.75)
#     pdf.line(x1=0, y1=70, x2=1000, y2=70)

#     pdf.set_font("times", "B", 16)
#     pdf.write(None, "Computer Model Analysis Results:\n\n\n")
#     pdf.set_font("times", "", 14)
#     if label_pred:
#         pdf.write(
#             None,
#             " Features indicative of COVID-19 found in uploaded Chest X-ray.\nPlease Correlate Clinically.\n\n\n\n",
#         )
#     else:
#         pdf.write(
#             None,
#             " No features corresponding to COVID-19 found in uploaded Chest X-ray.\nPlease Correlate Clinically.\n\n\n",
#         )

#     pdf.set_font("times", "B", 16)
#     pdf.write(None, "Radiologist Remarks:\n\n\n")
#     pdf.set_text_color(0, 0, 0)
#     pdf.cell(0, 120, border=True)
#     return pdf
