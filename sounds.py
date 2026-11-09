from pygame import mixer

def load_sounds(keys):
    sounds = {}
    for key, filename in key.items():
        sounds[key] = mixer.Sound(f"assets/sound/{filename}")
    return sounds