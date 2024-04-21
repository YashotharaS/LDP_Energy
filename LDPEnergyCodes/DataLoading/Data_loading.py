# Real data loading
import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import datetime
import itertools

import sys
import os
import Benchmarking.LaplacianLDP as lap

current_folder = os.path.abspath(os.path.dirname(__file__))
# parent_folder = os.path.abspath(os.path.join(current_folder, '..'))
sys.path.append(current_folder)

import Data_augmentation as daug

no_of_users = 39
user_list = []
appliance_energy_list = []
appliance_energy_dict = {}
# Check the name of the variable
user_values = {}
user_list = []


def data_loading():
    # # user1_65
    A1_1 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/home65_hall731_sensor8861_electric-appliance_vacuumcleaner.csv",
        header=None)
    A2_1 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/home65_kitchen733_sensor3109_electric-appliance_kettle.csv",
        header=None)
    A4_1 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/home65_kitchen733_sensor3111_electric-appliance_dishwasher.csv",
        header=None)
    A7_1 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/home65_kitchen733_sensor3110_electric-appliance_washingmachine.csv",
        header=None)

    # user2_House96
    A1_2 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home96_hall998_sensor11255_electric-appliance_vacuumcleaner.csv", header=None)
    A2_2 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home96_kitchen999_sensor9110_electric-appliance_kettle.csv", header=None)
    A3_2 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home96_kitchen999_sensor9111_electric-appliance_microwave.csv", header=None)
    A4_2 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home96_kitchen999_sensor9116_electric-appliance_dishwasher.csv", header=None)
    A6_2 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home96_kitchen999_sensor9608_electric-appliance_fridgefreezer.csv", header=None)
    A7_2 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home96_kitchen999_sensor11254_electric-appliance_washingmachine.csv", header=None)

    # user3_House136
    A1_3 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home136_hall1287_sensor9275_electric-appliance_vacuumcleaner.csv", header=None)
    A2_3 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home136_kitchen1294_sensor21311_electric-appliance_kettle.csv", header=None)
    A9_3 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home136_kitchen1294_sensor9273_electric-appliance_fridge.csv", header=None)
    A8_3 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home136_outside1291_sensor9274_electric-appliance_freezer.csv", header=None)
    A3_3 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home136_kitchen1294_sensor21312_electric-appliance_microwave.csv", header=None)
    A4_3 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home136_kitchen1294_sensor9475_electric-appliance_dishwasher.csv", header=None)
    A10_3 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home136_outside1291_sensor9272_electric-appliance_dehumidifier.csv", header=None)
    A7_3 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home136_kitchen1294_sensor9471_electric-appliance_washingmachine.csv", header=None)

    # user4_House61
    A2_4 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home61_kitchen695_sensor1967_electric-appliance_kettle.csv", header=None)
    A3_4 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home61_kitchen695_sensor1971_electric-appliance_microwave.csv", header=None)
    A4_4 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home61_kitchen695_sensor1969_electric-appliance_dishwasher.csv", header=None)
    A1_4 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home65_hall735_sensor5306_electric-appliance_vacuumcleaner.csv", header=None)
    A8_4 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home136_kitchen1294_sensor9270_electric-appliance_freezer.csv", header=None)

    # user5_House62
    A1_5 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home62_kitchen710_sensor2400_electric-appliance_vacuumcleaner.csv", header=None)
    A2_5 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home62_kitchen710_sensor1780_electric-appliance_kettle.csv", header=None)
    A4_5 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home62_kitchen710_sensor1782_electric-appliance_dishwasher.csv", header=None)
    A6_5 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home62_kitchen710_sensor1779_electric-appliance_fridgefreezer.csv", header=None)
    A7_5 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home62_kitchen710_sensor1781_electric-appliance_washingmachine.csv", header=None)

    # user6_House63
    A1_6 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home63_kitchen720_sensor3980_electric-appliance_vacuumcleaner.csv", header=None)
    A2_6 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home63_kitchen720_sensor3760_electric-appliance_kettle.csv", header=None)
    A3_6 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home63_kitchen720_sensor2269_electric-appliance_microwave.csv", header=None)
    A4_6 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home63_kitchen720_sensor2270_electric-appliance_dishwasher.csv", header=None)
    A7_6 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home63_kitchen720_sensor2268_electric-appliance_washingmachinetumbledrier.csv", header=None)

    # user7_House90
    A2_7 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home90_kitchen957_sensor4858_electric-appliance_kettle.csv", header=None)
    A3_7 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home90_kitchen957_sensor4859_electric-appliance_microwave.csv", header=None)
    A6_7 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home90_kitchen957_sensor4860_electric-appliance_fridgefreezer.csv", header=None)
    A1_7 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home65_bedroom736_sensor15880_electric-appliance_vacuumcleaner.csv", header=None)

    # user8_House212
    A5_8 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home212_hall1968_sensor18049_electric-appliance_tumbledrier.csv", header=None)
    A7_8 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home212_hall1968_sensor15873_electric-appliance_washingmachine.csv", header=None)
    A13_8 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home212_kitchen1973_sensor16943_electric-appliance_toaster.csv", header=None)
    A4_8 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home212_kitchen1973_sensor16939_electric-appliance_dishwasher.csv", header=None)
    A6_8 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home212_kitchen1973_sensor15874_electric-appliance_fridgefreezer.csv", header=None)
    A2_8 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home136_kitchen1294_sensor9271_electric-appliance_kettle.csv", header=None)

    # user9_House128
    A1_9 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home128_hall1250_sensor10802_electric-appliance_vacuumcleaner.csv", header=None)
    A2_9 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home128_kitchen1253_sensor9251_electric-appliance_kettle.csv", header=None)
    A6_9 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home128_kitchen1253_sensor9252_electric-appliance_fridgefreezer.csv", header=None)
    A11_9 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home128_kitchen1253_sensor10803_electric-appliance_other.csv", header=None)
    A13_9 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home128_kitchen1253_sensor10924_electric-appliance_toaster.csv", header=None)
    A3_9 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home128_kitchen1253_sensor10805_electric-appliance_microwave.csv", header=None)
    A7_9 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home128_kitchen1253_sensor13307_electric-appliance_washingmachine.csv", header=None)

    # user10_House139
    # A1_10 = pd.read_csv(
    #     "/Data/room_and_appliance_sensors/sensordata/" +
    #     "home139_hall1313_sensor14580_electric-appliance_vacuumcleaner.csv", header=None)
    A13_10 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home139_kitchen1315_sensor13310_electric-appliance_toaster.csv", header=None)
    A4_10 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home139_kitchen1315_sensor13304_electric-appliance_dishwasher.csv", header=None)
    A6_10 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home139_kitchen1315_sensor13305_electric-appliance_fridgefreezer.csv", header=None)
    A7_10 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home139_kitchen1315_sensor13306_electric-appliance_washingmachine.csv", header=None)

    # user11_House145
    A1_11 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home145_hall1345_sensor16526_electric-appliance_vacuumcleaner.csv", header=None)
    A6_11 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home145_kitchen1349_sensor13736_electric-appliance_fridgefreezer.csv", header=None)
    A7_11 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home145_kitchen1349_sensor14222_electric-appliance_washingmachine.csv", header=None)
    A3_11 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home136_kitchen1294_sensor9269_electric-appliance_microwave.csv", header=None)

    # user12_House146
    A1_12 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home146_hall1352_sensor15550_electric-appliance_vacuumcleaner.csv", header=None)
    A2_12 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home146_kitchen1355_sensor15432_electric-appliance_kettle.csv", header=None)
    A3_12 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home146_kitchen1355_sensor15431_electric-appliance_microwave.csv", header=None)
    A7_12 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home146_kitchen1355_sensor15885_electric-appliance_washingmachinetumbledrier.csv", header=None)

    # user13_House162
    A1_13 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home162_hall1618_sensor15133_electric-appliance_vacuumcleaner.csv", header=None)
    A2_13 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home162_kitchen1622_sensor15130_electric-appliance_kettle.csv", header=None)
    A6_13 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home162_kitchen1622_sensor15131_electric-appliance_fridgefreezer.csv", header=None)
    A7_13 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home162_kitchen1622_sensor15132_electric-appliance_washingmachinetumbledrier.csv", header=None)
    A15_13 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home227_livingroom2098_sensor18441_electric-appliance_electricheater.csv", header=None)

    # user14_House169
    A1_14 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home169_hall1551_sensor13370_electric-appliance_vacuumcleaner.csv", header=None)
    A11_14 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home169_bedroom1547_sensor13185_electric-appliance_other.csv", header=None)
    A12_14 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home169_kitchen1542_sensor13826_electric-appliance_grill.csv", header=None)
    A13_14 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home169_kitchen1542_sensor13192_electric-appliance_toaster.csv", header=None)
    A3_14 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home169_kitchen1542_sensor13184_electric-appliance_microwave.csv", header=None)
    A4_14 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home169_kitchen1542_sensor13187_electric-appliance_dishwasher.csv", header=None)
    A6_14 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home169_kitchen1542_sensor13188_electric-appliance_fridgefreezer.csv", header=None)
    A7_14 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home169_kitchen1542_sensor13186_electric-appliance_washingmachinetumbledrier.csv", header=None)
    A15_14 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home169_diningroom1543_sensor13183_electric-appliance_electricheater.csv", header=None)

    # user15_House227
    A1_15 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home227_hall2099_sensor16091_electric-appliance_vacuumcleaner.csv", header=None)
    A2_15 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home227_kitchen2103_sensor18035_electric-appliance_kettle.csv", header=None)
    A13_15 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home227_kitchen2103_sensor16079_electric-appliance_toaster.csv", header=None)
    A3_15 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home227_kitchen2103_sensor18031_electric-appliance_microwave.csv", header=None)
    A7_15 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home227_kitchen2103_sensor16060_electric-appliance_washingmachine.csv", header=None)
    A15_15 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home227_livingroom2098_sensor16441_electric-appliance_electricheater.csv", header=None)

    # user16_House231
    A1_16 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home231_hall2140_sensor18909_electric-appliance_vacuumcleaner.csv", header=None)
    A2_16 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home231_kitchen2147_sensor18900_electric-appliance_kettle.csv", header=None)
    A9_16 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home231_kitchen2147_sensor18901_electric-appliance_fridge.csv", header=None)
    A13_16 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home231_kitchen2147_sensor18914_electric-appliance_toaster.csv", header=None)
    A3_16 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home231_kitchen2147_sensor18899_electric-appliance_microwave.csv", header=None)
    A4_16 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home231_kitchen2147_sensor18902_electric-appliance_dishwasher.csv", header=None)
    A7_16 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home231_kitchen2147_sensor19709_electric-appliance_washingmachine.csv", header=None)

    # user17_House259
    A1_17 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home259_hall2485_sensor31450_electric-appliance_vacuumcleaner.csv", header=None)
    A8_17 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home259_other2488_sensor31348_electric-appliance_freezer.csv", header=None)
    A5_17 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home259_other2488_sensor31444_electric-appliance_tumbledrier.csv", header=None)
    A6_17 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home259_other2488_sensor31346_electric-appliance_fridgefreezer.csv", header=None)
    A2_17 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home259_kitchenliving2487_sensor31359_electric-appliance_kettle.csv", header=None)
    A13_17 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home259_kitchenliving2487_sensor31347_electric-appliance_toaster.csv", header=None)
    A3_17 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home259_kitchenliving2487_sensor31436_electric-appliance_microwave.csv", header=None)
    A4_17 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home259_kitchenliving2487_sensor31349_electric-appliance_dishwasher.csv", header=None)

    # user18_House262
    A1_18 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home262_hall2404_sensor19566_electric-appliance_vacuumcleaner.csv", header=None)
    A2_18 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home262_kitchen2414_sensor19565_electric-appliance_kettle.csv", header=None)
    A13_18 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home262_kitchen2414_sensor19564_electric-appliance_toaster.csv", header=None)
    A6_18 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home262_kitchen2414_sensor19563_electric-appliance_fridgefreezer.csv", header=None)
    A7_18 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home227_kitchen2103_sensor18029_electric-appliance_washingmachine.csv", header=None)

    # user19_House268
    A1_19 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home268_hall2465_sensor21708_electric-appliance_vacuumcleaner.csv", header=None)
    A2_19 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home268_kitchen2471_sensor21532_electric-appliance_kettle.csv", header=None)
    A13_19 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home268_kitchen2471_sensor21620_electric-appliance_toaster.csv", header=None)
    A3_19 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home268_kitchen2471_sensor21534_electric-appliance_microwave.csv", header=None)
    A6_19 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home268_kitchen2471_sensor21533_electric-appliance_fridgefreezer.csv", header=None)
    A7_19 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home268_kitchen2471_sensor21624_electric-appliance_washingmachine.csv", header=None)

    # user20_House328
    A1_20 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home328_hall2976_sensor31009_electric-appliance_vacuumcleaner.csv", header=None)
    A2_20 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home328_kitchen2980_sensor31003_electric-appliance_kettle.csv", header=None)
    A13_20 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home328_kitchen2980_sensor31004_electric-appliance_toaster.csv", header=None)
    A3_20 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home328_kitchen2980_sensor31014_electric-appliance_microwave.csv", header=None)
    A6_20 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home328_kitchen2980_sensor31005_electric-appliance_fridgefreezer.csv", header=None)

    # user21_House105
    A2_21 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home105_kitchen1110_sensor5283_electric-appliance_kettle.csv", header=None)
    A3_21 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home105_kitchen1110_sensor5286_electric-appliance_microwave.csv", header=None)
    A4_21 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home105_kitchen1110_sensor5287_electric-appliance_dishwasher.csv", header=None)
    A6_21 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home105_kitchen1110_sensor5284_electric-appliance_fridgefreezer.csv", header=None)
    A1_21 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home105_kitchen1110_sensor7932_electric-appliance_vacuumcleaner.csv", header=None)
    A7_21 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home105_kitchen1110_sensor5285_electric-appliance_washingmachine.csv", header=None)

    # user22_House106
    A2_22 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home106_kitchen1085_sensor5210_electric-appliance_kettle.csv", header=None)
    A3_22 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home106_kitchen1085_sensor5211_electric-appliance_microwave.csv", header=None)
    A6_22 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home106_kitchen1085_sensor5213_electric-appliance_fridgefreezer.csv", header=None)
    A7_22 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home106_kitchen1085_sensor5212_electric-appliance_washingmachine.csv", header=None)
    A13_22 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home227_kitchen2103_sensor18030_electric-appliance_toaster.csv", header=None)

    # user23_House238
    A11_23 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home238_kitchen2202_sensor21684_electric-appliance_other.csv", header=None)
    A13_23 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home238_kitchen2202_sensor21681_electric-appliance_toaster.csv", header=None)
    A3_23 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home238_kitchen2202_sensor21682_electric-appliance_microwave.csv", header=None)
    A4_23 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home238_kitchen2202_sensor21703_electric-appliance_dishwasher.csv", header=None)
    A1_23 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home238_kitchen2202_sensor22085_electric-appliance_vacuumcleaner.csv", header=None)
    A7_23 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home238_kitchen2202_sensor21683_electric-appliance_washingmachine.csv", header=None)

    # user24_House168
    A2_24 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home168_kitchen1534_sensor12521_electric-appliance_kettle.csv", header=None)
    A13_24 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home168_kitchen1534_sensor12589_electric-appliance_toaster.csv", header=None)
    A3_24 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home168_kitchen1534_sensor12522_electric-appliance_microwave.csv", header=None)
    A5_24 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home168_kitchen1534_sensor12524_electric-appliance_tumbledrier.csv", header=None)
    A6_24 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home168_kitchen1534_sensor12523_electric-appliance_fridgefreezer.csv", header=None)
    A1_24 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home168_kitchen1534_sensor12525_electric-appliance_vacuumcleaner.csv", header=None)
    A7_24 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home168_kitchen1534_sensor12520_electric-appliance_washingmachinetumbledrier.csv", header=None)

    # user25_House208
    A2_25 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home208_kitchen1935_sensor18019_electric-appliance_kettle.csv", header=None)
    A11_25 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home208_kitchen1935_sensor18020_electric-appliance_appliance.csv", header=None)
    A6_25 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home208_kitchen1935_sensor18018_electric-appliance_fridgefreezer.csv", header=None)
    A7_25 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home208_kitchen1935_sensor18021_electric-appliance_washingmachine.csv", header=None)

    # user26_House242
    A9_26 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home242_utility2241_sensor18810_electric-appliance_fridge.csv", header=None)
    A13_26 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home242_kitchen2240_sensor18821_electric-appliance_toaster.csv", header=None)
    A8_26 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home242_utility2241_sensor18808_electric-appliance_freezer.csv", header=None)
    A3_26 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home242_utility2241_sensor18818_electric-appliance_microwave.csv", header=None)
    A4_26 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home242_kitchen2240_sensor18822_electric-appliance_dishwasher.csv", header=None)
    A7_26 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home242_utility2241_sensor18809_electric-appliance_washingmachine.csv", header=None)
    A1_26 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home242_diningroom2246_sensor18830_electric-appliance_vacuumcleaner.csv", header=None)

    # user27_House264
    A2_27 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home264_kitchen2437_sensor20764_electric-appliance_kettle.csv", header=None)
    A13_27 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home264_kitchen2437_sensor20824_electric-appliance_toaster.csv", header=None)
    A3_27 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home264_kitchen2437_sensor20775_electric-appliance_microwave.csv", header=None)
    A4_27 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home264_kitchen2437_sensor20737_electric-appliance_dishwasher.csv", header=None)
    A1_27 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home264_kitchen2437_sensor20825_electric-appliance_vacuumcleaner.csv", header=None)
    A7_27 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home264_kitchen2437_sensor20738_electric-appliance_washingmachine.csv", header=None)
    A15_27 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home264_livingroom2446_sensor20763_electric-appliance_electricheater.csv", header=None)

    # user28_House266
    A9_28 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home266_kitchen2454_sensor18425_electric-appliance_fridge.csv", header=None)
    A3_28 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home266_kitchen2454_sensor18412_electric-appliance_microwave.csv", header=None)
    A11_28 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home266_kitchen2454_sensor18910_electric-appliance_appliance.csv", header=None)
    A6_28 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home266_kitchen2454_sensor18444_electric-appliance_fridgefreezer.csv", header=None)
    A7_28 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home266_kitchen2454_sensor18547_electric-appliance_washingmachinetumbledrier.csv", header=None)
    A1_28 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home266_livingroom2451_sensor18413_electric-appliance_vacuumcleaner.csv", header=None)

    # user29_House276
    A9_29 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home276_kitchen2561_sensor22068_electric-appliance_fridge.csv", header=None)
    A2_29 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home276_kitchen2561_sensor22075_electric-appliance_kettle.csv", header=None)
    A13_29 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home276_kitchen2561_sensor22066_electric-appliance_toaster.csv", header=None)
    A3_29 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home276_kitchen2561_sensor22076_electric-appliance_microwave.csv", header=None)
    A7_29 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home276_kitchen2561_sensor22067_electric-appliance_washingmachinetumbledrier.csv", header=None)
    A11_29 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home276_diningroom2560_sensor22069_electric-appliance_other.csv", header=None)
    A8_29 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home276_diningroom2560_sensor22065_electric-appliance_freezer.csv", header=None)

    # user30_House311
    A2_30 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home311_kitchen2857_sensor31432_electric-appliance_kettle.csv", header=None)
    A13_30 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home311_kitchen2857_sensor31433_electric-appliance_toaster.csv", header=None)
    A4_30 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home311_kitchen2857_sensor31437_electric-appliance_dishwasher.csv", header=None)
    A6_30 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home311_kitchen2857_sensor31431_electric-appliance_fridgefreezer.csv", header=None)
    A1_30 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home311_kitchen2857_sensor31438_electric-appliance_vacuumcleaner.csv", header=None)
    A7_30 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home311_kitchen2857_sensor31435_electric-appliance_washingmachine.csv", header=None)

    # user31_House171
    A13_31 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home171_kitchen1565_sensor12110_electric-appliance_toaster.csv", header=None)
    A3_31 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home171_kitchen1565_sensor11688_electric-appliance_microwave.csv", header=None)
    A6_31 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home171_kitchen1565_sensor11686_electric-appliance_fridgefreezer.csv", header=None)
    A7_31 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home171_kitchen1565_sensor11687_electric-appliance_washingmachine.csv", header=None)
    A2_31 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home168_kitchen1534_sensor21309_electric-appliance_kettle.csv", header=None)

    # user32_House225
    A13_32 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home225_kitchen2086_sensor17458_electric-appliance_toaster.csv", header=None)
    A8_32 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home225_kitchen2086_sensor17459_electric-appliance_freezer.csv", header=None)
    A6_32 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home225_kitchen2086_sensor17465_electric-appliance_fridgefreezer.csv", header=None)
    A11_32 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home225_livingroom2082_sensor17457_electric-appliance_other.csv", header=None)

    # user33_House263
    A13_33 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home263_kitchen2430_sensor21723_electric-appliance_toaster.csv", header=None)
    A3_33 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home263_kitchen2430_sensor18178_electric-appliance_microwave.csv", header=None)
    A4_33 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home263_kitchen2430_sensor18319_electric-appliance_dishwasher.csv", header=None)
    A14_33 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home263_kitchen2430_sensor18177_electric-appliance_electricoven.csv", header=None)
    A6_33 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home263_kitchen2430_sensor18176_electric-appliance_fridgefreezer.csv", header=None)
    A7_33 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home263_utility2428_sensor18320_electric-appliance_washingmachinetumbledrier.csv", header=None)

    # user34_House228
    A11_34 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home228_kitchen2109_sensor17384_electric-appliance_appliance.csv", header=None)
    A3_34 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home228_kitchen2109_sensor17400_electric-appliance_microwave.csv", header=None)
    A6_34 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home228_kitchen2109_sensor17330_electric-appliance_fridgefreezer.csv", header=None)
    A7_34 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home228_kitchen2109_sensor17329_electric-appliance_washingmachine.csv", header=None)

    # user35_House175
    A10_35 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home175_bedroom1641_sensor11553_electric-appliance_dehumidifier.csv", header=None)
    A2_35 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home175_diningroom1636_sensor11549_electric-appliance_kettle.csv", header=None)
    A13_35 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home175_diningroom1636_sensor11550_electric-appliance_toaster.csv", header=None)
    A3_35 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home175_diningroom1636_sensor11548_electric-appliance_microwave.csv", header=None)
    A4_35 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home175_diningroom1636_sensor11551_electric-appliance_dishwasher.csv", header=None)
    A6_35 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home175_diningroom1636_sensor11522_electric-appliance_fridgefreezer.csv", header=None)
    A1_35 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home175_livingroom1635_sensor11552_electric-appliance_vacuumcleaner.csv", header=None)
    A7_35 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home175_diningroom1636_sensor11523_electric-appliance_washingmachine.csv", header=None)

    # user36_House140
    A6_36 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home140_kitchen1317_sensor10457_electric-appliance_fridgefreezer.csv", header=None)
    A15_36 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home140_livingroom1318_sensor10464_electric-appliance_electricheater.csv", header=None)

    # user37_House255
    A1_37 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home255_utility2363_sensor21619_electric-appliance_vacuumcleaner.csv", header=None)
    A7_37 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home255_utility2363_sensor21618_electric-appliance_washingmachine.csv", header=None)
    A13_37 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home255_kitchenliving2357_sensor21462_electric-appliance_toaster.csv", header=None)
    A3_37 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home255_kitchenliving2357_sensor20661_electric-appliance_microwave.csv", header=None)
    A4_37 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home255_kitchenliving2357_sensor21186_electric-appliance_dishwasher.csv", header=None)
    A6_37 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home255_kitchenliving2357_sensor21457_electric-appliance_fridgefreezer.csv", header=None)

    # user38_House73
    A1_38 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home227_hall2099_sensor31451_electric-appliance_vacuumcleaner.csv", header=None)
    A2_38 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home73_kitchenliving781_sensor4077_electric-appliance_kettle.csv", header=None)
    A6_38 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home73_kitchenliving781_sensor4079_electric-appliance_fridgefreezer.csv", header=None)
    A7_38 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home73_kitchenliving781_sensor4078_electric-appliance_washingmachine.csv", header=None)

    # user39_House249
    A2_39 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home249_kitchenliving2305_sensor18366_electric-appliance_kettle.csv", header=None)
    A3_39 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home249_kitchenliving2305_sensor18410_electric-appliance_microwave.csv", header=None)
    A4_39 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home249_kitchenliving2305_sensor18541_electric-appliance_dishwasher.csv", header=None)
    A6_39 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home249_kitchenliving2305_sensor18363_electric-appliance_fridgefreezer.csv", header=None)
    A7_39 = pd.read_csv(
        "/Data/room_and_appliance_sensors/sensordata/" +
        "home249_kitchenliving2305_sensor18362_electric-appliance_washingmachinetumbledrier.csv",
        header=None)

    appliance_list = [A1_1, A2_1, A4_1, A7_1, A1_2, A2_2, A3_2, A4_2, A6_2, A7_2, A1_3, A2_3, A9_3, A8_3, A3_3, A4_3,
                      A10_3,
                      A7_3, A2_4, A3_4, A4_4, A1_4, A8_4, A1_5, A2_5, A4_5, A6_5, A7_5, A1_6, A2_6, A3_6, A4_6, A7_6,
                      A2_7,
                      A3_7, A6_7, A1_7, A5_8, A7_8, A13_8, A4_8, A6_8, A2_8, A1_9, A2_9, A6_9, A11_9, A13_9, A3_9, A7_9,
                      A13_10, A4_10, A6_10, A7_10, A1_11, A6_11, A7_11, A3_11, A1_12, A2_12, A3_12, A7_12, A1_13,
                      A2_13, A6_13, A7_13, A15_13, A1_14, A11_14, A12_14, A13_14, A3_14, A4_14, A6_14, A7_14, A15_14,
                      A1_15,
                      A2_15, A13_15, A3_15, A7_15, A15_15, A1_16, A2_16, A9_16, A13_16, A3_16, A4_16, A7_16, A1_17,
                      A8_17,
                      A5_17, A6_17, A2_17, A13_17, A3_17, A4_17, A1_18, A2_18, A13_18, A6_18, A7_18, A1_19, A2_19,
                      A13_19,
                      A3_19, A6_19, A7_19, A1_20, A2_20, A13_20, A3_20, A6_20, A2_21, A3_21, A4_21, A6_21, A1_21, A7_21,
                      A2_22, A3_22, A6_22, A7_22, A13_22, A11_23, A13_23, A3_23, A4_23, A1_23, A7_23, A2_24, A13_24,
                      A3_24,
                      A5_24, A6_24, A1_24, A7_24, A2_25, A11_25, A6_25, A7_25, A9_26, A13_26, A8_26, A3_26, A4_26,
                      A7_26,
                      A1_26, A2_27, A13_27, A3_27, A4_27, A1_27, A7_27, A15_27, A9_28, A3_28, A11_28, A6_28, A7_28,
                      A1_28,
                      A9_29, A2_29, A13_29, A3_29, A7_29, A11_29, A8_29, A2_30, A13_30, A4_30, A6_30, A1_30, A7_30,
                      A13_31,
                      A3_31, A6_31, A7_31, A2_31, A13_32, A8_32, A6_32, A11_32, A13_33, A3_33, A4_33, A14_33, A6_33,
                      A7_33,
                      A11_34, A3_34, A6_34, A7_34, A10_35, A2_35, A13_35, A3_35, A4_35, A6_35, A1_35, A7_35, A6_36,
                      A15_36,
                      A1_37, A7_37, A13_37, A3_37, A4_37, A6_37, A1_38, A2_38, A6_38, A7_38, A2_39, A3_39, A4_39, A6_39,
                      A7_39]
    appliance_list_copy = [A1_1, A2_1, A4_1, A7_1, A1_2, A2_2, A3_2, A4_2, A6_2, A7_2, A1_3, A2_3, A9_3, A8_3, A3_3,
                           A4_3,
                           A10_3, A7_3, A2_4, A3_4, A4_4, A1_4, A8_4, A1_5, A2_5, A4_5, A6_5, A7_5, A1_6, A2_6, A3_6,
                           A4_6,
                           A7_6, A2_7, A3_7, A6_7, A1_7, A5_8, A7_8, A13_8, A4_8, A6_8, A2_8, A1_9, A2_9, A6_9, A11_9,
                           A13_9, A3_9, A7_9, A13_10, A4_10, A6_10, A7_10, A1_11, A6_11, A7_11, A3_11, A1_12, A2_12,
                           A3_12, A7_12, A1_13, A2_13, A6_13, A7_13, A15_13, A1_14, A11_14, A12_14, A13_14, A3_14,
                           A4_14,
                           A6_14, A7_14, A15_14, A1_15, A2_15, A13_15, A3_15, A7_15, A15_15, A1_16, A2_16, A9_16,
                           A13_16,
                           A3_16, A4_16, A7_16, A1_17, A8_17, A5_17, A6_17, A2_17, A13_17, A3_17, A4_17, A1_18, A2_18,
                           A13_18, A6_18, A7_18, A1_19, A2_19, A13_19, A3_19, A6_19, A7_19, A1_20, A2_20, A13_20, A3_20,
                           A6_20, A2_21, A3_21, A4_21, A6_21, A1_21, A7_21, A2_22, A3_22, A6_22, A7_22, A13_22, A11_23,
                           A13_23, A3_23, A4_23, A1_23, A7_23, A2_24, A13_24, A3_24, A5_24, A6_24, A1_24, A7_24, A2_25,
                           A11_25, A6_25, A7_25, A9_26, A13_26, A8_26, A3_26, A4_26, A7_26, A1_26, A2_27, A13_27, A3_27,
                           A4_27, A1_27, A7_27, A15_27, A9_28, A3_28, A11_28, A6_28, A7_28, A1_28, A9_29, A2_29, A13_29,
                           A3_29, A7_29, A11_29, A8_29, A2_30, A13_30, A4_30, A6_30, A1_30, A7_30, A13_31, A3_31, A6_31,
                           A7_31, A2_31, A13_32, A8_32, A6_32, A11_32, A13_33, A3_33, A4_33, A14_33, A6_33, A7_33,
                           A11_34,
                           A3_34, A6_34, A7_34, A10_35, A2_35, A13_35, A3_35, A4_35, A6_35, A1_35, A7_35, A6_36, A15_36,
                           A1_37, A7_37, A13_37, A3_37, A4_37, A6_37, A1_38, A2_38, A6_38, A7_38, A2_39, A3_39, A4_39,
                           A6_39, A7_39]
    return appliance_list


