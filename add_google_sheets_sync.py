# -*- coding: utf-8 -*-
"""
Adds 4-Batch Google Sheets Database Sync to ai.html.
Features:
- Cohort / Batch Selector (รุ่นที่ ๑ - ๔) in Profile Form
- Live Cloud Sync Bar with status indicator
- Google Sheets Webhook Configuration Modal
- Auto-sync on quiz completion and manual sync button
- Certificate badge displaying batch number
"""

import re

def main():
    with open('/Users/hanaharper/Downloads/AI_LG/ai.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. ADD BATCH SELECTOR & SYNC BAR IN PROFILE FORM
    old_profile_form_tail = """                                <div>
                                    <label class="block text-xs font-heading font-semibold text-slate-700 mb-1">องค์กรปกครองส่วนท้องถิ่น (อปท.) *</label>
                                    <input type="text" id="prof-org" oninput="saveProfileFromForm()" placeholder="เช่น เทศบาลตำบลเมืองใหม่ จ.เชียงใหม่" class="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                </div>
                                <div class="pt-1 flex items-center justify-between">
                                    <p class="text-[11px] text-slate-400">ข้อมูลนี้จะถูกนำไปแสดงบนใบประกาศนียบัตรออนไลน์ทันที</p>
                                    <button type="button" onclick="saveProfileFromForm(true)" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-heading font-semibold rounded-lg transition shadow-xs">
                                        บันทึกข้อมูล
                                    </button>
                                </div>
                            </form>"""

    new_profile_form_tail = """                                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                                    <div>
                                        <label class="block text-xs font-heading font-semibold text-slate-700 mb-1">องค์กรปกครองส่วนท้องถิ่น (อปท.) *</label>
                                        <input type="text" id="prof-org" oninput="saveProfileFromForm()" placeholder="เช่น เทศบาลตำบลเมืองใหม่ จ.เชียงใหม่" class="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none">
                                    </div>
                                    <div>
                                        <label class="block text-xs font-heading font-semibold text-slate-700 mb-1">รุ่นการอบรม (Cohort) *</label>
                                        <select id="prof-batch" onchange="saveProfileFromForm(true)" class="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none bg-white font-medium text-slate-800">
                                            <option value="รุ่นที่ ๑">รุ่นที่ ๑ (Batch 1)</option>
                                            <option value="รุ่นที่ ๒">รุ่นที่ ๒ (Batch 2)</option>
                                            <option value="รุ่นที่ ๓">รุ่นที่ ๓ (Batch 3)</option>
                                            <option value="รุ่นที่ ๔">รุ่นที่ ๔ (Batch 4)</option>
                                        </select>
                                    </div>
                                </div>

                                <!-- Cloud Database Sync Bar (Google Sheets) -->
                                <div class="p-3.5 bg-gradient-to-r from-blue-50 to-indigo-50/80 rounded-xl border border-blue-200/80 space-y-2 text-xs">
                                    <div class="flex items-center justify-between gap-2">
                                        <div class="flex items-center gap-2">
                                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                                            <div>
                                                <span class="font-heading font-bold text-blue-950">ฐานข้อมูล: <span id="sync-batch-display" class="text-blue-700 font-extrabold">รุ่นที่ ๑</span></span>
                                                <span id="sync-status-text" class="text-slate-500 ml-1 block sm:inline text-[11px]">(พร้อมส่งข้อมูล)</span>
                                            </div>
                                        </div>
                                        <button type="button" onclick="openSheetsConfigModal()" aria-label="ตั้งค่า Google Sheet" class="p-1 rounded-lg hover:bg-white text-slate-500 hover:text-slate-800 transition" title="ตั้งค่า Google Sheet Webhook">
                                            <i data-lucide="settings" class="w-4 h-4"></i>
                                        </button>
                                    </div>
                                    <button type="button" onclick="syncToGoogleSheets(true)" id="btn-sync-sheet" class="w-full py-2 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-heading font-semibold rounded-lg flex items-center justify-center gap-1.5 transition shadow-xs">
                                        <i data-lucide="cloud-upload" class="w-4 h-4"></i>
                                        <span>ส่งข้อมูลยืนยันรับเกียรติบัตรเข้า Google Sheets</span>
                                    </button>
                                </div>

                                <div class="pt-1 flex items-center justify-between">
                                    <p class="text-[11px] text-slate-400">ข้อมูลนี้จะถูกส่งเข้า Google Sheet ของวิทยากรทันที</p>
                                    <button type="button" onclick="saveProfileFromForm(true)" class="px-3.5 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-heading font-semibold rounded-lg transition shadow-xs">
                                        บันทึกข้อมูล
                                    </button>
                                </div>
                            </form>"""
    html = html.replace(old_profile_form_tail, new_profile_form_tail)

    # 2. ADD BATCH BADGE ON CERTIFICATE VIEW
    old_cert_badge = """                                <span id="cert-status-badge" class="px-2.5 py-0.5 rounded-full text-xs font-heading font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                                    ผ่านการประเมินแล้ว
                                </span>"""
    new_cert_badge = """                                <span id="cert-status-badge" class="px-2.5 py-0.5 rounded-full text-xs font-heading font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40">
                                    ผ่านการประเมินแล้ว
                                </span>
                                <span id="cert-batch-badge" class="px-2.5 py-0.5 rounded-full text-xs font-heading font-semibold bg-blue-500/20 text-blue-300 border border-blue-500/40">
                                    รุ่นที่ ๑
                                </span>"""
    html = html.replace(old_cert_badge, new_cert_badge)

    # 3. ADD GOOGLE SHEETS CONFIG MODAL BEFORE </body>
    modal_html = """
    <!-- Google Sheets Webhook Configuration Modal -->
    <div id="sheets-config-modal" class="fixed inset-0 z-50 bg-slate-950/70 backdrop-blur-xs hidden flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-lg w-full p-6 sm:p-7 shadow-2xl border border-slate-200 space-y-4">
            <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                <div class="flex items-center gap-2">
                    <div class="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center">
                        <i data-lucide="sheet" class="w-5 h-5"></i>
                    </div>
                    <h3 class="font-heading font-bold text-slate-900 text-base">ตั้งค่าฐานข้อมูล Google Sheets (4 รุ่น)</h3>
                </div>
                <button onclick="closeSheetsConfigModal()" aria-label="ปิดหน้าต่างตั้งค่า" class="p-1 rounded-lg text-slate-400 hover:text-slate-700">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>
            <p class="text-xs text-slate-600 leading-relaxed">
                นำ <strong>URL ของเว็บแอป (Google Apps Script Web App URL)</strong> ที่ได้จากการ Deploy Google Sheet ของวิทยากร มาวางในช่องด้านล่างนี้ เพื่อให้ระบบส่งข้อมูลผู้เรียนแยกตาม <strong>รุ่นที่ ๑, ๒, ๓, ๔</strong> อัตโนมัติ:
            </p>
            <div class="space-y-1.5">
                <label for="input-webhook-url" class="block text-xs font-heading font-semibold text-slate-700">Google Apps Script Webhook URL:</label>
                <input type="url" id="input-webhook-url" placeholder="https://script.google.com/macros/s/.../exec" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-xs font-mono focus:ring-2 focus:ring-emerald-500 focus:outline-none">
            </div>
            <div class="p-3 rounded-xl bg-blue-50 border border-blue-200 text-[11px] text-blue-900 leading-relaxed">
                💡 โค้ด Apps Script พร้อมใช้งานถูกบันทึกไว้ในไฟล์ <strong>google_apps_script.js</strong> ในเครื่องของคุณ สามารถเปิดและคัดลอกไปวางใน Google Sheet ได้ทันที
            </div>
            <div class="pt-2 flex items-center justify-end gap-2 border-t border-slate-100">
                <button type="button" onclick="closeSheetsConfigModal()" class="px-4 py-2 text-xs font-heading font-medium text-slate-600 hover:bg-slate-100 rounded-xl">ยกเลิก</button>
                <button type="button" onclick="saveSheetsConfig()" class="px-5 py-2 bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-heading font-bold rounded-xl shadow-xs transition">บันทึกการตั้งค่า</button>
            </div>
        </div>
    </div>
"""
    html = html.replace('</body>', modal_html + '\n</body>')

    # 4. UPDATE JS STATE & FUNCTIONS
    # Update participantProfile definition
    old_profile_js = """        let participantProfile = {
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
        };"""

    new_profile_js = """        let participantProfile = {
            fullName: 'นายสมศักดิ์ มุ่งมั่นพัฒนา',
            position: 'นักจัดการงานทั่วไปชำนาญการ',
            department: 'สำนักปลัดเทศบาล',
            organization: 'เทศบาลตำบลเมืองใหม่ จ.เชียงใหม่',
            batch: 'รุ่นที่ ๑',
            quizScore: null,
            quizTotal: 5,
            quizPassed: false,
            certificateId: 'AI-LG-2569-' + Math.floor(1000 + Math.random() * 9000),
            issueDateThai: '๑ พฤศจิกายน ๒๕๖๙',
            sheetWebhookUrl: '',
            lastSyncedAt: null,
            savedPrompts: []
        };"""
    html = html.replace(old_profile_js, new_profile_js)

    # Add load batch and webhook in loadParticipantProfile
    old_sync_form = """            if (nameEl) nameEl.value = participantProfile.fullName;
            if (posEl) posEl.value = participantProfile.position;
            if (deptEl) deptEl.value = participantProfile.department;
            if (orgEl) orgEl.value = participantProfile.organization;"""

    new_sync_form = """            if (nameEl) nameEl.value = participantProfile.fullName;
            if (posEl) posEl.value = participantProfile.position;
            if (deptEl) deptEl.value = participantProfile.department;
            if (orgEl) orgEl.value = participantProfile.organization;
            
            const batchEl = document.getElementById('prof-batch');
            if (batchEl && participantProfile.batch) batchEl.value = participantProfile.batch;
            
            const savedWebhook = localStorage.getItem('ai_lg_sheet_webhook_url');
            if (savedWebhook) participantProfile.sheetWebhookUrl = savedWebhook;"""
    html = html.replace(old_sync_form, new_sync_form)

    # Add batch reading in saveProfileFromForm
    old_save_form = """            if (nameEl && nameEl.value.trim()) participantProfile.fullName = nameEl.value.trim();
            if (posEl && posEl.value.trim()) participantProfile.position = posEl.value.trim();
            if (deptEl) participantProfile.department = deptEl.value.trim();
            if (orgEl && orgEl.value.trim()) participantProfile.organization = orgEl.value.trim();"""

    new_save_form = """            if (nameEl && nameEl.value.trim()) participantProfile.fullName = nameEl.value.trim();
            if (posEl && posEl.value.trim()) participantProfile.position = posEl.value.trim();
            if (deptEl) participantProfile.department = deptEl.value.trim();
            if (orgEl && orgEl.value.trim()) participantProfile.organization = orgEl.value.trim();
            const batchEl = document.getElementById('prof-batch');
            if (batchEl) participantProfile.batch = batchEl.value;"""
    html = html.replace(old_save_form, new_save_form)

    # Add Google Sheets functions into the JS section
    sheets_js = """
        // ==========================================
        // GOOGLE SHEETS 4-BATCH CLOUD SYNC LOGIC
        // ==========================================
        function openSheetsConfigModal() {
            const modal = document.getElementById('sheets-config-modal');
            const input = document.getElementById('input-webhook-url');
            if (input) input.value = participantProfile.sheetWebhookUrl || localStorage.getItem('ai_lg_sheet_webhook_url') || '';
            if (modal) modal.classList.remove('hidden');
        }

        function closeSheetsConfigModal() {
            const modal = document.getElementById('sheets-config-modal');
            if (modal) modal.classList.add('hidden');
        }

        function saveSheetsConfig() {
            const input = document.getElementById('input-webhook-url');
            if (input) {
                const url = input.value.trim();
                participantProfile.sheetWebhookUrl = url;
                localStorage.setItem('ai_lg_sheet_webhook_url', url);
                saveParticipantProfile();
                closeSheetsConfigModal();
                showToast('บันทึก Webhook URL ของ Google Sheets สำเร็จ!');
                updateSyncUI();
            }
        }

        function updateSyncUI() {
            const batchDisplay = document.getElementById('sync-batch-display');
            if (batchDisplay) batchDisplay.textContent = participantProfile.batch || 'รุ่นที่ ๑';

            const statusText = document.getElementById('sync-status-text');
            if (statusText) {
                if (participantProfile.lastSyncedAt) {
                    statusText.textContent = `(ซิงค์แล้วล่าสุด: ${participantProfile.lastSyncedAt})`;
                    statusText.className = 'text-emerald-700 font-semibold ml-1 block sm:inline text-[11px]';
                } else if (participantProfile.sheetWebhookUrl) {
                    statusText.textContent = '(พร้อมส่งเข้าชีต)';
                    statusText.className = 'text-blue-700 ml-1 block sm:inline text-[11px]';
                } else {
                    statusText.textContent = '(คลิกรูปเฟืองเพื่อใส่ URL Google Sheets)';
                    statusText.className = 'text-slate-500 ml-1 block sm:inline text-[11px]';
                }
            }

            const certBatchBadge = document.getElementById('cert-batch-badge');
            if (certBatchBadge) certBatchBadge.textContent = participantProfile.batch || 'รุ่นที่ ๑';
        }

        async function syncToGoogleSheets(isManual = false) {
            const webhookUrl = participantProfile.sheetWebhookUrl || localStorage.getItem('ai_lg_sheet_webhook_url');
            if (!webhookUrl) {
                if (isManual) {
                    openSheetsConfigModal();
                    showToast('กรุณาระบุ URL ของ Google Apps Script ก่อนส่งข้อมูล');
                }
                return;
            }

            const payload = {
                fullName: participantProfile.fullName || 'ไม่ระบุชื่อ',
                position: participantProfile.position || '-',
                department: participantProfile.department || '-',
                organization: participantProfile.organization || '-',
                batch: participantProfile.batch || 'รุ่นที่ ๑',
                quizScore: participantProfile.quizScore,
                quizTotal: participantProfile.quizTotal || 5,
                quizPassed: participantProfile.quizPassed || false,
                certificateId: participantProfile.certificateId || '-',
                savedPromptsCount: (participantProfile.savedPrompts || []).length
            };

            const btn = document.getElementById('btn-sync-sheet');
            if (btn) {
                btn.disabled = true;
                btn.innerHTML = `<i data-lucide="loader-2" class="w-4 h-4 animate-spin"></i><span>กำลังส่งข้อมูลเข้า Google Sheets...</span>`;
                lucide.createIcons();
            }

            try {
                // Using mode: 'no-cors' for Google Apps Script Web App
                await fetch(webhookUrl, {
                    method: 'POST',
                    mode: 'no-cors',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });

                const timeStr = new Date().toLocaleTimeString('th-TH', { hour: '2-digit', minute: '2-digit' });
                participantProfile.lastSyncedAt = timeStr;
                saveParticipantProfile();
                updateSyncUI();

                showToast(`ส่งข้อมูลรุ่น ${participantProfile.batch} เข้า Google Sheets สำเร็จ!`);
            } catch (err) {
                console.error('Failed to sync to Google Sheets', err);
                if (isManual) showToast('ไม่สามารถส่งข้อมูลได้ กรุณาตรวจสอบการเชื่อมต่ออินเทอร์เน็ต');
            } finally {
                if (btn) {
                    btn.disabled = false;
                    btn.innerHTML = `<i data-lucide="cloud-upload" class="w-4 h-4"></i><span>ส่งข้อมูลยืนยันรับเกียรติบัตรเข้า Google Sheets</span>`;
                    lucide.createIcons();
                }
            }
        }
    """

    # Inject sheets_js before "// Initialize on load"
    html = html.replace('        // Initialize on load', sheets_js + '\n        // Initialize on load')

    # Trigger sync in submitQuiz()
    old_submit_trigger = """            showToast(`ตรวจคำตอบเรียบร้อย! คุณได้ ${score}/${quizQuestions.length} คะแนน`);
            updatePortfolioUI();
            updateCertificateUI();"""

    new_submit_trigger = """            showToast(`ตรวจคำตอบเรียบร้อย! คุณได้ ${score}/${quizQuestions.length} คะแนน`);
            updatePortfolioUI();
            updateCertificateUI();
            // Automatically sync score to Google Sheets in background
            syncToGoogleSheets(false);"""
    html = html.replace(old_submit_trigger, new_submit_trigger)

    # Call updateSyncUI in updatePortfolioUI
    old_port_tail = "            renderPortfolioList();\n        }"
    new_port_tail = "            renderPortfolioList();\n            updateSyncUI();\n        }"
    html = html.replace(old_port_tail, new_port_tail, 1)

    with open('/Users/hanaharper/Downloads/AI_LG/ai.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Successfully added 4-Batch Google Sheets Database Sync to ai.html!")

if __name__ == '__main__':
    main()
