import pdfkit
from django.core.mail import EmailMessage


def get_filename(filname):
    New_name = "new".join(filname)
    print(New_name)
    return New_name


def renderToPdf(HtmlText, roll="00001"):
    opath = "out/pdf/"
    print(opath + roll + ".pdf")
    config = pdfkit.configuration(
        wkhtmltopdf="D:\\Local_Projects\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    )
    pdfkit.from_string(
        HtmlText, output_path=opath + roll + ".pdf", configuration=config
    )
    return opath + roll + ".pdf"


def sendMail(filpath):

    email = EmailMessage(
        "Hello",
        "Body goes here",
        "mayurajxxx@gmail.com.com",
        ["hurvashidewangan8118@gmail.com"],
    )
    email.attach_file(filpath)
    email.send()
