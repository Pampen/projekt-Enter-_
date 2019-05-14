from tutorial import handleGreenHouse, handleOutside, handlePorch
from MainHall import handleMainHall
from greenDoor import handleBeach, handleCaptainsCabin, handleCellar, handleGate, handleShedFrontDoor, handleShed, handleBeachEastSide, handleShipwreck, handleLighthouse, handleLighthouseOutside, handleLighthouseTopFloor, handleOcean
from redDoor import handleUpperFloor, handleLivingRoom, handleKitchen, handleHall, handleBedroom, handleBasement, handleAttic
from pinkDoor import handleBabyRoom, handleCribRoom, handleMessyRoom, handleNursingRoom, handleStudyRoom, handleBabyRoomCrib, handleBabyRoomDoll, handleBabyRoomBlanket, handleBabyRoomPacifier, handleBabyRoomKey
from blueDoor import handleBlueCorridor1, handleBlueCorridor2, handleBlueCorridor3, handleBlueCorridor4, handleBlueCorridor5, handleBlueCorridor6, handleBlueCorridor7, handleBlueCorridor8, handleBlueCorridor9, handleBlueStart, handleBlueFinish, handleTorchRoom

levels = {
    'OUTSIDE': handleOutside,
    'GREENHOUSE': handleGreenHouse,
    'GREENHOUSE_LIGHT_ON': handleGreenHouse,
    'GREENHOUSE_LIGHT_AND_KEY_ON': handleGreenHouse,
    'PORCH': handlePorch,
    'MAIN_HALL': handleMainHall,
    'BEACH': handleBeach,
    'CAPTAINS_CABIN': handleCaptainsCabin,
    'CELLAR': handleCellar,
    'GATE': handleGate,
    'SHED_FRONT_DOOR': handleShedFrontDoor,
    'SHED': handleShed,
    'BEACH_EAST_SIDE': handleBeachEastSide,
    'SHIPWRECK': handleShipwreck,
    'LIGHTHOUSE_OUTSIDE': handleLighthouseOutside,
    'LIGHTHOUSE': handleLighthouse,
    'LIGHTHOUSE_TOP_FLOOR': handleLighthouseTopFloor,
    'LIVING_ROOM': handleLivingRoom,
    'KITCHEN': handleKitchen,
    'HALL': handleHall,
    'UPPER_FLOOR': handleUpperFloor,
    'BEDROOM': handleBedroom,
    'BASEMENT': handleBasement,
    'ATTIC': handleAttic,
    'CRIB_ROOM': handleCribRoom,
    'BABY_ROOM': handleBabyRoom,
    'NURSING_ROOM': handleNursingRoom,
    'STUDY_ROOM': handleStudyRoom,
    'MESSY_ROOM': handleMessyRoom,
    'BLUE_START': handleBlueStart,
    'BLUE_TORCH_ROOM': handleTorchRoom,
    'BLUE_CORRIDOR_1': handleBlueCorridor1,
    'BLUE_CORRIDOR_2': handleBlueCorridor2,
    'BLUE_CORRIDOR_3': handleBlueCorridor3,
    'BLUE_CORRIDOR_4': handleBlueCorridor4,
    'BLUE_CORRIDOR_5': handleBlueCorridor5,
    'BLUE_CORRIDOR_6': handleBlueCorridor6,
    'BLUE_CORRIDOR_7': handleBlueCorridor7,
    'BLUE_CORRIDOR_8': handleBlueCorridor8,
    'BLUE_CORRIDOR_9': handleBlueCorridor9,
    'BLUE_FINISH': handleBlueFinish,
    'LIVING_ROOMItem': handleKitchen,
    'BABYROOMCRIB' : handleBabyRoomCrib,
    'BABYROOMDOLL' : handleBabyRoomDoll,
    'BABYROOMBLANKET' : handleBabyRoomBlanket,
    'BABYROOMPACIFIER': handleBabyRoomPacifier,
    'BABYROOMKEY' : handleBabyRoomKey
}

def levelChecker(userInput, state):   
    level = state['level']
    return levels[level](userInput, state)