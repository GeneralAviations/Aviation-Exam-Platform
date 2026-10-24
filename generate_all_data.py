# -*- coding: utf-8 -*-
"""
Full Dataset Generator for Aviation Examination & Training Platform
"""
import json
import os

def build_mi17v5():
    questions = [
        # A. ISIAN
        {
            "id": "MI17-ISIAN-001",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Basic Weights & Capacity",
            "questionType": "fill-blank",
            "question": "Normal takeoff weight",
            "answer": "11.100 Kg",
            "acceptedAnswers": ["11.100", "11100", "11.100 Kg", "11100 kg", "11,100"],
            "unit": "Kg",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-ISIAN-002",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Basic Weights & Capacity",
            "questionType": "fill-blank",
            "question": "Maximum takeoff weight",
            "answer": "13.000 Kg",
            "acceptedAnswers": ["13.000", "13000", "13.000 Kg", "13000 kg", "13,000"],
            "unit": "Kg",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-ISIAN-003",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Troop Carrier",
            "questionType": "fill-blank",
            "question": "Troop carrier Maximum",
            "answer": "4.000 Kg",
            "acceptedAnswers": ["4.000", "4000", "4.000 Kg", "4000 kg", "4,000"],
            "unit": "Kg",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-ISIAN-004",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Troop Carrier",
            "questionType": "fill-blank",
            "question": "Troop carrier Numb Troopers carried",
            "answer": "36 Orang",
            "acceptedAnswers": ["36", "36 Orang", "36 orang", "36 person"],
            "unit": "Orang",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-ISIAN-005",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Speed",
            "questionType": "fill-blank",
            "question": "Maximum limit speed in horizontal flight at altitude from 0-1000 m (At normal takeoff weight)",
            "answer": "250 km/h",
            "acceptedAnswers": ["250", "250 km/h", "250km/h"],
            "unit": "km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-ISIAN-006",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Speed",
            "questionType": "fill-blank",
            "question": "Maximum limit speed in horizontal flight at altitude from 0-1000 m (At maximum takeoff weight)",
            "answer": "230 km/h",
            "acceptedAnswers": ["230", "230 km/h", "230km/h"],
            "unit": "km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-ISIAN-007",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Cruising Speed",
            "questionType": "fill-blank",
            "question": "Cruising speed at altitude from 0 to 1000 (At normal takeoff weight)",
            "answer": "220 to 230 km/h",
            "acceptedAnswers": ["220 to 230", "220-230", "220 to 230 km/h", "220-230 km/h", "220 sampai 230"],
            "unit": "km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-ISIAN-008",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Cruising Speed",
            "questionType": "fill-blank",
            "question": "Cruising speed at altitude from 0 to 1000 (At maximum takeoff weight)",
            "answer": "205 to 215 km/h",
            "acceptedAnswers": ["205 to 215", "205-215", "205 to 215 km/h", "205-215 km/h", "205 sampai 215"],
            "unit": "km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-ISIAN-009",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Ceiling",
            "questionType": "fill-blank",
            "question": "Hovering ceiling at normal takeoff weight, ISA, air bleed to Dust protection device ejectors being off",
            "answer": "3980 m",
            "acceptedAnswers": ["3980", "3980 m", "3.980", "3.980 m"],
            "unit": "m",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-ISIAN-010",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Ceiling",
            "questionType": "fill-blank",
            "question": "Service ceiling (At Normal takeoff weight)",
            "answer": "6000 m",
            "acceptedAnswers": ["6000", "6000 m", "6.000", "6.000 m"],
            "unit": "m",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-ISIAN-011",
            "aircraft": "MI-17V5",
            "section": "A. ISIAN",
            "category": "Ceiling",
            "questionType": "fill-blank",
            "question": "Service ceiling (At maximum takeoff wieight)",
            "answer": "4800 m",
            "acceptedAnswers": ["4800", "4800 m", "4.800", "4.800 m"],
            "unit": "m",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },

        # LIMITATION
        {
            "id": "MI17-LIM-001",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Weight Limitation",
            "questionType": "fill-blank",
            "question": "Maximum useful load",
            "answer": "4000 kg",
            "acceptedAnswers": ["4000", "4000 kg", "4.000", "4.000 kg"],
            "unit": "kg",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-002",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Weight Limitation",
            "questionType": "fill-blank",
            "question": "Maximum external load weight",
            "answer": "3000 (4000) kg",
            "acceptedAnswers": ["3000 (4000)", "3000 (4000) kg", "3000", "4000", "3000/4000", "3000-4000", "3.000 (4.000) kg"],
            "unit": "kg",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-003",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "CG Limitation",
            "questionType": "fill-blank",
            "question": "Forward CG limit is",
            "answer": "+300 mm",
            "acceptedAnswers": ["+300", "+300 mm", "300", "300 mm", "+300mm"],
            "unit": "mm",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-004",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "CG Limitation",
            "questionType": "fill-blank",
            "question": "Aft CG limit",
            "answer": "-95 mm",
            "acceptedAnswers": ["-95", "-95 mm", "-95mm"],
            "unit": "mm",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-005",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Speed Limitation",
            "questionType": "fill-blank",
            "question": "IAS limits at altitude Up to 1000 m (13.000 kg takeoff weight: Maximum / Minimum)",
            "answer": "230 / 60 Km/h",
            "acceptedAnswers": ["230 / 60", "230/60", "230 dan 60", "Max 230 Min 60", "230, 60"],
            "unit": "Km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-006",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Speed Limitation",
            "questionType": "fill-blank",
            "question": "IAS limits at altitude Up to 1000 m (11.100 kg takeoff weight: Maximum / Minimum)",
            "answer": "250 / 60 Km/h",
            "acceptedAnswers": ["250 / 60", "250/60", "250 dan 60", "Max 250 Min 60", "250, 60"],
            "unit": "Km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-007",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Speed Limitation",
            "questionType": "fill-blank",
            "question": "IAS limits at altitude 2000 m (13.000 kg: Max/Min vs 11.100 kg: Max/Min)",
            "answer": "195 / 60 dan 230 / 60 Km/h",
            "acceptedAnswers": ["195 / 60, 230 / 60", "195/60, 230/60", "195 60 230 60", "195/60 dan 230/60"],
            "unit": "Km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-008",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Speed Limitation",
            "questionType": "fill-blank",
            "question": "IAS limits at altitude 3000 m (13.000 kg: Max/Min vs 11.100 kg: Max/Min)",
            "answer": "160 / 60 dan 210 / 60 Km/h",
            "acceptedAnswers": ["160 / 60, 210 / 60", "160/60, 210/60", "160 60 210 60", "160/60 dan 210/60"],
            "unit": "Km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-009",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Speed Limitation",
            "questionType": "fill-blank",
            "question": "IAS limits at altitude 4000 m (13.000 kg: Max/Min vs 11.100 kg: Max/Min)",
            "answer": "120 / 60 dan 170 / 60 Km/h",
            "acceptedAnswers": ["120 / 60, 170 / 60", "120/60, 170/60", "120 60 170 60", "120/60 dan 170/60"],
            "unit": "Km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-010",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Speed Limitation",
            "questionType": "fill-blank",
            "question": "IAS limits at altitude 5000 m & 6000 m (11.100 kg takeoff weight: Max/Min)",
            "answer": "5000 m: 130 / 60, 6000 m: 100 / 60 Km/h",
            "acceptedAnswers": ["130 / 60, 100 / 60", "130/60, 100/60", "130 60 100 60", "130/60 dan 100/60"],
            "unit": "Km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-011",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Hovering Altitude",
            "questionType": "fill-blank",
            "question": "Hovering altitude for takeoff weight 11.100 kg and below",
            "answer": "Up to 10 m",
            "acceptedAnswers": ["Up to 10", "Up to 10 m", "10", "10 m", "sampai 10 m"],
            "unit": "m",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-012",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Hovering Altitude",
            "questionType": "fill-blank",
            "question": "Hovering altitude for takeoff weight Above 11.1000 kg",
            "answer": "Up to 5 m",
            "acceptedAnswers": ["Up to 5", "Up to 5 m", "5", "5 m", "sampai 5 m"],
            "unit": "m",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-013",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Maximum Allowed Wind Speed",
            "questionType": "fill-blank",
            "question": "Maximum allowed wind speed - Headwind (At M/R start & stop / At takeoff & landing)",
            "answer": "25 / 25 m/s",
            "acceptedAnswers": ["25 / 25", "25/25", "25 m/s", "25", "25 dan 25"],
            "unit": "m/s",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-014",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Maximum Allowed Wind Speed",
            "questionType": "fill-blank",
            "question": "Maximum allowed wind speed - Right side crosswind (At M/R start & stop / At takeoff & landing)",
            "answer": "10 / 10 m/s",
            "acceptedAnswers": ["10 / 10", "10/10", "10 m/s", "10", "10 dan 10"],
            "unit": "m/s",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-015",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Maximum Allowed Wind Speed",
            "questionType": "fill-blank",
            "question": "Maximum allowed wind speed - Left side crosswind (At M/R start & stop / At takeoff & landing)",
            "answer": "15 / 10 m/s",
            "acceptedAnswers": ["15 / 10", "15/10", "15 dan 10", "15/10 m/s"],
            "unit": "m/s",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-016",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Maximum Allowed Wind Speed",
            "questionType": "fill-blank",
            "question": "Maximum allowed wind speed - Tailwind (At M/R start & stop / At takeoff & landing)",
            "answer": "8 / 10 m/s",
            "acceptedAnswers": ["8 / 10", "8/10", "8 dan 10", "8/10 m/s"],
            "unit": "m/s",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-017",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Maximum Bank",
            "questionType": "fill-blank",
            "question": "Maximum Bank at 50 TO 3000 m (Gross weight 11100 kg or below / Above 11100 kg)",
            "answer": "30 / 20 deg",
            "acceptedAnswers": ["30 / 20", "30/20", "30 dan 20", "30 deg / 20 deg", "30° / 20°"],
            "unit": "deg",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-018",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Maximum Bank",
            "questionType": "fill-blank",
            "question": "Maximum Bank ABOVE 3000 m (Gross weight 11100 kg or below / Above 11100 kg)",
            "answer": "15 / 15 deg",
            "acceptedAnswers": ["15 / 15", "15/15", "15", "15 deg", "15°"],
            "unit": "deg",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-019",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Speed at Zoom and Dive",
            "questionType": "fill-blank",
            "question": "Max allowed speed for zoom from horizontal flight / recovery from dive (0 TO 500 m)",
            "answer": "220 / 300 km/h",
            "acceptedAnswers": ["220 / 300", "220/300", "220 dan 300"],
            "unit": "km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-020",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Speed at Zoom and Dive",
            "questionType": "fill-blank",
            "question": "Max allowed speed for zoom from horizontal flight / recovery from dive (500 TO 1000 m)",
            "answer": "200 / 300 km/h",
            "acceptedAnswers": ["200 / 300", "200/300", "200 dan 300"],
            "unit": "km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-021",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Speed at Zoom and Dive",
            "questionType": "fill-blank",
            "question": "Max allowed speed for zoom from horizontal flight / recovery from dive (1000 TO 2000 m)",
            "answer": "180 / 250 km/h",
            "acceptedAnswers": ["180 / 250", "180/250", "180 dan 250"],
            "unit": "km/h",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-022",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Engine Operating Parameters",
            "questionType": "fill-blank",
            "question": "Takeoff rating: Max gas generator turbine inlet gas temperature & Max gas generator turbine speed %",
            "answer": "990 °C / 101.15 %",
            "acceptedAnswers": ["990 / 101.15", "990 / 101.15%", "990, 101.15", "990 dan 101.15%"],
            "unit": "°C / %",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-023",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Engine Operating Parameters",
            "questionType": "fill-blank",
            "question": "30 min power OEI takeoff: Max gas generator inlet gas temp & Max speed %",
            "answer": "990 °C / 101.15 %",
            "acceptedAnswers": ["990 / 101.15", "990 / 101.15%", "990, 101.15", "990 dan 101.15%"],
            "unit": "°C / %",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-024",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Engine Operating Parameters",
            "questionType": "fill-blank",
            "question": "Continuous power OEI (normal): Max gas generator inlet gas temp & Max speed %",
            "answer": "955 °C / 99.0 %",
            "acceptedAnswers": ["955 / 99.0", "955 / 99%", "955, 99.0", "955 dan 99.0%"],
            "unit": "°C / %",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-025",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Engine Operating Parameters",
            "questionType": "fill-blank",
            "question": "Cruising 1 & Cruising 2: Max gas generator inlet gas temp",
            "answer": "910 °C / 870 °C",
            "acceptedAnswers": ["910 / 870", "910 dan 870", "910 °C / 870 °C", "910, 870"],
            "unit": "°C",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-LIM-026",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Engine Operating Parameters",
            "questionType": "fill-blank",
            "question": "Idle rating: Max gas generator inlet gas temperature",
            "answer": "780 °C",
            "acceptedAnswers": ["780", "780 °C", "780 C", "780°C"],
            "unit": "°C",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 2,
            "points": 1,
            "verified": True
        },

        # Main Gear Box
        {
            "id": "MI17-MGB-001",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Main Gear Box",
            "questionType": "fill-blank",
            "question": "Main Gear Box Oil Pressure: a. At idle, b. In sideslip flight (<= 30 s), c. At other power ratings",
            "answer": "0.5 kgf/cm2, min / 2.5 kgf/cm2, min / 3.5 ± 0.5 kgf/cm2",
            "acceptedAnswers": ["0.5 / 2.5 / 3.5 ± 0.5", "0.5, 2.5, 3.5", "0.5 / 2.5 / 3.5 +/- 0.5"],
            "unit": "kgf/cm2",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-MGB-002",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Main Gear Box",
            "questionType": "fill-blank",
            "question": "Main gearbox inlet oil temperature: Maximum & Recommended",
            "answer": "90°C, max / 50 to 80°C",
            "acceptedAnswers": ["90 max / 50 to 80", "90 / 50-80", "90 dan 50-80", "90°C, 50 to 80°C"],
            "unit": "°C",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-MGB-003",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Main Gear Box",
            "questionType": "fill-blank",
            "question": "Main gearbox inlet oil temp: Continuous operation min & starting without MGB heating min",
            "answer": "+30°C / -40°C",
            "acceptedAnswers": ["+30 / -40", "+30 dan -40", "30 / -40", "+30°C / -40°C"],
            "unit": "°C",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-MGB-004",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Main Gear Box",
            "questionType": "fill-blank",
            "question": "The maximum oil temperature in the tail and intermediate gear boxes is",
            "answer": "110°C",
            "acceptedAnswers": ["110", "110°C", "110 C", "110 °C"],
            "unit": "°C",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 1,
            "verified": True
        },

        # APU
        {
            "id": "MI17-APU-001",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "APU",
            "questionType": "fill-blank",
            "question": "Maximum allowed TGT of APU engine: At start / At idle / At air bleed and generators modes",
            "answer": "880 °C / 720 °C / 750 °C",
            "acceptedAnswers": ["880 / 720 / 750", "880, 720, 750", "880 / 720 / 750 °C"],
            "unit": "°C",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-APU-002",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "APU",
            "questionType": "fill-blank",
            "question": "Maximum continuous operation time on generator mode for APU",
            "answer": "30 min",
            "acceptedAnswers": ["30", "30 min", "30 menit", "30 minutes"],
            "unit": "min",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 1,
            "verified": True
        },

        # Slopes
        {
            "id": "MI17-SLOPE-001",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Take-off and Landing Slopes",
            "questionType": "fill-blank",
            "question": "Max slopes for vertical takeoff and landing WITHOUT shutdown: Uphill / Downhill / LH side / RH side",
            "answer": "7° / 5° / 7° / 3°",
            "acceptedAnswers": ["7 / 5 / 7 / 3", "7, 5, 7, 3", "7° / 5° / 7° / 3°", "7 5 7 3"],
            "unit": "degrees",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-SLOPE-002",
            "aircraft": "MI-17V5",
            "section": "LIMITATION",
            "category": "Take-off and Landing Slopes",
            "questionType": "fill-blank",
            "question": "Max slopes for vertical takeoff and landing maximal WITH shutdown engine after touchdown: Uphill, Downhill, LH / RH",
            "answer": "3° / 3°",
            "acceptedAnswers": ["3 / 3", "3° / 3°", "3", "3°"],
            "unit": "degrees",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 3,
            "points": 1,
            "verified": True
        },

        # Maneuver Khusus
        {
            "id": "MI17-MAN-001",
            "aircraft": "MI-17V5",
            "section": "Maneuver Khusus",
            "category": "External Load",
            "questionType": "fill-blank",
            "question": "External Load: MTOW & Berat Max Load",
            "answer": "13.000 Kg / 4.000 Kg",
            "acceptedAnswers": ["13000 / 4000", "13.000 / 4.000", "13.000 Kg / 4.000 Kg", "13000 kg dan 4000 kg"],
            "unit": "Kg",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 4,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-MAN-002",
            "aircraft": "MI-17V5",
            "section": "Maneuver Khusus",
            "category": "External Load",
            "questionType": "fill-blank",
            "question": "External Load: Max Speed & Max Turn/bank",
            "answer": "200 Km/jam / 15°",
            "acceptedAnswers": ["200 / 15", "200 Km/jam / 15°", "200 km/h / 15 deg", "200 dan 15"],
            "unit": "Km/jam / deg",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 4,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-MAN-003",
            "aircraft": "MI-17V5",
            "section": "Maneuver Khusus",
            "category": "Fastrooping/Rappelling",
            "questionType": "fill-blank",
            "question": "Fastrooping/Rappeling: Max berat 1 orang & Headwind max Wind Speed",
            "answer": "100 Kg / 10 m/s",
            "acceptedAnswers": ["100 / 10", "100 Kg / 10 m/s", "100 kg dan 10 m/s"],
            "unit": "Kg / m/s",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 4,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-MAN-004",
            "aircraft": "MI-17V5",
            "section": "Maneuver Khusus",
            "category": "Fastrooping/Rappelling",
            "questionType": "fill-blank",
            "question": "Fastrooping/Rappeling: Min Altitude & Pelaksanaan di hutan jarak dari ujung pohon tidak kurang dari",
            "answer": "45 m / 10 m",
            "acceptedAnswers": ["45 / 10", "45 m / 10 m", "45 dan 10"],
            "unit": "m",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 4,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-MAN-005",
            "aircraft": "MI-17V5",
            "section": "Maneuver Khusus",
            "category": "Hoist",
            "questionType": "fill-blank",
            "question": "Hoist: Max weight hoisted (at hovering 50 - 55 m) & Max hover height (panjang tali 60 m)",
            "answer": "300 kg / 55 m",
            "acceptedAnswers": ["300 kg / 55 m", "300 / 55", "300 kg dan 55 m"],
            "unit": "kg / m",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 4,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-MAN-006",
            "aircraft": "MI-17V5",
            "section": "Maneuver Khusus",
            "category": "Hoist",
            "questionType": "fill-blank",
            "question": "Hoist: Max hover di atas air untuk hoist",
            "answer": "20 m",
            "acceptedAnswers": ["20", "20 m", "20 meter"],
            "unit": "m",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 4,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-MAN-007",
            "aircraft": "MI-17V5",
            "section": "Maneuver Khusus",
            "category": "Fuel Reserve",
            "questionType": "fill-blank",
            "question": "Fuel Reserve 320 L (... minutes ... meter ... km/jam ... km)",
            "answer": "21 minutes ... 500 meter ... 220 km/jam ... 70 km",
            "acceptedAnswers": ["21 minutes, 500 meter, 220 km/jam, 70 km", "21 min, 500 m, 220 km/h, 70 km", "21 500 220 70", "21, 500, 220, 70"],
            "unit": "min / m / km/jam / km",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 4,
            "points": 1,
            "verified": True
        },
        {
            "id": "MI17-MAN-008",
            "aircraft": "MI-17V5",
            "section": "Maneuver Khusus",
            "category": "Fuel Reserve",
            "questionType": "fill-blank",
            "question": "Fuel Reserve 270 L (... minutes ... meter ... km/jam ... km)",
            "answer": "17 minutes ... 500 meter ... 220 km/jam ... 55 km",
            "acceptedAnswers": ["17 minutes, 500 meter, 220 km/jam, 55 km", "17 min, 500 m, 220 km/h, 55 km", "17 500 220 55", "17, 500, 220, 55"],
            "unit": "min / m / km/jam / km",
            "sourceDocument": "BOLD FACE MI-17V5 ISI.docx",
            "sourcePage": 4,
            "points": 1,
            "verified": True
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

def build_bell412ep():
    # Load 106 limitation questions from Bell 412 EP
    bell_limits = [
        ("FLIGHT CREW", "Minimum flight crew", "1 pilot who shall operate helicopter on right crew seat", ["1 pilot who shall operate helicopter on right crew seat", "1 pilot", "1 pilot on right crew seat", "1"]),
        ("GROSS WEIGHT", "Maximum gross weight for take off and landing", "11.900 Lbs", ["11.900", "11900", "11,900", "11.900 Lbs", "11900 lbs"]),
        ("GROSS WEIGHT", "Minimum gross weight for flight", "6400 Lbs", ["6400", "6.400", "6400 Lbs", "6400 lbs"]),
        ("GROSS WEIGHT", "Minimum combined crew weight at fuselage station 47.0", "170 Lbs", ["170", "170 Lbs", "170 lbs"]),
        ("CARGO", "Max allowable deck loading", "100 lbs/ft2", ["100", "100 lbs/ft2", "100 lbs/sq ft", "100 lb/ft2"]),
        ("CARGO", "Cargo deck tiedown fitting capacity: Vertical", "1250 lbs", ["1250", "1.250", "1250 lbs", "1250lbs"]),
        ("CARGO", "Cargo deck tiedown fitting capacity: Horizontal", "500 lbs", ["500", "500 lbs", "500lbs"]),
        ("CARGO", "Baggage compartment load limit (not to exceed 100 lbs/ft2)", "400 lbs", ["400", "400 lbs", "400lbs"]),
        ("CENTER OF GRAVITY", "Longitudinal center of gravity limits vary from station", "130 to 144", ["130 to 144", "130-144", "130 sampai 144"]),
        ("CENTER OF GRAVITY", "Lateral center of gravity (left and right)", "4.5 inch", ["4.5", "4.5 inch", "4,5", "4,5 inch"]),
        ("AIR SPEED", "Minimum IFR airspeed", "60 KIAS", ["60", "60 KIAS", "60 kias", "60 kts"]),
        ("AIR SPEED", "Basic Vne from sea level to 3000 ft (DA) at all gross weight", "140 KIAS", ["140", "140 KIAS", "140 kias"]),
        ("AIR SPEED", "Vne with only one autopilot engage", "115 KIAS", ["115", "115 KIAS", "115 kias"]),
        ("AIR SPEED", "Maximum airspeed when operating above 81% mast torque", "105 KIAS", ["105", "105 KIAS", "105 kias"]),
        ("AIR SPEED", "Vne for steady state autorotation: At or below 10.000 ft pressure altitude", "105 KIAS", ["105", "105 KIAS", "105 kias"]),
        ("AIR SPEED", "Vne for steady state autorotation: Above 10.000 ft pressure altitude", "80 KIAS", ["80", "80 KIAS", "80 kias"]),
        ("AIR SPEED", "Vne with cargo doors opened asymmetrically", "80 KIAS", ["80", "80 KIAS", "80 kias"]),
        ("AIR SPEED", "Vne with cargo doors in transit or in an unlocked position", "60 KIAS", ["60", "60 KIAS", "60 kias"]),
        ("AIR SPEED", "Vne with symmetrically doors open or removed with Bell installed energy attenuating passenger seats", "60 KIAS", ["60", "60 KIAS", "60 kias"]),
        ("AIR SPEED", "Vne with symmetrically doors open or removed with Bell Installed Blanket Interior/deluxe interior", "100 KIAS", ["100", "100 KIAS", "100 kias"]),
        ("AIR SPEED", "Maximum allowable air speed for sideward or rearward flight at or below 3.000 feet HD", "35 Knots", ["35", "35 Knots", "35 kts"]),
        ("AIR SPEED", "Maximum allowable tailwind and crosswind or bellow 3.000 feet HD", "35 Knots", ["35", "35 Knots", "35 kts"]),
        ("AIR SPEED", "Maximum operating pressure altitude", "20.000 Ft", ["20.000", "20000", "20.000 Ft", "20000 ft"]),
        ("AIR SPEED", "Maximum density altitude for take off, landing, and in-ground effect Maneuvers", "14.000 Ft", ["14.000", "14000", "14.000 Ft", "14000 ft"]),
        ("CLIMB/DESCENT", "Maximum IFR rate of climb or descent", "1000 ft/min", ["1000", "1.000", "1000 ft/min", "1000 fpm"]),
        ("CLIMB/DESCENT", "Maximum IFR approach slope", "5 degrees", ["5", "5 degrees", "5 deg", "5°"]),
        ("SLOPE LANDING", "Slope Landing: Forward/nose down", "4 degrees", ["4", "4 degrees", "4 deg", "4°"]),
        ("SLOPE LANDING", "Slope Landing: Rearward/nose up", "4 degrees", ["4", "4 degrees", "4 deg", "4°"]),
        ("SLOPE LANDING", "Slope Landing: Leftside slope", "10 degrees", ["10", "10 degrees", "10 deg", "10°"]),
        ("SLOPE LANDING", "Slope Landing: Rightside slope", "10 degrees", ["10", "10 degrees", "10 deg", "10°"]),
        ("MANEUVERING", "Max angle of bank", "50 degrees", ["50", "50 degrees", "50 deg", "50 degress", "50°"]),
        ("MANEUVERING", "Max nose up", "30 degrees", ["30", "30 degrees", "30 deg", "30 degress", "30°"]),
        ("MANEUVERING", "Max nose down", "15 degrees", ["15", "15 degrees", "15 deg", "15 degress", "15°"]),
        ("AMBIENT AIR TEMPERATURE", "Maximum sea level ambient temperature for operation", "51.7 °C/ 125 °F", ["51.7 °C/ 125 °F", "51.7", "51.7 C", "125 F", "51.7 °C / 125 °F", "51,7"]),
        ("AMBIENT AIR TEMPERATURE", "Minimum ambient temperature for operation at all altitudes", "-40 °C/ -40 °F", ["-40 °C/ -40 °F", "-40", "-40 C", "-40 F", "-40 °C / -40 °F"]),
        ("BATTERY", "Maximum battery temperature", "62.8 °C/ 145 °F", ["62.8 °C/ 145 °F", "62.8", "62.8 C", "145 F", "62,8"]),
        ("BATTERY", "Minimum ambient temperature for battery start when battery and helicopter have been cold soaked", "-25 °C/ -13 °F", ["-25 °C/ -13 °F", "-25", "-25 C", "-13 F"]),
        ("GENERATOR", "Generator: Continuous Operation", "0 to 75 amps", ["0 to 75", "0-75", "0 to 75 amps", "0-75 amps"]),
        ("GENERATOR", "Generator: Caution", "75 to 150 amps", ["75 to 150", "75-150", "75 to 150 amps", "75-150 amps"]),
        ("GENERATOR", "Generator: Maximum Continuous", "150 amps (each)", ["150", "150 amps", "150 amps (each)", "150 each"]),
        ("ENGINE STARTER", "Engine Starter sequence 1: second ON", "30 second ON", ["30", "30 second", "30 sec", "30 detik"]),
        ("ENGINE STARTER", "Engine Starter sequence 2: second OFF", "60 second OFF", ["60", "60 second", "60 sec", "60 detik"]),
        ("ENGINE STARTER", "Engine Starter sequence 3: second ON", "30 second ON", ["30", "30 second", "30 sec", "30 detik"]),
        ("ENGINE STARTER", "Engine Starter sequence 4: minutes OFF", "5 minutes OFF", ["5", "5 minutes", "5 min", "5 menit"]),
        ("ENGINE STARTER", "Engine Starter sequence 5: second ON", "30 second ON", ["30", "30 second", "30 sec", "30 detik"]),
        ("ENGINE STARTER", "Engine Starter sequence 6: minutes OFF", "15 minutes OFF", ["15", "15 minutes", "15 min", "15 menit"]),
        ("GROUND POWER STARTS", "28 VDC ground power units for starting shall be limited to", "1000 amps max", ["1000", "1000 amps", "1000 amps max", "1.000 amps"]),
        ("GAS PRODUCER RPM (N1)", "GAS PRODUCER RPM (N1): Twin Engine Operation: Continuous operation", "61 to 103.1 %", ["61 to 103.1", "61-103.1", "61 to 103.1 %", "61-103.1%"]),
        ("GAS PRODUCER RPM (N1)", "GAS PRODUCER RPM (N1): Twin Engine Operation: Maximum continuous", "103.1 %", ["103.1", "103.1 %", "103,1", "103.1%"]),
        ("GAS PRODUCER RPM (N1)", "GAS PRODUCER RPM (N1): Twin Engine Operation: Maximum for take off", "103.1 %", ["103.1", "103.1 %", "103,1", "103.1%"]),
        ("GAS PRODUCER RPM (N1)", "GAS PRODUCER RPM (N1): One Engine Inoperative (OEI): Continuous OEI", "103.1 to 103.7 %", ["103.1 to 103.7", "103.1-103.7", "103.1 to 103.7 %"]),
        ("GAS PRODUCER RPM (N1)", "GAS PRODUCER RPM (N1): One Engine Inoperative (OEI): 2 1/2 Minutes OEI", "103.7 to 109.2 %", ["103.7 to 109.2", "103.7-109.2", "103.7 to 109.2 %"]),
        ("GAS PRODUCER RPM (N1)", "GAS PRODUCER RPM (N1): One Engine Inoperative (OEI): Maximum OEI", "109.2 %", ["109.2", "109.2 %", "109,2", "109.2%"]),
        ("POWER TURBINE RPM (N2)", "POWER TURBINE RPM (N2): Minimum in cruise at or below 6000 ft HD", "97 %", ["97", "97 %", "97%"]),
        ("POWER TURBINE RPM (N2)", "POWER TURBINE RPM (N2): Min for hover, take off and climb", "100 %", ["100", "100 %", "100%"]),
        ("POWER TURBINE RPM (N2)", "POWER TURBINE RPM (N2): Min in cruise above 6000 ft HD", "100 %", ["100", "100 %", "100%"]),
        ("POWER TURBINE RPM (N2)", "POWER TURBINE RPM (N2): Operation with ENG torque at or below 30%", "100 to 104.5 %", ["100 to 104.5", "100-104.5", "100 to 104.5 %"]),
        ("POWER TURBINE RPM (N2)", "POWER TURBINE RPM (N2): Max with ENG torque at or below 30%", "104.5 %", ["104.5", "104.5 %", "104,5", "104.5%"]),
        ("INTER TURBINE TEMPERATURE (ITT)", "INTER TURBINE TEMPERATURE (ITT): Twin Engine Gauge P/N 212-075-067-115: Continuous operation", "300 to 810 °C", ["300 to 810", "300-810", "300 to 810 °C"]),
        ("INTER TURBINE TEMPERATURE (ITT)", "INTER TURBINE TEMPERATURE (ITT): Twin Engine Gauge P/N 212-075-067-115: Maximum continuous", "810 °C", ["810", "810 °C", "810 C", "810°C"]),
        ("INTER TURBINE TEMPERATURE (ITT)", "INTER TURBINE TEMPERATURE (ITT): Twin Engine Gauge P/N 212-075-067-115: Maximum transient (5 sec max above 810°C)", "925 °C", ["925", "925 °C", "925 C", "925°C"]),
        ("INTER TURBINE TEMPERATURE (ITT)", "INTER TURBINE TEMPERATURE (ITT): Twin Engine Gauge P/N 212-075-067-115: Maximum for starting (2 sec max above 960°C)", "1090 °C", ["1090", "1090 °C", "1090 C", "1090°C", "1.090"]),
        ("INTER TURBINE TEMPERATURE (ITT)", "INTER TURBINE TEMPERATURE (ITT): Twin Engine Gauge P/N 212-075-067-119: Continuous operation & Max continuous", "300 to 810 °C / 810 °C", ["300 to 810 / 810", "300-810 / 810", "300-810, 810"]),
        ("INTER TURBINE TEMPERATURE (ITT)", "INTER TURBINE TEMPERATURE (ITT): Twin Engine Gauge P/N 212-075-067-119: Maximum transient (5 sec max above 810°C)", "940 °C", ["940", "940 °C", "940 C", "940°C"]),
        ("INTER TURBINE TEMPERATURE (ITT)", "INTER TURBINE TEMPERATURE (ITT): Twin Engine Gauge P/N 212-075-067-119: Maximum for starting (2 sec max above 960°C)", "1090 °C", ["1090", "1090 °C", "1090 C", "1090°C"]),
        ("INTER TURBINE TEMPERATURE (ITT)", "INTER TURBINE TEMPERATURE (ITT): OEI Gauge P/N 212-075-067-115: Maximum continuous OEI", "820 °C", ["820", "820 °C", "820 C", "820°C"]),
        ("INTER TURBINE TEMPERATURE (ITT)", "INTER TURBINE TEMPERATURE (ITT): OEI Gauge P/N 212-075-067-115: 2 1/2 Min OEI & Maximum OEI", "820 to 925 °C / 925 °C", ["820 to 925 / 925", "820-925 / 925", "820 to 925, 925"]),
        ("INTER TURBINE TEMPERATURE (ITT)", "INTER TURBINE TEMPERATURE (ITT): OEI Gauge P/N 212-075-067-119: Maximum continuous OEI", "820 °C", ["820", "820 °C", "820 C", "820°C"]),
        ("INTER TURBINE TEMPERATURE (ITT)", "INTER TURBINE TEMPERATURE (ITT): OEI Gauge P/N 212-075-067-119: 2 1/2 Min OEI & Maximum OEI", "820 to 940 °C / 940 °C", ["820 to 940 / 940", "820-940 / 940", "820 to 940, 940"]),
        ("ENGINE TORQUE – OEI", "ENGINE TORQUE – OEI: Continuous OEI torque", "5 to 73.2 %", ["5 to 73.2", "5-73.2", "5 to 73.2 %", "5-73.2%"]),
        ("ENGINE TORQUE – OEI", "ENGINE TORQUE – OEI: Maximum continuous OEI torque", "73.2 %", ["73.2", "73.2 %", "73,2", "73.2%"]),
        ("ENGINE TORQUE – OEI", "ENGINE TORQUE – OEI: 2 1/2 Min OEI torque", "73.2 to 81 %", ["73.2 to 81", "73.2-81", "73.2 to 81 %"]),
        ("ENGINE TORQUE – OEI", "ENGINE TORQUE – OEI: Maximum OEI torque", "81 %", ["81", "81 %", "81%"]),
        ("FUEL PRESSURE", "Fuel Pressure: Minimum", "4 PSI", ["4", "4 PSI", "4 psi"]),
        ("FUEL PRESSURE", "Fuel Pressure: Continuous operation", "4 to 35 PSI", ["4 to 35", "4-35", "4 to 35 PSI"]),
        ("FUEL PRESSURE", "Fuel Pressure: Maximum", "35 PSI", ["35", "35 PSI", "35 psi"]),
        ("ENGINE OIL PRESSURE", "Engine Oil Press Gauge -113: Minimum for flight idle", "40 PSI", ["40", "40 PSI", "40 psi"]),
        ("ENGINE OIL PRESSURE", "Engine Oil Press Gauge -113: Operation below 79% N1 RPM", "40 to 90 PSI", ["40 to 90", "40-90", "40 to 90 PSI"]),
        ("ENGINE OIL PRESSURE", "Engine Oil Press Gauge -113: Continuous operation", "90 to 115 PSI", ["90 to 115", "90-115", "90 to 115 PSI"]),
        ("ENGINE OIL PRESSURE", "Engine Oil Press Gauge -113: Maximum", "115 PSI", ["115", "115 PSI", "115 psi"]),
        ("ENGINE OIL PRESSURE", "Engine Oil Press Gauge -109: Minimum for flight idle", "40 PSI", ["40", "40 PSI", "40 psi"]),
        ("ENGINE OIL PRESSURE", "Engine Oil Press Gauge -109: Operation below 79% N1 RPM", "40 to 80 PSI", ["40 to 80", "40-80", "40 to 80 PSI"]),
        ("ENGINE OIL PRESSURE", "Engine Oil Press Gauge -109: Continuous operation", "80 to 115 PSI", ["80 to 115", "80-115", "80 to 115 PSI"]),
        ("ENGINE OIL PRESSURE", "Engine Oil Press Gauge -109: Maximum", "115 PSI", ["115", "115 PSI", "115 psi"]),
        ("ENGINE OIL TEMPERATURE", "Engine Oil Temperature: Minimum", "0 °C", ["0", "0 °C", "0 C", "0°C"]),
        ("ENGINE OIL TEMPERATURE", "Engine Oil Temperature: Continuous operation", "0 to 115 °C", ["0 to 115", "0-115", "0 to 115 °C"]),
        ("ENGINE OIL TEMPERATURE", "Engine Oil Temperature: Maximum for MIL-PRF-7808 oil", "115 °C", ["115", "115 °C", "115 C"]),
        ("ENGINE OIL TEMPERATURE", "Engine Oil Temperature: Maximum for MIL-PRF-23699 oil", "120 °C", ["120", "120 °C", "120 C"]),
        ("C-BOX OIL PRESSURE", "C-BOX Oil Pressure: Minimum for flight idle", "40 PSI", ["40", "40 PSI", "40 psi"]),
        ("C-BOX OIL PRESSURE", "C-BOX Oil Pressure: Operation below 94% N2 RPM", "40 to 60 PSI", ["40 to 60", "40-60", "40 to 60 PSI"]),
        ("C-BOX OIL PRESSURE", "C-BOX Oil Pressure: Continuous operation", "60 to 80 PSI", ["60 to 80", "60-80", "60 to 80 PSI"]),
        ("C-BOX OIL PRESSURE", "C-BOX Oil Pressure: Maximum", "80 PSI", ["80", "80 PSI", "80 psi"]),
        ("C-BOX OIL TEMPERATURE", "C-BOX Oil Temperature: Minimum", "0 °C", ["0", "0 °C", "0 C"]),
        ("C-BOX OIL TEMPERATURE", "C-BOX Oil Temperature: Continuous operation", "0 to 115 °C", ["0 to 115", "0-115", "0 to 115 °C"]),
        ("C-BOX OIL TEMPERATURE", "C-BOX Oil Temperature: Maximum for MIL-PRF-7808 oil", "115 °C", ["115", "115 °C", "115 C"]),
        ("C-BOX OIL TEMPERATURE", "C-BOX Oil Temperature: Maximum for MIL-PRF-23699 oil", "120 °C", ["120", "120 °C", "120 C"]),
        ("XMSN OIL PRESSURE", "XMSN Oil Pressure: Minimum for flight idle", "30 PSI", ["30", "30 PSI", "30 psi"]),
        ("XMSN OIL PRESSURE", "XMSN Oil Pressure: Idle range", "30 to 40 PSI", ["30 to 40", "30-40", "30 to 40 PSI"]),
        ("XMSN OIL PRESSURE", "XMSN Oil Pressure: Continuous operation", "40 to 70 PSI", ["40 to 70", "40-70", "40 to 70 PSI"]),
        ("XMSN OIL PRESSURE", "XMSN Oil Pressure: Maximum", "70 PSI", ["70", "70 PSI", "70 psi"]),
        ("XMSN OIL TEMPERATURE", "XMSN Oil Temperature: Continuous operation", "15 to 110 °C", ["15 to 110", "15-110", "15 to 110 °C"]),
        ("XMSN OIL TEMPERATURE", "XMSN Oil Temperature: Maximum", "110 °C", ["110", "110 °C", "110 C"]),
        ("MAST TORQUE", "Mast Torque Twin Engine: Maximum continuous", "81 %", ["81", "81 %", "81%"]),
        ("MAST TORQUE", "Mast Torque Twin Engine: Take off range (5 minutes max)", "81 to 100 %", ["81 to 100", "81-100", "81 to 100 %"]),
        ("MAST TORQUE", "Mast Torque Twin Engine: Maximum", "100 %", ["100", "100 %", "100%"]),
        ("ROTOR RPM – POWER ON", "Rotor RPM Power On: Minimum", "97 %", ["97", "97 %", "97%"]),
        ("ROTOR RPM – POWER ON", "Rotor RPM Power On: Continuous operation at or below 6000 ft HD", "97 to 100 %", ["97 to 100", "97-100", "97 to 100 %"]),
        ("ROTOR RPM – POWER ON", "Rotor RPM Power On: Continuous operation above 6000 ft HD", "100 %", ["100", "100 %", "100%"]),
        ("ROTOR RPM – POWER ON", "Rotor RPM Power On: Maximum continuous", "100 %", ["100", "100 %", "100%"]),
        ("ROTOR RPM – POWER ON", "Rotor RPM Power On: Operation with ENG torque at or below 30%", "100 to 104.5 %", ["100 to 104.5", "100-104.5", "100 to 104.5 %"]),
        ("ROTOR RPM – POWER ON", "Rotor RPM Power On: Max with ENG torque at or below 30%", "104.5 %", ["104.5", "104.5 %", "104,5", "104.5%"]),
        ("ROTOR RPM – POWER OFF", "ROTOR RPM – POWER OFF: Min for autorotation with gross weight below 8000 lbs (3629 kg)", "80 %", ["80", "80 %", "80%"]),
        ("ROTOR RPM – POWER OFF", "ROTOR RPM – POWER OFF: Power off operation with gross weight below 8000 lbs (3629 kg)", "80 to 104.5 %", ["80 to 104.5", "80-104.5", "80 to 104.5 %"]),
        ("ROTOR RPM – POWER OFF", "ROTOR RPM – POWER OFF: Min for autorotation with gross weight at or above 8000 lbs (3629 kg)", "91 %", ["91", "91 %", "91%"]),
        ("ROTOR RPM – POWER OFF", "ROTOR RPM – POWER OFF: Power Off Maximum", "104.5 %", ["104.5", "104.5 %", "104,5", "104.5%"]),
        ("ROTOR RPM – GROUND OPERATION", "ROTOR RPM – GROUND OPERATION: Ground Operation: Minimum", "77 %", ["77", "77 %", "77%"]),
        ("ROTOR RPM – GROUND OPERATION", "ROTOR RPM – GROUND OPERATION: Ground Operation: Minimum with stick centering ind system inoperative", "97 %", ["97", "97 %", "97%"]),
        ("ROTOR RPM – GROUND OPERATION", "ROTOR RPM – GROUND OPERATION: Ground Operation: Transient (avoid steady state autorotation)", "26 to 77 %", ["26 to 77", "26-77", "26 to 77 %"]),
        ("HYDRAULIC PRESSURE", "Hydraulic Pressure: Minimum", "600 PSI", ["600", "600 PSI", "600 psi"]),
        ("HYDRAULIC PRESSURE", "Hydraulic Pressure: Caution", "600 to 900 PSI", ["600 to 900", "600-900", "600 to 900 PSI"]),
        ("HYDRAULIC PRESSURE", "Hydraulic Pressure: Continuous operation", "900 to 1100 PSI", ["900 to 1100", "900-1100", "900 to 1100 PSI"]),
        ("HYDRAULIC PRESSURE", "Hydraulic Pressure: Maximum", "1100 PSI", ["1100", "1100 PSI", "1100 psi", "1.100"]),
        ("HYDRAULIC TEMPERATURE", "Hydraulic Temperature: Maximum", "88 °C", ["88", "88 °C", "88 C", "88°C"]),
        ("AHRS ALIGNMENT", "AHRS Alignment: Pitch", "less than ± 10°", ["less than ± 10°", "less than 10", "< 10°", "± 10°", "10°", "<= 10°"]),
        ("AHRS ALIGNMENT", "AHRS Alignment: Roll", "less than ± 5°", ["less than ± 5°", "less than 5", "< 5°", "± 5°", "5°", "<= 5°"]),
        ("AHRS ALIGNMENT", "AHRS Alignment: Yaw", "less than 1°/sec", ["less than 1°/sec", "less than 1", "< 1°/sec", "1°/sec", "1"]),
        ("AHRS ALIGNMENT", "AHRS Alignment: Lateral and longitudinal acceleration", "less than 0.05g", ["less than 0.05g", "less than 0.05", "0.05g", "0.05", "< 0.05g", "0,05g"])
    ]

    questions = []
    for idx, (cat, q_text, ans, accepted) in enumerate(bell_limits, 1):
        questions.append({
            "id": f"B412-LIM-{idx:03d}",
            "aircraft": "BELL 412 EP",
            "section": "LIMITATION",
            "category": cat,
            "questionType": "fill-blank",
            "question": f"{idx}. {q_text}",
            "answer": ans,
            "acceptedAnswers": accepted,
            "unit": ans.split()[-1] if len(ans.split()) > 1 and ans.split()[-1] in ["Lbs", "KIAS", "Knots", "Ft", "degrees", "amps", "PSI", "°C", "%", "ft/min", "inch"] else "",
            "sourceDocument": "bold face bell 412 EP.pdf",
            "sourcePage": 16 + (idx - 1) // 27,
            "points": 1,
            "verified": True
        })

    # Indicator limitation dial & markings questions
    indicator_data = [
        (
            "Airspeed Dial Markings",
            "Airspeed indicator: Yellow arc (0-30), Green arc (30-140), Blue/White line (105), Red radial (140)",
            "0-30: Indicator Unreliable | 30-140: Cont. Operation | 105: Max for autorotation at/below 10.000 ft Hp | 140: VNE",
            ["0-30 Unreliable, 30-140 Cont. Operation, 105 Autorotation, 140 VNE"],
            [
                {"id": "sub_1", "label": "Yellow arc (0-30)", "answer": "Indicator Unreliable", "acceptedAnswers": ["Indicator Unreliable", "Unreliable"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_2", "label": "Green arc (30-140)", "answer": "Continuous Operation", "acceptedAnswers": ["Continuous Operation", "Cont. Operation", "Cont Operation", "Cont"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_3", "label": "Blue/White line (105)", "answer": "Max for autorotation at/below 10.000 ft Hp", "acceptedAnswers": ["Max for autorotation at/below 10.000 ft Hp", "Max for autorotation", "Autorotation", "Max autorotation"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_4", "label": "Red radial (140)", "answer": "VNE", "acceptedAnswers": ["VNE", "Vne", "Velocity Never Exceed"], "placeholder": "Batas / arti penunjukan..."}
            ]
        ),
        (
            "Mast Torque Dial Markings",
            "Mast Torque indicator: Green arc (10-81), Yellow arc (81-100), Red radial (100)",
            "10-81: Cont. Operation | 81-100: 5 Min Take Off Range | 100: Maximum",
            ["10-81 Cont, 81-100 5 Min Take Off, 100 Maximum"],
            [
                {"id": "sub_1", "label": "Green arc (10-81)", "answer": "Continuous Operation", "acceptedAnswers": ["Continuous Operation", "Cont. Operation", "Cont Operation", "Cont"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_2", "label": "Yellow arc (81-100)", "answer": "5 Min Take Off Range", "acceptedAnswers": ["5 Min Take Off Range", "5 Min Take Off", "5 Min Takeoff", "Take Off Range"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_3", "label": "Red radial (100)", "answer": "Maximum", "acceptedAnswers": ["Maximum", "Max"], "placeholder": "Batas / arti penunjukan..."}
            ]
        ),
        (
            "Engine Torque Dial Markings",
            "Engine Torque OEI: Green arc (5-73.2), Yellow arc (73.2-81), Red radial (81)",
            "5-73.2: Cont. OEI Operation | 73.2-81: 2 1/2 OEI | 81: Maximum OEI",
            ["5-73.2 Cont OEI, 73.2-81 2 1/2 OEI, 81 Maximum OEI"],
            [
                {"id": "sub_1", "label": "Green arc (5-73.2)", "answer": "Continuous OEI Operation", "acceptedAnswers": ["Continuous OEI Operation", "Cont. OEI Operation", "Cont OEI Operation", "Cont OEI", "Cont"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_2", "label": "Yellow arc (73.2-81)", "answer": "2 1/2 OEI", "acceptedAnswers": ["2 1/2 OEI", "2.5 OEI", "2 1/2 Min OEI", "2 1/2"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_3", "label": "Red radial (81)", "answer": "Maximum OEI", "acceptedAnswers": ["Maximum OEI", "Max OEI", "Maximum", "Max"], "placeholder": "Batas / arti penunjukan..."}
            ]
        ),
        (
            "Rotor RPM (Nr) Dial Markings",
            "Rotor RPM (Nr): Yellow (26-77), Red line (80), Yellow (80-91), Green (91-104.5), Red line (104.5)",
            "26-77: Transient Ground Operation | 80: Min for Autorotation below 8000 lbs | 80-91: Power Off below 8000 lbs | 91-104.5: Cont. Power Off | 104.5: Maximum",
            ["26-77 Transient, 80 Min Autorotation, 80-91 Power Off, 91-104.5 Cont Power Off, 104.5 Maximum"],
            [
                {"id": "sub_1", "label": "Yellow (26-77)", "answer": "Transient Ground Operation", "acceptedAnswers": ["Transient Ground Operation", "Transient Ground", "Transient"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_2", "label": "Red line (80)", "answer": "Min for Autorotation below 8000 lbs", "acceptedAnswers": ["Min for Autorotation below 8000 lbs", "Min for Autorotation", "Min Autorotation"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_3", "label": "Yellow (80-91)", "answer": "Power Off below 8000 lbs", "acceptedAnswers": ["Power Off below 8000 lbs", "Power Off"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_4", "label": "Green (91-104.5)", "answer": "Continuous Power Off", "acceptedAnswers": ["Continuous Power Off", "Cont. Power Off", "Cont Power Off", "Cont"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_5", "label": "Red line (104.5)", "answer": "Maximum", "acceptedAnswers": ["Maximum", "Max"], "placeholder": "Batas / arti penunjukan..."}
            ]
        ),
        (
            "Gas Producer RPM (Ni)",
            "Gas Producer RPM (Ni): White lines (12 & 61), Green arc (61-103.1), Red line (103.1), Yellow arcs (103.1-103.7 & 103.7-109.2), Red line (109.2)",
            "12: Min opening throttle during start | 61: Idle RPM | 61-103.1: Continuous Operation | 103.1: Max Continuous | 103.1-103.7: Cont OEI | 103.7-109.2: 2 1/2 Min OEI | 109.2: Max 2 1/2 OEI",
            ["12 Start, 61 Idle, 61-103.1 Cont, 103.1 Max Cont, 103.1-103.7 Cont OEI, 103.7-109.2 2 1/2 Min OEI, 109.2 Max OEI"],
            [
                {"id": "sub_1", "label": "White lines (12 & 61)", "answer": "12: Min opening throttle during start | 61: Idle RPM", "acceptedAnswers": ["12: Min opening throttle during start | 61: Idle RPM", "12 Start, 61 Idle", "12: Start, 61: Idle"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_2", "label": "Green arc (61-103.1)", "answer": "Continuous Operation", "acceptedAnswers": ["Continuous Operation", "Cont. Operation", "Cont Operation", "Cont"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_3", "label": "Red line (103.1)", "answer": "Max Continuous", "acceptedAnswers": ["Max Continuous", "Maximum Continuous", "Max Cont"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_4", "label": "Yellow arcs (103.1-103.7 & 103.7-109.2)", "answer": "103.1-103.7: Cont OEI | 103.7-109.2: 2 1/2 Min OEI", "acceptedAnswers": ["103.1-103.7: Cont OEI | 103.7-109.2: 2 1/2 Min OEI", "103.1-103.7 Cont OEI, 103.7-109.2 2 1/2 Min OEI", "Cont OEI / 2 1/2 Min OEI"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_5", "label": "Red line (109.2)", "answer": "Max 2 1/2 OEI", "acceptedAnswers": ["Max 2 1/2 OEI", "Max OEI", "Maximum OEI"], "placeholder": "Batas / arti penunjukan..."}
            ]
        ),
        (
            "ITT Dial Markings",
            "Inter Turbine Temperature (ITT): Green arc (300-810), Red line (810), Yellow arc (810-940), Red line (820, 940), Red triangle (1090)",
            "300-810: Continuous Operation | 810: Max Continuous | 810-940: OEI Operation | 820: Max Cont. OEI | 940: Max 2 1/2 OEI | 1090: Max for starting Engine",
            ["300-810 Cont, 810 Max Cont, 810-940 OEI, 820 Max Cont OEI, 940 Max 2 1/2 OEI, 1090 Starting"],
            [
                {"id": "sub_1", "label": "Green arc (300-810)", "answer": "Continuous Operation", "acceptedAnswers": ["Continuous Operation", "Cont. Operation", "Cont"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_2", "label": "Red line (810)", "answer": "Max Continuous", "acceptedAnswers": ["Max Continuous", "Maximum Continuous", "Max Cont"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_3", "label": "Yellow arc (810-940)", "answer": "OEI Operation", "acceptedAnswers": ["OEI Operation", "OEI"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_4", "label": "Red line (820, 940)", "answer": "820: Max Cont. OEI | 940: Max 2 1/2 OEI", "acceptedAnswers": ["820: Max Cont. OEI | 940: Max 2 1/2 OEI", "820 Max Cont OEI, 940 Max 2 1/2 OEI"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_5", "label": "Red triangle (1090)", "answer": "Max for starting Engine", "acceptedAnswers": ["Max for starting Engine", "Starting", "Starting Engine", "Max Starting"], "placeholder": "Batas / arti penunjukan..."}
            ]
        ),
        (
            "Hydraulic Pressure Dial Markings",
            "Hydraulic Pressure: Red line (600), Yellow arc (600-900), Green arc (900-1100), Red line (1100)",
            "600: Minimum | 600-900: Caution | 900-1100: Continuous operation | 1100: Maximum",
            ["600 Min, 600-900 Caution, 900-1100 Cont, 1100 Max"],
            [
                {"id": "sub_1", "label": "Red line (600)", "answer": "Minimum", "acceptedAnswers": ["Minimum", "Min"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_2", "label": "Yellow arc (600-900)", "answer": "Caution", "acceptedAnswers": ["Caution"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_3", "label": "Green arc (900-1100)", "answer": "Continuous operation", "acceptedAnswers": ["Continuous operation", "Cont. operation", "Cont operation", "Continuous", "Cont"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_4", "label": "Red line (1100)", "answer": "Maximum", "acceptedAnswers": ["Maximum", "Max"], "placeholder": "Batas / arti penunjukan..."}
            ]
        ),
        (
            "Fuel Pressure Dial Markings",
            "Fuel Pressure: Red line (4), Green arc (4-35), Red line (35)",
            "4: Minimum | 4-35: Continuous operation | 35: Maximum",
            ["4 Min, 4-35 Cont, 35 Max"],
            [
                {"id": "sub_1", "label": "Red line (4)", "answer": "Minimum", "acceptedAnswers": ["Minimum", "Min"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_2", "label": "Green arc (4-35)", "answer": "Continuous operation", "acceptedAnswers": ["Continuous operation", "Cont. operation", "Cont operation", "Continuous", "Cont"], "placeholder": "Batas / arti penunjukan..."},
                {"id": "sub_3", "label": "Red line (35)", "answer": "Maximum", "acceptedAnswers": ["Maximum", "Max"], "placeholder": "Batas / arti penunjukan..."}
            ]
        )
    ]

    for idx, item in enumerate(indicator_data, 1):
        cat, q_text, ans, accepted = item[0], item[1], item[2], item[3]
        sub_questions = item[4] if len(item) > 4 else None
        q_obj = {
            "id": f"B412-IND-{idx:03d}",
            "aircraft": "BELL 412 EP",
            "section": "INDICATOR LIMITATION",
            "category": cat,
            "questionType": "fill-blank",
            "question": q_text,
            "answer": ans,
            "acceptedAnswers": accepted,
            "unit": "",
            "sourceDocument": "bold face bell 412 EP.pdf",
            "sourcePage": 21 + (idx - 1) // 3,
            "points": 1,
            "verified": True
        }
        if sub_questions:
            q_obj["subQuestions"] = sub_questions
        questions.append(q_obj)

    # Emergency Procedures
    emergencies = [
        ("Terminology", "LAND AS SOON AS POSSIBLE definition", "Land without delay at the nearest suitable area (i.e. open field) at which safe approach and landing is reasonably assured", ["Land without delay at the nearest suitable area", "Land without delay at the nearest suitable area (i.e. open field) at which safe approach and landing is reasonably assured", "Land without delay at nearest suitable area"]),
        ("Terminology", "LAND AS SOON AS PRACTICAL definition", "The duration of the flight and landing site are at the discretion of the pilot. Extended flight beyond the nearest approved landing area is not recommended", ["The duration of the flight and landing site are at the discretion of the pilot", "The duration of the flight and landing site are at the discretion of the pilot. Extended flight beyond the nearest approved landing area is not recommended"]),
        ("Single Engine Failure", "Single Engine Failure: List 4 primary indications", "ENG 1 OUT or ENG 2 OUT W/L ILLUMINATE; N1 drop below 53% and decreasing; N2 drop below 85% and decreasing; ITT drop below 400°C and decreasing", ["ENG 1 OUT, N1 drop below 53%, N2 drop below 85%, ITT drop below 400°C", "ENG OUT, N1 below 53%, N2 below 85%, ITT below 400C"]),
        (
            "Single Engine Failure",
            "Single Engine Failure: FLY THE A/C immediate actions (steps a, b, c)",
            "a. Reduce power | b. Set airspeed 70 kts | c. Set N2 100% if possible",
            ["Reduce power, Set airspeed 70 kts, Set N2 100%", "Reduce power, 70 kts, N2 100%"],
            [
                {"id": "step_a", "label": "Step a (Power)", "answer": "Reduce power", "acceptedAnswers": ["Reduce power"], "placeholder": "Tindakan step a..."},
                {"id": "step_b", "label": "Step b (Airspeed)", "answer": "Set airspeed 70 kts", "acceptedAnswers": ["Set airspeed 70 kts", "70 kts", "Airspeed 70 kts", "70 knots"], "placeholder": "Tindakan step b..."},
                {"id": "step_c", "label": "Step c (N2)", "answer": "Set N2 100% if possible", "acceptedAnswers": ["Set N2 100% if possible", "Set N2 100%", "N2 100%", "N2 100% if possible"], "placeholder": "Tindakan step c..."}
            ]
        ),
        ("Single Engine Failure", "Single Engine Failure: IDENTIFY & Engine shutdown steps (steps d, e, f, g)", "d. IDLE STOP RELEASE to affected Eng | e. THROTTLE - CLOSED | f. BOOST PUMP - OFF | g. FUEL SWITCH - OFF", ["IDLE STOP RELEASE, THROTTLE CLOSED, BOOST PUMP OFF, FUEL SWITCH OFF"]),
        ("Dual Engine Failure", "Dual Engine Failure: AUTOROTATION immediate actions (steps a, b, c, d)", "a. Collective FULL DOWN | b. THROTTLE - CLOSE | c. Set airspeed 65 - 90 kts | d. ROTOR RPM - ON THE GREEN", ["Collective FULL DOWN, THROTTLE CLOSE, airspeed 65-90 kts, ROTOR RPM ON THE GREEN"]),
        (
            "Dual Engine Failure",
            "Dual Engine Failure: Altimeter reading actions (e. 300 FT AGL, f. 100 FT AGL)",
            "e. 300 FT AGL - OPEN THROTTLE | f. 100 FT AGL - FLARE",
            ["300 FT OPEN THROTTLE, 100 FT FLARE", "300 FT AGL OPEN THROTTLE, 100 FT AGL FLARE"],
            [
                {"id": "step_e", "label": "300 FT AGL (Step e)", "answer": "OPEN THROTTLE", "acceptedAnswers": ["OPEN THROTTLE", "Open throttle"], "placeholder": "Tindakan 300 FT AGL..."},
                {"id": "step_f", "label": "100 FT AGL (Step f)", "answer": "FLARE", "acceptedAnswers": ["FLARE", "Flare"], "placeholder": "Tindakan 100 FT AGL..."}
            ]
        ),
        (
            "Engine Fire In Flight",
            "Engine Fire in Flight: Immediate initial actions (steps a, b)",
            "a. FIRE PULL handle (affected Eng) - PULL | b. FIRE EXT - MAIN",
            ["FIRE PULL handle PULL, FIRE EXT MAIN", "FIRE PULL PULL, FIRE EXT MAIN"],
            [
                {"id": "step_a", "label": "Step a (FIRE PULL)", "answer": "FIRE PULL handle (affected Eng) - PULL", "acceptedAnswers": ["FIRE PULL handle (affected Eng) - PULL", "FIRE PULL handle PULL", "FIRE PULL PULL"], "placeholder": "Tindakan step a..."},
                {"id": "step_b", "label": "Step b (FIRE EXT)", "answer": "FIRE EXT - MAIN", "acceptedAnswers": ["FIRE EXT - MAIN", "FIRE EXT MAIN"], "placeholder": "Tindakan step b..."}
            ]
        ),
        ("Engine Fire In Flight", "Engine Fire in Flight: If 10 second FIRE PULL W/L remains ON", "FIRE EXT - RESERVE", ["FIRE EXT - RESERVE", "FIRE EXT RESERVE", "RESERVE"]),
        ("Pedal Malfunction", "RIGHT PEDAL LOCKED FORWARD OR NEUTRAL: Approach & Touchdown technique", "Shallow to normal approach; 2 to 5 ft AGL - Slowly reduce THROTTLE (luruskan heading); RUN ON LANDING", ["Shallow to normal approach, 2 to 5 ft reduce throttle, RUN ON LANDING"]),
        ("Pedal Malfunction", "LEFT PEDAL LOCKED FORWARD: Approach & Touchdown technique", "Normal to steep approach; 2 ft AGL - Apply COLLECTIVE as necessary (luruskan heading); ZERO SPEED TOUCHDOWN", ["Normal to steep approach, 2 ft apply collective, ZERO SPEED TOUCHDOWN"]),
        ("Hydraulic Failure", "HYDRAULIC SYSTEM FAILURE: Procedure steps (e, f, g, h)", "e. Affected system - IDENTIFY POSITIVELY | f. HYD SYS switch - OFF (affected system) | g. Set N2 100% | h. MASTER CAUTION - RESET | LAND AS SOON AS POSSIBLE", ["IDENTIFY POSITIVELY, HYD SYS switch OFF, Set N2 100%, MASTER CAUTION RESET"])
    ]

    for idx, item in enumerate(emergencies, 1):
        cat, q_text, ans, accepted = item[0], item[1], item[2], item[3]
        sub_questions = item[4] if len(item) > 4 else None
        q_obj = {
            "id": f"B412-EMER-{idx:03d}",
            "aircraft": "BELL 412 EP",
            "section": "EMERGENCY PROCEDURES",
            "category": cat,
            "questionType": "fill-blank",
            "question": q_text,
            "answer": ans,
            "acceptedAnswers": accepted,
            "unit": "",
            "sourceDocument": "bold face bell 412 EP.pdf",
            "sourcePage": 13 + (idx - 1) // 4,
            "points": 1,
            "verified": True
        }
        if sub_questions:
            q_obj["subQuestions"] = sub_questions
        questions.append(q_obj)

    return {
        "aircraft": "BELL 412 EP",
        "title": "BOLD FACE LIMITATION & EMERGENCY BELL 412 EP",
        "sourceDocument": "bold face bell 412 EP.pdf",
        "description": "Limitation 106 item lengkap, Indicator limitation ranges, dan Emergency Procedures Bell 412 EP",
        "totalQuestions": len(questions),
        "questions": questions
    }

def build_fennec_as550():
    fennec_items = [
        ("Weight Limitation", "Maximum internal weight for flight, take-off and landing with non-jettisonable load", "2250 kg", ["2250", "2.250", "2250 kg", "2250kg"], "kg", 1),
        ("Weight Limitation", "Minimum internal weight for flight, take-off and landing", "1310 kg", ["1310", "1.310", "1310 kg", "1310kg"], "kg", 1),
        ("VNE Limitation", "VNE power off", "125 kts", ["125", "125 kts", "125 kias", "125 knots"], "kts", 1),
        ("VNE Limitation", "VNE power On", "155 kts", ["155", "155 kts", "155 kias", "155 knots"], "kts", 1),
        ("Maximum Operating Altitude", "Maximum operating Altitude", "23.000 ft", ["23.000", "23000", "23.000 ft", "23000 ft", "23,000"], "ft", 1),
        ("Slope Landing Limitation", "Landing and rotor stopping limitation on slope: Nose up", "10°", ["10", "10°", "10 deg", "10 degrees"], "°", 1),
        ("Slope Landing Limitation", "Landing and rotor stopping limitation on slope: Nose down", "6°", ["6", "6°", "6 deg", "6 degrees"], "°", 1),
        ("Slope Landing Limitation", "Landing and rotor stopping limitation on slope: Sideways", "8°", ["8", "8°", "8 deg", "8 degrees"], "°", 1),
        ("Running Landings", "Excluding emergencies and failures, maximum speed for performing running landings", "40 kts", ["40", "40 kts", "40 knots", "40 kias"], "kts", 1),
        ("Main Rotor Limitation", "Rotor Brake operation max. speed", "170 rpm", ["170", "170 rpm"], "rpm", 1),
        ("Main Rotor Limitation", "Minimum power off rotor speed", "320 rpm", ["320", "320 rpm"], "rpm", 1),
        ("Main Rotor Limitation", "Caution Range I rotor speed", "320 to 375 rpm", ["320 to 375", "320-375", "320 to 375 rpm"], "rpm", 1),
        ("Main Rotor Limitation", "Normal operation range rotor speed", "375 to 405 rpm", ["375 to 405", "375-405", "375 to 405 rpm"], "rpm", 1),
        ("Main Rotor Limitation", "Caution range II rotor speed", "405 to 430 rpm", ["405 to 430", "405-430", "405 to 430 rpm"], "rpm", 1),
        ("Main Rotor Limitation", "Max power off rotor speed", "430 rpm", ["430", "430 rpm"], "rpm", 1),
        ("Main Rotor Limitation", "LOW AURAL WARNING rotor threshold", "< 360 rpm", ["< 360", "<360", "< 360 rpm", "360 rpm", "360"], "rpm", 1),
        ("Main Rotor Limitation", "HIGH AURAL WARNING rotor threshold", "> 410 rpm", ["> 410", ">410", "> 410 rpm", "410 rpm", "410"], "rpm", 1),
        ("First Limitation Indicator (FLI)", "FLI Max continuous rating", "9,6", ["9.6", "9,6", "9.6 rating"], "", 1),
        ("First Limitation Indicator (FLI)", "FLI Take off power range", "9,6 to 10", ["9.6 to 10", "9,6 to 10", "9.6-10", "9,6-10"], "", 1),
        ("First Limitation Indicator (FLI)", "FLI Max take off rating", "10", ["10", "10.0"], "", 1),
        ("First Limitation Indicator (FLI)", "FLI Max transient rating (5 sec)", "10,4", ["10.4", "10,4"], "", 1),
        ("Torque Transmission Limitation", "Torque Transmission: Max continuous rating", "92,7 %", ["92.7", "92,7", "92.7 %", "92,7 %", "92.7%"], "%", 1),
        ("Torque Transmission Limitation", "Torque Transmission: Take off power range", "92,7 to 100 %", ["92.7 to 100", "92,7 to 100", "92.7-100%", "92.7 to 100 %"], "%", 1),
        ("Torque Transmission Limitation", "Torque Transmission: Max take off rating", "100 %", ["100", "100 %", "100%"], "%", 1),
        ("Torque Transmission Limitation", "Torque Transmission: Max transient rating (5 sec)", "104 %", ["104", "104 %", "104%"], "%", 1),
        ("N2 Limitation", "N2 Minimum", "367 rpm", ["367", "367 rpm"], "rpm", 2),
        ("N2 Limitation", "N2 Normal operating range", "367 to 413 rpm", ["367 to 413", "367-413", "367 to 413 rpm"], "rpm", 2),
        ("N2 Limitation", "N2 Max continuous", "413 rpm", ["413", "413 rpm"], "rpm", 2),
        ("N2 Limitation", "N2 Max Transient Limit (20 sec)", "440 rpm", ["440", "440 rpm"], "rpm", 2),
        ("N1 Limitation", "N1 Min Stabilized Speed", "67%", ["67", "67%", "67 %"], "%", 2),
        ("N1 Limitation", "N1 Max continuous rating", "ΔN1 = -4 (-4 %)", ["ΔN1 = -4", "-4", "-4%", "-4 %", "dN1 = -4"], "%", 2),
        ("N1 Limitation", "N1 Take off power", "ΔN1 = -4 % to 0% (-4%)", ["ΔN1 = -4 % to 0%", "-4% to 0%", "-4 to 0", "-4% to 0"], "%", 2),
        ("N1 Limitation", "N1 Max take off rating", "ΔN1 = 0 % (0 %)", ["ΔN1 = 0 %", "0", "0%", "0 %", "dN1 = 0"], "%", 2),
        ("N1 Limitation", "N1 Max transient rating (≤20 sec)", "ΔN1 = +1 % (1 %)", ["ΔN1 = +1 %", "+1", "+1%", "+1 %", "1%"], "%", 2),
        ("TOT Limitation", "TOT Starting Limitation: Max continuous", "750 °C", ["750", "750 °C", "750 C", "750°C"], "°C", 2),
        ("TOT Limitation", "TOT Starting Limitation: Max transient (10 sec)", "840 °C", ["840", "840 °C", "840 C", "840°C"], "°C", 2),
        ("TOT Limitation", "TOT Flight Limitation: Max continuous rating", "905 °C", ["905", "905 °C", "905 C", "905°C"], "°C", 2),
        ("TOT Limitation", "TOT Flight Limitation: Takeoff power range", "905 to 949 °C", ["905 to 949", "905-949", "905 to 949 °C"], "°C", 2),
        ("TOT Limitation", "TOT Flight Limitation: Max takeoff rating", "949 °C", ["949", "949 °C", "949 C", "949°C"], "°C", 2),
        ("TOT Limitation", "TOT Flight Limitation: Max transient (20 sec)", "981 °C", ["981", "981 °C", "981 C", "981°C"], "°C", 2),
        ("Oil Temp and Pressure", "Max oil temperature limitation", "117 °C", ["117", "117 °C", "117 C", "117°C"], "°C", 2),
        ("Oil Temp and Pressure", "Max oil pressure limitation", "Depend on N1", ["Depend on N1", "depend on n1", "Depends on N1", "Tergantung N1"], "", 2),
        ("Electrical Circuit Limitation", "Electrical circuit Max voltage (normal operating range)", "31,5 V ( 26 - 29 V)", ["31.5 V (26 - 29 V)", "31.5 V", "31,5", "31.5", "26 - 29 V", "31.5 V (26-29 V)"], "V", 2),
        ("Electrical Circuit Limitation", "Max current continuous & Starter generator", "150 A / 200 A", ["150 A / 200 A", "150 / 200", "150 A dan 200 A", "150, 200"], "A", 2),
        ("Baggage Compartment Load Limit", "RH cargo compartment", "100 kg", ["100", "100 kg", "100kg"], "kg", 2),
        ("Baggage Compartment Load Limit", "LH cargo compartment", "120 kg", ["120", "120 kg", "120kg"], "kg", 2),
        ("Baggage Compartment Load Limit", "Rear cargo compartment", "80 kg", ["80", "80 kg", "80kg"], "kg", 2),
        ("Cabin Compartment Load Limit", "Rear cabin floor load limit", "310 kg", ["310", "310 kg", "310kg"], "kg", 2),
        ("Cabin Compartment Load Limit", "Forward left cabin floor load limit", "150 kg", ["150", "150 kg", "150kg"], "kg", 2)
    ]

    questions = []
    for idx, (cat, q_text, ans, accepted, unit, page) in enumerate(fennec_items, 1):
        questions.append({
            "id": f"FENNEC-LIM-{idx:03d}",
            "aircraft": "FENNEC AS550",
            "section": "LIMITATION",
            "category": cat,
            "questionType": "fill-blank",
            "question": q_text,
            "answer": ans,
            "acceptedAnswers": accepted,
            "unit": unit,
            "sourceDocument": "BOLD FACE FENNEC AS550.docx",
            "sourcePage": page,
            "points": 1,
            "verified": True
        })

    return {
        "aircraft": "FENNEC AS550",
        "title": "BOLD FACE FENNEC AS550",
        "sourceDocument": "BOLD FACE FENNEC AS550.docx",
        "description": "Limitation Weight, Speed, Altitude, Rotor, FLI, Torque, N1, N2, TOT, Electrical, dan Cargo Helikopter FENNEC AS550",
        "totalQuestions": len(questions),
        "questions": questions
    }

def build_sikorsky_s300c():
    s300c_items = [
        ("LIMITATION", "Berat Beban", "Berat beban (Gross Weight)", "2050 LBS", ["2050", "2050 LBS", "2050 lbs", "2.050"], "LBS", 1),
        ("LIMITATION", "Center of Gravity (CG)", "Gerakan titik berat (CG) maximum ke depan", "95 INCH", ["95", "95 INCH", "95 inch", "95 in"], "INCH", 1),
        ("LIMITATION", "Center of Gravity (CG)", "Gerakan titik berat (CG) maximum ke belakang", "101 INCH", ["101", "101 INCH", "101 inch", "101 in"], "INCH", 1),
        ("LIMITATION", "Kecepatan Max (VNE)", "Kecepatan Max (VNE) Pintu Terbuka", "102 MPH/ 89 KTS", ["102 MPH/ 89 KTS", "102 MPH", "89 KTS", "102 mph / 89 kts", "89 kts"], "MPH / KTS", 1),
        ("LIMITATION", "Kecepatan Max (VNE)", "Kecepatan Max (VNE) Pintu Tertutup", "109 MPH/ 95 KTS", ["109 MPH/ 95 KTS", "109 MPH", "95 KTS", "109 mph / 95 kts", "95 kts"], "MPH / KTS", 1),
        ("LIMITATION", "Oil Temp", "Temperatur Minyak Mesin: Garis Merah Radial / Bilah Hijau", "260°F / 100°F SAMPAI 250°F", ["260 / 100-250", "260°F / 100°F-250°F", "260, 100 sampai 250"], "°F", 1),
        ("LIMITATION", "Oil Press", "Tekanan Minyak Mesin: Garis Merah Radial / Bilah Hijau", "55 DAN 115 PSI / 55 SAMPAI 95 PSI", ["55 dan 115 / 55-95", "55 & 115 PSI / 55-95 PSI", "55 dan 115, 55 sampai 95"], "PSI", 1),
        ("LIMITATION", "CHT", "Temperature Head Cylinder (CHT): Garis Merah / Bilah Kuning / Bilah Hijau", "500°F / 450°F SAMPAI 500°F / 230°F SAMPAI 450°F", ["500 / 450-500 / 230-450", "500°F, 450-500°F, 230-450°F"], "°F", 1),
        ("LIMITATION", "Fuel Press", "Tekanan Bahan Bakar (Fuel Press): Garis Merah Radial / Bilah Hijau", "14 DAN 35 PSI / 14 DAN 30 PSI", ["14 dan 35 / 14 dan 30", "14 & 35 PSI / 14-30 PSI", "14 dan 35, 14 sampai 30"], "PSI", 1),
        ("LIMITATION", "Engine RPM", "Putaran Mesin (Lycoming HIO-360-DIA): Merah / Hijau Radial / Hijau Power", "3000 DAN 3200 RPM / 1200 SAMPAI 1600 RPM / 3000 SAMPAI 3200 RPM", ["3000 dan 3200 / 1200-1600 / 3000-3200", "3000-3200, 1200-1600, 3000-3200"], "RPM", 1),
        ("LIMITATION", "Engine RPM", "Putaran Mesin (Lycoming HIO-360-GIA): Merah / Hijau Radial / Hijau Power", "2500 DAN 2700 RPM / 1200 SAMPAI 1600 RPM / 2500 SAMPAI 2700 RPM", ["2500 dan 2700 / 1200-1600 / 2500-2700", "2500-2700, 1200-1600, 2500-2700"], "RPM", 1),
        ("LIMITATION", "Rotor RPM", "Putaran Baling-Baling Utama: Garis Merah Radial / Bilah Hijau", "390 DAN 504 RPM / 390 SAMPAI 504 RPM", ["390 dan 504 / 390-504", "390 & 504 / 390 sampai 504"], "RPM", 2),
        ("LIMITATION", "Manifold Press", "Tekanan Manifold: Garis Merah Radial / Bilah Kuning", "27,2 INCH MP / 23,3 SAMPAI 27,2 INCH MP", ["27.2 / 23.3-27.2", "27,2 / 23,3 sampai 27,2", "27.2 INCH MP"], "INCH MP", 2),
        ("LIMITATION", "Wind Velocity & Landing", "Max Wind Velocity & Max Running Landing", "20 MPH/ 17 KTS & 40 MPH/ 35 KTS", ["20 MPH/ 17 KTS & 40 MPH/ 35 KTS", "20 MPH / 40 MPH", "17 KTS / 35 KTS"], "MPH / KTS", 2),
        ("EMERGENCY", "Engine Fire On The Ground", "Tindakan Engine Fire On The Ground (a sampai e)", "a. Mixture Idle Cut Off, b. Fuel Valve closed, c. Battery Off, d. Alternator Off, e. Exit A/C with fire extinguisher", ["Mixture Idle Cut Off, Fuel Valve closed, Battery Off, Alternator Off, Exit A/C with fire extinguisher"], "", 2),
        ("EMERGENCY", "Transmission W/L", "Main Rotor Xmsn W/L ON: Indikasi & Tindakan", "Oil pressure below 2 1/2 Psi or Oil Temperature above 235°F -> LASAP (Land As Soon As Possible)", ["Oil pressure below 2 1/2 Psi or Oil Temperature above 235°F, LASAP"], "", 2),
        ("EMERGENCY", "Fuel Low", "Fuel Low W/L on: Fuel quantity, Time remaining, Tindakan", "Fuel quantity 1 gallon remain, Time remaining 5 min, Land immediately", ["1 gallon remain, 5 min, Land immediately", "1 gallon, 5 min, Land immediately"], "", 2),
        ("EMERGENCY", "Electrical Fire in Flight", "Tindakan Electrical Fire in Flight (a sampai g)", "a. Set Battery off, b. Alternator on, c. Land immediately, d. Close throttle, e. Mixture idle cut off, f. Fuel valve closed, g. Exit A/C with fire extinguisher", ["Set Battery off, Alternator on, Land immediately, Close throttle, Mixture idle cut off, Fuel valve closed, Exit A/C"], "", 3),
        ("EMERGENCY", "Engine Failure", "Engine Fail Below 7ft: Indikasi & Prosedur", "A/C sudden yawing left -> Maintain collective pitch, Apply right pedal, Apply collective as necessary", ["A/C sudden yawing left, Maintain collective, Apply right pedal, Apply collective as necessary"], "", 3),
        ("EMERGENCY", "Engine Failure", "Engine fail below 450 ft: Prosedur", "a. Lower Collective pitch, b. Maintain RPM, c. Control cyclic and collective to maintain A/C settle, d. Set Attitude, e. Prepare ground contact", ["Lower Collective pitch, Maintain RPM, Control cyclic and collective, Set Attitude, Prepare ground contact"], "", 3),
        ("EMERGENCY", "Engine Failure", "Engine Fail Alt above 450 ft: Key autorotation steps", "Steady glide 52 Kts; Backward cyclic at 50 ft; Coordinate cyclic & collective at 10 ft; Lower collective pitch; Land A/C", ["Steady glide 52 Kts, Backward cyclic at 50 ft, Coordinate cyclic and collective at 10 ft, Land A/C"], "", 3),
        ("EMERGENCY", "Tail Rotor Failure", "Tail Rotor Failure Complete lost T/R Thrust indication & Forward Flight", "Indicate by yawing to right; Lower Collective, Set airspeed 50-60 Kts, Move left cyclic, Control collective, Maintain heading, Autorotation", ["Indicate by yawing to right, Lower Collective, Set airspeed 50-60 Kts, Move left cyclic, Autorotation"], "", 4),
        ("EMERGENCY", "Simulated Anti Torque", "Simulated Anti Torque Malfunction: Altitude, Airspeed, RPM, Approach", "Altitude 300 ft AGL, Airspeed 55 kts, RPM 3000 (left) / 3200 (right), Approach 5 to 8 degrees", ["300 ft AGL, 55 kts, RPM 3000 / 3200, Approach 5 to 8 degrees", "300 ft, 55 kts, 3000/3200 RPM, 5-8 degrees"], "", 4)
    ]

    questions = []
    for idx, (sec, cat, q_text, ans, accepted, unit, page) in enumerate(s300c_items, 1):
        questions.append({
            "id": f"S300C-{sec[:3]}-{idx:03d}",
            "aircraft": "SIKORSKY S300C",
            "section": sec,
            "category": cat,
            "questionType": "fill-blank",
            "question": q_text,
            "answer": ans,
            "acceptedAnswers": accepted,
            "unit": unit,
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": page,
            "points": 1,
            "verified": True
        })

    return {
        "aircraft": "SIKORSKY S300C",
        "title": "BOLD FACE & EMERGENCY SIKORSKY S300C",
        "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
        "description": "Limitations, Engine RPM, Manifold Press, dan Prosedur Emergency Sikorsky S300C",
        "totalQuestions": len(questions),
        "questions": questions
    }

def main():
    os.makedirs("data", exist_ok=True)
    
    aircraft_list = [
        ("data/mi-17v5.json", build_mi17v5()),
        ("data/bell-412-ep.json", build_bell412ep()),
        ("data/fennec-as550.json", build_fennec_as550()),
        ("data/sikorsky-s300c.json", build_sikorsky_s300c())
    ]
    
    index_meta = []
    for path, data in aircraft_list:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Wrote {path} with {data['totalQuestions']} questions.")
        
        # Collect categories
        cats = sorted(list(set(q["category"] for q in data["questions"])))
        sections = sorted(list(set(q["section"] for q in data["questions"])))
        index_meta.append({
            "aircraft": data["aircraft"],
            "title": data["title"],
            "file": path.replace("\\", "/"),
            "sourceDocument": data["sourceDocument"],
            "description": data["description"],
            "totalQuestions": data["totalQuestions"],
            "categoriesCount": len(cats),
            "categories": cats,
            "sections": sections
        })
        
    with open("data/aircraft-index.json", "w", encoding="utf-8") as f:
        json.dump(index_meta, f, indent=2, ensure_ascii=False)
    print("Wrote data/aircraft-index.json successfully.")

if __name__ == "__main__":
    main()
