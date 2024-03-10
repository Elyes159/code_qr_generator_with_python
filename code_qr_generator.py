import qrcode

def generer_code_qr(data, nom_fichier='code_qr.png'):
    # Créer un objet QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Ajouter les données au QRCode
    qr.add_data(data)
    qr.make(fit=True)

    # Créer une image QRCode
    img = qr.make_image(fill_color="black", back_color="white")

    # Sauvegarder l'image
    img.save(nom_fichier)

if __name__ == "__main__":
    # Exemple d'utilisation : générer un code QR pour le lien "https://www.example.com"
    generer_code_qr("https://www.example.com", "code_qr_example.png")
