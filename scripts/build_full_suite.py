# -*- coding: utf-8 -*-
"""
High-Fidelity Dataset Builder for Aviation Examination & Training Platform
Accurately aligns multi-answer boldface items (1... a., b., c.) with original PDF documents.
"""
import json
import os
import glob

def build_casa212():
    questions = [
        {
            "id": "CASA212-BF-001",
            "aircraft": "CASA 212-200",
            "section": "BOLD FACE",
            "category": "Electrical Fire",
            "questionType": "fill-blank",
            "question": "1. Electrical fire on ground",
            "answer": "a. Master switch Off | b. APU Off & disconnect",
            "acceptedAnswers": [
                "Master switch Off, APU Off & disconnect",
                "Off, Off & disconnect"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE CASA 212-200 AVIOCAR.pdf",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Master switch",
                    "answer": "Off",
                    "acceptedAnswers": ["Off", "OFF"],
                    "placeholder": "Posisi Master switch..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "APU",
                    "answer": "Off & disconnect",
                    "acceptedAnswers": [
                        "Off & disconnect", "Off and disconnect", "Off & Disconnect",
                        "Off dan disconnect", "OFF & DISCONNECT", "OFF AND DISCONNECT",
                        "Off disconnect"
                    ],
                    "placeholder": "Posisi APU..."
                }
            ]
        },
        {
            "id": "CASA212-BF-002",
            "aircraft": "CASA 212-200",
            "section": "BOLD FACE",
            "category": "Engine Fire on Ground",
            "questionType": "fill-blank",
            "question": "2. Engine fire on the ground",
            "answer": "a. Fuel switch Close | b. Emergency shut down lever Feather | c. Fuel booster pumps Off | d. Heating lever Close | e. Air Conditioning Off | f. Fire discharge buttons Press as required",
            "acceptedAnswers": [
                "Close, Feather, Off, Close, Off, Press as required"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE CASA 212-200 AVIOCAR.pdf",
            "sourcePage": 1,
            "points": 6,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Fuel switch",
                    "answer": "Close",
                    "acceptedAnswers": ["Close", "CLOSE", "Tutup"],
                    "placeholder": "Posisi Fuel switch..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Emergency shut down lever",
                    "answer": "Feather",
                    "acceptedAnswers": ["Feather", "FEATHER"],
                    "placeholder": "Posisi Emergency shut down lever..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Fuel booster pumps",
                    "answer": "Off",
                    "acceptedAnswers": ["Off", "OFF"],
                    "placeholder": "Posisi Fuel booster pumps..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Heating lever",
                    "answer": "Close",
                    "acceptedAnswers": ["Close", "CLOSE", "Tutup"],
                    "placeholder": "Posisi Heating lever..."
                },
                {
                    "id": "sub_e",
                    "letter": "e",
                    "label": "Air Conditioning",
                    "answer": "Off",
                    "acceptedAnswers": ["Off", "OFF"],
                    "placeholder": "Posisi Air Conditioning..."
                },
                {
                    "id": "sub_f",
                    "letter": "f",
                    "label": "Fire discharge buttons",
                    "answer": "Press as required",
                    "acceptedAnswers": ["Press as required", "Press as req", "Press", "PRESS", "Press As Required"],
                    "placeholder": "Tindakan Fire discharge buttons..."
                }
            ]
        },
        {
            "id": "CASA212-BF-003",
            "aircraft": "CASA 212-200",
            "section": "BOLD FACE",
            "category": "Engine Failure before V1",
            "questionType": "fill-blank",
            "question": "3. Engine failure before V1 ( aborted take off )",
            "answer": "a. Power lever Aft of F.I | b. Control collum Full forward | c. Rudder Into dead engine | d. Brake As Required | e. Power lever Reverse as required",
            "acceptedAnswers": [
                "Aft of F.I, Full forward, Into dead engine, As Required, Reverse as required"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE CASA 212-200 AVIOCAR.pdf",
            "sourcePage": 1,
            "points": 5,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Power lever",
                    "answer": "Aft of F.I",
                    "acceptedAnswers": ["Aft of F.I", "Aft of FI", "Aft of F.I.", "Aft of F I"],
                    "placeholder": "Posisi Power lever..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Control collum",
                    "answer": "Full forward",
                    "acceptedAnswers": ["Full forward", "Full Forward", "FULL FORWARD"],
                    "placeholder": "Posisi Control column..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Rudder",
                    "answer": "Into dead engine",
                    "acceptedAnswers": ["Into dead engine", "Into dead eng", "Dead engine"],
                    "placeholder": "Arah Rudder..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Brake",
                    "answer": "As Required",
                    "acceptedAnswers": ["As Required", "As required", "As req", "AS REQUIRED"],
                    "placeholder": "Aplikasi Brake..."
                },
                {
                    "id": "sub_e",
                    "letter": "e",
                    "label": "Power lever",
                    "answer": "Reverse as required",
                    "acceptedAnswers": ["Reverse as required", "Reverse as req", "Reverse", "REVERSE AS REQUIRED"],
                    "placeholder": "Posisi Power lever lanjutan..."
                }
            ]
        },
        {
            "id": "CASA212-BF-004",
            "aircraft": "CASA 212-200",
            "section": "BOLD FACE",
            "category": "Engine Failure after V1",
            "questionType": "fill-blank",
            "question": "4. Engine failure / fire after V1 ( in flight )",
            "answer": "a. Speed lever Take off / landing | b. Power lever Max | c. Flaps As required | d. Maintain flight path | e. Identify and verify failed angine | f. APR light Check | g. Fuel switch Off | h. Emergency shut down engine Feather | i. Fuel booster pump Off | j. Heating lever Close | k. Air conditioning Off | l. IF FIRE Discharge no. 1 Press | m. IF FIRE Discharge no. 2 Press",
            "acceptedAnswers": [
                "Take off / landing, Max, As required, Maintain flight path, Identify and verify failed engine, Check, Off, Feather, Off, Close, Off, Press, Press"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE CASA 212-200 AVIOCAR.pdf",
            "sourcePage": 1,
            "points": 11,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Speed lever",
                    "answer": "Take off / landing",
                    "acceptedAnswers": ["Take off / landing", "Take off/landing", "Take off and landing", "Take off"],
                    "placeholder": "Posisi Speed lever..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Power lever",
                    "answer": "Max",
                    "acceptedAnswers": ["Max", "MAX", "Maximum"],
                    "placeholder": "Posisi Power lever..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Flaps",
                    "answer": "As required",
                    "acceptedAnswers": ["As required", "As Required", "As req"],
                    "placeholder": "Posisi Flaps..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Maintain flight path",
                    "answer": "Maintain flight path",
                    "acceptedAnswers": ["Maintain flight path", "Maintain", "Keep flight path"],
                    "placeholder": "Maintain flight path..."
                },
                {
                    "id": "sub_e",
                    "letter": "e",
                    "label": "Identify and verify failed angine",
                    "answer": "Identify and verify failed engine",
                    "acceptedAnswers": ["Identify and verify failed angine", "Identify and verify failed engine", "Identify and verify", "Verify"],
                    "placeholder": "Identify and verify..."
                },
                {
                    "id": "sub_f",
                    "letter": "f",
                    "label": "APR light",
                    "answer": "Check",
                    "acceptedAnswers": ["Check", "CHECK"],
                    "placeholder": "Kondisi APR light..."
                },
                {
                    "id": "sub_g",
                    "letter": "g",
                    "label": "Fuel switch",
                    "answer": "Off",
                    "acceptedAnswers": ["Off", "OFF"],
                    "placeholder": "Posisi Fuel switch..."
                },
                {
                    "id": "sub_h",
                    "letter": "h",
                    "label": "Emergency shut down engine",
                    "answer": "Feather",
                    "acceptedAnswers": ["Feather", "FEATHER"],
                    "placeholder": "Tindakan shutdown engine..."
                },
                {
                    "id": "sub_i",
                    "letter": "i",
                    "label": "Fuel booster pump",
                    "answer": "Off",
                    "acceptedAnswers": ["Off", "OFF"],
                    "placeholder": "Posisi Fuel booster pump..."
                },
                {
                    "id": "sub_j",
                    "letter": "j",
                    "label": "Heating lever",
                    "answer": "Close",
                    "acceptedAnswers": ["Close", "CLOSE", "Tutup"],
                    "placeholder": "Posisi Heating lever..."
                },
                {
                    "id": "sub_k",
                    "letter": "k",
                    "label": "Air conditioning",
                    "answer": "Off",
                    "acceptedAnswers": ["Off", "OFF"],
                    "placeholder": "Posisi Air conditioning..."
                }
            ]
        },
        {
            "id": "CASA212-BF-004B",
            "aircraft": "CASA 212-200",
            "section": "BOLD FACE",
            "category": "Engine Failure after V1",
            "questionType": "fill-blank",
            "question": "IF FIRE (Engine failure / fire after V1)",
            "answer": "a. Discharge no. 1 Press | b. Discharge no. 2 Press",
            "acceptedAnswers": [
                "Discharge no. 1 Press, Discharge no. 2 Press",
                "Press, Press"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE CASA 212-200 AVIOCAR.pdf",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Discharge no. 1",
                    "answer": "Press",
                    "acceptedAnswers": ["Press", "PRESS"],
                    "placeholder": "Tindakan Discharge no. 1..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Discharge no. 2 (If after 30 sec fire warning light remains ON)",
                    "answer": "Press",
                    "acceptedAnswers": ["Press", "PRESS"],
                    "placeholder": "Tindakan Discharge no. 2..."
                }
            ]
        },
        {
            "id": "CASA212-BF-005",
            "aircraft": "CASA 212-200",
            "section": "BOLD FACE",
            "category": "Smoke and Fume Elimination",
            "questionType": "fill-blank",
            "question": "5. Electrical fire in flight switch / smoke and fume elimination",
            "answer": "a. No smoking switch ON | b. Oxygen mask / smoke goggles Donned / 100 % | c. Oxygen main line valve Open | d. Heating lever Close | e. Air conditioning OFF",
            "acceptedAnswers": [
                "ON, Donned / 100 %, Open, Close, OFF"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE CASA 212-200 AVIOCAR.pdf",
            "sourcePage": 1,
            "points": 5,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "No smoking switch",
                    "answer": "ON",
                    "acceptedAnswers": ["ON", "On"],
                    "placeholder": "Posisi No smoking switch..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Oxygen mask / smoke goggles",
                    "answer": "Donned / 100 %",
                    "acceptedAnswers": ["Donned / 100 %", "Donned / 100%", "Donned/100%", "Donned 100%", "Donned"],
                    "placeholder": "Status Oxygen mask / smoke goggles..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Oxygen main line valve",
                    "answer": "Open",
                    "acceptedAnswers": ["Open", "OPEN", "Buka"],
                    "placeholder": "Posisi Oxygen main line valve..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Heating lever",
                    "answer": "Close",
                    "acceptedAnswers": ["Close", "CLOSE", "Tutup"],
                    "placeholder": "Posisi Heating lever..."
                },
                {
                    "id": "sub_e",
                    "letter": "e",
                    "label": "Air conditioning",
                    "answer": "OFF",
                    "acceptedAnswers": ["OFF", "Off"],
                    "placeholder": "Posisi Air conditioning..."
                }
            ]
        },
        {
            "id": "CASA212-BF-006",
            "aircraft": "CASA 212-200",
            "section": "BOLD FACE",
            "category": "Battery Warning",
            "questionType": "fill-blank",
            "question": "6. Battery over temperature warning (Affected battery)",
            "answer": "OFF",
            "acceptedAnswers": ["OFF", "Off", "Affected battery OFF", "Affected battery Off"],
            "unit": "",
            "sourceDocument": "BOLD FACE CASA 212-200 AVIOCAR.pdf",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "CASA212-BF-007",
            "aircraft": "CASA 212-200",
            "section": "BOLD FACE",
            "category": "Generator Failure",
            "questionType": "fill-blank",
            "question": "7. Two generator fail",
            "answer": "a. Bustied switch Emergency | b. Generator Reset / ON",
            "acceptedAnswers": [
                "Emergency, Reset / ON",
                "Emergency, Reset/ON"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE CASA 212-200 AVIOCAR.pdf",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Bustied switch",
                    "answer": "Emergency",
                    "acceptedAnswers": ["Emergency", "EMERGENCY"],
                    "placeholder": "Posisi Bustied switch..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Generator",
                    "answer": "Reset / ON",
                    "acceptedAnswers": ["Reset / ON", "Reset/ON", "Reset ON", "Reset / On", "RESET / ON"],
                    "placeholder": "Tindakan Generator..."
                }
            ]
        },
        {
            "id": "CASA212-BF-008",
            "aircraft": "CASA 212-200",
            "section": "BOLD FACE",
            "category": "Multiple Engine Failure",
            "questionType": "fill-blank",
            "question": "8. Multiple engine failure",
            "answer": "a. Emergency shut down lever Feather | b. Flaps 0° | c. Bustied switch Emergency",
            "acceptedAnswers": [
                "Feather, 0°, Emergency",
                "Feather, 0 deg, Emergency"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE CASA 212-200 AVIOCAR.pdf",
            "sourcePage": 1,
            "points": 3,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Emergency shut down lever",
                    "answer": "Feather",
                    "acceptedAnswers": ["Feather", "FEATHER"],
                    "placeholder": "Posisi Emergency shut down lever..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Flaps",
                    "answer": "0°",
                    "acceptedAnswers": ["0°", "0 deg", "0 degree", "0", "0 degrees"],
                    "placeholder": "Posisi Flaps..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Bustied switch",
                    "answer": "Emergency",
                    "acceptedAnswers": ["Emergency", "EMERGENCY"],
                    "placeholder": "Posisi Bustied switch..."
                }
            ]
        }
    ]

    return {
        "aircraft": "CASA 212-200",
        "title": "BOLD FACE CASA 212-200 AVIOCAR",
        "sourceDocument": "BOLD FACE CASA 212-200 AVIOCAR.pdf",
        "description": "Prosedur Bold Face Darurat Lengkap CASA 212-200 Aviocar",
        "totalQuestions": len(questions),
        "questions": questions
    }

