import pandas as pd
import itertools
import Preprocessing_and_encoding as preprocess
import Budget_division as bd
import random
import Helper as hp
import matplotlib.pyplot as plt
import seaborn as sns
from collections import OrderedDict
import collections
from LDP_Energy_code.Post_processing import Statistical_analysis as sa
import json

# # user1_65

A1_1 = pd.read_csv(
    "/Data/IDEAL/room_and_appliance_sensors/sensordata/home65_hall731_sensor8861_electric-appliance_vacuumcleaner.csv",
    header=None)
A2_1 = pd.read_csv(
    "/Data/IDEAL/room_and_appliance_sensors/sensordata/home65_kitchen733_sensor3109_electric-appliance_kettle.csv",
    header=None)
A4_1 = pd.read_csv(
    "/Data/IDEAL/room_and_appliance_sensors/sensordata/home65_kitchen733_sensor3111_electric-appliance_dishwasher.csv",
    header=None)
A7_1 = pd.read_csv(
    "/Data/IDEAL/room_and_appliance_sensors/sensordata/home65_kitchen733_sensor3110_electric-appliance_washingmachine.csv",
    header=None)

# user2_House96
A1_2 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home96_hall998_sensor11255_electric-appliance_vacuumcleaner.csv", header=None)
A2_2 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home96_kitchen999_sensor9110_electric-appliance_kettle.csv", header=None)
A3_2 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home96_kitchen999_sensor9111_electric-appliance_microwave.csv", header=None)
A4_2 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home96_kitchen999_sensor9116_electric-appliance_dishwasher.csv", header=None)
A6_2 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home96_kitchen999_sensor9608_electric-appliance_fridgefreezer.csv", header=None)
A7_2 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home96_kitchen999_sensor11254_electric-appliance_washingmachine.csv", header=None)

# user3_House136
A1_3 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home136_hall1287_sensor9275_electric-appliance_vacuumcleaner.csv", header=None)
A2_3 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home136_kitchen1294_sensor21311_electric-appliance_kettle.csv", header=None)
A9_3 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home136_kitchen1294_sensor9273_electric-appliance_fridge.csv", header=None)
A8_3 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home136_outside1291_sensor9274_electric-appliance_freezer.csv", header=None)
A3_3 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home136_kitchen1294_sensor21312_electric-appliance_microwave.csv", header=None)
A4_3 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home136_kitchen1294_sensor9475_electric-appliance_dishwasher.csv", header=None)
A10_3 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home136_outside1291_sensor9272_electric-appliance_dehumidifier.csv", header=None)
A7_3 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home136_kitchen1294_sensor9471_electric-appliance_washingmachine.csv", header=None)

# user4_House61
A2_4 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home61_kitchen695_sensor1967_electric-appliance_kettle.csv", header=None)
A3_4 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home61_kitchen695_sensor1971_electric-appliance_microwave.csv", header=None)
A4_4 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home61_kitchen695_sensor1969_electric-appliance_dishwasher.csv", header=None)
A1_4 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home65_hall735_sensor5306_electric-appliance_vacuumcleaner.csv", header=None)
A8_4 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home136_kitchen1294_sensor9270_electric-appliance_freezer.csv", header=None)

# user5_House62
A1_5 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home62_kitchen710_sensor2400_electric-appliance_vacuumcleaner.csv", header=None)
A2_5 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home62_kitchen710_sensor1780_electric-appliance_kettle.csv", header=None)
A4_5 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home62_kitchen710_sensor1782_electric-appliance_dishwasher.csv", header=None)
A6_5 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home62_kitchen710_sensor1779_electric-appliance_fridgefreezer.csv", header=None)
A7_5 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home62_kitchen710_sensor1781_electric-appliance_washingmachine.csv", header=None)

# user6_House63
A1_6 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home63_kitchen720_sensor3980_electric-appliance_vacuumcleaner.csv", header=None)
A2_6 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home63_kitchen720_sensor3760_electric-appliance_kettle.csv", header=None)
A3_6 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home63_kitchen720_sensor2269_electric-appliance_microwave.csv", header=None)
A4_6 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home63_kitchen720_sensor2270_electric-appliance_dishwasher.csv", header=None)
A7_6 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home63_kitchen720_sensor2268_electric-appliance_washingmachinetumbledrier.csv", header=None)

# user7_House90
A2_7 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home90_kitchen957_sensor4858_electric-appliance_kettle.csv", header=None)
A3_7 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home90_kitchen957_sensor4859_electric-appliance_microwave.csv", header=None)
A6_7 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home90_kitchen957_sensor4860_electric-appliance_fridgefreezer.csv", header=None)
A1_7 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home65_bedroom736_sensor15880_electric-appliance_vacuumcleaner.csv", header=None)

# user8_House212
A5_8 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home212_hall1968_sensor18049_electric-appliance_tumbledrier.csv", header=None)
A7_8 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home212_hall1968_sensor15873_electric-appliance_washingmachine.csv", header=None)
A13_8 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home212_kitchen1973_sensor16943_electric-appliance_toaster.csv", header=None)
A4_8 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home212_kitchen1973_sensor16939_electric-appliance_dishwasher.csv", header=None)
A6_8 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home212_kitchen1973_sensor15874_electric-appliance_fridgefreezer.csv", header=None)
A2_8 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home136_kitchen1294_sensor9271_electric-appliance_kettle.csv", header=None)

# user9_House128
A1_9 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home128_hall1250_sensor10802_electric-appliance_vacuumcleaner.csv", header=None)
A2_9 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home128_kitchen1253_sensor9251_electric-appliance_kettle.csv", header=None)
A6_9 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home128_kitchen1253_sensor9252_electric-appliance_fridgefreezer.csv", header=None)
A11_9 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home128_kitchen1253_sensor10803_electric-appliance_other.csv", header=None)
A13_9 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home128_kitchen1253_sensor10924_electric-appliance_toaster.csv", header=None)
A3_9 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home128_kitchen1253_sensor10805_electric-appliance_microwave.csv", header=None)
A7_9 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                   "home128_kitchen1253_sensor13307_electric-appliance_washingmachine.csv", header=None)

# user10_House139
A1_10 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home139_hall1313_sensor14580_electric-appliance_vacuumcleaner.csv", header=None)
A13_10 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home139_kitchen1315_sensor13310_electric-appliance_toaster.csv", header=None)
A4_10 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home139_kitchen1315_sensor13304_electric-appliance_dishwasher.csv", header=None)
A6_10 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home139_kitchen1315_sensor13305_electric-appliance_fridgefreezer.csv", header=None)
A7_10 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home139_kitchen1315_sensor13306_electric-appliance_washingmachine.csv", header=None)

# user11_House145
A1_11 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home145_hall1345_sensor16526_electric-appliance_vacuumcleaner.csv", header=None)
A6_11 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home145_kitchen1349_sensor13736_electric-appliance_fridgefreezer.csv", header=None)
A7_11 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home145_kitchen1349_sensor14222_electric-appliance_washingmachine.csv", header=None)
A3_11 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home136_kitchen1294_sensor9269_electric-appliance_microwave.csv", header=None)

