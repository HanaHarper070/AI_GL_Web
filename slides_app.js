/**
 * slides_app.js - Enhanced Presentation Engine for AI for Local Government Workshop
 */

let currentSlideIdx = 0;
let isNotesVisible = false;
let isOverviewOpen = false;
let isLaserActive = false;
let isBlankScreenActive = false;
let isTimerWidgetOpen = false;
let isLightTheme = false;

// Timer State
let timerTotalSeconds = 300; // 5 mins default
let timerRemainingSeconds = 300;
let timerInterval = null;
let isTimerRunning = false;

// Numeric Jump Buffer
let jumpBuffer = '';
let jumpTimeout = null;

document.addEventListener('DOMContentLoaded', () => {
    // Check saved theme
    if (localStorage.getItem('ai_lg_slide_theme') === 'light') {
        setTheme(true);
    }

    // Read URL hash (#slide=3)
    const hashMatch = window.location.hash.match(/slide=(\d+)/);
    if (hashMatch) {
        const reqIdx = parseInt(hashMatch[1], 10) - 1;
        if (reqIdx >= 0 && reqIdx < SLIDES_DATA.length) {
            currentSlideIdx = reqIdx;
        }
    }

    renderCurrentSlide();
    buildOverviewGrid();
    setupKeyboardAndMouse();
});

// Render Slide
function renderCurrentSlide() {
    const slide = SLIDES_DATA[currentSlideIdx];
    const wrapper = document.getElementById('slides-wrapper');
    if (!slide || !wrapper) return;

    // Update Header / Footer Information
    document.getElementById('current-module-tag').textContent = slide.module || 'อบรมเชิงปฏิบัติการ';
    document.getElementById('current-slide-title').textContent = slide.title || '';
    document.getElementById('slide-current-num').textContent = currentSlideIdx + 1;
    document.getElementById('slide-total-num').textContent = SLIDES_DATA.length;

    const progressPct = ((currentSlideIdx + 1) / SLIDES_DATA.length) * 100;
    document.getElementById('slide-progress-bar').style.width = `${progressPct}%`;

    // Disable / Enable Prev / Next buttons
    document.getElementById('btn-prev').disabled = currentSlideIdx === 0;
    document.getElementById('btn-next').disabled = currentSlideIdx === SLIDES_DATA.length - 1;

    // Update Speaker Notes
    document.getElementById('speaker-notes-content').textContent = slide.notes || 'ไม่มีบันทึกเพิ่มเติมสำหรับสไลด์นี้';

    // Update URL hash
    window.location.hash = `slide=${currentSlideIdx + 1}`;

    // Render HTML based on slide type with Larger Font Sizing
    wrapper.innerHTML = buildSlideHtml(slide);

    // Refresh Lucide Icons
    if (window.lucide) {
        window.lucide.createIcons();
    }
}