appliance_names = ['A1_1', 'A2_1', 'A4_1', 'A7_1', 'A1_2', 'A2_2', 'A3_2', 'A4_2', 'A6_2', 'A7_2', 'A1_3', 'A2_3',
                   'A9_3', 'A8_3', 'A3_3', 'A4_3', 'A10_3', 'A7_3', 'A2_4', 'A3_4', 'A4_4', 'A1_4', 'A8_4', 'A1_5',
                   'A2_5', 'A4_5', 'A6_5', 'A7_5', 'A1_6', 'A2_6', 'A3_6', 'A4_6', 'A7_6', 'A2_7', 'A3_7', 'A6_7',
                   'A1_7', 'A5_8', 'A7_8', 'A13_8', 'A4_8', 'A6_8', 'A2_8', 'A1_9', 'A2_9', 'A6_9', 'A11_9', 'A13_9',
                   'A3_9', 'A7_9', 'A13_10', 'A4_10', 'A6_10', 'A7_10', 'A1_11', 'A6_11', 'A7_11', 'A3_11',  # A1_10
                   'A1_12', 'A2_12', 'A3_12', 'A7_12', 'A1_13', 'A2_13', 'A6_13', 'A7_13', 'A15_13', 'A1_14', 'A11_14',
                   'A12_14', 'A13_14', 'A3_14', 'A4_14', 'A6_14', 'A7_14', 'A15_14', 'A1_15', 'A2_15', 'A13_15',
                   'A3_15', 'A7_15', 'A15_15', 'A1_16', 'A2_16', 'A9_16', 'A13_16', 'A3_16', 'A4_16', 'A7_16', 'A1_17',
                   'A8_17', 'A5_17', 'A6_17', 'A2_17', 'A13_17', 'A3_17', 'A4_17', 'A1_18', 'A2_18', 'A13_18', 'A6_18',
                   'A7_18', 'A1_19', 'A2_19', 'A13_19', 'A3_19', 'A6_19', 'A7_19', 'A1_20', 'A2_20', 'A13_20', 'A3_20',
                   'A6_20', 'A2_21', 'A3_21', 'A4_21', 'A6_21', 'A1_21', 'A7_21', 'A2_22', 'A3_22', 'A6_22', 'A7_22',
                   'A13_22', 'A11_23', 'A13_23', 'A3_23', 'A4_23', 'A1_23', 'A7_23', 'A2_24', 'A13_24', 'A3_24',
                   'A5_24', 'A6_24', 'A1_24', 'A7_24', 'A2_25', 'A11_25', 'A6_25', 'A7_25', 'A9_26', 'A13_26', 'A8_26',
                   'A3_26', 'A4_26', 'A7_26', 'A1_26', 'A2_27', 'A13_27', 'A3_27', 'A4_27', 'A1_27', 'A7_27', 'A15_27',
                   'A9_28', 'A3_28', 'A11_28', 'A6_28', 'A7_28', 'A1_28', 'A9_29', 'A2_29', 'A13_29', 'A3_29',
                   'A7_29', 'A11_29', 'A8_29', 'A2_30', 'A13_30', 'A4_30', 'A6_30', 'A1_30', 'A7_30', 'A13_31', 'A3_31',
                   'A6_31', 'A7_31', 'A2_31', 'A13_32', 'A8_32', 'A6_32', 'A11_32', 'A13_33', 'A3_33', 'A4_33',
                   'A14_33', 'A6_33', 'A7_33', 'A11_34', 'A3_34', 'A6_34', 'A7_34', 'A10_35', 'A2_35', 'A13_35',
                   'A3_35', 'A4_35', 'A6_35', 'A1_35', 'A7_35', 'A6_36', 'A15_36', 'A1_37', 'A7_37', 'A13_37', 'A3_37',
                   'A4_37', 'A6_37', 'A1_38', 'A2_38', 'A6_38', 'A7_38', 'A2_39', 'A3_39', 'A4_39', 'A6_39', 'A7_39']