# user12_House146
A1_12 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home146_hall1352_sensor15550_electric-appliance_vacuumcleaner.csv", header=None)
A2_12 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home146_kitchen1355_sensor15432_electric-appliance_kettle.csv", header=None)
A3_12 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home146_kitchen1355_sensor15431_electric-appliance_microwave.csv", header=None)
A7_12 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home146_kitchen1355_sensor15885_electric-appliance_washingmachinetumbledrier.csv", header=None)

# user13_House162
A1_13 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home162_hall1618_sensor15133_electric-appliance_vacuumcleaner.csv", header=None)
A2_13 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home162_kitchen1622_sensor15130_electric-appliance_kettle.csv", header=None)
A6_13 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home162_kitchen1622_sensor15131_electric-appliance_fridgefreezer.csv", header=None)
A7_13 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home162_kitchen1622_sensor15132_electric-appliance_washingmachinetumbledrier.csv", header=None)
A15_13 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home227_livingroom2098_sensor18441_electric-appliance_electricheater.csv", header=None)

# user14_House169
A1_14 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home169_hall1551_sensor13370_electric-appliance_vacuumcleaner.csv", header=None)
A11_14 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home169_bedroom1547_sensor13185_electric-appliance_other.csv", header=None)
A12_14 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home169_kitchen1542_sensor13826_electric-appliance_grill.csv", header=None)
A13_14 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home169_kitchen1542_sensor13192_electric-appliance_toaster.csv", header=None)
A3_14 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home169_kitchen1542_sensor13184_electric-appliance_microwave.csv", header=None)
A4_14 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home169_kitchen1542_sensor13187_electric-appliance_dishwasher.csv", header=None)
A6_14 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home169_kitchen1542_sensor13188_electric-appliance_fridgefreezer.csv", header=None)
A7_14 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home169_kitchen1542_sensor13186_electric-appliance_washingmachinetumbledrier.csv", header=None)
A15_14 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home169_diningroom1543_sensor13183_electric-appliance_electricheater.csv", header=None)

# user15_House227
A1_15 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home227_hall2099_sensor16091_electric-appliance_vacuumcleaner.csv", header=None)
A2_15 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home227_kitchen2103_sensor18035_electric-appliance_kettle.csv", header=None)
A13_15 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home227_kitchen2103_sensor16079_electric-appliance_toaster.csv", header=None)
A3_15 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home227_kitchen2103_sensor18031_electric-appliance_microwave.csv", header=None)
A7_15 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home227_kitchen2103_sensor16060_electric-appliance_washingmachine.csv", header=None)
A15_15 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home227_livingroom2098_sensor16441_electric-appliance_electricheater.csv", header=None)

# user16_House231
A1_16 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home231_hall2140_sensor18909_electric-appliance_vacuumcleaner.csv", header=None)
A2_16 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home231_kitchen2147_sensor18900_electric-appliance_kettle.csv", header=None)
A9_16 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home231_kitchen2147_sensor18901_electric-appliance_fridge.csv", header=None)
A13_16 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home231_kitchen2147_sensor18914_electric-appliance_toaster.csv", header=None)
A3_16 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home231_kitchen2147_sensor18899_electric-appliance_microwave.csv", header=None)
A4_16 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home231_kitchen2147_sensor18902_electric-appliance_dishwasher.csv", header=None)
A7_16 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home231_kitchen2147_sensor19709_electric-appliance_washingmachine.csv", header=None)

# user17_House259
A1_17 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home259_hall2485_sensor31450_electric-appliance_vacuumcleaner.csv", header=None)
A8_17 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home259_other2488_sensor31348_electric-appliance_freezer.csv", header=None)
A5_17 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home259_other2488_sensor31444_electric-appliance_tumbledrier.csv", header=None)
A6_17 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home259_other2488_sensor31346_electric-appliance_fridgefreezer.csv", header=None)
A2_17 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home259_kitchenliving2487_sensor31359_electric-appliance_kettle.csv", header=None)
A13_17 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home259_kitchenliving2487_sensor31347_electric-appliance_toaster.csv", header=None)
A3_17 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home259_kitchenliving2487_sensor31436_electric-appliance_microwave.csv", header=None)
A4_17 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home259_kitchenliving2487_sensor31349_electric-appliance_dishwasher.csv", header=None)

# user18_House262
A1_18 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home262_hall2404_sensor19566_electric-appliance_vacuumcleaner.csv", header=None)
A2_18 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home262_kitchen2414_sensor19565_electric-appliance_kettle.csv", header=None)
A13_18 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home262_kitchen2414_sensor19564_electric-appliance_toaster.csv", header=None)
A6_18 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home262_kitchen2414_sensor19563_electric-appliance_fridgefreezer.csv", header=None)
A7_18 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home227_kitchen2103_sensor18029_electric-appliance_washingmachine.csv", header=None)

# user19_House268
A1_19 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home268_hall2465_sensor21708_electric-appliance_vacuumcleaner.csv", header=None)
A2_19 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home268_kitchen2471_sensor21532_electric-appliance_kettle.csv", header=None)
A13_19 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home268_kitchen2471_sensor21620_electric-appliance_toaster.csv", header=None)
A3_19 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home268_kitchen2471_sensor21534_electric-appliance_microwave.csv", header=None)
A6_19 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home268_kitchen2471_sensor21533_electric-appliance_fridgefreezer.csv", header=None)
A7_19 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home268_kitchen2471_sensor21624_electric-appliance_washingmachine.csv", header=None)

# user20_House328
A1_20 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home328_hall2976_sensor31009_electric-appliance_vacuumcleaner.csv", header=None)
A2_20 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home328_kitchen2980_sensor31003_electric-appliance_kettle.csv", header=None)
A13_20 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home328_kitchen2980_sensor31004_electric-appliance_toaster.csv", header=None)
A3_20 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home328_kitchen2980_sensor31014_electric-appliance_microwave.csv", header=None)
A6_20 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home328_kitchen2980_sensor31005_electric-appliance_fridgefreezer.csv", header=None)

# user21_House105
A2_21 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home105_kitchen1110_sensor5283_electric-appliance_kettle.csv", header=None)
A3_21 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home105_kitchen1110_sensor5286_electric-appliance_microwave.csv", header=None)
A4_21 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home105_kitchen1110_sensor5287_electric-appliance_dishwasher.csv", header=None)
A6_21 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home105_kitchen1110_sensor5284_electric-appliance_fridgefreezer.csv", header=None)
A1_21 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home105_kitchen1110_sensor7932_electric-appliance_vacuumcleaner.csv", header=None)
A7_21 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home105_kitchen1110_sensor5285_electric-appliance_washingmachine.csv", header=None)

# user22_House106
A2_22 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home106_kitchen1085_sensor5210_electric-appliance_kettle.csv", header=None)
A3_22 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home106_kitchen1085_sensor5211_electric-appliance_microwave.csv", header=None)
A6_22 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home106_kitchen1085_sensor5213_electric-appliance_fridgefreezer.csv", header=None)
A7_22 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home106_kitchen1085_sensor5212_electric-appliance_washingmachine.csv", header=None)
A13_22 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home227_kitchen2103_sensor18030_electric-appliance_toaster.csv", header=None)

