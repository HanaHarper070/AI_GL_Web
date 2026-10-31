# -*- coding: utf-8 -*-
"""
Applies a Bright, Vibrant, High-Taste design theme to ai.html based on design-taste-frontend.
Features: Frosted Glass Nav, Vibrant Modern Gradients, Soft Atmospheric Glow, and Crisp Typography.
"""

import re

def main():
    with open('/Users/hanaharper/Downloads/AI_LG/ai.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. ENHANCE CSS & BODY BACKGROUND
    bright_css = """
        /* Bright & Vibrant Theme Atmosphere (design-taste-frontend) */
        body {
            font-family: 'Sarabun', sans-serif;
            background-color: #f8fafc;
            background-image: 
                radial-gradient(at 100% 0%, rgba(59, 130, 246, 0.07) 0px, transparent 50%),
                radial-gradient(at 0% 15%, rgba(245, 158, 11, 0.05) 0px, transparent 45%),
                radial-gradient(at 50% 100%, rgba(16, 185, 129, 0.04) 0px, transparent 50%);
            background-attachment: fixed;
        }
        .card-glow:hover {
            box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.08), 0 8px 10px -6px rgba(37, 99, 235, 0.04);
            transform: translateY(-2px);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }
    """
    
    # Replace the body { font-family: 'Sarabun', sans-serif; }
    html = re.sub(r'body\s*\{\s*font-family:\s*\'Sarabun\',\s*sans-serif;\s*\}', bright_css, html)

    # 2. UPDATE TOP NAVIGATION HEADER (Frosted Glass Bright Theme)
    old_header_pattern = r'<header class="sticky top-0 z-40 bg-gov-900.*?</header>'
    new_header = """<header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md text-slate-800 shadow-xs border-b border-slate-200/80 transition-all">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-3">
            <!-- Brand / Title -->
            <div class="flex items-center gap-3 shrink-0">
                <button id="mobile-menu-btn" onclick="toggleMobileSidebar()" aria-label="เปิดเมนูหลัก" class="lg:hidden p-2 rounded-xl text-slate-600 hover:text-blue-600 hover:bg-blue-50 focus:outline-none transition">
                    <i data-lucide="menu" class="w-6 h-6"></i>
                </button>
                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-600 via-indigo-600 to-sky-500 flex items-center justify-center shadow-md shadow-blue-500/20 shrink-0 text-white">
                    <i data-lucide="sparkles" class="w-5 h-5 text-amber-300"></i>
                </div>
                <div class="hidden sm:block">
                    <div class="flex items-center gap-2">
                        <span class="text-[11px] font-heading font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-blue-50 text-blue-700 border border-blue-200/80">ระบบการเรียนรู้ดิจิทัล อปท.</span>
                        <span class="text-xs font-medium text-slate-400">พ.ศ. 2569</span>
                    </div>
                    <h1 class="font-heading font-bold text-base text-slate-900 truncate max-w-[220px] md:max-w-xs lg:max-w-md">
                        การประยุกต์ใช้ AI ในการทำงาน อปท.
                    </h1>
                </div>
            </div>

            <!-- Central Navigation Tabs (Interactive Views) -->
            <nav class="flex items-center gap-1 sm:gap-1.5 overflow-x-auto py-1">
                <!-- 1. Workshop Lessons -->
                <button onclick="switchMainView('workshop')" id="nav-btn-workshop" class="nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-bold transition bg-gradient-to-r from-blue-600 to-indigo-600 text-white shadow-sm shadow-blue-500/25">
                    <i data-lucide="book-open" class="w-4 h-4"></i>
                    <span>บทเรียน</span>
                </button>

                <!-- 2. Interactive Prompt Builder -->
                <button onclick="switchMainView('builder')" id="nav-btn-builder" class="nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-medium text-slate-600 hover:text-blue-700 hover:bg-blue-50/80 transition">
                    <i data-lucide="wand-2" class="w-4 h-4 text-amber-500"></i>
                    <span class="hidden md:inline">สร้าง Prompt</span>
                    <span class="md:hidden">Prompt</span>
                </button>

                <!-- 3. Participant Portfolio -->
                <button onclick="switchMainView('portfolio')" id="nav-btn-portfolio" class="nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-medium text-slate-600 hover:text-blue-700 hover:bg-blue-50/80 transition relative">
                    <i data-lucide="folder-kanban" class="w-4 h-4 text-emerald-600"></i>
                    <span>แฟ้มผลงาน</span>
                    <span id="nav-portfolio-badge" class="hidden absolute -top-1 -right-1 px-1.5 py-0.2 bg-emerald-500 text-[10px] text-white font-bold rounded-full">0</span>
                </button>

                <!-- 4. Post-Test Quiz -->
                <button onclick="switchMainView('quiz')" id="nav-btn-quiz" class="nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-medium text-slate-600 hover:text-blue-700 hover:bg-blue-50/80 transition">
                    <i data-lucide="help-circle" class="w-4 h-4 text-indigo-500"></i>
                    <span class="hidden md:inline">แบบทดสอบ</span>
                    <span class="md:hidden">Quiz</span>
                </button>

                <!-- 5. E-Certificate -->
                <button onclick="switchMainView('certificate')" id="nav-btn-certificate" class="nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-medium text-slate-600 hover:text-blue-700 hover:bg-blue-50/80 transition">
                    <i data-lucide="award" class="w-4 h-4 text-amber-500"></i>
                    <span class="hidden md:inline">เกียรติบัตร</span>
                    <span class="md:hidden">ใบประกาศฯ</span>
                </button>
            </nav>

            <!-- Right Companion Links & Tools -->
            <div class="flex items-center gap-1.5 sm:gap-2 shrink-0">
                <!-- Companion Tools Dropdown/Links -->
                <div class="relative group">
                    <button class="flex items-center gap-1 px-3 py-1.5 rounded-xl text-xs font-heading font-semibold bg-slate-100 hover:bg-blue-50 hover:text-blue-700 text-slate-700 border border-slate-200 transition" title="สื่อการสอนประกอบหลักสูตร">
                        <i data-lucide="layers" class="w-3.5 h-3.5 text-blue-600"></i>
                        <span class="hidden sm:inline">สื่อประกอบ</span>
                        <i data-lucide="chevron-down" class="w-3 h-3 text-slate-400"></i>
                    </button>
                    <div class="absolute right-0 mt-1.5 w-56 bg-white border border-slate-200 rounded-2xl shadow-xl py-2 hidden group-hover:block z-50">
                        <a href="slides.html" target="_blank" rel="noopener noreferrer" class="flex items-center gap-2.5 px-4 py-2.5 text-xs font-heading font-medium text-slate-700 hover:bg-blue-50 hover:text-blue-700 transition">
                            <div class="w-7 h-7 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center shrink-0">
                                <i data-lucide="presentation" class="w-4 h-4"></i>
                            </div>
                            <div>
                                <div class="font-bold">สไลด์บรรยาย (Slides 16:9)</div>
                                <div class="text-[10px] text-slate-400">38 สไลด์ ครบ 6 ประเภท</div>
                            </div>
                        </a>
                        <a href="trainer_guide.html" target="_blank" rel="noopener noreferrer" class="flex items-center gap-2.5 px-4 py-2.5 text-xs font-heading font-medium text-slate-700 hover:bg-blue-50 hover:text-blue-700 transition">
                            <div class="w-7 h-7 rounded-lg bg-indigo-100 text-indigo-700 flex items-center justify-center shrink-0">
                                <i data-lucide="book-open-check" class="w-4 h-4"></i>
                            </div>
                            <div>
                                <div class="font-bold">คู่มือวิทยากร (Trainer Guide)</div>
                                <div class="text-[10px] text-slate-400">กำหนดการ & บทบรรยายละเอียด</div>
                            </div>
                        </a>
                        <a href="handout.html" target="_blank" rel="noopener noreferrer" class="flex items-center gap-2.5 px-4 py-2.5 text-xs font-heading font-medium text-slate-700 hover:bg-blue-50 hover:text-blue-700 transition">
                            <div class="w-7 h-7 rounded-lg bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">
                                <i data-lucide="file-text" class="w-4 h-4"></i>
                            </div>
                            <div>
                                <div class="font-bold">เอกสารสรุปฝึกอบรม (Handout)</div>
                                <div class="text-[10px] text-slate-400">พิมพ์ชีทและใบงาน A4</div>
                            </div>
                        </a>
                    </div>
                </div>

                <!-- Presentation Mode Toggle (Instructor) -->
                <button onclick="togglePresentationMode()" id="presentation-btn" title="โหมดบรรยายสำหรับวิทยากร (ขยายตัวอักษร)" class="p-2 rounded-xl bg-slate-100 hover:bg-blue-50 text-slate-600 hover:text-blue-700 border border-slate-200 transition">
                    <i data-lucide="projector" class="w-4 h-4"></i>
                </button>
            </div>
        </div>
    </header>"""
    html = re.sub(old_header_pattern, new_header, html, flags=re.DOTALL)

    # 3. UPDATE SIDEBAR HEADER & PROGRESS BOX
    old_sidebar_header = r'<div class="lg:hidden p-4 bg-gov-900 text-white flex items-center justify-between">.*?</div>'
    new_sidebar_header = """<div class="lg:hidden p-4 bg-gradient-to-r from-blue-700 to-indigo-800 text-white flex items-center justify-between">
                    <span class="font-heading font-bold">สารบัญหลักสูตรอบรม</span>
                    <button onclick="toggleMobileSidebar()" aria-label="ปิดเมนู" class="p-1 rounded-lg text-slate-300 hover:text-white">
                        <i data-lucide="x" class="w-5 h-5"></i>
                    </button>
                </div>"""
    html = re.sub(old_sidebar_header, new_sidebar_header, html, flags=re.DOTALL)

    # Update sidebar progress box to bright style
    old_prog_box = r'<div class="px-4 py-3 bg-slate-900 text-white flex items-center justify-between border-b border-slate-800">.*?</div>'
    new_prog_box = """<div class="px-4 py-3 bg-gradient-to-r from-blue-50 to-indigo-50/70 text-slate-800 flex items-center justify-between border-b border-blue-100">
                    <span class="text-xs font-heading font-semibold text-blue-950">ความคืบหน้าการอบรม:</span>
                    <div class="flex items-center gap-2">
                        <div class="w-20 h-2 bg-blue-200/80 rounded-full overflow-hidden">
                            <div id="progress-bar" class="h-full bg-gradient-to-r from-emerald-500 to-teal-400 transition-all duration-500" style="width: 14%"></div>
                        </div>
                        <span id="progress-text" class="text-xs font-bold text-emerald-700">1/7</span>
                    </div>
                </div>"""
    html = re.sub(old_prog_box, new_prog_box, html, flags=re.DOTALL)

    # 4. UPDATE WORKSHOP BANNER TO BRIGHT GRADIENT
    old_ws_banner = r'<div id="workshop-banner" class="bg-gradient-to-r from-gov-800 via-gov-700 to-blue-700 rounded-2xl p-6 sm:p-8 text-white shadow-lg relative overflow-hidden">'
    new_ws_banner = """<div id="workshop-banner" class="bg-gradient-to-r from-blue-600 via-indigo-600 to-cyan-500 rounded-3xl p-6 sm:p-8 text-white shadow-xl shadow-blue-500/15 relative overflow-hidden">
                        <!-- Atmospheric Ambient Glows -->
                        <div class="absolute -right-10 -bottom-10 w-64 h-64 bg-white/10 rounded-full blur-2xl pointer-events-none"></div>
                        <div class="absolute right-32 -top-10 w-40 h-40 bg-amber-400/20 rounded-full blur-xl pointer-events-none"></div>"""
    html = html.replace(old_ws_banner, new_ws_banner)

    # 5. UPDATE PROMPT BUILDER BANNER
    old_builder_banner = r'<div class="bg-gradient-to-r from-amber-500 via-amber-600 to-orange-600 rounded-2xl p-6 sm:p-8 text-white shadow-lg">'
    new_builder_banner = """<div class="bg-gradient-to-r from-amber-500 via-orange-500 to-rose-500 rounded-3xl p-6 sm:p-8 text-white shadow-xl shadow-orange-500/15 relative overflow-hidden">
                        <div class="absolute -right-10 -bottom-10 w-64 h-64 bg-white/10 rounded-full blur-2xl pointer-events-none"></div>"""
    html = html.replace(old_builder_banner, new_builder_banner)

    # 6. UPDATE QUIZ BANNER
    old_quiz_banner = r'<div class="bg-gradient-to-r from-emerald-800 via-teal-800 to-cyan-800 rounded-2xl p-6 sm:p-8 text-white shadow-lg">'
    new_quiz_banner = """<div class="bg-gradient-to-r from-emerald-600 via-teal-600 to-cyan-600 rounded-3xl p-6 sm:p-8 text-white shadow-xl shadow-emerald-500/15 relative overflow-hidden">
                        <div class="absolute -right-10 -bottom-10 w-64 h-64 bg-white/10 rounded-full blur-2xl pointer-events-none"></div>"""
    html = html.replace(old_quiz_banner, new_quiz_banner)

    # 7. UPDATE PORTFOLIO BANNER
    old_portfolio_banner = r'<div class="bg-gradient-to-r from-slate-900 via-indigo-950 to-blue-900 rounded-2xl p-6 sm:p-8 text-white shadow-lg relative overflow-hidden">'
    new_portfolio_banner = """<div class="bg-gradient-to-r from-indigo-700 via-purple-700 to-blue-600 rounded-3xl p-6 sm:p-8 text-white shadow-xl shadow-indigo-500/15 relative overflow-hidden">
                        <div class="absolute -right-10 -bottom-10 w-64 h-64 bg-white/10 rounded-full blur-2xl pointer-events-none"></div>"""
    html = html.replace(old_portfolio_banner, new_portfolio_banner)

    # 8. UPDATE CERTIFICATE BANNER & WRAPPER
    old_cert_banner = r'<div class="bg-slate-900 text-white rounded-2xl p-6 sm:p-7 shadow-lg flex flex-col md:flex-row md:items-center justify-between gap-4">'
    new_cert_banner = """<div class="bg-gradient-to-r from-slate-900 via-blue-950 to-indigo-950 text-white rounded-3xl p-6 sm:p-8 shadow-xl relative overflow-hidden flex flex-col md:flex-row md:items-center justify-between gap-4">
                        <div class="absolute -right-10 -bottom-10 w-64 h-64 bg-amber-400/10 rounded-full blur-2xl pointer-events-none"></div>"""
    html = html.replace(old_cert_banner, new_cert_banner)

    # Frame wrapper for certificate
    old_cert_wrap = r'<div class="overflow-x-auto pb-6">'
    new_cert_wrap = """<div class="overflow-x-auto pb-6 bg-slate-100/60 p-4 sm:p-8 rounded-3xl border border-slate-200/80 shadow-inner">"""
    html = html.replace(old_cert_wrap, new_cert_wrap, 1)

    # 9. UPDATE switchMainView TAB ACTIVE/INACTIVE CLASSES IN JS
    old_btn_style_code = """                    if (v === viewName) {
                        btn.className = "nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-bold transition bg-amber-500 text-slate-950 shadow-sm";
                    } else {
                        btn.className = "nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition";
                    }"""

    new_btn_style_code = """                    if (v === viewName) {
                        btn.className = "nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-bold transition bg-gradient-to-r from-blue-600 to-indigo-600 text-white shadow-sm shadow-blue-500/25";
                    } else {
                        btn.className = "nav-tab-btn flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs sm:text-sm font-heading font-medium text-slate-600 hover:text-blue-700 hover:bg-blue-50/80 transition";
                    }"""
    html = html.replace(old_btn_style_code, new_btn_style_code)

    # 10. UPDATE SIDEBAR ACTIVE MODULE BUTTONS IN renderSidebar
    old_sidebar_btn_class = """                btn.className = `w-full text-left p-3 rounded-xl transition flex items-start gap-3 group ${
                    isActive 
                        ? 'bg-gov-800 text-white shadow-sm' 
                        : 'hover:bg-slate-100 text-slate-700'
                }`;"""
    new_sidebar_btn_class = """                btn.className = `w-full text-left p-3 rounded-xl transition flex items-start gap-3 group ${
                    isActive 
                        ? 'bg-gradient-to-r from-blue-600 to-indigo-600 text-white shadow-md shadow-blue-500/20 font-medium' 
                        : 'hover:bg-blue-50/80 hover:text-blue-900 text-slate-700'
                }`;"""
    html = html.replace(old_sidebar_btn_class, new_sidebar_btn_class)

    with open('/Users/hanaharper/Downloads/AI_LG/ai.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Successfully transformed ai.html into Bright & Vibrant Theme!")

if __name__ == '__main__':
    main()