function buildSlideHtml(slide) {
    const isLight = isLightTheme;
    const cardBg = isLight ? 'bg-white border-slate-300 shadow-sm' : 'bg-slate-900/90 border-slate-800';
    const textHead = isLight ? 'text-slate-900' : 'text-white';
    const textMuted = isLight ? 'text-slate-600' : 'text-slate-300';
    const innerBox = isLight ? 'bg-slate-50 border-slate-200' : 'bg-slate-950/80 border-slate-800';

    if (slide.type === 'hero') {
        return `
            <div class="h-full flex flex-col justify-between p-6 sm:p-12">
                <div class="space-y-4">
                    <span class="inline-block px-3.5 py-1 rounded-full text-xs sm:text-sm font-heading font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30">
                        ${slide.badge}
                    </span>
                    <h1 class="text-3xl sm:text-5xl font-heading font-extrabold ${textHead} tracking-tight leading-tight">
                        ${slide.title}
                    </h1>
                    <p class="text-blue-300 text-base sm:text-xl font-medium max-w-4xl leading-relaxed">
                        ${slide.subtitle}
                    </p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 my-auto py-4">
                    ${slide.content.features.map(f => `
                        <div class="p-5 rounded-2xl ${cardBg} border hover:border-blue-500/60 transition space-y-3">
                            <div class="w-12 h-12 rounded-xl bg-blue-600/20 text-blue-400 flex items-center justify-center border border-blue-500/30">
                                <i data-lucide="${f.icon}" class="w-6 h-6"></i>
                            </div>
                            <h4 class="font-heading font-bold ${textHead} text-base sm:text-lg">${f.title}</h4>
                            <p class="text-xs sm:text-sm ${textMuted} leading-relaxed">${f.desc}</p>
                        </div>
                    `).join('')}
                </div>

                <div class="pt-3 border-t ${isLight ? 'border-slate-300' : 'border-slate-800/80'} flex items-center justify-between text-xs sm:text-sm ${textMuted}">
                    <span>${slide.content.footer_note || ''}</span>
                    <span class="font-mono font-bold text-amber-400">สไลด์ที่ ${slide.id} / ${SLIDES_DATA.length}</span>
                </div>
            </div>
        `;
    } else if (slide.type === 'grid_roadmap') {
        return `
            <div class="h-full flex flex-col justify-between p-6 sm:p-10">
                <div class="space-y-2">
                    <span class="inline-block px-3 py-1 rounded-full text-xs sm:text-sm font-heading font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                        ${slide.badge}
                    </span>
                    <h2 class="text-2xl sm:text-4xl font-heading font-extrabold ${textHead}">${slide.title}</h2>
                    <p class="text-sm sm:text-base ${textMuted}">${slide.subtitle}</p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 my-auto py-2">
                    ${slide.content.modules.map((m, idx) => `
                        <div class="p-4 rounded-2xl ${cardBg} border hover:border-indigo-500/60 transition space-y-2 ${idx === 6 ? 'sm:col-span-2 lg:col-span-1' : ''}">
                            <div class="flex items-center justify-between">
                                <span class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/40">${m.code}</span>
                                <span class="text-xs ${isLight ? 'text-slate-500' : 'text-slate-400'}">ส่วนที่ ${idx + 1}</span>
                            </div>
                            <h4 class="font-heading font-bold ${textHead} text-sm sm:text-base">${m.name}</h4>
                            <p class="text-xs sm:text-sm ${textMuted} leading-relaxed">${m.desc}</p>
                        </div>
                    `).join('')}
                </div>

                <div class="text-xs sm:text-sm ${textMuted} flex justify-between items-center pt-2 border-t ${isLight ? 'border-slate-300' : 'border-slate-800'}">
                    <span>หลักสูตรบูรณาการภาคทฤษฎีควบคู่การปฏิบัติการเข้มข้นตลอด 1 วันเต็ม</span>
                    <span class="font-mono font-bold text-amber-400">สไลด์ที่ ${slide.id}</span>
                </div>
            </div>
        `;
    } else if (slide.type === 'prompt_formula') {
        return `
            <div class="h-full flex flex-col justify-between p-6 sm:p-10">
                <div class="space-y-2">
                    <span class="inline-block px-3 py-1 rounded-full text-xs sm:text-sm font-heading font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30">
                        ${slide.badge}
                    </span>
                    <h2 class="text-2xl sm:text-4xl font-heading font-extrabold ${textHead}">${slide.title}</h2>
                    <p class="text-sm sm:text-base ${textMuted}">${slide.subtitle}</p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5 my-auto py-2">
                    ${slide.content.elements.map(el => `
                        <div class="p-5 rounded-2xl ${cardBg} border hover:border-amber-500/50 transition space-y-2.5">
                            <div class="flex items-center gap-3">
                                <div class="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-400 font-mono font-extrabold text-lg flex items-center justify-center border border-amber-500/40">
                                    ${el.letter}
                                </div>
                                <h4 class="font-heading font-bold ${textHead} text-base sm:text-lg">${el.name}</h4>
                            </div>
                            <p class="text-xs sm:text-sm ${textMuted} leading-relaxed">${el.desc}</p>
                            <div class="p-3 rounded-xl ${innerBox} text-xs sm:text-sm text-amber-300 font-mono">
                                ${el.example}
                            </div>
                        </div>
                    `).join('')}
                </div>

                <div class="text-xs sm:text-sm ${textMuted} flex justify-between items-center pt-2 border-t ${isLight ? 'border-slate-300' : 'border-slate-800'}">
                    <span>สูตร RTCF: Role (บทบาท) + Task (งานที่ต้องการ) + Context (บริบทและข้อมูล) + Format (รูปแบบผลลัพธ์)</span>
                    <span class="font-mono font-bold text-amber-400">สไลด์ที่ ${slide.id}</span>
                </div>
            </div>
        `;
    } else if (slide.type === 'gov_types_interactive' || slide.type === 'gov_types') {
        return `
            <div class="h-full flex flex-col justify-between p-6 sm:p-10">
                <div class="space-y-2">
                    <span class="inline-block px-3 py-1 rounded-full text-xs sm:text-sm font-heading font-bold bg-indigo-500/20 text-indigo-400 border border-indigo-500/30">
                        ${slide.badge}
                    </span>
                    <h2 class="text-2xl sm:text-4xl font-heading font-extrabold ${textHead}">${slide.title}</h2>
                    <p class="text-sm sm:text-base ${textMuted}">${slide.subtitle}</p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 my-auto py-2">
                    ${slide.content.types.map(t => {
                        const targetSlide = t.target_slide ? t.target_slide - 1 : null;
                        const clickAttr = targetSlide !== null ? `onclick="goToSlide(${targetSlide})"` : '';
                        const cursorClass = targetSlide !== null ? 'cursor-pointer hover:border-amber-400 hover:scale-[1.02] shadow-md group ring-2 ring-transparent hover:ring-amber-400/40' : '';
                        
                        return `
                        <div ${clickAttr} class="p-4 sm:p-5 rounded-2xl ${cardBg} border transition-all space-y-2.5 ${cursorClass}">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-2.5">
                                    <span class="w-8 h-8 rounded-full bg-blue-500/20 text-blue-300 font-bold text-sm flex items-center justify-center font-mono border border-blue-500/30">${t.num}</span>
                                    <h4 class="font-heading font-bold ${textHead} text-base sm:text-lg group-hover:text-amber-400 transition-colors">${t.title}</h4>
                                </div>
                                ${targetSlide !== null ? `
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-heading font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/40 flex items-center gap-1">
                                        <span>${t.target_label || 'ดูตัวอย่าง'}</span>
                                        <i data-lucide="arrow-right" class="w-3 h-3"></i>
                                    </span>
                                ` : ''}
                            </div>
                            <p class="text-xs sm:text-sm text-blue-300 font-medium">${t.desc}</p>
                            <p class="text-xs ${isLight ? 'text-slate-600 bg-slate-100' : 'text-slate-400 bg-slate-950/70'} p-2.5 rounded-xl border ${isLight ? 'border-slate-200' : 'border-slate-800'} leading-relaxed">${t.detail}</p>
                            ${targetSlide !== null ? `
                                <div class="pt-1 text-[11px] text-amber-400/90 font-medium flex items-center gap-1 group-hover:underline">
                                    <span>👉 คลิกเพื่อเปิดหน้าตัวอย่าง Prompt & ภาพเอกสารจำลอง</span>
                                </div>
                            ` : ''}
                        </div>
                    `;
                    }).join('')}
                </div>

                <div class="text-xs sm:text-sm ${textMuted} flex justify-between items-center pt-2 border-t ${isLight ? 'border-slate-300' : 'border-slate-800'}">
                    <span>💡 แนะนำ: คลิกที่การ์ดประเภทหนังสือใดก็ได้ เพื่อกระโดดไปยังสไลด์ตัวอย่างของหนังสือชนิดนั้น</span>
                    <span class="font-mono font-bold text-amber-400">สไลด์ที่ ${slide.id}</span>
                </div>
            </div>
        `;
    } else if (slide.type === 'prompt_display') {
        const rawText = slide.content.prompt_text;
        const encodedText = encodeURIComponent(rawText);
        const previewId = slide.content.preview_id || '';

        return `
            <div class="h-full flex flex-col justify-between p-6 sm:p-10">
                <div class="flex items-start justify-between gap-4">
                    <div class="space-y-1.5">
                        <span class="inline-block px-3 py-1 rounded-full text-xs sm:text-sm font-heading font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                            ${slide.badge}
                        </span>
                        <h2 class="text-2xl sm:text-3xl font-heading font-extrabold ${textHead}">${slide.title}</h2>
                        <p class="text-xs sm:text-sm ${textMuted}">${slide.subtitle}</p>
                    </div>

                    <!-- Action Buttons: Copy Prompt & View Document Mockup -->
                    <div class="flex items-center gap-2 shrink-0">
                        <button onclick="copyEncodedPrompt('${encodedText}')" class="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white text-xs sm:text-sm font-heading font-medium transition border border-slate-700 shadow-sm" title="คัดลอกคำสั่งเพื่อนำไปวางใน ChatGPT/Gemini">
                            <i data-lucide="copy" class="w-4 h-4 text-emerald-400"></i> คัดลอกคำสั่ง
                        </button>
                        ${previewId ? `
                            <button onclick="openDocPreview('${previewId}')" class="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs sm:text-sm font-heading font-semibold transition shadow-md shadow-blue-600/30 border border-blue-400" title="คลิกดูภาพหนังสือราชการและผลลัพธ์จำลอง">
                                <i data-lucide="external-link" class="w-4 h-4 text-amber-300"></i> คลิกดูตัวอย่างฉบับเต็ม
                            </button>
                        ` : ''}
                    </div>
                </div>

                <div class="my-auto py-2 space-y-3">
                    <div class="relative ${innerBox} rounded-2xl p-5 sm:p-6 font-mono text-xs sm:text-sm text-emerald-300 leading-relaxed shadow-inner overflow-y-auto max-h-[40vh] border">
                        <pre class="whitespace-pre-wrap font-sans text-xs sm:text-sm ${isLight ? 'text-slate-800' : 'text-slate-200'} leading-relaxed">${escapeHtml(rawText)}</pre>
                    </div>

                    ${slide.content.key_takeaway ? `
                        <div class="p-3.5 rounded-xl bg-blue-900/30 border border-blue-500/40 flex items-center justify-between text-xs sm:text-sm text-blue-200">
                            <div class="flex items-center gap-2">
                                <i data-lucide="check-circle" class="w-5 h-5 text-emerald-400 shrink-0"></i>
                                <span>${slide.content.key_takeaway}</span>
                            </div>
                            ${previewId ? `
                                <button onclick="openDocPreview('${previewId}')" class="text-xs font-heading font-semibold text-amber-300 hover:text-white underline underline-offset-4 ml-2">
                                    [ คลิกดูเอกสารจำลอง ]
                                </button>
                            ` : ''}
                        </div>
                    ` : ''}
                </div>

                <div class="text-xs sm:text-sm ${textMuted} flex justify-between items-center pt-2 border-t ${isLight ? 'border-slate-300' : 'border-slate-800'}">
                    <span>ท่านสามารถคลิกปุ่ม 'คัดลอกคำสั่ง' หรือกดปุ่ม 'คลิกดูตัวอย่างฉบับเต็ม' เพื่อดูการจัดหน้าจริง</span>
                    <span class="font-mono font-bold text-amber-400">สไลด์ที่ ${slide.id}</span>
                </div>
            </div>
        `;
    } else if (slide.type === 'feature_card') {
        return `
            <div class="h-full flex flex-col justify-between p-6 sm:p-10">
                <div class="space-y-2">
                    <span class="inline-block px-3 py-1 rounded-full text-xs sm:text-sm font-heading font-bold bg-blue-500/20 text-blue-400 border border-blue-500/30">
                        ${slide.badge}
                    </span>
                    <h2 class="text-2xl sm:text-4xl font-heading font-extrabold ${textHead}">${slide.title}</h2>
                    <p class="text-sm sm:text-base ${textMuted}">${slide.subtitle}</p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-5 my-auto py-4">
                    ${slide.content.features.map(f => `
                        <div class="p-6 rounded-2xl ${cardBg} border hover:border-blue-500/50 transition space-y-3.5">
                            <div class="w-12 h-12 rounded-xl bg-blue-600/20 text-blue-400 flex items-center justify-center border border-blue-500/40">
                                <i data-lucide="${f.icon}" class="w-6 h-6"></i>
                            </div>
                            <h3 class="font-heading font-bold ${textHead} text-base sm:text-xl">${f.title}</h3>
                            <p class="text-xs sm:text-sm ${textMuted} leading-relaxed">${f.desc}</p>
                        </div>
                    `).join('')}
                </div>

                <div class="text-xs sm:text-sm ${textMuted} flex justify-between items-center pt-2 border-t ${isLight ? 'border-slate-300' : 'border-slate-800'}">
                    <span>แนวทางการประยุกต์ใช้เพื่อลดภาระงานซ้ำซ้อนและเพิ่มประสิทธิภาพการให้บริการประชาชน</span>
                    <span class="font-mono font-bold text-amber-400">สไลด์ที่ ${slide.id}</span>
                </div>
            </div>
        `;
    } else if (slide.type === 'two_column') {
        const previewId = slide.content.preview_id || '';
        return `
            <div class="h-full flex flex-col justify-between p-6 sm:p-10">
                <div class="flex items-start justify-between gap-4">
                    <div class="space-y-1.5">
                        <span class="inline-block px-3 py-1 rounded-full text-xs sm:text-sm font-heading font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">
                            ${slide.badge}
                        </span>
                        <h2 class="text-2xl sm:text-4xl font-heading font-extrabold ${textHead}">${slide.title}</h2>
                        <p class="text-xs sm:text-sm ${textMuted}">${slide.subtitle}</p>
                    </div>
                    ${previewId ? `
                        <button onclick="openDocPreview('${previewId}')" class="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-purple-600 hover:bg-purple-500 text-white text-xs sm:text-sm font-heading font-semibold transition shadow-md shadow-purple-600/30 border border-purple-400 shrink-0">
                            <i data-lucide="external-link" class="w-4 h-4 text-amber-300"></i> ดูตัวอย่างจำลอง
                        </button>
                    ` : ''}
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-5 my-auto py-2">
                    <div class="p-5 sm:p-6 rounded-2xl ${cardBg} border space-y-3">
                        <h4 class="font-heading font-bold text-emerald-400 text-base sm:text-lg flex items-center gap-2">
                            <i data-lucide="check-circle-2" class="w-5 h-5"></i>
                            ${slide.content.left_title}
                        </h4>
                        <ul class="space-y-2 text-xs sm:text-sm ${textMuted}">
                            ${slide.content.left_items.map(it => `
                                <li class="p-3 rounded-xl ${innerBox} border leading-relaxed">
                                    ${it}
                                </li>
                            `).join('')}
                        </ul>
                    </div>

                    <div class="p-5 sm:p-6 rounded-2xl ${cardBg} border space-y-3">
                        <h4 class="font-heading font-bold text-rose-400 text-base sm:text-lg flex items-center gap-2">
                            <i data-lucide="alert-circle" class="w-5 h-5"></i>
                            ${slide.content.right_title}
                        </h4>
                        <ul class="space-y-2 text-xs sm:text-sm ${textMuted}">
                            ${slide.content.right_items.map(it => `
                                <li class="p-3 rounded-xl ${innerBox} border leading-relaxed">
                                    ${it}
                                </li>
                            `).join('')}
                        </ul>
                    </div>
                </div>

                <div class="text-xs sm:text-sm ${textMuted} flex justify-between items-center pt-2 border-t ${isLight ? 'border-slate-300' : 'border-slate-800'}">
                    <span>การวิเคราะห์ข้อมูลเปรียบเทียบและการวางยุทธศาสตร์ท้องถิ่น</span>
                    <span class="font-mono font-bold text-amber-400">สไลด์ที่ ${slide.id}</span>
                </div>
            </div>
        `;
    } else if (slide.type === 'comparison') {
        const items = slide.content.items;
        return `
            <div class="h-full flex flex-col justify-between p-6 sm:p-10">
                <div class="space-y-2">
                    <span class="inline-block px-3 py-1 rounded-full text-xs sm:text-sm font-heading font-bold bg-rose-500/20 text-rose-400 border border-rose-500/30">
                        ${slide.badge}
                    </span>
                    <h2 class="text-2xl sm:text-4xl font-heading font-extrabold ${textHead}">${slide.title}</h2>
                    <p class="text-sm sm:text-base ${textMuted}">${slide.subtitle}</p>
                </div>

                <div class="grid grid-cols-1 ${items.length === 2 ? 'md:grid-cols-2' : 'md:grid-cols-3'} gap-5 my-auto py-2">
                    ${items.map(it => `
                        <div class="p-5 rounded-2xl ${cardBg} border space-y-3 flex flex-col justify-between">
                            <div class="space-y-2">
                                <h4 class="font-heading font-bold ${textHead} text-sm sm:text-base">${it.title}</h4>
                                <div class="text-xs sm:text-sm ${textMuted} leading-relaxed whitespace-pre-line ${innerBox} p-3.5 rounded-xl border">
                                    ${it.desc}
                                </div>
                            </div>
                            ${it.preview_id ? `
                                <button onclick="openDocPreview('${it.preview_id}')" class="mt-2 w-full py-1.5 px-3 rounded-xl bg-blue-600/30 hover:bg-blue-600/50 text-blue-300 border border-blue-400/50 text-xs font-heading font-semibold flex items-center justify-center gap-1.5 transition">
                                    <i data-lucide="external-link" class="w-3.5 h-3.5"></i> คลิกดูตัวอย่างจำลอง
                                </button>
                            ` : ''}
                        </div>
                    `).join('')}
                </div>

                <div class="text-xs sm:text-sm ${textMuted} flex justify-between items-center pt-2 border-t ${isLight ? 'border-slate-300' : 'border-slate-800'}">
                    <span>ข้อควรระวังและการปฏิบัติตามกฎหมายและระเบียบราชการ</span>
                    <span class="font-mono font-bold text-amber-400">สไลด์ที่ ${slide.id}</span>
                </div>
            </div>
        `;
    }

    return '';
}