# user23_House238
A11_23 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home238_kitchen2202_sensor21684_electric-appliance_other.csv", header=None)
A13_23 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home238_kitchen2202_sensor21681_electric-appliance_toaster.csv", header=None)
A3_23 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home238_kitchen2202_sensor21682_electric-appliance_microwave.csv", header=None)
A4_23 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home238_kitchen2202_sensor21703_electric-appliance_dishwasher.csv", header=None)
A1_23 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home238_kitchen2202_sensor22085_electric-appliance_vacuumcleaner.csv", header=None)
A7_23 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home238_kitchen2202_sensor21683_electric-appliance_washingmachine.csv", header=None)

# user24_House168
A2_24 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home168_kitchen1534_sensor12521_electric-appliance_kettle.csv", header=None)
A13_24 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home168_kitchen1534_sensor12589_electric-appliance_toaster.csv", header=None)
A3_24 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home168_kitchen1534_sensor12522_electric-appliance_microwave.csv", header=None)
A5_24 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home168_kitchen1534_sensor12524_electric-appliance_tumbledrier.csv", header=None)
A6_24 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home168_kitchen1534_sensor12523_electric-appliance_fridgefreezer.csv", header=None)
A1_24 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home168_kitchen1534_sensor12525_electric-appliance_vacuumcleaner.csv", header=None)
A7_24 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home168_kitchen1534_sensor12520_electric-appliance_washingmachinetumbledrier.csv", header=None)

# user25_House208
A2_25 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home208_kitchen1935_sensor18019_electric-appliance_kettle.csv", header=None)
A11_25 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home208_kitchen1935_sensor18020_electric-appliance_appliance.csv", header=None)
A6_25 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home208_kitchen1935_sensor18018_electric-appliance_fridgefreezer.csv", header=None)
A7_25 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home208_kitchen1935_sensor18021_electric-appliance_washingmachine.csv", header=None)

# user26_House242
A9_26 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home242_utility2241_sensor18810_electric-appliance_fridge.csv", header=None)
A13_26 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home242_kitchen2240_sensor18821_electric-appliance_toaster.csv", header=None)
A8_26 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home242_utility2241_sensor18808_electric-appliance_freezer.csv", header=None)
A3_26 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home242_utility2241_sensor18818_electric-appliance_microwave.csv", header=None)
A4_26 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home242_kitchen2240_sensor18822_electric-appliance_dishwasher.csv", header=None)
A7_26 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home242_utility2241_sensor18809_electric-appliance_washingmachine.csv", header=None)
A1_26 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home242_diningroom2246_sensor18830_electric-appliance_vacuumcleaner.csv", header=None)

# user27_House264
A2_27 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home264_kitchen2437_sensor20764_electric-appliance_kettle.csv", header=None)
A13_27 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home264_kitchen2437_sensor20824_electric-appliance_toaster.csv", header=None)
A3_27 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home264_kitchen2437_sensor20775_electric-appliance_microwave.csv", header=None)
A4_27 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home264_kitchen2437_sensor20737_electric-appliance_dishwasher.csv", header=None)
A1_27 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home264_kitchen2437_sensor20825_electric-appliance_vacuumcleaner.csv", header=None)
A7_27 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home264_kitchen2437_sensor20738_electric-appliance_washingmachine.csv", header=None)
A15_27 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home264_livingroom2446_sensor20763_electric-appliance_electricheater.csv", header=None)

# user28_House266
A9_28 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home266_kitchen2454_sensor18425_electric-appliance_fridge.csv", header=None)
A3_28 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home266_kitchen2454_sensor18412_electric-appliance_microwave.csv", header=None)
A11_28 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home266_kitchen2454_sensor18910_electric-appliance_appliance.csv", header=None)
A6_28 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home266_kitchen2454_sensor18444_electric-appliance_fridgefreezer.csv", header=None)
A7_28 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home266_kitchen2454_sensor18547_electric-appliance_washingmachinetumbledrier.csv", header=None)
A1_28 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home266_livingroom2451_sensor18413_electric-appliance_vacuumcleaner.csv", header=None)

# user29_House276
A9_29 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home276_kitchen2561_sensor22068_electric-appliance_fridge.csv", header=None)
A2_29 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home276_kitchen2561_sensor22075_electric-appliance_kettle.csv", header=None)
A13_29 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home276_kitchen2561_sensor22066_electric-appliance_toaster.csv", header=None)
A3_29 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home276_kitchen2561_sensor22076_electric-appliance_microwave.csv", header=None)
A7_29 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home276_kitchen2561_sensor22067_electric-appliance_washingmachinetumbledrier.csv", header=None)
A11_29 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home276_diningroom2560_sensor22069_electric-appliance_other.csv", header=None)
A8_29 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home276_diningroom2560_sensor22065_electric-appliance_freezer.csv", header=None)

# user30_House311
A2_30 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home311_kitchen2857_sensor31432_electric-appliance_kettle.csv", header=None)
A13_30 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home311_kitchen2857_sensor31433_electric-appliance_toaster.csv", header=None)
A4_30 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home311_kitchen2857_sensor31437_electric-appliance_dishwasher.csv", header=None)
A6_30 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home311_kitchen2857_sensor31431_electric-appliance_fridgefreezer.csv", header=None)
A1_30 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home311_kitchen2857_sensor31438_electric-appliance_vacuumcleaner.csv", header=None)
A7_30 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home311_kitchen2857_sensor31435_electric-appliance_washingmachine.csv", header=None)

# user31_House171
A13_31 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home171_kitchen1565_sensor12110_electric-appliance_toaster.csv", header=None)
A3_31 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home171_kitchen1565_sensor11688_electric-appliance_microwave.csv", header=None)
A6_31 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home171_kitchen1565_sensor11686_electric-appliance_fridgefreezer.csv", header=None)
A7_31 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home171_kitchen1565_sensor11687_electric-appliance_washingmachine.csv", header=None)
A2_31 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home168_kitchen1534_sensor21309_electric-appliance_kettle.csv", header=None)

# user32_House225
A13_32 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home225_kitchen2086_sensor17458_electric-appliance_toaster.csv", header=None)
A8_32 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home225_kitchen2086_sensor17459_electric-appliance_freezer.csv", header=None)
A6_32 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home225_kitchen2086_sensor17465_electric-appliance_fridgefreezer.csv", header=None)
A11_32 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home225_livingroom2082_sensor17457_electric-appliance_other.csv", header=None)

# user33_House263
A13_33 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home263_kitchen2430_sensor21723_electric-appliance_toaster.csv", header=None)
A3_33 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home263_kitchen2430_sensor18178_electric-appliance_microwave.csv", header=None)
A4_33 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home263_kitchen2430_sensor18319_electric-appliance_dishwasher.csv", header=None)
A14_33 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home263_kitchen2430_sensor18177_electric-appliance_electricoven.csv", header=None)
A6_33 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home263_kitchen2430_sensor18176_electric-appliance_fridgefreezer.csv", header=None)
A7_33 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home263_utility2428_sensor18320_electric-appliance_washingmachinetumbledrier.csv", header=None)

