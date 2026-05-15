
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

class AymanNexusApp(MDApp):
    def build(self):
        # إعدادات الألوان (نيون غيمرز)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        
        screen = MDScreen()
        layout = BoxLayout(orientation='vertical', padding=dp(40), spacing=dp(20))

        # عنوان التطبيق
        layout.add_widget(MDLabel(
            text="AYMAN AI NEXUS",
            halign="center",
            font_style="H4",
            theme_text_color="Primary"
        ))

        layout.add_widget(MDLabel(
            text="Pexil Xbox Platform",
            halign="center",
            font_style="Subtitle1",
            theme_text_color="Secondary"
        ))

        # حقل إدخال الكود
        self.key_input = MDTextField(
            hint_text="أدخل كود التفعيل (ayman-xxxx)",
            mode="rectangle",
            size_hint_x=None,
            width=dp(250),
            pos_hint={"center_x": .5}
        )
        layout.add_widget(self.key_input)

        # زر التفعيل
        activate_btn = MDRaisedButton(
            text="تفعيل النظام",
            pos_hint={"center_x": .5},
            on_release=self.check_activation
        )
        layout.add_widget(activate_btn)

        screen.add_widget(layout)
        return screen

    def check_activation(self, instance):
        # نظام التحقق
        if self.key_input.text == "ayman-2026-X":
            self.key_input.helper_text = "تم التفعيل بنجاح!"
            self.key_input.error = False
        else:
            self.key_input.helper_text = "كود خاطئ، تواصل مع أيمن خطيب"
            self.key_input.error = True

if __name__ == "__main__":
    AymanNexusApp().run()
