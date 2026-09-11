settings = {
    "theme": "light",
    "language": "en"
}

def change_settings(settings,theme,language):
    settings["theme"] = theme
    settings["language"] = language

change_settings(settings,"dark","fr")
print(settings)