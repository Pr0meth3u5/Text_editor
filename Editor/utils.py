import pdfkit
from django.core.mail import EmailMessage


def get_filename(filname):
    New_name = "new".join(filname)
    print(New_name)
    return New_name


def renderToPdf(HtmlText, Tid, roll="00001" ):
    opath = "out/pdf/"
    opath = opath + roll + "_" + Tid +".pdf"
    print(opath + roll + ".pdf")
    config = pdfkit.configuration(
        wkhtmltopdf="D:\\Local_Projects\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    )
    pdfkit.from_string(
        HtmlText, output_path=opath, configuration=config
    )
    return opath


def sendMail(filpath, mailId):
    
    email = EmailMessage(
        "Hello",
        "Body goes here",
        "SSECTextEditor",
        [mailId],#"16.richa3@gmail.com","pmpreeti497@gmail.com"
    )
    email.attach_file(filpath)
    email.send()