// Navigation Functions
function nextSlide() {
    if (currentSlideIdx < SLIDES_DATA.length - 1) {
        currentSlideIdx++;
        renderCurrentSlide();
    }
}

function prevSlide() {
    if (currentSlideIdx > 0) {
        currentSlideIdx--;
        renderCurrentSlide();
    }
}

function goToSlide(index) {
    if (index >= 0 && index < SLIDES_DATA.length) {
        currentSlideIdx = index;
        renderCurrentSlide();
        if (isOverviewOpen) {
            toggleOverview();
        }
    }
}

// Light / Dark Theme Toggle
function toggleTheme() {
    setTheme(!isLightTheme);
}

function setTheme(light) {
    isLightTheme = light;
    localStorage.setItem('ai_lg_slide_theme', isLightTheme ? 'light' : 'dark');

    const body = document.getElementById('app-body');
    const stage = document.getElementById('slide-stage');
    const topNav = document.getElementById('top-nav');
    const bottomBar = document.getElementById('bottom-bar');
    const icon = document.getElementById('theme-icon');

    if (isLightTheme) {
        body.classList.remove('bg-slate-950', 'text-slate-100');
        body.classList.add('bg-slate-200', 'text-slate-900');

        stage.classList.remove('bg-slate-900', 'border-slate-800');
        stage.classList.add('bg-slate-100', 'border-slate-300');

        topNav.classList.remove('bg-slate-900/95', 'border-slate-800');
        topNav.classList.add('bg-gov-800', 'border-gov-900');

        bottomBar.classList.remove('bg-slate-900/95', 'border-slate-800');
        bottomBar.classList.add('bg-white', 'border-slate-300');

        if (icon) icon.setAttribute('data-lucide', 'moon');
    } else {
        body.classList.remove('bg-slate-200', 'text-slate-900');
        body.classList.add('bg-slate-950', 'text-slate-100');

        stage.classList.remove('bg-slate-100', 'border-slate-300');
        stage.classList.add('bg-slate-900', 'border-slate-800');

        topNav.classList.remove('bg-gov-800', 'border-gov-900');
        topNav.classList.add('bg-slate-900/95', 'border-slate-800');

        bottomBar.classList.remove('bg-white', 'border-slate-300');
        bottomBar.classList.add('bg-slate-900/95', 'border-slate-800');

        if (icon) icon.setAttribute('data-lucide', 'sun');
    }

    renderCurrentSlide();
    if (window.lucide) window.lucide.createIcons();
}

