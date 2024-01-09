import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class PopcatGame(App):

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # สร้าง Label สำหรับแสดงคะแนน
        self.score_label = Label(text="Score: 0", font_size=24)
        layout.add_widget(self.score_label)

        # สร้าง Button สำหรับเล่นเกม
        self.pop_button = Button(text="Pop!", size_hint=(1, 0.5))
        self.pop_button.bind(on_press=self.pop_cat)
        layout.add_widget(self.pop_button)

        return layout

    def pop_cat(self, instance):
        # เพิ่มคะแนนเมื่อกดปุ่ม
        self.score += 1
        self.score_label.text = f"Score: {self.score}"

        # เปลี่ยนสีของปุ่มเพื่อแสดงให้เห็นว่ามีการกด
        self.pop_button.background_color = (0, 1, 0, 1)  # สีเขียว
        self.pop_button.text = "Popped!"

        # สั่งให้ปุ่มกลับมาสีเดิมและข้อความเดิมหลังจาก 0.5 วินาที
        Clock.schedule_once(self.reset_button, 0.5)

    def reset_button(self, dt):
        self.pop_button.background_color = (1, 1, 1, 1)  # สีขาว
        self.pop_button.text = "Pop!"

if __name__ == "__main__":
    PopcatGame().run()