# user34_House228
A11_34 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home228_kitchen2109_sensor17384_electric-appliance_appliance.csv", header=None)
A3_34 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home228_kitchen2109_sensor17400_electric-appliance_microwave.csv", header=None)
A6_34 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home228_kitchen2109_sensor17330_electric-appliance_fridgefreezer.csv", header=None)
A7_34 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home228_kitchen2109_sensor17329_electric-appliance_washingmachine.csv", header=None)

# user35_House175
A10_35 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home175_bedroom1641_sensor11553_electric-appliance_dehumidifier.csv", header=None)
A2_35 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home175_diningroom1636_sensor11549_electric-appliance_kettle.csv", header=None)
A13_35 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home175_diningroom1636_sensor11550_electric-appliance_toaster.csv", header=None)
A3_35 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home175_diningroom1636_sensor11548_electric-appliance_microwave.csv", header=None)
A4_35 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home175_diningroom1636_sensor11551_electric-appliance_dishwasher.csv", header=None)
A6_35 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home175_diningroom1636_sensor11522_electric-appliance_fridgefreezer.csv", header=None)
A1_35 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home175_livingroom1635_sensor11552_electric-appliance_vacuumcleaner.csv", header=None)
A7_35 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home175_diningroom1636_sensor11523_electric-appliance_washingmachine.csv", header=None)

# user36_House140
A6_36 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home140_kitchen1317_sensor10457_electric-appliance_fridgefreezer.csv", header=None)
A15_36 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home140_livingroom1318_sensor10464_electric-appliance_electricheater.csv", header=None)

# user37_House255
A1_37 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home255_utility2363_sensor21619_electric-appliance_vacuumcleaner.csv", header=None)
A7_37 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home255_utility2363_sensor21618_electric-appliance_washingmachine.csv", header=None)
A13_37 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                     "home255_kitchenliving2357_sensor21462_electric-appliance_toaster.csv", header=None)
A3_37 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home255_kitchenliving2357_sensor20661_electric-appliance_microwave.csv", header=None)
A4_37 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home255_kitchenliving2357_sensor21186_electric-appliance_dishwasher.csv", header=None)
A6_37 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home255_kitchenliving2357_sensor21457_electric-appliance_fridgefreezer.csv", header=None)

# user38_House73
A1_38 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home227_hall2099_sensor31451_electric-appliance_vacuumcleaner.csv", header=None)
A2_38 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home73_kitchenliving781_sensor4077_electric-appliance_kettle.csv", header=None)
A6_38 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home73_kitchenliving781_sensor4079_electric-appliance_fridgefreezer.csv", header=None)
A7_38 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home73_kitchenliving781_sensor4078_electric-appliance_washingmachine.csv", header=None)

# user39_House249
A2_39 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home249_kitchenliving2305_sensor18366_electric-appliance_kettle.csv", header=None)
A3_39 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home249_kitchenliving2305_sensor18410_electric-appliance_microwave.csv", header=None)
A4_39 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home249_kitchenliving2305_sensor18541_electric-appliance_dishwasher.csv", header=None)
A6_39 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home249_kitchenliving2305_sensor18363_electric-appliance_fridgefreezer.csv", header=None)
A7_39 = pd.read_csv("/Data/IDEAL/room_and_appliance_sensors/sensordata/" +
                    "home249_kitchenliving2305_sensor18362_electric-appliance_washingmachinetumbledrier.csv",
                    header=None)

appliance_list = [A1_1, A2_1, A4_1, A7_1, A1_2, A2_2, A3_2, A4_2, A6_2, A7_2, A1_3, A2_3, A9_3, A8_3, A3_3, A4_3, A10_3,
                  A7_3, A2_4, A3_4, A4_4, A1_4, A8_4, A1_5, A2_5, A4_5, A6_5, A7_5, A1_6, A2_6, A3_6, A4_6, A7_6, A2_7,
                  A3_7, A6_7, A1_7, A5_8, A7_8, A13_8, A4_8, A6_8, A2_8, A1_9, A2_9, A6_9, A11_9, A13_9, A3_9, A7_9,
                  A1_10, A13_10, A4_10, A6_10, A7_10, A1_11, A6_11, A7_11, A3_11, A1_12, A2_12, A3_12, A7_12, A1_13,
                  A2_13, A6_13, A7_13, A15_13, A1_14, A11_14, A12_14, A13_14, A3_14, A4_14, A6_14, A7_14, A15_14, A1_15,
                  A2_15, A13_15, A3_15, A7_15, A15_15, A1_16, A2_16, A9_16, A13_16, A3_16, A4_16, A7_16, A1_17, A8_17,
                  A5_17, A6_17, A2_17, A13_17, A3_17, A4_17, A1_18, A2_18, A13_18, A6_18, A7_18, A1_19, A2_19, A13_19,
                  A3_19, A6_19, A7_19, A1_20, A2_20, A13_20, A3_20, A6_20, A2_21, A3_21, A4_21, A6_21, A1_21, A7_21,
                  A2_22, A3_22, A6_22, A7_22, A13_22, A11_23, A13_23, A3_23, A4_23, A1_23, A7_23, A2_24, A13_24, A3_24,
                  A5_24, A6_24, A1_24, A7_24, A2_25, A11_25, A6_25, A7_25, A9_26, A13_26, A8_26, A3_26, A4_26, A7_26,
                  A1_26, A2_27, A13_27, A3_27, A4_27, A1_27, A7_27, A15_27, A9_28, A3_28, A11_28, A6_28, A7_28, A1_28,
                  A9_29, A2_29, A13_29, A3_29, A7_29, A11_29, A8_29, A2_30, A13_30, A4_30, A6_30, A1_30, A7_30, A13_31,
                  A3_31, A6_31, A7_31, A2_31, A13_32, A8_32, A6_32, A11_32, A13_33, A3_33, A4_33, A14_33, A6_33, A7_33,
                  A11_34, A3_34, A6_34, A7_34, A10_35, A2_35, A13_35, A3_35, A4_35, A6_35, A1_35, A7_35, A6_36, A15_36,
                  A1_37, A7_37, A13_37, A3_37, A4_37, A6_37, A1_38, A2_38, A6_38, A7_38, A2_39, A3_39, A4_39, A6_39,
                  A7_39]