// Document Preview Modal
function openDocPreview(previewId) {
    const preview = DOCUMENT_PREVIEWS[previewId];
    if (!preview) return;

    document.getElementById('preview-modal-title').textContent = preview.title;
    document.getElementById('preview-modal-subtitle').textContent = preview.subtitle;
    document.getElementById('preview-modal-body').innerHTML = preview.html;

    const modal = document.getElementById('doc-preview-modal');
    modal.classList.remove('hidden');

    if (window.lucide) window.lucide.createIcons();
}

function closeDocPreview() {
    const modal = document.getElementById('doc-preview-modal');
    modal.classList.add('hidden');
}

// Timer Functions
function toggleTimerWidget() {
    isTimerWidgetOpen = !isTimerWidgetOpen;
    const widget = document.getElementById('timer-widget');
    if (isTimerWidgetOpen) {
        widget.classList.remove('hidden');
    } else {
        widget.classList.add('hidden');
    }
}

function setTimerDuration(seconds) {
    clearInterval(timerInterval);
    isTimerRunning = false;
    timerTotalSeconds = seconds;
    timerRemainingSeconds = seconds;
    updateTimerDisplay();
    document.getElementById('btn-timer-action').textContent = 'เริ่มจับเวลา';
    document.getElementById('btn-timer-action').classList.replace('bg-amber-600', 'bg-emerald-600');
    document.getElementById('timer-status').textContent = `ตั้งเวลา ${Math.floor(seconds/60)} นาที`;
}

