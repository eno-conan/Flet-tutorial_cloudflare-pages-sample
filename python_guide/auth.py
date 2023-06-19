import os

from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider
import flet as ft
import requests
import json

from dotenv import load_dotenv
load_dotenv()

def main(page: ft.Page):

    # Define Provider
    provider = GitHubOAuthProvider(
        client_id=os.getenv("GITHUB_CLIENT_ID"),
        client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
        redirect_url="http://localhost:8550/api/oauth/redirect",
    )

    def login_button_click(e):
        page.login(provider, scope=["public_repo"])

    def on_login(e: ft.LoginEvent):
        if not e.error:
            toggle_login_buttons()

    def logout_button_click(e):
        page.logout()

    def on_logout(e):
        toggle_login_buttons()

    def toggle_login_buttons():
        login_button.visible = page.auth is None
        logout_button.visible = page.auth is not None
        repos_button.visible = page.auth is not None
        page.update()

    def display_repos(e):
        headers = {"Authorization": "Bearer {}".format(page.auth.token.access_token)}
        repos_resp = requests.get("https://api.github.com/user/repos", headers=headers)
        user_repos = json.loads(repos_resp.text)
        for repo in user_repos:
            print(repo["full_name"])


    login_button = ft.ElevatedButton("Login with GitHub", on_click=login_button_click)
    logout_button = ft.ElevatedButton("Logout", on_click=logout_button_click)
    repos_button = ft.ElevatedButton("Show Repos", on_click=display_repos)
    toggle_login_buttons()
    page.on_login = on_login
    page.on_logout = on_logout
    # page.
    page.add(login_button, logout_button,repos_button)

ft.app(target=main, port=8550, view=ft.WEB_BROWSER)