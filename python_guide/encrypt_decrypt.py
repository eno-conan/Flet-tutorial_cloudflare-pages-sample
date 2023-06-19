import flet as ft
from flet.security import encrypt, decrypt
import os
from dotenv import load_dotenv
load_dotenv()


def main(page):

    secret_key = os.getenv("GITHUB_CLIENT_ID")
    to_encrypt_text = ft.Ref[ft.TextField]()
    to_decrypt_text = ft.Ref[ft.TextField]()

    def run_encrypt(e):
        encrypted_data = encrypt(to_encrypt_text.current.value, secret_key)
        to_encrypt_text.current.value = ""
        print(encrypted_data)
        page.update()

    def run_decrypt(e):
        plain_text_data = decrypt(to_decrypt_text.current.value, secret_key)
        to_decrypt_text.current.value = ""
        print(plain_text_data)
        page.update()

    page.add(
        ft.Text(value="Encrypt", size=28, color="blue"),
        ft.TextField(ref=to_encrypt_text,
                     label="To Encrypt Text", autofocus=True),
        ft.ElevatedButton("encrypt!", on_click=run_encrypt),
        ft.Text(value="Decrypt", size=28, color="red"),
        ft.TextField(ref=to_decrypt_text, label="To Decrypt Text"),
        ft.ElevatedButton("decrypt", on_click=run_decrypt),

    )


ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