function startPauseTimer() {
    const btn = document.getElementById('btn-timer-action');
    if (isTimerRunning) {
        clearInterval(timerInterval);
        isTimerRunning = false;
        btn.textContent = 'จับเวลาต่อ';
        btn.classList.replace('bg-amber-600', 'bg-emerald-600');
        document.getElementById('timer-status').textContent = 'หยุดชั่วคราว';
    } else {
        isTimerRunning = true;
        btn.textContent = 'พักเวลา';
        btn.classList.replace('bg-emerald-600', 'bg-amber-600');
        document.getElementById('timer-status').textContent = 'กำลังจับเวลา...';
        timerInterval = setInterval(() => {
            if (timerRemainingSeconds > 0) {
                timerRemainingSeconds--;
                updateTimerDisplay();
            } else {
                clearInterval(timerInterval);
                isTimerRunning = false;
                document.getElementById('timer-status').textContent = '⏰ หมดเวลาปฏิบัติการ!';
                btn.textContent = 'เริ่มใหม่';
                btn.classList.replace('bg-amber-600', 'bg-emerald-600');
                showToast('⏰ หมดเวลาทำกิจกรรม Workshop!');
            }
        }, 1000);
    }
}

function resetTimer() {
    clearInterval(timerInterval);
    isTimerRunning = false;
    timerRemainingSeconds = timerTotalSeconds;
    updateTimerDisplay();
    document.getElementById('btn-timer-action').textContent = 'เริ่มจับเวลา';
    document.getElementById('btn-timer-action').classList.replace('bg-amber-600', 'bg-emerald-600');
    document.getElementById('timer-status').textContent = 'รีเซ็ตเรียบร้อย';
}

