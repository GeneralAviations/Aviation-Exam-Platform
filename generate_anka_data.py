# -*- coding: utf-8 -*-
"""
Generator for ANKA MALE UAV Question Bank
Extracts and builds all 132 questions across 6 sections with full variant expansion.
"""
import json
import re

def clean_text(s):
    if not s:
        return ''
    return ' '.join(str(s).split()).strip()

def expand_variants(answer, accepted_list, unit=''):
    variants = set()
    base_items = [answer] + (accepted_list or [])
    
    for item in base_items:
        if not item:
            continue
        cleaned = clean_text(item)
        variants.add(cleaned)
        
        # 'sampai' <-> '-'
        if 'sampai' in cleaned.lower():
            variants.add(re.sub(r'\bsampai\b', '-', cleaned, flags=re.IGNORECASE))
            variants.add(re.sub(r'\bsampai\b', ' - ', cleaned, flags=re.IGNORECASE))
            variants.add(re.sub(r'\bsampai\b', 'to', cleaned, flags=re.IGNORECASE))
            variants.add(re.sub(r'\bsampai\b', 's/d', cleaned, flags=re.IGNORECASE))
            variants.add(re.sub(r'\bsampai\b', 's.d.', cleaned, flags=re.IGNORECASE))
        if '-' in cleaned:
            variants.add(re.sub(r'(\w+)\s*[-–—]\s*(\w+)', r'\1 sampai \2', cleaned))
            variants.add(re.sub(r'(\w+)\s*[-–—]\s*(\w+)', r'\1 - \2', cleaned))
            variants.add(re.sub(r'(\w+)\s*[-–—]\s*(\w+)', r'\1 to \2', cleaned))
            variants.add(re.sub(r'(\w+)\s*[-–—]\s*(\w+)', r'\1 s/d \2', cleaned))

        # 'dan' <-> '&' <-> 'and'
        if re.search(r'\bdan\b', cleaned, re.IGNORECASE):
            variants.add(re.sub(r'\bdan\b', '&', cleaned, flags=re.IGNORECASE))
            variants.add(re.sub(r'\bdan\b', ' & ', cleaned, flags=re.IGNORECASE))
            variants.add(re.sub(r'\bdan\b', 'and', cleaned, flags=re.IGNORECASE))
        if '&' in cleaned:
            variants.add(re.sub(r'\s*&\s*', ' dan ', cleaned))
            variants.add(re.sub(r'\s*&\s*', ' and ', cleaned))
            variants.add(re.sub(r'\s*&\s*', ' & ', cleaned))
        if re.search(r'\band\b', cleaned, re.IGNORECASE):
            variants.add(re.sub(r'\band\b', 'dan', cleaned, flags=re.IGNORECASE))
            variants.add(re.sub(r'\band\b', '&', cleaned, flags=re.IGNORECASE))

        # Unit stripping / appending
        if unit:
            u_clean = clean_text(unit)
            u_pat = re.escape(u_clean)
            if re.search(rf'\b{u_pat}\b', cleaned, re.IGNORECASE):
                no_unit = clean_text(re.sub(rf'\b{u_pat}\b', '', cleaned, flags=re.IGNORECASE))
                if no_unit:
                    variants.add(no_unit)
            else:
                variants.add(f"{cleaned} {u_clean}")

        # Degree variations
        if '°' in cleaned:
            variants.add(cleaned.replace('°', ' deg'))
            variants.add(cleaned.replace('°', ''))
            variants.add(cleaned.replace('°', ' derajat'))

    # Final list
    final_list = []
    for v in variants:
        c = clean_text(v)
        if c and c not in final_list:
            final_list.append(c)
    return final_list

def create_q(qid, section, category, question, answer, raw_accepted, unit='', page=1):
    all_acc = expand_variants(answer, raw_accepted, unit)
    return {
        "id": qid,
        "aircraft": "ANKA MALE UAV",
        "section": section,
        "category": category,
        "questionType": "fill-blank",
        "question": question,
        "answer": answer,
        "acceptedAnswers": all_acc,
        "unit": unit,
        "sourceDocument": "ANKAID-T0544-AFM-2",
        "sourcePage": page,
        "points": 1,
        "verified": True
    }

