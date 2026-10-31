# Project Memory & Operating Guidelines: AI สำหรับ อปท. (Local Government AI Workshop)

This project contains the complete curriculum, interactive slide system, trainer guide, participant workbook, and web learning platform for the **Local Government AI Workshop (การประยุกต์ใช้ AI เพื่อยกระดับการทำงานขององค์กรปกครองส่วนท้องถิ่น - อปท.)**.

---

## 1. Core Ecosystem Files & Roles

Always refer to and maintain these five integrated components:

1. **`ai.html`**: Interactive web application featuring:
   - Module Lessons (Workshops 1-7)
   - 4-Part Prompt Builder (Role, Task, Context, Format with PDPA guard)
   - Participant Workspace & Portfolio (Auto-save profile in LocalStorage, saved prompts library)
   - Post-Test Quiz (5 questions linked directly to certificate issuance)
   - Royal Thai Government E-Certificate (A4 Landscape, print-optimized with `@page { size: A4 landscape; margin: 0; }`)
2. **`slides.html` & `AI_LG_Workshop_Presentation.pptx`**:
   - 38 widescreen 16:9 slides
   - Interactive jump cards on Slide 7 jumping to all 6 government document types and 9 subtypes
   - Full mockups (15 realistic government document modals in `document_previews.js`)
   - Presentation tools: Countdown timer (`T`), Laser pointer (`L`), Blank screen (`B`), Speaker notes (`N`), Overview (`O`)
3. **`trainer_guide.html`**: Master schedule (08:30-16:30), step-by-step teaching scripts, pitfall warnings, scoring rubrics, and quiz answer keys.
4. **`handout.html`**: Printable A4 workbook & cheat sheet with RTCF formulas, PDPA rules, and 30-day action plan.
5. **`workflow.md`**: Master system documentation and maintenance guide.

---

## 2. Thai Government Document Knowledge Base (ระเบียบสารบรรณ พ.ศ. 2526)

When updating content or prompts, strictly adhere to the 6 types of Thai official government documents:
- **1. หนังสือภายนอก (External Letter):** กระดาษตราครุฑ 3 ซม. ติดต่อส่วนราชการภายนอก/เอกชน
- **2. หนังสือภายใน (Internal Memo):** บันทึกข้อความ ครุฑ 1.5 ซม. โครงสร้าง 3 ส่วน: ต้นเรื่อง, ข้อเท็จจริง, ข้อพิจารณาและข้อเสนอ
- **3. หนังสือประทับตรา (Seal Letter):** ประทับตราแทนการลงชื่อ หมึกสีชาด (ทรงกระบอก 4.5 ซม.)
- **4. หนังสือสั่งการ (3 ประเภทย่อย):**
  - 4.1 คำสั่ง (นายก อปท./ผู้ว่าฯ)
  - 4.2 ระเบียบ (สภาท้องถิ่น/กรรมการ)
  - 4.3 ข้อบังคับ (ความปลอดภัย/วินัย)
- **5. หนังสือประชาสัมพันธ์ (3 ประเภทย่อย):**
  - 5.1 ประกาศ (แจ้งให้ทราบโดยทั่วกัน)
  - 5.2 แถลงการณ์ (วิกฤต/ฉุกเฉิน)
  - 5.3 ข่าว (ข่าวแจกสื่อมวลชน)
- **6. หนังสือที่เจ้าหน้าที่ทำขึ้นหรือรับไว้เป็นหลักฐาน (3 ประเภทย่อย):**
  - 6.1 หนังสือรับรอง (การทำงาน/เงินเดือน)
  - 6.2 รายงานการประชุม (ตามระเบียบข้อ 25)
  - 6.3 บันทึก (บันทึกตรวจรับพัสดุ/รายงานผล)

---

## 3. Automation Scripts Pipeline

- **Python environment with python-pptx:** `/Library/Frameworks/Python.framework/Versions/3.10/bin/python3`
- **Recompile slide data:** `python3 build_full_slides_data.py`
- **Generate PPTX deck:** `/Library/Frameworks/Python.framework/Versions/3.10/bin/python3 generate_pptx.py`
- **Upgrade/Sync ai.html:** `python3 upgrade_ai_html.py`
- **Source docx:** `คู่มือการฝึกอบรมเชิงปฏิบัติการ (Workshop)_ การประยุกต์ใช้ AI สำหรับองค์กรปกครองส่วนท้องถิ่น (อปท.).docx`

---

## 4. Behavioral & Quality Standards

- Maintain formal, professional Thai language suited for Thai local government officials (ภาษาราชการ).
- Always ensure all 4 HTML tools (`ai.html`, `slides.html`, `trainer_guide.html`, `handout.html`) contain reciprocal links in their headers/floating navigation bars.
- When generating or editing government documents, ensure PDPA anonymization rules are respected (no real 13-digit citizen IDs or personal phone numbers).
