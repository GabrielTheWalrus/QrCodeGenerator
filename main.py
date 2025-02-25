import qrcode

def gerar_qrcode(url, nome_arquivo="qrcode.jpg"):
    # Cria um objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    # Adiciona a URL ao QR Code
    qr.add_data(url)
    qr.make(fit=True)

    # Gera a imagem do QR Code
    img = qr.make_image(fill_color="black", back_color="white")
    # Salva a imagem em um arquivo
    img.save(nome_arquivo)
    print(f"QR Code salvo como {nome_arquivo}")

# Exemplo de uso
if __name__ == "__main__":
    url_input = "https://open.spotify.com/intl-pt/album/22XkBaW2DwVVyhpWbsBtG6?si=tuccniCySkmLAYQSLdxBsQ"  # Coloque aqui a URL desejada
    gerar_qrcode(url_input, "GET BORN STAY BORN.jpg")