def build_anka_dataset():
    q = []
    sec1 = "BOLD FACE LIMITATIONS"
    
    # Airspeed Limitations
    cat = "Airspeed Limitations"
    q.append(create_q("ANKA-LIM-001", sec1, cat, "VNE (Never Exceed)", "108 KIAS", ["108", "108 KIAS", "108 kias", "108 kts"], "KIAS", 1))
    q.append(create_q("ANKA-LIM-002", sec1, cat, "VCFOP (Max Cowling open Flap open / close and half opened flight)", "90 KIAS", ["90", "90 KIAS", "90 kias", "90 kts"], "KIAS", 1))
    q.append(create_q("ANKA-LIM-003", sec1, cat, "VLO (Max LDGGEAR normal extension)", "90 KIAS", ["90", "90 KIAS", "90 kias", "90 kts"], "KIAS", 1))
    q.append(create_q("ANKA-LIM-004", sec1, cat, "VLO (Max LDGGEAR emergency extension)", "83 KIAS", ["83", "83 KIAS", "83 kias", "83 kts"], "KIAS", 1))
    q.append(create_q("ANKA-LIM-005", sec1, cat, "VLE (Max LDGGEAR extended flight)", "90 KIAS", ["90", "90 KIAS", "90 kias", "90 kts"], "KIAS", 1))

    # Wind Limitations
    cat = "Wind Limitations"
    q.append(create_q("ANKA-LIM-006", sec1, cat, "Wind Limit - HEAD WIND (AUTOTAKEOFF)", "<= 20 KTS", ["<= 20 KTS", "20 KTS", "20 KTS max", "<=20 KTS", "20", "<= 20", "<=20"], "KTS", 1))
    q.append(create_q("ANKA-LIM-007", sec1, cat, "Wind Limit - HEAD WIND (AUTOLAND)", "<= 20 KTS", ["<= 20 KTS", "20 KTS", "20 KTS max", "<=20 KTS", "20", "<= 20", "<=20"], "KTS", 1))
    q.append(create_q("ANKA-LIM-008", sec1, cat, "Wind Limit - HEAD WIND (GUST)", "+/- 7 KTS", ["+/- 7 KTS", "7 KTS", "+/-7 KTS", "7", "+/- 7", "+/-7"], "KTS", 1))
    q.append(create_q("ANKA-LIM-009", sec1, cat, "Wind Limit - CROSS WIND (AUTOTAKEOFF)", "<= 15 KTS", ["<= 15 KTS", "15 KTS", "15 KTS max", "<=15 KTS", "15", "<= 15", "<=15"], "KTS", 1))
    q.append(create_q("ANKA-LIM-010", sec1, cat, "Wind Limit - CROSS WIND (AUTOLAND)", "<= 15 KTS", ["<= 15 KTS", "15 KTS", "15 KTS max", "<=15 KTS", "15", "<= 15", "<=15"], "KTS", 1))
    q.append(create_q("ANKA-LIM-011", sec1, cat, "Wind Limit - CROSS WIND (GUST)", "+/- 7 KTS", ["+/- 7 KTS", "7 KTS", "+/-7 KTS", "7", "+/- 7", "+/-7"], "KTS", 1))
    q.append(create_q("ANKA-LIM-012", sec1, cat, "Wind Limit - TAIL WIND (AUTOTAKEOFF)", "<= 6 KTS", ["<= 6 KTS", "6 KTS", "6 KTS max", "<=6 KTS", "6", "<= 6", "<=6"], "KTS", 1))
    q.append(create_q("ANKA-LIM-013", sec1, cat, "Wind Limit - TAIL WIND (AUTOLAND)", "<= 6 KTS", ["<= 6 KTS", "6 KTS", "6 KTS max", "<=6 KTS", "6", "<= 6", "<=6"], "KTS", 1))
    q.append(create_q("ANKA-LIM-014", sec1, cat, "Wind Limit - TAIL WIND (GUST)", "+/- 4 KTS", ["+/- 4 KTS", "4 KTS", "+/-4 KTS", "4", "+/- 4", "+/-4"], "KTS", 1))

    # Performance & Flight Limitations
    cat = "Performance & Flight Limitations"
    q.append(create_q("ANKA-LIM-015", sec1, cat, "Turning Speed", "5 kts or less", ["5 kts or less", "5 kts", "5 knots or less", "<= 5 kts", "5"], "kts", 1))
    q.append(create_q("ANKA-LIM-016", sec1, cat, "MTOW (Max Takeoff Weight)", "1700 Kg", ["1700 Kg", "1700 kg", "1700", "1.700 kg", "1,700 kg"], "Kg", 1))
    q.append(create_q("ANKA-LIM-017", sec1, cat, "Climbing Gradient", "2,5% or more", ["2,5% or more", "2.5% or more", "2,5 percent or more", "2.5 percent or more", ">= 2.5%", "2.5", "2,5"], "%", 1))
    q.append(create_q("ANKA-LIM-018", sec1, cat, "Flight Level Wind", "60 kts or less", ["60 kts or less", "60 kts", "60 knots or less", "<= 60 kts", "60"], "kts", 1))

    # KU-Band Data Link Limitations
    cat = "KU-Band Data Link Limitations"
    q.append(create_q("ANKA-LIM-019", sec1, cat, "KU-Band: Directional Antenna Narrow Band - Ground vs UAV (10,71 Mbps)", "200 Km", ["200 Km", "200 km", "200"], "Km", 1))
    q.append(create_q("ANKA-LIM-020", sec1, cat, "KU-Band: Directional Antenna Narrow Band - Ground vs UAV (21,73 Mbps)", "200 Km", ["200 Km", "200 km", "200"], "Km", 1))
    q.append(create_q("ANKA-LIM-021", sec1, cat, "KU-Band: Directional Antenna Narrow Band - Ground vs UAV (44,73 Mbps)", "200 Km", ["200 Km", "200 km", "200"], "Km", 1))
    q.append(create_q("ANKA-LIM-022", sec1, cat, "KU-Band: Directional Antenna Narrow Band - Ground vs Omni Antenna (10,71 Mbps)", "90 Km", ["90 Km", "90 km", "90"], "Km", 1))
    q.append(create_q("ANKA-LIM-023", sec1, cat, "KU-Band: Directional Antenna Narrow Band - Ground vs Omni Antenna (21,73 Mbps)", "65 Km", ["65 Km", "65 km", "65"], "Km", 1))
    q.append(create_q("ANKA-LIM-024", sec1, cat, "KU-Band: Directional Antenna Narrow Band - Ground vs Omni Antenna (44,73 Mbps)", "45 Km", ["45 Km", "45 km", "45"], "Km", 1))

    q.append(create_q("ANKA-LIM-025", sec1, cat, "KU-Band: Directional Antenna Wide Band - Ground vs UAV (10,71 Mbps)", "40 Km", ["40 Km", "40 km", "40"], "Km", 1))
    q.append(create_q("ANKA-LIM-026", sec1, cat, "KU-Band: Directional Antenna Wide Band - Ground vs UAV (21,73 Mbps)", "30 Km", ["30 Km", "30 km", "30"], "Km", 1))
    q.append(create_q("ANKA-LIM-027", sec1, cat, "KU-Band: Directional Antenna Wide Band - Ground vs UAV (44,73 Mbps)", "20 Km", ["20 Km", "20 km", "20"], "Km", 1))
    q.append(create_q("ANKA-LIM-028", sec1, cat, "KU-Band: Directional Antenna Wide Band - Ground vs Omni Antenna (10,71 Mbps)", "7,5 Km", ["7,5 Km", "7.5 Km", "7,5 km", "7.5 km", "7.5", "7,5"], "Km", 1))
    q.append(create_q("ANKA-LIM-029", sec1, cat, "KU-Band: Directional Antenna Wide Band - Ground vs Omni Antenna (21,73 Mbps)", "5 Km", ["5 Km", "5 km", "5"], "Km", 1))
    q.append(create_q("ANKA-LIM-030", sec1, cat, "KU-Band: Directional Antenna Wide Band - Ground vs Omni Antenna (44,73 Mbps)", "3,5 Km", ["3,5 Km", "3.5 km", "3,5 km", "3.5", "3,5"], "Km", 1))

    q.append(create_q("ANKA-LIM-031", sec1, cat, "KU-Band: Omni Antenna - Ground vs UAV (10,71 Mbps)", "7 Km", ["7 Km", "7 km", "7"], "Km", 1))
    q.append(create_q("ANKA-LIM-032", sec1, cat, "KU-Band: Omni Antenna - Ground vs UAV (21,73 Mbps)", "5 Km", ["5 Km", "5 km", "5"], "Km", 1))
    q.append(create_q("ANKA-LIM-033", sec1, cat, "KU-Band: Omni Antenna - Ground vs UAV (44,73 Mbps)", "3,5 Km", ["3,5 Km", "3.5 km", "3,5 km", "3.5", "3,5"], "Km", 1))
    q.append(create_q("ANKA-LIM-034", sec1, cat, "KU-Band: Omni Antenna - Ground vs Omni Antenna (10,71 Mbps)", "N/A", ["N/A", "NA", "n/a", "-"], "", 1))
    q.append(create_q("ANKA-LIM-035", sec1, cat, "KU-Band: Omni Antenna - Ground vs Omni Antenna (21,73 Mbps)", "N/A", ["N/A", "NA", "n/a", "-"], "", 1))
    q.append(create_q("ANKA-LIM-036", sec1, cat, "KU-Band: Omni Antenna - Ground vs Omni Antenna (44,73 Mbps)", "N/A", ["N/A", "NA", "n/a", "-"], "", 1))

    # Engine & System Limitations Table
    cat = "Engine & System Limitations"
    q.append(create_q("ANKA-LIM-037", sec1, cat, "ENGINE RPM - MIN", "900", ["900", "900 rpm"], "RPM", 1))
    q.append(create_q("ANKA-LIM-038", sec1, cat, "ENGINE RPM - NORMAL OPERATION", "980-2320", ["980-2320", "980 - 2320", "980 to 2320", "980 sampai 2320", "980-2320 rpm"], "RPM", 1))
    q.append(create_q("ANKA-LIM-039", sec1, cat, "ENGINE RPM - MAX", "2357", ["2357", "2357 rpm"], "RPM", 1))

    q.append(create_q("ANKA-LIM-040", sec1, cat, "OIL PRESSURE IN AIR (PSI) - MIN", "17", ["17", "17 psi"], "PSI", 1))
    q.append(create_q("ANKA-LIM-041", sec1, cat, "OIL PRESSURE IN AIR (PSI) - NORMAL OPERATION", "51-87", ["51-87", "51 - 87", "51 to 87", "51 sampai 87", "51-87 psi"], "PSI", 1))
    q.append(create_q("ANKA-LIM-042", sec1, cat, "OIL PRESSURE IN AIR (PSI) - MAX", "94", ["94", "94 psi"], "PSI", 1))

    q.append(create_q("ANKA-LIM-043", sec1, cat, "OIL TEMPERATURE (°C) - MIN", "50", ["50", "50°c", "50 deg c", "50 c"], "°C", 1))
    q.append(create_q("ANKA-LIM-044", sec1, cat, "OIL TEMPERATURE (°C) - NORMAL OPERATION", "75-110", ["75-110", "75 - 110", "75 to 110", "75 sampai 110", "75-110°c"], "°C", 1))
    q.append(create_q("ANKA-LIM-045", sec1, cat, "OIL TEMPERATURE (°C) - MAX", "140", ["140", "140°c", "140 c"], "°C", 1))

    q.append(create_q("ANKA-LIM-046", sec1, cat, "GEAR BOX TEMPERATURE (°C) - MIN", "-30", ["-30", "-30°c", "-30 c"], "°C", 1))
    q.append(create_q("ANKA-LIM-047", sec1, cat, "GEAR BOX TEMPERATURE (°C) - NORMAL OPERATION", "70-100", ["70-100", "70 - 100", "70 to 100", "70 sampai 100", "70-100°c"], "°C", 1))
    q.append(create_q("ANKA-LIM-048", sec1, cat, "GEAR BOX TEMPERATURE (°C) - MAX", "120", ["120", "120°c", "120 c"], "°C", 1))

    q.append(create_q("ANKA-LIM-049", sec1, cat, "COOLANT TEMPERATURE (°C) - MIN", "-32", ["-32", "-32°c", "-32 c"], "°C", 1))
    q.append(create_q("ANKA-LIM-050", sec1, cat, "COOLANT TEMPERATURE (°C) - NORMAL OPERATION", "80-100", ["80-100", "80 - 100", "80 to 100", "80 sampai 100", "80-100°c"], "°C", 1))
    q.append(create_q("ANKA-LIM-051", sec1, cat, "COOLANT TEMPERATURE (°C) - MAX", "105", ["105", "105°c", "105 c"], "°C", 1))

    q.append(create_q("ANKA-LIM-052", sec1, cat, "RAIL PRESSURE (BAR) - MIN", "330", ["330", "330 bar"], "BAR", 1))
    q.append(create_q("ANKA-LIM-053", sec1, cat, "RAIL PRESSURE (BAR) - NORMAL OPERATION", "360-1350", ["360-1350", "360 - 1350", "360 to 1350", "360 sampai 1350", "360-1350 bar"], "BAR", 1))
    q.append(create_q("ANKA-LIM-054", sec1, cat, "RAIL PRESSURE (BAR) - MAX", "1425", ["1425", "1425 bar"], "BAR", 1))

    q.append(create_q("ANKA-LIM-055", sec1, cat, "FUEL PRESSURE (PSI) - MIN", "4", ["4", "4 psi"], "PSI", 1))
    q.append(create_q("ANKA-LIM-056", sec1, cat, "FUEL PRESSURE (PSI) - NORMAL OPERATION", "5-35", ["5-35", "5 - 35", "5 to 35", "5 sampai 35", "5-35 psi"], "PSI", 1))
    q.append(create_q("ANKA-LIM-057", sec1, cat, "FUEL PRESSURE (PSI) - MAX", "44", ["44", "44 psi"], "PSI", 1))

    q.append(create_q("ANKA-LIM-058", sec1, cat, "ALTERNATOR VOLTAGE (V) - MIN", "22", ["22", "22 v", "22 volt"], "V", 1))
    q.append(create_q("ANKA-LIM-059", sec1, cat, "ALTERNATOR VOLTAGE (V) - NORMAL OPERATION", "27-28", ["27-28", "27 - 28", "27 to 28", "27 sampai 28", "27-28 v"], "V", 1))
    q.append(create_q("ANKA-LIM-060", sec1, cat, "ALTERNATOR VOLTAGE (V) - MAX", "29", ["29", "29 v", "29 volt"], "V", 1))

    q.append(create_q("ANKA-LIM-061", sec1, cat, "ALTERNATOR CURRENT (AMP) - NORMAL OPERATION", "0-140", ["0-140", "0 - 140", "0 to 140", "0 sampai 140", "0-140 amp"], "AMP", 1))
    q.append(create_q("ANKA-LIM-062", sec1, cat, "ALTERNATOR CURRENT (AMP) - MAX", "141", ["141", "141 amp"], "AMP", 1))

    # Operational Wind & Weather
    cat = "Operational Wind & Weather Limits"
    q.append(create_q("ANKA-LIM-063", sec1, cat, "Max allowable wind speed at UAV", "60", ["60", "60 kts", "60 knots"], "kts", 1))
    q.append(create_q("ANKA-LIM-064", sec1, cat, "Pilot may exceed wind limit according to fuel, range & ground speed up to", "80", ["80", "80 kts", "80 knots"], "kts", 1))
    q.append(create_q("ANKA-LIM-065", sec1, cat, "For rain condition, add to Stall speeds", "+1", ["+1", "1", "+1 kts", "1 kts", "+ 1"], "kts", 1))

    # Takeoff entry conditions
    cat = "Takeoff Entry Conditions"
    q.append(create_q("ANKA-LIM-066", sec1, cat, "TAKEOFF entry conditions: Airspeed below", "20", ["20", "20 kts", "< 20", "< 20 kts"], "kts", 1))
    q.append(create_q("ANKA-LIM-067", sec1, cat, "TAKEOFF entry conditions: Heading within runway", "10°", ["10°", "10 deg", "10", "10 derajat"], "°", 1))
    q.append(create_q("ANKA-LIM-068", sec1, cat, "TAKEOFF entry conditions: Lateral deviation from centerline +/-", "3", ["3", "3 meters", "3 m", "+/- 3", "+/- 3 m", "+/-3"], "meters", 1))
    q.append(create_q("ANKA-LIM-069", sec1, cat, "TAKEOFF entry conditions: Start point deviation +/-", "5", ["5", "5 meters", "5 m", "+/- 5", "+/- 5 m", "+/-5"], "meters", 1))

    # Landing limitations
    cat = "Landing Limitations"
    q.append(create_q("ANKA-LIM-070", sec1, cat, "Landing limitations: Max CRAB angle at touchdown <", "4°", ["4°", "4", "4 deg", "< 4°", "< 4"], "°", 1))
    q.append(create_q("ANKA-LIM-071", sec1, cat, "Landing limitations: Pitch angle at touchdown between (min)", "-1°", ["-1°", "-1", "-1 deg", "- 1°"], "°", 1))
    q.append(create_q("ANKA-LIM-072", sec1, cat, "Landing limitations: Pitch angle at touchdown and (max)", "7°", ["7°", "7", "7 deg", "8°", "8", "8 deg"], "°", 1))
    q.append(create_q("ANKA-LIM-073", sec1, cat, "Landing limitations: Max roll angle at touchdown <", "8°", ["8°", "8", "8 deg", "< 8°", "< 8"], "°", 1))
    q.append(create_q("ANKA-LIM-074", sec1, cat, "Landing limitations: Max deviation from centerline +/-", "7,5 meters", ["7,5 meters", "7.5 meters", "7,5m", "7.5m", "7.5", "7,5", "+/- 7.5"], "meters", 1))

    # Weather Avoidance
    cat = "Weather Avoidance"
    q.append(create_q("ANKA-LIM-075", sec1, cat, "Do Not Enter or fly in CB Vicinity within", "10 km", ["10 km", "10 KM", "10"], "km", 1))

    # ==========================================
    # SECTION 2: EMER - ACT POSITION FAIL
    # ==========================================
    sec2 = "EMER - ACT POSITION FAIL"
    cat2 = "Actuator Position Fail Emergency"
    q.append(create_q("ANKA-ACT-001", sec2, cat2, "1. Flight Mode", "HOLD - ROLL", ["HOLD - ROLL", "HOLD ROLL", "HOLD-ROLL"], "", 2))
    q.append(create_q("ANKA-ACT-002", sec2, cat2, "2. Airspeed", "1.2 Vs", ["1.2 Vs", "1.2VS", "1.2 VS", "1 2 vs", "1,2 Vs"], "", 2))
    q.append(create_q("ANKA-ACT-003", sec2, cat2, "3. Actuators (affected)", "FLOAT", ["FLOAT"], "", 2))
    q.append(create_q("ANKA-ACT-004", sec2, cat2, "4. Actuators (affected)", "RESET", ["RESET"], "", 2))
    q.append(create_q("ANKA-ACT-005", sec2, cat2, "If failure message remains: 5A. Actuator (affected)", "FLOAT", ["FLOAT"], "", 2))
    q.append(create_q("ANKA-ACT-006", sec2, cat2, "If failure message remains: 5B. Landing Action", "LAND AS SOON AS PRACTICABLE", ["LAND AS SOON AS PRACTICABLE"], "", 2))

    # Crosswind Ruddervator Failure Parameters
    cat2_cw = "Crosswind Ruddervator Failure Surface Wind"
    q.append(create_q("ANKA-ACT-007", sec2, cat2_cw, "Surface Landing Wind Direction - RIRV", "Left", ["Left", "LEFT", "Kiri"], "", 2))
    q.append(create_q("ANKA-ACT-008", sec2, cat2_cw, "Surface Landing Wind Direction - RORV", "Left", ["Left", "LEFT", "Kiri"], "", 2))
    q.append(create_q("ANKA-ACT-009", sec2, cat2_cw, "Surface Landing Wind Direction - LIRV", "Right", ["Right", "RIGHT", "Kanan"], "", 2))
    q.append(create_q("ANKA-ACT-010", sec2, cat2_cw, "Surface Landing Wind Direction - LORV", "Right", ["Right", "RIGHT", "Kanan"], "", 2))
    q.append(create_q("ANKA-ACT-011", sec2, cat2_cw, "Surface Landing Wind Direction - RIA", "Right", ["Right", "RIGHT", "Kanan"], "", 2))
    q.append(create_q("ANKA-ACT-012", sec2, cat2_cw, "Surface Landing Wind Direction - ROA", "Right", ["Right", "RIGHT", "Kanan"], "", 2))
    q.append(create_q("ANKA-ACT-013", sec2, cat2_cw, "Surface Landing Wind Direction - LIA", "Left", ["Left", "LEFT", "Kiri"], "", 2))
    q.append(create_q("ANKA-ACT-014", sec2, cat2_cw, "Surface Landing Wind Direction - LOA", "Left", ["Left", "LEFT", "Kiri"], "", 2))

    q.append(create_q("ANKA-ACT-015", sec2, cat2, "5C. AUTOLAND", "Verify DEGRADED", ["Verify DEGRADED", "Verify degraded", "DEGRADED"], "", 2))

    # ==========================================
    # SECTION 3: EMER - ENG RPM HIGH
    # ==========================================
    sec3 = "EMER - ENG RPM HIGH"
    cat3 = "Engine RPM High Emergency"
    q.append(create_q("ANKA-RPMH-001", sec3, cat3, "1. Flight Mode", "HOLD - THR", ["HOLD - THR", "HOLD THR", "HOLD-THR"], "", 3))
    q.append(create_q("ANKA-RPMH-002", sec3, cat3, "2. ENG THR", "Decrease", ["Decrease", "DECREASE", "Turunkan"], "", 3))
    q.append(create_q("ANKA-RPMH-003", sec3, cat3, "3. Airspeed", "Adjust", ["Adjust", "ADJUST", "Sesuaikan"], "", 3))
    q.append(create_q("ANKA-RPMH-004", sec3, cat3, "4. ENG THR", "As Required", ["As Required", "AS REQUIRED", "Sesuai kebutuhan"], "", 3))
    q.append(create_q("ANKA-RPMH-005", sec3, cat3, "5. ENG RPM", "Check", ["Check", "CHECK", "Periksa"], "", 3))
    q.append(create_q("ANKA-RPMH-006", sec3, cat3, "If RPM is below 2,320:", "LAND AS SOON AS PRACTICABLE", ["LAND AS SOON AS PRACTICABLE"], "", 3))
    q.append(create_q("ANKA-RPMH-007", sec3, cat3, "If RPM is above 2,320:", "LAND AS SOON AS POSSIBLE", ["LAND AS SOON AS POSSIBLE"], "", 3))
    q.append(create_q("ANKA-RPMH-008", sec3, cat3, "Continue / consider:", "Consider DEGRADED", ["Consider DEGRADED", "Consider degraded", "DEGRADED"], "", 3))

    # ==========================================
    # SECTION 4: EMER - ENG RPM LOW
    # ==========================================
    sec4 = "EMER - ENG RPM LOW"
    cat4 = "Engine RPM Low Emergency"
    q.append(create_q("ANKA-RPML-001", sec4, cat4, "1. Flight Mode", "HOLD - THR", ["HOLD - THR", "HOLD THR", "HOLD-THR"], "", 4))
    q.append(create_q("ANKA-RPML-002", sec4, cat4, "2. ENG THR", "As Required", ["As Required", "AS REQUIRED", "Sesuai kebutuhan"], "", 4))
    q.append(create_q("ANKA-RPML-003", sec4, cat4, "3. Propeller", "On", ["On", "ON"], "", 4))
    q.append(create_q("ANKA-RPML-004", sec4, cat4, "4. System", "Consider OFF", ["Consider OFF", "OFF"], "", 4))
    q.append(create_q("ANKA-RPML-005", sec4, cat4, "5. Landing decision", "LAND AS SOON AS POSSIBLE", ["LAND AS SOON AS POSSIBLE"], "", 4))
    q.append(create_q("ANKA-RPML-006", sec4, cat4, "6. Status", "DEGRADED", ["DEGRADED"], "", 4))

    # ==========================================
    # SECTION 5: EMER - LDG GR EXTENTION FAIL
    # ==========================================
    sec5 = "EMER - LDG GR EXTENTION FAIL"
    cat5 = "Landing Gear Extension Fail Emergency"
    q.append(create_q("ANKA-LDG-001", sec5, cat5, "1. Flight Mode", "FORCE EXT", ["FORCE EXT", "FORCE EXTENSION", "FORCE EXTEND"], "", 5))
    q.append(create_q("ANKA-LDG-002", sec5, cat5, "2. ENG THR", "Decrease", ["Decrease", "DECREASE", "Turunkan"], "", 5))
    q.append(create_q("ANKA-LDG-003", sec5, cat5, "3. System", "STOW", ["STOW", "STOWED"], "", 5))
    q.append(create_q("ANKA-LDG-004", sec5, cat5, "4. Landing gear", "Consider POS 1 or POS 2", ["Consider POS 1 or POS 2", "POS 1 or POS 2", "CONSIDER POS 1 OR POS 2", "POS 1 atau POS 2", "POS 1/POS 2"], "", 5))
    q.append(create_q("ANKA-LDG-005", sec5, cat5, "5. Touchdown action", "CUT, at Touchdown", ["CUT, at Touchdown", "CUT AT TOUCHDOWN", "CUT, AT TOUCHDOWN", "CUT"], "", 5))
    q.append(create_q("ANKA-LDG-006", sec5, cat5, "6. Backup plan", "Consider BACKUP at Touchdown", ["Consider BACKUP at Touchdown", "BACKUP AT TOUCHDOWN", "CONSIDER BACKUP AT TOUCHDOWN", "BACKUP"], "", 5))
    q.append(create_q("ANKA-LDG-007", sec5, cat5, "7. Engine thrust", "As Required", ["As Required", "AS REQUIRED"], "", 5))

    # ==========================================
    # SECTION 6: EMER - ENG STOPPED
    # ==========================================
    sec6 = "EMER - ENG STOPPED"
    cat6 = "Engine Stopped Emergency"
    q.append(create_q("ANKA-STOP-001", sec6, cat6, "1. THR Response", "Check", ["Check", "CHECK", "Periksa"], "", 6))
    q.append(create_q("ANKA-STOP-002", sec6, cat6, "If it is NOT possible to reach Main/Emer Base: 2A. Emergency Landing Area", "Update", ["Update", "UPDATE"], "", 6))
    q.append(create_q("ANKA-STOP-003", sec6, cat6, "If it is NOT possible to reach Main/Emer Base: 2B. Flight Mode", "EMER", ["EMER", "EMERGENCY"], "", 6))
    q.append(create_q("ANKA-STOP-004", sec6, cat6, "If it is possible to reach Main/Emer Base: 2A. Airspeed", "GLIDE SPEED", ["GLIDE SPEED", "GLIDE-SPEED", "GLIDESPEED"], "", 6))
    q.append(create_q("ANKA-STOP-005", sec6, cat6, "3. WBS, ADT, and FLIR", "Consider OFF within 2 minutes", ["Consider OFF within 2 minutes", "CONSIDER OFF WITHIN 2 MINUTES", "OFF within 2 minutes", "OFF"], "", 6))
    q.append(create_q("ANKA-STOP-006", sec6, cat6, "If time and altitude permit for engine restart: 4. Altitude", "Below 13,000 ft MSL", ["Below 13,000 ft MSL", "BELOW 13,000 FT MSL", "below 13000 ft msl", "< 13000", "< 13,000 ft", "13000", "13.000", "13,000"], "ft MSL", 6))
    q.append(create_q("ANKA-STOP-007", sec6, cat6, "If engine does NOT start automatically: 5. FUEL PUMP", "Verify ON", ["Verify ON", "VERIFY ON", "ON"], "", 6))
    q.append(create_q("ANKA-STOP-008", sec6, cat6, "6. THR", "IDLE", ["IDLE", "Idle"], "", 6))
    q.append(create_q("ANKA-STOP-009", sec6, cat6, "If RPM is above 600, repeat ENG STOP and START: 7. ENG", "STOP", ["STOP", "Stop"], "", 6))
    q.append(create_q("ANKA-STOP-010", sec6, cat6, "8. ENG", "START", ["START", "Start"], "", 6))
    q.append(create_q("ANKA-STOP-011", sec6, cat6, "If propeller does NOT start and RPM is below 600: 9. BUS", "TIE", ["TIE", "Tie"], "", 6))
    q.append(create_q("ANKA-STOP-012", sec6, cat6, "10. STARTER", "ON", ["ON", "On"], "", 6))
    q.append(create_q("ANKA-STOP-013", sec6, cat6, "If engine starts: 11A. BUS", "Verify UNTIE", ["Verify UNTIE", "VERIFY UNTIE", "UNTIE"], "", 6))
    q.append(create_q("ANKA-STOP-014", sec6, cat6, "11B. Failure Messages", "Check", ["Check", "CHECK"], "", 6))
    q.append(create_q("ANKA-STOP-015", sec6, cat6, "11C. Engine RPM and Throttle", "Check", ["Check", "CHECK"], "", 6))
    q.append(create_q("ANKA-STOP-016", sec6, cat6, "11D. Action", "LAND AS SOON AS PRACTICABLE", ["LAND AS SOON AS PRACTICABLE"], "", 6))
    q.append(create_q("ANKA-STOP-017", sec6, cat6, "If engine does NOT start and possible to reach base: 11A. RTB and Emergency Landing Area", "Update", ["Update", "UPDATE"], "", 6))
    q.append(create_q("ANKA-STOP-018", sec6, cat6, "11B. AUTOLAND", "Verify DEGRADED", ["Verify DEGRADED", "VERIFY DEGRADED", "DEGRADED"], "", 6))
    q.append(create_q("ANKA-STOP-019", sec6, cat6, "11C. Action", "LAND AS SOON AS POSSIBLE", ["LAND AS SOON AS POSSIBLE"], "", 6))
    q.append(create_q("ANKA-STOP-020", sec6, cat6, "If engine does NOT start and NOT possible to reach base: 11A. Emergency Landing Area", "Update", ["Update", "UPDATE"], "", 6))
    q.append(create_q("ANKA-STOP-021", sec6, cat6, "11B. Flight Mode", "EMER", ["EMER", "EMERGENCY"], "", 6))

    categories = sorted(list(set(item["category"] for item in q)))
    sections = [
        "BOLD FACE LIMITATIONS",
        "EMER - ACT POSITION FAIL",
        "EMER - ENG RPM HIGH",
        "EMER - ENG RPM LOW",
        "EMER - LDG GR EXTENTION FAIL",
        "EMER - ENG STOPPED"
    ]

    return {
        "aircraft": "ANKA MALE UAV",
        "title": "ANKA MALE UAV - BOLD FACE LIMITATIONS & EMERGENCY PROCEDURES",
        "sourceDocument": "ANKAID-T0544-AFM-2",
        "description": "Bold Face Limitations (Airspeed, Wind, KU-Band, Engine & System Limits), Takeoff/Landing Limitations, dan Emergency Procedures (Actuator Fail, Engine RPM High/Low, Gear Extension Fail, Engine Stopped) ANKA MALE UAV",
        "totalQuestions": len(q),
        "categoriesCount": len(categories),
        "categories": categories,
        "sections": sections,
        "questions": q
    }

if __name__ == '__main__':
    data = build_anka_dataset()
    with open('data/anka-male-uav.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Generated data/anka-male-uav.json with {data['totalQuestions']} questions across {len(data['sections'])} sections and {data['categoriesCount']} categories.")
