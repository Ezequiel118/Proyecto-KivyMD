from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:

    MDBoxLayout:
        orientation: "vertical"

        
        MDTopAppBar:
            title: "Plataforma de Cursos"

        
        ScrollView:
            MDList:

                OneLineAvatarIconListItem:
                    text: "Curso de Python"
                    IconRightWidget:
                        icon: "account-plus"
                        on_release: app.inscribirse("Python")

                OneLineAvatarIconListItem:
                    text: "Curso de HTML"
                    IconRightWidget:
                        icon: "account-plus"
                        on_release: app.inscribirse("HTML")

                OneLineAvatarIconListItem:
                    text: "Curso de CSS"
                    IconRightWidget:
                        icon: "account-plus"
                        on_release: app.inscribirse("CSS")

                OneLineAvatarIconListItem:
                    text: "Curso de JavaScript"
                    IconRightWidget:
                        icon: "account-plus"
                        on_release: app.inscribirse("JavaScript")

        MDRaisedButton:
            text: "Continuar"
            pos_hint: {"center_x": 0.5}
            on_release: app.continuar()
'''

class CursosApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def inscribirse(self, curso):
        print(f"Te inscribiste en {curso}")

    def continuar(self):
        print("Continuando al siguiente paso...")

if __name__ == "__main__":
    CursosApp().run()