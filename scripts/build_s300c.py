# -*- coding: utf-8 -*-
"""
Builder for SIKORSKY S-300C Bold Face & Emergency Dataset
Standardizes questions with exact subQuestions (a., b., c., etc.)
matching the user's official military document layout and numbering.
"""
import json
import os

def build_s300c():
    questions = [
        # 1. Gross Weight
        {
            "id": "S300C-LIM-001",
            "aircraft": "SIKORSKY S300C",
            "section": "LIMITATION",
            "category": "Gross Weight",
            "questionType": "fill-blank",
            "question": "1. Berat Beban (Gross Weight)",
            "answer": "2050 LBS",
            "acceptedAnswers": [
                "2050",
                "2050 LBS",
                "2050 lbs",
                "2.050",
                "2,050",
                "2050LBS"
            ],
            "unit": "LBS",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 1,
            "points": 1,
            "verified": True
        },
        # 2. Centre of Gravity (CG)
        {
            "id": "S300C-LIM-002",
            "aircraft": "SIKORSKY S300C",
            "section": "LIMITATION",
            "category": "Centre of Gravity (CG)",
            "questionType": "fill-blank",
            "question": "2. Centre of Gravity (CG)",
            "answer": "a. Gerakan Titik Berat (CG) Maximum ke Depan 95 INCH | b. Gerakan Titik Berat (CG) Maximum ke Belakang 101 INCH",
            "acceptedAnswers": [
                "95 INCH, 101 INCH",
                "95, 101",
                "95 / 101",
                "95/101"
            ],
            "unit": "INCH",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Gerakan Titik Berat (CG) Maximum ke Depan",
                    "answer": "95 INCH",
                    "acceptedAnswers": [
                        "95",
                        "95 INCH",
                        "95 inch",
                        "95 in",
                        "95INCH"
                    ],
                    "unit": "INCH",
                    "placeholder": "Nilai batas ke depan (misal: 95 INCH)..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Gerakan Titik Berat (CG) Maximum ke Belakang",
                    "answer": "101 INCH",
                    "acceptedAnswers": [
                        "101",
                        "101 INCH",
                        "101 inch",
                        "101 in",
                        "101INCH"
                    ],
                    "unit": "INCH",
                    "placeholder": "Nilai batas ke belakang (misal: 101 INCH)..."
                }
            ]
        },
        # 3. Kecepatan Max (VNE)
        {
            "id": "S300C-LIM-003",
            "aircraft": "SIKORSKY S300C",
            "section": "LIMITATION",
            "category": "Kecepatan Max (VNE)",
            "questionType": "fill-blank",
            "question": "3. Kecepatan Max (VNE)",
            "answer": "a. Pintu Terbuka 102 MPH/ 89 KTS | b. Pintu Tertutup 109 MPH/ 95 KTS",
            "acceptedAnswers": [
                "102 MPH/ 89 KTS, 109 MPH/ 95 KTS",
                "102/89, 109/95",
                "102, 109",
                "89, 95"
            ],
            "unit": "MPH / KTS",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Pintu Terbuka",
                    "answer": "102 MPH/ 89 KTS",
                    "acceptedAnswers": [
                        "102",
                        "89",
                        "102 MPH",
                        "89 KTS",
                        "102/89",
                        "102 / 89",
                        "102 MPH/ 89 KTS",
                        "102 MPH / 89 KTS",
                        "102 mph",
                        "89 kts"
                    ],
                    "unit": "MPH / KTS",
                    "placeholder": "102 MPH atau 89 KTS..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Pintu Tertutup",
                    "answer": "109 MPH/ 95 KTS",
                    "acceptedAnswers": [
                        "109",
                        "95",
                        "109 MPH",
                        "95 KTS",
                        "109/95",
                        "109 / 95",
                        "109 MPH/ 95 KTS",
                        "109 MPH / 95 KTS",
                        "109 mph",
                        "95 kts"
                    ],
                    "unit": "MPH / KTS",
                    "placeholder": "109 MPH atau 95 KTS..."
                }
            ]
        },
        # 4. Temperatur Minyak Mesin (Oil Temp)
        {
            "id": "S300C-LIM-004",
            "aircraft": "SIKORSKY S300C",
            "section": "LIMITATION",
            "category": "Oil Temp",
            "questionType": "fill-blank",
            "question": "4. Temperatur Minyak Mesin (Oil Temp)",
            "answer": "a. Garis Merah Radial 260°F | b. Bilah Hijau 100°F SAMPAI 250°F",
            "acceptedAnswers": [
                "260°F, 100°F SAMPAI 250°F",
                "260 / 100-250",
                "260/100-250",
                "260, 100-250"
            ],
            "unit": "°F",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Garis Merah Radial",
                    "answer": "260°F",
                    "acceptedAnswers": [
                        "260",
                        "260°F",
                        "260 F",
                        "260F",
                        "260 DEG F",
                        "260°"
                    ],
                    "unit": "°F",
                    "placeholder": "Nilai Garis Merah Radial (misal: 260°F)..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Bilah Hijau",
                    "answer": "100°F SAMPAI 250°F",
                    "acceptedAnswers": [
                        "100-250",
                        "100 - 250",
                        "100 sampai 250",
                        "100°F SAMPAI 250°F",
                        "100°F-250°F",
                        "100 F - 250 F",
                        "100-250°F",
                        "100 to 250",
                        "100 s/d 250"
                    ],
                    "unit": "°F",
                    "placeholder": "Rentang Bilah Hijau (misal: 100-250°F)..."
                }
            ]
        },
        # 5. Tekanan Minyak Mesin (Oil Press)
        {
            "id": "S300C-LIM-005",
            "aircraft": "SIKORSKY S300C",
            "section": "LIMITATION",
            "category": "Oil Press",
            "questionType": "fill-blank",
            "question": "5. Tekanan Minyak Mesin (Oil Press)",
            "answer": "a. Garis Merah Radial 55 DAN 115 PSI | b. Bilah Hijau 55 SAMPAI 95 PSI",
            "acceptedAnswers": [
                "55 DAN 115 PSI, 55 SAMPAI 95 PSI",
                "55 dan 115 / 55-95",
                "55 dan 115/55-95",
                "55 & 115 / 55-95"
            ],
            "unit": "PSI",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Garis Merah Radial",
                    "answer": "55 DAN 115 PSI",
                    "acceptedAnswers": [
                        "55 dan 115",
                        "55 & 115",
                        "55, 115",
                        "55 and 115",
                        "55 DAN 115 PSI",
                        "55 & 115 PSI",
                        "55 dan 115 psi",
                        "55/115",
                        "55 / 115"
                    ],
                    "unit": "PSI",
                    "placeholder": "Garis Merah Radial (misal: 55 dan 115 PSI)..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Bilah Hijau",
                    "answer": "55 SAMPAI 95 PSI",
                    "acceptedAnswers": [
                        "55-95",
                        "55 - 95",
                        "55 sampai 95",
                        "55 SAMPAI 95 PSI",
                        "55-95 PSI",
                        "55-95 psi",
                        "55 to 95",
                        "55 s/d 95"
                    ],
                    "unit": "PSI",
                    "placeholder": "Rentang Bilah Hijau (misal: 55-95 PSI)..."
                }
            ]
        },
        # 6. Temperature Head Cylinder (CHT)
        {
            "id": "S300C-LIM-006",
            "aircraft": "SIKORSKY S300C",
            "section": "LIMITATION",
            "category": "CHT",
            "questionType": "fill-blank",
            "question": "6. Temperature Head Cylinder (CHT)",
            "answer": "a. Garis Merah Radial 500°F | b. Bilah Kuning 450°F SAMPAI 500°F | c. Bilah Hijau 230°F SAMPAI 450°F",
            "acceptedAnswers": [
                "500 / 450-500 / 230-450",
                "500°F, 450-500°F, 230-450°F"
            ],
            "unit": "°F",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 1,
            "points": 3,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Garis Merah Radial",
                    "answer": "500°F",
                    "acceptedAnswers": [
                        "500",
                        "500°F",
                        "500 F",
                        "500F",
                        "500 deg f"
                    ],
                    "unit": "°F",
                    "placeholder": "Garis Merah Radial (misal: 500°F)..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Bilah Kuning",
                    "answer": "450°F SAMPAI 500°F",
                    "acceptedAnswers": [
                        "450-500",
                        "450 - 500",
                        "450 sampai 500",
                        "450°F SAMPAI 500°F",
                        "450°F-500°F",
                        "450-500°F",
                        "450 to 500",
                        "450 s/d 500"
                    ],
                    "unit": "°F",
                    "placeholder": "Bilah Kuning (misal: 450-500°F)..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Bilah Hijau",
                    "answer": "230°F SAMPAI 450°F",
                    "acceptedAnswers": [
                        "230-450",
                        "230 - 450",
                        "230 sampai 450",
                        "230°F SAMPAI 450°F",
                        "230°F-450°F",
                        "230-450°F",
                        "230 to 450",
                        "230 s/d 450"
                    ],
                    "unit": "°F",
                    "placeholder": "Bilah Hijau (misal: 230-450°F)..."
                }
            ]
        },
        # 7. Tekanan Bahan Bakar (Fuel Press)
        {
            "id": "S300C-LIM-007",
            "aircraft": "SIKORSKY S300C",
            "section": "LIMITATION",
            "category": "Fuel Press",
            "questionType": "fill-blank",
            "question": "7. Tekanan Bahan Bakar (Fuel Press)",
            "answer": "a. Garis Merah Radial 14 DAN 35 PSI | b. Bilah Hijau 14 DAN 30 PSI",
            "acceptedAnswers": [
                "14 DAN 35 PSI, 14 DAN 30 PSI",
                "14 dan 35 / 14 dan 30",
                "14 & 35 / 14 & 30",
                "14-35 / 14-30"
            ],
            "unit": "PSI",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 1,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Garis Merah Radial",
                    "answer": "14 DAN 35 PSI",
                    "acceptedAnswers": [
                        "14 dan 35",
                        "14 & 35",
                        "14, 35",
                        "14 and 35",
                        "14 DAN 35 PSI",
                        "14 & 35 PSI",
                        "14/35",
                        "14-35"
                    ],
                    "unit": "PSI",
                    "placeholder": "Garis Merah Radial (misal: 14 dan 35 PSI)..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Bilah Hijau",
                    "answer": "14 DAN 30 PSI",
                    "acceptedAnswers": [
                        "14 dan 30",
                        "14 & 30",
                        "14, 30",
                        "14-30",
                        "14 sampai 30",
                        "14 DAN 30 PSI",
                        "14 & 30 PSI",
                        "14 and 30",
                        "14/30"
                    ],
                    "unit": "PSI",
                    "placeholder": "Bilah Hijau (misal: 14 dan 30 PSI)..."
                }
            ]
        },
        # 8. Penunjuk Putaran Mesin (Lycoming HIO-360-DIA)
        {
            "id": "S300C-LIM-008",
            "aircraft": "SIKORSKY S300C",
            "section": "LIMITATION",
            "category": "Engine RPM",
            "questionType": "fill-blank",
            "question": "8. Penunjuk Putaran Mesin (Lycoming HIO-360-DIA)",
            "answer": "a. Garis Merah Radial 3000 DAN 3200 RPM | b. Bilah Hijau Radial 1200 SAMPAI 1600 RPM | c. Bilah Hijau Power 3000 SAMPAI 3200 RPM",
            "acceptedAnswers": [
                "3000 dan 3200 / 1200-1600 / 3000-3200",
                "3000-3200, 1200-1600, 3000-3200"
            ],
            "unit": "RPM",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 1,
            "points": 3,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Garis Merah Radial",
                    "answer": "3000 DAN 3200 RPM",
                    "acceptedAnswers": [
                        "3000 dan 3200",
                        "3000 & 3200",
                        "3000, 3200",
                        "3000 and 3200",
                        "3000 DAN 3200 RPM",
                        "3000-3200",
                        "3000/3200"
                    ],
                    "unit": "RPM",
                    "placeholder": "Garis Merah Radial (misal: 3000 dan 3200 RPM)..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Bilah Hijau Radial",
                    "answer": "1200 SAMPAI 1600 RPM",
                    "acceptedAnswers": [
                        "1200-1600",
                        "1200 - 1600",
                        "1200 sampai 1600",
                        "1200 SAMPAI 1600 RPM",
                        "1200-1600 RPM",
                        "1200 to 1600"
                    ],
                    "unit": "RPM",
                    "placeholder": "Bilah Hijau Radial (misal: 1200 sampai 1600 RPM)..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Bilah Hijau Power",
                    "answer": "3000 SAMPAI 3200 RPM",
                    "acceptedAnswers": [
                        "3000-3200",
                        "3000 - 3200",
                        "3000 sampai 3200",
                        "3000 SAMPAI 3200 RPM",
                        "3000-3200 RPM",
                        "3000 to 3200",
                        "3000 dan 3200"
                    ],
                    "unit": "RPM",
                    "placeholder": "Bilah Hijau Power (misal: 3000 sampai 3200 RPM)..."
                }
            ]
        },
        # 9. Penunjuk Putaran Mesin (Lycoming HIO-360-GIA)
        {
            "id": "S300C-LIM-009",
            "aircraft": "SIKORSKY S300C",
            "section": "LIMITATION",
            "category": "Engine RPM",
            "questionType": "fill-blank",
            "question": "9. Penunjuk Putaran Mesin (Lycoming HIO-360-GIA)",
            "answer": "a. Garis Merah Radial 2500 DAN 2700 RPM | b. Bilah Hijau Radial 1200 SAMPAI 1600 RPM | c. Bilah Hijau Power 2500 SAMPAI 2700 RPM",
            "acceptedAnswers": [
                "2500 dan 2700 / 1200-1600 / 2500-2700",
                "2500-2700, 1200-1600, 2500-2700"
            ],
            "unit": "RPM",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 1,
            "points": 3,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Garis Merah Radial",
                    "answer": "2500 DAN 2700 RPM",
                    "acceptedAnswers": [
                        "2500 dan 2700",
                        "2500 & 2700",
                        "2500, 2700",
                        "2500 and 2700",
                        "2500 DAN 2700 RPM",
                        "2500-2700",
                        "2500/2700"
                    ],
                    "unit": "RPM",
                    "placeholder": "Garis Merah Radial (misal: 2500 dan 2700 RPM)..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Bilah Hijau Radial",
                    "answer": "1200 SAMPAI 1600 RPM",
                    "acceptedAnswers": [
                        "1200-1600",
                        "1200 - 1600",
                        "1200 sampai 1600",
                        "1200 SAMPAI 1600 RPM",
                        "1200-1600 RPM",
                        "1200 to 1600"
                    ],
                    "unit": "RPM",
                    "placeholder": "Bilah Hijau Radial (misal: 1200 sampai 1600 RPM)..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Bilah Hijau Power",
                    "answer": "2500 SAMPAI 2700 RPM",
                    "acceptedAnswers": [
                        "2500-2700",
                        "2500 - 2700",
                        "2500 sampai 2700",
                        "2500 SAMPAI 2700 RPM",
                        "2500-2700 RPM",
                        "2500 to 2700",
                        "2500 dan 2700"
                    ],
                    "unit": "RPM",
                    "placeholder": "Bilah Hijau Power (misal: 2500 sampai 2700 RPM)..."
                }
            ]
        },
        # 10. Putaran Baling-Baling Utama (Rotor RPM)
        {
            "id": "S300C-LIM-010",
            "aircraft": "SIKORSKY S300C",
            "section": "LIMITATION",
            "category": "Rotor RPM",
            "questionType": "fill-blank",
            "question": "10. Putaran Baling-Baling Utama (Rotor RPM)",
            "answer": "a. Garis Merah Radial 390 DAN 504 RPM | b. Bilah Hijau 390 SAMPAI 504 RPM",
            "acceptedAnswers": [
                "390 dan 504 / 390-504",
                "390 & 504 / 390 sampai 504"
            ],
            "unit": "RPM",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 2,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Garis Merah Radial",
                    "answer": "390 DAN 504 RPM",
                    "acceptedAnswers": [
                        "390 dan 504",
                        "390 & 504",
                        "390, 504",
                        "390 DAN 504 RPM",
                        "390 and 504",
                        "390/504",
                        "390-504"
                    ],
                    "unit": "RPM",
                    "placeholder": "Garis Merah Radial (misal: 390 dan 504 RPM)..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Bilah Hijau",
                    "answer": "390 SAMPAI 504 RPM",
                    "acceptedAnswers": [
                        "390-504",
                        "390 - 504",
                        "390 sampai 504",
                        "390 SAMPAI 504 RPM",
                        "390 to 504",
                        "390 s/d 504"
                    ],
                    "unit": "RPM",
                    "placeholder": "Bilah Hijau (misal: 390 sampai 504 RPM)..."
                }
            ]
        },
        # 11. Tekanan Manifold (Manifold Pressure)
        {
            "id": "S300C-LIM-011",
            "aircraft": "SIKORSKY S300C",
            "section": "LIMITATION",
            "category": "Manifold Press",
            "questionType": "fill-blank",
            "question": "11. Tekanan Manifold (Manifold Pressure)",
            "answer": "a. Garis Merah Radial 27,2 INCH MP | b. Bilah Kuning 23,3 SAMPAI 27,2 INCH MP",
            "acceptedAnswers": [
                "27.2 / 23.3-27.2",
                "27,2 / 23,3 sampai 27,2"
            ],
            "unit": "INCH MP",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 2,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Garis Merah Radial",
                    "answer": "27,2 INCH MP",
                    "acceptedAnswers": [
                        "27.2",
                        "27,2",
                        "27.2 INCH MP",
                        "27,2 INCH MP",
                        "27.2 in mp",
                        "27,2 in mp"
                    ],
                    "unit": "INCH MP",
                    "placeholder": "Garis Merah Radial (misal: 27,2 INCH MP)..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Bilah Kuning",
                    "answer": "23,3 SAMPAI 27,2 INCH MP",
                    "acceptedAnswers": [
                        "23.3-27.2",
                        "23,3-27,2",
                        "23.3 - 27.2",
                        "23,3 - 27,2",
                        "23.3 sampai 27.2",
                        "23,3 sampai 27,2",
                        "23,3 SAMPAI 27,2 INCH MP",
                        "23.3-27.2 INCH MP"
                    ],
                    "unit": "INCH MP",
                    "placeholder": "Bilah Kuning (misal: 23,3 sampai 27,2 INCH MP)..."
                }
            ]
        },
        # 12. Kecepatan Angin & Pendaratan
        {
            "id": "S300C-LIM-012",
            "aircraft": "SIKORSKY S300C",
            "section": "LIMITATION",
            "category": "Wind Velocity & Landing",
            "questionType": "fill-blank",
            "question": "12. Kecepatan Angin & Pendaratan (Wind Velocity & Landing)",
            "answer": "a. Max Wind Velocity 20 MPH/ 17 KTS | b. Max Running Landing 40 MPH/ 35 KTS",
            "acceptedAnswers": [
                "20 MPH/ 17 KTS & 40 MPH/ 35 KTS",
                "20/17 & 40/35",
                "20, 40",
                "17, 35"
            ],
            "unit": "MPH / KTS",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 2,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Max Wind Velocity",
                    "answer": "20 MPH/ 17 KTS",
                    "acceptedAnswers": [
                        "20",
                        "17",
                        "20 MPH",
                        "17 KTS",
                        "20/17",
                        "20 / 17",
                        "20 MPH/ 17 KTS",
                        "20 mph",
                        "17 kts"
                    ],
                    "unit": "MPH / KTS",
                    "placeholder": "20 MPH atau 17 KTS..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Max Running Landing",
                    "answer": "40 MPH/ 35 KTS",
                    "acceptedAnswers": [
                        "40",
                        "35",
                        "40 MPH",
                        "35 KTS",
                        "40/35",
                        "40 / 35",
                        "40 MPH/ 35 KTS",
                        "40 mph",
                        "35 kts"
                    ],
                    "unit": "MPH / KTS",
                    "placeholder": "40 MPH atau 35 KTS..."
                }
            ]
        },
        # 13. Engine Fire On The Ground
        {
            "id": "S300C-EME-013",
            "aircraft": "SIKORSKY S300C",
            "section": "EMERGENCY",
            "category": "Engine Fire On The Ground",
            "questionType": "fill-blank",
            "question": "13. Tindakan Engine Fire On The Ground (Langkah a sampai e)",
            "answer": "a. Mixture Idle Cut Off | b. Fuel Valve closed | c. Battery Off | d. Alternator Off | e. Exit A/C with fire extinguisher",
            "acceptedAnswers": [
                "Mixture Idle Cut Off, Fuel Valve closed, Battery Off, Alternator Off, Exit A/C with fire extinguisher"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 2,
            "points": 5,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Mixture",
                    "answer": "Idle Cut Off",
                    "acceptedAnswers": [
                        "Idle Cut Off",
                        "idle cut off",
                        "cut off",
                        "idle-cut-off"
                    ],
                    "placeholder": "Posisi Mixture..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Fuel Valve",
                    "answer": "Closed",
                    "acceptedAnswers": [
                        "Closed",
                        "closed",
                        "close",
                        "tutup"
                    ],
                    "placeholder": "Posisi Fuel Valve..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Battery",
                    "answer": "Off",
                    "acceptedAnswers": [
                        "Off",
                        "off",
                        "mati"
                    ],
                    "placeholder": "Posisi Battery Switch..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Alternator",
                    "answer": "Off",
                    "acceptedAnswers": [
                        "Off",
                        "off",
                        "mati"
                    ],
                    "placeholder": "Posisi Alternator Switch..."
                },
                {
                    "id": "sub_e",
                    "letter": "e",
                    "label": "Evakuasi",
                    "answer": "Exit A/C with fire extinguisher",
                    "acceptedAnswers": [
                        "Exit A/C with fire extinguisher",
                        "Exit A/C",
                        "Keluar pesawat bawa APAR",
                        "Exit aircraft with fire extinguisher",
                        "fire extinguisher"
                    ],
                    "placeholder": "Tindakan evakuasi..."
                }
            ]
        },
        # 14. Main Rotor Xmsn W/L ON
        {
            "id": "S300C-EME-014",
            "aircraft": "SIKORSKY S300C",
            "section": "EMERGENCY",
            "category": "Transmission W/L",
            "questionType": "fill-blank",
            "question": "14. Main Rotor Xmsn W/L ON: Indikasi & Tindakan",
            "answer": "a. Indikasi Oil pressure below 2 1/2 Psi or Oil Temperature above 235°F | b. Tindakan LASAP (Land As Soon As Possible)",
            "acceptedAnswers": [
                "Oil pressure below 2 1/2 Psi or Oil Temperature above 235°F, LASAP"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 2,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Indikasi Tekanan / Temperatur",
                    "answer": "Oil pressure below 2 1/2 Psi or Oil Temperature above 235°F",
                    "acceptedAnswers": [
                        "Oil pressure below 2 1/2 Psi or Oil Temperature above 235°F",
                        "Oil pressure below 2.5 Psi or Oil Temp above 235°F",
                        "Press below 2.5 Psi or Temp above 235°F",
                        "2 1/2 Psi or 235°F",
                        "2.5 psi or 235 f"
                    ],
                    "placeholder": "Kondisi parameter..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Tindakan Pendaratan",
                    "answer": "LASAP (Land As Soon As Possible)",
                    "acceptedAnswers": [
                        "LASAP",
                        "Land As Soon As Possible",
                        "Mendarat sesegera mungkin",
                        "LASAP (Land As Soon As Possible)"
                    ],
                    "placeholder": "Tindakan (LASAP)..."
                }
            ]
        },
        # 15. Fuel Low W/L ON
        {
            "id": "S300C-EME-015",
            "aircraft": "SIKORSKY S300C",
            "section": "EMERGENCY",
            "category": "Fuel Low",
            "questionType": "fill-blank",
            "question": "15. Fuel Low W/L ON: Fuel Quantity, Time Remaining & Tindakan",
            "answer": "a. Fuel quantity 1 gallon remain | b. Time remaining 5 min | c. Tindakan Land immediately",
            "acceptedAnswers": [
                "1 gallon remain, 5 min, Land immediately",
                "1 gallon, 5 min, Land immediately"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 2,
            "points": 3,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Fuel Quantity Remaining",
                    "answer": "1 gallon remain",
                    "acceptedAnswers": [
                        "1 gallon remain",
                        "1 gallon",
                        "1 gal",
                        "1 galon",
                        "1"
                    ],
                    "unit": "gallon",
                    "placeholder": "Sisa bahan bakar (1 gallon)..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Time Remaining",
                    "answer": "5 min",
                    "acceptedAnswers": [
                        "5 min",
                        "5 minutes",
                        "5 menit",
                        "5"
                    ],
                    "unit": "min",
                    "placeholder": "Sisa waktu terbang (5 min)..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Tindakan",
                    "answer": "Land immediately",
                    "acceptedAnswers": [
                        "Land immediately",
                        "Mendarat seketika",
                        "land immediately",
                        "mendarat darurat"
                    ],
                    "placeholder": "Tindakan pendaratan..."
                }
            ]
        },
        # 16. Electrical Fire in Flight
        {
            "id": "S300C-EME-016",
            "aircraft": "SIKORSKY S300C",
            "section": "EMERGENCY",
            "category": "Electrical Fire in Flight",
            "questionType": "fill-blank",
            "question": "16. Tindakan Electrical Fire in Flight (Langkah a sampai g)",
            "answer": "a. Battery Off | b. Alternator On | c. Land immediately | d. Throttle Close | e. Mixture Idle cut off | f. Fuel valve Closed | g. Exit A/C with fire extinguisher",
            "acceptedAnswers": [
                "Battery Off, Alternator On, Land immediately, Close throttle, Mixture idle cut off, Fuel valve closed, Exit A/C with fire extinguisher"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 3,
            "points": 7,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Set Battery",
                    "answer": "Off",
                    "acceptedAnswers": ["Off", "off", "mati"],
                    "placeholder": "Posisi Battery..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Alternator",
                    "answer": "On",
                    "acceptedAnswers": ["On", "on", "hidup"],
                    "placeholder": "Posisi Alternator..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Pendaratan",
                    "answer": "Land immediately",
                    "acceptedAnswers": ["Land immediately", "Mendarat seketika", "land immediately"],
                    "placeholder": "Tindakan pendaratan..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Throttle",
                    "answer": "Close",
                    "acceptedAnswers": ["Close", "closed", "tutup"],
                    "placeholder": "Posisi Throttle..."
                },
                {
                    "id": "sub_e",
                    "letter": "e",
                    "label": "Mixture",
                    "answer": "Idle cut off",
                    "acceptedAnswers": ["Idle cut off", "idle-cut-off", "cut off"],
                    "placeholder": "Posisi Mixture..."
                },
                {
                    "id": "sub_f",
                    "letter": "f",
                    "label": "Fuel Valve",
                    "answer": "Closed",
                    "acceptedAnswers": ["Closed", "close", "tutup"],
                    "placeholder": "Posisi Fuel Valve..."
                },
                {
                    "id": "sub_g",
                    "letter": "g",
                    "label": "Evakuasi",
                    "answer": "Exit A/C with fire extinguisher",
                    "acceptedAnswers": ["Exit A/C with fire extinguisher", "Exit A/C", "Keluar bawa APAR", "Exit aircraft"],
                    "placeholder": "Tindakan evakuasi..."
                }
            ]
        },
        # 17. Engine Failure Below 7 ft
        {
            "id": "S300C-EME-017",
            "aircraft": "SIKORSKY S300C",
            "section": "EMERGENCY",
            "category": "Engine Failure",
            "questionType": "fill-blank",
            "question": "17. Engine Fail Below 7ft: Indikasi & Prosedur",
            "answer": "a. Indikasi A/C sudden yawing left | b. Prosedur Maintain collective pitch, Apply right pedal, Apply collective as necessary",
            "acceptedAnswers": [
                "A/C sudden yawing left, Maintain collective, Apply right pedal, Apply collective as necessary"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 3,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Indikasi Pergerakan Pesawat",
                    "answer": "A/C sudden yawing left",
                    "acceptedAnswers": [
                        "A/C sudden yawing left",
                        "sudden yawing left",
                        "yawing left",
                        "pesawat yawing ke kiri",
                        "yawing to left"
                    ],
                    "placeholder": "Indikasi arah yawing..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Prosedur Kontrol (Collective & Pedal)",
                    "answer": "Maintain collective pitch, Apply right pedal, Apply collective as necessary",
                    "acceptedAnswers": [
                        "Maintain collective pitch, Apply right pedal, Apply collective as necessary",
                        "Maintain collective, Apply right pedal, Apply collective as necessary",
                        "Maintain collective pitch, right pedal, collective as necessary",
                        "maintain collective, right pedal"
                    ],
                    "placeholder": "Prosedur tindakan..."
                }
            ]
        },
        # 18. Engine Failure Below 450 ft
        {
            "id": "S300C-EME-018",
            "aircraft": "SIKORSKY S300C",
            "section": "EMERGENCY",
            "category": "Engine Failure",
            "questionType": "fill-blank",
            "question": "18. Engine Fail Below 450 ft: Prosedur Tindakan (Langkah a sampai e)",
            "answer": "a. Lower Collective pitch | b. Maintain RPM | c. Control cyclic and collective to maintain A/C settle | d. Set Attitude | e. Prepare ground contact",
            "acceptedAnswers": [
                "Lower Collective pitch, Maintain RPM, Control cyclic and collective, Set Attitude, Prepare ground contact"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 3,
            "points": 5,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Langkah 1 (Collective)",
                    "answer": "Lower Collective pitch",
                    "acceptedAnswers": ["Lower Collective pitch", "lower collective", "turunkan collective"],
                    "placeholder": "Tindakan collective pitch..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Langkah 2 (RPM)",
                    "answer": "Maintain RPM",
                    "acceptedAnswers": ["Maintain RPM", "maintain rotor rpm", "pertahankan rpm"],
                    "placeholder": "Tindakan rotor RPM..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Langkah 3 (Kontrol Sikap)",
                    "answer": "Control cyclic and collective to maintain A/C settle",
                    "acceptedAnswers": [
                        "Control cyclic and collective to maintain A/C settle",
                        "Control cyclic and collective",
                        "kendalikan cyclic dan collective"
                    ],
                    "placeholder": "Tindakan flight control..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Langkah 4 (Attitude)",
                    "answer": "Set Attitude",
                    "acceptedAnswers": ["Set Attitude", "atur attitude", "attitude"],
                    "placeholder": "Pengaturan attitude..."
                },
                {
                    "id": "sub_e",
                    "letter": "e",
                    "label": "Langkah 5 (Pendaratan)",
                    "answer": "Prepare ground contact",
                    "acceptedAnswers": ["Prepare ground contact", "persiapkan ground contact", "ground contact"],
                    "placeholder": "Persiapan kontak tanah..."
                }
            ]
        },
        # 19. Engine Failure Alt Above 450 ft
        {
            "id": "S300C-EME-019",
            "aircraft": "SIKORSKY S300C",
            "section": "EMERGENCY",
            "category": "Engine Failure",
            "questionType": "fill-blank",
            "question": "19. Engine Fail Alt Above 450 ft: Key Autorotation Steps (Langkah a sampai e)",
            "answer": "a. Steady glide 52 Kts | b. Backward cyclic at 50 ft | c. Coordinate cyclic & collective at 10 ft | d. Lower collective pitch | e. Land A/C",
            "acceptedAnswers": [
                "Steady glide 52 Kts, Backward cyclic at 50 ft, Coordinate cyclic and collective at 10 ft, Lower collective pitch, Land A/C"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 3,
            "points": 5,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Langkah 1 (Glide Speed)",
                    "answer": "Steady glide 52 Kts",
                    "acceptedAnswers": ["Steady glide 52 Kts", "glide 52 kts", "52 kts", "steady glide 52 knots", "52"],
                    "placeholder": "Kecepatan glide (52 Kts)..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Langkah 2 (Flare pada 50 ft)",
                    "answer": "Backward cyclic at 50 ft",
                    "acceptedAnswers": ["Backward cyclic at 50 ft", "backward cyclic 50 ft", "tarik cyclic 50 ft", "backward cyclic"],
                    "placeholder": "Tindakan cyclic pada 50 ft..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Langkah 3 (Leveling pada 10 ft)",
                    "answer": "Coordinate cyclic & collective at 10 ft",
                    "acceptedAnswers": [
                        "Coordinate cyclic & collective at 10 ft",
                        "Coordinate cyclic and collective at 10 ft",
                        "koordinasi cyclic dan collective 10 ft"
                    ],
                    "placeholder": "Koordinasi kontrol pada 10 ft..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Langkah 4 (Touchdown Cushion)",
                    "answer": "Lower collective pitch",
                    "acceptedAnswers": ["Lower collective pitch", "lower collective", "turunkan collective"],
                    "placeholder": "Tindakan collective..."
                },
                {
                    "id": "sub_e",
                    "letter": "e",
                    "label": "Langkah 5 (Pendaratan)",
                    "answer": "Land A/C",
                    "acceptedAnswers": ["Land A/C", "land aircraft", "mendarat", "land"],
                    "placeholder": "Penyelesaian pendaratan..."
                }
            ]
        },
        # 20. Tail Rotor Failure
        {
            "id": "S300C-EME-020",
            "aircraft": "SIKORSKY S300C",
            "section": "EMERGENCY",
            "category": "Tail Rotor Failure",
            "questionType": "fill-blank",
            "question": "20. Tail Rotor Failure (Complete Lost T/R Thrust): Indikasi & Prosedur",
            "answer": "a. Indikasi Yawing to right | b. Prosedur Forward Flight Lower Collective, Set airspeed 50-60 Kts, Move left cyclic, Control collective, Maintain heading, Autorotation",
            "acceptedAnswers": [
                "Indikasi Yawing to right, Lower Collective, Set airspeed 50-60 Kts, Move left cyclic, Autorotation"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 4,
            "points": 2,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Indikasi Pergerakan",
                    "answer": "Yawing to right",
                    "acceptedAnswers": [
                        "Yawing to right",
                        "yawing right",
                        "yawing ke kanan",
                        "putaran ke kanan",
                        "yawing to the right"
                    ],
                    "placeholder": "Indikasi arah yawing..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Prosedur Forward Flight",
                    "answer": "Lower Collective, Set airspeed 50-60 Kts, Move left cyclic, Control collective, Maintain heading, Autorotation",
                    "acceptedAnswers": [
                        "Lower Collective, Set airspeed 50-60 Kts, Move left cyclic, Control collective, Maintain heading, Autorotation",
                        "Lower Collective, Set airspeed 50-60 Kts, Move left cyclic, Autorotation",
                        "lower collective, 50-60 kts, left cyclic, autorotation"
                    ],
                    "placeholder": "Urutan prosedur tindakan..."
                }
            ]
        },
        # 21. Simulated Anti Torque Malfunction
        {
            "id": "S300C-EME-021",
            "aircraft": "SIKORSKY S300C",
            "section": "EMERGENCY",
            "category": "Simulated Anti Torque",
            "questionType": "fill-blank",
            "question": "21. Simulated Anti Torque Malfunction: Altitude, Airspeed, RPM, Approach",
            "answer": "a. Altitude 300 ft AGL | b. Airspeed 55 kts | c. RPM 3000 (left) / 3200 (right) | d. Approach 5 to 8 degrees",
            "acceptedAnswers": [
                "300 ft AGL, 55 kts, RPM 3000 / 3200, Approach 5 to 8 degrees",
                "300 ft, 55 kts, 3000/3200 RPM, 5-8 degrees"
            ],
            "unit": "",
            "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
            "sourcePage": 4,
            "points": 4,
            "verified": True,
            "subQuestions": [
                {
                    "id": "sub_a",
                    "letter": "a",
                    "label": "Altitude",
                    "answer": "300 ft AGL",
                    "acceptedAnswers": [
                        "300",
                        "300 ft",
                        "300 ft AGL",
                        "300ft",
                        "300 AGL"
                    ],
                    "unit": "ft AGL",
                    "placeholder": "Ketinggian (300 ft AGL)..."
                },
                {
                    "id": "sub_b",
                    "letter": "b",
                    "label": "Airspeed",
                    "answer": "55 kts",
                    "acceptedAnswers": [
                        "55",
                        "55 kts",
                        "55 knots",
                        "55 KIAS"
                    ],
                    "unit": "kts",
                    "placeholder": "Kecepatan terbang (55 kts)..."
                },
                {
                    "id": "sub_c",
                    "letter": "c",
                    "label": "Engine RPM (Kiri / Kanan)",
                    "answer": "3000 (left) / 3200 (right)",
                    "acceptedAnswers": [
                        "3000 / 3200",
                        "3000/3200",
                        "3000 (left) / 3200 (right)",
                        "3000 dan 3200",
                        "3000-3200",
                        "3000, 3200"
                    ],
                    "unit": "RPM",
                    "placeholder": "RPM (3000 / 3200)..."
                },
                {
                    "id": "sub_d",
                    "letter": "d",
                    "label": "Approach Angle",
                    "answer": "5 to 8 degrees",
                    "acceptedAnswers": [
                        "5 to 8 degrees",
                        "5-8",
                        "5 - 8",
                        "5-8 degrees",
                        "5 sampai 8 derajat",
                        "5 to 8 deg",
                        "5-8°"
                    ],
                    "unit": "degrees",
                    "placeholder": "Sudut approach (5 to 8 degrees)..."
                }
            ]
        }
    ]

    return {
        "aircraft": "SIKORSKY S-300C",
        "title": "BOLD FACE & LIMITATIONS SIKORSKY S-300C",
        "sourceDocument": "BOLD FACE SIKORSKY S300C.docx",
        "description": "Limitations, Engine Operating Limits, Rotor RPM, Manifold Press, dan Prosedur Emergency Helikopter Sikorsky S-300C",
        "totalQuestions": len(questions),
        "questions": questions
    }

def main():
    os.makedirs("data", exist_ok=True)
    dataset = build_s300c()
    out_file = "data/sikorsky-s300c.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    print(f"Generated {out_file} with {dataset['totalQuestions']} items.")

if __name__ == "__main__":
    main()