function updateTimerDisplay() {
    const mins = Math.floor(timerRemainingSeconds / 60);
    const secs = timerRemainingSeconds % 60;
    const formatted = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    document.getElementById('timer-digits').textContent = formatted;
    document.getElementById('timer-display-btn').textContent = formatted;
}

// Digital Laser Pointer
function toggleLaserPointer() {
    isLaserActive = !isLaserActive;
    const laser = document.getElementById('laser-pointer');
    const btn = document.getElementById('btn-laser-toggle');
    if (isLaserActive) {
        laser.style.display = 'block';
        btn.classList.add('bg-rose-600', 'text-white');
    } else {
        laser.style.display = 'none';
        btn.classList.remove('bg-rose-600', 'text-white');
    }
}

// Blank Screen Toggle (Press B)
function toggleBlankScreen() {
    isBlankScreenActive = !isBlankScreenActive;
    const overlay = document.getElementById('blank-screen-overlay');
    if (isBlankScreenActive) {
        overlay.style.display = 'flex';
    } else {
        overlay.style.display = 'none';
    }
}

// Speaker Notes Toggle
function toggleNotes() {
    isNotesVisible = !isNotesVisible;
    const drawer = document.getElementById('speaker-notes-drawer');
    const btn = document.getElementById('btn-toggle-notes');
    if (isNotesVisible) {
        drawer.classList.remove('hidden');
        btn.classList.add('text-amber-400', 'bg-slate-700');
    } else {
        drawer.classList.add('hidden');
        btn.classList.remove('text-amber-400', 'bg-slate-700');
    }
}

