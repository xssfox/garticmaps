Draws maps on gartic page for use in the flags game mode. `locator.png` is what is used to locate where the app should be drawing. `playarea.png` can be used for testing without needing the game running.

Warning: Do not use maps drawing on gartic.io for survey or navigation purposes. The maps aren't correctly projected and are basically squashed onto the play space.

Requirements
==
 - Python3
 - pyautogui
 - opencv-python


Shapefile
==
Not all countries are available because they get simplified to no shape as they are too small. 

Shapefile originally came from [arcgis hub](https://hub.arcgis.com/datasets/2b93b06dc0dc4e809d3c8db5cb96ba69_0?geometry=-82.266%2C-89.382%2C82.266%2C86.054) but was simplified using https://mapshaper.org and converted to GeoJSON