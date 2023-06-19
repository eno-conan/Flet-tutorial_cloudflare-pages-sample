import flet as ft


def main(page: ft.Page):
    page.title = "Check Storage"
    client_values = ft.Ref[ft.Column]()
    session_values = ft.Ref[ft.Column]()

    def set_client_storage_values(e):
        # strings
        page.client_storage.set("key", "value")
        # numbers, booleans
        page.client_storage.set("number.setting", 12345)
        page.client_storage.set("bool_setting", True)
        # lists
        page.client_storage.set("favorite_colors", ["read", "green", "blue"])

    def check_client_storage_values(e):
        client_values.current.controls.clear()
        client_values.current.controls.append(
            ft.Text(
                f"client storage values : {page.client_storage.get('key')}")
        )
        page.update()

    def set_session_storage_values(e):
        # strings
        page.session.set("key", "value")

        # numbers, booleans
        page.session.set("number.setting", 12345)
        page.session.set("bool_setting", True)

        # lists
        page.session.set("favorite_colors", ["read", "green", "blue"])

    def check_session_storage_values(e):
        session_values.current.controls.clear()
        session_values.current.controls.append(
            ft.Text(
                f"session storage values : {page.session.get('key')}")
        )
        page.update()

    page.add(
        # client
        ft.Text(value="Client Storage Part", size=28, color="red"),
        ft.ElevatedButton("Set!",
                          on_click=set_client_storage_values
                          ),
        ft.ElevatedButton("check!",
                          on_click=check_client_storage_values),
        ft.Column(ref=client_values),
        # session
        ft.Text(value="Session Storage Part", size=28, color="blue"),
        ft.ElevatedButton("Set!",
                          on_click=set_session_storage_values),
        ft.ElevatedButton("check!",
                          on_click=check_session_storage_values),
        ft.Column(ref=session_values),
    )


ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
