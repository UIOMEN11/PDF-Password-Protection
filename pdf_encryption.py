import pikepdf

old_pdf = pikepdf.Pdf.open("Data model.pdf")

no_extract = pikepdf.Permissions(extract = False)

old_pdf.save("Data model_encrypted.pdf",
             encryption=pikepdf.Encryption(user="qwerty12345",
                                           owner = "Aditya",
                                           allow=no_extract))