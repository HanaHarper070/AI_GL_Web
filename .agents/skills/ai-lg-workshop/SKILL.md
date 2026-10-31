---
name: ai-lg-workshop
description: >-
  Expert skill for maintaining, extending, and updating the Local Government AI Workshop (อปท.)
  teaching materials, slides, web platform (ai.html), PowerPoint deck, and government document prompts.
  Use this skill whenever the user asks to modify, add, or review content in this repository.
---

# Local Government AI Workshop (อปท.) Expert Skill

This skill provides specialized domain knowledge, operational pipelines, and technical rules for the Local Government AI Workshop codebase in `/Users/hanaharper/Downloads/AI_LG`.

## When to Activate This Skill
- The user asks to add new modules, workshops, or slides.
- The user updates the source Word document (`คู่มือการฝึกอบรมเชิงปฏิบัติการ (Workshop)...docx`).
- The user requests modifications to the prompt structures, document mockups, or quiz questions.
- The user wants to adjust the certificate design, portfolio logic, or presentation features.

## Project Structure & Architecture
- **Web Learning Platform:** `ai.html` (Modules, Prompt Builder, Portfolio, Quiz, Royal Certificate)
- **Interactive Slide Presentation Deck:** `slides.html` (38 widescreen 16:9 slides, Jump Cards on Slide 7)
- **PowerPoint Deck:** `AI_LG_Workshop_Presentation.pptx` (Generated via python-pptx with Speaker Notes)
- **Slide Data & Logic:** `slides_data.js`, `slides_app.js`, `document_previews.js` (15 realistic document mockups)
- **Trainer Guide:** `trainer_guide.html` (Schedule 08:30-16:30, scripts, rubrics, quiz keys)
- **Participant Handout:** `handout.html` (A4 printable cheatsheet, RTCF, 30-day plan)
- **System Documentation:** `workflow.md`

## Standard Government Document Classification (พ.ร.บ. สารบรรณ พ.ศ. ๒๕๒๖)
1. หนังสือภายนอก (External)
2. หนังสือภายใน (Internal Memo - 3 parts: ต้นเรื่อง, ข้อเท็จจริง, ข้อพิจารณา/ข้อเสนอ)
3. หนังสือประทับตรา (Seal Letter)
4. หนังสือสั่งการ (Orders: คำสั่ง, ระเบียบ, ข้อบังคับ)
5. หนังสือประชาสัมพันธ์ (Public Relations: ประกาศ, แถลงการณ์, ข่าว)
6. หนังสือที่เจ้าหน้าที่ทำขึ้น (Officer Records: หนังสือรับรอง, รายงานการประชุม, บันทึก)

## Key Maintenance Commands
- Rebuild slides data: `python3 build_full_slides_data.py`
- Rebuild PowerPoint deck: `/Library/Frameworks/Python.framework/Versions/3.10/bin/python3 generate_pptx.py`
- Update ai.html system: `python3 upgrade_ai_html.py`
