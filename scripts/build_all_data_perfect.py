# -*- coding: utf-8 -*-
"""
Perfect Aviation Platform Data Generator
Fully aligns with the official military aviation bold face test PDFs:
- MI-17V5
- CASA 212-200
- BELL 412 EP
- FENNEC AS550
- AH-64E APACHE
"""
import json
import os
import glob

# Import builders from build_full_suite, build_ballface_datasets, and build_ah64e
from build_full_suite import build_casa212, build_fennec_as550_full
from build_ballface_datasets import build_mi17v5
from build_ah64e import build_ah64e_suite

def build_bell412ep_perfect():
    # 106 Limitation questions with exact numbering and subQuestions
    lim_defs = [
        # FLIGHT CREW
        (1, "FLIGHT CREW", "1. Minimum flight crew", "1 pilot who shall operate helicopter on right crew seat", ["1 pilot who shall operate helicopter on right crew seat", "1 pilot", "1 pilot on right crew seat", "1"], "", 16, None),
        # GROSS WEIGHT
        (2, "GROSS WEIGHT", "2. Maximum gross weight for take off and landing", "11.900 Lbs", ["11.900", "11900", "11,900", "11.900 Lbs", "11900 lbs"], "Lbs", 16, None),
        (3, "GROSS WEIGHT", "3. Minimum gross weight for flight", "6400 Lbs", ["6400", "6.400", "6400 Lbs", "6400 lbs"], "Lbs", 16, None),
        (4, "GROSS WEIGHT", "4. Minimum combined crew weight at fuselage station 47.0", "170 Lbs", ["170", "170 Lbs", "170 lbs"], "Lbs", 16, None),
        # CARGO
        (5, "CARGO", "5. Max allowable deck loading", "100 lbs/ft2", ["100", "100 lbs/ft2", "100 lbs/sq ft", "100 lb/ft2"], "lbs/ft2", 16, None),
        (
            6, "CARGO", "6. Cargo deck tiedown fitting capacity",
            "a. Vertical 1250 lbs | b. Horizontal 500 lbs",
            ["1250 lbs, 500 lbs", "1250, 500"], "lbs", 16,
            [
                {"id": "sub_a", "letter": "a", "label": "Vertical", "answer": "1250 lbs", "acceptedAnswers": ["1250", "1.250", "1250 lbs", "1250lbs", "1,250"], "unit": "lbs", "placeholder": "Kapasitas vertikal..."},
                {"id": "sub_b", "letter": "b", "label": "Horizontal", "answer": "500 lbs", "acceptedAnswers": ["500", "500 lbs", "500lbs"], "unit": "lbs", "placeholder": "Kapasitas horizontal..."}
            ]
        ),
        (7, "CARGO", "7. Baggage compartment load limit (not to exceed 100 lbs/ft2)", "400 lbs", ["400", "400 lbs", "400lbs"], "lbs", 16, None),
        # CENTER OF GRAVITY
        (8, "CENTER OF GRAVITY", "8. Longitudinal center of gravity limits vary from station", "130 to 144", ["130 to 144", "130 - 144", "130-144", "130 sampai 144"], "", 16, None),
        (9, "CENTER OF GRAVITY", "9. Lateral center of gravity (left and right)", "4.5 inch", ["4.5", "4,5", "4.5 inch", "4.5 in", "4,5 inch"], "inch", 16, None),
        # AIR SPEED
        (10, "AIR SPEED", "10. Minimum IFR airspeed", "60 KIAS", ["60", "60 KIAS", "60 kias", "60 kts", "60 knots"], "KIAS", 16, None),
        (11, "AIR SPEED", "11. Basic Vne from sea level to 3000 ft (DA) at all gross weight", "140 KIAS", ["140", "140 KIAS", "140 kias", "140 kts", "140 knots"], "KIAS", 16, None),
        (12, "AIR SPEED", "12. Vne with only one autopilot engage", "115 KIAS", ["115", "115 KIAS", "115 kias", "115 kts"], "KIAS", 16, None),
        (13, "AIR SPEED", "13. Maximum airspeed when operating above 81% mast torque", "105 KIAS", ["105", "105 KIAS", "105 kias", "105 kts"], "KIAS", 16, None),
        (
            14, "AIR SPEED", "14. Vne for steady state autorotation",
            "a. At or below 10.000 ft pressure altitude 105 KIAS | b. Above 10.000 ft pressure altitude 80 KIAS",
            ["105 KIAS, 80 KIAS", "105, 80"], "KIAS", 16,
            [
                {"id": "sub_a", "letter": "a", "label": "At or below 10.000 ft pressure altitude", "answer": "105 KIAS", "acceptedAnswers": ["105", "105 KIAS", "105 kias", "105 kts"], "unit": "KIAS", "placeholder": "Vne <= 10.000 ft..."},
                {"id": "sub_b", "letter": "b", "label": "Above 10.000 ft pressure altitude", "answer": "80 KIAS", "acceptedAnswers": ["80", "80 KIAS", "80 kias", "80 kts"], "unit": "KIAS", "placeholder": "Vne > 10.000 ft..."}
            ]
        ),
        (15, "AIR SPEED", "15. Vne with cargo doors opened asymmetrically", "80 KIAS", ["80", "80 KIAS", "80 kias", "80 kts"], "KIAS", 16, None),
        (16, "AIR SPEED", "16. Vne with cargo doors in transit or in an unlocked position", "60 KIAS", ["60", "60 KIAS", "60 kias", "60 kts"], "KIAS", 16, None),
        (17, "AIR SPEED", "17. Vne with symmetrically doors open or removed with Bell Helicopter installed energy attenuating passenger seats", "60 KIAS", ["60", "60 KIAS", "60 kias", "60 kts"], "KIAS", 16, None),
        (18, "AIR SPEED", "18. Vne with symmetrically doors open or removed with Bell Helicopter Installed Blanket Interior/deluxe interior", "100 KIAS", ["100", "100 KIAS", "100 kias", "100 kts"], "KIAS", 16, None),
        (19, "AIR SPEED", "19. Maximum allowable air speed for sideward or rearward flight at or below 3.000 feet HD", "35 Knots", ["35", "35 Knots", "35 knots", "35 kts"], "Knots", 16, None),
        (20, "AIR SPEED", "20. Maximum allowable tailwind and crosswind or bellow 3.000 feet HD", "35 Knots", ["35", "35 Knots", "35 knots", "35 kts"], "Knots", 16, None),
        (21, "AIR SPEED", "21. Maximum operating pressure altitude", "20.000 Ft", ["20.000", "20000", "20,000", "20.000 Ft", "20000 ft"], "Ft", 16, None),
        (22, "AIR SPEED", "22. Maximum density altitude for take off, landing, and in-ground effect Maneuvers", "14.000 Ft", ["14.000", "14000", "14,000", "14.000 Ft", "14000 ft"], "Ft", 16, None),
        # CLIMB/DESCENT
        (23, "CLIMB/DESCENT", "23. Maximum IFR rate of climb or descent", "1000 ft/min", ["1000", "1.000", "1000 ft/min", "1000 fpm", "1000ft/min"], "ft/min", 16, None),
        (24, "CLIMB/DESCENT", "24. Maximum IFR approach slope", "5 degrees", ["5", "5 degrees", "5 deg", "5°", "5 degree"], "degrees", 16, None),
        # SLOPE LANDING
        (25, "SLOPE LANDING", "25. Forward/nose down", "4 degrees", ["4", "4 degrees", "4 deg", "4°"], "degrees", 16, None),
        (26, "SLOPE LANDING", "26. Rearward/nose up", "4 degrees", ["4", "4 degrees", "4 deg", "4°"], "degrees", 16, None),
        (27, "SLOPE LANDING", "27. Leftside slope", "10 degrees", ["10", "10 degrees", "10 deg", "10°"], "degrees", 16, None),
        (28, "SLOPE LANDING", "28. Rightside slope", "10 degrees", ["10", "10 degrees", "10 deg", "10°"], "degrees", 16, None),
        # MANEUVERING
        (29, "MANEUVERING", "29. Max angle of bank", "50 degress", ["50", "50 degrees", "50 degress", "50 deg", "50°"], "degress", 17, None),
        (30, "MANEUVERING", "30. Max nose up", "30 degress", ["30", "30 degrees", "30 degress", "30 deg", "30°"], "degress", 17, None),
        (31, "MANEUVERING", "31. Max nose down", "15 degress", ["15", "15 degrees", "15 degress", "15 deg", "15°"], "degress", 17, None),
        # AMBIENT AIR TEMPERATURE
        (32, "AMBIENT AIR TEMPERATURE", "32. Maximum sea level ambient temperature for operation", "51.7 °C/ 125 °F", ["51.7 °C/ 125 °F", "51.7 / 125", "51.7 C / 125 F", "51.7", "51,7"], "°C/ °F", 17, None),
        (33, "AMBIENT AIR TEMPERATURE", "33. Minimum ambient temperature for operation at all altitudes", "-40 °C/ -40 °F", ["-40 °C/ -40 °F", "-40 / -40", "-40 C / -40 F", "-40"], "°C/ °F", 17, None),
        # BATTERY
        (34, "BATTERY", "34. Maximum battery temperature", "62.8 °C/ 145 °F", ["62.8 °C/ 145 °F", "62.8 / 145", "62.8", "62,8", "62.8 C"], "°C/ °F", 17, None),
        (35, "BATTERY", "35. Minimum ambient temperature for battery start when battery and helicopter have been cold soaked", "-25 °C/ -13 °F", ["-25 °C/ -13 °F", "-25 / -13", "-25", "-25 C"], "°C/ °F", 17, None),
        # GENERATOR
        (36, "GENERATOR", "36. Continuous Operation", "0 to 75 amps", ["0 to 75", "0 - 75", "0-75", "0 sampai 75", "0 to 75 amps"], "amps", 17, None),
        (37, "GENERATOR", "37. Caution", "75 to 150 amps", ["75 to 150", "75 - 150", "75-150", "75 sampai 150", "75 to 150 amps"], "amps", 17, None),
        (38, "GENERATOR", "38. Maximum Continuous", "150 amps (each)", ["150", "150 amps", "150 amps (each)", "150 each"], "amps", 17, None),
        # ENGINE STARTER
        (39, "ENGINE STARTER", "39. Engine Starter Cycle 1 (ON)", "30 second ON", ["30", "30 second", "30 second ON", "30 sec on", "30 detik on", "30s on"], "second ON", 17, None),
        (40, "ENGINE STARTER", "40. Engine Starter Cycle 1 (OFF)", "60 second OFF", ["60", "60 second", "60 second OFF", "60 sec off", "60 detik off", "60s off"], "second OFF", 17, None),
        (41, "ENGINE STARTER", "41. Engine Starter Cycle 2 (ON)", "30 second ON", ["30", "30 second", "30 second ON", "30 sec on", "30 detik on", "30s on"], "second ON", 17, None),
        (42, "ENGINE STARTER", "42. Engine Starter Cycle 2 (OFF)", "5 minutes OFF", ["5", "5 minutes", "5 minutes OFF", "5 min off", "5 menit off"], "minutes OFF", 17, None),
        (43, "ENGINE STARTER", "43. Engine Starter Cycle 3 (ON)", "30 second ON", ["30", "30 second", "30 second ON", "30 sec on", "30 detik on", "30s on"], "second ON", 17, None),
        (44, "ENGINE STARTER", "44. Engine Starter Cycle 3 (OFF)", "15 minutes OFF", ["15", "15 minutes", "15 minutes OFF", "15 min off", "15 menit off"], "minutes OFF", 17, None),
        # GROUND POWER STARTS
        (45, "GROUND POWER STARTS", "45. 28 VDC ground power units for starting shall be limited to", "1000 amps max", ["1000", "1.000", "1000 amps", "1000 amps max", "1000A"], "amps max", 17, None),
        # GAS PRODUCER RPM (N1)
        (
            46, "GAS PRODUCER RPM (N1)", "46. Twin Engine Operation",
            "a. Continuous operation 61 to 103.1 % | b. Maximum continuous 103.1 % | c. Maximum for take off 103.1 %",
            ["61 to 103.1 %, 103.1 %, 103.1 %", "61-103.1, 103.1, 103.1"], "%", 17,
            [
                {"id": "sub_a", "letter": "a", "label": "Continuous operation", "answer": "61 to 103.1 %", "acceptedAnswers": ["61 to 103.1", "61 - 103.1", "61-103.1", "61 sampai 103.1"], "unit": "%", "placeholder": "N1 kontinu..."},
                {"id": "sub_b", "letter": "b", "label": "Maximum continuous", "answer": "103.1 %", "acceptedAnswers": ["103.1", "103.1 %", "103,1"], "unit": "%", "placeholder": "N1 max kontinu..."},
                {"id": "sub_c", "letter": "c", "label": "Maximum for take off", "answer": "103.1 %", "acceptedAnswers": ["103.1", "103.1 %", "103,1"], "unit": "%", "placeholder": "N1 max takeoff..."}
            ]
        ),
        (
            47, "GAS PRODUCER RPM (N1)", "47. One Engine Inoperative (OEI)",
            "a. Continuous OEI 103.1 to 103.7 % | b. 2 1/2 Minutes OEI 103.7 to 109.2 % | c. Maximum OEI 109.2 %",
            ["103.1 to 103.7, 103.7 to 109.2, 109.2"], "%", 17,
            [
                {"id": "sub_a", "letter": "a", "label": "Continuous OEI", "answer": "103.1 to 103.7 %", "acceptedAnswers": ["103.1 to 103.7", "103.1 - 103.7", "103.1-103.7", "103.1 sampai 103.7"], "unit": "%", "placeholder": "N1 kontinu OEI..."},
                {"id": "sub_b", "letter": "b", "label": "2 1/2 Minutes OEI", "answer": "103.7 to 109.2 %", "acceptedAnswers": ["103.7 to 109.2", "103.7 - 109.2", "103.7-109.2", "103.7 sampai 109.2"], "unit": "%", "placeholder": "N1 2.5 min OEI..."},
                {"id": "sub_c", "letter": "c", "label": "Maximum OEI", "answer": "109.2 %", "acceptedAnswers": ["109.2", "109.2 %", "109,2"], "unit": "%", "placeholder": "N1 max OEI..."}
            ]
        ),
        # POWER TURBINE RPM (N2)
        (48, "POWER TURBINE RPM (N2)", "48. Minimum in cruise at or below 6000 ft HD", "97 %", ["97", "97 %", "97%"], "%", 17, None),
        (49, "POWER TURBINE RPM (N2)", "49. Min for hover, take off and climb", "100 %", ["100", "100 %", "100%"], "%", 17, None),
        (50, "POWER TURBINE RPM (N2)", "50. Min in cruise above 6000 ft HD", "100 %", ["100", "100 %", "100%"], "%", 17, None),
        (51, "POWER TURBINE RPM (N2)", "51. Operation with ENG torque at or below 30%", "100 to 104.5 %", ["100 to 104.5", "100 - 104.5", "100-104.5", "100 sampai 104.5", "100 to 104.5 %"], "%", 17, None),
        (52, "POWER TURBINE RPM (N2)", "52. Max with ENG torque at or below 30%", "104.5 %", ["104.5", "104.5 %", "104,5"], "%", 17, None),
        # INTER TURBINE TEMPERATURE (ITT)
        (
            53, "INTER TURBINE TEMPERATURE (ITT)", "53. Twin Engine Operation (ITT)",
            "Gauge P/N ...115: 300-810°C, 810°C, 925°C, 1090°C | Gauge P/N ...119: 300-810°C, 810°C, 940°C, 1090°C",
            ["300 to 810, 810, 925, 1090"], "°C", 18,
            [
                {"id": "sub_a1", "letter": "a.1", "label": "Gauge P/N 212-075-067-115: Continuous operation", "answer": "300 to 810 °C", "acceptedAnswers": ["300 to 810", "300 - 810", "300-810", "300 sampai 810"], "unit": "°C", "placeholder": "Continuous..."},
                {"id": "sub_a2", "letter": "a.2", "label": "Gauge P/N 212-075-067-115: Maximum continuous", "answer": "810 °C", "acceptedAnswers": ["810", "810 °C", "810°C"], "unit": "°C", "placeholder": "Max continuous..."},
                {"id": "sub_a3", "letter": "a.3", "label": "Gauge P/N 212-075-067-115: Maximum transient (5 sec max above 810°C)", "answer": "925 °C", "acceptedAnswers": ["925", "925 °C", "925°C"], "unit": "°C", "placeholder": "Max transient..."},
                {"id": "sub_a4", "letter": "a.4", "label": "Gauge P/N 212-075-067-115: Maximum for starting (2 sec max above 960°C)", "answer": "1090 °C", "acceptedAnswers": ["1090", "1090 °C", "1090°C", "1.090"], "unit": "°C", "placeholder": "Max starting..."},
                {"id": "sub_b1", "letter": "b.1", "label": "Gauge P/N 212-075-067-119: Continuous operation", "answer": "300 to 810 °C", "acceptedAnswers": ["300 to 810", "300 - 810", "300-810", "300 sampai 810"], "unit": "°C", "placeholder": "Continuous..."},
                {"id": "sub_b2", "letter": "b.2", "label": "Gauge P/N 212-075-067-119: Maximum continuous", "answer": "810 °C", "acceptedAnswers": ["810", "810 °C", "810°C"], "unit": "°C", "placeholder": "Max continuous..."},
                {"id": "sub_b3", "letter": "b.3", "label": "Gauge P/N 212-075-067-119: Maximum transient (5 sec max above 810°C)", "answer": "940 °C", "acceptedAnswers": ["940", "940 °C", "940°C"], "unit": "°C", "placeholder": "Max transient..."},
                {"id": "sub_b4", "letter": "b.4", "label": "Gauge P/N 212-075-067-119: Maximum for starting (2 sec max above 960°C)", "answer": "1090 °C", "acceptedAnswers": ["1090", "1090 °C", "1090°C", "1.090"], "unit": "°C", "placeholder": "Max starting..."}
            ]
        ),
        (
            54, "INTER TURBINE TEMPERATURE (ITT)", "54. One Engine Inoperative (OEI) (ITT)",
            "Gauge P/N ...115: 820°C, 820-925°C, 925°C | Gauge P/N ...119: 820°C, 820-940°C, 940°C",
            ["820, 820 to 925, 925"], "°C", 18,
            [
                {"id": "sub_a1", "letter": "a.1", "label": "Gauge P/N 212-075-067-115: Maximum continuous OEI", "answer": "820 °C", "acceptedAnswers": ["820", "820 °C", "820°C"], "unit": "°C", "placeholder": "Max continuous OEI..."},
                {"id": "sub_a2", "letter": "a.2", "label": "Gauge P/N 212-075-067-115: 2 ½ Min OEI", "answer": "820 to 925 °C", "acceptedAnswers": ["820 to 925", "820 - 925", "820-925", "820 sampai 925"], "unit": "°C", "placeholder": "2.5 Min OEI..."},
                {"id": "sub_a3", "letter": "a.3", "label": "Gauge P/N 212-075-067-115: Maximum OEI", "answer": "925 °C", "acceptedAnswers": ["925", "925 °C", "925°C"], "unit": "°C", "placeholder": "Max OEI..."},
                {"id": "sub_b1", "letter": "b.1", "label": "Gauge P/N 212-075-067-119: Maximum continuous OEI", "answer": "820 °C", "acceptedAnswers": ["820", "820 °C", "820°C"], "unit": "°C", "placeholder": "Max continuous OEI..."},
                {"id": "sub_b2", "letter": "b.2", "label": "Gauge P/N 212-075-067-119: 2 ½ Min OEI", "answer": "820 to 940 °C", "acceptedAnswers": ["820 to 940", "820 - 940", "820-940", "820 sampai 940"], "unit": "°C", "placeholder": "2.5 Min OEI..."},
                {"id": "sub_b3", "letter": "b.3", "label": "Gauge P/N 212-075-067-119: Maximum OEI", "answer": "940 °C", "acceptedAnswers": ["940", "940 °C", "940°C"], "unit": "°C", "placeholder": "Max OEI..."}
            ]
        ),
        # ENGINE TORQUE – ONE ENGINE INOPERATIVE (OEI)
        (55, "ENGINE TORQUE – OEI", "55. Continuous OEI", "5 to 73.2 %", ["5 to 73.2", "5 - 73.2", "5-73.2", "5 sampai 73.2", "5 to 73.2 %"], "%", 18, None),
        (56, "ENGINE TORQUE – OEI", "56. Maximum continuous OEI", "73.2 %", ["73.2", "73.2 %", "73,2"], "%", 18, None),
        (57, "ENGINE TORQUE – OEI", "57. 2 ½ Min OEI", "73.2 to 81 %", ["73.2 to 81", "73.2 - 81", "73.2-81", "73.2 sampai 81", "73.2 to 81 %"], "%", 18, None),
        (58, "ENGINE TORQUE – OEI", "58. Maximum OEI", "81 %", ["81", "81 %", "81%"], "%", 18, None),
        # FUEL PRESSURE
        (59, "FUEL PRESSURE", "59. Minimum", "4 PSI", ["4", "4 PSI", "4psi"], "PSI", 18, None),
        (60, "FUEL PRESSURE", "60. Continuous operation", "4 to 35 PSI", ["4 to 35", "4 - 35", "4-35", "4 sampai 35", "4 to 35 PSI"], "PSI", 18, None),
        (61, "FUEL PRESSURE", "61. Maximum", "35 PSI", ["35", "35 PSI", "35psi"], "PSI", 18, None),
        # ENGINE OIL PRESSURE
        (
            62, "ENGINE OIL PRESSURE", "62. Gauge P/N 209-070-262-113",
            "a. Minimum for flight idle 40 PSI | b. Operation below 79% N1 RPM 40 to 90 PSI | c. Continuous operation 90 to 115 PSI | d. Maximum 115 PSI",
            ["40, 40 to 90, 90 to 115, 115"], "PSI", 18,
            [
                {"id": "sub_a", "letter": "a", "label": "Minimum for flight idle", "answer": "40 PSI", "acceptedAnswers": ["40", "40 PSI", "40psi"], "unit": "PSI", "placeholder": "Min idle..."},
                {"id": "sub_b", "letter": "b", "label": "Operation below 79% N1 RPM", "answer": "40 to 90 PSI", "acceptedAnswers": ["40 to 90", "40 - 90", "40-90", "40 sampai 90"], "unit": "PSI", "placeholder": "Below 79% N1..."},
                {"id": "sub_c", "letter": "c", "label": "Continuous operation", "answer": "90 to 115 PSI", "acceptedAnswers": ["90 to 115", "90 - 115", "90-115", "90 sampai 115"], "unit": "PSI", "placeholder": "Continuous..."},
                {"id": "sub_d", "letter": "d", "label": "Maximum", "answer": "115 PSI", "acceptedAnswers": ["115", "115 PSI", "115psi"], "unit": "PSI", "placeholder": "Maximum..."}
            ]
        ),
        (
            63, "ENGINE OIL PRESSURE", "63. Gauge P/N 209-070-262-109",
            "a. Minimum for flight idle 40 PSI | b. Operation below 79% N1 RPM 40 to 80 PSI | c. Continuous operation 80 to 115 PSI | d. Maximum 115 PSI",
            ["40, 40 to 80, 80 to 115, 115"], "PSI", 18,
            [
                {"id": "sub_a", "letter": "a", "label": "Minimum for flight idle", "answer": "40 PSI", "acceptedAnswers": ["40", "40 PSI", "40psi"], "unit": "PSI", "placeholder": "Min idle..."},
                {"id": "sub_b", "letter": "b", "label": "Operation below 79% N1 RPM", "answer": "40 to 80 PSI", "acceptedAnswers": ["40 to 80", "40 - 80", "40-80", "40 sampai 80"], "unit": "PSI", "placeholder": "Below 79% N1..."},
                {"id": "sub_c", "letter": "c", "label": "Continuous operation", "answer": "80 to 115 PSI", "acceptedAnswers": ["80 to 115", "80 - 115", "80-115", "80 sampai 115"], "unit": "PSI", "placeholder": "Continuous..."},
                {"id": "sub_d", "letter": "d", "label": "Maximum", "answer": "115 PSI", "acceptedAnswers": ["115", "115 PSI", "115psi"], "unit": "PSI", "placeholder": "Maximum..."}
            ]
        ),
        # ENGINE OIL TEMPERATURE
        (64, "ENGINE OIL TEMPERATURE", "64. Minimum", "0 °C", ["0", "0 °C", "0°C", "0 C"], "°C", 19, None),
        (65, "ENGINE OIL TEMPERATURE", "65. Continuous operation", "0 to 115 °C", ["0 to 115", "0 - 115", "0-115", "0 sampai 115", "0 to 115 °C"], "°C", 19, None),
        (66, "ENGINE OIL TEMPERATURE", "66. Maximum for MIL-PRF-7808 oil", "115 °C", ["115", "115 °C", "115°C", "115 C"], "°C", 19, None),
        (67, "ENGINE OIL TEMPERATURE", "67. Maximum for MIL-PRF-23699 oil", "120 °C", ["120", "120 °C", "120°C", "120 C"], "°C", 19, None),
        # C-BOX OIL PRESSURE
        (68, "C-BOX OIL PRESSURE", "68. Minimum for flight idle", "40 PSI", ["40", "40 PSI", "40psi"], "PSI", 19, None),
        (69, "C-BOX OIL PRESSURE", "69. Operation below 94% N2 RPM", "40 to 60 PSI", ["40 to 60", "40 - 60", "40-60", "40 sampai 60", "40 to 60 PSI"], "PSI", 19, None),
        (70, "C-BOX OIL PRESSURE", "70. Continuous operation", "60 to 80 PSI", ["60 to 80", "60 - 80", "60-80", "60 sampai 80", "60 to 80 PSI"], "PSI", 19, None),
        (71, "C-BOX OIL PRESSURE", "71. Maximum", "80 PSI", ["80", "80 PSI", "80psi"], "PSI", 19, None),
        # C-BOX OIL TEMPERATURE
        (72, "C-BOX OIL TEMPERATURE", "72. Minimum", "0 °C", ["0", "0 °C", "0°C"], "°C", 19, None),
        (73, "C-BOX OIL TEMPERATURE", "73. Continuous operation", "0 to 115 °C", ["0 to 115", "0 - 115", "0-115", "0 sampai 115", "0 to 115 °C"], "°C", 19, None),
        (74, "C-BOX OIL TEMPERATURE", "74. Maximum for MIL-PRF-7808 oil", "115 °C", ["115", "115 °C", "115°C"], "°C", 19, None),
        (75, "C-BOX OIL TEMPERATURE", "75. Maximum for MIL-PRF-23699 oil", "120 °C", ["120", "120 °C", "120°C"], "°C", 19, None),
        # XMSN OIL PRESSURE
        (76, "XMSN OIL PRESSURE", "76. Minimum for flight idle", "30 PSI", ["30", "30 PSI", "30psi"], "PSI", 19, None),
        (77, "XMSN OIL PRESSURE", "77. Idle range", "30 to 40 PSI", ["30 to 40", "30 - 40", "30-40", "30 sampai 40", "30 to 40 PSI"], "PSI", 19, None),
        (78, "XMSN OIL PRESSURE", "78. Continuous operation", "40 to 70 PSI", ["40 to 70", "40 - 70", "40-70", "40 sampai 70", "40 to 70 PSI"], "PSI", 19, None),
        (79, "XMSN OIL PRESSURE", "79. Maximum", "70 PSI", ["70", "70 PSI", "70psi"], "PSI", 19, None),
        # XMSN OIL TEMPERATURE
        (80, "XMSN OIL TEMPERATURE", "80. Continuous operation", "15 to 110 °C", ["15 to 110", "15 - 110", "15-110", "15 sampai 110", "15 to 110 °C"], "°C", 19, None),
        (81, "XMSN OIL TEMPERATURE", "81. Maximum", "110 °C", ["110", "110 °C", "110°C"], "°C", 19, None),
        # MAST TORQUE – TWIN ENGINE OPERATION
        (82, "MAST TORQUE", "82. Maximum continuous", "81 %", ["81", "81 %", "81%"], "%", 19, None),
        (83, "MAST TORQUE", "83. Take off range (5 minutes max)", "81 to 100 %", ["81 to 100", "81 - 100", "81-100", "81 sampai 100", "81 to 100 %"], "%", 19, None),
        (84, "MAST TORQUE", "84. Maximum", "100 %", ["100", "100 %", "100%"], "%", 19, None),
        # ROTOR RPM – POWER ON
        (85, "ROTOR RPM – POWER ON", "85. Minimum", "97 %", ["97", "97 %", "97%"], "%", 19, None),
        (86, "ROTOR RPM – POWER ON", "86. Continuous operation at or below 6000 ft HD", "97 to 100 %", ["97 to 100", "97 - 100", "97-100", "97 sampai 100", "97 to 100 %"], "%", 19, None),
        (87, "ROTOR RPM – POWER ON", "87. Continuous operation above 6000 ft HD", "100 %", ["100", "100 %", "100%"], "%", 19, None),
        (88, "ROTOR RPM – POWER ON", "88. Maximum continuous", "100 %", ["100", "100 %", "100%"], "%", 19, None),
        (89, "ROTOR RPM – POWER ON", "89. Operation with ENG torque at or below 30%", "100 to 104.5 %", ["100 to 104.5", "100 - 104.5", "100-104.5", "100 sampai 104.5", "100 to 104.5 %"], "%", 19, None),
        (90, "ROTOR RPM – POWER ON", "90. Max with ENG torque at or below 30%", "104.5 %", ["104.5", "104.5 %", "104,5"], "%", 19, None),
        # ROTOR RPM – POWER OFF
        (91, "ROTOR RPM – POWER OFF", "91. Min for autorotation with gross weight below 8000 lbs (3629 kg)", "80 %", ["80", "80 %", "80%"], "%", 19, None),
        (92, "ROTOR RPM – POWER OFF", "92. Power off operation with gross weight below 8000 lbs (3629 kg)", "80 to 104.5 %", ["80 to 104.5", "80 - 104.5", "80-104.5", "80 sampai 104.5", "80 to 104.5 %"], "%", 19, None),
        (93, "ROTOR RPM – POWER OFF", "93. Min for autorotation with gross weight at or above 8000 lbs (3629 kg)", "91 %", ["91", "91 %", "91%"], "%", 19, None),
        (94, "ROTOR RPM – POWER OFF", "94. Maximum", "104.5 %", ["104.5", "104.5 %", "104,5"], "%", 19, None),
        # ROTOR RPM – GROUND OPERATION
        (95, "ROTOR RPM – GROUND OPERATION", "95. Minimum", "77 %", ["77", "77 %", "77%"], "%", 20, None),
        (96, "ROTOR RPM – GROUND OPERATION", "96. Minimum with stick centering ind system inoperative", "97 %", ["97", "97 %", "97%"], "%", 20, None),
        (97, "ROTOR RPM – GROUND OPERATION", "97. Transient (avoid steady state autorotation)", "26 to 77 %", ["26 to 77", "26 - 77", "26-77", "26 sampai 77", "26 to 77 %"], "%", 20, None),
        # HYDRAULIC PRESSURE
        (98, "HYDRAULIC PRESSURE", "98. Minimum", "600 PSI", ["600", "600 PSI", "600psi"], "PSI", 20, None),
        (99, "HYDRAULIC PRESSURE", "99. Caution", "600 to 900 PSI", ["600 to 900", "600 - 900", "600-900", "600 sampai 900", "600 to 900 PSI"], "PSI", 20, None),
        (100, "HYDRAULIC PRESSURE", "100. Continuous operation", "900 to 1100 PSI", ["900 to 1100", "900 - 1100", "900-1100", "900 sampai 1100", "900 to 1100 PSI", "900 to 1.100"], "PSI", 20, None),
        (101, "HYDRAULIC PRESSURE", "101. Maximum", "1100 PSI", ["1100", "1.100", "1100 PSI", "1100psi"], "PSI", 20, None),
        # HYDRAULIC TEMPERATURE
        (102, "HYDRAULIC TEMPERATURE", "102. Maximum", "88 °C", ["88", "88 °C", "88°C", "88 C"], "°C", 20, None),
        # AHRS ALIGNMENT
        (103, "AHRS ALIGNMENT", "103. Pitch", "less than ± 10°", ["less than ± 10°", "less than +- 10", "< 10", "10", "± 10°", "+- 10°"], "", 20, None),
        (104, "AHRS ALIGNMENT", "104. Roll", "less than ± 5°", ["less than ± 5°", "less than +- 5", "< 5", "5", "± 5°", "+- 5°"], "", 20, None),
        (105, "AHRS ALIGNMENT", "105. Yaw", "less than 1°/sec", ["less than 1°/sec", "less than 1", "< 1", "1", "1°/sec"], "", 20, None),
        (106, "AHRS ALIGNMENT", "106. Lateral and longitudinal acceleration", "less than 0.05g", ["less than 0.05g", "0.05g", "0.05", "0,05g", "0,05", "< 0.05g"], "", 20, None)
    ]

    questions = []
    for num, cat, q_text, ans, accepted, unit, page, subs in lim_defs:
        q_obj = {
            "id": f"B412-LIM-{num:03d}",
            "aircraft": "BELL 412 EP",
            "section": "LIMITATION",
            "category": cat,
            "questionType": "fill-blank",
            "question": q_text,
            "answer": ans,
            "acceptedAnswers": accepted,
            "unit": unit,
            "sourceDocument": "bold face bell 412 EP.pdf",
            "sourcePage": page,
            "points": len(subs) if subs else 1,
            "verified": True
        }
        if subs:
            q_obj["subQuestions"] = subs
        questions.append(q_obj)

    # Indicator Limitation (pages 21-24)
    ind_defs = [
        ("Airspeed Dial Markings", "Airspeed Indicator Markings", "0-30: Unreliable | 30-140: Cont. Operation | 105: Max autorotation | 140: VNE", [
            {"id": "sub_1", "letter": "a", "label": "0 – 30 (Yellow)", "answer": "Indicator Unreliable", "acceptedAnswers": ["Indicator Unreliable", "Unreliable"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_2", "letter": "b", "label": "30 – 140 (Green)", "answer": "Cont. Operation", "acceptedAnswers": ["Cont. Operation", "Continuous Operation", "Cont Operation"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_3", "letter": "c", "label": "105 (Blue/White)", "answer": "Max for autorotation at or below 10.000 ft Hp", "acceptedAnswers": ["Max for autorotation at or below 10.000 ft Hp", "Max for autorotation", "Max autorotation"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_4", "letter": "d", "label": "140 (Red)", "answer": "VNE", "acceptedAnswers": ["VNE", "Vne"], "placeholder": "Arti penunjukan..."}
        ]),
        ("Mast Torque Dial Markings", "Mast Torque Indicator Markings", "10-81: Cont. Operation | 81-100: 5 Min Take Off Range | 100: Maximum", [
            {"id": "sub_1", "letter": "a", "label": "10 – 81 (Green)", "answer": "Cont. Operation", "acceptedAnswers": ["Cont. Operation", "Continuous Operation"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_2", "letter": "b", "label": "81 – 100 (Yellow)", "answer": "5 Min Take Off Range", "acceptedAnswers": ["5 Min Take Off Range", "5 Min Take Off", "Take off range"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_3", "letter": "c", "label": "100 (Red)", "answer": "Maximum", "acceptedAnswers": ["Maximum", "Max"], "placeholder": "Arti penunjukan..."}
        ]),
        ("Engine Torque Dial Markings", "Engine Torque Indicator Markings", "5-73.2: Cont. OEI Operation | 73.2-81: 2 ½ OEI | 81: Maximum OEI", [
            {"id": "sub_1", "letter": "a", "label": "5 – 73.2 (Green)", "answer": "Cont. OEI Operation", "acceptedAnswers": ["Cont. OEI Operation", "Continuous OEI Operation", "Cont. OEI"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_2", "letter": "b", "label": "73.2 – 81 (Yellow)", "answer": "2 ½ OEI", "acceptedAnswers": ["2 ½ OEI", "2.5 OEI", "2 1/2 OEI"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_3", "letter": "c", "label": "81 (Red)", "answer": "Maximum OEI", "acceptedAnswers": ["Maximum OEI", "Max OEI"], "placeholder": "Arti penunjukan..."}
        ]),
        ("Rotor RPM (Nr) Dial Markings", "Rotor RPM (Nr) Indicator Markings", "26-77: Transient Ground | 80: Min autorotation | 80-91: Power off | 91-104.5: Cont. Power off | 104.5: Maximum", [
            {"id": "sub_1", "letter": "a", "label": "26 – 77 (Yellow)", "answer": "Transient Ground Operation", "acceptedAnswers": ["Transient Ground Operation", "Transient Ground"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_2", "letter": "b", "label": "80 (Red)", "answer": "Min for Autorotation below 8000 lbs gross weight", "acceptedAnswers": ["Min for Autorotation below 8000 lbs", "Min for autorotation"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_3", "letter": "c", "label": "80 – 91 (Yellow)", "answer": "Power Off Operation below 8000 lbs gross weight", "acceptedAnswers": ["Power Off Operation below 8000 lbs", "Power off below 8000 lbs"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_4", "letter": "d", "label": "91 – 104.5 (Green)", "answer": "Cont. Power Off Operation (Min 91%)", "acceptedAnswers": ["Cont. Power Off Operation", "Cont Power Off"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_5", "letter": "e", "label": "104.5 (Red)", "answer": "Maximum", "acceptedAnswers": ["Maximum", "Max"], "placeholder": "Arti penunjukan..."}
        ]),
        ("Gas Producer RPM (Ni)", "Gas Producer RPM (Ni) Dial Markings", "12: Min start | 61: Idle | 61-103.1: Continuous | 103.1: Max Cont | 103.1-103.7: Cont OEI | 103.7-109.2: 2.5 Min OEI", [
            {"id": "sub_1", "letter": "a", "label": "12", "answer": "Minimum for opening throttle during start", "acceptedAnswers": ["Minimum for opening throttle during start", "Min for opening throttle"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_2", "letter": "b", "label": "61", "answer": "Idle RPM", "acceptedAnswers": ["Idle RPM", "Idle"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_3", "letter": "c", "label": "61 - 103.1", "answer": "Continuous Operation", "acceptedAnswers": ["Continuous Operation", "Cont Operation"], "placeholder": "Arti penunjukan..."},
            {"id": "sub_4", "letter": "d", "label": "103.1", "answer": "Maximum Continuous", "acceptedAnswers": ["Maximum Continuous", "Max Continuous"], "placeholder": "Arti penunjukan..."}
        ])
    ]

    for idx, (cat, q_title, ans, subs) in enumerate(ind_defs, 1):
        questions.append({
            "id": f"B412-IND-{idx:03d}",
            "aircraft": "BELL 412 EP",
            "section": "INDICATOR LIMITATION",
            "category": cat,
            "questionType": "fill-blank",
            "question": f"{idx}. {q_title}",
            "answer": ans,
            "acceptedAnswers": [ans],
            "unit": "",
            "sourceDocument": "bold face bell 412 EP.pdf",
            "sourcePage": 21 + idx - 1,
            "points": len(subs),
            "verified": True,
            "subQuestions": subs
        })

    # Emergency Procedures (pages 10-15)
    emer_defs = [
        (
            1, "Terminology", "1. TERMINOLOGY",
            "a. LAND AS SOON AS POSSIBLE Land without delay at nearest suitable area | b. LAND AS SOON AS PRACTICAL Discretion of pilot",
            [
                {"id": "sub_a", "letter": "a", "label": "LAND AS SOON AS POSSIBLE", "answer": "Land without delay at the nearest suitable area (i.e. open field) at which safe approach and landing is reasonably assured", "acceptedAnswers": ["Land without delay at the nearest suitable area", "Land without delay at the nearest suitable area (i.e. open field) at which safe approach and landing is reasonably assured", "Land without delay", "Land without delay at nearest suitable area"], "placeholder": "Definisi..."},
                {"id": "sub_b", "letter": "b", "label": "LAND AS SOON AS PRACTICAL", "answer": "The duration of the flight and landing site are at the discretion of the pilot. Extended flight beyond the nearest approved landing area is not recommended", "acceptedAnswers": ["The duration of the flight and landing site are at the discretion of the pilot", "The duration of the flight and landing site are at the discretion of the pilot. Extended flight beyond the nearest approved landing area is not recommended", "At the discretion of the pilot"], "placeholder": "Definisi..."}
            ]
        ),
        (
            2, "Single Engine Failure", "2. SINGLE ENGINE FAILURE (INDICATION)",
            "a. ENG 1 OUT or ENG 2 OUT W/L – ILLUMINATE | b. NI drop below 53% and decreasing | c. NII drop below 85% and decreasing | d. ITT drop below 400°C and decreasing | e. No 1 or 2 OIL PRESS C/L – ILLUMINATE | f. DC GEN C/L (affected Eng) – ILLUMINATE | g. PART SEP (affected Eng) – ILLUMINATE | h. NII NORMAL ENG drop to 97%",
            [
                {"id": "sub_a", "letter": "a", "label": "ENG 1 OUT or ENG 2 OUT W/L", "answer": "ENG 1 OUT or ENG 2 OUT W/L – ILLUMINATE", "acceptedAnswers": ["ENG 1 OUT or ENG 2 OUT W/L – ILLUMINATE", "ENG 1 OUT or ENG 2 OUT W/L ILLUMINATE", "ENG 1 OUT or ENG 2 OUT ILLUMINATE", "ENG OUT W/L ILLUMINATE", "ILLUMINATE"], "placeholder": "Indikasi a..."},
                {"id": "sub_b", "letter": "b", "label": "NI", "answer": "NI drop below 53% and decreasing", "acceptedAnswers": ["NI drop below 53% and decreasing", "N1 drop below 53% and decreasing", "NI drop below 53%", "N1 drop below 53%"], "placeholder": "Indikasi b..."},
                {"id": "sub_c", "letter": "c", "label": "NII", "answer": "NII drop below 85% and decreasing", "acceptedAnswers": ["NII drop below 85% and decreasing", "N2 drop below 85% and decreasing", "NII drop below 85%", "N2 drop below 85%"], "placeholder": "Indikasi c..."},
                {"id": "sub_d", "letter": "d", "label": "ITT", "answer": "ITT drop below 400°C and decreasing", "acceptedAnswers": ["ITT drop below 400°C and decreasing", "ITT drop below 400°C", "ITT below 400C"], "placeholder": "Indikasi d..."},
                {"id": "sub_e", "letter": "e", "label": "No 1 or 2 OIL PRESS C/L", "answer": "No 1 or 2 OIL PRESS C/L – ILLUMINATE", "acceptedAnswers": ["No 1 or 2 OIL PRESS C/L – ILLUMINATE", "OIL PRESS C/L – ILLUMINATE", "ILLUMINATE"], "placeholder": "Indikasi e..."},
                {"id": "sub_f", "letter": "f", "label": "DC GEN C/L (affected Eng)", "answer": "DC GEN C/L (affected Eng) – ILLUMINATE", "acceptedAnswers": ["DC GEN C/L (affected Eng) – ILLUMINATE", "DC GEN C/L – ILLUMINATE", "ILLUMINATE"], "placeholder": "Indikasi f..."},
                {"id": "sub_g", "letter": "g", "label": "PART SEP (affected Eng)", "answer": "PART SEP (affected Eng) – ILLUMINATE", "acceptedAnswers": ["PART SEP (affected Eng) – ILLUMINATE", "PART SEP – ILLUMINATE", "ILLUMINATE"], "placeholder": "Indikasi g..."},
                {"id": "sub_h", "letter": "h", "label": "NII NORMAL ENG", "answer": "NII NORMAL ENG drop to 97%", "acceptedAnswers": ["NII NORMAL ENG drop to 97%", "drop to 97%", "97%"], "placeholder": "Indikasi h..."}
            ]
        ),
        (
            3, "Single Engine Failure", "2. SINGLE ENGINE FAILURE (PROCEDURE)",
            "a. Reduce power | b. Set airspeed 70 kts | c. Set NII 100% if possible | d. IDLE STOP RELEASE to affected Eng | e. THROTTLE – CLOSED | f. BOOST PUMP – OFF | g. FUEL SWITCH – OFF | h. FUEL XFEED – OVRD CLOSE | i. FUEL INTCON – OPEN | j. GEN (affected Eng) – OFF | k. NON-ESNTL BUS – AS DESIRED | l. BATT BUS 1 & 2 – ON | m. MASTER CAUTION LT - RESET | n. SHALLOW APP – RUN ON LANDING",
            [
                {"id": "sub_a", "letter": "a", "label": "Power (FLY THE A/C)", "answer": "Reduce power", "acceptedAnswers": ["Reduce power"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Airspeed", "answer": "Set airspeed 70 kts", "acceptedAnswers": ["Set airspeed 70 kts", "70 kts", "Airspeed 70 kts"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "NII", "answer": "Set NII 100% if possible", "acceptedAnswers": ["Set NII 100% if possible", "Set N2 100% if possible", "Set N2 100%", "Set NII 100%"], "placeholder": "Tindakan c..."},
                {"id": "sub_d", "letter": "d", "label": "IDLE STOP (IDENTIFY)", "answer": "IDLE STOP RELEASE to affected Eng", "acceptedAnswers": ["IDLE STOP RELEASE to affected Eng", "IDLE STOP RELEASE"], "placeholder": "Tindakan d..."},
                {"id": "sub_e", "letter": "e", "label": "THROTTLE", "answer": "THROTTLE – CLOSED", "acceptedAnswers": ["THROTTLE – CLOSED", "THROTTLE - CLOSED", "THROTTLE CLOSED", "CLOSED"], "placeholder": "Tindakan e..."},
                {"id": "sub_f", "letter": "f", "label": "BOOST PUMP", "answer": "BOOST PUMP – OFF", "acceptedAnswers": ["BOOST PUMP – OFF", "BOOST PUMP - OFF", "BOOST PUMP OFF", "OFF"], "placeholder": "Tindakan f..."},
                {"id": "sub_g", "letter": "g", "label": "FUEL SWITCH", "answer": "FUEL SWITCH – OFF", "acceptedAnswers": ["FUEL SWITCH – OFF", "FUEL SWITCH - OFF", "FUEL SWITCH OFF", "OFF"], "placeholder": "Tindakan g..."},
                {"id": "sub_h", "letter": "h", "label": "FUEL XFEED", "answer": "FUEL XFEED – OVRD CLOSE", "acceptedAnswers": ["FUEL XFEED – OVRD CLOSE", "FUEL XFEED - OVRD CLOSE", "OVRD CLOSE", "CLOSE"], "placeholder": "Tindakan h..."},
                {"id": "sub_i", "letter": "i", "label": "FUEL INTCON", "answer": "FUEL INTCON – OPEN", "acceptedAnswers": ["FUEL INTCON – OPEN", "FUEL INTCON - OPEN", "OPEN"], "placeholder": "Tindakan i..."},
                {"id": "sub_j", "letter": "j", "label": "GEN (affected Eng)", "answer": "GEN (affected Eng) – OFF", "acceptedAnswers": ["GEN (affected Eng) – OFF", "GEN - OFF", "OFF"], "placeholder": "Tindakan j..."},
                {"id": "sub_k", "letter": "k", "label": "NON-ESNTL BUS", "answer": "NON-ESNTL BUS – AS DESIRED", "acceptedAnswers": ["NON-ESNTL BUS – AS DESIRED", "AS DESIRED"], "placeholder": "Tindakan k..."},
                {"id": "sub_l", "letter": "l", "label": "BATT BUS 1 & 2", "answer": "BATT BUS 1 & 2 – ON", "acceptedAnswers": ["BATT BUS 1 & 2 – ON", "ON"], "placeholder": "Tindakan l..."},
                {"id": "sub_m", "letter": "m", "label": "MASTER CAUTION LT", "answer": "MASTER CAUTION LT - RESET", "acceptedAnswers": ["MASTER CAUTION LT - RESET", "RESET"], "placeholder": "Tindakan m..."},
                {"id": "sub_n", "letter": "n", "label": "LAND AS SOON AS PRACTICAL", "answer": "SHALLOW APP – RUN ON LANDING", "acceptedAnswers": ["SHALLOW APP – RUN ON LANDING", "SHALLOW APP - RUN ON LANDING", "RUN ON LANDING"], "placeholder": "Tindakan n..."}
            ]
        ),
        (
            4, "Dual Engine Failure", "3. DUAL ENGINE FAILURE (INDICATION)",
            "a. ENG 1 OUT & ENG 2 OUT W/L ILLUMINATE | b. NI drop below 53% and decreasing (both) | c. NII drop below 85% and decreasing (both) | d. ITT drop below 400°C and decreasing (both) | e. No 1 & 2 OIL PRESS C/L – ILLUMINATE | f. DC GEN C/L (both Eng) – ILLUMINATE | g. PART SEP (both Eng) – ILLUMINATE",
            [
                {"id": "sub_a", "letter": "a", "label": "ENG 1 OUT & ENG 2 OUT W/L", "answer": "ENG 1 OUT & ENG 2 OUT W/L ILLUMINATE", "acceptedAnswers": ["ENG 1 OUT & ENG 2 OUT W/L ILLUMINATE", "ILLUMINATE"], "placeholder": "Indikasi a..."},
                {"id": "sub_b", "letter": "b", "label": "NI", "answer": "NI drop below 53% and decreasing (both)", "acceptedAnswers": ["NI drop below 53% and decreasing (both)", "NI drop below 53%", "N1 drop below 53%"], "placeholder": "Indikasi b..."},
                {"id": "sub_c", "letter": "c", "label": "NII", "answer": "NII drop below 85% and decreasing (both)", "acceptedAnswers": ["NII drop below 85% and decreasing (both)", "NII drop below 85%", "N2 drop below 85%"], "placeholder": "Indikasi c..."},
                {"id": "sub_d", "letter": "d", "label": "ITT", "answer": "ITT drop below 400°C and decreasing (both)", "acceptedAnswers": ["ITT drop below 400°C and decreasing (both)", "ITT drop below 400°C", "below 400C"], "placeholder": "Indikasi d..."},
                {"id": "sub_e", "letter": "e", "label": "No 1 & 2 OIL PRESS C/L", "answer": "No 1 & 2 OIL PRESS C/L – ILLUMINATE", "acceptedAnswers": ["No 1 & 2 OIL PRESS C/L – ILLUMINATE", "ILLUMINATE"], "placeholder": "Indikasi e..."},
                {"id": "sub_f", "letter": "f", "label": "DC GEN C/L (both Eng)", "answer": "DC GEN C/L (both Eng) – ILLUMINATE", "acceptedAnswers": ["DC GEN C/L (both Eng) – ILLUMINATE", "ILLUMINATE"], "placeholder": "Indikasi f..."},
                {"id": "sub_g", "letter": "g", "label": "PART SEP (both Eng)", "answer": "PART SEP (both Eng) – ILLUMINATE", "acceptedAnswers": ["PART SEP (both Eng) – ILLUMINATE", "ILLUMINATE"], "placeholder": "Indikasi g..."}
            ]
        ),
        (
            5, "Dual Engine Failure", "3. DUAL ENGINE FAILURE (PROCEDURE - Perform AUTOROTATION)",
            "a. Collective FULL DOWN | b. THROTTLE - CLOSE | c. Set airspeed 65 - 90 kts | d. ROTOR RPM – ON THE GREEN | e. 300 FT AGL – OPEN THROTTLE | f. 100 FT AGL – FLARE | g. FIRST APPLICATION",
            [
                {"id": "sub_a", "letter": "a", "label": "Collective", "answer": "Collective FULL DOWN", "acceptedAnswers": ["Collective FULL DOWN", "FULL DOWN", "Full down"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "THROTTLE", "answer": "THROTTLE - CLOSE", "acceptedAnswers": ["THROTTLE - CLOSE", "THROTTLE – CLOSE", "THROTTLE CLOSE", "CLOSE"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Airspeed", "answer": "Set airspeed 65 - 90 kts", "acceptedAnswers": ["Set airspeed 65 - 90 kts", "65 - 90 kts", "65-90 kts", "Airspeed 65-90 kts"], "placeholder": "Tindakan c..."},
                {"id": "sub_d", "letter": "d", "label": "ROTOR RPM", "answer": "ROTOR RPM – ON THE GREEN", "acceptedAnswers": ["ROTOR RPM – ON THE GREEN", "ROTOR RPM - ON THE GREEN", "ROTOR RPM ON THE GREEN", "ON THE GREEN"], "placeholder": "Tindakan d..."},
                {"id": "sub_e", "letter": "e", "label": "300 FT AGL (ALTIMETER – CX READING)", "answer": "300 FT AGL – OPEN THROTTLE", "acceptedAnswers": ["300 FT AGL – OPEN THROTTLE", "OPEN THROTTLE", "Open throttle"], "placeholder": "Tindakan e..."},
                {"id": "sub_f", "letter": "f", "label": "100 FT AGL", "answer": "100 FT AGL – FLARE", "acceptedAnswers": ["100 FT AGL – FLARE", "FLARE", "Flare"], "placeholder": "Tindakan f..."},
                {"id": "sub_g", "letter": "g", "label": "Touchdown", "answer": "FIRST APPLICATION", "acceptedAnswers": ["FIRST APPLICATION", "First application"], "placeholder": "Tindakan g..."}
            ]
        ),
        (
            6, "Engine Fire In Flight", "4. ENGINE FIRE – in flight (INDICATION)",
            "FIRE 1 PULL or FIRE 2 PULL handle – ILLUMINATE",
            None
        ),
        (
            7, "Engine Fire In Flight", "4. ENGINE FIRE – in flight (PROCEDURE)",
            "a. FIRE PULL handle (affected Eng) – PULL | b. FIRE EXT – MAIN | c. Reduce power | d. Set airspeed 70 kts | e. Set NII 100% if possible | f. IDLE STOP RELEASE | g. THROTTLE – CLOSED | h. BOOST PUMP – OFF | i. FUEL SWITCH – OFF | j. FUEL XFEED – OVRD CLOSE | k. FUEL INTCON – OPEN | l. GEN (affected Eng) – OFF | m. NON-ESNTL BUS – AS DESIRED | n. BATT BUS 1 & 2 – ON | o. MASTER CAUTION LT - RESET | p. FIRE EXT – RESERVE (if 10s light ON) | q. SHALLOW APP – RUN ON LANDING | r. Complete Eng Shutdown | s. Exit Helicopter",
            [
                {"id": "sub_a", "letter": "a", "label": "FIRE PULL handle (affected Eng)", "answer": "FIRE PULL handle (affected Eng) – PULL", "acceptedAnswers": ["FIRE PULL handle (affected Eng) – PULL", "PULL"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "FIRE EXT", "answer": "FIRE EXT – MAIN", "acceptedAnswers": ["FIRE EXT – MAIN", "MAIN"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Power (FLY THE A/C)", "answer": "Reduce power", "acceptedAnswers": ["Reduce power"], "placeholder": "Tindakan c..."},
                {"id": "sub_d", "letter": "d", "label": "Airspeed", "answer": "Set airspeed 70 kts", "acceptedAnswers": ["Set airspeed 70 kts", "70 kts"], "placeholder": "Tindakan d..."},
                {"id": "sub_e", "letter": "e", "label": "NII", "answer": "Set NII 100% if possible", "acceptedAnswers": ["Set NII 100% if possible", "100%"], "placeholder": "Tindakan e..."},
                {"id": "sub_f", "letter": "f", "label": "IDLE STOP RELEASE", "answer": "IDLE STOP RELEASE to affected Eng", "acceptedAnswers": ["IDLE STOP RELEASE to affected Eng", "IDLE STOP RELEASE"], "placeholder": "Tindakan f..."},
                {"id": "sub_g", "letter": "g", "label": "THROTTLE", "answer": "THROTTLE – CLOSED", "acceptedAnswers": ["THROTTLE – CLOSED", "CLOSED"], "placeholder": "Tindakan g..."},
                {"id": "sub_h", "letter": "h", "label": "BOOST PUMP", "answer": "BOOST PUMP – OFF", "acceptedAnswers": ["BOOST PUMP – OFF", "OFF"], "placeholder": "Tindakan h..."},
                {"id": "sub_i", "letter": "i", "label": "FUEL SWITCH", "answer": "FUEL SWITCH – OFF", "acceptedAnswers": ["FUEL SWITCH – OFF", "OFF"], "placeholder": "Tindakan i..."},
                {"id": "sub_j", "letter": "j", "label": "FUEL XFEED", "answer": "FUEL XFEED – OVRD CLOSE", "acceptedAnswers": ["FUEL XFEED – OVRD CLOSE", "OVRD CLOSE"], "placeholder": "Tindakan j..."},
                {"id": "sub_k", "letter": "k", "label": "FUEL INTCON", "answer": "FUEL INTCON – OPEN", "acceptedAnswers": ["FUEL INTCON – OPEN", "OPEN"], "placeholder": "Tindakan k..."},
                {"id": "sub_l", "letter": "l", "label": "GEN (affected Eng)", "answer": "GEN (affected Eng) – OFF", "acceptedAnswers": ["GEN (affected Eng) – OFF", "OFF"], "placeholder": "Tindakan l..."},
                {"id": "sub_m", "letter": "m", "label": "NON-ESNTL BUS", "answer": "NON-ESNTL BUS – AS DESIRED", "acceptedAnswers": ["NON-ESNTL BUS – AS DESIRED", "AS DESIRED"], "placeholder": "Tindakan m..."},
                {"id": "sub_n", "letter": "n", "label": "BATT BUS 1 & 2", "answer": "BATT BUS 1 & 2 – ON", "acceptedAnswers": ["BATT BUS 1 & 2 – ON", "ON"], "placeholder": "Tindakan n..."},
                {"id": "sub_o", "letter": "o", "label": "MASTER CAUTION LT", "answer": "MASTER CAUTION LT - RESET", "acceptedAnswers": ["MASTER CAUTION LT - RESET", "RESET"], "placeholder": "Tindakan o..."},
                {"id": "sub_p", "letter": "p", "label": "If 10 second FIRE PULL W/L remains ON", "answer": "FIRE EXT – RESERVE", "acceptedAnswers": ["FIRE EXT – RESERVE", "RESERVE"], "placeholder": "Tindakan p..."},
                {"id": "sub_q", "letter": "q", "label": "LAND AS SOON AS POSSIBLE", "answer": "SHALLOW APP – RUN ON LANDING", "acceptedAnswers": ["SHALLOW APP – RUN ON LANDING", "RUN ON LANDING"], "placeholder": "Tindakan q..."},
                {"id": "sub_r", "letter": "r", "label": "After Landing (Engine)", "answer": "Complete Eng Shutdown", "acceptedAnswers": ["Complete Eng Shutdown", "Shutdown"], "placeholder": "Tindakan r..."},
                {"id": "sub_s", "letter": "s", "label": "After Landing (Helicopter)", "answer": "Exit Helicopter", "acceptedAnswers": ["Exit Helicopter", "Exit"], "placeholder": "Tindakan s..."}
            ]
        ),
        (
            8, "Pedal Emergency", "5. RIGHT PEDAL LOCKED FORWARD OR NEUTRAL (PROCEDURE)",
            "b. ENG RPM – Maintain on the green | c. Set airspeed at or above 60 kts | d. Shallow to normal approach | e. 2 to 5 ft AGL – Slowly reduce THROTTLE (luruskan heading) | f. RUN ON LANDING",
            [
                {"id": "sub_b", "letter": "b", "label": "ENG RPM", "answer": "ENG RPM – Maintain on the green", "acceptedAnswers": ["ENG RPM – Maintain on the green", "Maintain on the green"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Airspeed", "answer": "Set airspeed at or above 60 kts", "acceptedAnswers": ["Set airspeed at or above 60 kts", "at or above 60 kts", "60 kts"], "placeholder": "Tindakan c..."},
                {"id": "sub_d", "letter": "d", "label": "Approach", "answer": "Shallow to normal approach", "acceptedAnswers": ["Shallow to normal approach", "shallow to normal"], "placeholder": "Tindakan d..."},
                {"id": "sub_e", "letter": "e", "label": "2 to 5 ft AGL", "answer": "Slowly reduce THROTTLE (luruskan heading)", "acceptedAnswers": ["Slowly reduce THROTTLE (luruskan heading)", "Slowly reduce THROTTLE"], "placeholder": "Tindakan e..."},
                {"id": "sub_f", "letter": "f", "label": "Landing", "answer": "RUN ON LANDING", "acceptedAnswers": ["RUN ON LANDING", "run on landing"], "placeholder": "Tindakan f..."}
            ]
        ),
        (
            9, "Pedal Emergency", "6. LEFT PEDAL LOCKED FORWARD (PROCEDURE)",
            "a. Reduce Power | b. ENG RPM – Maintain on the green | c. Set airspeed at or above 60 kts | d. Normal to steep approach | e. 2 ft AGL – Apply COLLECTIVE as necessary (luruskan heading) | f. ZERO SPEED TOUCHDOWN",
            [
                {"id": "sub_a", "letter": "a", "label": "Power", "answer": "Reduce Power", "acceptedAnswers": ["Reduce Power", "reduce power"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "ENG RPM", "answer": "ENG RPM – Maintain on the green", "acceptedAnswers": ["ENG RPM – Maintain on the green", "Maintain on the green"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Airspeed", "answer": "Set airspeed at or above 60 kts", "acceptedAnswers": ["Set airspeed at or above 60 kts", "at or above 60 kts", "60 kts"], "placeholder": "Tindakan c..."},
                {"id": "sub_d", "letter": "d", "label": "Approach", "answer": "Normal to steep approach", "acceptedAnswers": ["Normal to steep approach", "normal to steep"], "placeholder": "Tindakan d..."},
                {"id": "sub_e", "letter": "e", "label": "2 ft AGL", "answer": "Apply COLLECTIVE as necessary (luruskan heading)", "acceptedAnswers": ["Apply COLLECTIVE as necessary (luruskan heading)", "Apply COLLECTIVE as necessary"], "placeholder": "Tindakan e..."},
                {"id": "sub_f", "letter": "f", "label": "Touchdown", "answer": "ZERO SPEED TOUCHDOWN", "acceptedAnswers": ["ZERO SPEED TOUCHDOWN", "Zero speed touchdown"], "placeholder": "Tindakan f..."}
            ]
        ),
        (
            10, "Hydraulic Emergency", "7. HYDRAULIC SYSTEM FAILURE (INDICATION)",
            "a. NO 1 or NO 2 HYD C/L ILLUMINATE | b. Abnormal hyd press (low, high or fluctuating) | c. Possible high temp (affected system) | d. Increased pedal force (if Hyd System 1 failed)",
            [
                {"id": "sub_a", "letter": "a", "label": "Warning Light", "answer": "NO 1 or NO 2 HYD C/L ILLUMINATE", "acceptedAnswers": ["NO 1 or NO 2 HYD C/L ILLUMINATE", "ILLUMINATE"], "placeholder": "Indikasi a..."},
                {"id": "sub_b", "letter": "b", "label": "Hydraulic Pressure", "answer": "Abnormal hyd press (low, high or fluctuating)", "acceptedAnswers": ["Abnormal hyd press (low, high or fluctuating)", "Abnormal hyd press"], "placeholder": "Indikasi b..."},
                {"id": "sub_c", "letter": "c", "label": "Hydraulic Temp", "answer": "Possible high temp (affected system)", "acceptedAnswers": ["Possible high temp (affected system)", "Possible high temp"], "placeholder": "Indikasi c..."},
                {"id": "sub_d", "letter": "d", "label": "Pedal force", "answer": "Increased pedal force (if Hyd System 1 failed)", "acceptedAnswers": ["Increased pedal force (if Hyd System 1 failed)", "Increased pedal force"], "placeholder": "Indikasi d..."}
            ]
        ),
        (
            11, "Hydraulic Emergency", "7. HYDRAULIC SYSTEM FAILURE (PROCEDURE)",
            "e. Affected system – IDENTIFY POSITIVELY | f. HYD SYS switch – OFF (affected system) | g. Set NII 100% | h. MASTER CAUTION – RESET | LAND AS SOON AS POSSIBLE",
            [
                {"id": "sub_e", "letter": "e", "label": "Affected system", "answer": "Affected system – IDENTIFY POSITIVELY", "acceptedAnswers": ["Affected system – IDENTIFY POSITIVELY", "IDENTIFY POSITIVELY"], "placeholder": "Tindakan e..."},
                {"id": "sub_f", "letter": "f", "label": "HYD SYS switch", "answer": "HYD SYS switch – OFF (affected system)", "acceptedAnswers": ["HYD SYS switch – OFF (affected system)", "OFF"], "placeholder": "Tindakan f..."},
                {"id": "sub_g", "letter": "g", "label": "NII", "answer": "Set NII 100%", "acceptedAnswers": ["Set NII 100%", "100%"], "placeholder": "Tindakan g..."},
                {"id": "sub_h", "letter": "h", "label": "MASTER CAUTION", "answer": "MASTER CAUTION – RESET", "acceptedAnswers": ["MASTER CAUTION – RESET", "RESET"], "placeholder": "Tindakan h..."}
            ]
        )
    ]

    for idx, cat, q_title, ans, subs in emer_defs:
        q_obj = {
            "id": f"B412-EMER-{idx:03d}",
            "aircraft": "BELL 412 EP",
            "section": "EMERGENCY PROCEDURES",
            "category": cat,
            "questionType": "fill-blank",
            "question": q_title,
            "answer": ans,
            "acceptedAnswers": [ans],
            "unit": "",
            "sourceDocument": "bold face bell 412 EP.pdf",
            "sourcePage": 10 + (idx // 2),
            "points": len(subs) if subs else 1,
            "verified": True
        }
        if subs:
            q_obj["subQuestions"] = subs
        questions.append(q_obj)

    return {
        "aircraft": "BELL 412 EP",
        "title": "BOLD FACE LIMITATION & EMERGENCY BELL 412 EP",
        "sourceDocument": "bold face bell 412 EP.pdf",
        "description": "Limitation 106 item lengkap, Indicator limitation ranges, dan Emergency Procedures Bell 412 EP",
        "totalQuestions": len(questions),
        "questions": questions
    }

def update_aircraft_index():
    index_list = []
    meta_order = [
        ("data/ah-64e.json", "AH-64E APACHE", "AH-64E Rv. 3.0 EMERGENCY PROCEDURES & LIMITATIONS", "AH-64E Rv. 3.0 EMERGENCY PROCEDURES PRACTICE TEST.pdf"),
        ("data/anka-male-uav.json", "ANKA MALE UAV", "ANKA MALE UAV - BOLD FACE LIMITATIONS & EMERGENCY PROCEDURES", "ANKAID-T0544-AFM-2"),
        ("data/bell-412-ep.json", "BELL 412 EP", "BOLD FACE LIMITATION & EMERGENCY BELL 412 EP", "bold face bell 412 EP.pdf"),
        ("data/bo-105.json", "BO-105", "BOLD FACE BO-105", "BOLD FACE BO-105.pdf"),
        ("data/casa-212-200.json", "CASA 212-200", "BOLD FACE CASA 212-200 AVIOCAR", "BOLD FACE CASA 212-200 AVIOCAR.pdf"),
        ("data/fennec-as550.json", "FENNEC AS 550", "BOLD FACE FENNEC AS 550", "BOLD FACE FENNEC.pdf"),
        ("data/mi-17v5.json", "MI-17V5", "BOLD FACE MI-17V5", "BOLD FACE MI-17V5.pdf"),
        ("data/sikorsky-s300c.json", "SIKORSKY S-300C", "BOLD FACE & LIMITATIONS SIKORSKY S-300C", "SIKORSKY S-300C POOH")
    ]

    for file_path, default_name, default_title, default_source in meta_order:
        if not os.path.exists(file_path):
            continue
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            qs = data.get("questions", [])
            categories = sorted(list(set(q.get("category", "") for q in qs if q.get("category"))))
            sections = sorted(list(set(q.get("section", "") for q in qs if q.get("section"))))
            
            entry = {
                "aircraft": data.get("aircraft", default_name),
                "title": data.get("title", default_title),
                "file": file_path.replace("\\", "/"),
                "sourceDocument": data.get("sourceDocument", default_source),
                "description": data.get("description", ""),
                "totalQuestions": len(qs),
                "categoriesCount": len(categories),
                "categories": categories,
                "sections": sections
            }
            index_list.append(entry)
        except Exception as e:
            print(f"Error indexing {file_path}: {e}")

    with open("data/aircraft-index.json", "w", encoding="utf-8") as f:
        json.dump(index_list, f, indent=2, ensure_ascii=False)
    print(f"Updated data/aircraft-index.json with {len(index_list)} aircraft suites.")

def main():
    os.makedirs("data", exist_ok=True)
    c212 = build_casa212()
    with open("data/casa-212-200.json", "w", encoding="utf-8") as f:
        json.dump(c212, f, indent=2, ensure_ascii=False)
    print(f"Generated data/casa-212-200.json with {c212['totalQuestions']} items.")

    mi17 = build_mi17v5()
    with open("data/mi-17v5.json", "w", encoding="utf-8") as f:
        json.dump(mi17, f, indent=2, ensure_ascii=False)
    print(f"Generated data/mi-17v5.json with {mi17['totalQuestions']} items.")

    fennec = build_fennec_as550_full()
    with open("data/fennec-as550.json", "w", encoding="utf-8") as f:
        json.dump(fennec, f, indent=2, ensure_ascii=False)
    print(f"Generated data/fennec-as550.json with {fennec['totalQuestions']} items.")

    b412 = build_bell412ep_perfect()
    with open("data/bell-412-ep.json", "w", encoding="utf-8") as f:
        json.dump(b412, f, indent=2, ensure_ascii=False)
    print(f"Generated data/bell-412-ep.json with {b412['totalQuestions']} items.")

    ah64 = build_ah64e_suite()
    with open("data/ah-64e.json", "w", encoding="utf-8") as f:
        json.dump(ah64, f, indent=2, ensure_ascii=False)
    print(f"Generated data/ah-64e.json with {ah64['totalQuestions']} items.")

    update_aircraft_index()

if __name__ == "__main__":
    main()
