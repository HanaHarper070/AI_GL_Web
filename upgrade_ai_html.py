# -*- coding: utf-8 -*-
"""
Script to upgrade ai.html with:
1. Updated Header Navigation with all 5 views + 3 companion tools.
2. Participant Workspace & Portfolio (view-portfolio) with profile, progress tracking, saved prompt library.
3. Royal Thai Government E-Certificate Generator (view-certificate) in A4 Landscape with print CSS.
4. Cross-linking: Builder to Portfolio, Workshop Prompts to Portfolio, Quiz to Certificate.
"""

import re

def main():
    with open('/Users/hanaharper/Downloads/AI_LG/ai.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. ENHANCE CSS STYLES (<style> tag)
    css_addition = """
        /* Certificate & Portfolio Print & Visual Styles */
        @media print {
            body {
                background: #ffffff !important;
                color: #000000 !important;
                padding: 0 !important;
                margin: 0 !important;
            }
            header, #sidebar, #sidebar-overlay, #toast, .no-print, nav {
                display: none !important;
            }
            main, #main-content {
                padding: 0 !important;
                margin: 0 !important;
                max-width: 100% !important;
                width: 100% !important;
            }
            .print-only {
                display: block !important;
            }
            
            /* Certificate Print in A4 Landscape */
            body.printing-certificate {
                margin: 0 !important;
                padding: 0 !important;
            }
            body.printing-certificate #view-certificate {
                display: block !important;
                padding: 0 !important;
                margin: 0 !important;
            }
            body.printing-certificate #certificate-frame {
                box-shadow: none !important;
                border-radius: 0 !important;
                width: 297mm !important;
                height: 209mm !important;
                max-width: 297mm !important;
                margin: 0 auto !important;
                page-break-inside: avoid !important;
                page-break-after: avoid !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
            @page {
                size: A4 landscape;
                margin: 0;
            }
        }

        /* Certificate Aesthetics */
        .cert-outer-border {
            border: 4px solid #1e3a8a;
            position: relative;
        }
        .cert-inner-border {
            border: 2px solid #d97706;
        }
        .cert-watermark {
            background-image: radial-gradient(circle at center, rgba(30, 58, 138, 0.03) 0%, rgba(255, 255, 255, 0) 70%);
        }
        .cert-gold-foil {
            background: radial-gradient(ellipse farthest-corner at right bottom, #FEDB37 0%, #FDB931 8%, #9f7928 30%, #8A6E2F 40%, transparent 80%),
                        radial-gradient(ellipse farthest-corner at left top, #FFFFFF 0%, #FFFFAC 8%, #D1B464 25%, #5d4a1f 62.5%, #5d4a1f 100%);
        }
        .signature-font {
            font-family: 'Brush Script MT', 'Segoe Script', cursive, sans-serif;
        }
    """
    
    # Inject CSS before </style>
    html = html.replace('    </style>', css_addition + '\n    </style>')

    # 2. REPLACE HEADER WITH ENHANCED NAVIGATION
    old_header_pattern = r'<header class="sticky top-0 z-40 bg-gov-900.*?</header>'
    new_header = """<header class="sticky top-0 z-40 bg-gov-900 text-white shadow-lg border-b border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-3">
            <!-- Brand / Title -->
            <div class="flex items-center gap-3 shrink-0">
                <button id="mobile-menu-btn" onclick="toggleMobileSidebar()" class="lg:hidden p-2 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 focus:outline-none">
                    <i data-lucide="menu" class="w-6 h-6"></i>
                </button>
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-amber-400 to-amber-600 flex items-center justify-center shadow-md shrink-0">
                    <i data-lucide="landmark" class="w-6 h-6 text-slate-950"></i>
                </div>
                <div class="hidden sm:block">
                    <div class="flex items-center gap-2">
                        <span class="text-[11px] font-heading font-semibold uppercase tracking-wider px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">ระบบการเรียนรู้ดิจิทัล อปท.</span>
                        <span class="text-xs text-slate-400">พ.ศ. 2569</span>
                    </div>
                    <h1 class="font-heading font-bold text-base text-white truncate max-w-[220px] md:max-w-xs lg:max-w-md">
                        การประยุกต์ใช้ AI ในการทำงาน อปท.
                    </h1>
                </div>
            </div>

            <!-- Central Navigation Tabs (Interactive Views) -->
            <nav class="flex items-center gap-1 sm:gap-1.5 overflow-x-auto py-1">
                <!-- 1. Workshop Lessons -->
                <button onclick="switchMainView('workshop')" id="nav-btn-workshop" class="nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-semibold transition bg-amber-500 text-slate-950 shadow-sm">
                    <i data-lucide="book-open" class="w-4 h-4"></i>
                    <span>บทเรียน</span>
                </button>

                <!-- 2. Interactive Prompt Builder -->
                <button onclick="switchMainView('builder')" id="nav-btn-builder" class="nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition">
                    <i data-lucide="wand-2" class="w-4 h-4"></i>
                    <span class="hidden md:inline">สร้าง Prompt</span>
                    <span class="md:hidden">Prompt</span>
                </button>

                <!-- 3. Participant Portfolio -->
                <button onclick="switchMainView('portfolio')" id="nav-btn-portfolio" class="nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition relative">
                    <i data-lucide="folder-kanban" class="w-4 h-4 text-emerald-400"></i>
                    <span>แฟ้มผลงาน</span>
                    <span id="nav-portfolio-badge" class="hidden absolute -top-1 -right-1 px-1.5 py-0.2 bg-emerald-500 text-[10px] text-white font-bold rounded-full">0</span>
                </button>

                <!-- 4. Post-Test Quiz -->
                <button onclick="switchMainView('quiz')" id="nav-btn-quiz" class="nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition">
                    <i data-lucide="help-circle" class="w-4 h-4 text-amber-400"></i>
                    <span class="hidden md:inline">แบบทดสอบ</span>
                    <span class="md:hidden">Quiz</span>
                </button>

                <!-- 5. E-Certificate -->
                <button onclick="switchMainView('certificate')" id="nav-btn-certificate" class="nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition">
                    <i data-lucide="award" class="w-4 h-4 text-amber-300"></i>
                    <span class="hidden md:inline">เกียรติบัตร</span>
                    <span class="md:hidden">ใบประกาศฯ</span>
                </button>
            </nav>

            <!-- Right Companion Links & Tools -->
            <div class="flex items-center gap-1.5 sm:gap-2 shrink-0">
                <!-- Companion Tools Dropdown/Links -->
                <div class="relative group">
                    <button class="flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-xs font-heading font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition" title="สื่อการสอนประกอบหลักสูตร">
                        <i data-lucide="layers" class="w-3.5 h-3.5 text-amber-400"></i>
                        <span class="hidden sm:inline">สื่อประกอบ</span>
                        <i data-lucide="chevron-down" class="w-3 h-3 text-slate-400"></i>
                    </button>
                    <div class="absolute right-0 mt-1 w-52 bg-slate-900 border border-slate-700 rounded-xl shadow-xl py-1.5 hidden group-hover:block z-50">
                        <a href="slides.html" target="_blank" class="flex items-center gap-2 px-3 py-2 text-xs text-slate-200 hover:bg-slate-800 hover:text-amber-300 transition">
                            <i data-lucide="presentation" class="w-4 h-4 text-amber-400"></i>
                            <span>สไลด์บรรยาย (Slides 16:9)</span>
                        </a>
                        <a href="trainer_guide.html" target="_blank" class="flex items-center gap-2 px-3 py-2 text-xs text-slate-200 hover:bg-slate-800 hover:text-amber-300 transition">
                            <i data-lucide="book-open-check" class="w-4 h-4 text-amber-400"></i>
                            <span>คู่มือวิทยากร (Trainer Guide)</span>
                        </a>
                        <a href="handout.html" target="_blank" class="flex items-center gap-2 px-3 py-2 text-xs text-slate-200 hover:bg-slate-800 hover:text-emerald-400 transition">
                            <i data-lucide="file-text" class="w-4 h-4 text-emerald-400"></i>
                            <span>เอกสารสรุปฝึกอบรม (Handout)</span>
                        </a>
                    </div>
                </div>

                <!-- Presentation Mode Toggle (Instructor) -->
                <button onclick="togglePresentationMode()" id="presentation-btn" title="โหมดบรรยายสำหรับวิทยากร (ขยายตัวอักษร)" class="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 transition">
                    <i data-lucide="projector" class="w-4 h-4"></i>
                </button>
            </div>
        </div>
    </header>"""

    html = re.sub(old_header_pattern, new_header, html, flags=re.DOTALL)

    # 3. ADD SAVE BUTTON IN VIEW-BUILDER
    # In view-builder, right under copy button:
    old_copy_btn = """                                    <button onclick="copyGeneratedPrompt()" class="w-full py-3 px-4 bg-amber-500 hover:bg-amber-400 text-slate-950 font-heading font-bold rounded-xl shadow-lg transition flex items-center justify-center gap-2">
                                        <i data-lucide="copy" class="w-4 h-4"></i>
                                        <span>คัดลอกคำสั่ง Prompt นี้</span>
                                    </button>"""
    new_builder_btns = """                                    <button onclick="copyGeneratedPrompt()" class="w-full py-2.5 px-4 bg-amber-500 hover:bg-amber-400 text-slate-950 font-heading font-bold rounded-xl shadow-md transition flex items-center justify-center gap-2">
                                        <i data-lucide="copy" class="w-4 h-4"></i>
                                        <span>คัดลอกคำสั่ง Prompt นี้</span>
                                    </button>
                                    <button onclick="saveCurrentBuilderToPortfolio()" class="w-full py-2.5 px-4 bg-emerald-600 hover:bg-emerald-500 text-white font-heading font-semibold rounded-xl shadow-md transition flex items-center justify-center gap-2">
                                        <i data-lucide="bookmark-plus" class="w-4 h-4"></i>
                                        <span>บันทึกเข้าแฟ้มผลงานของฉัน (Save to Portfolio)</span>
                                    </button>"""
    html = html.replace(old_copy_btn, new_builder_btns)

    # 4. INSERT VIEW 4 (PORTFOLIO) AND VIEW 5 (CERTIFICATE) BEFORE </main>
    new_views_html = """
                <!-- VIEW 4: PARTICIPANT WORKSPACE & PORTFOLIO -->
                <div id="view-portfolio" class="space-y-6 hidden">
                    <!-- Banner -->
                    <div class="bg-gradient-to-r from-slate-900 via-indigo-950 to-blue-900 rounded-2xl p-6 sm:p-8 text-white shadow-lg relative overflow-hidden">
                        <div class="relative z-10 space-y-3">
                            <div class="flex flex-wrap items-center justify-between gap-3">
                                <span class="px-3 py-1 rounded-full text-xs font-heading font-semibold bg-emerald-400 text-slate-950">
                                    แฟ้มผลงานและสมุดงานประจำตัว (My Workspace & Portfolio)
                                </span>
                                <div class="flex items-center gap-2">
                                    <button onclick="switchMainView('workshop')" class="text-xs font-heading bg-white/10 hover:bg-white/20 text-white px-3 py-1.5 rounded-lg flex items-center gap-1.5 transition">
                                        <i data-lucide="arrow-left" class="w-4 h-4"></i>
                                        <span>กลับสู่บทเรียน</span>
                                    </button>
                                    <button onclick="switchMainView('certificate')" class="text-xs font-heading bg-amber-500 hover:bg-amber-400 text-slate-950 font-semibold px-3 py-1.5 rounded-lg flex items-center gap-1.5 transition shadow-sm">
                                        <i data-lucide="award" class="w-4 h-4"></i>
                                        <span>ดูใบประกาศนียบัตร</span>
                                    </button>
                                </div>
                            </div>
                            <h2 class="text-2xl sm:text-3xl font-heading font-bold">
                                แฟ้มผลงานคำสั่ง Prompt และบันทึกการเรียนรู้
                            </h2>
                            <p class="text-slate-300 text-sm sm:text-base max-w-3xl leading-relaxed">
                                บันทึกและจัดเก็บคำสั่ง Prompt ที่ท่านฝึกปฏิบัติ, ตรวจสอบความก้าวหน้าการเรียนรู้ตลอดหลักสูตร ๗ หัวข้อ และพิมพ์สรุปเป็นแฟ้มผลงานดิจิทัลสำหรับนำไปใช้งานจริงใน อปท. ของท่าน
                            </p>
                        </div>
                    </div>

                    <!-- Profile & Metrics Row -->
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                        <!-- Profile Card (5 Cols) -->
                        <div class="lg:col-span-5 bg-white rounded-2xl p-6 border border-slate-200 shadow-xs space-y-4">
                            <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                                <h3 class="font-heading font-bold text-slate-900 flex items-center gap-2 text-base">
                                    <i data-lucide="user-check" class="w-5 h-5 text-indigo-600"></i>
                                    <span>ข้อมูลผู้เข้าอบรม (สำหรับใบประกาศฯ)</span>
                                </h3>
                                <span class="text-[11px] font-heading px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200">บันทึกอัตโนมัติ</span>
                            </div>

                            <form id="portfolio-profile-form" onsubmit="event.preventDefault(); saveProfileFromForm();" class="space-y-3.5">
                                <div>
                                    <label class="block text-xs font-heading font-semibold text-slate-700 mb-1">คำนำหน้า-ชื่อ-นามสกุล *</label>
                                    <input type="text" id="prof-name" oninput="saveProfileFromForm()" placeholder="เช่น นายสมศักดิ์ มุ่งมั่นพัฒนา" class="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                </div>
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                    <div>
                                        <label class="block text-xs font-heading font-semibold text-slate-700 mb-1">ตำแหน่ง *</label>
                                        <input type="text" id="prof-position" oninput="saveProfileFromForm()" placeholder="เช่น นักจัดการงานทั่วไปชำนาญการ" class="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                    </div>
                                    <div>
                                        <label class="block text-xs font-heading font-semibold text-slate-700 mb-1">ฝ่าย / กอง</label>
                                        <input type="text" id="prof-dept" oninput="saveProfileFromForm()" placeholder="เช่น สำนักปลัดเทศบาล" class="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-xs font-heading font-semibold text-slate-700 mb-1">องค์กรปกครองส่วนท้องถิ่น (อปท.) *</label>
                                    <input type="text" id="prof-org" oninput="saveProfileFromForm()" placeholder="เช่น เทศบาลตำบลเมืองใหม่ จ.เชียงใหม่" class="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                </div>
                                <div class="pt-1 flex items-center justify-between">
                                    <p class="text-[11px] text-slate-400">ข้อมูลนี้จะถูกนำไปแสดงบนใบประกาศนียบัตรออนไลน์ทันที</p>
                                    <button type="button" onclick="saveProfileFromForm(true)" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-heading font-semibold rounded-lg transition shadow-xs">
                                        บันทึกข้อมูล
                                    </button>
                                </div>
                            </form>
                        </div>

                        <!-- Learning Metrics & Action Checklist (7 Cols) -->
                        <div class="lg:col-span-7 bg-white rounded-2xl p-6 border border-slate-200 shadow-xs space-y-4">
                            <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                                <h3 class="font-heading font-bold text-slate-900 flex items-center gap-2 text-base">
                                    <i data-lucide="gauge" class="w-5 h-5 text-amber-500"></i>
                                    <span>สถานะความก้าวหน้าและการสำเร็จหลักสูตร</span>
                                </h3>
                                <button onclick="printPortfolio()" class="text-xs font-heading text-indigo-600 hover:text-indigo-800 flex items-center gap-1 font-semibold">
                                    <i data-lucide="printer" class="w-3.5 h-3.5"></i> พิมพ์สรุปแฟ้มผลงาน (PDF)
                                </button>
                            </div>

                            <!-- 3 Stat Badges -->
                            <div class="grid grid-cols-3 gap-3">
                                <div class="bg-indigo-50/70 border border-indigo-100 rounded-xl p-3 text-center">
                                    <div class="text-xs font-heading text-indigo-700">บทเรียนที่สำเร็จ</div>
                                    <div id="stat-modules-done" class="text-2xl font-bold font-heading text-indigo-950 mt-0.5">0 / 7</div>
                                    <div class="text-[10px] text-indigo-600 mt-0.5">ครบทั้ง 7 หัวข้อ</div>
                                </div>
                                <div class="bg-emerald-50/70 border border-emerald-100 rounded-xl p-3 text-center">
                                    <div class="text-xs font-heading text-emerald-700">แบบทดสอบ Post-Test</div>
                                    <div id="stat-quiz-score" class="text-2xl font-bold font-heading text-emerald-950 mt-0.5">- / 5</div>
                                    <div id="stat-quiz-status" class="text-[10px] text-emerald-600 mt-0.5">ยังไม่ได้ทำแบบทดสอบ</div>
                                </div>
                                <div class="bg-amber-50/70 border border-amber-100 rounded-xl p-3 text-center">
                                    <div class="text-xs font-heading text-amber-800">ผลงาน Prompt สะสม</div>
                                    <div id="stat-prompts-count" class="text-2xl font-bold font-heading text-amber-950 mt-0.5">0</div>
                                    <div class="text-[10px] text-amber-700 mt-0.5">ชิ้นงานในแฟ้ม</div>
                                </div>
                            </div>

                            <!-- Modules Checklist Accordion -->
                            <div class="pt-1">
                                <div class="text-xs font-heading font-semibold text-slate-700 mb-2 flex items-center justify-between">
                                    <span>เช็คลิสต์ ๗ หัวข้อการอบรม:</span>
                                    <span class="text-[11px] text-slate-400">คลิกที่หัวข้อเพื่อเปิดบทเรียน</span>
                                </div>
                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs" id="portfolio-modules-checklist">
                                    <!-- Rendered dynamically via JS -->
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Saved Prompts Library Section -->
                    <div class="bg-white rounded-2xl p-6 sm:p-8 border border-slate-200 shadow-xs space-y-6">
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-4">
                            <div>
                                <h3 class="font-heading font-bold text-slate-900 text-lg flex items-center gap-2">
                                    <i data-lucide="bookmark-check" class="w-5 h-5 text-emerald-600"></i>
                                    <span>คลังคำสั่ง Prompt ประจำตัวของฉัน</span>
                                    <span id="portfolio-count-badge" class="px-2 py-0.5 rounded-full bg-slate-100 text-slate-700 text-xs">0 ชิ้น</span>
                                </h3>
                                <p class="text-xs text-slate-500 mt-0.5">คำสั่ง Prompt ทั้งหมดที่ท่านบันทึกจาก Workshop หรือเครื่องมือสร้าง Prompt</p>
                            </div>

                            <div class="flex flex-wrap items-center gap-2">
                                <button onclick="switchMainView('builder')" class="px-3 py-1.5 bg-amber-500 hover:bg-amber-400 text-slate-950 text-xs font-heading font-bold rounded-xl flex items-center gap-1.5 transition shadow-xs">
                                    <i data-lucide="plus" class="w-3.5 h-3.5"></i>
                                    <span>สร้าง Prompt ใหม่</span>
                                </button>
                                <button onclick="loadSamplePortfolioPrompts()" class="px-3 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-heading font-medium rounded-xl flex items-center gap-1.5 transition">
                                    <i data-lucide="download" class="w-3.5 h-3.5"></i>
                                    <span>โหลดตัวอย่างแม่แบบ</span>
                                </button>
                            </div>
                        </div>

                        <!-- Filter & Search Bar -->
                        <div class="flex flex-col sm:flex-row items-center justify-between gap-3">
                            <div class="flex items-center gap-1.5 overflow-x-auto w-full sm:w-auto pb-1" id="portfolio-category-filters">
                                <button onclick="filterPortfolio('all')" class="cat-filter-btn px-3 py-1 rounded-lg text-xs font-heading font-semibold bg-slate-900 text-white transition">ทั้งหมด</button>
                                <button onclick="filterPortfolio('หนังสือราชการ')" class="cat-filter-btn px-3 py-1 rounded-lg text-xs font-heading font-medium bg-slate-100 hover:bg-slate-200 text-slate-700 transition">หนังสือราชการ</button>
                                <button onclick="filterPortfolio('แผนและงบประมาณ')" class="cat-filter-btn px-3 py-1 rounded-lg text-xs font-heading font-medium bg-slate-100 hover:bg-slate-200 text-slate-700 transition">แผน/งบประมาณ</button>
                                <button onclick="filterPortfolio('วิเคราะห์ข้อมูล')" class="cat-filter-btn px-3 py-1 rounded-lg text-xs font-heading font-medium bg-slate-100 hover:bg-slate-200 text-slate-700 transition">วิเคราะห์ข้อมูล</button>
                                <button onclick="filterPortfolio('ประชาสัมพันธ์')" class="cat-filter-btn px-3 py-1 rounded-lg text-xs font-heading font-medium bg-slate-100 hover:bg-slate-200 text-slate-700 transition">ประชาสัมพันธ์</button>
                            </div>
                            <div class="relative w-full sm:w-64">
                                <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2"></i>
                                <input type="text" id="portfolio-search" oninput="renderPortfolioList()" placeholder="ค้นหาในแฟ้มผลงาน..." class="w-full pl-9 pr-3 py-1.5 bg-slate-50 border border-slate-200 rounded-xl text-xs focus:ring-2 focus:ring-blue-500 focus:outline-none">
                            </div>
                        </div>

                        <!-- Prompts Grid Container -->
                        <div id="portfolio-prompts-container" class="space-y-4">
                            <!-- Rendered dynamically via JS -->
                        </div>
                    </div>
                </div>

                <!-- VIEW 5: ROYAL THAI GOVERNMENT E-CERTIFICATE -->
                <div id="view-certificate" class="space-y-6 hidden">
                    <!-- Top Action Bar -->
                    <div class="bg-slate-900 text-white rounded-2xl p-6 sm:p-7 shadow-lg flex flex-col md:flex-row md:items-center justify-between gap-4">
                        <div class="space-y-1">
                            <div class="flex items-center gap-2">
                                <span class="px-2.5 py-0.5 rounded-full text-xs font-heading font-semibold bg-amber-400 text-slate-950">
                                    ใบประกาศนียบัตรออนไลน์ (E-Certificate)
                                </span>
                                <span id="cert-status-badge" class="px-2.5 py-0.5 rounded-full text-xs font-heading font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                                    ผ่านการประเมินแล้ว
                                </span>
                            </div>
                            <h2 class="text-xl sm:text-2xl font-heading font-bold text-white">
                                ใบประกาศนียบัตรรับรองการสำเร็จหลักสูตร
                            </h2>
                            <p class="text-xs sm:text-sm text-slate-300">
                                พิมพ์เป็นเอกสารรับรอง A4 แนวนอน หรือบันทึกเป็นไฟล์ PDF คุณภาพสูงเพื่อเป็นหลักฐานการพัฒนาตนเอง
                            </p>
                        </div>

                        <div class="flex flex-wrap items-center gap-2">
                            <button onclick="printCertificate()" class="px-5 py-2.5 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-heading font-bold text-sm rounded-xl shadow-lg flex items-center gap-2 transition">
                                <i data-lucide="printer" class="w-4 h-4"></i>
                                <span>พิมพ์เกียรติบัตร / บันทึก PDF (A4)</span>
                            </button>
                            <button onclick="openEditProfileModal()" class="px-3.5 py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-heading font-medium rounded-xl border border-slate-700 flex items-center gap-1.5 transition">
                                <i data-lucide="edit-3" class="w-3.5 h-3.5 text-amber-400"></i>
                                <span>แก้ไขชื่อ-ตำแหน่ง</span>
                            </button>
                            <button onclick="switchMainView('portfolio')" class="px-3.5 py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-heading font-medium rounded-xl border border-slate-700 flex items-center gap-1.5 transition">
                                <i data-lucide="folder-kanban" class="w-3.5 h-3.5 text-emerald-400"></i>
                                <span>กลับสู่แฟ้มผลงาน</span>
                            </button>
                        </div>
                    </div>

                    <!-- Printing Instruction Tip -->
                    <div class="no-print bg-amber-50 border border-amber-200 rounded-xl p-3.5 text-xs text-amber-900 flex items-center gap-3">
                        <i data-lucide="info" class="w-5 h-5 text-amber-600 shrink-0"></i>
                        <p class="leading-relaxed">
                            <strong>คำแนะนำการพิมพ์:</strong> เมื่อกดปุ่มพิมพ์ ให้เลือกปลายทางเป็น <strong>"Save as PDF" (บันทึกเป็น PDF)</strong>, การวางแนว: <strong>"แนวนอน (Landscape)"</strong>, ขนาดกระดาษ: <strong>A4</strong> และอย่าลืมติ๊กเปิดตัวเลือก <strong>"Background graphics (กราฟิกพื้นหลัง)"</strong> เพื่อให้ลายกรอบทองและสีตราประทับแสดงผลครบถ้วนคมชัด
                        </p>
                    </div>

                    <!-- CERTIFICATE CONTAINER (A4 LANDSCAPE: 297mm x 210mm) -->
                    <div class="overflow-x-auto pb-6">
                        <div id="certificate-frame" class="w-full max-w-[1020px] mx-auto bg-[#faf8f5] text-slate-900 p-8 sm:p-12 shadow-2xl rounded-2xl relative cert-outer-border cert-watermark transition-all">
                            
                            <!-- Inner Gold Double Border -->
                            <div class="cert-inner-border p-6 sm:p-8 h-full flex flex-col justify-between relative bg-white/70 backdrop-blur-xs">
                                
                                <!-- 4 Corner Ornaments (SVG) -->
                                <div class="absolute -top-3 -left-3 w-8 h-8 text-amber-600 pointer-events-none">
                                    <svg viewBox="0 0 100 100" fill="currentColor"><path d="M0 0 L100 0 L100 20 L20 20 L20 100 L0 100 Z M30 30 L80 30 L80 40 L40 40 L40 80 L30 80 Z"></path></svg>
                                </div>
                                <div class="absolute -top-3 -right-3 w-8 h-8 text-amber-600 pointer-events-none rotate-90">
                                    <svg viewBox="0 0 100 100" fill="currentColor"><path d="M0 0 L100 0 L100 20 L20 20 L20 100 L0 100 Z M30 30 L80 30 L80 40 L40 40 L40 80 L30 80 Z"></path></svg>
                                </div>
                                <div class="absolute -bottom-3 -left-3 w-8 h-8 text-amber-600 pointer-events-none -rotate-90">
                                    <svg viewBox="0 0 100 100" fill="currentColor"><path d="M0 0 L100 0 L100 20 L20 20 L20 100 L0 100 Z M30 30 L80 30 L80 40 L40 40 L40 80 L30 80 Z"></path></svg>
                                </div>
                                <div class="absolute -bottom-3 -right-3 w-8 h-8 text-amber-600 pointer-events-none rotate-180">
                                    <svg viewBox="0 0 100 100" fill="currentColor"><path d="M0 0 L100 0 L100 20 L20 20 L20 100 L0 100 Z M30 30 L80 30 L80 40 L40 40 L40 80 L30 80 Z"></path></svg>
                                </div>

                                <!-- Header: Emblem & Institutions -->
                                <div class="text-center space-y-2">
                                    <!-- Official Garuda / Royal Crest SVG -->
                                    <div class="flex justify-center mb-1">
                                        <div class="w-16 h-16 sm:w-20 sm:h-20 flex items-center justify-center">
                                            <svg viewBox="0 0 120 120" class="w-full h-full text-amber-600 drop-shadow-sm" fill="currentColor">
                                                <!-- Stylized Royal Crest / Emblem Vector -->
                                                <circle cx="60" cy="60" r="54" fill="none" stroke="#d97706" stroke-width="2.5" stroke-dasharray="4 2"></circle>
                                                <circle cx="60" cy="60" r="48" fill="none" stroke="#1e3a8a" stroke-width="1.5"></circle>
                                                <!-- Crown & Garuda Silhouette -->
                                                <path d="M60 16 L65 28 L78 28 L68 36 L72 48 L60 40 L48 48 L52 36 L42 28 L55 28 Z" fill="#d97706"></path>
                                                <path d="M60 42 C45 42 35 55 24 62 C34 65 44 60 52 56 C52 75 42 85 34 94 C46 92 56 86 60 76 C64 86 74 92 86 94 C78 85 68 75 68 56 C76 60 86 65 96 62 C85 55 75 42 60 42 Z" fill="#b45309"></path>
                                                <circle cx="60" cy="60" r="6" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"></circle>
                                            </svg>
                                        </div>
                                    </div>

                                    <div class="text-[12px] sm:text-sm font-heading font-semibold text-slate-600 tracking-wider uppercase">
                                        สถาบันพัฒนาองค์กรปกครองส่วนท้องถิ่นดิจิทัล ร่วมกับ ศูนย์นวัตกรรมปัญญาประดิษฐ์ภาครัฐ
                                    </div>
                                    <h1 class="text-xl sm:text-2xl md:text-3xl font-heading font-extrabold text-blue-950 tracking-normal pt-1">
                                        ใบประกาศนียบัตรฉบับนี้ให้ไว้เพื่อแสดงว่า
                                    </h1>
                                </div>

                                <!-- Body: Recipient Name & Details -->
                                <div class="text-center py-4 sm:py-6 space-y-3">
                                    <div class="relative inline-block px-8 py-1">
                                        <div id="cert-name-display" class="font-heading font-bold text-2xl sm:text-3xl md:text-4xl text-slate-900 border-b-2 border-amber-500 pb-2 inline-block min-w-[280px]">
                                            นายสมศักดิ์ มุ่งมั่นพัฒนา
                                        </div>
                                    </div>
                                    <div id="cert-role-org-display" class="text-sm sm:text-base md:text-lg text-slate-700 font-medium">
                                        ตำแหน่ง นักจัดการงานทั่วไปชำนาญการ สังกัด เทศบาลตำบลเมืองใหม่ จ.เชียงใหม่
                                    </div>

                                    <div class="text-xs sm:text-sm text-slate-600 font-heading pt-2">
                                        ได้สำเร็จการฝึกอบรมเชิงปฏิบัติการหลักสูตร
                                    </div>

                                    <div class="font-heading font-extrabold text-lg sm:text-xl md:text-2xl text-blue-900 tracking-tight max-w-2xl mx-auto leading-snug">
                                        "การประยุกต์ใช้ปัญญาประดิษฐ์ (AI) เพื่อยกระดับการทำงานขององค์กรปกครองส่วนท้องถิ่น (อปท.)"
                                    </div>

                                    <p class="text-[11px] sm:text-xs text-slate-600 max-w-2xl mx-auto leading-relaxed">
                                        ครอบคลุมการร่างหนังสือราชการตามระเบียบงานสารบรรณ พ.ศ. ๒๕๒๖ (ครบทั้ง ๖ ประเภท), การจัดทำแผนยุทธศาสตร์และวิเคราะห์งบประมาณท้องถิ่น, การบริการประชาชน และหลักจริยธรรมความปลอดภัยตาม พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล (PDPA)
                                    </p>
                                    <div class="text-[11px] sm:text-xs font-semibold text-slate-500">
                                        ระยะเวลาการฝึกอบรม ๖ ชั่วโมงการเรียนรู้เชิงปฏิบัติการ (ภาคบรรยายและฝึกปฏิบัติการ)
                                    </div>
                                </div>

                                <!-- Footer: Signatures & Verification -->
                                <div class="pt-4 border-t border-amber-200/60 flex items-end justify-between gap-4 text-center">
                                    <!-- Left Signature -->
                                    <div class="w-1/3 space-y-1">
                                        <div class="h-12 flex items-center justify-center">
                                            <svg class="h-10 text-blue-900" viewBox="0 0 160 50" fill="none" stroke="currentColor" stroke-width="2">
                                                <path d="M10 35 C 30 10, 50 45, 70 20 S 110 5, 130 30 S 150 15, 155 25" stroke-linecap="round"></path>
                                            </svg>
                                        </div>
                                        <div class="text-xs sm:text-sm font-heading font-bold text-slate-800">(รองศาสตราจารย์ ดร.ปัญญา ประชานุกูล)</div>
                                        <div class="text-[10px] sm:text-xs text-slate-600">ประธานสถาบันพัฒนาองค์กรปกครองส่วนท้องถิ่นดิจิทัล</div>
                                    </div>

                                    <!-- Center Seal / Crest -->
                                    <div class="w-1/3 flex flex-col items-center justify-center space-y-1">
                                        <!-- Gold Foil Seal Medallion -->
                                        <div class="w-16 h-16 rounded-full cert-gold-foil shadow-md flex items-center justify-center border-2 border-amber-300 p-1">
                                            <div class="w-full h-full rounded-full border border-dashed border-amber-900/60 flex flex-col items-center justify-center text-[7px] font-bold text-amber-950 uppercase tracking-tighter">
                                                <span>OFFICIAL</span>
                                                <span class="text-[9px] font-extrabold">2026</span>
                                                <span>CERTIFIED</span>
                                            </div>
                                        </div>
                                        <div class="text-[10px] text-slate-500 font-heading">
                                            ให้ไว้ ณ วันที่ <span id="cert-date-display">๑ พฤศจิกายน ๒๕๖๙</span>
                                        </div>
                                        <div class="text-[9px] font-mono text-slate-400 bg-slate-100 px-2 py-0.5 rounded border border-slate-200">
                                            รหัส: <span id="cert-id-display">AI-LG-2569-8B74</span>
                                        </div>
                                    </div>

                                    <!-- Right Signature -->
                                    <div class="w-1/3 space-y-1">
                                        <div class="h-12 flex items-center justify-center">
                                            <svg class="h-10 text-blue-900" viewBox="0 0 160 50" fill="none" stroke="currentColor" stroke-width="2">
                                                <path d="M15 30 C 40 40, 60 10, 80 35 S 120 15, 140 25" stroke-linecap="round"></path>
                                                <line x1="25" y1="42" x2="135" y2="42" stroke-dasharray="3 3"></line>
                                            </svg>
                                        </div>
                                        <div class="text-xs sm:text-sm font-heading font-bold text-slate-800">(นายวิทยา ก้องเกียรติวงศ์)</div>
                                        <div class="text-[10px] sm:text-xs text-slate-600">วิทยากรผู้เชี่ยวชาญด้านปัญญาประดิษฐ์ภาครัฐและ อปท.</div>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
"""

    html = html.replace('            </main>', new_views_html + '\n            </main>')

    # 5. UPDATE JAVASCRIPT: switchMainView, submitQuiz, and new Portfolio & Certificate logic
    # Find existing switchMainView function
    old_switch_main_view = """        function switchMainView(viewName) {
            const views = ['workshop', 'builder', 'quiz'];
            views.forEach(v => {
                const el = document.getElementById(`view-${v}`);
                if (v === viewName) {
                    el.classList.remove('hidden');
                } else {
                    el.classList.add('hidden');
                }
            });
            window.scrollTo({ top: 0, behavior: 'smooth' });
            lucide.createIcons();
        }"""

    new_switch_main_view = """        function switchMainView(viewName) {
            const views = ['workshop', 'builder', 'portfolio', 'quiz', 'certificate'];
            views.forEach(v => {
                const el = document.getElementById(`view-${v}`);
                if (el) {
                    if (v === viewName) {
                        el.classList.remove('hidden');
                    } else {
                        el.classList.add('hidden');
                    }
                }
            });

            // Adjust navigation tab styles
            views.forEach(v => {
                const btn = document.getElementById(`nav-btn-${v}`);
                if (btn) {
                    if (v === viewName) {
                        btn.className = "nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-bold transition bg-amber-500 text-slate-950 shadow-sm";
                    } else {
                        btn.className = "nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition";
                    }
                }
            });

            // Manage sidebar: hide sidebar on desktop for builder, portfolio, quiz, certificate to provide full width
            const sidebar = document.getElementById('sidebar');
            if (sidebar) {
                if (viewName === 'workshop') {
                    sidebar.classList.remove('lg:hidden');
                } else {
                    sidebar.classList.add('lg:hidden');
                }
            }

            // Sync UIs if switching
            if (viewName === 'portfolio') {
                updatePortfolioUI();
            } else if (viewName === 'certificate') {
                updateCertificateUI();
            }

            window.scrollTo({ top: 0, behavior: 'smooth' });
            lucide.createIcons();
        }"""
    html = html.replace(old_switch_main_view, new_switch_main_view)

    # Replace submitQuiz with enhanced version
    old_submit_quiz = """        function submitQuiz() {
            let score = 0;
            quizQuestions.forEach((item, qIdx) => {
                const expEl = document.getElementById(`quiz-exp-${qIdx}`);
                const selected = userQuizAnswers[qIdx];
                expEl.classList.remove('hidden');

                if (selected === item.correct) {
                    score++;
                    expEl.className = "p-3.5 rounded-xl text-xs leading-relaxed bg-emerald-100/80 text-emerald-950 border border-emerald-300";
                    expEl.innerHTML = `<strong>ถูกต้อง!</strong> ${item.explanation}`;
                } else {
                    expEl.className = "p-3.5 rounded-xl text-xs leading-relaxed bg-rose-100/80 text-rose-950 border border-rose-300";
                    expEl.innerHTML = `<strong>คำตอบที่ถูกต้องคือ: ${item.options[item.correct]}</strong><br>${item.explanation}`;
                }
            });

            const banner = document.getElementById('quiz-score-banner');
            banner.classList.remove('hidden');
            banner.innerHTML = `คะแนนของคุณ: <span class="text-lg font-bold text-emerald-700">${score} / ${quizQuestions.length} คะแนน</span> (${Math.round((score/quizQuestions.length)*100)}%) — ${score >= 4 ? 'ยอดเยี่ยม! คุณพร้อมนำ AI ไปประยุกต์ใช้ในหน่วยงานอย่างปลอดภัยแล้ว' : 'แนะนำให้ทบทวนเนื้อหาโครงสร้าง Prompt และข้อควรระวัง PDPA อีกครั้ง'}`;
            showToast(`ตรวจคำตอบเรียบร้อย! คุณได้ ${score}/${quizQuestions.length} คะแนน`);
        }"""

    new_submit_quiz = """        function submitQuiz() {
            let score = 0;
            quizQuestions.forEach((item, qIdx) => {
                const expEl = document.getElementById(`quiz-exp-${qIdx}`);
                const selected = userQuizAnswers[qIdx];
                expEl.classList.remove('hidden');

                if (selected === item.correct) {
                    score++;
                    expEl.className = "p-3.5 rounded-xl text-xs leading-relaxed bg-emerald-100/80 text-emerald-950 border border-emerald-300";
                    expEl.innerHTML = `<strong>ถูกต้อง!</strong> ${item.explanation}`;
                } else {
                    expEl.className = "p-3.5 rounded-xl text-xs leading-relaxed bg-rose-100/80 text-rose-950 border border-rose-300";
                    expEl.innerHTML = `<strong>คำตอบที่ถูกต้องคือ: ${item.options[item.correct]}</strong><br>${item.explanation}`;
                }
            });

            // Update participant profile state
            participantProfile.quizScore = score;
            participantProfile.quizTotal = quizQuestions.length;
            participantProfile.quizPassed = (score >= 3);
            saveParticipantProfile();

            const banner = document.getElementById('quiz-score-banner');
            banner.classList.remove('hidden');
            const pct = Math.round((score / quizQuestions.length) * 100);
            const passed = score >= 3;

            banner.innerHTML = `
                <div class="flex flex-col md:flex-row items-center justify-between gap-4 p-4 rounded-xl ${passed ? 'bg-emerald-50 border border-emerald-200 text-emerald-950' : 'bg-amber-50 border border-amber-200 text-amber-950'}">
                    <div>
                        <div class="text-xs uppercase tracking-wider font-semibold font-heading ${passed ? 'text-emerald-700' : 'text-amber-700'}">ผลการประเมินองค์ความรู้ (Post-Test)</div>
                        <div class="text-lg font-bold font-heading mt-0.5">
                            คะแนนของคุณ: <span class="text-2xl ${passed ? 'text-emerald-700' : 'text-amber-700'}">${score} / ${quizQuestions.length}</span> คะแนน (${pct}%)
                        </div>
                        <p class="text-xs text-slate-600 mt-1">
                            ${passed ? '🎉 ยอดเยี่ยม! ท่านผ่านเกณฑ์การประเมินองค์ความรู้ พร้อมรับใบประกาศนียบัตรออนไลน์' : 'แนะนำให้ทบทวนเนื้อหาโครงสร้าง Prompt และทำแบบทดสอบใหม่อีกครั้งเพื่อปรับปรุงคะแนน'}
                        </p>
                    </div>
                    ${passed ? `
                        <button onclick="switchMainView('certificate')" class="px-5 py-2.5 rounded-xl bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-heading font-bold text-sm shadow-md flex items-center gap-2 shrink-0 transition">
                            <i data-lucide="award" class="w-5 h-5"></i>
                            <span>รับใบประกาศนียบัตรออนไลน์ (E-Certificate)</span>
                        </button>
                    ` : ''}
                </div>
            `;
            showToast(`ตรวจคำตอบเรียบร้อย! คุณได้ ${score}/${quizQuestions.length} คะแนน`);
            updatePortfolioUI();
            updateCertificateUI();
            lucide.createIcons();
        }"""
    html = html.replace(old_submit_quiz, new_submit_quiz)

    # 6. ADD SAVE TO PORTFOLIO BUTTON IN PROMPTS LIST
    # Search for copyTextDecode in prompt-card
    old_prompt_action = """                            <button onclick="copyTextDecode('${encodedPrompt}')" class="text-xs bg-amber-500 hover:bg-amber-400 text-slate-950 font-heading font-semibold px-3 py-1 rounded-lg flex items-center gap-1 transition shadow-xs">
                                <i data-lucide="copy" class="w-3.5 h-3.5"></i>
                                <span>คัดลอก Prompt</span>
                            </button>"""
    new_prompt_action = """                            <button onclick="saveWorkshopPromptToPortfolio(${idx})" class="text-xs bg-emerald-600 hover:bg-emerald-500 text-white font-heading px-2.5 py-1 rounded-lg flex items-center gap-1 transition" title="บันทึกเข้าแฟ้มผลงานของฉัน">
                                <i data-lucide="bookmark-plus" class="w-3.5 h-3.5"></i>
                                <span class="hidden sm:inline">เก็บเข้าแฟ้ม</span>
                            </button>
                            <button onclick="copyTextDecode('${encodedPrompt}')" class="text-xs bg-amber-500 hover:bg-amber-400 text-slate-950 font-heading font-semibold px-3 py-1 rounded-lg flex items-center gap-1 transition shadow-xs">
                                <i data-lucide="copy" class="w-3.5 h-3.5"></i>
                                <span>คัดลอก Prompt</span>
                            </button>"""
    html = html.replace(old_prompt_action, new_prompt_action)

    # 7. ADD FULL PORTFOLIO & CERTIFICATE JS LOGIC BEFORE initApp
    full_portfolio_cert_js = """
        // ==========================================
        // 9. PARTICIPANT PORTFOLIO & CERTIFICATE SYSTEM
        // ==========================================
        let participantProfile = {
            fullName: 'นายสมศักดิ์ มุ่งมั่นพัฒนา',
            position: 'นักจัดการงานทั่วไปชำนาญการ',
            department: 'สำนักปลัดเทศบาล',
            organization: 'เทศบาลตำบลเมืองใหม่ จ.เชียงใหม่',
            quizScore: null,
            quizTotal: 5,
            quizPassed: false,
            certificateId: 'AI-LG-2569-' + Math.floor(1000 + Math.random() * 9000),
            issueDateThai: '๑ พฤศจิกายน ๒๕๖๙',
            savedPrompts: []
        };

        function loadParticipantProfile() {
            try {
                const saved = localStorage.getItem('ai_lg_participant_data_v2');
                if (saved) {
                    const parsed = JSON.parse(saved);
                    participantProfile = { ...participantProfile, ...parsed };
                }
            } catch (e) {
                console.error('Failed to load profile', e);
            }

            // Sync Form Inputs
            const nameEl = document.getElementById('prof-name');
            const posEl = document.getElementById('prof-position');
            const deptEl = document.getElementById('prof-dept');
            const orgEl = document.getElementById('prof-org');

            if (nameEl) nameEl.value = participantProfile.fullName;
            if (posEl) posEl.value = participantProfile.position;
            if (deptEl) deptEl.value = participantProfile.department;
            if (orgEl) orgEl.value = participantProfile.organization;

            updatePortfolioUI();
            updateCertificateUI();
        }

        function saveParticipantProfile() {
            try {
                localStorage.setItem('ai_lg_participant_data_v2', JSON.stringify(participantProfile));
            } catch (e) {
                console.error('Failed to save profile', e);
            }
        }

        function saveProfileFromForm(showNotification = false) {
            const nameEl = document.getElementById('prof-name');
            const posEl = document.getElementById('prof-position');
            const deptEl = document.getElementById('prof-dept');
            const orgEl = document.getElementById('prof-org');

            if (nameEl && nameEl.value.trim()) participantProfile.fullName = nameEl.value.trim();
            if (posEl && posEl.value.trim()) participantProfile.position = posEl.value.trim();
            if (deptEl) participantProfile.department = deptEl.value.trim();
            if (orgEl && orgEl.value.trim()) participantProfile.organization = orgEl.value.trim();

            saveParticipantProfile();
            updateCertificateUI();
            if (showNotification) {
                showToast('บันทึกข้อมูลส่วนตัวและอัปเดตใบประกาศนียบัตรเรียบร้อยแล้ว!');
            }
        }

        function saveWorkshopPromptToPortfolio(promptIdx) {
            const mod = workshopsData[currentModuleIndex];
            const p = mod.prompts[promptIdx];
            if (!p) return;

            const newPromptItem = {
                id: 'prompt_' + Date.now(),
                title: `${mod.code}: ${p.title}`,
                category: mod.category || 'หนังสือราชการ',
                moduleCode: mod.code,
                role: p.role,
                task: p.task,
                context: p.context,
                format: p.format,
                fullPrompt: `บทบาท: ${p.role}\\nงานที่ต้องการให้ทำ: ${p.task}\\nบริบทและข้อมูลสำคัญ: ${p.context}\\nรูปแบบภาษาและผลลัพธ์: ${p.format}`,
                savedAt: new Date().toLocaleDateString('th-TH', { day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' })
            };

            // Avoid exact duplicate titles
            const exists = participantProfile.savedPrompts.some(item => item.title === newPromptItem.title);
            if (!exists) {
                participantProfile.savedPrompts.unshift(newPromptItem);
                saveParticipantProfile();
                updatePortfolioUI();
                showToast(`บันทึก "${p.title}" เข้าแฟ้มผลงานแล้ว!`);
            } else {
                showToast('คำสั่ง Prompt นี้ถูกบันทึกไว้ในแฟ้มผลงานแล้ว');
            }
        }

        function saveCurrentBuilderToPortfolio() {
            const role = document.getElementById('builder-role').value.trim() || 'เจ้าหน้าที่ผู้รับผิดชอบงาน อปท.';
            const task = document.getElementById('builder-task').value.trim() || 'ภารกิจปฏิบัติงานราชการ';
            const context = document.getElementById('builder-context').value.trim() || 'ข้อมูลตามข้อเท็จจริง';
            const format = document.getElementById('builder-format').value.trim() || 'ภาษาราชการตามระเบียบงานสารบรรณ';

            const newPromptItem = {
                id: 'builder_' + Date.now(),
                title: `Prompt สร้างเอง: ${task.substring(0, 35)}...`,
                category: 'กำหนดเอง',
                moduleCode: 'CUSTOM',
                role: role,
                task: task,
                context: context,
                format: format,
                fullPrompt: `บทบาท: ${role}\\nงานที่ต้องการให้ทำ: ${task}\\nบริบทและข้อมูลสำคัญ: ${context}\\nรูปแบบภาษาและผลลัพธ์: ${format}`,
                savedAt: new Date().toLocaleDateString('th-TH', { day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' })
            };

            participantProfile.savedPrompts.unshift(newPromptItem);
            saveParticipantProfile();
            updatePortfolioUI();
            showToast('บันทึกคำสั่ง Prompt จากเครื่องมือสร้าง เข้าแฟ้มผลงานเรียบร้อยแล้ว!');
        }

        function deletePortfolioPrompt(id) {
            participantProfile.savedPrompts = participantProfile.savedPrompts.filter(p => p.id !== id);
            saveParticipantProfile();
            updatePortfolioUI();
            showToast('ลบรายการออกจากแฟ้มผลงานแล้ว');
        }

        function loadSamplePortfolioPrompts() {
            const samples = [
                {
                    id: 'sample_1',
                    title: 'WS 1: ร่างบันทึกข้อความขออนุมัติโครงการอบรม AI',
                    category: 'หนังสือราชการ',
                    moduleCode: 'WS 1',
                    role: 'นักจัดการงานทั่วไปชำนาญการ สังกัดสำนักปลัด เทศบาลตำบล',
                    task: 'ร่างบันทึกข้อความ (หนังสือภายใน) เสนอต่อนายกเทศมนตรี ขออนุมัติจัดโครงการฝึกอบรม AI ในงานราชการ',
                    context: 'กลุ่มเป้าหมายบุคลากร 50 คน วันที่ 15 พ.ย. 2569 งบประมาณ 15,000 บาท หมวดค่าใช้สอย',
                    format: 'ระเบียบงานสารบรรณ พ.ศ. 2526 แบ่ง 3 ส่วน: 1. ต้นเรื่อง 2. ข้อเท็จจริง 3. ข้อพิจารณาและข้อเสนอ',
                    fullPrompt: 'บทบาท: นักจัดการงานทั่วไปชำนาญการ สังกัดสำนักปลัด เทศบาลตำบล\\nงานที่ต้องการให้ทำ: ร่างบันทึกข้อความ (หนังสือภายใน) เสนอต่อนายกเทศมนตรี ขออนุมัติจัดโครงการฝึกอบรม AI ในงานราชการ\\nบริบทและข้อมูลสำคัญ: กลุ่มเป้าหมายบุคลากร 50 คน วันที่ 15 พ.ย. 2569 งบประมาณ 15,000 บาท หมวดค่าใช้สอย\\nรูปแบบภาษาและผลลัพธ์: ระเบียบงานสารบรรณ พ.ศ. 2526 แบ่ง 3 ส่วน: 1. ต้นเรื่อง 2. ข้อเท็จจริง 3. ข้อพิจารณาและข้อเสนอ',
                    savedAt: 'ตัวอย่างแม่แบบ'
                },
                {
                    id: 'sample_2',
                    title: 'WS 3: วิเคราะห์ข้อมูลข้อบัญญัติงบประมาณ 5 ปีย้อนหลัง',
                    category: 'แผนและงบประมาณ',
                    moduleCode: 'WS 3',
                    role: 'นักวิเคราะห์นโยบายและแผนชำนาญการ กองยุทธศาสตร์และงบประมาณ',
                    task: 'วิเคราะห์แนวโน้มการจัดสรรงบประมาณ 5 ปีย้อนหลัง และหาช่องว่างการพัฒนาเพื่อตั้งโครงการใหม่',
                    context: 'งบด้านสาธารณสุขและเทคโนโลยีมีสัดส่วนต่ำกว่า 8% ขณะที่ภารกิจขยายตัวสูง',
                    format: 'สรุปเป็นตารางเปรียบเทียบสัดส่วน ร้อยละการเปลี่ยนแปลง และ 3 ข้อเสนอเชิงยุทธศาสตร์',
                    fullPrompt: 'บทบาท: นักวิเคราะห์นโยบายและแผนชำนาญการ กองยุทธศาสตร์และงบประมาณ\\nงานที่ต้องการให้ทำ: วิเคราะห์แนวโน้มการจัดสรรงบประมาณ 5 ปีย้อนหลัง และหาช่องว่างการพัฒนาเพื่อตั้งโครงการใหม่\\nบริบทและข้อมูลสำคัญ: งบด้านสาธารณสุขและเทคโนโลยีมีสัดส่วนต่ำกว่า 8% ขณะที่ภารกิจขยายตัวสูง\\nรูปแบบภาษาและผลลัพธ์: สรุปเป็นตารางเปรียบเทียบสัดส่วน ร้อยละการเปลี่ยนแปลง และ 3 ข้อเสนอเชิงยุทธศาสตร์',
                    savedAt: 'ตัวอย่างแม่แบบ'
                },
                {
                    id: 'sample_3',
                    title: 'WS 5: ร่างโพสต์ Facebook ประชาสัมพันธ์โครงการลงทะเบียนเบี้ยยังชีพ',
                    category: 'ประชาสัมพันธ์',
                    moduleCode: 'WS 5',
                    role: 'นักประชาสัมพันธ์ชำนาญการ ดูแลสื่อสารสังคมออนไลน์ของ อปท.',
                    task: 'เขียนโพสต์ Facebook และโครงร่างภาพ Infographic แจ้งประชาชนลงทะเบียนเบี้ยยังชีพผู้สูงอายุ',
                    context: 'รับลงทะเบียนภายในเดือนพฤศจิกายน ณ กองสวัสดิการสังคม เอกสาร: บัตร ปชช., ทะเบียนบ้าน, สมุดบัญชี',
                    format: 'ภาษาเป็นกันเอง สุภาพ มีอิโมจิ อ่านง่ายใน 3 วินาที พร้อมแฮชแท็ก 3 อัน',
                    fullPrompt: 'บทบาท: นักประชาสัมพันธ์ชำนาญการ ดูแลสื่อสารสังคมออนไลน์ของ อปท.\\nงานที่ต้องการให้ทำ: เขียนโพสต์ Facebook และโครงร่างภาพ Infographic แจ้งประชาชนลงทะเบียนเบี้ยยังชีพผู้สูงอายุ\\nบริบทและข้อมูลสำคัญ: รับลงทะเบียนภายในเดือนพฤศจิกายน ณ กองสวัสดิการสังคม เอกสาร: บัตร ปชช., ทะเบียนบ้าน, สมุดบัญชี\\nรูปแบบภาษาและผลลัพธ์: ภาษาเป็นกันเอง สุภาพ มีอิโมจิ อ่านง่ายใน 3 วินาที พร้อมแฮชแท็ก 3 อัน',
                    savedAt: 'ตัวอย่างแม่แบบ'
                }
            ];

            samples.forEach(s => {
                if (!participantProfile.savedPrompts.some(item => item.title === s.title)) {
                    participantProfile.savedPrompts.push(s);
                }
            });

            saveParticipantProfile();
            updatePortfolioUI();
            showToast('โหลดตัวอย่างแม่แบบ 3 รายการเข้าสู่แฟ้มผลงานแล้ว!');
        }

        let currentPortfolioFilter = 'all';

        function filterPortfolio(cat) {
            currentPortfolioFilter = cat;
            const buttons = document.querySelectorAll('.cat-filter-btn');
            buttons.forEach(b => {
                if ((cat === 'all' && b.textContent === 'ทั้งหมด') || b.textContent.includes(cat)) {
                    b.className = "cat-filter-btn px-3 py-1 rounded-lg text-xs font-heading font-semibold bg-slate-900 text-white transition";
                } else {
                    b.className = "cat-filter-btn px-3 py-1 rounded-lg text-xs font-heading font-medium bg-slate-100 hover:bg-slate-200 text-slate-700 transition";
                }
            });
            renderPortfolioList();
        }

        function renderPortfolioList() {
            const container = document.getElementById('portfolio-prompts-container');
            const searchKeyword = (document.getElementById('portfolio-search')?.value || '').toLowerCase().trim();

            let list = participantProfile.savedPrompts || [];

            if (currentPortfolioFilter !== 'all') {
                list = list.filter(item => (item.category || '').includes(currentPortfolioFilter));
            }

            if (searchKeyword) {
                list = list.filter(item => 
                    item.title.toLowerCase().includes(searchKeyword) ||
                    item.task.toLowerCase().includes(searchKeyword) ||
                    item.role.toLowerCase().includes(searchKeyword)
                );
            }

            if (list.length === 0) {
                container.innerHTML = `
                    <div class="text-center py-12 px-4 border-2 border-dashed border-slate-200 rounded-2xl bg-slate-50/50 space-y-3">
                        <div class="w-12 h-12 rounded-full bg-slate-200 text-slate-500 flex items-center justify-center mx-auto">
                            <i data-lucide="bookmark" class="w-6 h-6"></i>
                        </div>
                        <h4 class="font-heading font-semibold text-slate-800 text-sm">ยังไม่มีคำสั่ง Prompt ที่บันทึกไว้</h4>
                        <p class="text-xs text-slate-500 max-w-md mx-auto">
                            ท่านสามารถบันทึก Prompt ได้ง่ายๆ โดยกดปุ่ม <strong>"เก็บเข้าแฟ้ม"</strong> ในหน้ารายละเอียดบทเรียน หรือสร้างขึ้นใหม่ในเครื่องมือสร้าง Prompt
                        </p>
                        <div class="pt-2 flex justify-center gap-2">
                            <button onclick="loadSamplePortfolioPrompts()" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-heading font-semibold rounded-xl shadow-xs transition">
                                โหลดแม่แบบมาตรฐาน 3 รายการ
                            </button>
                            <button onclick="switchMainView('builder')" class="px-4 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 text-xs font-heading font-semibold rounded-xl shadow-xs transition">
                                สร้าง Prompt ใหม่เดี๋ยวนี้
                            </button>
                        </div>
                    </div>
                `;
                lucide.createIcons();
                return;
            }

            container.innerHTML = list.map((item, idx) => {
                const encodedPrompt = encodeURIComponent(item.fullPrompt);
                return `
                <div class="border border-slate-200 hover:border-indigo-300 rounded-xl overflow-hidden bg-white shadow-2xs transition space-y-0">
                    <div class="bg-slate-800 text-white px-4 py-2.5 flex flex-wrap items-center justify-between gap-2">
                        <div class="flex items-center gap-2 truncate">
                            <span class="px-2 py-0.5 rounded text-[11px] font-heading font-semibold bg-indigo-500/30 text-indigo-200 border border-indigo-400/30">${item.category || 'ทั่วไป'}</span>
                            <span class="font-heading font-semibold text-sm text-amber-300 truncate">${item.title}</span>
                        </div>
                        <div class="flex items-center gap-1.5 text-xs">
                            <span class="text-[11px] text-slate-400 hidden sm:inline">${item.savedAt}</span>
                            <button onclick="copyTextDecode('${encodedPrompt}', 'คัดลอก Prompt จากแฟ้มผลงานแล้ว!')" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-heading font-semibold px-2.5 py-1 rounded-lg flex items-center gap-1 transition">
                                <i data-lucide="copy" class="w-3.5 h-3.5"></i>
                                <span>คัดลอก</span>
                            </button>
                            <a href="https://gemini.google.com/" target="_blank" rel="noopener noreferrer" class="bg-slate-700 hover:bg-slate-600 text-slate-200 px-2 py-1 rounded-lg flex items-center gap-1 transition" title="เปิด Gemini">
                                <i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-300"></i>
                            </a>
                            <button onclick="deletePortfolioPrompt('${item.id}')" class="bg-rose-500/20 hover:bg-rose-500/40 text-rose-300 hover:text-white px-2 py-1 rounded-lg transition" title="ลบรายการนี้">
                                <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
                            </button>
                        </div>
                    </div>
                    <div class="p-4 space-y-2 text-xs sm:text-sm text-slate-700 bg-slate-50/40">
                        <div><strong class="font-heading text-indigo-950">• บทบาท:</strong> ${item.role}</div>
                        <div><strong class="font-heading text-indigo-950">• ภารกิจ:</strong> ${item.task}</div>
                        <div><strong class="font-heading text-indigo-950">• บริบท:</strong> ${item.context}</div>
                        <div><strong class="font-heading text-indigo-950">• รูปแบบ:</strong> ${item.format}</div>
                    </div>
                </div>
                `;
            }).join('');

            lucide.createIcons();
        }

        function updatePortfolioUI() {
            // Update Stat badges
            const totalModules = workshopsData.length;
            const doneModules = completedModules.size;
            const modulesDoneEl = document.getElementById('stat-modules-done');
            if (modulesDoneEl) modulesDoneEl.textContent = `${doneModules} / ${totalModules}`;

            const quizScoreEl = document.getElementById('stat-quiz-score');
            const quizStatusEl = document.getElementById('stat-quiz-status');
            if (quizScoreEl) {
                if (participantProfile.quizScore !== null) {
                    quizScoreEl.textContent = `${participantProfile.quizScore} / ${participantProfile.quizTotal || 5}`;
                    if (quizStatusEl) {
                        quizStatusEl.textContent = participantProfile.quizPassed ? 'ผ่านเกณฑ์แล้ว (รับเกียรติบัตรได้)' : 'ยังไม่ผ่านเกณฑ์ (ทำใหม่ได้)';
                        quizStatusEl.className = participantProfile.quizPassed ? 'text-[10px] text-emerald-600 mt-0.5 font-bold' : 'text-[10px] text-amber-600 mt-0.5 font-bold';
                    }
                } else {
                    quizScoreEl.textContent = '- / 5';
                    if (quizStatusEl) quizStatusEl.textContent = 'ยังไม่ได้ทำแบบทดสอบ';
                }
            }

            const promptsCount = (participantProfile.savedPrompts || []).length;
            const countEl = document.getElementById('stat-prompts-count');
            if (countEl) countEl.textContent = promptsCount;

            const badgeEl = document.getElementById('portfolio-count-badge');
            if (badgeEl) badgeEl.textContent = `${promptsCount} ชิ้น`;

            const navBadge = document.getElementById('nav-portfolio-badge');
            if (navBadge) {
                if (promptsCount > 0) {
                    navBadge.textContent = promptsCount;
                    navBadge.classList.remove('hidden');
                } else {
                    navBadge.classList.add('hidden');
                }
            }

            // Render Modules Checklist in Portfolio
            const checklistContainer = document.getElementById('portfolio-modules-checklist');
            if (checklistContainer) {
                checklistContainer.innerHTML = workshopsData.map((mod, idx) => {
                    const isDone = completedModules.has(mod.id);
                    return `
                    <div class="flex items-center justify-between p-2 rounded-lg border ${isDone ? 'bg-emerald-50/60 border-emerald-200 text-emerald-950' : 'bg-slate-50 border-slate-200 text-slate-700'}">
                        <span class="truncate flex items-center gap-1.5 cursor-pointer hover:underline" onclick="switchMainView('workshop'); selectModule(${idx});">
                            <i data-lucide="${isDone ? 'check-circle-2' : 'circle'}" class="w-4 h-4 ${isDone ? 'text-emerald-600 shrink-0' : 'text-slate-400 shrink-0'}"></i>
                            <span class="truncate font-heading font-medium">${mod.code}: ${mod.title.substring(0, 26)}...</span>
                        </span>
                        <button onclick="toggleModuleDoneDirect('${mod.id}')" class="text-[11px] font-heading px-1.5 py-0.5 rounded ${isDone ? 'bg-emerald-200 text-emerald-900' : 'bg-slate-200 text-slate-700'}">
                            ${isDone ? 'เรียนจบแล้ว' : 'ติ๊กจบ'}
                        </button>
                    </div>
                    `;
                }).join('');
            }

            renderPortfolioList();
        }

        function toggleModuleDoneDirect(modId) {
            if (completedModules.has(modId)) {
                completedModules.delete(modId);
            } else {
                completedModules.add(modId);
            }
            updateProgressUI();
            updatePortfolioUI();
            renderSidebar(document.getElementById('search-input')?.value || '');
            renderCurrentModule();
        }

        function updateCertificateUI() {
            // Update Certificate recipient details
            const nameEl = document.getElementById('cert-name-display');
            const roleOrgEl = document.getElementById('cert-role-org-display');
            const dateEl = document.getElementById('cert-date-display');
            const idEl = document.getElementById('cert-id-display');
            const statusBadge = document.getElementById('cert-status-badge');

            if (nameEl) nameEl.textContent = participantProfile.fullName || 'นายสมศักดิ์ มุ่งมั่นพัฒนา';
            
            const position = participantProfile.position || 'นักจัดการงานทั่วไปชำนาญการ';
            const dept = participantProfile.department ? ` ${participantProfile.department}` : '';
            const org = participantProfile.organization || 'องค์กรปกครองส่วนท้องถิ่น';
            if (roleOrgEl) roleOrgEl.textContent = `ตำแหน่ง ${position}${dept} สังกัด ${org}`;

            if (dateEl) dateEl.textContent = participantProfile.issueDateThai || '๑ พฤศจิกายน ๒๕๖๙';
            if (idEl) idEl.textContent = participantProfile.certificateId || 'AI-LG-2569-8B74';

            if (statusBadge) {
                if (participantProfile.quizScore !== null) {
                    statusBadge.textContent = `ผ่านการประเมิน (${participantProfile.quizScore}/${participantProfile.quizTotal || 5})`;
                    statusBadge.className = 'px-2.5 py-0.5 rounded-full text-xs font-heading font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40';
                } else {
                    statusBadge.textContent = 'สมบูรณ์ (พร้อมออกใบประกาศฯ)';
                    statusBadge.className = 'px-2.5 py-0.5 rounded-full text-xs font-heading font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/40';
                }
            }
        }

        function printCertificate() {
            document.body.classList.add('printing-certificate');
            window.print();
            setTimeout(() => {
                document.body.classList.remove('printing-certificate');
            }, 1000);
        }

        function printPortfolio() {
            window.print();
        }

        function openEditProfileModal() {
            switchMainView('portfolio');
            const form = document.getElementById('portfolio-profile-form');
            if (form) {
                form.scrollIntoView({ behavior: 'smooth', block: 'center' });
                form.classList.add('ring-4', 'ring-indigo-400');
                setTimeout(() => form.classList.remove('ring-4', 'ring-indigo-400'), 2000);
            }
        }
    """

    # Add loadParticipantProfile into initApp
    old_init = """        // Initialize on load
        window.onload = initApp;"""

    new_init = full_portfolio_cert_js + """
        // Initialize on load
        window.addEventListener('DOMContentLoaded', () => {
            initApp();
            loadParticipantProfile();
        });
"""
    html = html.replace(old_init, new_init)

    with open('/Users/hanaharper/Downloads/AI_LG/ai.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Successfully updated ai.html with Portfolio and Certificate!")

if __name__ == '__main__':
    main()