appliance_list_copy = [A1_1, A2_1, A4_1, A7_1, A1_2, A2_2, A3_2, A4_2, A6_2, A7_2, A1_3, A2_3, A9_3, A8_3, A3_3, A4_3,
                       A10_3, A7_3, A2_4, A3_4, A4_4, A1_4, A8_4, A1_5, A2_5, A4_5, A6_5, A7_5, A1_6, A2_6, A3_6, A4_6,
                       A7_6, A2_7, A3_7, A6_7, A1_7, A5_8, A7_8, A13_8, A4_8, A6_8, A2_8, A1_9, A2_9, A6_9, A11_9,
                       A13_9, A3_9, A7_9, A1_10, A13_10, A4_10, A6_10, A7_10, A1_11, A6_11, A7_11, A3_11, A1_12, A2_12,
                       A3_12, A7_12, A1_13, A2_13, A6_13, A7_13, A15_13, A1_14, A11_14, A12_14, A13_14, A3_14, A4_14,
                       A6_14, A7_14, A15_14, A1_15, A2_15, A13_15, A3_15, A7_15, A15_15, A1_16, A2_16, A9_16, A13_16,
                       A3_16, A4_16, A7_16, A1_17, A8_17, A5_17, A6_17, A2_17, A13_17, A3_17, A4_17, A1_18, A2_18,
                       A13_18, A6_18, A7_18, A1_19, A2_19, A13_19, A3_19, A6_19, A7_19, A1_20, A2_20, A13_20, A3_20,
                       A6_20, A2_21, A3_21, A4_21, A6_21, A1_21, A7_21, A2_22, A3_22, A6_22, A7_22, A13_22, A11_23,
                       A13_23, A3_23, A4_23, A1_23, A7_23, A2_24, A13_24, A3_24, A5_24, A6_24, A1_24, A7_24, A2_25,
                       A11_25, A6_25, A7_25, A9_26, A13_26, A8_26, A3_26, A4_26, A7_26, A1_26, A2_27, A13_27, A3_27,
                       A4_27, A1_27, A7_27, A15_27, A9_28, A3_28, A11_28, A6_28, A7_28, A1_28, A9_29, A2_29, A13_29,
                       A3_29, A7_29, A11_29, A8_29, A2_30, A13_30, A4_30, A6_30, A1_30, A7_30, A13_31, A3_31, A6_31,
                       A7_31, A2_31, A13_32, A8_32, A6_32, A11_32, A13_33, A3_33, A4_33, A14_33, A6_33, A7_33, A11_34,
                       A3_34, A6_34, A7_34, A10_35, A2_35, A13_35, A3_35, A4_35, A6_35, A1_35, A7_35, A6_36, A15_36,
                       A1_37, A7_37, A13_37, A3_37, A4_37, A6_37, A1_38, A2_38, A6_38, A7_38, A2_39, A3_39, A4_39,
                       A6_39, A7_39]
appliance_names = ['A1_1', 'A2_1', 'A4_1', 'A7_1', 'A1_2', 'A2_2', 'A3_2', 'A4_2', 'A6_2', 'A7_2', 'A1_3', 'A2_3',
                   'A9_3', 'A8_3', 'A3_3', 'A4_3', 'A10_3', 'A7_3', 'A2_4', 'A3_4', 'A4_4', 'A1_4', 'A8_4', 'A1_5',
                   'A2_5', 'A4_5', 'A6_5', 'A7_5', 'A1_6', 'A2_6', 'A3_6', 'A4_6', 'A7_6', 'A2_7', 'A3_7', 'A6_7',
                   'A1_7', 'A5_8', 'A7_8', 'A13_8', 'A4_8', 'A6_8', 'A2_8', 'A1_9', 'A2_9', 'A6_9', 'A11_9', 'A13_9',
                   'A3_9', 'A7_9', 'A1_10', 'A13_10', 'A4_10', 'A6_10', 'A7_10', 'A1_11', 'A6_11', 'A7_11', 'A3_11',
                   'A1_12', 'A2_12', 'A3_12', 'A7_12', 'A1_13', 'A2_13', 'A6_13', 'A7_13', 'A15_13', 'A1_14', 'A11_14',
                   'A12_14', 'A13_14', 'A3_14', 'A4_14', 'A6_14', 'A7_14', 'A15_14', 'A1_15', 'A2_15', 'A13_15',
                   'A3_15',
                   'A7_15', 'A15_15', 'A1_16', 'A2_16', 'A9_16', 'A13_16', 'A3_16', 'A4_16', 'A7_16', 'A1_17', 'A8_17',
                   'A5_17', 'A6_17', 'A2_17', 'A13_17', 'A3_17', 'A4_17', 'A1_18', 'A2_18', 'A13_18', 'A6_18', 'A7_18',
                   'A1_19', 'A2_19', 'A13_19', 'A3_19', 'A6_19', 'A7_19', 'A1_20', 'A2_20', 'A13_20', 'A3_20', 'A6_20',
                   'A2_21', 'A3_21', 'A4_21', 'A6_21', 'A1_21', 'A7_21', 'A2_22', 'A3_22', 'A6_22', 'A7_22', 'A13_22',
                   'A11_23', 'A13_23', 'A3_23', 'A4_23', 'A1_23', 'A7_23', 'A2_24', 'A13_24', 'A3_24', 'A5_24', 'A6_24',
                   'A1_24', 'A7_24', 'A2_25', 'A11_25', 'A6_25', 'A7_25', 'A9_26', 'A13_26', 'A8_26', 'A3_26', 'A4_26',
                   'A7_26', 'A1_26', 'A2_27', 'A13_27', 'A3_27', 'A4_27', 'A1_27', 'A7_27', 'A15_27', ' ' 'A9_28',
                   'A3_28',
                   'A11_28', 'A6_28', 'A7_28', 'A1_28', 'A9_29', 'A2_29', 'A13_29', 'A3_29', 'A7_29', 'A11_29', 'A8_29',
                   'A2_30', 'A13_30', 'A4_30', 'A6_30', 'A1_30', 'A7_30', 'A13_31', 'A3_31', 'A6_31', 'A7_31', 'A2_31',
                   'A13_32', 'A8_32', 'A6_32', 'A11_32', 'A13_33', 'A3_33', 'A4_33', 'A14_33', 'A6_33', 'A7_33',
                   'A11_34',
                   'A3_34', 'A6_34', 'A7_34', 'A10_35', 'A2_35', 'A13_35', 'A3_35', 'A4_35', 'A6_35', 'A1_35', 'A7_35',
                   'A6_36', 'A15_36', 'A1_37', 'A7_37', 'A13_37', 'A3_37', 'A4_37', 'A6_37', 'A1_38', 'A2_38', 'A6_38',
                   'A7_38', 'A2_39', 'A3_39', 'A4_39', 'A6_39', 'A7_39']

user_list = []
no_of_users = 10
n = len(appliance_list)  # Number of appliances
# Input: granularity levels with ranges(d-levels)
domain = ['l10', 'l9', 'l8', 'l7', 'l6', 'l5', 'l4', 'l3', 'l2', 'l1']

applaince_energy_list = []
appliance_energy_dict = {}
# Tuning parameters
epsilon = 5  # 0 < ε ≤ 10
alpha = 10  # 4-10
window_size = 3
window_appliance_data = []
window_binary_array_data = []
user_appliance_list = {}
user_actual_value = {}
user_perturbed_data_list = {}
user_true_level_list = {}
user_perturbed_level_list = {}
appliance_level_list = {}
appliance_level_count = {}
appliance_level_average = {}
appliance_level_max = {}
appliance_perturbed_level_count = {}
appliance_perturbed_level_average = {}
appliance_perturbed_level_max = {}


def energy_per_day_calculation(df):
    """The data can be measured in different time intervals. But, generally data is shared with service providers once in a day.
    This method computes the energy consumption per day
    :param df: Dataframe that contains all data
    :return consumption_per_day: energy consumption of appliances per day
    """
    df[0] = pd.to_datetime(df[0])  # convert column to datetime object
    df.set_index(0, inplace=True)  # set column 'date' to index

    consumption_per_day = round(df.resample('D').sum() / 1000, 2)  # note!! (Sum) # D =>> for day sample
    return consumption_per_day