def build_fennec_as550_full():
    items = [
        {
            "num": 1,
            "cat": "Weight Limitation",
            "q": "1. Maximum & Minimum internal weight for flight, take-off and landing with non-jettisonable load",
            "subs": [
                ("a", "Maximum internal weight for flight, take-off and landing with non-jettisonable load", "2250 kg", ["2250", "2.250", "2250 kg", "2250kg", "2,250"], "kg"),
                ("b", "Minimum internal weight for flight, take-off and landing", "1310 kg", ["1310", "1.310", "1310 kg", "1310kg", "1,310"], "kg")
            ]
        },
        {
            "num": 2,
            "cat": "VNE Limitation",
            "q": "2. VNE power off and power On",
            "subs": [
                ("a", "VNE power off", "125 kts", ["125", "125 kts", "125 kias", "125 knots"], "kts"),
                ("b", "VNE power On", "155 kts", ["155", "155 kts", "155 kias", "155 knots"], "kts")
            ]
        },
        {
            "num": 3,
            "cat": "Maximum Operating Altitude",
            "q": "3. Maximum operating Altitude",
            "ans": "23.000 ft",
            "acc": ["23.000", "23000", "23.000 ft", "23000 ft", "23,000"],
            "unit": "ft"
        },
        {
            "num": 4,
            "cat": "Slope Landing Limitation",
            "q": "4. Landing and rotor stopping limitation on slope",
            "subs": [
                ("a", "Nose up", "10°", ["10", "10°", "10 deg", "10 degrees"], "°"),
                ("b", "Nose down", "6°", ["6", "6°", "6 deg", "6 degrees"], "°"),
                ("c", "Sideways", "8°", ["8", "8°", "8 deg", "8 degrees"], "°")
            ]
        },
        {
            "num": 5,
            "cat": "Running Landing",
            "q": "5. Excluding emergencies and failures, maximum speed for performing running landings",
            "ans": "40 kts",
            "acc": ["40", "40 kts", "40 kias", "40 knots"],
            "unit": "kts"
        },
        {
            "num": 6,
            "cat": "Main Rotor Limitation",
            "q": "6. MAIN ROTOR LIMITATION",
            "subs": [
                ("a", "Rotor Brake operation max. speed", "170 rpm", ["170", "170 rpm"], "rpm"),
                ("b", "Minimum power off", "320 rpm", ["320", "320 rpm"], "rpm"),
                ("c", "Caution Range I", "320 to 375 rpm", ["320 to 375", "320 - 375", "320-375", "320 sampai 375"], "rpm"),
                ("d", "Normal operation range", "375 to 405 rpm", ["375 to 405", "375 - 405", "375-405", "375 sampai 405"], "rpm"),
                ("e", "Caution range II", "405 to 430 rpm", ["405 to 430", "405 - 430", "405-430", "405 sampai 430"], "rpm"),
                ("f", "Max power off", "430 rpm", ["430", "430 rpm"], "rpm"),
                ("g", "LOW AURAL WARNING", "< 360 rpm", ["< 360", "<360", "< 360 rpm", "360"], "rpm"),
                ("h", "HIGH AURAL WARNING", "> 410 rpm", ["> 410", ">410", "> 410 rpm", "410"], "rpm")
            ]
        },
        {
            "num": 7,
            "cat": "First Limitation Indicator",
            "q": "7. FIRST LIMITITATION INDICATOR",
            "subs": [
                ("a", "Max continuous rating", "9,6", ["9.6", "9,6"], ""),
                ("b", "Take off power", "9,6 to 10", ["9.6 to 10", "9,6 to 10", "9.6 - 10", "9,6 - 10", "9.6-10", "9,6 sampai 10"], ""),
                ("c", "Max take off rating", "10", ["10"], ""),
                ("d", "Max transient rating (5 sec)", "10,4", ["10.4", "10,4"], "")
            ]
        },
        {
            "num": 8,
            "cat": "Torque Transmission Limitation",
            "q": "8. TORQUE TRANSMISSION LIMITATION",
            "subs": [
                ("a", "Max continuous rating", "92,7 %", ["92.7", "92,7", "92.7 %", "92,7 %"], "%"),
                ("b", "Take off power", "92,7 to 100 %", ["92.7 to 100", "92,7 to 100", "92.7 - 100", "92,7 - 100", "92.7 sampai 100"], "%"),
                ("c", "Max take off rating", "100 %", ["100", "100 %", "100%"], "%"),
                ("d", "Max transient rating (5 sec)", "104 %", ["104", "104 %", "104%"], "%")
            ]
        },
        {
            "num": 9,
            "cat": "N2 Limitation",
            "q": "9. N2 LIMITATION",
            "subs": [
                ("a", "Minimum", "367 rpm", ["367", "367 rpm"], "rpm"),
                ("b", "Normal operating range", "367 to 413 rpm", ["367 to 413", "367 - 413", "367-413", "367 sampai 413"], "rpm"),
                ("c", "Max continuous", "413 rpm", ["413", "413 rpm"], "rpm"),
                ("d", "Max Transient Limit (20 sec)", "440 rpm", ["440", "440 rpm"], "rpm")
            ]
        },
        {
            "num": 10,
            "cat": "N1 Limitation",
            "q": "10. N1 LIMITATION",
            "subs": [
                ("a", "Min Stabilized Speed", "67%", ["67", "67%"], "%"),
                ("b", "Max continuous rating", "∆N1 = -4 (-4 %)", ["-4", "-4%", "-4 %", "∆N1 = -4", "delta N1 = -4"], ""),
                ("c", "Take off power", "∆N1 = -4 % to 0% (-4%)", ["-4% to 0%", "-4 to 0", "-4 sampai 0", "-4% - 0%"], ""),
                ("d", "Max take off rating", "∆N1 = 0 % (0 %)", ["0", "0%", "0 %", "∆N1 = 0", "delta N1 = 0"], ""),
                ("e", "Max transient rating (≤20 sec)", "∆N1 = +1 % (1 %)", ["+1", "1", "1%", "+1%", "+1 %", "∆N1 = +1", "delta N1 = +1"], "")
            ]
        },
        {
            "num": 11,
            "cat": "TOT Limitation",
            "q": "11. TOT LIMITATION",
            "subs": [
                ("a", "STARTING LIMITATION: Max continuous", "750 °C", ["750", "750 °C", "750°C"], "°C"),
                ("b", "STARTING LIMITATION: Max transient (10 sec)", "840 °C", ["840", "840 °C", "840°C"], "°C"),
                ("c", "FLIGHT LIMITATION: Max continuous rating", "905 °C", ["905", "905 °C", "905°C"], "°C"),
                ("d", "FLIGHT LIMITATION: Takeoff power", "905 to 949 °C", ["905 to 949", "905 - 949", "905-949", "905 sampai 949"], "°C"),
                ("e", "FLIGHT LIMITATION: Max takeoff rating", "949 °C", ["949", "949 °C", "949°C"], "°C"),
                ("f", "FLIGHT LIMITATION: Max transient (20 sec)", "981 °C", ["981", "981 °C", "981°C"], "°C")
            ]
        },
        {
            "num": 12,
            "cat": "Oil Limitation",
            "q": "12. Oil temperature and pressure limitation",
            "subs": [
                ("a", "Max oil temperature limitation", "117 °C", ["117", "117 °C", "117°C"], "°C"),
                ("b", "Max oil pressure limitation", "Depend on N1", ["Depend on N1", "Depend on N1 RPM", "Tergantung N1", "Depend on NI"], "")
            ]
        },
        {
            "num": 13,
            "cat": "Electrical Circuit Limitation",
            "q": "13. Electrical circuit limitation & MAX CURRENT",
            "subs": [
                ("a", "Max voltage", "31,5 V (26 - 29 V)", ["31.5", "31,5", "31.5 V", "31,5 V", "26 - 29 V", "31,5 V (26 - 29 V)"], "V"),
                ("b", "MAX CURRENT: Max continuous", "150 A", ["150", "150 A", "150A"], "A"),
                ("c", "MAX CURRENT: Starter generator", "200 A", ["200", "200 A", "200A"], "A")
            ]
        },
        {
            "num": 14,
            "cat": "Baggage Compartment",
            "q": "14. BAGGAGE COMPARTMENT LOAD LIMIT",
            "subs": [
                ("a", "RH cargo compartment", "100 kg", ["100", "100 kg", "100kg"], "kg"),
                ("b", "LH cargo compartment", "120 kg", ["120", "120 kg", "120kg"], "kg"),
                ("c", "Rear cargo compartment", "80 kg", ["80", "80 kg", "80kg"], "kg")
            ]
        },
        {
            "num": 15,
            "cat": "Cabin Compartment",
            "q": "15. CABIN COMPARTMENT LOAD LIMIT",
            "subs": [
                ("a", "Rear cabin floor", "310 kg", ["310", "310 kg", "310kg"], "kg"),
                ("b", "Forward left cabin floor", "150 kg", ["150", "150 kg", "150kg"], "kg")
            ]
        }
    ]

    questions = []
    for it in items:
        idx = it["num"]
        if "subs" in it:
            sub_objs = []
            for s_let, s_lbl, s_ans, s_acc, s_unit in it["subs"]:
                sub_objs.append({
                    "id": f"sub_{s_let}",
                    "letter": s_let,
                    "label": s_lbl,
                    "answer": s_ans,
                    "acceptedAnswers": s_acc,
                    "unit": s_unit,
                    "placeholder": f"Nilai {s_lbl}..."
                })
            full_ans = " | ".join([f"{s['letter']}. {s['label']} {s['answer']}" for s in sub_objs])
            q_obj = {
                "id": f"FENNEC-LIM-{idx:03d}",
                "aircraft": "FENNEC AS550",
                "section": "LIMITATION",
                "category": it["cat"],
                "questionType": "fill-blank",
                "question": it["q"],
                "answer": full_ans,
                "acceptedAnswers": [", ".join([s["answer"] for s in sub_objs])],
                "unit": "",
                "sourceDocument": "BOLD FACE FENNEC AS550.docx",
                "sourcePage": 1 if idx <= 8 else 2,
                "points": len(sub_objs),
                "verified": True,
                "subQuestions": sub_objs
            }
        else:
            q_obj = {
                "id": f"FENNEC-LIM-{idx:03d}",
                "aircraft": "FENNEC AS550",
                "section": "LIMITATION",
                "category": it["cat"],
                "questionType": "fill-blank",
                "question": it["q"],
                "answer": it["ans"],
                "acceptedAnswers": it["acc"],
                "unit": it["unit"],
                "sourceDocument": "BOLD FACE FENNEC AS550.docx",
                "sourcePage": 1 if idx <= 8 else 2,
                "points": 1,
                "verified": True
            }
        questions.append(q_obj)

    return {
        "aircraft": "FENNEC AS550",
        "title": "BOLD FACE FENNEC AS550",
        "sourceDocument": "BOLD FACE FENNEC AS550.docx",
        "description": "Limitation Weight, Speed, Altitude, Rotor, FLI, Torque, N1, N2, TOT, Electrical, dan Cargo Helikopter FENNEC AS550",
        "totalQuestions": len(questions),
        "questions": questions
    }

def main():
    os.makedirs("data", exist_ok=True)
    c212 = build_casa212()
    with open("data/casa-212-200.json", "w", encoding="utf-8") as f:
        json.dump(c212, f, indent=2, ensure_ascii=False)
    print(f"Generated data/casa-212-200.json with {c212['totalQuestions']} items.")

    fennec = build_fennec_as550_full()
    with open("data/fennec-as550.json", "w", encoding="utf-8") as f:
        json.dump(fennec, f, indent=2, ensure_ascii=False)
    print(f"Generated data/fennec-as550.json with {fennec['totalQuestions']} items.")

if __name__ == "__main__":
    main()