// Overview Grid Modal
function toggleOverview() {
    isOverviewOpen = !isOverviewOpen;
    const modal = document.getElementById('overview-modal');
    if (isOverviewOpen) {
        modal.classList.remove('hidden');
    } else {
        modal.classList.add('hidden');
    }
}

function buildOverviewGrid() {
    const grid = document.getElementById('overview-grid');
    if (!grid) return;

    grid.innerHTML = SLIDES_DATA.map((s, idx) => `
        <button onclick="goToSlide(${idx})" class="p-3.5 rounded-2xl bg-slate-900 border border-slate-800 hover:border-blue-500 text-left transition group space-y-1.5 flex flex-col justify-between aspect-[16/10] shadow-sm">
            <div>
                <div class="flex items-center justify-between text-[11px] text-slate-400 font-mono">
                    <span class="font-bold text-amber-400">#${s.id}</span>
                    <span class="text-blue-400 font-sans truncate ml-2">${s.module}</span>
                </div>
                <h5 class="font-heading font-bold text-xs sm:text-sm text-white group-hover:text-blue-300 line-clamp-2 mt-1">
                    ${s.title}
                </h5>
            </div>
            <span class="text-[11px] text-slate-500 truncate">${s.badge}</span>
        </button>
    `).join('');
}

// Fullscreen Toggle
function toggleFullscreen() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {
            console.warn('Error enabling fullscreen:', err);
        });
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
}