# Create user list
for i in range(no_of_users):
    user_list.append('U' + str(i + 1))

# Calculating energy per day as we send the data once a day
for i in range(len(appliance_list)):
    consumption_per_day = energy_per_day_calculation(appliance_list[i])
    var_name = 'appliance_energy{}'.format(i)
    # Assign a value to the variable
    globals()[var_name] = []

    for j in range(len(consumption_per_day)):
        globals()[var_name].append(consumption_per_day[1][j])  # Energy consumption for an appliance in a day
    applaince_energy_list.append(globals()[var_name])  # Energy consumption for 7 days for all the appliances

A1 = list(itertools.chain(
    applaince_energy_list[0], applaince_energy_list[4], applaince_energy_list[10], applaince_energy_list[16],
    applaince_energy_list[21], applaince_energy_list[23], applaince_energy_list[28], applaince_energy_list[36],
    applaince_energy_list[39], applaince_energy_list[43], applaince_energy_list[46], applaince_energy_list[47],
    applaince_energy_list[50], applaince_energy_list[51], applaince_energy_list[55], applaince_energy_list[59],
    applaince_energy_list[63], applaince_energy_list[67], applaince_energy_list[68], applaince_energy_list[69],
    applaince_energy_list[70], applaince_energy_list[71], applaince_energy_list[76], applaince_energy_list[77],
    applaince_energy_list[79], applaince_energy_list[82], applaince_energy_list[83], applaince_energy_list[86],
    applaince_energy_list[90], applaince_energy_list[95], applaince_energy_list[98], applaince_energy_list[100],
    applaince_energy_list[103], applaince_energy_list[105], applaince_energy_list[109], applaince_energy_list[111],
    applaince_energy_list[118], applaince_energy_list[124], applaince_energy_list[125], applaince_energy_list[126],
    applaince_energy_list[129], applaince_energy_list[132], applaince_energy_list[136], applaince_energy_list[139],
    applaince_energy_list[143], applaince_energy_list[148], applaince_energy_list[150], applaince_energy_list[153],
    applaince_energy_list[155], applaince_energy_list[158], applaince_energy_list[161], applaince_energy_list[164],
    applaince_energy_list[167], applaince_energy_list[170], applaince_energy_list[173], applaince_energy_list[175],
    applaince_energy_list[180], applaince_energy_list[183], applaince_energy_list[184], applaince_energy_list[187],
    applaince_energy_list[190], applaince_energy_list[194], applaince_energy_list[196], applaince_energy_list[200],
    applaince_energy_list[203], applaince_energy_list[204], applaince_energy_list[206], applaince_energy_list[210]

))
A2 = list(itertools.chain(
applaince_energy_list[1],  applaince_energy_list[5],  applaince_energy_list[11],  applaince_energy_list[18],  applaince_energy_list[24],  applaince_energy_list[29],  applaince_energy_list[33],  applaince_energy_list[42],  applaince_energy_list[44],  applaince_energy_list[60],  applaince_energy_list[64],  applaince_energy_list[78],  applaince_energy_list[84],  applaince_energy_list[94],  applaince_energy_list[99],  applaince_energy_list[104],  applaince_energy_list[110],  applaince_energy_list[114],  applaince_energy_list[120],  applaince_energy_list[131],  applaince_energy_list[138],  applaince_energy_list[149],  applaince_energy_list[163],  applaince_energy_list[169],  applaince_energy_list[179],  applaince_energy_list[195],  applaince_energy_list[211],  applaince_energy_list[214]
))

A3= list(itertools.chain(
applaince_energy_list[6],  applaince_energy_list[14],  applaince_energy_list[19],  applaince_energy_list[30],  applaince_energy_list[34],  applaince_energy_list[48],  applaince_energy_list[58],  applaince_energy_list[61],  applaince_energy_list[72],  applaince_energy_list[80],  applaince_energy_list[87],  applaince_energy_list[96],  applaince_energy_list[106],  applaince_energy_list[112],  applaince_energy_list[115],  applaince_energy_list[121],  applaince_energy_list[127],  applaince_energy_list[133],  applaince_energy_list[145],  applaince_energy_list[151],  applaince_energy_list[157],  applaince_energy_list[165],  applaince_energy_list[176],  applaince_energy_list[185],  applaince_energy_list[191],  applaince_energy_list[197],  applaince_energy_list[207],  applaince_energy_list[215]
))

A4 = list(itertools.chain(
applaince_energy_list[2],
 applaince_energy_list[7],
 applaince_energy_list[15],
 applaince_energy_list[20],
 applaince_energy_list[25],
 applaince_energy_list[31],
 applaince_energy_list[40],
 applaince_energy_list[52],
 applaince_energy_list[73],
 applaince_energy_list[88],
 applaince_energy_list[97],
 applaince_energy_list[116],
 applaince_energy_list[128],
 applaince_energy_list[146],
 applaince_energy_list[152],
 applaince_energy_list[171],
 applaince_energy_list[186],
 applaince_energy_list[198],
 applaince_energy_list[208],
 applaince_energy_list[216]

))

A5 = list(itertools.chain(
applaince_energy_list[37],
 applaince_energy_list[92],
 applaince_energy_list[134]
))

A6 = list(itertools.chain(
applaince_energy_list[8],
 applaince_energy_list[26],
 applaince_energy_list[35],
 applaince_energy_list[41],
 applaince_energy_list[45],
 applaince_energy_list[53],
 applaince_energy_list[56],
 applaince_energy_list[65],
 applaince_energy_list[74],
 applaince_energy_list[93],
 applaince_energy_list[101],
 applaince_energy_list[107],
 applaince_energy_list[113],
 applaince_energy_list[117],
 applaince_energy_list[122],
 applaince_energy_list[135],
 applaince_energy_list[140],
 applaince_energy_list[159],
 applaince_energy_list[172],
 applaince_energy_list[177],
 applaince_energy_list[182],
 applaince_energy_list[188],
 applaince_energy_list[192],
 applaince_energy_list[199],
 applaince_energy_list[202],
 applaince_energy_list[209],
 applaince_energy_list[212],
 applaince_energy_list[217]
))

A7 = list(itertools.chain(
applaince_energy_list[3],
 applaince_energy_list[9],
 applaince_energy_list[17],
 applaince_energy_list[27],
 applaince_energy_list[32],
 applaince_energy_list[38],
 applaince_energy_list[49],
 applaince_energy_list[54],
 applaince_energy_list[57],
 applaince_energy_list[62],
 applaince_energy_list[66],
 applaince_energy_list[75],
 applaince_energy_list[81],
 applaince_energy_list[89],
 applaince_energy_list[102],
 applaince_energy_list[108],
 applaince_energy_list[119],
 applaince_energy_list[123],
 applaince_energy_list[130],
 applaince_energy_list[137],
 applaince_energy_list[141],
 applaince_energy_list[147],
 applaince_energy_list[154],
 applaince_energy_list[160],
 applaince_energy_list[166],
 applaince_energy_list[174],
 applaince_energy_list[178],
 applaince_energy_list[189],
 applaince_energy_list[193],
 applaince_energy_list[201],
 applaince_energy_list[205],
 applaince_energy_list[213],
 applaince_energy_list[218]
))

