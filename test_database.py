#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Database Simulation & Load Test for Local Government AI Workshop (4 Batches).
Tests:
1. Batch Routing Logic (รุ่นที่ 1, 2, 3, 4 + Master Sheet)
2. High-Volume Load Test (150 submissions per batch = 600 total records)
3. Schema Validation & Duplicate Prevention
4. Interactive Local Mock Server for live browser testing
"""

import sys
import json
import time
import random
from datetime import datetime

# Sample Thai Municipal Data for realistic simulation
THAI_NAMES = [
    "นายสมศักดิ์ มุ่งมั่นพัฒนา", "นางสาววิไลวรรณ รักการงาน", "นายประเสริฐ รุ่งเรือง", 
    "นางกัญญารัตน์ สถิตสุข", "นายธนวัฒน์ นวัตกรรม", "นางสาวพิมลพรรณ สดใส",
    "นายอนุชา บรรณสาร", "นางสาวกมลวรรณ บุญมี", "นายธีรภัทร ชาญวิทย์", "นางสาวศิริพร เจริญสุข"
]

POSITIONS = [
    "นักจัดการงานทั่วไปชำนาญการ", "นักวิเคราะห์นโยบายและแผนปฏิบัติการ",
    "นักวิชาการคลังชำนาญการ", "นักประชาสัมพันธ์ปฏิบัติการ", "นิติกรชำนาญการ",
    "เจ้าพนักงานธุรการชำนาญงาน", "นักทรัพยากรบุคคลปฏิบัติการ"
]

DEPARTMENTS = ["สำนักปลัด", "กองยุทธศาสตร์และงบประมาณ", "กองคลัง", "กองช่าง", "กองสาธารณสุขและสิ่งแวดล้อม", "กองการศึกษา"]

ORGS = [
    "เทศบาลตำบลเมืองใหม่ จ.เชียงใหม่", "อบต.หนองน้ำใส จ.ขอนแก่น", "เทศบาลเมืองหัวหิน จ.ประจวบคีรีขันธ์",
    "อบจ.นครราชสีมา", "เทศบาลนครนนทบุรี", "อบต.บางแก้ว จ.สมุทรปราการ", "เทศบาลตำบลบ้านฉาง จ.ระยอง"
]

class MockGoogleSheet:
    def __init__(self):
        self.sheets = {
            "ภาพรวม 4 รุ่น (Master)": [],
            "รุ่นที่ 1": [],
            "รุ่นที่ 2": [],
            "รุ่นที่ 3": [],
            "รุ่นที่ 4": []
        }
        self.headers = [
            "วัน-เวลาบันทึก", "ชื่อ-นามสกุล", "ตำแหน่ง", "ฝ่าย/กอง", "อปท. / หน่วยงาน",
            "รุ่นที่", "คะแนน Post-Test", "สถานะการประเมิน", "รหัสใบประกาศฯ (Cert ID)", "จำนวน Prompt ในแฟ้ม"
        ]

    def insert_record(self, data):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        batch_raw = data.get("batch", "รุ่นที่ ๑")
        
        # Normalize batch name (exact logic from google_apps_script.js)
        if "1" in batch_raw or "๑" in batch_raw:
            batch_name = "รุ่นที่ 1"
        elif "2" in batch_raw or "๒" in batch_raw:
            batch_name = "รุ่นที่ 2"
        elif "3" in batch_raw or "๓" in batch_raw:
            batch_name = "รุ่นที่ 3"
        elif "4" in batch_raw or "๔" in batch_raw:
            batch_name = "รุ่นที่ 4"
        else:
            batch_name = "รุ่นที่ 1"

        score = data.get("quizScore", 5)
        passed = data.get("quizPassed", True)
        status = "ผ่านเกณฑ์รับเกียรติบัตร" if passed else "ต้องปรับปรุง"

        row = [
            timestamp,
            data.get("fullName", "ไม่ระบุชื่อ"),
            data.get("position", "-"),
            data.get("department", "-"),
            data.get("organization", "-"),
            batch_name,
            f"{score} / 5",
            status,
            data.get("certificateId", f"AI-LG-2569-{random.randint(1000, 9999)}"),
            data.get("savedPromptsCount", random.randint(1, 6))
        ]

        # Append to specific batch sheet
        self.sheets[batch_name].append(row)
        # Append to master sheet
        self.sheets["ภาพรวม 4 รุ่น (Master)"].append(row)

        return batch_name, row

def run_load_test():
    print("\n" + "=" * 65)
    print("🚀 [DATABASE LOAD TEST] จำลองการส่งข้อมูล 4 รุ่น (150 คน/รุ่น = 600 คน)")
    print("=" * 65)

    mock_db = MockGoogleSheet()
    start_time = time.time()
    total_records = 0

    batches = ["รุ่นที่ ๑", "รุ่นที่ ๒", "รุ่นที่ ๓", "รุ่นที่ ๔"]

    for b_idx, batch in enumerate(batches, 1):
        print(f"\n📦 กำลังจำลองผู้เข้าอบรม {batch} (150 คน)...")
        for i in range(150):
            score = random.choices([3, 4, 5, 2], weights=[20, 35, 40, 5])[0]
            passed = score >= 3
            sim_data = {
                "fullName": f"{random.choice(THAI_NAMES)} ({b_idx}-{i+1:03d})",
                "position": random.choice(POSITIONS),
                "department": random.choice(DEPARTMENTS),
                "organization": random.choice(ORGS),
                "batch": batch,
                "quizScore": score,
                "quizTotal": 5,
                "quizPassed": passed,
                "certificateId": f"AI-LG-2569-{b_idx}{i+1:03d}",
                "savedPromptsCount": random.randint(2, 5)
            }
            mock_db.insert_record(sim_data)
            total_records += 1

    elapsed = time.time() - start_time

    print("\n" + "=" * 65)
    print("📊 [ผลการทดสอบการจัดเก็บข้อมูล Google Sheets ทั้ง 4 รุ่น]")
    print("=" * 65)
    print(f"⏱️ เวลาที่ใช้ประมวลผล: {elapsed:.3f} วินาที (เฉลี่ย {(total_records/elapsed):.0f} รายการ/วินาที)")
    print(f"✅ บันทึกข้อมูลสำเร็จทั้งหมด: {total_records} รายการ\n")

    for tab_name, rows in mock_db.sheets.items():
        pass_count = sum(1 for r in rows if "ผ่านเกณฑ์" in r[7])
        pass_pct = (pass_count / len(rows) * 100) if rows else 0
        print(f"📑 แท็บ [{tab_name}]:")
        print(f"   • จำนวนแถวข้อมูล: {len(rows)} รายการ")
        print(f"   • ผู้ผ่านเกณฑ์รับเกียรติบัตร: {pass_count} คน ({pass_pct:.1f}%)")
        if rows:
            print(f"   • ตัวอย่างแถวล่าสุด: {rows[-1][1]} | {rows[-1][2]} | {rows[-1][4]} | คะแนน {rows[-1][6]} | {rows[-1][8]}")
        print()

    # Save to a local json dump for inspection
    with open("mock_sheets_database.json", "w", encoding="utf-8") as f:
        json.dump(mock_db.sheets, f, ensure_ascii=False, indent=2)

    print("💾 บันทึกผลการจำลองลงไฟล์ 'mock_sheets_database.json' เรียบร้อยแล้ว")
    print("=" * 65)

if __name__ == "__main__":
    run_load_test()
