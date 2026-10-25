# -*- coding: utf-8 -*-
"""
Builder for AH-64E Apache Rv. 3.0 Emergency Procedures Practice Test
Exact alignment with practice test pages 1-9:
- 26 Limitation questions with multi-part subQuestions (a, b, c...)
- 35 Emergency Procedures questions with multi-step subQuestions (a, b, c...)
- 15 Warning / Caution / Advisory questions with multi-step subQuestions
"""
import json

def build_ah64e_suite():
    questions = []

    # ==========================
    # 1. LIMITATIONS (Pages 1-3)
    # ==========================
    lim_defs = [
        (
            1, "NR LIMITS", "1. NR LIMITS (%)",
            "a. Maximum (> 110 red) 110 | b. Transient (yellow) 105 - 110 | c. High rotor warning annunciated 105 | d. Normal (green) 94 - 104 | e. Transient (red) 0 - 93",
            "%", 1,
            [
                {"id": "sub_a", "letter": "a", "label": "Maximum (> red)", "answer": "110 %", "acceptedAnswers": ["110", "110 %", "110%"], "unit": "%", "placeholder": "Max (> 110 red)..."},
                {"id": "sub_b", "letter": "b", "label": "Transient (yellow)", "answer": "105 - 110 %", "acceptedAnswers": ["105 - 110", "105-110", "105 to 110"], "unit": "%", "placeholder": "105 - 110..."},
                {"id": "sub_c", "letter": "c", "label": "High rotor warning annunciated", "answer": "105 %", "acceptedAnswers": ["105", "105 %", "105%"], "unit": "%", "placeholder": "105..."},
                {"id": "sub_d", "letter": "d", "label": "Normal (green)", "answer": "94 - 104 %", "acceptedAnswers": ["94 - 104", "94-104", "94 to 104"], "unit": "%", "placeholder": "94 - 104..."},
                {"id": "sub_e", "letter": "e", "label": "Transient (red)", "answer": "0 - 93 %", "acceptedAnswers": ["0 - 93", "0-93", "0 to 93"], "unit": "%", "placeholder": "0 - 93..."}
            ]
        ),
        (
            2, "ENGINE OIL PRESSURE", "2. ENGINE OIL 1 OR 2 PRESSURE (PSI)",
            "a. Maximum (> 120 red w Box) 120 | b. Normal (green) 23 - 120 | c. Minimum (< 23 red) 23",
            "PSI", 1,
            [
                {"id": "sub_a", "letter": "a", "label": "Maximum (> red w Box)", "answer": "120 PSI", "acceptedAnswers": ["120", "120 PSI", "120psi"], "unit": "PSI", "placeholder": "120..."},
                {"id": "sub_b", "letter": "b", "label": "Normal (green)", "answer": "23 - 120 PSI", "acceptedAnswers": ["23 - 120", "23-120", "23 to 120"], "unit": "PSI", "placeholder": "23 - 120..."},
                {"id": "sub_c", "letter": "c", "label": "Minimum (< red)", "answer": "23 PSI", "acceptedAnswers": ["23", "23 PSI", "23psi"], "unit": "PSI", "placeholder": "23..."}
            ]
        ),
        (
            3, "HYDRAULIC SYSTEMS", "3. HYDRAULIC SYSTEMS (PSI)",
            "a. Transient permitted 5 Sec/Min (> red w/box) > 3410 | b. Transient permitted 5 Sec/Min (> red w/box) 3310 - 3400 | c. Normal (green) 2700 - 3300 | d. Minimum (<= 1260 red w/box) 1260",
            "PSI", 1,
            [
                {"id": "sub_a", "letter": "a", "label": "Transient – permitted for 5 Sec/Min (> red w/box)", "answer": "> 3410 PSI", "acceptedAnswers": ["> 3410", ">3410", "3410", "> 3.410"], "unit": "PSI", "placeholder": "> 3410..."},
                {"id": "sub_b", "letter": "b", "label": "Transient – permitted for 5 Sec/Min (> red w/box)", "answer": "3310 - 3400 PSI", "acceptedAnswers": ["3310 - 3400", "3310-3400", "3310 to 3400"], "unit": "PSI", "placeholder": "3310 - 3400..."},
                {"id": "sub_c", "letter": "c", "label": "Normal (green)", "answer": "2700 - 3300 PSI", "acceptedAnswers": ["2700 - 3300", "2700-3300", "2700 to 3300"], "unit": "PSI", "placeholder": "2700 - 3300..."},
                {"id": "sub_d", "letter": "d", "label": "Minimum (<= 1260 red w/box)", "answer": "1260 PSI", "acceptedAnswers": ["1260", "1.260", "<= 1260", "<=1260"], "unit": "PSI", "placeholder": "1260..."}
            ]
        ),
        (
            4, "TGT LIMITS 701 D", "4. TGT LIMITS 701 D DIGITAL READOUTS (°C)",
            "a. Max (> 949 red) 949 | b. Transient 12 Sec/Min 904-949 | c. Contingency 2.5 Sec/Min 880-903 | d. Max rated power 10 Sec/Min 847-879 | e. Max during start 851 | f. Intermediate 30 Sec/Min 794-846 | g. Max continuous 793 | h. Normal 0-793",
            "°C", 1,
            [
                {"id": "sub_a", "letter": "a", "label": "Max (> red)", "answer": "949 °C", "acceptedAnswers": ["949", "949 °C", "949°C"], "unit": "°C", "placeholder": "949..."},
                {"id": "sub_b", "letter": "b", "label": "Transient 12 Sec/Min (yellow)", "answer": "904 - 949 °C", "acceptedAnswers": ["904 - 949", "904-949", "904 to 949"], "unit": "°C", "placeholder": "904 - 949..."},
                {"id": "sub_c", "letter": "c", "label": "Contingency 2.5 Sec/Min (yellow)", "answer": "880 - 903 °C", "acceptedAnswers": ["880 - 903", "880-903", "880 to 903"], "unit": "°C", "placeholder": "880 - 903..."},
                {"id": "sub_d", "letter": "d", "label": "Max rated power 10 Sec/Min (yellow)", "answer": "847 - 879 °C", "acceptedAnswers": ["847 - 879", "847-879", "847 to 879"], "unit": "°C", "placeholder": "847 - 879..."},
                {"id": "sub_e", "letter": "e", "label": "Max during start", "answer": "851 °C", "acceptedAnswers": ["851", "851 °C", "851°C"], "unit": "°C", "placeholder": "851..."},
                {"id": "sub_f", "letter": "f", "label": "Intermediate rated power 30 Sec/Min (yellow)", "answer": "794 - 846 °C", "acceptedAnswers": ["794 - 846", "794-846", "794 to 846"], "unit": "°C", "placeholder": "794 - 846..."},
                {"id": "sub_g", "letter": "g", "label": "Maximum continuous power", "answer": "793 °C", "acceptedAnswers": ["793", "793 °C", "793°C"], "unit": "°C", "placeholder": "793..."},
                {"id": "sub_h", "letter": "h", "label": "Normal operation (green)", "answer": "0 - 793 °C", "acceptedAnswers": ["0 - 793", "0-793", "0 to 793"], "unit": "°C", "placeholder": "0 - 793..."}
            ]
        ),
        (
            5, "APU OPERATION", "5. Avoid prolonged operation at ___ Nr with the APU running",
            "94% - 96%", "%", 2, None
        ),
        (
            6, "TORQUE LIMITS", "6. TORQUE LIMITS",
            "NR < 50%: Max 30, Normal 0-30 | NR 50%-90%: Max 70, Normal 0-70 | DUAL: Max 115, Trans 101-115, Norm 0-100 | SINGLE: Max 125, Trans 121-125, Cont 111-120, MCP 110, Norm 0-100",
            "%", 2,
            [
                {"id": "sub_a", "letter": "a", "label": "TORQUE NR LESS THAN 50%: Maximum (> red)", "answer": "30 %", "acceptedAnswers": ["30", "30 %", "30%"], "unit": "%", "placeholder": "30..."},
                {"id": "sub_b", "letter": "b", "label": "TORQUE NR LESS THAN 50%: Normal operation (green)", "answer": "0 - 30 %", "acceptedAnswers": ["0 - 30", "0-30", "0 to 30"], "unit": "%", "placeholder": "0 - 30..."},
                {"id": "sub_c", "letter": "c", "label": "TORQUE NR LESS THAN 50 % - 90 %: Maximum (> red)", "answer": "70 %", "acceptedAnswers": ["70", "70 %", "70%"], "unit": "%", "placeholder": "70..."},
                {"id": "sub_d", "letter": "d", "label": "TORQUE NR LESS THAN 50 % - 90 %: Normal operation (green)", "answer": "0 - 70 %", "acceptedAnswers": ["0 - 70", "0-70", "0 to 70"], "unit": "%", "placeholder": "0 - 70..."},
                {"id": "sub_e", "letter": "e", "label": "DUAL ENGINE TORQUE: Maximum (> red)", "answer": "115 %", "acceptedAnswers": ["115", "115 %", "115%"], "unit": "%", "placeholder": "115..."},
                {"id": "sub_f", "letter": "f", "label": "DUAL ENGINE TORQUE: Transient 6 Sec/Min (yellow)", "answer": "101 - 115 %", "acceptedAnswers": ["101 - 115", "101-115", "101 to 115"], "unit": "%", "placeholder": "101 - 115..."},
                {"id": "sub_g", "letter": "g", "label": "DUAL ENGINE TORQUE: Normal (green)", "answer": "0 - 100 %", "acceptedAnswers": ["0 - 100", "0-100", "0 to 100"], "unit": "%", "placeholder": "0 - 100..."},
                {"id": "sub_h", "letter": "h", "label": "SINGLE ENGINE TORQUE: Maximum (> red)", "answer": "125 %", "acceptedAnswers": ["125", "125 %", "125%"], "unit": "%", "placeholder": "125..."},
                {"id": "sub_i", "letter": "i", "label": "SINGLE ENGINE TORQUE: Transient 6 Sec/Min (yellow)", "answer": "121 - 125 %", "acceptedAnswers": ["121 - 125", "121-125", "121 to 125"], "unit": "%", "placeholder": "121 - 125..."},
                {"id": "sub_j", "letter": "j", "label": "SINGLE ENGINE TORQUE: Single engine contingency 2.5 Sec/Min (yellow)", "answer": "111 - 120 %", "acceptedAnswers": ["111 - 120", "111-120", "111 to 120"], "unit": "%", "placeholder": "111 - 120..."},
                {"id": "sub_k", "letter": "k", "label": "SINGLE ENGINE TORQUE: Single engine maximum continuous power (green)", "answer": "110 %", "acceptedAnswers": ["110", "110 %", "110%"], "unit": "%", "placeholder": "110..."},
                {"id": "sub_l", "letter": "l", "label": "SINGLE ENGINE TORQUE: Normal (green)", "answer": "0 - 100 %", "acceptedAnswers": ["0 - 100", "0-100", "0 to 100"], "unit": "%", "placeholder": "0 - 100..."}
            ]
        ),
        (
            7, "NG LIMITS", "7. NG LIMITS - ENG1 OR 2 NG (%) DIGITAL READOUTS",
            "a. Maximum (> 106.0 red) 106.0 | b. Transient 12 Sec/Min 105.1 - 106.0 | c. Normal (green) 63.1 - 105.0 | d. Minimum engine out warning (< 63.0 red w/ box) 63.0",
            "%", 2,
            [
                {"id": "sub_a", "letter": "a", "label": "Maximum (> red)", "answer": "106.0 %", "acceptedAnswers": ["106.0", "106", "106.0 %", "106,0"], "unit": "%", "placeholder": "106.0..."},
                {"id": "sub_b", "letter": "b", "label": "Transient 12 Sec/Min (yellow)", "answer": "105.1 - 106.0 %", "acceptedAnswers": ["105.1 - 106.0", "105.1-106.0", "105.1 to 106.0"], "unit": "%", "placeholder": "105.1 - 106.0..."},
                {"id": "sub_c", "letter": "c", "label": "Normal (green)", "answer": "63.1 - 105.0 %", "acceptedAnswers": ["63.1 - 105.0", "63.1-105.0", "63.1 to 105.0"], "unit": "%", "placeholder": "63.1 - 105.0..."},
                {"id": "sub_d", "letter": "d", "label": "Minimum engine out warning annunciated (< red w/ box)", "answer": "63.0 %", "acceptedAnswers": ["63.0", "63", "63.0 %", "63,0"], "unit": "%", "placeholder": "63.0..."}
            ]
        ),
        (
            8, "NP LIMITS", "8. NP LIMITS - ENG1 OR 2 NP (%) DIGITAL READOUTS",
            "a. Maximum (> 119 red) 119 | b. Engine overspeed annunciated 114 | c. Transient operation 12 Sec/Min (yellow w/box at 114) 104 - 119 | d. Normal (green) 0 - 103",
            "%", 2,
            [
                {"id": "sub_a", "letter": "a", "label": "Maximum (> red)", "answer": "119 %", "acceptedAnswers": ["119", "119 %", "119%"], "unit": "%", "placeholder": "119..."},
                {"id": "sub_b", "letter": "b", "label": "Engine overspeed annunciated", "answer": "114 %", "acceptedAnswers": ["114", "114 %", "114%"], "unit": "%", "placeholder": "114..."},
                {"id": "sub_c", "letter": "c", "label": "Transient operation 12 Sec/Min (yellow w/box at 114)", "answer": "104 - 119 %", "acceptedAnswers": ["104 - 119", "104-119", "104 to 119"], "unit": "%", "placeholder": "104 - 119..."},
                {"id": "sub_d", "letter": "d", "label": "Normal (green)", "answer": "0 - 103 %", "acceptedAnswers": ["0 - 103", "0-103", "0 to 103"], "unit": "%", "placeholder": "0 - 103..."}
            ]
        ),
        (
            9, "GROUND OPERATIONS", "9. Prolonged ground operations and XMSN TEMP limit",
            "a. Duration threshold 30 minutes | b. Temperature limit 140 °C",
            "", 2,
            [
                {"id": "sub_a", "letter": "a", "label": "Prolonged ground operations greater than", "answer": "30 minutes", "acceptedAnswers": ["30", "30 minutes", "30 min", "30 menit"], "unit": "minutes", "placeholder": "30 minutes..."},
                {"id": "sub_b", "letter": "b", "label": "If XMSN TEMP 1 & 2 exceed", "answer": "140 °C", "acceptedAnswers": ["140", "140 °C", "140°C", "140 C"], "unit": "°C", "placeholder": "140 °C..."}
            ]
        ),
        (
            10, "ENGINE STARTS", "10. Engine Starts At Ambient Temperatures of 61F (16C) and Below",
            "a. 2 consecutive start cycles, 3 min rest | b. 2 additional start cycles, 30 min rest",
            "", 3,
            [
                {"id": "sub_a", "letter": "a", "label": "Consecutive start cycles and rest period", "answer": "Two start cycles, followed by 3 min rest period", "acceptedAnswers": ["Two, 3 min", "2, 3 min", "2, 3", "Two, 3", "3 min", "3"], "unit": "", "placeholder": "2 siklus, 3 min..."},
                {"id": "sub_b", "letter": "b", "label": "Additional consecutive start cycles and rest period", "answer": "Two additional cycles, followed by 30 min rest period", "acceptedAnswers": ["Two, 30 min", "2, 30 min", "2, 30", "Two, 30", "30 min", "30"], "unit": "", "placeholder": "2 siklus, 30 min..."}
            ]
        ),
        (
            11, "ENGINE STARTS", "11. Fault or aborted start wait times",
            "a. After fault/abort wait 30 sec after APU stopped | b. After 2 consecutive starts wait 20 min before 3rd attempt",
            "", 3,
            [
                {"id": "sub_a", "letter": "a", "label": "Wait after APU has stopped before attempting another start", "answer": "30 sec", "acceptedAnswers": ["30 sec", "30", "30 s", "30 detik"], "unit": "sec", "placeholder": "30 sec..."},
                {"id": "sub_b", "letter": "b", "label": "After 2 consecutive starts wait before third start attempt", "answer": "20 min", "acceptedAnswers": ["20 min", "20", "20 menit", "20 Sec/Min"], "unit": "min", "placeholder": "20 min..."}
            ]
        ),
        (
            12, "SLOPE LANDING", "12. Landing on terrain limits (pitch & roll attitude change)",
            "a. Pitch greater than 7° nose up or 10° nose down | b. Roll attitude greater than 10°",
            "", 3,
            [
                {"id": "sub_a", "letter": "a", "label": "Pitch attitude change from hover greater than", "answer": "7° nose up or 10° nose down", "acceptedAnswers": ["7° nose up or 10° nose down", "7 nose up or 10 nose down", "7 / 10", "7° / 10°", "7 nose up, 10 nose down"], "unit": "", "placeholder": "7° up / 10° down..."},
                {"id": "sub_b", "letter": "b", "label": "Roll attitude greater than", "answer": "10°", "acceptedAnswers": ["10°", "10", "10 deg"], "unit": "°", "placeholder": "10°..."}
            ]
        ),
        (
            13, "MANEUVERS", "13. Intentional maneuvers beyond attitudes prohibited",
            "a. Pitch +/- 30° | b. Roll +/- 60°",
            "", 3,
            [
                {"id": "sub_a", "letter": "a", "label": "Pitch attitude beyond", "answer": "+/- 30°", "acceptedAnswers": ["+/- 30°", "+/- 30", "+- 30", "30°", "30"], "unit": "°", "placeholder": "+/- 30°..."},
                {"id": "sub_b", "letter": "b", "label": "Roll attitude beyond", "answer": "+/- 60°", "acceptedAnswers": ["+/- 60°", "+/- 60", "+- 60", "60°", "60"], "unit": "°", "placeholder": "+/- 60°..."}
            ]
        ),
        (14, "FLIGHT CONTROLS", "14. Avoid aggressive directional and lateral control inputs greater than", "1 inch / sec", ["1 inch / sec", "1 inch/sec", "1 in/sec", "1"], "inch / sec", 3, None),
        (15, "TURBULENCE", "15. Flight into Turbulence prohibited", "Known or forecast extreme, known severe", ["Known or forecast extreme, known severe", "extreme, severe", "extreme, known severe", "forecast extreme"], "", 3, None),
        (16, "WIND LIMITATION", "16. Maximum wind velocity for rotor start or stop to prevent droop stop damage", "45 KTAS", ["45", "45 KTAS", "45 ktas", "45 kts"], "KTAS", 3, None),
        (17, "FLIGHT CONTROLS", "17. Force trim will not be turned off except in a", "Failed or partial failed mode", ["Failed or partial failed mode", "Failed or partial failed", "failed or partial", "failed"], "", 3, None),
        (18, "TAIL ROTOR", "18. Avoid large pedal step inputs in arresting right hovering/yawing turns greater than", "60° / sec", ["60° / sec", "60 / sec", "60 deg/sec", "60"], "° / sec", 3, None),
        (19, "ENGINE STARTS", "19. Dual engine starts are prohibited due to insufficient", "IPAS air", ["IPAS air", "IPAS", "ipas air"], "", 3, None),
        (20, "SEARCHLIGHT", "20. Maximum airspeed for searchlight operation (extend/retract/rotate)", "90 knots", ["90", "90 knots", "90 kts", "90 KTAS"], "knots", 3, None),
        (
            21, "GROSS WEIGHT", "21. Aircraft maximum gross weight limits",
            "a. Standard maximum gross weight 20.260 lbs | b. Non-tactical ferry flights 23.000 lbs",
            "lbs", 3,
            [
                {"id": "sub_a", "letter": "a", "label": "Maximum gross weight", "answer": "20.260 lbs", "acceptedAnswers": ["20.260", "20260", "20,260", "20.260 lbs", "20260 lbs"], "unit": "lbs", "placeholder": "20.260 lbs..."},
                {"id": "sub_b", "letter": "b", "label": "Non-tactical ferry flights except may not exceed", "answer": "23.000 lbs", "acceptedAnswers": ["23.000", "23000", "23,000", "23.000 lbs", "23000 lbs"], "unit": "lbs", "placeholder": "23.000 lbs..."}
            ]
        ),
        (22, "AIRSPEED", "22. Airspeed limits for autorotation", "145 KTAS", ["145", "145 KTAS", "145 ktas", "145 kts"], "KTAS", 3, None),
        (23, "AIRSPEED", "23. Maximum rearward / sideward flight speed", "45 KTAS", ["45", "45 KTAS", "45 ktas", "45 kts"], "KTAS", 3, None),
        (24, "AIRSPEED", "24. Maximum airspeed for stores jettison", "130 KTAS", ["130", "130 KTAS", "130 ktas", "130 kts"], "KTAS", 3, None),
        (25, "AIRSPEED", "25. Maximum airspeed for external tanks jettison", "90 KTAS", ["90", "90 KTAS", "90 ktas", "90 kts"], "KTAS", 3, None),
        (
            26, "TGT LIMIT", "26. TGT limit for dual and single engine",
            "a. Dual engine 879° +/- 5°C | b. Single engine 903° +/- 5°C",
            "°C", 3,
            [
                {"id": "sub_a", "letter": "a", "label": "Dual engine", "answer": "879° +/- 5°C", "acceptedAnswers": ["879° +/- 5°C", "879 +- 5", "879", "879 +/- 5", "879°"], "unit": "°C", "placeholder": "879° +/- 5°C..."},
                {"id": "sub_b", "letter": "b", "label": "Single engine", "answer": "903° +/- 5°C", "acceptedAnswers": ["903° +/- 5°C", "903 +- 5", "903", "903 +/- 5", "903°"], "unit": "°C", "placeholder": "903° +/- 5°C..."}
            ]
        )
    ]

    for item in lim_defs:
        if len(item) == 7:
            idx, cat, q_title, ans, unit, page, subs = item
            acc = [ans]
        else:
            idx, cat, q_title, ans, acc, unit, page, subs = item
        q_obj = {
            "id": f"AH64-LIM-{idx:03d}",
            "aircraft": "AH-64E",
            "section": "LIMITATIONS",
            "category": cat,
            "questionType": "fill-blank",
            "question": f"{idx}. {q_title}" if not q_title.startswith(str(idx)) else q_title,
            "answer": ans,
            "acceptedAnswers": acc if acc else [ans],
            "unit": unit,
            "sourceDocument": "AH-64E Rv. 3.0 Emergency Procedures Practice Test.pdf",
            "sourcePage": page,
            "points": len(subs) if subs else 1,
            "verified": True
        }
        if subs:
            q_obj["subQuestions"] = subs
        questions.append(q_obj)

    # ==========================================
    # 2. EMERGENCY PROCEDURES (Pages 4-8)
    # ==========================================
    emer_defs = [
        (
            1, "Emergency Terminology", "1. Land Without Delay",
            "Landing in which the primary consideration is continued control of the A/C & survival of the occupants, it is mean to be more urgent than Land as soon as possible",
            4, None
        ),
        (
            2, "Emergency Terminology", "2. Land as Soon as Possible",
            "Landing at the nearest suitable landing area (e.g. open field) without delay. The primary consideration is to ensure the survival of occupants",
            4, None
        ),
        (
            3, "Emergency Terminology", "3. Land As Soon As Practicable",
            "Landing at a suitable landing area. The primary consideration is the urgency of the emergency",
            4, None
        ),
        (
            4, "Emergency Egress", "4. Emergency Egress",
            "a. Helmet Visor - Down | b. Area Around Helicopter - Clear of Personnel | c. Canopy Jettison Handle - Turn 90°, release, then push to jettison canopy",
            4,
            [
                {"id": "sub_a", "letter": "a", "label": "Helmet Visor", "answer": "Down", "acceptedAnswers": ["Down", "down"], "placeholder": "Tindakan..."},
                {"id": "sub_b", "letter": "b", "label": "Area Around Helicopter", "answer": "Clear of Personnel", "acceptedAnswers": ["Clear of Personnel", "Clear", "clear of personnel"], "placeholder": "Kondisi..."},
                {"id": "sub_c", "letter": "c", "label": "Canopy Jettison Handle", "answer": "Turn 90°, release, then push to jettison canopy", "acceptedAnswers": ["Turn 90°, release, then push to jettison canopy", "Turn 90, release, then push to jettison canopy", "Turn 90°, release, push to jettison"], "placeholder": "Tindakan..."}
            ]
        ),
        (
            5, "Abort Start", "5. ABORT START Procedures",
            "a. Power Levers - OFF | b. ENG Start Switch - IGN Oride for 30 sec & until TGT is below 540°c",
            4,
            [
                {"id": "sub_a", "letter": "a", "label": "Power Levers", "answer": "OFF", "acceptedAnswers": ["OFF", "off"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "ENG Start Switch", "answer": "IGN Oride for 30 sec & until TGT is below 540°c", "acceptedAnswers": ["IGN Oride for 30 sec & until TGT is below 540°c", "IGN Oride for 30 sec", "IGN Oride for 30 sec & until TGT is below 540C"], "placeholder": "Tindakan b..."}
            ]
        ),
        (
            6, "Dual Engine Failure", "6. Dual Engine Failure - Low Altitude / Low Airspeed and Cruise",
            "a. Autorotate | b. ENG CHOP Button - Reset only if ENG CHOP warning message is present | c. Reset may be accomplished by Either Crewmember",
            4,
            [
                {"id": "sub_a", "letter": "a", "label": "Primary action", "answer": "Autorotate", "acceptedAnswers": ["Autorotate", "autorotate"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "ENG CHOP Button", "answer": "Reset only if ENG CHOP warning message is present", "acceptedAnswers": ["Reset only if ENG CHOP warning message is present", "Reset if ENG CHOP warning message present", "Reset only if ENG CHOP warning message is present"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Reset responsibility", "answer": "Reset may be accomplished by Either Crewmember", "acceptedAnswers": ["Reset may be accomplished by Either Crewmember", "Either Crewmember", "Either crewmember"], "placeholder": "Tindakan c..."}
            ]
        ),
        (
            7, "Single Engine Failure", "7. Single Engine Failure - Low Altitude / Low Airspeed and Cruise",
            "a. Airspeed - Adjust as appropriate | b. Wing Stores Jettison - As appropriate | c. Land as soon as practicable",
            4,
            [
                {"id": "sub_a", "letter": "a", "label": "Airspeed", "answer": "Adjust as appropriate", "acceptedAnswers": ["Adjust as appropriate", "adjust as appropriate"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Wing Stores Jettison", "answer": "As appropriate", "acceptedAnswers": ["As appropriate", "as appropriate"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Landing", "answer": "Land as soon as practicable", "acceptedAnswers": ["Land as soon as practicable", "LAND AS SOON AS PRACTICABLE"], "placeholder": "Tindakan c..."}
            ]
        ),
        (
            8, "Overspeed", "8. Engine 1 or 2 Overspeed - NP Failed High",
            "a. Collective - Adjust to Maintain NR within Limits | b. If condition persists: Power Lever (affected engine) - retard to equalize torque | c. Land as soon as practicable",
            4,
            [
                {"id": "sub_a", "letter": "a", "label": "Collective", "answer": "Adjust to Maintain NR within Limits", "acceptedAnswers": ["Adjust to Maintain NR within Limits", "Adjust to maintain NR within limits", "Adjust to maintain NR"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "If condition persists: Power Lever (affected engine)", "answer": "Retard to equalize torque", "acceptedAnswers": ["Retard to equalize torque", "retard to equalize torque"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Landing", "answer": "Land as soon as practicable", "acceptedAnswers": ["Land as soon as practicable", "LAND AS SOON AS PRACTICABLE"], "placeholder": "Tindakan c..."}
            ]
        ),
        (
            9, "Low RPM Rotor", "9. Low RPM Rotor - NP Failed Low",
            "a. Collective - Adjust to maintain NR within limits | b. Power Lever (affected Engine) - LOCKOUT & then retard to equalize torque | c. If manual control is not possible: Power Lever (affected Engine) - IDLE | d. Land as soon as practicable",
            5,
            [
                {"id": "sub_a", "letter": "a", "label": "Collective", "answer": "Adjust to maintain NR within limits", "acceptedAnswers": ["Adjust to maintain NR within limits", "Adjust to maintain NR"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "If condition persists: Power Lever (affected Engine)", "answer": "LOCKOUT & then retard to equalize torque", "acceptedAnswers": ["LOCKOUT & then retard to equalize torque", "LOCKOUT and then retard to equalize torque", "LOCKOUT & retard to equalize torque"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "If manual control not possible: Power Lever (affected Engine)", "answer": "IDLE", "acceptedAnswers": ["IDLE", "idle"], "placeholder": "Tindakan c..."},
                {"id": "sub_d", "letter": "d", "label": "Landing", "answer": "Land as soon as practicable", "acceptedAnswers": ["Land as soon as practicable", "LAND AS SOON AS PRACTICABLE"], "placeholder": "Tindakan d..."}
            ]
        ),
        (
            10, "Compressor Stall", "10. Engine Compressor Stall",
            "a. Collective - Reduce | b. Power Lever (affected Engine) - Retard | c. If TGT decreases: Power Lever - FLY | d. If stall recurs: Power Lever - IDLE | e. Land as soon as practicable",
            5,
            [
                {"id": "sub_a", "letter": "a", "label": "Collective", "answer": "Reduce", "acceptedAnswers": ["Reduce", "reduce"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Power Lever (affected Engine)", "answer": "Retard", "acceptedAnswers": ["Retard", "retard"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "If TGT decreases and no further evidence of stall: Power Lever", "answer": "FLY", "acceptedAnswers": ["FLY", "fly"], "placeholder": "Tindakan c..."},
                {"id": "sub_d", "letter": "d", "label": "If stall condition recurs: Power Lever (affected Engine)", "answer": "IDLE", "acceptedAnswers": ["IDLE", "idle"], "placeholder": "Tindakan d..."},
                {"id": "sub_e", "letter": "e", "label": "Landing", "answer": "Land as soon as practicable", "acceptedAnswers": ["Land as soon as practicable", "LAND AS SOON AS PRACTICABLE"], "placeholder": "Tindakan e..."}
            ]
        ),
        (
            11, "Tail Rotor Thrust Loss", "11. Loss of Tail Rotor Thrust in cruise flight - Continued flight possible",
            "a. EMERG HYD Button - Press ON | b. Airspeed - 100 KTAS minimum (until 10 to 20 ft above Touchdown) | c. Wing Stores Jettison - As appropriate | d. Power Lever - Retard as necessary (5 to 10 ft above Touchdown)",
            5,
            [
                {"id": "sub_a", "letter": "a", "label": "EMERG HYD Button", "answer": "Press ON", "acceptedAnswers": ["Press ON", "press on", "ON"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Airspeed", "answer": "100 KTAS minimum (until 10 to 20 ft above Touchdown)", "acceptedAnswers": ["100 KTAS minimum (until 10 to 20 ft above Touchdown)", "100 KTAS minimum", "100 KTAS"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Wing Stores Jettison", "answer": "As appropriate", "acceptedAnswers": ["As appropriate", "as appropriate"], "placeholder": "Tindakan c..."},
                {"id": "sub_d", "letter": "d", "label": "Power Lever", "answer": "Retard as necessary (5 to 10 ft above Touchdown)", "acceptedAnswers": ["Retard as necessary (5 to 10 ft above Touchdown)", "Retard as necessary", "retard as necessary"], "placeholder": "Tindakan d..."}
            ]
        ),
        (
            12, "Tail Rotor Thrust Loss", "12. Loss of Tail Rotor Thrust in cruise flight - Continued flight not possible or Low airspeed / Hover",
            "a. EMERG HYD Button - Press ON | b. Collective Reduce (compromise between rate of turn & Rate of Descent) | c. Wing stores Jettison - As Appropriate | d. Minimize Rate of Descent (10 to 20 ft above Touchdown) | e. Power levers - OFF (5 to 10 ft above Touchdown)",
            5,
            [
                {"id": "sub_a", "letter": "a", "label": "EMERG HYD Button", "answer": "Press ON", "acceptedAnswers": ["Press ON", "press on", "ON"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Collective", "answer": "Reduce (compromise between rate of turn & Rate of Descent)", "acceptedAnswers": ["Reduce (compromise between rate of turn & Rate of Descent)", "Reduce", "reduce"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Wing stores Jettison", "answer": "As Appropriate", "acceptedAnswers": ["As Appropriate", "as appropriate"], "placeholder": "Tindakan c..."},
                {"id": "sub_d", "letter": "d", "label": "Rate of Descent", "answer": "Minimize Rate of Descent (10 to 20 ft above Touchdown)", "acceptedAnswers": ["Minimize Rate of Descent (10 to 20 ft above Touchdown)", "Minimize Rate of Descent", "minimize"], "placeholder": "Tindakan d..."},
                {"id": "sub_e", "letter": "e", "label": "Power levers", "answer": "OFF (5 to 10 ft above Touchdown)", "acceptedAnswers": ["OFF (5 to 10 ft above Touchdown)", "OFF", "off"], "placeholder": "Tindakan e..."}
            ]
        ),
        (
            13, "Clutch Failure", "13. Main Transmission Input Drive Clutch Failure - In Flight",
            "a. Power lever (affected Engine) - IDLE | b. If NP is below NR: EMER ENG SHUTDOWN (affected Engine) | c. Land as soon as practicable | d. If NP does not drop below NR: Land as soon as possible | e. EMERG ENG(S) SHUTDOWN (both Engines Simultaneously)",
            5,
            [
                {"id": "sub_a", "letter": "a", "label": "Power lever (affected Engine)", "answer": "IDLE", "acceptedAnswers": ["IDLE", "idle"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "If NP below NR: Emergency action", "answer": "EMER ENG SHUTDOWN (affected Engine)", "acceptedAnswers": ["EMER ENG SHUTDOWN (affected Engine)", "EMER ENG SHUTDOWN"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Landing (if NP below NR)", "answer": "Land as soon as practicable", "acceptedAnswers": ["Land as soon as practicable", "LAND AS SOON AS PRACTICABLE"], "placeholder": "Tindakan c..."},
                {"id": "sub_d", "letter": "d", "label": "Landing (if NP does not drop below NR)", "answer": "Land as soon as possible", "acceptedAnswers": ["Land as soon as possible", "LAND AS SOON AS POSSIBLE"], "placeholder": "Tindakan d..."},
                {"id": "sub_e", "letter": "e", "label": "Shutdown (if NP does not drop below NR)", "answer": "EMERG ENG(S) SHUTDOWN (both Engines Simultaneously)", "acceptedAnswers": ["EMERG ENG(S) SHUTDOWN (both Engines Simultaneously)", "EMERG ENG(S) SHUTDOWN", "Shutdown both engines"], "placeholder": "Tindakan e..."}
            ]
        ),
        (
            14, "Clutch Failure", "14. Main Transmission Input Drive Clutch Failure - On Ground",
            "a. Clutch failed to engage: EMER ENG SHUTDOWN (affected Engine only), Check NG < 10%, Normal Engine Shutdown perform | b. Clutch failed to disengage: EMERG ENG(S) SHUTDOWN (Both Engines Simultaneously)",
            6,
            [
                {"id": "sub_a", "letter": "a", "label": "Clutch failed to engage", "answer": "EMER ENG SHUTDOWN (affected Engine only), Check NG is less than 10%, Normal Engine Shutdown - perform", "acceptedAnswers": ["EMER ENG SHUTDOWN (affected Engine only), Check NG is less than 10%, Normal Engine Shutdown - perform", "EMER ENG SHUTDOWN (affected Engine only)", "Check NG is less than 10%"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Clutch failed to disengage", "answer": "EMERG ENG(S) SHUTDOWN (Both Engines Simultaneously)", "acceptedAnswers": ["EMERG ENG(S) SHUTDOWN (Both Engines Simultaneously)", "EMERG ENG(S) SHUTDOWN", "Both Engines Simultaneously"], "placeholder": "Tindakan b..."}
            ]
        ),
        (
            15, "Engine Fire In Flight", "15. Engine Fire in Flight",
            "a. EMERG ENG SHUTDOWN (affected Engine) - when condition permit | b. Illuminated ENG FIRE Button - Press & RDY Light Illuminates | c. FIRE DISCH Button (s) - Press | d. LAND AS SOON AS POSSIBLE",
            6,
            [
                {"id": "sub_a", "letter": "a", "label": "EMERG ENG SHUTDOWN (affected Engine)", "answer": "when condition permit", "acceptedAnswers": ["when condition permit", "when conditions permit", "When condition permit"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Illuminated ENG FIRE Button", "answer": "Press & RDY Light Illuminates", "acceptedAnswers": ["Press & RDY Light Illuminates", "Press", "press & RDY Light Illuminates"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "FIRE DISCH Button (s)", "answer": "Press", "acceptedAnswers": ["Press", "press"], "placeholder": "Tindakan c..."},
                {"id": "sub_d", "letter": "d", "label": "Landing", "answer": "LAND AS SOON AS POSSIBLE", "acceptedAnswers": ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], "placeholder": "Tindakan d..."}
            ]
        ),
        (
            16, "Engine Fire On Ground", "16. Engine Fire On Ground",
            "a. EMERG ENG(S) SHUTDOWN | b. Illuminated ENG FIRE Button - Press & RDY Light Illuminates | c. FIRE DISCH Button(s) - Press",
            6,
            [
                {"id": "sub_a", "letter": "a", "label": "Shutdown", "answer": "EMERG ENG(S) SHUTDOWN", "acceptedAnswers": ["EMERG ENG(S) SHUTDOWN", "EMERG ENG SHUTDOWN"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Illuminated ENG FIRE Button", "answer": "Press & RDY Light Illuminates", "acceptedAnswers": ["Press & RDY Light Illuminates", "Press"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "FIRE DISCH Button(s)", "answer": "Press", "acceptedAnswers": ["Press", "press"], "placeholder": "Tindakan c..."}
            ]
        ),
        (
            17, "APU Fire", "17. APU Compartment Fire On Ground",
            "a. APU - OFF | b. Illuminated APU FIRE Button - Press & RDY Light Illuminates | c. FIRE DISCH Button(s) - press",
            6,
            [
                {"id": "sub_a", "letter": "a", "label": "APU", "answer": "OFF", "acceptedAnswers": ["OFF", "off"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Illuminated APU FIRE Button", "answer": "Press & RDY Light Illuminates", "acceptedAnswers": ["Press & RDY Light Illuminates", "Press"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "FIRE DISCH Button(s)", "answer": "press", "acceptedAnswers": ["press", "Press"], "placeholder": "Tindakan c..."}
            ]
        ),
        (
            18, "APU Fire", "18. APU Compartment Fire In Flight",
            "a. Illuminated APU FIRE Button - Press & RDY Light Illuminates | b. FIRE DISCH Button(s) - Press | c. LAND AS SOON AS POSSIBLE",
            6,
            [
                {"id": "sub_a", "letter": "a", "label": "Illuminated APU FIRE Button", "answer": "Press & RDY Light Illuminates", "acceptedAnswers": ["Press & RDY Light Illuminates", "Press"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "FIRE DISCH Button(s)", "answer": "Press", "acceptedAnswers": ["Press", "press"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Landing", "answer": "LAND AS SOON AS POSSIBLE", "acceptedAnswers": ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], "placeholder": "Tindakan c..."}
            ]
        ),
        (19, "Deck Fire", "19. Deck Fire", "LAND AS SOON AS POSSIBLE", 6, None),
        (
            20, "Fuselage Fire", "20. Fuselage Fire On Ground",
            "a. EMERG ENG(S) SHUTDOWN | b. APU - OFF (if applicable)",
            6,
            [
                {"id": "sub_a", "letter": "a", "label": "Shutdown", "answer": "EMERG ENG(S) SHUTDOWN", "acceptedAnswers": ["EMERG ENG(S) SHUTDOWN", "EMERG ENG SHUTDOWN"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "APU", "answer": "OFF (if applicable)", "acceptedAnswers": ["OFF (if applicable)", "OFF", "off"], "placeholder": "Tindakan b..."}
            ]
        ),
        (
            21, "Electrical Fire", "21. Electrical Fire In Flight",
            "a. GEN 1 & GEN 2 - OFF | b. LAND AS SOON AS POSSIBLE",
            6,
            [
                {"id": "sub_a", "letter": "a", "label": "Generators", "answer": "GEN 1 & GEN 2 - OFF", "acceptedAnswers": ["GEN 1 & GEN 2 - OFF", "GEN 1 & 2 - OFF", "OFF"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Landing", "answer": "LAND AS SOON AS POSSIBLE", "acceptedAnswers": ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], "placeholder": "Tindakan b..."}
            ]
        ),
        (
            22, "Smoke and Fume", "22. Smoke and Fume Elimination",
            "a. Airspeed - Slow to 20 KTAS Maximum | b. Canopy door (affected crew station) - Open to intermediate position | c. LAND AS SOON AS POSSIBLE",
            6,
            [
                {"id": "sub_a", "letter": "a", "label": "Airspeed", "answer": "Slow to 20 KTAS Maximum", "acceptedAnswers": ["Slow to 20 KTAS Maximum", "20 KTAS Maximum", "20 KTAS", "Slow to 20 KTAS"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Canopy door (affected crew station)", "answer": "Open to intermediate position", "acceptedAnswers": ["Open to intermediate position", "Open to intermediate position"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Landing", "answer": "LAND AS SOON AS POSSIBLE", "acceptedAnswers": ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], "placeholder": "Tindakan c..."}
            ]
        ),
        (
            23, "Hydraulic Emergency", "23. Primary Hydraulic Pressure Low and Utility Hydraulic Pressure Low",
            "a. EMERG HYD Button - Press ON | b. LAND WITHOUT DELAY | c. EMERG ENG(S) SHUTDOWN",
            7,
            [
                {"id": "sub_a", "letter": "a", "label": "EMERG HYD Button", "answer": "Press ON", "acceptedAnswers": ["Press ON", "press on", "ON"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Landing", "answer": "LAND WITHOUT DELAY", "acceptedAnswers": ["LAND WITHOUT DELAY", "Land without delay"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Shutdown", "answer": "EMERG ENG(S) SHUTDOWN", "acceptedAnswers": ["EMERG ENG(S) SHUTDOWN", "EMERG ENG SHUTDOWN"], "placeholder": "Tindakan c..."}
            ]
        ),
        (24, "Hydraulic Emergency", "24. Primary Hydraulic Pressure Low and Utility Hydraulic Level Low", "LAND AS SOON AS POSSIBLE", 7, None),
        (25, "Emergency Landing", "25. EMERGENCY LANDING IN WOODED AREAS (POWER OFF)", "AUTOROTATE - Apply full collective to Decay Rotor RPM as Helicopter Settles", 7, None),
        (
            26, "Ditching", "26. DITCHING (POWER OFF)",
            "a. AUTOROTATE - Apply full collective to decay rotor RPM as Helicopter Settles | b. Canopies - Jettison prior to entering water | c. Cyclic - position on direction of roll | d. Exit when main rotor has stopped",
            7,
            [
                {"id": "sub_a", "letter": "a", "label": "Autorotate", "answer": "Apply full collective to decay rotor RPM as Helicopter Settles", "acceptedAnswers": ["Apply full collective to decay rotor RPM as Helicopter Settles", "Apply full collective"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Canopies", "answer": "Jettison prior to entering water", "acceptedAnswers": ["Jettison prior to entering water", "Jettison"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Cyclic", "answer": "position on direction of roll", "acceptedAnswers": ["position on direction of roll", "direction of roll"], "placeholder": "Tindakan c..."},
                {"id": "sub_d", "letter": "d", "label": "Exit", "answer": "Exit when main rotor has stopped", "acceptedAnswers": ["Exit when main rotor has stopped", "when main rotor has stopped"], "placeholder": "Tindakan d..."}
            ]
        ),
        (
            27, "Ditching", "27. DITCHING (POWER ON)",
            "a. Approach to Hover | b. Canopies - Jettison prior to entering water | c. Pilot Shoulder Harness - Lock | d. CPG - Exit Helicopter | e. Hover downwind to a safe distance | f. Power Levers - OFF | g. Perform Hovering Autorotation - apply full collective | h. Cyclic - position on direction of roll | i. Exit when main rotor has stopped",
            7,
            [
                {"id": "sub_a", "letter": "a", "label": "Approach", "answer": "Approach to Hover", "acceptedAnswers": ["Approach to Hover", "Hover"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Canopies", "answer": "Jettison prior to entering water", "acceptedAnswers": ["Jettison prior to entering water", "Jettison"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Pilot Shoulder Harness", "answer": "Lock", "acceptedAnswers": ["Lock", "lock"], "placeholder": "Tindakan c..."},
                {"id": "sub_d", "letter": "d", "label": "CPG", "answer": "Exit Helicopter", "acceptedAnswers": ["Exit Helicopter", "Exit"], "placeholder": "Tindakan d..."},
                {"id": "sub_e", "letter": "e", "label": "Hover positioning", "answer": "Hover downwind to a safe distance", "acceptedAnswers": ["Hover downwind to a safe distance", "safe distance"], "placeholder": "Tindakan e..."},
                {"id": "sub_f", "letter": "f", "label": "Power Levers", "answer": "OFF", "acceptedAnswers": ["OFF", "off"], "placeholder": "Tindakan f..."},
                {"id": "sub_g", "letter": "g", "label": "Hovering Autorotation", "answer": "Perform Hovering Autorotation - apply full collective to decay rotor RPM as Helicopter Settles", "acceptedAnswers": ["Perform Hovering Autorotation - apply full collective to decay rotor RPM as Helicopter Settles", "Perform Hovering Autorotation", "apply full collective"], "placeholder": "Tindakan g..."},
                {"id": "sub_h", "letter": "h", "label": "Cyclic", "answer": "position on direction of roll", "acceptedAnswers": ["position on direction of roll"], "placeholder": "Tindakan h..."},
                {"id": "sub_i", "letter": "i", "label": "Exit", "answer": "Exit when main rotor has stopped", "acceptedAnswers": ["Exit when main rotor has stopped"], "placeholder": "Tindakan i..."}
            ]
        ),
        (
            28, "Flight Controls", "28. BUCS Fail / BUCS ON",
            "a. LAND AS SOON AS POSSIBLE | b. APU - ON | c. EMERG ENG(S) SHUTDOWN",
            7,
            [
                {"id": "sub_a", "letter": "a", "label": "Landing", "answer": "LAND AS SOON AS POSSIBLE", "acceptedAnswers": ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "APU", "answer": "ON", "acceptedAnswers": ["ON", "on"], "placeholder": "Tindakan b..."},
                {"id": "sub_c", "letter": "c", "label": "Shutdown", "answer": "EMERG ENG(S) SHUTDOWN", "acceptedAnswers": ["EMERG ENG(S) SHUTDOWN", "EMERG ENG SHUTDOWN"], "placeholder": "Tindakan c..."}
            ]
        ),
        (
            29, "Electrical Emergency", "29. Both GEN 1 FAIL and GEN 2 FAIL",
            "a. GEN 1 & GEN 2 - OFF/RESET, then ON (pilot GEN OFF/RST panel) | b. If condition persists: LAND AS SOON AS POSSIBLE",
            7,
            [
                {"id": "sub_a", "letter": "a", "label": "GEN 1 & GEN 2 switch", "answer": "OFF/RESET, then ON (pilot GEN OFF/RST panel)", "acceptedAnswers": ["OFF/RESET, then ON (pilot GEN OFF/RST panel)", "OFF/RESET, then ON", "OFF/RESET then ON"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "If condition persists: Landing", "answer": "LAND AS SOON AS POSSIBLE", "acceptedAnswers": ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], "placeholder": "Tindakan b..."}
            ]
        ),
        (
            30, "Electrical Emergency", "30. Single Generator and Single RTRU Failure",
            "a. Affected GEN 1 or GEN 2 - OFF/RESET, then ON (pilot GEN OFF/RST panel) | b. If condition persists: LAND AS SOON AS POSSIBLE",
            7,
            [
                {"id": "sub_a", "letter": "a", "label": "Affected GEN 1 or GEN 2 switch", "answer": "OFF/RESET, then ON (pilot GEN OFF/RST panel)", "acceptedAnswers": ["OFF/RESET, then ON (pilot GEN OFF/RST panel)", "OFF/RESET, then ON", "OFF/RESET then ON"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "If condition persists: Landing", "answer": "LAND AS SOON AS POSSIBLE", "acceptedAnswers": ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], "placeholder": "Tindakan b..."}
            ]
        ),
        (
            31, "Rotor Emergency", "31. Main Rotor Components",
            "a. LAND AS SOON AS POSSIBLE | b. EMERG ENG(S) SHUTDOWN",
            7,
            [
                {"id": "sub_a", "letter": "a", "label": "Landing", "answer": "LAND AS SOON AS POSSIBLE", "acceptedAnswers": ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Shutdown", "answer": "EMERG ENG(S) SHUTDOWN", "acceptedAnswers": ["EMERG ENG(S) SHUTDOWN", "EMERG ENG SHUTDOWN"], "placeholder": "Tindakan b..."}
            ]
        ),
        (
            32, "Stores Jettison", "32. WING STORES JETTISON",
            "a. All Armament: 130 KTAS Max, Collective JETT Button press | b. Selected Armament: 130 KTAS Max, STORES JETTISON press ARM, JETT Button press | c. External Fuel: 90 KTAS Max, STORES JETTISON press ARM, JETT Button press",
            8,
            [
                {"id": "sub_a", "letter": "a", "label": "All Armament Wing Stores", "answer": "Airspeed - 130 KTAS Maximum, Collective JETT Button - press", "acceptedAnswers": ["Airspeed - 130 KTAS Maximum, Collective JETT Button - press", "130 KTAS Maximum, Collective JETT Button - press", "130 KTAS, Collective JETT Button"], "placeholder": "Prosedur a..."},
                {"id": "sub_b", "letter": "b", "label": "Selected Armament Wing Stores", "answer": "Airspeed - 130 KTAS Maximum, Selected STORES JETTISON Buttons - press to ARM, JETT Button - press", "acceptedAnswers": ["Airspeed - 130 KTAS Maximum, Selected STORES JETTISON Buttons - press to ARM, JETT Button - press", "130 KTAS Maximum, Selected STORES JETTISON Buttons - press to ARM", "130 KTAS, Selected STORES JETTISON, JETT Button"], "placeholder": "Prosedur b..."},
                {"id": "sub_c", "letter": "c", "label": "External Fuel Wing Stores", "answer": "Airspeed - 90 KTAS Maximum, Selected STORES JETTISON Buttons - Press to ARM, JETT Button - press", "acceptedAnswers": ["Airspeed - 90 KTAS Maximum, Selected STORES JETTISON Buttons - Press to ARM, JETT Button - press", "90 KTAS Maximum, Selected STORES JETTISON Buttons - Press to ARM", "90 KTAS, Selected STORES JETTISON, JETT Button"], "placeholder": "Prosedur c..."}
            ]
        ),
        (33, "Avionics Failure", "33. PNVS Failure", "NVS Select Switch (pilot) - TADS", 8, None),
        (
            34, "Avionics Failure", "34. Single MP Operation",
            "a. NVS Select Switch - Reselect (PNVS or TADS) | b. Or: Crewmember (not on controls) - Assume Control",
            8,
            [
                {"id": "sub_a", "letter": "a", "label": "NVS Select Switch", "answer": "Reselect (PNVS or TADS)", "acceptedAnswers": ["Reselect (PNVS or TADS)", "Reselect (PNVS or TADS)", "Reselect"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Crewmember (not on controls)", "answer": "Assume Control", "acceptedAnswers": ["Assume Control", "assume control"], "placeholder": "Tindakan b..."}
            ]
        ),
        (35, "Avionics Failure", "35. Dual MP Failure", "LAND AS SOON AS POSSIBLE", 8, None)
    ]

    for idx, cat, q_title, ans, page, subs in emer_defs:
        q_obj = {
            "id": f"AH64-EMER-{idx:03d}",
            "aircraft": "AH-64E",
            "section": "EMERGENCY PROCEDURES",
            "category": cat,
            "questionType": "fill-blank",
            "question": q_title,
            "answer": ans,
            "acceptedAnswers": [ans],
            "unit": "",
            "sourceDocument": "AH-64E Rv. 3.0 Emergency Procedures Practice Test.pdf",
            "sourcePage": page,
            "points": len(subs) if subs else 1,
            "verified": True
        }
        if subs:
            q_obj["subQuestions"] = subs
        questions.append(q_obj)

    # ==========================================
    # 3. WARNING / CAUTION / ADVISORIES (Pages 8-9)
    # ==========================================
    wca_defs = [
        (1, "WARNING/CAUTION/ADVISORIES", "1. AFT FUEL LOW", "LAND AS SOON AS POSSIBLE", ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], 8, None),
        (
            2, "WARNING/CAUTION/ADVISORIES", "2. ENGINE 1 CHIPS",
            "a. POWER LEVER - IDLE | b. LAND AS SOON AS PRACTICABLE",
            ["POWER LEVER - IDLE, LAND AS SOON AS PRACTICABLE"], 8,
            [
                {"id": "sub_a", "letter": "a", "label": "POWER LEVER", "answer": "IDLE", "acceptedAnswers": ["IDLE", "idle"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Landing", "answer": "LAND AS SOON AS PRACTICABLE", "acceptedAnswers": ["LAND AS SOON AS PRACTICABLE", "Land as soon as practicable"], "placeholder": "Tindakan b..."}
            ]
        ),
        (
            3, "WARNING/CAUTION/ADVISORIES", "3. ENG 1 FUEL BYPASS",
            "a. POWER LEVER - IDLE | b. LAND AS SOON AS PRACTICABLE",
            ["POWER LEVER - IDLE, LAND AS SOON AS PRACTICABLE"], 8,
            [
                {"id": "sub_a", "letter": "a", "label": "POWER LEVER", "answer": "IDLE", "acceptedAnswers": ["IDLE", "idle"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Landing", "answer": "LAND AS SOON AS PRACTICABLE", "acceptedAnswers": ["LAND AS SOON AS PRACTICABLE", "Land as soon as practicable"], "placeholder": "Tindakan b..."}
            ]
        ),
        (
            4, "WARNING/CAUTION/ADVISORIES", "4. ENG 1 FUEL PSI LOW",
            "a. Achieve Safe Single Engine Airspeed | b. LAND AS SOON AS PRACTICABLE",
            ["Achieve Safe Single Engine Airspeed, LAND AS SOON AS PRACTICABLE"], 8,
            [
                {"id": "sub_a", "letter": "a", "label": "Airspeed", "answer": "Achieve safe Single Engine Airspeed", "acceptedAnswers": ["Achieve safe Single Engine Airspeed", "Safe Single Engine Airspeed", "Achieve safe single engine airspeed"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Landing", "answer": "LAND AS SOON AS PRACTICABLE", "acceptedAnswers": ["LAND AS SOON AS PRACTICABLE", "Land as soon as practicable"], "placeholder": "Tindakan b..."}
            ]
        ),
        (
            5, "WARNING/CAUTION/ADVISORIES", "5. Both ENG 1 FUEL PSI LOW and ENG 2 FUEL PSI LOW",
            "a. FUEL page, BOOST Button - press ON | b. LAND AS SOON AS POSSIBLE",
            ["FUEL page, BOOST Button - press ON, LAND AS SOON AS POSSIBLE"], 8,
            [
                {"id": "sub_a", "letter": "a", "label": "FUEL page, BOOST Button", "answer": "press ON", "acceptedAnswers": ["press ON", "Press ON", "ON", "press on"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Landing", "answer": "LAND AS SOON AS POSSIBLE", "acceptedAnswers": ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], "placeholder": "Tindakan b..."}
            ]
        ),
        (
            6, "WARNING/CAUTION/ADVISORIES", "6. ENG 1 OIL BYPASS",
            "a. POWER LEVER - IDLE | b. LAND AS SOON AS PRACTICABLE",
            ["POWER LEVER - IDLE, LAND AS SOON AS PRACTICABLE"], 9,
            [
                {"id": "sub_a", "letter": "a", "label": "POWER LEVER", "answer": "IDLE", "acceptedAnswers": ["IDLE", "idle"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Landing", "answer": "LAND AS SOON AS PRACTICABLE", "acceptedAnswers": ["LAND AS SOON AS PRACTICABLE", "Land as soon as practicable"], "placeholder": "Tindakan b..."}
            ]
        ),
        (
            7, "WARNING/CAUTION/ADVISORIES", "7. ENG 1 OIL PSI LOW",
            "a. EMERG ENG SHUTDOWN | b. LAND AS SOON AS PRACTICABLE",
            ["EMERG ENG SHUTDOWN, LAND AS SOON AS PRACTICABLE"], 9,
            [
                {"id": "sub_a", "letter": "a", "label": "Shutdown", "answer": "EMERG ENG SHUTDOWN", "acceptedAnswers": ["EMERG ENG SHUTDOWN", "Emerg Eng Shutdown"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Landing", "answer": "LAND AS SOON AS PRACTICABLE", "acceptedAnswers": ["LAND AS SOON AS PRACTICABLE", "Land as soon as practicable"], "placeholder": "Tindakan b..."}
            ]
        ),
        (8, "WARNING/CAUTION/ADVISORIES", "8. FORWARD FUEL LOW", "LAND AS SOON AS PRACTICABLE", ["LAND AS SOON AS PRACTICABLE", "Land as soon as practicable"], 9, None),
        (9, "WARNING/CAUTION/ADVISORIES", "9. GEARBOX TEMP HIGH", "LAND AS SOON AS PRACTICABLE", ["LAND AS SOON AS PRACTICABLE", "Land as soon as practicable"], 9, None),
        (10, "WARNING/CAUTION/ADVISORIES", "10. GRBX VIBRATION", "LAND AS SOON AS POSSIBLE", ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], 9, None),
        (11, "WARNING/CAUTION/ADVISORIES", "11. MAIN XMSN CHIPS", "LAND AS SOON AS POSSIBLE", ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], 9, None),
        (12, "WARNING/CAUTION/ADVISORIES", "12. PRI HYD BYP", "LAND AS SOON AS PRACTICABLE", ["LAND AS SOON AS PRACTICABLE", "Land as soon as practicable"], 9, None),
        (13, "WARNING/CAUTION/ADVISORIES", "13. PRI HYD LEVEL LOW", "LAND AS SOON AS PRACTICABLE", ["LAND AS SOON AS PRACTICABLE", "Land as soon as practicable"], 9, None),
        (14, "WARNING/CAUTION/ADVISORIES", "14. PRI HYD PSI LOW", "LAND AS SOON AS POSSIBLE", ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], 9, None),
        (
            15, "WARNING/CAUTION/ADVISORIES", "15. ROTOR BRAKE ON/LK",
            "a. RTR BRK Switch - OFF | b. LAND AS SOON AS POSSIBLE",
            ["RTR BRK Switch - OFF, LAND AS SOON AS POSSIBLE"], 9,
            [
                {"id": "sub_a", "letter": "a", "label": "RTR BRK Switch", "answer": "OFF", "acceptedAnswers": ["OFF", "off"], "placeholder": "Tindakan a..."},
                {"id": "sub_b", "letter": "b", "label": "Landing", "answer": "LAND AS SOON AS POSSIBLE", "acceptedAnswers": ["LAND AS SOON AS POSSIBLE", "Land as soon as possible"], "placeholder": "Tindakan b..."}
            ]
        )
    ]

    for idx, cat, q_title, ans, acc, page, subs in wca_defs:
        q_obj = {
            "id": f"AH64-WCA-{idx:03d}",
            "aircraft": "AH-64E",
            "section": "WARNING/CAUTION/ADVISORIES",
            "category": cat,
            "questionType": "fill-blank",
            "question": q_title,
            "answer": ans,
            "acceptedAnswers": acc if acc else [ans],
            "unit": "",
            "sourceDocument": "AH-64E Rv. 3.0 Emergency Procedures Practice Test.pdf",
            "sourcePage": page,
            "points": len(subs) if subs else 1,
            "verified": True
        }
        if subs:
            q_obj["subQuestions"] = subs
        questions.append(q_obj)

    return {
        "aircraft": "AH-64E",
        "title": "AH-64E RV. 3.0 EMERGENCY PROCEDURES & LIMITATIONS PRACTICE TEST",
        "sourceDocument": "AH-64E Rv. 3.0 Emergency Procedures Practice Test.pdf",
        "description": "Tes Boldface & Limitations AH-64E Apache lengkap: Limitations 1-26, Emergency Procedures 1-35, Warning/Caution/Advisories 1-15",
        "totalQuestions": len(questions),
        "questions": questions
    }

if __name__ == "__main__":
    suite = build_ah64e_suite()
    with open("data/ah-64e.json", "w", encoding="utf-8") as f:
        json.dump(suite, f, indent=2, ensure_ascii=False)
    print(f"Generated data/ah-64e.json with {suite['totalQuestions']} items.")
