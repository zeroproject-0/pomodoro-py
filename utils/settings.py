import os
import json


class Settings:
  __instance = None

  def __init__(self):
    if Settings.__instance is not None:
      print("This class is a singleton!")
    self.auto_hide_title_bar = True
    self.time = 1
    self.alway_on_top = False
    self.update_settings()

  @staticmethod
  def get_instance():
    if Settings.__instance is None:
      Settings.__instance = Settings()
    return Settings.__instance

  def update_settings(self):
    if os.path.exists("./settings.json"):
      with open("./settings.json", "r") as f:
        settings = json.load(f)
        self.auto_hide_title_bar = settings["auto_hide_title_bar"]
        self.time = settings["time"]
        self.alway_on_top = settings["alway_on_top"]

  def save(self):
    with open("settings.json", "w") as f:
      json.dump(self.__dict__, f)