def energy_per_day_calculation(df):
    """The data can be measured in different time intervals. But, generally data is shared with service providers once in a day.
    This method computes the energy consumption per day
    :param df: Dataframe that contains all data
    :return consumption_per_day: energy consumption of appliances per day
    """
    df[0] = pd.to_datetime(df[0])  # convert column to datetime object
    df.set_index(0, inplace=True)  # set column 'date' to index

    consumption_per_day = round(df.resample('D').sum() / 100, 2)  # note!! (Sum) # D =>> for day sample
    return consumption_per_day


# Data loading and mapping: Default method I: I already did earlier
def data_loading_method_one_appliance_wise(appliance_list):
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
        appliance_energy_list.append(globals()[var_name])  # Energy consumption for 7 days for all the appliances

    appliances = daug.appliance_wise_augmentation(appliance_energy_list)
    return appliances


# aa = data_loading_method_one_appliance_wise(appliance_list)

# Data loading and mapping: Default method II: User-wise mapping the data: User|Appliance|Energy_consumption_values
# Calculating energy per day as we send the data once a day
def data_loading_method_two_user_wise(appliance_list):
    for i in range(len(appliance_list)):
        consumption_per_day = energy_per_day_calculation(appliance_list[i])
        var_name = 'appliance_energy{}'.format(i)
        # Assign a value to the variable
        globals()[var_name] = []

        for j in range(len(consumption_per_day)):
            globals()[var_name].append(consumption_per_day[1][j])  # Energy consumption for an appliance in a day
        appliance_energy_list.append(globals()[var_name])  # Energy consumption for all days for all the appliances

        appliance_values = {}

        # Split the value based on the underscore character
        parts = appliance_names[i].split("_")

        # Extract the user and appliance values
        appliance = parts[0]
        user = 'U' + parts[1]

        # Check if the user exists in the dictionary, if not, create an empty list
        if user not in user_values:
            user_values[user] = []

        # Check if the appliance exists in the dictionary, if not, create an empty list
        if appliance not in appliance_values:
            appliance_values[appliance] = []

        # Append the value to the corresponding user and appliance lists
        appliance_values[appliance] = np.array(consumption_per_day).flatten()
        # appliance_values[appliance].append(np.array(consumption_per_day).flatten())
        user_values[user].append(appliance_values)
        # user_values[user] = appliance_values

    # Converting data in a dictionary format of appliances instead of list of appliances in the dictionary format The
    # 'user_values' dictionary is like within a dictionary list of dictionaries are there. but I want it in a format
    # that dictionary inside dictionary. For example original_data 'U1':[{'A1':[1,2,3,]},{ 'A2':[4,5]}], 'U2': :[{'A1':[
    # 1,2,3,]},{ 'A2':[4,5]}]} but I want like 'u1':{'A1':[2,5], 'A2':[3.4]
    converted_data = {}
    for user, appliances in user_values.items():
        user_data = {}
        for appliance_dict in appliances:
            for appliance, values in appliance_dict.items():
                user_data[appliance] = values
        converted_data[user] = user_data

    # Taking 30 days data for further processing.
    limited_data = {}
    for user, appliances in converted_data.items():
        limited_data[user] = {}
        for appliance, values in appliances.items():
            # Limit the values to 30
            limited_values = values[:30]
            # If there are fewer than 30 values, calculate the average of available values
            if len(limited_values) < 30:
                average_value = sum(limited_values) / len(limited_values)
                limited_values = np.append(limited_values, [average_value] * (30 - len(limited_values)))
            limited_data[user][appliance] = limited_values

    # Make sure all the users have same number of appliances. Here, if I don't have an appliance,
    # the appliance energy consumption value will be replaced with 0's as they don't consume any energy.
    all_appliances = set()
    for user_data in limited_data.values():
        all_appliances.update(user_data.keys())

    # Add missing appliances with zeros
    for user_data in limited_data.values():
        for appliance in all_appliances:
            if appliance not in user_data:
                user_data[appliance] = np.zeros(30)

    # Benchmarking: LDP-Laplacian (single noise adding everytime)
    # noise = lap.add_laplacian_noise(limited_data)

    # Data augmentation: Generates new data with a similar mean and variance as the original data
    augmented_mean_variance_df, augmented_data = daug.user_wise_mean_variance_augmentation(limited_data)
    limited_data.update(augmented_data)
    # Data augmentation: method 2 : Generates new data using VAE
    # augmented_VAE_df = daug.VAE_augmentation(limited_data)

    # # Create a new DataFrame for the original data
    # columns = ['user', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15']
    # original_df = pd.DataFrame(columns=columns)
    #
    # # Map the dictionary values to the dataframe
    # for user, appliances in limited_data.items():
    #     row = [user]  # Start with the user value
    #     for column in columns[1:]:
    #         # if column in appliances:
    #         row.append(appliances[column])
    #         # else:
    #         #     row.append([0])  # Use [0] as the default value if column not found
    #     original_df.loc[len(original_df)] = row
    #
    # # Concatenate the dataframes vertically
    # combined_df = pd.concat([original_df, augmented_mean_variance_df], axis=0)
    return limited_data

# Max value calculation
# max_value = None
# for user, appliances in limited_data.items():
#     for appliance, values in appliances.items():
#         if max_value is None or max(values) > max_value:
#             max_value = max(values)
#
# print(max_value)
#