// Keyboard and Mouse Events
function setupKeyboardAndMouse() {
    // Laser pointer movement
    window.addEventListener('mousemove', (e) => {
        if (isLaserActive) {
            const laser = document.getElementById('laser-pointer');
            laser.style.left = `${e.clientX}px`;
            laser.style.top = `${e.clientY}px`;
        }
    });

    window.addEventListener('keydown', (e) => {
        if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

        // Escape closes modals
        if (e.key === 'Escape') {
            if (!document.getElementById('doc-preview-modal').classList.contains('hidden')) {
                closeDocPreview();
                return;
            }
            if (isOverviewOpen) {
                toggleOverview();
                return;
            }
            if (isBlankScreenActive) {
                toggleBlankScreen();
                return;
            }
            if (isTimerWidgetOpen) {
                toggleTimerWidget();
                return;
            }
        }

        // Navigation
        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
            e.preventDefault();
            nextSlide();
        } else if (e.key === 'ArrowLeft' || e.key === 'Backspace' || e.key === 'PageUp') {
            e.preventDefault();
            prevSlide();
        } else if (e.key === 'Home') {
            e.preventDefault();
            goToSlide(0);
        } else if (e.key === 'End') {
            e.preventDefault();
            goToSlide(SLIDES_DATA.length - 1);
        } else if (e.key.toLowerCase() === 'f' || e.key === 'F5') {
            e.preventDefault();
            toggleFullscreen();
        } else if (e.key.toLowerCase() === 'l') {
            e.preventDefault();
            toggleLaserPointer();
        } else if (e.key.toLowerCase() === 'b') {
            e.preventDefault();
            toggleBlankScreen();
        } else if (e.key.toLowerCase() === 't') {
            e.preventDefault();
            toggleTimerWidget();
        } else if (e.key.toLowerCase() === 'n') {
            e.preventDefault();
            toggleNotes();
        } else if (e.key.toLowerCase() === 'o') {
            e.preventDefault();
            toggleOverview();
        }

        // Numeric jump (e.g. type '12' and press Enter)
        if (e.key >= '0' && e.key <= '9') {
            jumpBuffer += e.key;
            clearTimeout(jumpTimeout);
            jumpTimeout = setTimeout(() => { jumpBuffer = ''; }, 2000);
        } else if (e.key === 'Enter' && jumpBuffer.length > 0) {
            const targetNum = parseInt(jumpBuffer, 10);
            if (targetNum >= 1 && targetNum <= SLIDES_DATA.length) {
                goToSlide(targetNum - 1);
                showToast(`กระโดดไปสไลด์ที่ ${targetNum}`);
            }
            jumpBuffer = '';
        }
    });
}

// Copy prompt
function copyEncodedPrompt(encodedText) {
    const text = decodeURIComponent(encodedText);
    navigator.clipboard.writeText(text).then(() => {
        showToast('คัดลอกคำสั่ง Prompt เรียบร้อยแล้ว!');
    }).catch(() => {
        showToast('ไม่สามารถคัดลอกได้');
    });
}

function showToast(message) {
    const toast = document.getElementById('toast');
    const toastMsg = document.getElementById('toast-message');
    if (!toast) return;

    toastMsg.textContent = message;
    toast.classList.remove('opacity-0', 'translate-y-12');
    toast.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toast.classList.remove('opacity-100', 'translate-y-0');
        toast.classList.add('opacity-0', 'translate-y-12');
    }, 2500);
}

function escapeHtml(string) {
    const entityMap = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
    };
    return String(string).replace(/[&<>"']/g, function (s) {
        return entityMap[s];
    });
}
