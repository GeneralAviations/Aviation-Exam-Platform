# -*- coding: utf-8 -*-
"""
Ballface / Boldface Comprehensive Dataset Builder
Standardizes multi-item questions with exact subQuestions (a., b., c., etc.)
matching the user's official PDF documents.
"""
import json
import os
import glob

def build_mi17v5():
    questions = [
        # 1. Normal takeoff weight
        {
            "id": "MI17-ISIAN-001",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Basic Weights & Capacity",
            "questionType": "fill-blank",
            "question": "1. Normal takeoff weight",
            "answer": "11.100 Kg",
            "acceptedAnswers": ["11.100", "11100", "11.100 Kg", "11100 kg", "11,100"],
            "unit": "Kg",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        # 2. Maximum takeoff weight
        {
            "id": "MI17-ISIAN-002",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Basic Weights & Capacity",
            "questionType": "fill-blank",
            "question": "2. Maximum takeoff weight",
            "answer": "13.000 Kg",
            "acceptedAnswers": ["13.000", "13000", "13.000 Kg", "13000 kg", "13,000"],
            "unit": "Kg",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        # 3. Troop carrier (Maximum, Numb Troopers carried)
        {
            "id": "MI17-ISIAN-003",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Troop Carrier",
            "questionType": "fill-blank",
            "question": "3. Troop carrier",
            "answer": "a. Maximum 4.000 Kg | b. Numb Troopers carried 36 Orang",
            "acceptedAnswers": ["4.000 Kg, 36 Orang", "4000 kg, 36 orang", "4000, 36"],
            "unit": "",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Maximum",
                    "answer": "4.000 Kg",
                    "acceptedAnswers": ["4.000", "4000", "4.000 Kg", "4000 kg", "4,000"],
                    "unit": "Kg",
                    "placeholder": "Kapasitas maksimum..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Numb Troopers carried",
                    "answer": "36 Orang",
                    "acceptedAnswers": ["36", "36 Orang", "36 orang", "36 person"],
                    "unit": "Orang",
                    "placeholder": "Jumlah pasukan..."
                }
            ]
        },
        # 4. Maximum limit speed in horizontal flight at altitude from 0-1000 m
        {
            "id": "MI17-ISIAN-004",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Speed",
            "questionType": "fill-blank",
            "question": "4. Maximum limit speedin horizontal flight at altitudefrom 0-1000 m",
            "answer": "a. At normal takeoff weight 250 km/h | b. At maximum takeoff weight 230 km/h",
            "acceptedAnswers": ["250 km/h, 230 km/h", "250, 230"],
            "unit": "km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "At normal takeoff weight",
                    "answer": "250 km/h",
                    "acceptedAnswers": ["250", "250 km/h", "250km/h"],
                    "unit": "km/h",
                    "placeholder": "Kecepatan bobot normal..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "At maximum takeoff weight",
                    "answer": "230 km/h",
                    "acceptedAnswers": ["230", "230 km/h", "230km/h"],
                    "unit": "km/h",
                    "placeholder": "Kecepatan bobot maksimum..."
                }
            ]
        },
        # 5. Cruising speed at altitude from 0 to 1000
        {
            "id": "MI17-ISIAN-005",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Cruising Speed",
            "questionType": "fill-blank",
            "question": "5. Cruising speed at altitude from 0 to 1000",
            "answer": "a. At normal takeoff weight 220 to 230 km/h | b. At maximum takeoff weight 205 to 215 km/h",
            "acceptedAnswers": ["220 to 230 km/h, 205 to 215 km/h", "220-230, 205-215"],
            "unit": "km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "At normal takeoff weight",
                    "answer": "220 to 230 km/h",
                    "acceptedAnswers": ["220 to 230", "220-230", "220 to 230 km/h", "220-230 km/h", "220 sampai 230"],
                    "unit": "km/h",
                    "placeholder": "Jelajah bobot normal..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "At maximum takeoff weight",
                    "answer": "205 to 215 km/h",
                    "acceptedAnswers": ["205 to 215", "205-215", "205 to 215 km/h", "205-215 km/h", "205 sampai 215"],
                    "unit": "km/h",
                    "placeholder": "Jelajah bobot maksimum..."
                }
            ]
        },
        # 6. Hovering ceiling
        {
            "id": "MI17-ISIAN-006",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Ceiling",
            "questionType": "fill-blank",
            "question": "6. Hovering ceiling at normal takeoff weight , ISA, air bleed to Dust protection device ejectors being off",
            "answer": "3980 m",
            "acceptedAnswers": ["3980", "3980 m", "3.980", "3.980 m"],
            "unit": "m",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        # 7. Service ceiling
        {
            "id": "MI17-ISIAN-007",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Ceiling",
            "questionType": "fill-blank",
            "question": "7. Service ceiling",
            "answer": "a. At Normal takeoff weight 6000 m | b. At maximum takeoff wieight 4800 m",
            "acceptedAnswers": ["6000 m, 4800 m", "6000, 4800"],
            "unit": "m",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "At Normal takeoff weight",
                    "answer": "6000 m",
                    "acceptedAnswers": ["6000", "6000 m", "6.000", "6.000 m"],
                    "unit": "m",
                    "placeholder": "Langit-langit servis normal..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "At maximum takeoff wieight",
                    "answer": "4800 m",
                    "acceptedAnswers": ["4800", "4800 m", "4.800", "4.800 m"],
                    "unit": "m",
                    "placeholder": "Langit-langit servis max..."
                }
            ]
        },
        # 8. Weight limitation
        {
            "id": "MI17-LIM-008",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Weight Limitation",
            "questionType": "fill-blank",
            "question": "8. Weight limitation",
            "answer": "a. Maximum useful load 4000 kg | b. Maximum external load weight 3000 (4000) kg",
            "acceptedAnswers": ["4000 kg, 3000 (4000) kg", "4000, 3000 (4000)"],
            "unit": "kg",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Maximum useful load",
                    "answer": "4000 kg",
                    "acceptedAnswers": ["4000", "4000 kg", "4.000", "4.000 kg"],
                    "unit": "kg",
                    "placeholder": "Beban berguna maksimum..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Maximum external load weight",
                    "answer": "3000 (4000) kg",
                    "acceptedAnswers": ["3000 (4000)", "3000 (4000) kg", "3000", "4000", "3000/4000", "3000-4000", "3.000 (4.000) kg"],
                    "unit": "kg",
                    "placeholder": "Beban luar maksimum..."
                }
            ]
        },
        # 9. CG Limitation
        {
            "id": "MI17-LIM-009",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "CG Limitation",
            "questionType": "fill-blank",
            "question": "9. CG Limitation",
            "answer": "a. Forward CG limit is +300 mm | b. Aft CG limit -95 mm",
            "acceptedAnswers": ["+300 mm, -95 mm", "+300, -95", "300, -95"],
            "unit": "mm",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Forward CG limit is",
                    "answer": "+300 mm",
                    "acceptedAnswers": ["+300", "+300 mm", "300", "300 mm", "+300mm"],
                    "unit": "mm",
                    "placeholder": "Batas CG depan..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Aft CG limit",
                    "answer": "-95 mm",
                    "acceptedAnswers": ["-95", "-95 mm", "95", "-95mm"],
                    "unit": "mm",
                    "placeholder": "Batas CG belakang..."
                }
            ]
        },
        # 10. Speed limitation (IAS limits Km/h)
        {
            "id": "MI17-LIM-010",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Speed Limitation Table",
            "questionType": "fill-blank",
            "question": "10. Speed limitation (IAS limits. Km/h at 13.000 kg & 11.100 kg takeoff weight)",
            "answer": "Up to 1000m: 230/60 & 250/60 | 2000m: 195/60 & 230/60 | 3000m: 160/60 & 210/60 | 4000m: 120/60 & 170/60",
            "acceptedAnswers": [
                "230/60, 250/60",
                "Up to 1000: 230/60 & 250/60"
            ],
            "unit": "km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 6,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Up to 1000 m (13.000 kg Max/Min | 11.100 kg Max/Min)",
                    "answer": "230/60 & 250/60",
                    "acceptedAnswers": ["230/60 & 250/60", "230, 60, 250, 60", "230 60 250 60"],
                    "unit": "km/h",
                    "placeholder": "Ketik nilai batas IAS..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "2000 m (13.000 kg Max/Min | 11.100 kg Max/Min)",
                    "answer": "195/60 & 230/60",
                    "acceptedAnswers": ["195/60 & 230/60", "195, 60, 230, 60", "195 60 230 60"],
                    "unit": "km/h",
                    "placeholder": "Ketik nilai batas IAS..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "3000 m (13.000 kg Max/Min | 11.100 kg Max/Min)",
                    "answer": "160/60 & 210/60",
                    "acceptedAnswers": ["160/60 & 210/60", "160, 60, 210, 60", "160 60 210 60"],
                    "unit": "km/h",
                    "placeholder": "Ketik nilai batas IAS..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "4000 m (13.000 kg Max/Min | 11.100 kg Max/Min)",
                    "answer": "120/60 & 170/60",
                    "acceptedAnswers": ["120/60 & 170/60", "120, 60, 170, 60", "120 60 170 60"],
                    "unit": "km/h",
                    "placeholder": "Ketik nilai batas IAS..."
                },
                {
                    "id": "sub_e",
                    "letter": "e",
                    "label": "5000 m (11.100 kg takeoff weight Maximum/Minimum)",
                    "answer": "130/60",
                    "acceptedAnswers": ["130/60", "130, 60", "130 / 60", "130 60"],
                    "unit": "km/h",
                    "placeholder": "Ketik nilai batas IAS..."
                },
                {
                    "id": "sub_f",
                    "letter": "f",
                    "label": "6000 m (11.100 kg takeoff weight Maximum/Minimum)",
                    "answer": "100/60",
                    "acceptedAnswers": ["100/60", "100, 60", "100 / 60", "100 60"],
                    "unit": "km/h",
                    "placeholder": "Ketik nilai batas IAS..."
                }
            ]
        },
        # 11. Hovering Altitude
        {
            "id": "MI17-LIM-011",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Hovering Altitude",
            "questionType": "fill-blank",
            "question": "11. Hovering Altitude :",
            "answer": "a. 11.100 and below Up to 10 m | b. Above 11.1000 Up to 5 m",
            "acceptedAnswers": ["Up to 10 m, Up to 5 m", "10, 5", "Up to 10, Up to 5"],
            "unit": "m",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "11.100 and below",
                    "answer": "Up to 10 m",
                    "acceptedAnswers": ["Up to 10", "10", "Up to 10 m", "10 m", "up to 10"],
                    "unit": "m",
                    "placeholder": "Hovering altitude bobot <= 11.100 kg..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Above 11.1000",
                    "answer": "Up to 5 m",
                    "acceptedAnswers": ["Up to 5", "5", "Up to 5 m", "5 m", "up to 5"],
                    "unit": "m",
                    "placeholder": "Hovering altitude bobot > 11.100 kg..."
                }
            ]
        },
        # 12. Maximum allowed wind speed at:
        {
            "id": "MI17-LIM-012",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Wind Limitation",
            "questionType": "fill-blank",
            "question": "12. Maximum allowed wind speed at: (AT M/R START AND STOP & AT TAKEOFF AND LANDING)",
            "answer": "Headwind: 25 / 25 | Right side: 10 / 10 | Left side: 15 / 10 | Tailwind: 8 / 10",
            "acceptedAnswers": ["25/25, 10/10, 15/10, 8/10"],
            "unit": "m/s",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 4,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Headwind (M/R START AND STOP / TAKEOFF AND LANDING)",
                    "answer": "25 m/s / 25 m/s",
                    "acceptedAnswers": ["25", "25 m/s", "25 / 25", "25 dan 25", "25/25"],
                    "unit": "m/s",
                    "placeholder": "Kecepatan angin sakal..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Right side crosswind (M/R START AND STOP / TAKEOFF AND LANDING)",
                    "answer": "10 m/s / 10 m/s",
                    "acceptedAnswers": ["10", "10 m/s", "10 / 10", "10 dan 10", "10/10"],
                    "unit": "m/s",
                    "placeholder": "Kecepatan angin samping kanan..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Left side crosswind (M/R START AND STOP / TAKEOFF AND LANDING)",
                    "answer": "15 m/s / 10 m/s",
                    "acceptedAnswers": ["15 / 10", "15 dan 10", "15 m/s / 10 m/s", "15, 10", "15/10"],
                    "unit": "m/s",
                    "placeholder": "Kecepatan angin samping kiri..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Tailwind (M/R START AND STOP / TAKEOFF AND LANDING)",
                    "answer": "8 m/s / 10 m/s",
                    "acceptedAnswers": ["8 / 10", "8 dan 10", "8 m/s / 10 m/s", "8, 10", "8/10"],
                    "unit": "m/s",
                    "placeholder": "Kecepatan angin buritan..."
                }
            ]
        },
        # 13. Maximum Bank
        {
            "id": "MI17-LIM-013",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Bank Limitation",
            "questionType": "fill-blank",
            "question": "13. Maximum Bank :",
            "answer": "a. 50 TO 3000: 30 deg / 20 deg | b. ABOVE 3000: 15 deg / 15 deg",
            "acceptedAnswers": ["30 / 20, 15 / 15"],
            "unit": "deg",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "50 TO 3000 (Gross weight 11100 kg or below / Above 11100 kg)",
                    "answer": "30 deg / 20 deg",
                    "acceptedAnswers": ["30 / 20", "30 dan 20", "30 deg / 20 deg", "30° / 20°", "30/20"],
                    "unit": "deg",
                    "placeholder": "Bank 50 - 3000 m..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "ABOVE 3000 (Gross weight 11100 kg or below / Above 11100 kg)",
                    "answer": "15 deg / 15 deg",
                    "acceptedAnswers": ["15 / 15", "15 dan 15", "15 deg / 15 deg", "15° / 15°", "15/15", "15"],
                    "unit": "deg",
                    "placeholder": "Bank > 3000 m..."
                }
            ]
        },
        # 14. Maximum allowed speed at zoom and dive
        {
            "id": "MI17-LIM-014",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Zoom & Dive Limitation",
            "questionType": "fill-blank",
            "question": "14. Maximum allowed speed at zoom and dive :",
            "answer": "0-500: 220 / 300 | 500-1000: 200 / 300 | 1000-2000: 180 / 250",
            "acceptedAnswers": ["220/300, 200/300, 180/250"],
            "unit": "km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 3,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "0 TO 500 (Zoom / Recovery from dive)",
                    "answer": "220 km/h / 300 km/h",
                    "acceptedAnswers": ["220 / 300", "220 dan 300", "220 km/h / 300 km/h", "220/300"],
                    "unit": "km/h",
                    "placeholder": "Kecepatan 0-500 m..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "500 TO 1000 (Zoom / Recovery from dive)",
                    "answer": "200 km/h / 300 km/h",
                    "acceptedAnswers": ["200 / 300", "200 dan 300", "200 km/h / 300 km/h", "200/300"],
                    "unit": "km/h",
                    "placeholder": "Kecepatan 500-1000 m..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "1000 TO 2000 (Zoom / Recovery from dive)",
                    "answer": "180 km/h / 250 km/h",
                    "acceptedAnswers": ["180 / 250", "180 dan 250", "180 km/h / 250 km/h", "180/250"],
                    "unit": "km/h",
                    "placeholder": "Kecepatan 1000-2000 m..."
                }
            ]
        },
        # 15. Engine maximum operating parameters at different power rating
        {
            "id": "MI17-LIM-015",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Engine Power Rating",
            "questionType": "fill-blank",
            "question": "15. Engine maximum operating parameters at different power rating :",
            "answer": "Takeoff: 990°C / 101.15% | 30 min OEI: 990°C / 101.15% | Continuous OEI: 955°C / 99.0% | Cruising 1: 910°C / 97.5% | Cruising 2: 870°C / 95.5% | Idle: 780°C / See Fig 3.3",
            "acceptedAnswers": ["Takeoff 990 / 101.15, Cruising 1 910 / 97.5"],
            "unit": "",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 6,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Takeoff (both engine operating and 2,5 min power OEI) (contingency)",
                    "answer": "990 °C / 101.15 %",
                    "acceptedAnswers": ["990 / 101.15", "990 dan 101.15", "990/101.15"],
                    "unit": "°C / %",
                    "placeholder": "Max gas temp / Max turbine speed..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "30, min power OEI takeoff",
                    "answer": "990 °C / 101.15 %",
                    "acceptedAnswers": ["990 / 101.15", "990 dan 101.15", "990/101.15"],
                    "unit": "°C / %",
                    "placeholder": "Max gas temp / Max turbine speed..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Continuous power OEI (normal)",
                    "answer": "955 °C / 99.0 %",
                    "acceptedAnswers": ["955 / 99.0", "955 dan 99.0", "955 / 99", "955/99"],
                    "unit": "°C / %",
                    "placeholder": "Max gas temp / Max turbine speed..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Cruising 1",
                    "answer": "910 °C / 97.5 %",
                    "acceptedAnswers": ["910 / 97.5", "910 dan 97.5", "910/97.5"],
                    "unit": "°C / %",
                    "placeholder": "Max gas temp / Max turbine speed..."
                },
                {
                    "id": "sub_e",
                    "letter": "e",
                    "label": "Cruising 2",
                    "answer": "870 °C / 95.5 %",
                    "acceptedAnswers": ["870 / 95.5", "870 dan 95.5", "870/95.5"],
                    "unit": "°C / %",
                    "placeholder": "Max gas temp / Max turbine speed..."
                },
                {
                    "id": "sub_f",
                    "letter": "f",
                    "label": "Idle",
                    "answer": "780 °C / See Fig 3.3",
                    "acceptedAnswers": ["780 / See Fig 3.3", "780", "See Fig 3.3", "780 C"],
                    "unit": "°C",
                    "placeholder": "Max gas temp / Max turbine speed..."
                }
            ]
        },
        # 16. Engine operating parameter
        {
            "id": "MI17-LIM-016",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Engine Operating Parameter",
            "questionType": "fill-blank",
            "question": "16. Engine operating parameter : (cruising 1 & 2, max continuous, take off oil pressure)",
            "answer": "3.5±0.5 kgf/cm²",
            "acceptedAnswers": ["3.5±0.5", "3.5 +- 0.5", "3.5 ± 0.5", "3.5±0.5 kgf/cm²", "3.5+-0.5"],
            "unit": "kgf/cm²",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 1,
            "verified": True
        },
        # 17. Characteristics of the Main Gear Box: Oil Pressure
        {
            "id": "MI17-LIM-017",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Main Gear Box",
            "questionType": "fill-blank",
            "question": "17. Characteristics of the Main Gear Box: Oil Pressure",
            "answer": "a. At idle 0.5 kgf/cm2, min | b. In sideslip flight (for not more than 30 s) 2.5 kgf/cm2, min | c. At other power rattings 3.5 ± 0.5 kgf/cm2",
            "acceptedAnswers": ["0.5, 2.5, 3.5±0.5", "0.5 kgf/cm2, 2.5 kgf/cm2, 3.5 ± 0.5 kgf/cm2"],
            "unit": "kgf/cm2",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 3,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "At idle",
                    "answer": "0.5 kgf/cm2, min",
                    "acceptedAnswers": ["0.5", "0,5", "0.5 kgf/cm2", "0.5 kgf/cm2, min", "0.5 min"],
                    "unit": "kgf/cm2",
                    "placeholder": "Tekanan oli idle..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "In sideslip flight (for not more than 30 s)",
                    "answer": "2.5 kgf/cm2, min",
                    "acceptedAnswers": ["2.5", "2,5", "2.5 kgf/cm2", "2.5 kgf/cm2, min", "2.5 min"],
                    "unit": "kgf/cm2",
                    "placeholder": "Tekanan oli sideslip..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "At other power rattings",
                    "answer": "3.5 ± 0.5 kgf/cm2",
                    "acceptedAnswers": ["3.5 ± 0.5", "3.5 +- 0.5", "3,5 +- 0,5", "3.5 ± 0.5 kgf/cm2", "3.0 - 4.0", "3-4", "3.5±0.5"],
                    "unit": "kgf/cm2",
                    "placeholder": "Tekanan oli rating lainnya..."
                }
            ]
        },
        # 18. Main gearbox inlet oil temperature at all power rattings
        {
            "id": "MI17-LIM-018",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Main Gear Box",
            "questionType": "fill-blank",
            "question": "18. Main gearbox inlet oil temperature at all power rattings :",
            "answer": "a. Maximum 90°C, max | b. Recomended 50 to 80°C | c. Min accel from idle -15°C | d. Min continuous +30°C | e. Min starting without heating -40°C | f. Max temp tail & intermediate boxes 110°C",
            "acceptedAnswers": ["90, 50-80, -15, +30, -40, 110"],
            "unit": "°C",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 6,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Maximum",
                    "answer": "90°C, max",
                    "acceptedAnswers": ["90", "90°C", "90 C", "90°C, max", "90 max", "900C", "900c"],
                    "unit": "°C",
                    "placeholder": "Suhu oli maksimum..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Recomended",
                    "answer": "50 to 80°C",
                    "acceptedAnswers": ["50 to 80", "50 - 80", "50-80", "50 sampai 80", "50 to 80°C", "50-80°C", "50 to 800C"],
                    "unit": "°C",
                    "placeholder": "Suhu oli rekomendasi..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Minimum allowed for acceleration from idle up to operational power ratings",
                    "answer": "-15°C",
                    "acceptedAnswers": ["-15", "-15°C", "-15 C", "-150C"],
                    "unit": "°C",
                    "placeholder": "Suhu minimum akselerasi..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Minimum allowed for continuous operation",
                    "answer": "+30°C",
                    "acceptedAnswers": ["+30", "30", "+30°C", "30°C", "+30 C", "+300C"],
                    "unit": "°C",
                    "placeholder": "Suhu minimum kontinu..."
                },
                {
                    "id": "sub_e",
                    "letter": "e",
                    "label": "Minimum allowed for starting the engines without main gearbox heating",
                    "answer": "-40°C",
                    "acceptedAnswers": ["-40", "-40°C", "-40 C", "-400C"],
                    "unit": "°C",
                    "placeholder": "Suhu minimum start tanpa pemanas..."
                },
                {
                    "id": "sub_f",
                    "letter": "f",
                    "label": "The maximum oil temperature in the tail and intermediate gear boxes is",
                    "answer": "110°C",
                    "acceptedAnswers": ["110", "110°C", "110 C", "1100C"],
                    "unit": "°C",
                    "placeholder": "Suhu maksimum tail gearbox..."
                }
            ]
        },
        # 19. APU
        {
            "id": "MI17-LIM-019",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "APU",
            "questionType": "fill-blank",
            "question": "19. APU (The maximum allowed TGT of APU engine & generator mode time)",
            "answer": "a. At start 880 °C | b. At idle 720 °C | c. At air bleed and generators modes 750 °C | d. Maximum continuous operation time on generator mode 30 min",
            "acceptedAnswers": ["880, 720, 750, 30 min"],
            "unit": "",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 4,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "The maximum allowed TGT of APU engine: At start",
                    "answer": "880 °C",
                    "acceptedAnswers": ["880", "880 °C", "880°C", "880 C"],
                    "unit": "°C",
                    "placeholder": "TGT APU start..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "At idle",
                    "answer": "720 °C",
                    "acceptedAnswers": ["720", "720 °C", "720°C", "720 C"],
                    "unit": "°C",
                    "placeholder": "TGT APU idle..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "At air bleed and generators modes",
                    "answer": "750 °C",
                    "acceptedAnswers": ["750", "750 °C", "750°C", "750 C"],
                    "unit": "°C",
                    "placeholder": "TGT APU air bleed & generator..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Maximum continuous operation time on generator mode",
                    "answer": "30 min",
                    "acceptedAnswers": ["30", "30 min", "30 menit", "30 minutes"],
                    "unit": "min",
                    "placeholder": "Waktu maksimum generator..."
                }
            ]
        },
        # 20. Slopes field without shutdown
        {
            "id": "MI17-LIM-020",
            "aircraft": "MI-17V5",
            "section": "Take off and Landing slopes field",
            "category": "Slope Landing",
            "questionType": "fill-blank",
            "question": "20. The maximum slopes of fields used for vertical takeoff and landing without shutdown of the engine are listened below:",
            "answer": "a. 7° for uphill headed (depan) | b. 5° for downhill headed (belakang) | c. 7° for LH side uphill position (Kiri) | d. 3° for RH side uphill position (kanan)",
            "acceptedAnswers": ["7°, 5°, 7°, 3°", "7, 5, 7, 3"],
            "unit": "°",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 4,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "For uphill headed (depan)",
                    "answer": "7°",
                    "acceptedAnswers": ["7", "7°", "7 deg", "7 degrees", "7 o"],
                    "unit": "°",
                    "placeholder": "Kemiringan depan..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "For downhill headed (belakang)",
                    "answer": "5°",
                    "acceptedAnswers": ["5", "5°", "5 deg", "5 degrees", "5 o"],
                    "unit": "°",
                    "placeholder": "Kemiringan belakang..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "For LH side uphill position (Kiri)",
                    "answer": "7°",
                    "acceptedAnswers": ["7", "7°", "7 deg", "7 degrees", "7 o"],
                    "unit": "°",
                    "placeholder": "Kemiringan kiri..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "For RH side uphill position (kanan)",
                    "answer": "3°",
                    "acceptedAnswers": ["3", "3°", "3 deg", "3 degrees", "3 o"],
                    "unit": "°",
                    "placeholder": "Kemiringan kanan..."
                }
            ]
        },
        # 21. Slopes field with shutdown
        {
            "id": "MI17-LIM-021",
            "aircraft": "MI-17V5",
            "section": "Take off and Landing slopes field",
            "category": "Slope Landing",
            "questionType": "fill-blank",
            "question": "21. The maximum slopes of fields used for vertical takeoff and landing maximal with shutdown engine after touchdown are listed below :",
            "answer": "a. 3° for uphill and downhill headed position, and LH side uphill position | b. 3° for RH side uphill position",
            "acceptedAnswers": ["3°, 3°", "3, 3"],
            "unit": "°",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "For uphill and downhill headed position, and LH side uphill position",
                    "answer": "3°",
                    "acceptedAnswers": ["3", "3°", "3 deg", "3 degrees", "3 o"],
                    "unit": "°",
                    "placeholder": "Kemiringan depan/belakang/kiri..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "For RH side uphill position",
                    "answer": "3°",
                    "acceptedAnswers": ["3", "3°", "3 deg", "3 degrees", "3 o"],
                    "unit": "°",
                    "placeholder": "Kemiringan kanan..."
                }
            ]
        },
        # 22. Eksternal Load
        {
            "id": "MI17-MAN-022",
            "aircraft": "MI-17V5",
            "section": "Manuever Khusus",
            "category": "Eksternal Load",
            "questionType": "fill-blank",
            "question": "22. Eksternal Load",
            "answer": "a. MTOW 13.000 Kg | b. Berat Max Load 4.000 Kg | c. Max Speed 200 Km/jam | d. Max Turn/bank 15°",
            "acceptedAnswers": ["13000 kg, 4000 kg, 200 km/h, 15°"],
            "unit": "",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 4,
            "points": 4,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "MTOW",
                    "answer": "13.000 Kg",
                    "acceptedAnswers": ["13.000", "13000", "13.000 Kg", "13000 kg", "13,000"],
                    "unit": "Kg",
                    "placeholder": "MTOW eksternal load..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Berat Max Load",
                    "answer": "4.000 Kg",
                    "acceptedAnswers": ["4.000", "4000", "4.000 Kg", "4000 kg", "4,000"],
                    "unit": "Kg",
                    "placeholder": "Berat muatan maksimum..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Max Speed",
                    "answer": "200 Km/jam",
                    "acceptedAnswers": ["200", "200 Km/jam", "200 km/h", "200km/h"],
                    "unit": "Km/jam",
                    "placeholder": "Kecepatan maksimum..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Max Turn/bank",
                    "answer": "15°",
                    "acceptedAnswers": ["15", "15°", "15 deg", "15 degrees", "15 0"],
                    "unit": "°",
                    "placeholder": "Kemiringan belok maksimum..."
                }
            ]
        },
        # 23. Fastrooping/Rappeling
        {
            "id": "MI17-MAN-023",
            "aircraft": "MI-17V5",
            "section": "Manuever Khusus",
            "category": "Fastrooping/Rappeling",
            "questionType": "fill-blank",
            "question": "23. Fastrooping/Rappeling",
            "answer": "a. Max berat 1 orang 100 Kg | b. Headwind, max Wind Speed 10 m/s | c. Min Altitude 45 m | d. Pelaksanaan di hutan jarak dari ujung pohon tidak kurang dari 10 m",
            "acceptedAnswers": ["100 kg, 10 m/s, 45 m, 10 m"],
            "unit": "",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 4,
            "points": 4,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Max berat 1 orang",
                    "answer": "100 Kg",
                    "acceptedAnswers": ["100", "100 Kg", "100 kg"],
                    "unit": "Kg",
                    "placeholder": "Berat per personel..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Headwind, max Wind Speed",
                    "answer": "10 m/s",
                    "acceptedAnswers": ["10", "10 m/s", "10m/s"],
                    "unit": "m/s",
                    "placeholder": "Kecepatan angin sakal max..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Min Altitude",
                    "answer": "45 m",
                    "acceptedAnswers": ["45", "45 m", "45m"],
                    "unit": "m",
                    "placeholder": "Ketinggian minimum..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Pelaksanaan di hutan jarak dari ujung pohon tidak kurang dari",
                    "answer": "10 m",
                    "acceptedAnswers": ["10", "10 m", "10m"],
                    "unit": "m",
                    "placeholder": "Jarak dari ujung pohon..."
                }
            ]
        },
        # 24. Hoist
        {
            "id": "MI17-MAN-024",
            "aircraft": "MI-17V5",
            "section": "Manuever Khusus",
            "category": "Hoist",
            "questionType": "fill-blank",
            "question": "24. Hoist",
            "answer": "a. Max weight hoisted 300 kg at hovering 50 - 55 m | b. Max hover height 55 m (panjang tali 60 m) | c. Max hover di atas air untuk hoist 20 m",
            "acceptedAnswers": ["300 kg, 55 m, 20 m"],
            "unit": "",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 4,
            "points": 3,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Max weight hoisted",
                    "answer": "300 kg at hovering 50 - 55 m",
                    "acceptedAnswers": ["300 kg at hovering 50 - 55 m", "300 kg at hovering 50-55 m", "300 kg", "300", "300kg"],
                    "unit": "kg",
                    "placeholder": "Beban angkat hoist..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Max hover height",
                    "answer": "55 m (panjang tali 60 m)",
                    "acceptedAnswers": ["55 m (panjang tali 60 m)", "55 m", "55", "55m"],
                    "unit": "m",
                    "placeholder": "Ketinggian hover..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Max hover di atas air untuk hoist",
                    "answer": "20 m",
                    "acceptedAnswers": ["20", "20 m", "20m"],
                    "unit": "m",
                    "placeholder": "Ketinggian hover atas air..."
                }
            ]
        },
        # 25. Fuel Reserve 320 L dan 270 L
        {
            "id": "MI17-MAN-025",
            "aircraft": "MI-17V5",
            "section": "Manuever Khusus",
            "category": "Fuel Reserve",
            "questionType": "fill-blank",
            "question": "25. Fuel Reserve 320 L dan 270 L",
            "answer": "a. 320 L = 21 minutes, 500 meter, 220 km/jam, 70 km | b. 270 L = 17 minutes, 500 meter, 220 km/jam, 55 km",
            "acceptedAnswers": ["21 min / 500m / 220km/h / 70km, 17 min / 500m / 220km/h / 55km"],
            "unit": "",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 4,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "320 L (waktu, ketinggian, kecepatan, jarak)",
                    "answer": "21 minutes, 500 meter, 220 km/jam, 70 km",
                    "acceptedAnswers": [
                        "21 minutes ... 500 meter ... 220 km/jam ... 70 km",
                        "21 minutes, 500 meter, 220 km/jam, 70 km",
                        "21 min, 500 m, 220 km/h, 70 km",
                        "21 menit, 500 meter, 220 km/jam, 70 km",
                        "21, 500, 220, 70"
                    ],
                    "placeholder": "21 minutes ... 500 meter ... 220 km/jam ... 70 km"
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "270 L (waktu, ketinggian, kecepatan, jarak)",
                    "answer": "17 minutes, 500 meter, 220 km/jam, 55 km",
                    "acceptedAnswers": [
                        "17 minutes ... 500 meter ... 220 km/jam ... 55 km",
                        "17 minutes, 500 meter, 220 km/jam, 55 km",
                        "17 min, 500 m, 220 km/h, 55 km",
                        "17 menit, 500 meter, 220 km/jam, 55 km",
                        "17, 500, 220, 55"
                    ],
                    "placeholder": "17 minutes ... 500 meter ... 220 km/jam ... 55 km"
                }
            ]
        }
    ]

    return {
        "aircraft": "MI-17V5",
        "title": "BOLD FACE MI-17V5",
        "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
        "description": "Limitation, Engine Operating Parameters, Gearbox, APU, Slopes, dan Maneuver Khusus Helikopter MI-17V5",
        "totalQuestions": len(questions),
        "questions": questions
    }

def main():
    os.makedirs("data", exist_ok=True)
    mi17 = build_mi17v5()
    with open("data/mi-17v5.json", "w", encoding="utf-8") as f:
        json.dump(mi17, f, indent=2, ensure_ascii=False)
    print(f"Generated data/mi-17v5.json with {mi17['totalQuestions']} items.")

if __name__ == "__main__":
    main()
