#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Local Live Database & Dashboard Server for Local Government AI Workshop.
Simulates Google Apps Script Web App locally on port 8765.
Also serves a live Admin Dashboard (live_database_summary.html) so you can see live submissions!
"""

import http.server
import socketserver
import json
import os
from datetime import datetime

PORT = 8765
DB_FILE = os.path.join(os.path.dirname(__file__), "live_workshop_database.json")

def load_db():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "Master": [],
        "รุ่นที่ 1": [],
        "รุ่นที่ 2": [],
        "รุ่นที่ 3": [],
        "รุ่นที่ 4": []
    }

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

class LiveDBHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS for all local requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path == "/status" or self.path == "/":
            db = load_db()
            total_students = len(db["Master"])
            response = {
                "status": "online",
                "message": "Local Live Database Server for AI Local Government Workshop is active",
                "totalSubmissions": total_students,
                "batches": {k: len(v) for k, v in db.items() if k != "Master"}
            }
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        raw_body = self.rfile.read(content_length).decode('utf-8')
        
        try:
            data = json.loads(raw_body)
        except Exception:
            data = {"raw": raw_body}

        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        batch_raw = data.get("batch", "รุ่นที่ ๑")
        
        # Normalize batch
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

        student_record = {
            "timestamp": timestamp,
            "fullName": data.get("fullName", "ไม่ระบุชื่อ"),
            "position": data.get("position", "-"),
            "department": data.get("department", "-"),
            "organization": data.get("organization", "-"),
            "batch": batch_name,
            "quizScore": data.get("quizScore", "-"),
            "quizTotal": data.get("quizTotal", 5),
            "quizPassed": data.get("quizPassed", False),
            "certificateId": data.get("certificateId", "-"),
            "savedPromptsCount": data.get("savedPromptsCount", 0)
        }

        # Save to database
        db = load_db()
        db[batch_name].append(student_record)
        db["Master"].append(student_record)
        save_db(db)

        # Print live notification to console
        print("\n" + "🟢" * 25)
        print(f"📥 [LIVE DATA RECEIVED] ข้อมูลใหม่เข้ามาในระบบ! ({timestamp})")
        print(f"👤 ชื่อ: {student_record['fullName']}")
        print(f"💼 ตำแหน่ง: {student_record['position']} ({student_record['organization']})")
        print(f"📦 รุ่น: {student_record['batch']}")
        print(f"🏆 คะแนน Post-Test: {student_record['quizScore']} / {student_record['quizTotal']} ({'ผ่านเกณฑ์ ✅' if student_record['quizPassed'] else 'ไม่ผ่าน ❌'})")
        print(f"🎓 รหัสเกียรติบัตร: {student_record['certificateId']}")
        print(f"📊 สรุปยอดรวมขณะนี้: {len(db['Master'])} คน (รุ่นที่ 1: {len(db['รุ่นที่ 1'])}, รุ่นที่ 2: {len(db['รุ่นที่ 2'])}, รุ่นที่ 3: {len(db['รุ่นที่ 3'])}, รุ่นที่ 4: {len(db['รุ่นที่ 4'])})")
        print("🟢" * 25 + "\n")

        # Response
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        res_data = {
            "status": "success",
            "message": f"บันทึกข้อมูลเรียบร้อยแล้ว ({batch_name})",
            "batch": batch_name,
            "timestamp": timestamp
        }
        self.wfile.write(json.dumps(res_data, ensure_ascii=False).encode('utf-8'))

def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), LiveDBHandler) as httpd:
        print(f"\n========================================================")
        print(f"🌐 [LOCAL DATABASE SERVER] ทำงานอยู่ที่ http://localhost:{PORT}")
        print(f"   • Endpoint สำหรับส่งข้อมูล: http://localhost:{PORT}/webhook")
        print(f"   • ตรวจสอบสถานะเซิร์ฟเวอร์: http://localhost:{PORT}/status")
        print(f"========================================================\n")
        httpd.serve_forever()

if __name__ == '__main__':
    run_server()