A8 = list(itertools.chain(
applaince_energy_list[13],
 applaince_energy_list[22],
 applaince_energy_list[91],
 applaince_energy_list[144],
 applaince_energy_list[168],
 applaince_energy_list[181]
))

A9 = list(itertools.chain(
applaince_energy_list[12],
 applaince_energy_list[85],
 applaince_energy_list[142],
 applaince_energy_list[156],
 applaince_energy_list[162]
))

A10 = list(itertools.chain(
applaince_energy_list[16], applaince_energy_list[194]
))

A11 = list(itertools.chain(
applaince_energy_list[139],
 applaince_energy_list[158],
 applaince_energy_list[167],
 applaince_energy_list[183],
 applaince_energy_list[190]
))

A12 = list(itertools.chain(
applaince_energy_list[70]
))

A13 = list(itertools.chain(
applaince_energy_list[39],
 applaince_energy_list[47],
 applaince_energy_list[51],
 applaince_energy_list[71],
 applaince_energy_list[79],
 applaince_energy_list[86],
 applaince_energy_list[95],
 applaince_energy_list[100],
 applaince_energy_list[105],
 applaince_energy_list[111],
 applaince_energy_list[124],
 applaince_energy_list[126],
 applaince_energy_list[132],
 applaince_energy_list[143],
 applaince_energy_list[150],
 applaince_energy_list[164],
 applaince_energy_list[170],
 applaince_energy_list[175],
 applaince_energy_list[180],
 applaince_energy_list[184],
 applaince_energy_list[196],
 applaince_energy_list[206]
))

A14 = list(itertools.chain(
applaince_energy_list[187]
))

A15 = list(itertools.chain(
applaince_energy_list[67],
 applaince_energy_list[76],
 applaince_energy_list[82],
 applaince_energy_list[155],
 applaince_energy_list[203]
))

appliances = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15]

# Normal distribution
import numpy as np
from scipy.stats import truncnorm
def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

for i in range(len(appliances)):
    needed = 30000-len(appliances[i])
    X = get_truncated_normal(mean=np.average(appliances[i]), sd=np.var(appliances[i]), low=min(appliances[i]), upp=max(appliances[i]))
    appliance1 = X.rvs(needed)
    appliances[i] = appliances[i] + list(appliance1)


user_appliance_energy_dict_days = {}
count = 0
for k in range(1000):
    day_data = {}
    for i in range(30):
        appliances_data = {}
        for j in range(len(appliances)):
            appliances_data["A"+ str(j+1)] = appliances[j][count]
        count = count + 1
        day_data["day" + str(i + 1)] = appliances_data
    user_appliance_energy_dict_days["U" + str(k + 1)] = day_data

no_of_users = 1000
# Input: granularity levels with ranges(d-levels)
appliance_list = appliance_list = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
                                   'A10', 'A11', 'A12', 'A13', 'A14', 'A15']
n = len(appliance_list) # Number of appliances
no_of_days = 30
no_of_appliances = 15
sensitivity = 2*n



domain = ['l10', 'l9', 'l8', 'l7', 'l6', 'l5', 'l4', 'l3', 'l2', 'l1' ]
range_levels = {
  "l1": "0-10",
  "l2": "10-30",
  "l3": "30-60",
  "l4": "60-100",
  "l5": "100-200",
  "l6": "200-300",
  "l7": "300-500",
  "l8": "500-800",
  "l9": "800-1000",
  "l10": "1000"
}

#Tuning parameters
epsilon = 15 # 0 < ε ≤ 10
# alpha = 10 # 4-10
window_size = 2
user_appliance_list = {}
user_actual_value = {}
user_perturbed_data_list = {}
user_true_level_list = {}
user_perturbed_level_list = {}
appliance_level_list = {}
appliance_level_count = {}
appliance_level_average = {}
appliance_level_max = {}
appliance_perturbed_level_count = {}
appliance_perturbed_level_average = {}
appliance_perturbed_level_max = {}

for k in range(no_of_users):
      # Appliance_energy dictionary per day for 30 days. In appliance_energy_dict_days, key specifies the day
    # (day 1, 2, 3...), and value represents the dictionary of  appliances with their energy consumption for the day.
    window_appliance_data = []
    window_binary_array_data = []
    appliance_energy_dict_days = user_appliance_energy_dict_days['U' + str(k+1)]

    #Encode the energy data into energy levels (granularity levels)
    for key, value in appliance_energy_dict_days.items():
        true_energy_levels_dict = preprocess.create_appliance_energy_encoding(appliance_energy_dict_days[key], range_levels)
        # Declare, l = (d*n); // d- number of granular levels, n- number of appliances
        # Generate a long binary string B with the length of l by merging the binary arrays
        binary_array = []
        for i in range(len(true_energy_levels_dict)):
            binary_array.append(list(true_energy_levels_dict.values())[i])
        binary_array = np.array(binary_array).flatten()

        window_appliance_data.append(true_energy_levels_dict.values())
        window_binary_array_data.append(binary_array)

    perturbed_data_window_lbd = []
    perturbed_data_window_lba = []
    #LBD parameters
    previously_spent_epsilons = []
    previously_released = []
    published_epsilons_et2 = []
    #LBA parameters
    nullify = []
    window_iterate = 0
    actual_data = []
    current_timestamp = 0
    previously_spent_et2_lba = []
    # Adding the encoded data in a sliding window format for our calculation
    for window in hp.sliding_window(window_binary_array_data, window_size):
        current_window = window
        window_iterate = window_iterate + 1
        if window_iterate == 1:
            current_window = current_window
        else:
            a = current_window[window_size-1]
            current_window = []
            current_window.append(a.tolist())
            previously_spent_et2.pop(0)
            # nullify.pop(0)

        actual_data.append(current_window)

        # Adaptive Budget division
        # Generate a random number to determine which sampling timestamp to select for use in the LDP sampling method.
        sampling_timestamp = random.randint(window_iterate, (window_iterate+window_size)-1)
        perturbed_data_sampling = []

        for i in range(len(current_window)):

            # LDP Budget Distribution method
            perturbed_data_lbd, previously_spent_et2 = bd.local_budget_distribution(window_size, current_window[i],
                                                                                     previously_spent_epsilons, published_epsilons_et2,
                                                                                     previously_released, sensitivity, epsilon)
            perturbed_data_window_lbd.append(perturbed_data_lbd)
            previously_released = perturbed_data_lbd

    user_perturbed_data_list['U' + str(k+1) ] = perturbed_data_window_lbd
    user_actual_value['U' + str(k+1)] = window_binary_array_data

    day_data ={}
    #Appliances true energy levels
    for i in range (no_of_days):
        a = hp.true_data_appliance_level(user_actual_value['U' + str(k+1) ][i], len(domain), n)
        day_data["day" + str(i + 1)] = a
    user_true_level_list['U' + str(k+1)] = day_data

    day_perturbed_data = {}
    #Appliances perturbed energy levels
    for i in range(no_of_days):
        b = hp.perturbed_data_appliance_level(user_perturbed_data_list['U' + str(k+1) ][i], len(domain), n)
        day_perturbed_data["day" + str(i + 1)] = b
    user_perturbed_level_list['U' + str(k+1)] = day_perturbed_data

