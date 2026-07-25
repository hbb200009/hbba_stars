import os
import json
import sys

class Config:
    def create_config():
        settings = {
          "Gems": 100,
          "Gold": 1000,
          "Tickets": 0,
          "Starpoints": 0,
          "BrawlBoxTokens": 1000,
          "BigBoxTokens": 100,
          "MenuTokens": 200,
          "Trophies": 0,
          "ExperiencePoints": 0,
          "BrawlerTrophies": 0,
          "BrawlerTrophiesForRank": 0,
          "BrawlerPowerLevel": 8,
          "BrawlerUpgradePoints": 0,
          "ThemeID": 11,
          "SupportedContentCreator": "HBBA2000",
          "ShowPacketsInLog": False,
          "Maintenance": False,
          "MaintenanceTime": 3600,
          "Patch": False,
          "PatchUrl": "http://192.168.0.103:8080/",
          "UpdateUrl": "https://github.com/PhoenixFire6879/Classic-Brawl"
}


        with open('config.json', 'w') as config_file:
            json.dump(settings, config_file)

    def GetValue():
      config_settings = {}

      Config_file = open('config.json', 'r')
      config_values = Config_file.read()

      config_settings = json.loads(config_values)
      return config_settings

