import pyautogui

while True:
    try:
        #battle = pyautogui.locateOnScreen('imgs/battle_region.png', confidence=0.8)
        #if battle != None:
        #    print(f"Regiao battle detectada - {battle}")

        #player = pyautogui.locateOnScreen('imgs/battle_player.png', confidence=0.8)
        #if player != None:
        #    print(f"Regiao player detectada - {player}")

        #minimap = pyautogui.locateOnScreen('imgs/minimap_region.png', confidence=0.8)
        #if minimap != None:
        #    print(f"Regiao minimap detectada - {minimap}")

        #ring = pyautogui.locateOnScreen('imgs/ring_region.png', confidence=0.8)
        #if ring != None:
        #    print(f"Regiao ring detectada - {ring}")

        barra = pyautogui.locateOnScreen('imgs/status/barra.png', confidence=0.8)
        if barra != None:
            print(f"Regiao barra detectada - {barra}")

    except pyautogui.ImageNotFoundException:
        print('ImageNotFoundException: image not found')

