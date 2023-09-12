import flet as ft
from Chatgpt import Generate
from time import sleep

def main(page:ft.Page):
    page.title = "Explain the Concept"
    page.horizontal_alignment = "center"
    page.theme_mode = "dark"
    page.window_max_width = 850
    page.window_max_height = 900
    page.window_width = 700
    page.window_height = 650
    page.padding = 10
    page.auto_scroll = False
    page.scroll = True
    page.scroll_to_async = True
    page.bgcolor = "#1a001a"
    page.set_clipboard = True
    page.get_clipboard = True

    page.fonts={
        "Orbitron":"fonts\\Orbitron-Bold.ttf"
    }

    

    def Generate_answer(e):
        answer = str(Generate(user_input.value).send_response())
        output_Text.value = "Generating"
        output_Text.update()
        sleep(0.5)
        output_Text.value += "."
        output_Text.update()
        sleep(0.5)
        output_Text.value += "."
        output_Text.update()
        sleep(0.5)
        output_Text.value += "."
        output_Text.update()

        sleep(1)

        output_Text.value = "\n\n\t\t\t"
        for x in answer:
            output_Text.value += x + "_"
            sleep(0.01)
            output_Text.value = output_Text.value[:-1]
            output_Text.update()

    logo = ft.Image(src="Logo\\favicon.png",width=100)
    user_input = ft.TextField(hint_text="Enter any sentence...",border_radius=10,width=450,autofocus=True)
    generate_btn = ft.ElevatedButton("Generate",bgcolor="#1a0f00",on_click=Generate_answer)
    output_Text = ft.Text(value=" ",font_family="Titllium",size=15,weight=90,max_lines=900,selectable=True)

    page.add(
        logo,
        ft.Row([user_input,generate_btn],alignment="center"),
        output_Text,
        ft.Row([ft.Text("Developed by ",font_family="Orbitron",text_align="center"),ft.Image(src="./logo//GitHub.png",width=40),ft.Text("Shri556",font_family="Orbitron",size=20)],alignment="center",vertical_alignment="bottom"),
    )

ft.app(target=main,assets_dir="assets")