final_output = {}
output_day_appliance = {}
#For true value aggregation and level mapping
for w in range(no_of_days):
    for i in range(n):
        all_user_appliance_true_values = []
        for j in range(no_of_users):
            appliance_data = user_true_level_list['U' + str(j+1)]['day' + str(w+1)]['A' + str(i+1)]
            all_user_appliance_true_values.append(appliance_data)
        levels =  hp.frequency_estimation_true_value(all_user_appliance_true_values, domain)
        counter = collections.Counter(levels)
        appliance_level_list['A' + str(i + 1)] = levels
        appliance_level_count['A' + str(i + 1)] = counter
        appliance_level_count = {k: dict(v) for k, v in appliance_level_count.items()}
        # Calculating average energy consumption: True value
        appliance_average, max_value = hp.average_calculation(counter, range_levels, domain)
        appliance_level_average['A' + str(i + 1)] = appliance_average
        appliance_level_max['A' + str(i + 1)] = max_value

    appliance_level_count_full = {}
    for j in range(len(appliance_level_count)):
        level_dic = {}
        diff = list(set(domain).symmetric_difference(set(list(list(appliance_level_count.values())[j].keys()))))
        for k in range(len(list(list(appliance_level_count.values())[j].keys()))):
            level_dic[int(list(list(appliance_level_count.values())[j].keys())[k].replace('l', ''))] \
                = list(list(appliance_level_count.values())[j].values())[k]
        for i in range(len(diff)):
            level_dic[int(diff[i].replace('l', ''))] = 0
        level_dic = OrderedDict(sorted(level_dic.items()))

        title_actual = 'Histogram of actual values: Appliance' + str(j + 1)

        ax = sns.barplot(x=list(level_dic.keys()), y=list(level_dic.values()))
        ax.set(xlabel='Energy levels', ylabel='No. of users', title=title_actual)
        # saveTitle = 'plotAc' + str(j + 1) + '.pdf'
        plt.show()

        appliance_level_count_full['A' + str(j + 1)] = level_dic

    # Plotting the histogram: true values
    # sns.histplot(data = appliance_level_list['A1'], kde=True)
    # plt.show()

    #For perturbed value aggregation
    for i in range (n):
        all_user_appliance_perturbed_values = []
        for j in range (no_of_users):
            appliance_data = user_perturbed_level_list['U' + str(j+1)]['day' + str(w+1)]['A' + str(i+1) ]
            all_user_appliance_perturbed_values.append(appliance_data)
        # Estimation and aggregation
        estimated_answers = hp.estimation_from_perturbed_value(all_user_appliance_perturbed_values, The, sensitivity)
        levels_with_count = dict(zip(domain, estimated_answers))
        res = OrderedDict(reversed(list(levels_with_count.items())))
        res_new = {}
        for j in range(len(list(res.keys()))):
            res_new[j + 1] = list(res.values())[j]
        appliance_perturbed_level_count['A' + str(i + 1)] = res_new
        # Plotting the histogram: perturbed values
        title_perturbed = 'Histogram of perturbed values: Appliance' + str(i + 1)
        ax = sns.barplot(x=list(res_new.keys()), y=list(res_new.values()))
        ax.set(xlabel='Energy levels', ylabel='No. of users', title=title_perturbed)
        # savepTitle = 'plotPer' + str(i + 1) + '.pdf'
        plt.show()


    output_appliance = {}

# Statistical analysis I: mean/variance analysis
    for k in range(len(appliance_list)):
        overall_values = {}
        a = appliance_level_count_full['A' + str(k+1)]
        temp_actual = list(a.keys())
        count_actual = list(a.values())
        final_actual_data = []

        for i in range(len(temp_actual)):
            for j in range (count_actual[i]):
                final_actual_data.append(temp_actual[i])

        b = appliance_perturbed_level_count['A' + str(k+1)]
        temp = list(b.keys())
        counte = list(b.values())
        final_perturbed_data = []

        for i in range(len(temp)):
            for j in range (counte[i]):
                final_perturbed_data.append(temp[i])

        mean_actual = sum(final_actual_data) / len(final_actual_data)
        variance_actual = sum((i - mean_actual) ** 2 for i in final_actual_data) / len(final_actual_data)

        mean = sum(final_perturbed_data) / len(final_perturbed_data)
        variance = sum((i - mean) ** 2 for i in final_perturbed_data) / len(final_perturbed_data)


        kw_stat, kw_pval = sa.kruskal_wallis_test(count_actual, counte)
        overall_values['kw_pval'] = kw_pval
        output_appliance['A' + str(k + 1)] = overall_values

    final_output['D' + str(w + 1)] = output_appliance

avg_pvalue = []
for i in range (no_of_appliances):
    sum_val = 0
    for k in range (no_of_days):
        sum_val = sum_val + final_output['D' + str(k + 1)]['A' + str(i+1)]['kw_pval']
    avg = sum_val/no_of_days
    avg_pvalue.append(avg)

x = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15']
ax = sns.lineplot(x=x, y=avg_pvalue)
ax.set(xlabel='Appliance', ylabel='pvalue', title='similaity')
plt.show()

with open('convert.txt', 'w') as convert_file:
    convert_file.write(json.dumps(final_output))


# Method comparison
avg_pvalue_lbu = []
for i in range (no_of_appliances):
    sum_val = 0
    for k in range (no_of_days):
        sum_val = sum_val + final_output['D' + str(k + 1)]['A' + str(i+1)]['kw_pval']
    avg = sum_val/no_of_days
    avg_pvalue_lbu.append(avg)

x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
ax = sns.lineplot(x=x, y=avg_pvalue_lbu)
ax.set(xlabel='Appliances', ylabel='p value', title='LBU method')
plt.savefig('realLBU.pdf')

avg_pvalue_lsp = []
for i in range (no_of_appliances):
    sum_val = 0
    for k in range (no_of_days):
        sum_val = sum_val + final_output['D' + str(k + 1)]['A' + str(i+1)]['kw_pval']
    avg = sum_val/no_of_days
    avg_pvalue_lsp.append(avg)

x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
ax = sns.lineplot(x=x, y=avg_pvalue_lsp)
ax.set(xlabel='Appliances', ylabel='p value', title='LSP method')
plt.savefig('realLSP.pdf')

avg_pvalue_lbd = []
for i in range (no_of_appliances):
    sum_val = 0
    for k in range (no_of_days):
        sum_val = sum_val + final_output['D' + str(k + 1)]['A' + str(i+1)]['kw_pval']
    avg = sum_val/no_of_days
    avg_pvalue_lbd.append(avg)

x = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
ax = sns.lineplot(x=x, y=avg_pvalue_lbd)
ax.set(xlabel='Appliances', ylabel='p value', title='LBD method')
plt.savefig('realLBD.pdf')
