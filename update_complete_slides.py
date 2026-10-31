import json

# 1. Update document_previews.js
doc_previews = """/**
 * document_previews.js - Realistic Thai Government Document Previews for Workshop Slides
 */
const DOCUMENT_PREVIEWS = {
    'doc-external': {
        title: 'ตัวอย่างหนังสือราชการภายนอก (ใช้กระดาษตราครุฑ)',
        subtitle: 'หนังสือขอความอนุเคราะห์วิทยากร ถึงอธิการบดีมหาวิทยาลัยราชภัฏ',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-6 text-sm leading-relaxed" style="min-height: 700px;">
                <div class="text-center relative">
                    <div class="w-16 h-16 mx-auto mb-1 flex items-center justify-center font-serif text-3xl font-bold text-amber-700">
                        🦅
                    </div>
                    <div class="text-xs text-slate-500 font-serif">(ตราครุฑสูง 3 ซม.)</div>
                </div>

                <div class="flex justify-between items-start text-xs pt-2">
                    <div><strong>ที่</strong> มท ๕๔๓๐๑ / ว ๑๐๒๔</div>
                    <div class="text-right">
                        <div>สำนักงานเทศบาลตำบลเมืองใหม่</div>
                        <div>อำเภอเมือง จังหวัดเชียงใหม่ ๕๐๐๐๐</div>
                    </div>
                </div>

                <div class="text-center text-xs py-1">๑ พฤศจิกายน ๒๕๖๙</div>

                <div class="text-xs space-y-1">
                    <div><strong>เรื่อง</strong>  ขอความอนุเคราะห์บุคลากรเป็นวิทยากรบรรยายโครงการฝึกอบรม</div>
                    <div><strong>เรียน</strong>  อธิการบดีมหาวิทยาลัยราชภัฏเชียงใหม่</div>
                    <div><strong>สิ่งที่ส่งมาด้วย</strong>  ๑. กำหนดการฝึกอบรม  จำนวน ๑ ชุด</div>
                </div>

                <div class="text-xs text-justify indent-8 leading-relaxed">
                    ด้วย เทศบาลตำบลเมืองใหม่ มีความประสงค์จะจัดทำโครงการฝึกอบรมเชิงปฏิบัติการ เรื่อง "การประยุกต์ใช้ปัญญาประดิษฐ์ (AI) เพื่อยกระดับการทำงานและการให้บริการประชาชนขององค์กรปกครองส่วนท้องถิ่น" ประจำปีงบประมาณ พ.ศ. ๒๕๖๙ ในวันศุกร์ที่ ๑๕ พฤศจิกายน ๒๕๖๙ เวลา ๐๙.๐๐ - ๑๖.๐๐ น. ณ ห้องประชุมสภาเทศบาลตำบลเมืองใหม่ โดยมีกลุ่มเป้าหมายเป็นข้าราชการ พนักงานเทศบาล และบุคลากรทางการศึกษาในสังกัด จำนวน ๕๐ คน
                </div>

                <div class="text-xs text-justify indent-8 leading-relaxed">
                    เทศบาลตำบลเมืองใหม่ ได้พิจารณาแล้วเห็นว่า บุคลากรในสังกัดของท่านเป็นผู้มีความรู้ ความเชี่ยวชาญ และมีประสบการณ์สูงด้านการประยุกต์ใช้เทคโนโลยีปัญญาประดิษฐ์ในภาครัฐ จึงใคร่ขอความอนุเคราะห์ อาจารย์ ดร.สมศักดิ์ นวัตกรรม ตำแหน่ง อาจารย์ประจำคณะวิทยาการจัดการ ไปเป็นวิทยากรบรรยายและฝึกปฏิบัติการตามวัน เวลา และสถานที่ดังกล่าว ทั้งนี้ เทศบาลตำบลเมืองใหม่ ยินดีรับผิดชอบค่าใช้จ่ายในการเดินทางและค่าสมนาคุณวิทยากรตามระเบียบกระทรวงมหาดไทยทุกประการ
                </div>

                <div class="text-xs text-justify indent-8 leading-relaxed">
                    จึงเรียนมาเพื่อโปรดพิจารณาให้ความอนุเคราะห์ และหวังเป็นอย่างยิ่งว่าจะได้รับความร่วมมือด้วยดีจากท่าน ขอขอบคุณมา ณ โอกาสนี้
                </div>

                <div class="text-right pt-6 pr-8 text-xs space-y-8">
                    <div>ขอแสดงความนับถือ</div>
                    <div>
                        <div class="font-bold">(นายกิตติคุณ ท้องถิ่นก้าวหน้า)</div>
                        <div class="text-slate-600">นายกเทศมนตรีตำบลเมืองใหม่</div>
                    </div>
                </div>

                <div class="border-t border-slate-200 pt-4 text-[11px] text-slate-500">
                    <div>สำนักปลัดเทศบาล (ฝ่ายอำนวยการ)</div>
                    <div>โทรศัพท์ ๐ ๕๓๑๒ ๓๔๕๖ ต่อ ๑๑  โทรสาร ๐ ๕๓๑๒ ๓๔๕๗</div>
                </div>
            </div>
        `
    },
    'doc-internal': {
        title: 'ตัวอย่างหนังสือราชการภายใน (กระดาษบันทึกข้อความ)',
        subtitle: 'บันทึกข้อความขออนุมัติจัดโครงการและเบิกจ่ายงบประมาณ 25,000 บาท',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-5 text-sm leading-relaxed" style="min-height: 700px;">
                <div class="border-b-2 border-slate-900 pb-3">
                    <div class="flex items-center gap-4">
                        <div class="text-2xl font-bold text-amber-700">🦅</div>
                        <h2 class="text-2xl font-heading font-bold tracking-wider text-slate-900">บันทึกข้อความ</h2>
                    </div>
                    <div class="grid grid-cols-2 gap-2 text-xs pt-3">
                        <div><strong>ส่วนราชการ:</strong> สำนักปลัดเทศบาล เทศบาลตำบลเมืองใหม่ โทร. ๑๑</div>
                        <div><strong>ที่:</strong> ชม ๕๔๓๐๑ / ๘๙๒</div>
                        <div><strong>วันที่:</strong> ๑ พฤศจิกายน ๒๕๖๙</div>
                        <div><strong>เรื่อง:</strong> ขออนุมัติจัดโครงการฝึกอบรมการใช้ AI ในงานราชการ และขออนุมัติงบประมาณ</div>
                    </div>
                </div>

                <div class="text-xs">
                    <strong>เรียน:</strong> นายกเทศมนตรีตำบลเมืองใหม่ (ผ่านปลัดเทศบาลตำบลเมืองใหม่)
                </div>

                <div class="text-xs space-y-1">
                    <div class="font-bold text-gov-800">๑. ต้นเรื่อง</div>
                    <div class="indent-8 text-justify">
                        ตามแผนพัฒนาบุคลากรของเทศบาลตำบลเมืองใหม่ ประจำปีงบประมาณ พ.ศ. ๒๕๖๙ กำหนดให้มีการจัดฝึกอบรมทักษะดิจิทัลเพื่อเพิ่มประสิทธิภาพการปฏิบัติราชการและการให้บริการประชาชน นั้น
                    </div>
                </div>

                <div class="text-xs space-y-1">
                    <div class="font-bold text-gov-800">๒. ข้อเท็จจริง</div>
                    <div class="indent-8 text-justify leading-relaxed">
                        สำนักปลัดเทศบาล ได้จัดทำโครงการฝึกอบรมเชิงปฏิบัติการ เรื่อง "การประยุกต์ใช้ปัญญาประดิษฐ์ (AI) ในงานราชการ" กำหนดจัดในวันศุกร์ที่ ๑๕ พฤศจิกายน ๒๕๖๙ ณ ห้องประชุมเทศบาลตำบลเมืองใหม่ กลุ่มเป้าหมายคือพนักงานเทศบาลจำนวน ๕๐ คน โดยใช้งบประมาณหมวดค่าใช้สอย แผนงานบริหารงานทั่วไป โครงการพัฒนาบุคลากร เป็นจำนวนเงิน ๒๕,๐๐๐ บาท (สองหมื่นห้าพันบาทถ้วน)
                    </div>
                </div>

                <div class="text-xs space-y-1">
                    <div class="font-bold text-gov-800">๓. ข้อพิจารณาและข้อเสนอ</div>
                    <div class="indent-8 text-justify leading-relaxed">
                        เพื่อให้การปฏิบัติงานเป็นไปด้วยความเรียบร้อยและถูกต้องตามระเบียบกระทรวงมหาดไทยว่าด้วยค่าใช้จ่ายในการฝึกอบรมขององค์กรปกครองส่วนท้องถิ่น พ.ศ. ๒๕๕๗ จึงเรียนมาเพื่อโปรดพิจารณา:
                    </div>
                    <div class="pl-12 space-y-1 pt-1">
                        <div>๑. อนุมัติให้จัดโครงการฝึกอบรมตามวัน เวลา และสถานที่ดังกล่าว</div>
                        <div>๒. อนุมัติให้เบิกจ่ายงบประมาณ จำนวน ๒๕,๐๐๐ บาท จากโครงการพัฒนาบุคลากร</div>
                        <div>๓. ลงนามในหนังสือขอความอนุเคราะห์วิทยากร ถึงมหาวิทยาลัยราชภัฏเชียงใหม่</div>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-4 pt-8 text-xs">
                    <div class="text-center space-y-6">
                        <div>(ลงชื่อ)....................................................</div>
                        <div>
                            <div>(นางสาวจิตรา บริหารงาน)</div>
                            <div class="text-slate-500">นักจัดการงานทั่วไปชำนาญการ</div>
                        </div>
                    </div>
                    <div class="text-center space-y-6 border-l border-slate-200 pl-4">
                        <div class="text-emerald-700 font-bold">[ คำสั่งการ / อนุมัติ ]</div>
                        <div>(ลงชื่อ)....................................................</div>
                        <div>
                            <div>(นายกิตติคุณ ท้องถิ่นก้าวหน้า)</div>
                            <div class="text-slate-500">นายกเทศมนตรีตำบลเมืองใหม่</div>
                        </div>
                    </div>
                </div>
            </div>
        `
    },
    'doc-seal': {
        title: 'ตัวอย่างหนังสือประทับตรา (ใช้ประทับตราแทนการลงชื่อ)',
        subtitle: 'หนังสือส่งรายงานสถิติข้อมูลประจำเดือน ถึงสำนักงานส่งเสริมการปกครองท้องถิ่นอำเภอ',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-6 text-sm leading-relaxed" style="min-height: 600px;">
                <div class="text-center relative">
                    <div class="w-16 h-16 mx-auto mb-1 flex items-center justify-center font-serif text-3xl font-bold text-amber-700">
                        🦅
                    </div>
                    <div class="text-xs text-slate-500 font-serif">(กระดาษตราครุฑ)</div>
                </div>

                <div class="text-xs">
                    <div><strong>ที่</strong> ชม ๕๔๓๐๑ / ต ๒๔๕</div>
                </div>

                <div class="text-xs space-y-3 pt-2">
                    <div><strong>ถึง</strong> สำนักงานส่งเสริมการปกครองท้องถิ่นอำเภอเมืองเชียงใหม่</div>
                    <div class="indent-8 text-justify leading-relaxed">
                        เทศบาลตำบลเมืองใหม่ ขอส่งรายงานสถิติการให้บริการประชาชนและการจัดเก็บรายได้ ประจำเดือนตุลาคม ๒๕๖๙ จำนวน ๑ ชุด รายละเอียดปรากฏตามเอกสารแนบท้ายนี้
                    </div>
                </div>

                <!-- Stamp Mark Area -->
                <div class="pt-12 text-center space-y-4">
                    <div class="inline-block p-6 rounded-full border-2 border-dashed border-rose-400 text-rose-700 bg-rose-50/50">
                        <div class="font-bold text-xs">[ ประทับตราชื่อส่วนราชการ ]</div>
                        <div class="text-[11px]">เทศบาลตำบลเมืองใหม่ (หมึกสีชาด)</div>
                        <div class="text-[10px] text-slate-500">พร้อมลายมือชื่อย่อเจ้าหน้าที่กำกับ</div>
                    </div>
                    <div class="text-xs text-slate-600">เทศบาลตำบลเมืองใหม่</div>
                    <div class="text-xs text-slate-500">๑ พฤศจิกายน ๒๕๖๙</div>
                </div>

                <div class="border-t border-slate-200 pt-4 text-[11px] text-slate-500">
                    <div>กองยุทธศาสตร์และงบประมาณ โทร ๐ ๕๓๑๒ ๓๔๕๖ ต่อ ๑๓</div>
                </div>
            </div>
        `
    },
    'doc-order': {
        title: 'ตัวอย่างหนังสือสั่งการ: คำสั่งเทศบาลตำบลเมืองใหม่',
        subtitle: 'คำสั่งแต่งตั้งคณะทำงานขับเคลื่อนการประยุกต์ใช้ปัญญาประดิษฐ์ (AI) ในงานราชการ',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-5 text-sm leading-relaxed" style="min-height: 700px;">
                <div class="text-center relative">
                    <div class="w-16 h-16 mx-auto mb-1 flex items-center justify-center font-serif text-3xl font-bold text-amber-700">
                        🦅
                    </div>
                    <h3 class="text-base font-heading font-bold">คำสั่งเทศบาลตำบลเมืองใหม่</h3>
                    <div class="text-xs">ที่ ๔๑๒ / ๒๕๖๙</div>
                    <div class="text-xs font-bold pt-1">เรื่อง แต่งตั้งคณะทำงานขับเคลื่อนการประยุกต์ใช้ปัญญาประดิษฐ์ (AI) ในงานราชการ</div>
                </div>

                <div class="text-xs text-justify indent-8 leading-relaxed">
                    ด้วย เทศบาลตำบลเมืองใหม่ มีนโยบายในการพัฒนานวัตกรรมการบริหารราชการท้องถิ่นและยกระดับการให้บริการประชาชนด้วยเทคโนโลยีดิจิทัล เพื่อให้การดำเนินงานเป็นไปด้วยความเรียบร้อย มีประสิทธิภาพ และเกิดผลสัมฤทธิ์อย่างเป็นรูปธรรม อาศัยอำนาจตามความในมาตรา ๔๘ เตรส แห่งพระราชบัญญัติเทศบาล พ.ศ. ๒๔๙๖ และที่แก้ไขเพิ่มเติม จึงแต่งตั้งคณะทำงาน ดังนี้:
                </div>

                <div class="text-xs pl-8 space-y-1.5 leading-relaxed">
                    <div>๑. ปลัดเทศบาลตำบลเมืองใหม่ <span class="float-right font-bold text-gov-800">ประธานคณะทำงาน</span></div>
                    <div>๒. ผู้อำนวยการกองคลัง <span class="float-right text-slate-700">คณะทำงาน</span></div>
                    <div>๓. ผู้อำนวยการกองช่าง <span class="float-right text-slate-700">คณะทำงาน</span></div>
                    <div>๔. ผู้อำนวยการกองสาธารณสุขและสิ่งแวดล้อม <span class="float-right text-slate-700">คณะทำงาน</span></div>
                    <div>๕. นิติกรปฏิบัติการ/ชำนาญการ <span class="float-right text-slate-700">คณะทำงาน</span></div>
                    <div>๖. หัวหน้าฝ่ายอำนวยการ สำนักปลัดเทศบาล <span class="float-right font-bold text-gov-800">คณะทำงานและเลขานุการ</span></div>
                </div>

                <div class="text-xs space-y-1 pt-1">
                    <div class="font-bold">ให้คณะทำงานมีอำนาจหน้าที่ ดังต่อไปนี้:</div>
                    <div class="pl-4 space-y-0.5 text-justify">
                        <div>๑) วางแผนและกำหนดแนวทางปฏิบัติการประยุกต์ใช้ AI ในภารกิจของเทศบาล</div>
                        <div>๒) กำกับดูแลความมั่นคงปลอดภัยของข้อมูลและคุ้มครองข้อมูลส่วนบุคคล (PDPA)</div>
                        <div>๓) ติดตาม ประเมินผล และรายงานผลต่อนายกเทศมนตรีตำบลเมืองใหม่ทุกไตรมาส</div>
                    </div>
                </div>

                <div class="text-xs text-justify indent-8 pt-2">
                    ทั้งนี้ ตั้งแต่บัดนี้เป็นต้นไป
                </div>

                <div class="text-right pt-6 pr-8 text-xs space-y-8">
                    <div>สั่ง ณ วันที่ ๑ พฤศจิกายน พ.ศ. ๒๕๖๙</div>
                    <div>
                        <div class="font-bold">(นายกิตติคุณ ท้องถิ่นก้าวหน้า)</div>
                        <div class="text-slate-600">นายกเทศมนตรีตำบลเมืองใหม่</div>
                    </div>
                </div>
            </div>
        `
    },
    'doc-announce': {
        title: 'ตัวอย่างหนังสือประชาสัมพันธ์: ประกาศเทศบาลตำบลเมืองใหม่',
        subtitle: 'ประกาศกำหนดการออกให้บริการจัดเก็บภาษีเคลื่อนที่และลงทะเบียนสวัสดิการชุมชน',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-5 text-sm leading-relaxed" style="min-height: 650px;">
                <div class="text-center relative">
                    <div class="w-16 h-16 mx-auto mb-1 flex items-center justify-center font-serif text-3xl font-bold text-amber-700">
                        🦅
                    </div>
                    <h3 class="text-base font-heading font-bold">ประกาศเทศบาลตำบลเมืองใหม่</h3>
                    <div class="text-xs font-bold pt-1">เรื่อง กำหนดการออกหน่วยบริการจัดเก็บภาษีเคลื่อนที่และรับลงทะเบียนเบี้ยยังชีพ ประจำปี ๒๕๖๙</div>
                </div>

                <div class="text-xs text-justify indent-8 leading-relaxed">
                    ด้วย เทศบาลตำบลเมืองใหม่ จะดำเนินโครงการเทศบาลเคลื่อนที่เพื่ออำนวยความสะดวกแก่ประชาชนในการชำระภาษีที่ดินและสิ่งปลูกสร้าง ภาษีป้าย และรับลงทะเบียนผู้สูงอายุ ผู้พิการ และเงินอุดหนุนเด็กแรกเกิด จึงขอแจ้งกำหนดการออกให้บริการ ณ ศาลาประชาคมประจำหมู่บ้าน ตั้งแต่เวลา ๐๙.๐๐ - ๑๕.๓๐ น. ดังนี้:
                </div>

                <div class="overflow-x-auto text-xs">
                    <table class="w-full text-left border-collapse border border-slate-300">
                        <tr class="bg-slate-100 font-bold">
                            <th class="p-2 border border-slate-300">วัน/เดือน/ปี</th>
                            <th class="p-2 border border-slate-300">สถานที่ให้บริการ</th>
                            <th class="p-2 border border-slate-300">กลุ่มเป้าหมาย</th>
                        </tr>
                        <tr>
                            <td class="p-2 border border-slate-300">วันพุธที่ ๖ พ.ย. ๖๙</td>
                            <td class="p-2 border border-slate-300">ศาลาประชาคม หมู่ที่ ๑ และหมู่ที่ ๒</td>
                            <td class="p-2 border border-slate-300">ประชาชนทั่วไปในหมู่ที่ ๑-๒</td>
                        </tr>
                        <tr class="bg-slate-50">
                            <td class="p-2 border border-slate-300">วันพุธที่ ๑๓ พ.ย. ๖๙</td>
                            <td class="p-2 border border-slate-300">ศาลาประชาคม หมู่ที่ ๓ และหมู่ที่ ๔</td>
                            <td class="p-2 border border-slate-300">ประชาชนทั่วไปในหมู่ที่ ๓-๔</td>
                        </tr>
                    </table>
                </div>

                <div class="text-xs text-justify indent-8 leading-relaxed">
                    เอกสารที่ต้องนำมา: บัตรประจำตัวประชาชน, สำเนาทะเบียนบ้าน, และเอกสารสิทธิที่ดิน จึงประกาศให้ทราบโดยทั่วกัน
                </div>

                <div class="text-right pt-6 pr-8 text-xs space-y-8">
                    <div>ประกาศ ณ วันที่ ๑ พฤศจิกายน พ.ศ. ๒๕๖๙</div>
                    <div>
                        <div class="font-bold">(นายกิตติคุณ ท้องถิ่นก้าวหน้า)</div>
                        <div class="text-slate-600">นายกเทศมนตรีตำบลเมืองใหม่</div>
                    </div>
                </div>
            </div>
        `
    },
    'doc-minutes': {
        title: 'ตัวอย่างหนังสือที่เจ้าหน้าที่ทำขึ้น: รายงานการประชุมคณะทำงาน',
        subtitle: 'รายงานการประชุมคณะทำงานขับเคลื่อน AI ท้องถิ่น ครั้งที่ 1/2569 (5 ระเบียบวาระ)',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-4 text-xs leading-relaxed" style="min-height: 700px;">
                <div class="text-center border-b border-slate-200 pb-3">
                    <h3 class="text-sm font-heading font-bold text-slate-900">รายงานการประชุมคณะทำงานขับเคลื่อน AI ในงานราชการ เทศบาลตำบลเมืองใหม่</h3>
                    <div class="text-xs">ครั้งที่ ๑ / ๒๕๖๙</div>
                    <div class="text-[11px] text-slate-600">เมื่อวันศุกร์ที่ ๑ พฤศจิกายน ๒๕๖๙ ณ ห้องประชุมสภาเทศบาลตำบลเมืองใหม่</div>
                </div>

                <div class="space-y-1">
                    <div class="font-bold text-gov-800">ผู้มาประชุม:</div>
                    <div class="pl-4 text-slate-700">ปลัดเทศบาลตำบลเมืองใหม่ (ประธาน), ผอ.กองคลัง, ผอ.กองช่าง, ผอ.กองสาธารณสุขฯ, นิติกร, และ หน.ฝ่ายอำนวยการ (เลขานุการ)</div>
                </div>

                <div class="space-y-2 pt-2">
                    <div>
                        <div class="font-bold text-gov-800">ระเบียบวาระที่ ๑ : เรื่องที่ประธานแจ้งให้ที่ประชุมทราบ</div>
                        <div class="indent-6 text-justify">ประธานแจ้งนโยบายกระทรวงมหาดไทยในการยกระดับองค์กรปกครองส่วนท้องถิ่นสู่ระบบดิจิทัลและการนำ AI มาสนับสนุนงานสารบรรณและการวิเคราะห์ข้อมูล เพื่อลดระยะเวลาการทำงาน</div>
                    </div>

                    <div>
                        <div class="font-bold text-gov-800">ระเบียบวาระที่ ๒ : รับรองรายงานการประชุม</div>
                        <div class="indent-6 text-justify">เป็นการประชุมครั้งแรก จึงไม่มีรายงานการประชุมที่ต้องรับรอง</div>
                    </div>

                    <div>
                        <div class="font-bold text-gov-800">ระเบียบวาระที่ ๓ : เรื่องเสนอเพื่อทราบ</div>
                        <div class="indent-6 text-justify">เลขานุการรายงานร่างกำหนดการฝึกอบรมเชิงปฏิบัติการการใช้ AI สำหรับบุคลากร ๕๐ คน ในวันที่ ๑๕ พฤศจิกายน ๒๕๖๙</div>
                    </div>

                    <div>
                        <div class="font-bold text-gov-800">ระเบียบวาระที่ ๔ : เรื่องเสนอเพื่อพิจารณา</div>
                        <div class="indent-6 text-justify">การกำหนดมาตรการความปลอดภัยของข้อมูลราชการและข้อมูลส่วนบุคคล (PDPA) ในการใช้งาน Generative AI</div>
                        <div class="pl-6 pt-1 text-emerald-800 font-semibold">มติที่ประชุม: เห็นชอบเป็นเอกฉันท์ให้จัดทำประกาศเทศบาลเรื่อง ข้อปฏิบัติการใช้งาน AI และกำหนดห้ามนำเข้าเอกสารลับและเลขบัตร ๑๓ หลักโดยเด็ดขาด</div>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-4 pt-6 text-xs text-center border-t border-slate-200">
                    <div>(นางสาวจิตรา บริหารงาน)<br><span class="text-slate-500">ผู้จดรายงานการประชุม</span></div>
                    <div>(นายชัชวาล พัฒนาท้องถิ่น)<br><span class="text-slate-500">ผู้ตรวจรายงานการประชุม</span></div>
                </div>
            </div>
        `
    },
    'doc-summary': {
        title: 'ตัวอย่างบทสรุปสำหรับผู้บริหาร (Executive Summary)',
        subtitle: 'สรุปหนังสือเวียน สถ. สู่การปฏิบัติการของ อปท. ใน 1 หน้า A4',
        html: `
            <div class="bg-white text-slate-900 p-6 sm:p-10 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-4 text-xs leading-relaxed">
                <div class="bg-gov-800 text-white p-4 rounded-xl flex justify-between items-center">
                    <div>
                        <div class="text-[11px] text-amber-300 font-bold uppercase tracking-wider">Executive Summary สำหรับผู้บริหาร</div>
                        <h3 class="text-base font-heading font-bold text-white">สรุปหนังสือเวียนกรมส่งเสริมการปกครองท้องถิ่น ที่ มท ๐๘๐๘.๒/ว ๑๔๕๐</h3>
                    </div>
                    <span class="px-2 py-1 bg-amber-500 text-slate-950 font-bold text-xs rounded">สำคัญเร่งด่วน</span>
                </div>

                <div class="grid grid-cols-2 gap-3 p-3 bg-slate-50 rounded-lg border border-slate-200">
                    <div><strong>เรื่อง:</strong> ซักซ้อมแนวทางปฏิบัติด้านงบประมาณปี ๒๕๗๐</div>
                    <div><strong>วันที่มีผล:</strong> ๑ ตุลาคม ๒๕๖๙ เป็นต้นไป</div>
                    <div><strong>ฝ่ายประสานงาน:</strong> กองคลัง / สำนักปลัด</div>
                    <div><strong>เวลาเสนอผู้บริหาร:</strong> ภายใน ๓ วันทำการ</div>
                </div>

                <div class="space-y-1.5">
                    <h4 class="font-heading font-bold text-gov-800 text-sm">๑. สาระสำคัญและการเปลี่ยนแปลงหลัก</h4>
                    <p class="text-justify text-slate-700">
                        กระทรวงมหาดไทยได้ปรับปรุงระเบียบการจัดซื้อจัดจ้างสำหรับโครงการงบลงทุนต่ำกว่า ๕๐๐,๐๐๐ บาท ให้ใช้ระบบ e-Catalog แบบ Fast-Track เพื่อเร่งรัดการเบิกจ่ายในไตรมาสที่ ๑ โดยกำหนดให้ อปท. ต้องบันทึกราคากลางล่วงหน้าไม่น้อยกว่า ๑๕ วันทำการ
                    </p>
                </div>

                <div class="space-y-2">
                    <h4 class="font-heading font-bold text-gov-800 text-sm">๒. แผนปฏิบัติการที่ อปท. ต้องดำเนินการ (Action Checklist)</h4>
                    <table class="w-full text-left border-collapse border border-slate-200 text-xs">
                        <thead>
                            <tr class="bg-slate-100 text-slate-800 font-semibold">
                                <th class="p-2 border border-slate-200">สิ่งที่ต้องทำ</th>
                                <th class="p-2 border border-slate-200 w-32">ฝ่ายรับผิดชอบ</th>
                                <th class="p-2 border border-slate-200 w-28">กำหนดแล้วเสร็จ</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-200 text-slate-700">
                            <tr>
                                <td class="p-2 border border-slate-200">๑. รวบรวมบัญชีโครงการงบลงทุนต่ำกว่า ๕ แสนบาท</td>
                                <td class="p-2 border border-slate-200">กองช่าง / กองคลัง</td>
                                <td class="p-2 border border-slate-200 text-rose-600 font-bold">๑๕ พ.ย. ๖๙</td>
                            </tr>
                            <tr>
                                <td class="p-2 border border-slate-200">๒. จัดทำราคากลางมาตรฐานเข้าระบบ e-Catalog</td>
                                <td class="p-2 border border-slate-200">งานพัสดุ กองคลัง</td>
                                <td class="p-2 border border-slate-200 text-rose-600 font-bold">๓๐ พ.ย. ๖๙</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="p-3 bg-amber-50 border border-amber-200 rounded-lg text-amber-900 space-y-1">
                    <div class="font-bold flex items-center gap-1.5">
                        ⚠️ ข้อสังเกตและความเสี่ยงที่ผู้บริหารควรระวัง:
                    </div>
                    <div>หากไม่เริ่มกระบวนการจัดทำราคากลางภายในเดือนพฤศจิกายน จะส่งผลให้การก่อหนี้ผูกพันไม่ทันสิ้นไตรมาสที่ ๑ และอาจถูกเรียกเงินอุดหนุนคืน</div>
                </div>
            </div>
        `
    },
    'doc-facebook': {
        title: 'ตัวอย่างโพสต์ Facebook ประชาสัมพันธ์ (Citizen-Centric)',
        subtitle: 'ย่อยภาษีที่ดินและสิ่งปลูกสร้าง ให้ประชาชนเข้าใจง่ายพร้อมกราฟิกจำลอง',
        html: `
            <div class="bg-slate-100 p-4 sm:p-6 rounded-2xl max-w-xl mx-auto font-sans">
                <div class="bg-white rounded-xl shadow-md border border-slate-200 overflow-hidden text-xs">
                    <div class="p-4 flex items-center justify-between border-b border-slate-100">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-sm">
                                ทต.
                            </div>
                            <div>
                                <div class="font-heading font-bold text-slate-900 text-sm flex items-center gap-1">
                                    เทศบาลตำบลเมืองใหม่ <span class="text-blue-500">✓</span>
                                </div>
                                <div class="text-[11px] text-slate-400">เมื่อสักครู่ • 🌐 สาธารณะ</div>
                            </div>
                        </div>
                    </div>
                    <div class="p-4 space-y-3 text-slate-800 leading-relaxed text-sm">
                        <p class="font-bold text-blue-900 text-base">
                            📢 ข่าวดีชาวตำบลเมืองใหม่! ชำระภาษีที่ดินและสิ่งปลูกสร้าง ประจำปี 2569 ได้แล้ววันนี้ สะดวก สบาย ไม่ต้องรอนาน 🏠✨
                        </p>
                        <div class="p-3.5 bg-blue-50 border border-blue-200 rounded-xl space-y-2 text-xs">
                            <div class="font-bold text-blue-800 text-sm">💡 4 ช่องทางชำระภาษีสุดสะดวก:</div>
                            <div>1️⃣ ชำระ ณ กองคลัง ชั้น 1 เทศบาลตำบลเมืองใหม่</div>
                            <div>2️⃣ สแกน QR Code ผ่าน Mobile Banking ทุกธนาคาร</div>
                            <div>3️⃣ ชำระผ่านเคาน์เตอร์เซอร์วิส และ 7-Eleven ใกล้บ้าน</div>
                            <div>4️⃣ โอนผ่านบัญชี ธ.กรุงไทย เลขที่ 501-X-XXXXX-X</div>
                        </div>
                    </div>
                    <div class="bg-gradient-to-r from-blue-700 via-indigo-700 to-gov-900 p-6 text-white text-center space-y-1">
                        <div class="text-amber-300 font-bold text-xs tracking-wider">หมดเขต 30 เมษายน 2569</div>
                        <div class="text-xl font-heading font-bold">ภาษีที่ดินและสิ่งปลูกสร้าง เทศบาลตำบลเมืองใหม่</div>
                    </div>
                </div>
            </div>
        `
    },
    'doc-complaint': {
        title: 'ตัวอย่างข้อความแชทตอบกลับเรื่องร้องเรียน (Empathy & Timely)',
        subtitle: 'จำลองการตอบกลับประชาชนผ่าน LINE / Facebook Inbox เรื่องไฟกิ่งดับ',
        html: `
            <div class="bg-slate-200 p-4 sm:p-6 rounded-2xl max-w-lg mx-auto font-sans">
                <div class="bg-white rounded-2xl shadow-md border border-slate-300 overflow-hidden">
                    <div class="bg-gov-800 text-white p-3.5 flex items-center gap-3">
                        <div class="w-8 h-8 rounded-full bg-emerald-500 flex items-center justify-center font-bold text-xs">แอดมิน</div>
                        <div>
                            <div class="font-bold text-xs">ศูนย์รับเรื่องร้องทุกข์ เทศบาลตำบลเมืองใหม่</div>
                            <div class="text-[10px] text-emerald-300">● ใช้งานอยู่ • ตอบกลับทันที</div>
                        </div>
                    </div>
                    <div class="p-4 space-y-3 text-xs bg-slate-50 min-h-[260px]">
                        <div class="flex justify-end">
                            <div class="bg-blue-600 text-white p-3 rounded-2xl rounded-tr-none max-w-[80%] space-y-1 shadow-sm">
                                <div>แอดมินครับ ไฟกิ่งในซอย 5 หมู่ 2 ดับมา 3 คืนแล้ว มืดมาก อันตรายกับเด็กๆ รบกวนส่งช่างมาดูให้หน่อยครับ</div>
                                <div class="text-[9px] text-blue-200 text-right">10:14 น.</div>
                            </div>
                        </div>
                        <div class="flex justify-start">
                            <div class="bg-white border border-slate-200 text-slate-800 p-3.5 rounded-2xl rounded-tl-none max-w-[85%] space-y-2 shadow-sm">
                                <div class="text-rose-600 font-bold">❤️ เทศบาลตำบลเมืองใหม่ขออภัยในความไม่สะดวกครับ</div>
                                <div class="p-2.5 bg-blue-50 border border-blue-200 rounded-lg space-y-1">
                                    <div><strong>รหัสคำร้อง:</strong> #EF-6902 (กองช่างไฟฟ้า)</div>
                                    <div><strong>แผนการเข้าซ่อม:</strong> วันพรุ่งนี้ (ช่วงบ่าย 13.00 - 16.30 น.)</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `
    },
    'doc-swot': {
        title: 'ตัวอย่างตาราง SWOT Matrix วิเคราะห์ยุทธศาสตร์ท้องถิ่น',
        subtitle: 'ยุทธศาสตร์การพัฒนาการท่องเที่ยวเชิงวัฒนธรรมและเศรษฐกิจชุมชนริมน้ำ',
        html: `
            <div class="bg-white p-6 sm:p-8 rounded-xl shadow-lg border border-slate-300 max-w-4xl mx-auto text-xs space-y-4">
                <div class="border-b border-slate-200 pb-3 flex justify-between items-center">
                    <div>
                        <h3 class="text-base font-heading font-bold text-gov-900">SWOT Matrix : ยุทธศาสตร์การพัฒนาการท่องเที่ยวชุมชนริมน้ำ</h3>
                        <div class="text-slate-500">สังเคราะห์โดย AI ร่วมกับกลุ่มงานนโยบายและแผน เทศบาลตำบล...</div>
                    </div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-4 rounded-xl bg-emerald-50 border border-emerald-200 space-y-2">
                        <div class="font-heading font-bold text-emerald-800 text-sm">💪 จุดแข็ง (Strengths - S)</div>
                        <ul class="space-y-1 text-slate-700 list-disc pl-4">
                            <li>มีต้นทุนวัฒนธรรมริมน้ำและวัดโบราณ 200 ปี เป็นเอกลักษณ์</li>
                            <li>ชุมชนเข้มแข็ง มีวิสาหกิจชุมชนและปราชญ์ชาวบ้านจักสาน</li>
                        </ul>
                    </div>
                    <div class="p-4 rounded-xl bg-amber-50 border border-amber-200 space-y-2">
                        <div class="font-heading font-bold text-amber-800 text-sm">⚠️ จุดอ่อน (Weaknesses - W)</div>
                        <ul class="space-y-1 text-slate-700 list-disc pl-4">
                            <li>ปัญหาขยะตกค้างริมตลิ่ง ส่งผลต่อทัศนียภาพ</li>
                            <li>ขาดช่องทางการตลาดออนไลน์และการชำระเงินดิจิทัล</li>
                        </ul>
                    </div>
                </div>
            </div>
        `
    },
    'doc-workflow': {
        title: 'ตัวอย่าง Standard Operating Procedure (SOP) ดิจิทัล',
        subtitle: 'การขอรับใบอนุญาตก่อสร้าง (แบบ อ.1) ลดเวลาจาก 14 วัน เหลือ 5 วันทำการ',
        html: `
            <div class="bg-white p-6 sm:p-8 rounded-xl shadow-lg border border-slate-300 max-w-4xl mx-auto text-xs space-y-4">
                <div class="border-b border-slate-200 pb-3 flex justify-between items-center">
                    <h3 class="text-base font-heading font-bold text-gov-900">ผังกระบวนงานมาตรฐาน (SOP): การขอรับใบอนุญาตก่อสร้าง (แบบ อ.1)</h3>
                    <span class="px-2.5 py-1 bg-emerald-100 text-emerald-800 font-bold rounded-lg text-xs">ลดเวลาลง 64%</span>
                </div>
                <table class="w-full text-left border-collapse border border-slate-200 text-xs">
                    <tr class="bg-slate-100 font-bold">
                        <th class="p-2 border">ขั้นตอน</th>
                        <th class="p-2 border">กระบวนงาน</th>
                        <th class="p-2 border">เดิม</th>
                        <th class="p-2 border text-emerald-700">ปรับปรุงใหม่</th>
                    </tr>
                    <tr>
                        <td class="p-2 border">1</td>
                        <td class="p-2 border">ยื่นคำขอและตรวจเอกสารหลักฐานเบื้องต้น</td>
                        <td class="p-2 border">2 วัน</td>
                        <td class="p-2 border text-emerald-700 font-bold">1 วัน</td>
                    </tr>
                    <tr>
                        <td class="p-2 border">2</td>
                        <td class="p-2 border">ตรวจแบบแปลนและลงพื้นที่ตรวจสอบ</td>
                        <td class="p-2 border">7 วัน</td>
                        <td class="p-2 border text-emerald-700 font-bold">2 วัน</td>
                    </tr>
                </table>
            </div>
        `
    },
    'doc-ethics': {
        title: 'ตัวอย่างเปรียบเทียบ Good Prompt vs Bad Prompt ในงาน อปท.',
        subtitle: 'แนวทางปฏิบัติตาม พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล พ.ศ. 2562 (PDPA)',
        html: `
            <div class="bg-white p-6 sm:p-8 rounded-xl shadow-lg border border-slate-300 max-w-4xl mx-auto text-xs space-y-4">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-4 rounded-xl bg-rose-50 border border-rose-200 space-y-2">
                        <div class="font-heading font-bold text-rose-800 text-sm">❌ Bad Prompt (ละเมิด PDPA)</div>
                        <div class="p-3 bg-white rounded border border-rose-200 text-slate-700 font-mono text-[11px]">
                            "ช่วยสรุปข้อร้องเรียนของนายสมศักดิ์ รักดี เลขบัตร 3-5099-00123-45-6 บ้านเลขที่ 99 หมู่ 3 ที่มาร้องเรียนว่านายกฮั้วประมูลหน่อย"
                        </div>
                    </div>
                    <div class="p-4 rounded-xl bg-emerald-50 border border-emerald-200 space-y-2">
                        <div class="font-heading font-bold text-emerald-800 text-sm">✅ Good Prompt (ปลอดภัย 100%)</div>
                        <div class="p-3 bg-white rounded border border-emerald-200 text-slate-700 font-mono text-[11px]">
                            "บทบาท: เจ้าหน้าที่นิติกร เทศบาล... งาน: ร่างแบบฟอร์มตรวจสอบข้อเท็จจริงกระบวนการจัดซื้อจัดจ้างตาม พ.ร.บ. จัดซื้อจัดจ้างฯ 2560"
                        </div>
                    </div>
                </div>
            </div>
        `
    }
};
"""

with open('/Users/hanaharper/Downloads/AI_LG/document_previews.js', 'w', encoding='utf-8') as f:
    f.write(doc_previews)

print("Updated document_previews.js with all 6 gov doc types!")

# 2. Build full slides_data.js with ALL 6 types as dedicated slides and interactive jump links
slides = [
    # 0. Title & Roadmap
    {
        "id": 1,
        "module": "บทนำหลักสูตร",
        "badge": "โครงการฝึกอบรมเชิงปฏิบัติการ",
        "title": "การประยุกต์ใช้ AI เพื่อยกระดับการทำงานขององค์กรปกครองส่วนท้องถิ่น (อปท.)",
        "subtitle": "Practical AI for Local Government: จากงานสารบรรณ สู่การบริหารยุทธศาสตร์และบริการประชาชน",
        "type": "hero",
        "content": {
            "features": [
                {"icon": "pen-tool", "title": "ร่างหนังสือราชการ 6 ชนิด", "desc": "หนังสือภายนอก ภายใน ประทับตรา สั่งการ ประชาสัมพันธ์ และหนังสือ จนท."},
                {"icon": "megaphone", "title": "สื่อสารประชาชน", "desc": "ย่อยกฎหมายภาษีที่ดินฯ สื่อโซเชียล ตอบข้อร้องเรียน"},
                {"icon": "trending-up", "title": "ยุทธศาสตร์ & งบประมาณ", "desc": "SWOT ท้องถิ่น งบประมาณ 5 ปี และ Root Cause"},
                {"icon": "shield-check", "title": "จริยธรรม & PDPA", "desc": "รักษาความลับราชการ กฎหมาย PDPA และ 3 Dos & 3 Don'ts"}
            ],
            "footer_note": "หลักสูตรฝึกปฏิบัติจริง (Hands-on Workshop) อ้างอิงระเบียบงานสารบรรณ พ.ศ. 2526 และแก้ไขเพิ่มเติม"
        },
        "notes": "กล่าวต้อนรับผู้บริหาร ปลัด และข้าราชการ/พนักงาน อปท. ทุกท่าน เน้นย้ำว่า AI ไม่ได้มาแทนที่คน แต่คนท้องถิ่นที่ใช้ AI เป็น จะทำงานได้รวดเร็ว ถูกต้อง และบริการประชาชนได้อย่างมีประสิทธิภาพยิ่งขึ้น"
    },
    {
        "id": 2,
        "module": "ภาพรวมหลักสูตร",
        "badge": "Roadmap การเรียนรู้",
        "title": "โครงสร้างการฝึกอบรม 7 โมดูลหลัก",
        "subtitle": "เส้นทางการเรียนรู้ตั้งแต่พื้นฐานคำสั่ง สู่การประยุกต์ใช้งานจริงในทุกภารกิจของ อปท.",
        "type": "grid_roadmap",
        "content": {
            "modules": [
                {"code": "Module 1", "name": "หลักการเขียน Prompt งานราชการ", "desc": "โครงสร้างสูตร RTCF 4 องค์ประกอบ และเทคนิค Iterative Prompting"},
                {"code": "Module 2", "name": "ระเบียบสารบรรณ 6 ชนิด กับ AI", "desc": "หนังสือภายนอก ภายใน ประทับตรา สั่งการ ประชาสัมพันธ์ และหนังสือ จนท."},
                {"code": "Module 3", "name": "AI จัดทำ & สรุปเอกสาร อปท.", "desc": "สรุปหนังสือเวียน สถ. สู่ Executive Summary & ตรวจร่างข้อบัญญัติ"},
                {"code": "Module 4", "name": "AI เพื่อการประชาสัมพันธ์", "desc": "ย่อยภาษีที่ดินฯ สื่อสารเชิงรุก และตอบกลับประชาชนด้วย Empathy"},
                {"code": "Module 5", "name": "วิเคราะห์แผนงาน & งบประมาณ", "desc": "SWOT การท่องเที่ยว วิเคราะห์งบประมาณ 5 ปี & Root Cause Analysis"},
                {"code": "Module 6", "name": "ออกแบบ Workflow & ร้องทุกข์", "desc": "SOP ขออนุญาตก่อสร้าง (แบบ อ.1) & จัดกลุ่มข้อมูล Traffy Fondue"},
                {"code": "Module 7", "name": "จริยธรรม PDPA & Action Plan", "desc": "ชั้นความลับข้อมูลราชการ, PDPA, 3 Dos & 3 Don'ts และแผน 30 วัน"}
            ]
        },
        "notes": "อธิบาย Roadmap 7 ขั้นตอน ชี้แจงว่าจะเริ่มจากโครงสร้างคำสั่งก่อน จากนั้นเจาะระเบียบสารบรรณ แล้วขยายสู่งานประชาสัมพันธ์ ยุทธศาสตร์ กระบวนงาน และปิดท้ายด้วยความปลอดภัยทางกฎหมาย"
    },

    # 1. Prompt Structure (Separated)
    {
        "id": 3,
        "module": "ส่วนที่ 1 : โครงสร้าง Prompt",
        "badge": "สูตร RTCF",
        "title": "ศาสตร์แห่งการสั่งการ: โครงสร้าง Prompt 4 องค์ประกอบ (RTCF)",
        "subtitle": "สูตรมาตรฐานสากลที่ปรับใช้สำหรับงานราชการไทย เพื่อให้ AI ตอบได้แม่นยำตั้งแต่ครั้งแรก",
        "type": "prompt_formula",
        "content": {
            "elements": [
                {
                    "letter": "R",
                    "name": "บทบาท (Role)",
                    "desc": "กำหนดตำแหน่ง หน้าที่ และสังกัด เพื่อให้ AI สวมบทบาทและใช้ฐานความคิดที่ถูกต้อง",
                    "example": "เช่น 'คุณคือนักจัดการงานทั่วไปชำนาญการ สังกัดสำนักปลัด เทศบาล...'"
                },
                {
                    "letter": "T",
                    "name": "งานที่ต้องการ (Task)",
                    "desc": "ระบุภารกิจหรือผลงานที่ต้องการอย่างชัดเจน ไม่คลุมเครือ",
                    "example": "เช่น 'ร่างหนังสือราชการภายนอก เพื่อขอความอนุเคราะห์วิทยากร...'"
                },
                {
                    "letter": "C",
                    "name": "บริบท & ข้อมูลสำคัญ (Context)",
                    "desc": "ใส่ข้อเท็จจริง วัน เวลา สถานที่ วัตถุประสงค์ กลุ่มเป้าหมาย ผู้ลงนาม และงบประมาณ",
                    "example": "เช่น 'จัดอบรมวันที่ 15 พ.ย. 69 ผู้เข้าอบรม 50 คน ผู้ลงนามคือนายกเทศมนตรี...'"
                },
                {
                    "letter": "F",
                    "name": "รูปแบบภาษา & โครงสร้าง (Format)",
                    "desc": "กำหนดระดับภาษาทางการและโครงสร้างเอกสารตามระเบียบงานสารบรรณ",
                    "example": "เช่น 'ใช้ภาษาราชการตามระเบียบสารบรรณ 2526 แบ่งเหตุที่มีหนังสือไปและจุดประสงค์'"
                }
            ]
        },
        "notes": "เน้นย้ำสูตร RTCF อธิบายว่าทำไมการสั่งสั้นๆ แบบเดิมจึงไม่ได้ผล การใส่ครบ 4 ส่วนจะทำให้ได้งานพร้อมใช้ทันที"
    },
    {
        "id": 4,
        "module": "ส่วนที่ 1 : โครงสร้าง Prompt",
        "badge": "เจาะลึกองค์ประกอบ",
        "title": "เจาะลึก R (Role) & T (Task) สำหรับบุคลากร อปท.",
        "subtitle": "การกำหนดฐานความคิดและขอบเขตงานให้ AI ทำงานตรงตามสายงาน",
        "type": "two_column",
        "content": {
            "left_title": "🎯 การกำหนดบทบาท (Role) ตามกอง/ฝ่าย",
            "left_items": [
                "สำนักปลัด: 'คุณคือนักจัดการงานทั่วไปชำนาญการ ผู้เชี่ยวชาญระเบียบงานสารบรรณและการบริหารงานบุคคลท้องถิ่น'",
                "กองคลัง: 'คุณคือนักวิชาการเงินและบัญชี / นิติกรชำนาญการ ผู้เชี่ยวชาญระเบียบการเบิกจ่ายและ พ.ร.บ. จัดซื้อจัดจ้างฯ 2560'",
                "กองช่าง: 'คุณคือนายช่างโยธาชำนาญงาน ผู้ดูแลการควบคุมอาคารตาม พ.ร.บ. ควบคุมอาคาร พ.ศ. 2522'",
                "กองสาธารณสุข: 'คุณคือนักวิชาการสุขาภิบาลชำนาญการ ผู้ดูแลสุขอนามัยชุมชนและการจัดการขยะมูลฝอย'"
            ],
            "right_title": "⚡ การระบุคำสั่งงาน (Task) ที่ชัดเจนและวัดผลได้",
            "right_items": [
                "คำกริยาที่ทรงพลัง: 'ร่าง', 'สรุปเปรียบเทียบ', 'วิเคราะห์หาสาเหตุ', 'จัดทำ Checklist', 'ย่อยภาษา'",
                "ระบุประเภทเอกสาร: ระบุให้ชัดว่าต้องการ 'บันทึกข้อความ', 'หนังสือภายนอก', หรือ 'ประกาศ'",
                "ระบุผู้รับสาร: ต้องการให้ใครอ่าน เช่น 'สำหรับเสนอผู้บริหารระดับสูง (ปลัด/นายก)' หรือ 'สำหรับประชาชนทั่วไป'",
                "หลีกเลี่ยงคำสั่งคลุมเครือ: อย่าสั่งแค่ 'ช่วยดูให้หน่อย' หรือ 'เขียนมาให้ดีๆ'"
            ]
        },
        "notes": "ให้ผู้เรียนสังเกตความแตกต่างเมื่อใส่ Role ที่เจาะจง กองคลัง vs สำนักปลัด AI จะเลือกใช้ศัพท์เทคนิคและระเบียบที่เกี่ยวข้องต่างกันอย่างสิ้นเชิง"
    },
    {
        "id": 5,
        "module": "ส่วนที่ 1 : โครงสร้าง Prompt",
        "badge": "เจาะลึกองค์ประกอบ",
        "title": "เจาะลึก C (Context) & F (Format) เพื่อผลลัพธ์พร้อมใช้",
        "subtitle": "การป้อนข้อเท็จจริงที่ครบถ้วนและบังคับรูปแบบผลลัพธ์ให้ตรงตามระเบียบ",
        "type": "two_column",
        "content": {
            "left_title": "📋 บริบทและข้อเท็จจริงสำคัญ (Context)",
            "left_items": [
                "วันที่และเวลา: ระบุวันจัดงาน หรือกำหนดส่งมอบงานที่แน่นอน",
                "กลุ่มเป้าหมายและสถานที่: ใครเข้าร่วม จำนวนกี่คน ณ สถานที่ใด",
                "ผู้ลงนามและหน่วยงาน: ใครเป็นผู้ลงนาม (เช่น นายกเทศมนตรี / ปลัดเทศบาล) และส่งถึงใคร",
                "งบประมาณและโครงการ: โครงการตามแผนพัฒนาท้องถิ่น งบประมาณหมวดใด จำนวนเท่าใด",
                "ข้อจำกัด: เช่น 'จำกัดความยาวไม่เกิน 1 หน้ากระดาษ A4'"
            ],
            "right_title": "📄 การกำหนดรูปแบบผลลัพธ์ (Format)",
            "right_items": [
                "โครงสร้างสารบรรณ 3 ส่วน: 1. เหตุที่มีหนังสือไป 2. จุดประสงค์และความจำเป็น 3. คำลงท้าย",
                "ตารางสรุปเปรียบเทียบ: กำหนดหัวคอลัมน์ เช่น 'ระเบียบเดิม | ระเบียบใหม่ | สิ่งที่ อปท. ต้องปฏิบัติ'",
                "Checklist ขั้นตอน: สั่งให้แสดงเป็นข้อๆ พร้อมช่องทำเครื่องหมาย [ ]",
                "ระดับภาษา (Tone): 'ภาษาราชการระดับสูง', 'ภาษาทางการกระชับ', หรือ 'ภาษาเป็นกันเองสำหรับประชาชน (Citizen-friendly)'"
            ]
        },
        "notes": "เน้นย้ำว่าถ้าเราไม่บอก Format AI มักจะตอบยาวเป็นพืด หรือใส่หัวข้อที่ไม่ได้ใช้ในหนังสือราชการ"
    },
    {
        "id": 6,
        "module": "ส่วนที่ 1 : โครงสร้าง Prompt",
        "badge": "เทคนิคการสั่งปรับแก้",
        "title": "Iterative Prompting: เทคนิคการขัดเกลาคำสั่งต่อเนื่อง",
        "subtitle": "เมื่อผลลัพธ์รอบแรกยังไม่สมบูรณ์ 100% ควรต่อยอดคำสั่งอย่างไรให้ได้งานที่เป๊ะที่สุด",
        "type": "comparison",
        "content": {
            "items": [
                {
                    "title": "❌ คำสั่งแก้แบบคลุมเครือ (ไม่แนะนำ)",
                    "desc": "\"ยังไม่ค่อยดี ช่วยเขียนใหม่ให้เพราะกว่านี้หน่อย\"\n\"ขอทางการกว่านี้อีกนิด\"\n\nผลกระทบ: AI จะสุ่มเดาความต้องการ และมักรื้อโครงสร้างเดิมที่ทำไว้ดีแล้วทิ้งทั้งหมด"
                },
                {
                    "title": "✅ คำสั่งปรับแก้แบบชี้จุดเฉพาะ (แนะนำ)",
                    "desc": "\"ในย่อหน้าที่ 2 ช่วยปรับคำว่า 'ขอเชิญ' เป็น 'ขอความอนุเคราะห์' และเพิ่มประโยคเรื่องเบิกจ่ายค่าตอบแทนวิทยากรตามระเบียบกระทรวงมหาดไทย\"\n\nผลลัพธ์: AI แก้ไขเฉพาะจุดที่ระบุ โดยยังคงรักษาโครงสร้างส่วนอื่นไว้อย่างสมบูรณ์"
                },
                {
                    "title": "✅ เทคนิคคุมความยาวและรูปแบบ",
                    "desc": "\"ขอให้ย่อสรุปเนื้อหาในส่วน 'ข้อเท็จจริง' ให้เหลือไม่เกิน 5 บรรทัด และจัดทำเป็นข้อ 1, 2, 3\"\n\nผลลัพธ์: ได้ข้อความกระชับ ตรงตามธรรมเนียมการเสนอแฟ้มบันทึกข้อความต่อผู้บริหาร"
                }
            ]
        },
        "notes": "สอนให้ผู้เรียนมอง AI เหมือนการตรวจงานลูกน้อง เมื่อลูกน้องทำมายังไม่เป๊ะ อย่าเพิ่งโยนทิ้ง ให้สั่งแก้เฉพาะจุด"
    },

    # 2. Government Documents - Interactive Menu Slide (Slide 7)
    {
        "id": 7,
        "module": "ส่วนที่ 2 : ระเบียบงานสารบรรณ",
        "badge": "Module 2 : คลิกการ์ดเพื่อกระโดดดูตัวอย่าง",
        "title": "ระเบียบสำนักนายกรัฐมนตรีว่าด้วยงานสารบรรณ พ.ศ. 2526 (หนังสือ 6 ชนิด)",
        "subtitle": "คลิกที่การ์ดประเภทหนังสือใดก็ได้ เพื่อกระโดดไปยังสไลด์ตัวอย่าง Prompt และดูตัวอย่างเอกสารจริงทันที",
        "type": "gov_types_interactive",
        "content": {
            "types": [
                {
                    "num": "1",
                    "title": "หนังสือภายนอก",
                    "desc": "ติดต่อระหว่างส่วนราชการ หรือหน่วยงานภายนอก/บุคคลภายนอก",
                    "detail": "กระดาษตราครุฑ (สูง 3 ซม.) ลงนามโดยนายกเทศมนตรี/นายก อบต.",
                    "target_slide": 8,
                    "target_label": "สไลด์ที่ 8"
                },
                {
                    "num": "2",
                    "title": "หนังสือภายใน",
                    "desc": "ติดต่อภายในกระทรวง กรม จังหวัด หรือภายใน อปท. เดียวกัน",
                    "detail": "กระดาษบันทึกข้อความ (ครุฑสูง 1.5 ซม.) พิธีการน้อยกว่า ไม่มีคำลงท้าย",
                    "target_slide": 9,
                    "target_label": "สไลด์ที่ 9"
                },
                {
                    "num": "3",
                    "title": "หนังสือประทับตรา",
                    "desc": "ใช้ประทับตราแทนการลงชื่อในเรื่องที่ไม่สำคัญมาก",
                    "detail": "ใช้กระดาษตราครุฑ หมึกสีชาด ส่งเอกสาร/แจ้งเตือน/ขอรายละเอียด",
                    "target_slide": 10,
                    "target_label": "สไลด์ที่ 10"
                },
                {
                    "num": "4",
                    "title": "หนังสือสั่งการ",
                    "desc": "มี 3 ชนิด: คำสั่ง, ข้อบังคับ, ระเบียบ",
                    "detail": "ผู้มีอำนาจสั่งให้ปฏิบัติโดยชอบด้วยกฎหมาย มีผลบังคับทางปกครอง",
                    "target_slide": 11,
                    "target_label": "สไลด์ที่ 11"
                },
                {
                    "num": "5",
                    "title": "หนังสือประชาสัมพันธ์",
                    "desc": "มี 3 ชนิด: ประกาศ, แถลงการณ์, ข่าว",
                    "detail": "ชี้แจงให้ทราบ กำหนดแนวทาง หรือเผยแพร่แก่สาธารณชน",
                    "target_slide": 12,
                    "target_label": "สไลด์ที่ 12"
                },
                {
                    "num": "6",
                    "title": "หนังสือที่ จนท. ทำขึ้น",
                    "desc": "หนังสือรับรอง, รายงานการประชุม, บันทึก",
                    "detail": "เอกสารที่เจ้าหน้าที่จัดทำขึ้นหรือรับไว้เป็นหลักฐานในราชการ",
                    "target_slide": 13,
                    "target_label": "สไลด์ที่ 13"
                }
            ]
        },
        "notes": "นี่คือหน้าสารบัญ Interactive วิทยากรหรือผู้เรียนสามารถคลิกที่การ์ดใดก็ได้ เพื่อกระโดดไปยังสไลด์ตัวอย่างของหนังสือชนิดนั้นทันที"
    },

    # Dedicated Slide for Type 1
    {
        "id": 8,
        "module": "ส่วนที่ 2 : ระเบียบงานสารบรรณ",
        "badge": "ประเภทที่ 1 : หนังสือภายนอก",
        "title": "ตัวอย่าง Prompt: ร่างหนังสือราชการภายนอก (ขอความอนุเคราะห์วิทยากร)",
        "subtitle": "การร่างหนังสือติดต่อหน่วยงานภายนอก (มหาวิทยาลัยราชภัฏ) ใช้กระดาษตราครุฑ",
        "type": "prompt_display",
        "content": {
            "prompt_text": "บทบาท: คุณคือนักจัดการงานทั่วไปชำนาญการ สังกัดสำนักปลัด เทศบาลตำบลเมืองใหม่\nงานที่ต้องการให้ทำ: ร่างหนังสือราชการภายนอก (ใช้กระดาษตราครุฑ) ถึงอธิการบดีมหาวิทยาลัยราชภัฏในพื้นที่ เพื่อขอความอนุเคราะห์บุคลากรเป็นวิทยากร\nบริบทและข้อมูลสำคัญ:\n- โครงการฝึกอบรมการประยุกต์ใช้ AI ในงานราชการ วันศุกร์ที่ 15 พฤศจิกายน 2569 เวลา 09.00 - 16.00 น. ณ ห้องประชุมเทศบาลตำบลเมืองใหม่\n- กลุ่มเป้าหมายคือข้าราชการและพนักงานเทศบาล 50 คน\n- เทศบาลยินดีสนับสนุนค่าสมนาคุณวิทยากรและค่าพาหนะตามระเบียบกระทรวงมหาดไทย\n- ผู้ลงนามคือนายกเทศมนตรีตำบลเมืองใหม่\nรูปแบบภาษาและผลลัพธ์:\n- ใช้ภาษาราชการถูกต้องตามระเบียบสำนักนายกรัฐมนตรีว่าด้วยงานสารบรรณ พ.ศ. 2526\n- แบ่งโครงสร้างเป็น 3 ย่อหน้า: 1. เหตุที่มีหนังสือไป 2. จุดประสงค์และความจำเป็น 3. สรุปความต้องการและคำลงท้าย (ขอแสดงความนับถือ)",
            "key_takeaway": "จุดเด่น: ระบุชัดเจนเรื่องระเบียบเบิกจ่ายค่าสมนาคุณ และโครงสร้าง 3 ย่อหน้าตามสารบรรณ",
            "preview_id": "doc-external"
        },
        "notes": "คลิกปุ่มดูตัวอย่างหนังสือตราครุฑฉบับเต็ม ชี้ให้เห็นการจัดวางหัวหนังสือ วันที่ และคำลงท้ายตามระเบียบสารบรรณ 2526"
    },

    # Dedicated Slide for Type 2
    {
        "id": 9,
        "module": "ส่วนที่ 2 : ระเบียบงานสารบรรณ",
        "badge": "ประเภทที่ 2 : หนังสือภายใน",
        "title": "ตัวอย่าง Prompt: ร่างบันทึกข้อความ (ขออนุมัติจัดโครงการและงบประมาณ)",
        "subtitle": "การร่างหนังสือภายในเสนอผู้บริหารท้องถิ่น โครงสร้าง 3 ส่วน (ต้นเรื่อง - ข้อเท็จจริง - ข้อเสนอ)",
        "type": "prompt_display",
        "content": {
            "prompt_text": "บทบาท: คุณคือนักจัดการงานทั่วไปชำนาญการ สังกัดสำนักปลัด เทศบาลตำบลเมืองใหม่\nงานที่ต้องการให้ทำ: ร่างหนังสือราชการภายใน (กระดาษบันทึกข้อความ) เสนอต่อนายกเทศมนตรีตำบลเมืองใหม่ เพื่อขออนุมัติจัดโครงการและเบิกจ่ายงบประมาณ\nบริบทและข้อมูลสำคัญ:\n- เรื่อง: ขออนุมัติจัดโครงการฝึกอบรมการใช้ AI ในงานราชการ ประจำปีงบประมาณ พ.ศ. 2569\n- วันศุกร์ที่ 15 พฤศจิกายน 2569 ณ ห้องประชุมเทศบาลฯ กลุ่มเป้าหมาย 50 คน\n- ใช้งบประมาณหมวดค่าใช้สอย โครงการพัฒนาบุคลากร จำนวน 25,000 บาท\nรูปแบบภาษาและผลลัพธ์:\n- จัดรูปแบบบันทึกข้อความ: ส่วนหัว (ข้อความ ส่วนราชการ ที่ วันที่ เรื่อง)\n- เนื้อหา 3 ส่วน: 1. ต้นเรื่อง 2. ข้อเท็จจริง/รายละเอียดโครงการ 3. ข้อพิจารณาและข้อเสนอ\n- ใช้ภาษาทางการ กะทัดรัด ชัดเจน (ไม่มีคำลงท้าย ขอแสดงความนับถือ)",
            "key_takeaway": "จุดเด่น: โครงสร้าง ต้นเรื่อง / ข้อเท็จจริง / ข้อพิจารณาและข้อเสนอ เป็นหัวใจของบันทึกข้อความราชการไทย",
            "preview_id": "doc-internal"
        },
        "notes": "กดปุ่มดูตัวอย่างบันทึกข้อความฉบับเต็ม ชี้ให้เห็นว่าไม่มีคำว่า 'ขอแสดงความนับถือ' แต่จบด้วย 'จึงเรียนมาเพื่อโปรดพิจารณา หากเห็นชอบโปรดอนุมัติ...'"
    },

    # Dedicated Slide for Type 3
    {
        "id": 10,
        "module": "ส่วนที่ 2 : ระเบียบงานสารบรรณ",
        "badge": "ประเภทที่ 3 : หนังสือประทับตรา",
        "title": "ตัวอย่าง Prompt: ร่างหนังสือประทับตรา (ส่งรายงานสถิติประจำเดือน)",
        "subtitle": "หนังสือที่ใช้ประทับตราแทนการลงชื่อในเรื่องไม่สำคัญ เช่น ส่งเอกสาร แบบตอบรับ หรือแจ้งเตือน",
        "type": "prompt_display",
        "content": {
            "prompt_text": "บทบาท: เจ้าพนักงานธุรการ กองยุทธศาสตร์และงบประมาณ เทศบาลตำบลเมืองใหม่\nงานที่ต้องการให้ทำ: ร่างหนังสือประทับตรา (ใช้กระดาษตราครุฑ) สำหรับนำส่งรายงานสถิติการให้บริการประชาชนและการจัดเก็บรายได้ ประจำเดือนตุลาคม 2569\nบริบทและข้อมูลสำคัญ:\n- ส่งถึง: สำนักงานส่งเสริมการปกครองท้องถิ่นอำเภอเมืองเชียงใหม่\n- อ้างถึง: หนังสือแจ้งเวียนของจังหวัดเชียงใหม่ เรื่อง การส่งรายงานสถิติประจำเดือน\n- รายละเอียด: ส่งรายงานสถิติ จำนวน 1 ชุด ภายในกำหนดวันที่ 1 พฤศจิกายน 2569\nรูปแบบภาษาและผลลัพธ์:\n- รูปแบบหนังสือประทับตราตามระเบียบงานสารบรรณ พ.ศ. 2526 (ระบุ ที่, ถึง, ข้อความสั้นกระชับตรงประเด็น, ชื่อส่วนราชการที่ส่งออก, วันที่)\n- ไม่มีการลงลายมือชื่อบุคคล ให้ทำพื้นที่วงกลมระบุการประทับตราชื่อเทศบาลด้วยหมึกสีชาด",
            "key_takeaway": "จุดเด่น: หนังสือประทับตราใช้สำหรับเรื่องทั่วไป ไม่ลงชื่อนายกฯ แต่ประทับตราชื่อส่วนราชการ",
            "preview_id": "doc-seal"
        },
        "notes": "คลิกปุ่มดูตัวอย่างหนังสือประทับตรา ชี้ให้เห็นการประทับตราชื่อเทศบาลด้วยหมึกสีชาดแทนการลงลายมือชื่อ"
    },

    # Dedicated Slide for Type 4
    {
        "id": 11,
        "module": "ส่วนที่ 2 : ระเบียบงานสารบรรณ",
        "badge": "ประเภทที่ 4 : หนังสือสั่งการ",
        "title": "ตัวอย่าง Prompt: ร่างคำสั่งเทศบาลตำบลเมืองใหม่ (หนังสือสั่งการ)",
        "subtitle": "การร่างคำสั่งแต่งตั้งคณะทำงานขับเคลื่อนการประยุกต์ใช้ AI ในงานราชการ",
        "type": "prompt_display",
        "content": {
            "prompt_text": "บทบาท: นิติกรชำนาญการ ร่วมกับสำนักปลัด เทศบาลตำบลเมืองใหม่\nงานที่ต้องการให้ทำ: ร่างคำสั่งเทศบาลตำบลเมืองใหม่ เรื่อง แต่งตั้งคณะทำงานขับเคลื่อนการประยุกต์ใช้ปัญญาประดิษฐ์ (AI) ในงานราชการ ประจำปี 2569\nบริบทและข้อมูลสำคัญ:\n- ฐานอำนาจ: อาศัยอำนาจตามมาตรา 48 เตรส แห่งพระราชบัญญัติเทศบาล พ.ศ. 2496 และที่แก้ไขเพิ่มเติม\n- องค์ประกอบคณะทำงาน: ปลัดเทศบาล (ประธาน), ผอ.กองคลัง, ผอ.กองช่าง, ผอ.กองสาธารณสุขฯ, นิติกร เป็นคณะทำงาน และ หน.ฝ่ายอำนวยการ เป็นเลขานุการ\n- อำนาจหน้าที่: วางแผนการใช้ AI, กำกับดูแลความปลอดภัยข้อมูลและ PDPA, และรายงานผลต่อนายกเทศมนตรี\nรูปแบบภาษาและผลลัพธ์:\n- รูปแบบคำสั่งราชการ: 1. ส่วนหัวคำสั่ง 2. อารัมภบทปรารภเหตุผล 3. รายชื่อคณะทำงานและอำนาจหน้าที่ 4. 'ทั้งนี้ ตั้งแต่บัดนี้เป็นต้นไป สั่ง ณ วันที่...' ลงนามโดยนายกเทศมนตรี",
            "key_takeaway": "จุดเด่น: มีผลบังคับใช้ทางปกครอง ต้องอ้างฐานอำนาจตามกฎหมายจัดตั้ง อปท. ให้ถูกต้อง",
            "preview_id": "doc-order"
        },
        "notes": "คลิกปุ่มดูตัวอย่างคำสั่งราชการฉบับเต็ม ชี้ให้เห็นการอ้างฐานอำนาจตาม พ.ร.บ. เทศบาล และโครงสร้างคำสั่ง"
    },

    # Dedicated Slide for Type 5
    {
        "id": 12,
        "module": "ส่วนที่ 2 : ระเบียบงานสารบรรณ",
        "badge": "ประเภทที่ 5 : หนังสือประชาสัมพันธ์",
        "title": "ตัวอย่าง Prompt: ร่างประกาศเทศบาลตำบลเมืองใหม่ (หนังสือประชาสัมพันธ์)",
        "subtitle": "การร่างประกาศกำหนดการออกหน่วยบริการจัดเก็บภาษีเคลื่อนที่และลงทะเบียนสวัสดิการ",
        "type": "prompt_display",
        "content": {
            "prompt_text": "บทบาท: นักประชาสัมพันธ์ชำนาญการ ร่วมกับกองคลัง เทศบาลตำบลเมืองใหม่\nงานที่ต้องการให้ทำ: ร่างหนังสือประชาสัมพันธ์ ประเภท 'ประกาศ' เรื่อง กำหนดการออกหน่วยบริการจัดเก็บภาษีเคลื่อนที่และรับลงทะเบียนสวัสดิการชุมชน ประจำปี 2569\nบริบทและข้อมูลสำคัญ:\n- วัตถุประสงค์: ชี้แจงกำหนดการออกให้บริการประชาชนในหมู่ที่ 1 ถึงหมู่ที่ 4 ณ ศาลาประชาคมหมู่บ้าน ตลอดเดือนพฤศจิกายน 2569 เวลา 09.00 - 15.30 น.\n- ภารกิจที่ให้บริการ: ชำระภาษีที่ดินและสิ่งปลูกสร้าง, ภาษีป้าย, ลงทะเบียนเบี้ยยังชีพผู้สูงอายุและคนพิการ\n- เอกสารที่ประชาชนต้องเตรียม: บัตรประชาชน, ทะเบียนบ้าน, เอกสารสิทธิที่ดิน\nรูปแบบภาษาและผลลัพธ์:\n- รูปแบบประกาศราชการ: ส่วนหัวประกาศตราครุฑ (ประกาศเทศบาลตำบลเมืองใหม่ เรื่อง...), เนื้อหาชี้แจงรายละเอียด, 'จึงประกาศให้ทราบโดยทั่วกัน', 'ประกาศ ณ วันที่...' ลงนามโดยนายกเทศมนตรี",
            "key_takeaway": "จุดเด่น: รูปแบบประกาศราชการสำหรับแจ้งให้สาธารณชนทราบอย่างเป็นทางการ",
            "preview_id": "doc-announce"
        },
        "notes": "คลิกปุ่มดูตัวอย่างประกาศเทศบาลฉบับเต็ม ชี้ให้เห็นการจัดตารางวันเวลาออกหน่วยบริการเคลื่อนที่"
    },

    # Dedicated Slide for Type 6
    {
        "id": 13,
        "module": "ส่วนที่ 2 : ระเบียบงานสารบรรณ",
        "badge": "ประเภทที่ 6 : หนังสือที่ จนท. ทำขึ้น",
        "title": "ตัวอย่าง Prompt: ร่างรายงานการประชุมสภา / คณะทำงาน (5 วาระ)",
        "subtitle": "การร่างรายงานการประชุมคณะทำงานขับเคลื่อน AI ท้องถิ่น ครั้งที่ 1/2569",
        "type": "prompt_display",
        "content": {
            "prompt_text": "บทบาท: นักจัดการงานทั่วไปชำนาญการ เลขานุการคณะทำงาน เทศบาลตำบลเมืองใหม่\nงานที่ต้องการให้ทำ: ร่างรายงานการประชุมคณะทำงานขับเคลื่อน AI ในงานราชการ ครั้งที่ 1/2569\nบริบทและข้อมูลสำคัญ:\n- ประชุมเมื่อวันศุกร์ที่ 1 พฤศจิกายน 2569 ณ ห้องประชุมเทศบาลฯ ปลัดเทศบาลเป็นประธาน ผู้เข้าร่วมคือ ผอ.ทุกกอง\n- วาระสำคัญ: 1. แจ้งนโยบาย AI มท. 2. แผนการจัดอบรมบุคลากร 50 คน วันที่ 15 พ.ย. 69 3. การกำหนดมาตรการคุ้มครองข้อมูลส่วนบุคคล (PDPA) ห้ามนำข้อมูลลับและเลขบัตร 13 หลักเข้า AI\nรูปแบบภาษาและผลลัพธ์:\n- รูปแบบรายงานการประชุมตามระเบียบงานสารบรรณ พ.ศ. 2526 (ภาค 2)\n- แบ่งเป็น 5 ระเบียบวาระ พร้อมระบุ 'มติที่ประชุม' ที่เป็นทางการและชัดเจนในแต่ละวาระ",
            "key_takeaway": "จุดเด่น: แปลงภาษาพูดจากการประชุมให้เป็นสำนวนสารบรรณ และบันทึกมติอย่างรัดกุม",
            "preview_id": "doc-minutes"
        },
        "notes": "คลิกปุ่มดูตัวอย่างรายงานการประชุม 5 วาระฉบับเต็ม พร้อมมติที่ประชุมและช่องลงชื่อผู้จด/ตรวจรายงาน"
    },

    # 3. Document Analysis & Circulars
    {
        "id": 14,
        "module": "ส่วนที่ 3 : งานเอกสาร & ระเบียบ",
        "badge": "Module 3",
        "title": "AI ช่วยจัดทำเอกสารราชการ & สรุปหนังสือเวียน สถ.",
        "subtitle": "การวิเคราะห์และสรุปสาระสำคัญจากไฟล์ PDF/Word กฎหมาย และระเบียบราชการ",
        "type": "feature_card",
        "content": {
            "features": [
                {"icon": "file-search", "title": "สรุปหนังสือเวียน มท. / สถ.", "desc": "แปลงเอกสารระเบียบ 20-30 หน้า ให้เป็น Executive Summary 1 หน้า พร้อม Checklist สิ่งที่ อปท. ต้องทำ"},
                {"icon": "scale", "title": "เปรียบเทียบระเบียบฉบับเก่า-ใหม่", "desc": "ค้นหาจุดแตกต่าง เช่น เกณฑ์การเบิกจ่ายใหม่ เทียบกับเกณฑ์เดิม สรุปเป็นตารางเปรียบเทียบจุดต่อจุด"},
                {"icon": "check-square", "title": "ตรวจสอบร่างเทศบัญญัติ/ข้อบัญญัติ", "desc": "ตรวจทานความถูกต้องของการอ้างอิงมาตรา กฎหมายลำดับรอง และความสอดคล้องของสำนวนกฎหมาย"}
            ]
        },
        "notes": "เข้าสู่ส่วนที่ 3 การใช้ AI วิเคราะห์และย่อยเอกสารระเบียบราชการขนาดใหญ่"
    },
    {
        "id": 15,
        "module": "ส่วนที่ 3 : งานเอกสาร & ระเบียบ",
        "badge": "ตัวอย่างสรุปหนังสือเวียน",
        "title": "ตัวอย่าง Prompt: สรุปหนังสือเวียน สถ. สู่ Executive Summary",
        "subtitle": "คำสั่งเพื่อให้ AI สรุปสาระสำคัญสำหรับเสนอผู้บริหารระดับสูง (ปลัด/นายก)",
        "type": "prompt_display",
        "content": {
            "prompt_text": "บทบาท: คุณคือนิติกรชำนาญการ ปฏิบัติงานในองค์กรปกครองส่วนท้องถิ่น\nงานที่ต้องการให้ทำ: อ่านและสรุปสาระสำคัญจากหนังสือเวียนกรมส่งเสริมการปกครองท้องถิ่น (ไฟล์แนบ) เพื่อจัดทำเป็น 'บทสรุปสำหรับผู้บริหาร (Executive Summary)' ความยาวไม่เกิน 1 หน้ากระดาษ A4\nรูปแบบภาษาและโครงสร้างผลลัพธ์:\n1. ชื่อเรื่อง เลขที่หนังสือ และวันที่บังคับใช้\n2. วัตถุประสงค์และที่มาของการออกหนังสือเวียนโดยย่อ\n3. สาระสำคัญและการเปลี่ยนแปลงหลัก (เปรียบเทียบสิ่งที่เปลี่ยนไปจากแนวปฏิบัติเดิม)\n4. สิ่งที่เทศบาล/อบต. ต้องดำเนินการ (Action Items) จัดทำเป็น Checklist ระบุฝ่ายที่รับผิดชอบและกำหนดเวลาที่ต้องแล้วเสร็จ\n5. ข้อสังเกตหรือความเสี่ยงทางกฎหมายที่ผู้บริหารควรระวัง",
            "key_takeaway": "ผลลัพธ์ที่ได้: ผู้บริหารสามารถอ่านจบได้ใน 3 นาที และรู้ทันทีว่าฝ่ายไหนต้องทำอะไรต่อ",
            "preview_id": "doc-summary"
        },
        "notes": "คลิกปุ่มดูตัวอย่างรายงานสรุปผู้บริหารจำลอง ชี้ให้เห็นตาราง Action Checklist"
    },
    {
        "id": 16,
        "module": "ส่วนที่ 3 : งานเอกสาร & ระเบียบ",
        "badge": "งานประจำ อปท.",
        "title": "ตัวอย่าง: ตรวจสอบร่างข้อบัญญัติงบประมาณ & ระเบียบ มท.",
        "subtitle": "การประยุกต์ใช้ AI ในการตรวจทานความถูกต้องทางกฎหมายและระเบียบการเบิกจ่าย",
        "type": "two_column",
        "content": {
            "left_title": "⚖️ ตรวจทานร่างเทศบัญญัติ/ข้อบัญญัติงบประมาณ",
            "left_items": [
                "โจทย์: ตรวจสอบความสอดคล้องระหว่างหมวดรายจ่าย และระเบียบกระทรวงมหาดไทยว่าด้วยการรับเงิน การเบิกจ่ายเงินฯ 2566",
                "คำสั่ง AI: 'ตรวจสอบร่างข้อบัญญัติงบประมาณรายจ่ายประจำปี (แนบไฟล์) ว่ามีรายการใดที่อาจขัดหรือแย้งกับระเบียบ มท. ล่าสุดหรือไม่'",
                "ผลลัพธ์: AI จะระบุข้อสังเกตพร้อมอ้างอิงมาตราที่เกี่ยวข้อง ช่วยนิติกรตรวจสอบความถูกต้องก่อนเสนอนายกฯ"
            ],
            "right_title": "🔍 เปรียบเทียบระเบียบการจัดซื้อจัดจ้างฉบับใหม่",
            "right_items": [
                "โจทย์: กรมบัญชีกลางหรือ มท. ออกระเบียบใหม่ ต้องการรู้ว่าจุดใดบ้างที่เปลี่ยนแปลงจากเดิม",
                "คำสั่ง AI: 'เปรียบเทียบข้อความในระเบียบฉบับปี 2560 กับฉบับแก้ไขปีล่าสุด สรุปเป็นตาราง 3 คอลัมน์: ข้อความเดิม | ข้อความใหม่ | ผลกระทบต่อ อปท.'",
                "ผลลัพธ์: ได้ตารางเปรียบเทียบจุดต่อจุดในเวลาเพียง 1 นาที"
            ]
        },
        "notes": "ช่วยลดเวลาของฝ่ายกฎหมายและฝ่ายการเงินในการเปรียบเทียบเอกสารกฎหมาย"
    },

    # 4. Public Relations & Social Media
    {
        "id": 17,
        "module": "ส่วนที่ 4 : ประชาสัมพันธ์ & สื่อสาร",
        "badge": "Module 4",
        "title": "AI เพื่อการประชาสัมพันธ์และการสื่อสารกับประชาชน",
        "subtitle": "ปรับเปลี่ยนภาษาทางการที่เข้าใจยาก ให้เป็นมิตร เข้าถึงง่าย และถูกต้องตามระเบียบ",
        "type": "feature_card",
        "content": {
            "features": [
                {"icon": "message-circle", "title": "Social Media Posts (Facebook/LINE)", "desc": "แปลงประกาศเทศบัญญัติภาษี สิทธิสวัสดิการ ให้เป็นโพสต์ที่ประชาชนอ่านเข้าใจทันที พร้อม Emoji เหมาะสม"},
                {"icon": "heart-handshake", "title": "ข้อความตอบกลับเรื่องร้องเรียน", "desc": "ตอบกลับประชาชนทางโซเชียลด้วยความเห็นอกเห็นใจ (Empathy) ชี้แจงขั้นตอน และกำหนดเวลาแก้ไขชัดเจน"},
                {"icon": "mic", "title": "คำกล่าวเปิดงาน & สคริปต์พิธีกร", "desc": "ร่างคำกล่าวเปิดงานประเพณี กิจกรรมชุมชน สอดคล้องกับธรรมเนียมและระดับของประธานในพิธี"}
            ]
        },
        "notes": "เข้าสู่ส่วนที่ 4 การสื่อสารหน้าบ้านกับประชาชน เปลี่ยนภาษากฎหมายเป็นภาษาชาวบ้าน"
    },
    {
        "id": 18,
        "module": "ส่วนที่ 4 : ประชาสัมพันธ์ & สื่อสาร",
        "badge": "ตัวอย่างโพสต์ Facebook",
        "title": "ตัวอย่าง Prompt: ย่อยภาษีที่ดินและสิ่งปลูกสร้างเป็น Facebook Post",
        "subtitle": "เปลี่ยนระเบียบกฎหมายซับซ้อน เป็นโพสต์ประชาสัมพันธ์ที่อ่านเข้าใจง่ายและดึงดูดใจ",
        "type": "prompt_display",
        "content": {
            "prompt_text": "บทบาท: คุณคือนักประชาสัมพันธ์ปฏิบัติการ ร่วมกับฝ่ายพัฒนารายได้ กองคลัง เทศบาลเมือง...\nงานที่ต้องการให้ทำ: ย่อยข้อมูลกฎหมาย พ.ร.บ. ภาษีที่ดินและสิ่งปลูกสร้าง เรื่อง 'การชำระภาษีประจำปี 2569' ให้เป็นโพสต์ Facebook ประชาสัมพันธ์สำหรับประชาชนทั่วไป\nบริบทและข้อมูลสำคัญ:\n- กำหนดชำระภายในเดือนเมษายน 2569 ช่องทางชำระ: เคาน์เตอร์กองคลัง, โอนผ่าน QR Code ธนาคาร, หรือเคาน์เตอร์เซอร์วิส\n- หากไม่ชำระตามกำหนดจะมีเบี้ยปรับและเงินเพิ่มตามกฎหมาย\nรูปแบบภาษาและผลลัพธ์:\n- ภาษาเป็นกันเอง สุภาพ ชัดเจน ไม่ใช้ศัพท์กฎหมายที่เข้าใจยาก (Citizen-Friendly Tone)\n- ใช้เทคนิคการพาดหัวข่าว (Hook) ที่ดึงดูดสายตา\n- จัดเรียงข้อมูลสำคัญเป็นข้อย่อย ใช้ Emoji อย่างพอเหมาะเพื่อช่วยให้อ่านง่าย\n- ระบุ Call to Action (ช่องทางติดต่อสอบถาม) และ Call Center เทศบาล",
            "key_takeaway": "ผลสัมฤทธิ์: ประชาชนรู้ว่าต้องจ่ายเมื่อไหร่ จ่ายที่ไหน ไม่จ่ายจะเกิดอะไรขึ้น และติดต่อใครได้",
            "preview_id": "doc-facebook"
        },
        "notes": "คลิกปุ่มดูตัวอย่างโพสต์ Facebook จำลอง ชี้ให้เห็นการใช้ Emoji ดึงดูดสายตา"
    },
    {
        "id": 19,
        "module": "ส่วนที่ 4 : ประชาสัมพันธ์ & สื่อสาร",
        "badge": "การตอบข้อร้องเรียน",
        "title": "ตัวอย่าง Prompt: ตอบกลับประชาชนกรณีไฟกิ่งชำรุด / น้ำไม่ไหล",
        "subtitle": "เทคนิคการร่างข้อความตอบกลับด้วยหลัก Empathy + Action Plan ชัดเจน",
        "type": "comparison",
        "content": {
            "items": [
                {
                    "title": "❌ ตอบแบบราชการเดิมๆ (ประชาชนรู้สึกห่างเหิน)",
                    "desc": "\"รับเรื่องแล้ว จะแจ้งกองช่างดำเนินการต่อไปตามขั้นตอนระเบียบราชการ\"\n\nผลกระทบ: ประชาชนไม่รู้ว่าจะเสร็จเมื่อไหร่ รู้สึกว่าโยนเรื่อง และเกิดการโพสต์ต่อว่าซ้ำในโซเชียล"
                },
                {
                    "title": "✅ สั่ง AI ให้ตอบด้วยหลัก 3 ส่วน (แนะนำ)",
                    "desc": "\"สวัสดีครับคุณสมชาย เทศบาลตำบล... ต้องขออภัยในความไม่สะดวกเป็นอย่างยิ่งครับ เบื้องต้นแอดมินได้ส่งเรื่องประสานกองช่างไฟฟ้าเรียบร้อยแล้ว (รหัสคำร้อง #EF-6902) โดยเจ้าหน้าที่จะลงพื้นที่ตรวจสอบและเปลี่ยนหลอดไฟให้ในวันพรุ่งนี้ (ช่วงบ่าย 13.00 - 16.30 น.) หากมีความคืบหน้าจะแจ้งให้ทราบทันทีครับ หากฉุกเฉินติดต่อ 053-XXXXXX ต่อ 14 ครับ\"\n\nผลลัพธ์: ประชาชนรู้สึกว่าได้รับการใส่ใจ มีรหัสติดตาม และมีกำหนดเวลาแน่นอน",
                    "preview_id": "doc-complaint"
                }
            ]
        },
        "notes": "คลิกปุ่มดูตัวอย่างข้อความแชทตอบกลับประชาชน ชี้ให้เห็นว่าช่วยลดข้อร้องเรียนซ้ำซ้อนได้มาก"
    },

    # 5. Local Strategy & Budget
    {
        "id": 20,
        "module": "ส่วนที่ 5 : แผนงาน & ยุทธศาสตร์",
        "badge": "Module 5",
        "title": "AI กับงานบริหาร การวางแผน และยุทธศาสตร์ อปท.",
        "subtitle": "ยกระดับการทำงานของนักวิเคราะห์นโยบายและแผน และผู้บริหารท้องถิ่น",
        "type": "feature_card",
        "content": {
            "features": [
                {"icon": "compass", "title": "SWOT & TOWS Matrix", "desc": "วิเคราะห์จุดแข็ง จุดอ่อน โอกาส อุปสรรค ของพื้นที่ อปท. เพื่อสังเคราะห์เป็นโครงการเชิงยุทธศาสตร์"},
                {"icon": "pie-chart", "title": "วิเคราะห์งบประมาณ 5 ปี", "desc": "จำแนกโครงสร้างรายรับ-รายจ่าย งบลงทุน งบบุคลากร และคำนวณสัดส่วนอย่างแม่นยำ"},
                {"icon": "alert-triangle", "title": "Root Cause Analysis", "desc": "หาสาเหตุที่แท้จริงของการเบิกจ่ายงบประมาณล่าช้า และเสนอ 3 มาตรการเร่งรัดแก่ผู้บริหาร"}
            ]
        },
        "notes": "เข้าสู่ส่วนที่ 5 ยกระดับสู่งานนโยบายและแผนพัฒนาท้องถิ่น AI ทำหน้าที่เป็นที่ปรึกษาเชิงยุทธศาสตร์"
    },
    {
        "id": 21,
        "module": "ส่วนที่ 5 : แผนงาน & ยุทธศาสตร์",
        "badge": "SWOT Analysis",
        "title": "ตัวอย่าง Prompt: SWOT พัฒนาการท่องเที่ยวและเศรษฐกิจริมน้ำ",
        "subtitle": "ให้ AI ช่วยระดมความคิดและจัดกลุ่มยุทธศาสตร์สำหรับแผนพัฒนาท้องถิ่น",
        "type": "prompt_display",
        "content": {
            "prompt_text": "บทบาท: คุณคือนักวิเคราะห์นโยบายและแผนชำนาญการ เทศบาล...\nงานที่ต้องการให้ทำ: วิเคราะห์ SWOT Analysis สำหรับจัดทำแผนพัฒนาท้องถิ่น (พ.ศ. 2566-2570) ในประเด็น 'ยุทธศาสตร์การพัฒนาการท่องเที่ยวเชิงวัฒนธรรมและเศรษฐกิจชุมชนริมน้ำ'\nบริบทพื้นที่:\n- มีวัดเก่าแก่ริมแม่น้ำ มีตลาดน้ำชุมชนเสาร์-อาทิตย์ ปราชญ์ชาวบ้านเข้มแข็ง\n- ปัญหา: น้ำเสียริมตลิ่ง, ขยะตกค้างช่วงวันหยุด, ร้านค้าชุมชนยังไม่รับชำระเงินดิจิทัล\n- โอกาส: นโยบาย Soft Power และการท่องเที่ยวเมืองรองของรัฐบาล\n- อุปสรรค: สภาวะเศรษฐกิจผันผวน และแหล่งท่องเที่ยวอำเภอข้างเคียงเปิดตัวใหม่\nรูปแบบผลลัพธ์:\n- ตาราง SWOT Matrix 4 ช่อง (S-W-O-T) ระบุข้อวิเคราะห์ช่องละ 3-4 ข้อ\n- เสนอแนะโครงการเชิงยุทธศาสตร์ 3 โครงการที่บรรจุในแผนพัฒนาท้องถิ่นได้ทันที",
            "key_takeaway": "ผลลัพธ์ที่ได้: ตาราง SWOT ชัดเจน พร้อมข้อเสนอ 3 โครงการสำหรับบรรจุในแผนพัฒนาท้องถิ่น",
            "preview_id": "doc-swot"
        },
        "notes": "คลิกดูตัวอย่างตาราง SWOT Matrix เต็ม 4 ช่อง พร้อมโครงการยุทธศาสตร์บรรจุในแผนพัฒนาท้องถิ่น"
    },
    {
        "id": 22,
        "module": "ส่วนที่ 5 : แผนงาน & ยุทธศาสตร์",
        "badge": "วิเคราะห์งบประมาณ",
        "title": "ตัวอย่าง Prompt: วิเคราะห์งบประมาณ 5 ปี & สาเหตุเบิกจ่ายล่าช้า",
        "subtitle": "Root Cause Analysis & ข้อเสนอแนะเชิงบริหารเพื่อเร่งรัดการเบิกจ่ายงบลงทุน",
        "type": "comparison",
        "content": {
            "items": [
                {
                    "title": "🔍 การวิเคราะห์สาเหตุหลัก 3 ประการ (Root Causes)",
                    "desc": "1. ความล่าช้าในกระบวนการจัดทำราคากลางและแบบรูปรายการ (กองช่างบุคลากรไม่พอ)\n2. ขั้นตอนการจัดซื้อจัดจ้าง e-bidding เกิดการอุทธรณ์ผลการประกวดราคา\n3. การบริหารสัญญาขาดระบบแจ้งเตือนกำหนดส่งมอบงานของผู้รับจ้าง"
                },
                {
                    "title": "💡 ข้อเสนอแนะเชิงบริหาร 3 ข้อ สำหรับผู้บริหาร อปท.",
                    "desc": "1. ตั้งคณะทำงานเฉพาะกิจ (Fast-Track Taskforce) ประกบโครงการงบลงทุนเกิน 5 แสนบาททุกสัปดาห์\n2. นำเทมเพลตมาตรฐานมาใช้ในการทำราคากลางเพื่อลดเวลาตรวจแก้\n3. จัดทำ Dashboard ติดตามสถานะสัญญาแบบ Real-time รายงานปลัดเทศบาลทุกวันจันทร์"
                }
            ]
        },
        "notes": "ชี้ให้เห็นว่าช่วยให้นักวิเคราะห์นโยบายและแผนจัดทำเอกสารเสนอผู้บริหารได้ในเวลาอันรวดเร็ว"
    },

    # 6. Workflow & Complaints
    {
        "id": 23,
        "module": "ส่วนที่ 6 : กระบวนงาน & ร้องทุกข์",
        "badge": "Module 6",
        "title": "AI ช่วยออกแบบกระบวนการทำงาน (SOP) & วิเคราะห์ข้อมูล",
        "subtitle": "ปรับปรุงกระบวนการบริการประชาชนสู่ Digital One-Stop Service",
        "type": "feature_card",
        "content": {
            "features": [
                {"icon": "git-merge", "title": "ออกแบบ Workflow & SOP ดิจิทัล", "desc": "เขียนขั้นตอนการขอใบอนุญาตก่อสร้าง (แบบ อ.1) ลดขั้นตอนซ้ำซ้อนจาก 14 วัน เหลือ 5 วันทำการ"},
                {"icon": "database", "title": "ประมวลผลข้อมูลเรื่องร้องทุกข์", "desc": "นำเข้าข้อมูลข้อร้องเรียนจาก Traffy Fondue หรือสมุดร้องทุกข์ เพื่อจัดกลุ่มปัญหาและพื้นที่เสี่ยง"},
                {"icon": "check-circle", "title": "สร้าง Service Checklist", "desc": "จัดทำรายการตรวจสอบเอกสารสำหรับประชาชนและเจ้าหน้าที่ผู้รับคำขอ เพื่อป้องกันเอกสารไม่ครบ"}
            ]
        },
        "notes": "เข้าสู่ส่วนที่ 6 การปรับปรุงกระบวนงานภาครัฐ (BPR) และการใช้ AI วิเคราะห์ข้อมูลร้องเรียนประชาชน"
    },
    {
        "id": 24,
        "module": "ส่วนที่ 6 : กระบวนงาน & ร้องทุกข์",
        "badge": "ตัวอย่าง Workflow SOP",
        "title": "ตัวอย่าง Prompt: ออกแบบ SOP การขอใบอนุญาตก่อสร้าง (แบบ อ.1)",
        "subtitle": "ลดขั้นตอนและระยะเวลาตาม พ.ร.บ. การอำนวยความสะดวกในการพิจารณาอนุญาตฯ พ.ศ. 2558",
        "type": "prompt_display",
        "content": {
            "prompt_text": "บทบาท: คุณคือหัวหน้าฝ่ายควบคุมอาคาร กองช่าง ร่วมกับฝ่ายนิติการ เทศบาล...\nงานที่ต้องการให้ทำ: ทบทวนและออกแบบกระบวนการทำงานมาตรฐาน (Standard Operating Procedure: SOP) เรื่อง 'การขอรับใบอนุญาตก่อสร้าง ดัดแปลง หรือรื้อถอนอาคาร (แบบ อ.1)'\nเป้าหมาย:\n- ปรับลดระยะเวลาดำเนินการจากเดิม 14 วันทำการ ให้เหลือไม่เกิน 5 วันทำการ\n- ประยุกต์ใช้ระบบยื่นคำขอออนไลน์ (e-Service) และตรวจแบบดิจิทัล\nรูปแบบผลลัพธ์:\n1. แผนผังกระบวนงาน (Flowchart) 5 ขั้นตอนหลัก\n2. ตารางระบุ: ขั้นตอน | ผู้รับผิดชอบ | ระยะเวลาเดิม | ระยะเวลาใหม่ | เครื่องมือดิจิทัลที่ใช้\n3. Checklist เอกสารหลักฐานที่ประชาชนต้องเตรียม เพื่อป้องกันการขอเอกสารซ้ำซ้อน",
            "key_takeaway": "ผลลัพธ์: ตาราง SOP ชัดเจน ช่วยลดระยะเวลาและตัดขั้นตอนซ้ำซ้อนได้อย่างเป็นรูปธรรม",
            "preview_id": "doc-workflow"
        },
        "notes": "คลิกดูตัวอย่างตาราง SOP และ Flowchart จำลองการอนุญาตก่อสร้างแบบ อ.1"
    },
    {
        "id": 25,
        "module": "ส่วนที่ 6 : กระบวนงาน & ร้องทุกข์",
        "badge": "วิเคราะห์ Traffy Fondue",
        "title": "ตัวอย่าง Prompt: จัดกลุ่มเรื่องร้องเรียน Traffy Fondue & เสนอทางแก้",
        "subtitle": "กรณีศึกษา: ข้อมูลร้องเรียน 100 เรื่อง นำมาจัดกลุ่มและวิเคราะห์ความเร่งด่วนใน 15 วินาที",
        "type": "two_column",
        "content": {
            "left_title": "📊 ผลการจัดกลุ่มปัญหาโดย AI (Top 3 Categories)",
            "left_items": [
                "1. แสงสว่างและความปลอดภัย (42%): ไฟกิ่งดับในซอยเปลี่ยว เสี่ยงอุบัติเหตุและอาชญากรรม",
                "2. ขยะและสิ่งแวดล้อม (31%): ขยะตกค้างช่วงวันหยุด และการเผาเศษวัชพืชในที่โล่ง",
                "3. โครงสร้างพื้นฐาน (27%): ท่อระบายน้ำอุดตัน ผิวถนนเป็นหลุมบ่อ"
            ],
            "right_title": "💡 แนวทางแก้ไขเชิงรุก (Proactive Strategy)",
            "right_items": [
                "แผนที่ความเสี่ยง (Heatmap): กำหนดพิกัดซอยที่มีไฟดับซ้ำซาก เพื่อเปลี่ยนเป็นโคม LED อัจฉริยะ",
                "ปรับรอบเก็บขยะ: เพิ่มรอบจัดเก็บในวันหยุดเสาร์-อาทิตย์เฉพาะโซนร้านอาหารริมน้ำ",
                "ระบบแจ้งเตือนอัตโนมัติ: เชื่อมโยงสถานะการซ่อมจากกองช่างตรงถึงประชาชนผู้แจ้งเรื่อง"
            ]
        },
        "notes": "ให้ผู้เข้าอบรมเห็นว่า AI ช่วยประมวลผลข้อร้องเรียน 100 เรื่องได้ใน 15 วินาที"
    },

    # 7. Ethics, Secrets & PDPA
    {
        "id": 26,
        "module": "ส่วนที่ 7 : จริยธรรม AI & PDPA",
        "badge": "Module 7",
        "title": "การใช้ AI อย่างปลอดภัย มีจริยธรรม และถูกต้องตามระเบียบ",
        "subtitle": "ข้อพึงระวังสูงสุดสำหรับเจ้าหน้าที่รัฐในการนำเครื่องมือ AI มาใช้ในงานราชการ",
        "type": "feature_card",
        "content": {
            "features": [
                {"icon": "lock", "title": "ความลับของทางราชการ", "desc": "ห้ามใส่เอกสารชั้น 'ลับ', 'ลับมาก', 'ลับที่สุด' หรือเอกสารที่ยังไม่เผยแพร่ลงในระบบ AI สาธารณะ"},
                {"icon": "user-x", "title": "กฎหมาย PDPA (พ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล)", "desc": "ต้องตัดเลขบัตรประชาชน 13 หลัก, ชื่อนามสกุลจริง, ข้อมูลสุขภาพ หรือเบอร์โทรศัพท์ออกก่อนเสมอ"},
                {"icon": "user-check", "title": "Human-in-the-loop (คนต้องเป็นผู้ตรวจรับ)", "desc": "AI ไม่มีความรับผิดทางกฎหมาย ผู้ลงนามและเจ้าหน้าที่ผู้เสนอเรื่องต้องรับผิดชอบความถูกต้อง 100%"}
            ]
        },
        "notes": "เข้าสู่ส่วนที่ 7 หัวข้อที่สำคัญที่สุดของหลักสูตร ย้ำเตือนเรื่องความรับผิดชอบทางกฎหมายและการคุ้มครองข้อมูล"
    },
    {
        "id": 27,
        "module": "ส่วนที่ 7 : จริยธรรม AI & PDPA",
        "badge": "ระดับชั้นความลับ",
        "title": "ระดับชั้นความลับของข้อมูลที่ 'ห้าม' นำเข้า AI สาธารณะ",
        "subtitle": "ตามระเบียบว่าด้วยการรักษาความลับของทางราชการ พ.ศ. 2544 และ พ.ร.บ. ข้อมูลข่าวสารฯ 2540",
        "type": "gov_types",
        "content": {
            "types": [
                {"num": "🔴", "title": "ลับที่สุด (Top Secret)", "desc": "ข้อมูลความมั่นคง แผนรับมือวินาศกรรม หากรั่วไหลจะเกิดความเสียหายร้ายแรงยิ่ง", "detail": "ห้ามนำเข้าสู่ระบบ AI ทุกกรณีโดยเด็ดขาด"},
                {"num": "🔴", "title": "ลับมาก (Secret)", "desc": "ข้อมูลยุทธศาสตร์สำคัญ แผนกำลังพลลับ ข้อมูลความมั่นคงท้องถิ่นระดับสูง", "detail": "ห้ามนำเข้าสู่ AI สาธารณะ"},
                {"num": "🟠", "title": "ลับ (Confidential)", "desc": "สำนวนการสอบสวนวินัย ข้อเท็จจริงการทุจริตที่ยังไม่ยุติ ข้อมูลราคากลางก่อนประกาศ e-GP", "detail": "ห้ามนำเข้า AI ที่ไม่มีสัญญาคุ้มครองข้อมูล"},
                {"num": "🟢", "title": "ข้อมูลส่วนบุคคล (PDPA)", "desc": "เลขบัตร ปชช., ฐานข้อมูลภาษี, ข้อมูลผู้ป่วย/เบี้ยยังชีพผู้พิการ", "detail": "ต้องทำ Anonymization (ตัดข้อมูลระบุตัวตนออก) ก่อนให้ AI ประมวลผล"},
                {"num": "⚪", "title": "ข้อมูลเปิดเผยทั่วไป", "desc": "ระเบียบ มท., หนังสือเวียน สถ., ข่าวประชาสัมพันธ์, คู่มือประชาชน", "detail": "สามารถใช้ AI ช่วยสรุป ร่าง และวิเคราะห์ได้อย่างปลอดภัย"}
            ]
        },
        "notes": "อธิบายตารางสัญญาณไฟจราจร สีแดงคือห้ามเด็ดขาด สีส้มต้องระวัง สีเขียวคือทำ Anonymization และสีขาวคือใช้งานได้อย่างอิสระ"
    },
    {
        "id": 28,
        "module": "ส่วนที่ 7 : จริยธรรม AI & PDPA",
        "badge": "Good vs Bad Prompt",
        "title": "เปรียบเทียบ Good Prompt vs Bad Prompt สำหรับงาน อปท.",
        "subtitle": "บทเรียนจริงเพื่อป้องกันข้อผิดพลาดและข้อมูลรั่วไหลในการใช้งาน AI",
        "type": "comparison",
        "content": {
            "items": [
                {
                    "title": "❌ Bad Prompt (ละเมิด PDPA และคลุมเครือ)",
                    "desc": "\"ช่วยสรุปข้อร้องเรียนของนายสมศักดิ์ รักดี เลขบัตร 3-5099-00123-45-6 บ้านเลขที่ 99 หมู่ 3 ที่มาร้องเรียนว่านายกเทศมนตรีฮั้วประมูลหน่อย\"\n\nจุดอันตราย: ละเมิด PDPA รุนแรง และใส่ข้อมูลกล่าวหาที่ยังไม่มีข้อเท็จจริงเข้าสู่ระบบสาธารณะ"
                },
                {
                    "title": "✅ Good Prompt (ปลอดภัยและได้ผลลัพธ์แม่นยำ)",
                    "desc": "\"บทบาท: เจ้าหน้าที่นิติกร เทศบาล...\nงาน: ร่างแบบฟอร์มตรวจสอบข้อเท็จจริงเบื้องต้น กรณีได้รับเรื่องร้องเรียนเกี่ยวกับกระบวนการจัดซื้อจัดจ้างโครงการก่อสร้างถนน\nข้อมูล: ไม่ระบุชื่อบุคคล แต่ต้องการหัวข้อตรวจสอบตาม พ.ร.บ. จัดซื้อจัดจ้างฯ 2560 มาตรา 64-67\nผลลัพธ์: ตาราง Checklist สำหรับคณะกรรมการสืบสวนข้อเท็จจริง\"\n\nจุดเด่น: ปลอดภัย ไม่ระบุตัวบุคคล ได้โครงสร้างการทำงานที่เป็นมาตรฐาน",
                    "preview_id": "doc-ethics"
                }
            ]
        },
        "notes": "คลิกดูตัวอย่างเปรียบเทียบ Good vs Bad Prompt ฉบับเต็ม พร้อมคำอธิบายข้อกฎหมาย PDPA"
    },
    {
        "id": 29,
        "module": "ส่วนที่ 7 : จริยธรรม AI & PDPA",
        "badge": "กฎเหล็กจริยธรรม",
        "title": "กฎเหล็ก 3 Dos & 3 Don'ts สำหรับบุคลากร อปท.",
        "subtitle": "แนวทางปฏิบัติที่ต้องจำขึ้นใจในการใช้ Generative AI ในหน่วยงานรัฐ",
        "type": "two_column",
        "content": {
            "left_title": "✅ 3 Dos (สิ่งที่ควรทำเสมอ)",
            "left_items": [
                "1. Do Verify Facts: ตรวจสอบความถูกต้องของระเบียบ เลขที่หนังสือ และข้อกฎหมายก่อนใช้งานเสมอ (ป้องกัน AI Hallucination)",
                "2. Do Anonymize: ลบชื่อ นามสกุล เลขบัตร 13 หลัก และข้อมูลส่วนบุคคลออกก่อนส่งเข้า AI ทุกครั้ง",
                "3. Do Keep Human Control: ข้าราชการ/พนักงานต้องเป็นผู้ตัดสินใจขั้นสุดท้าย และรับผิดชอบในเอกสารที่ลงนาม"
            ],
            "right_title": "❌ 3 Don'ts (สิ่งที่ไม่ควรทำเด็ดขาด)",
            "right_items": [
                "1. Don't Upload Secrets: อย่าอัปโหลดเอกสารชั้นความลับ หรือข้อมูลราคากลางก่อนการประมูลลงใน AI สาธารณะ",
                "2. Don't Blindly Trust: อย่าเชื่อผลลัพธ์ AI โดยไม่อ่านตรวจทาน โดยเฉพาะตัวเลขงบประมาณและการคำนวณภาษี",
                "3. Don't Replace Discretion: อย่าให้ AI ทำหน้าที่ตัดสินใจแทนอำนาจดุลพินิจของผู้บริหารตามกฎหมาย"
            ]
        },
        "notes": "สไลด์ Infographic 1 หน้า สำหรับให้ผู้เรียนบันทึกเก็บไว้เป็นแนวทางปฏิบัติประจำโต๊ะทำงาน"
    },

    # 8. Action Plan & Next Steps
    {
        "id": 30,
        "module": "ส่วนที่ 8 : สรุป & Action Plan",
        "badge": "End-to-End Case Study",
        "title": "โจทย์จำลองงานจริง: จัดงานประเพณีท้องถิ่นแบบครบวงจร",
        "subtitle": "ฝึกปฏิบัติการบูรณาการ AI ในทุกขั้นตอนตั้งแต่ต้นจนจบ (End-to-End Workflow)",
        "type": "feature_card",
        "content": {
            "features": [
                {"icon": "file-plus", "title": "ขั้นที่ 1: ร่างโครงร่างโครงการ", "desc": "โครงการจัดงานประเพณีลอยกระทงปลอดเหล้า ประจำปี 2569 พร้อมกำหนดวัตถุประสงค์และตัวชี้วัด KPI"},
                {"icon": "mail", "title": "ขั้นที่ 2: ร่างหนังสือเชิญประธาน", "desc": "ร่างหนังสือภายนอก (ตราครุฑ) ถึงผู้ว่าราชการจังหวัดหรือนายอำเภอ เพื่อเชิญเป็นประธานเปิดงาน"},
                {"icon": "share-2", "title": "ขั้นที่ 3: สื่อประชาสัมพันธ์", "desc": "ร่างโพสต์ Facebook เชิญชวนประชาชน พร้อมข้อความรณรงค์ใช้วัสดุธรรมชาติและงดประทัด"},
                {"icon": "shield-alert", "title": "ขั้นที่ 4: Checklist ความปลอดภัย", "desc": "จัดทำตารางตรวจสอบความปลอดภัยท่าน้ำ แสงสว่าง และทีมกู้ชีพเทศบาล"}
            ]
        },
        "notes": "โจทย์บูรณาการ End-to-End ให้ผู้เรียนทำภารกิจจำลองสถานการณ์จริงครบทั้ง 4 ด้าน"
    },
    {
        "id": 31,
        "module": "ส่วนที่ 8 : สรุป & Action Plan",
        "badge": "แผนปฏิบัติการ 30 วัน",
        "title": "การจัดทำ Action Plan นำ AI ไปใช้จริงใน 30 วันแรก",
        "subtitle": "เปลี่ยนความรู้จากการอบรม สู่การลงมือปฏิบัติจริงในกอง/ฝ่ายของตนเอง",
        "type": "comparison",
        "content": {
            "items": [
                {
                    "title": "📅 แผนงานระยะ 1-10 วันแรก (Quick Wins)",
                    "desc": "• นำ Prompt มาตรฐานไปใช้ในงานร่างบันทึกข้อความและหนังสือภายนอก\n• สร้างโฟลเดอร์รวบรวม Prompt ประจำกอง/ฝ่าย\n• ตั้งจุดตรวจทานข้อมูลส่วนบุคคล (PDPA Check) ในคอมพิวเตอร์ประจำโต๊ะ"
                },
                {
                    "title": "📅 แผนงานระยะ 11-30 วัน (Systematic Adoption)",
                    "desc": "• เริ่มนำ AI ช่วยสรุปหนังสือเวียน สถ. และทำบทสรุปผู้บริหารเสนอปลัด/นายก\n• ปรับรูปแบบโพสต์ประชาสัมพันธ์หน้าเพจเทศบาล/อบต. ให้ทันสมัยขึ้น\n• วัดผลตัวชี้วัด (KPI): ลดเวลาการร่างเอกสารลงอย่างน้อย 50%"
                }
            ]
        },
        "notes": "ให้ผู้เรียนกรอกใบงาน Action Plan ใน Handout หน้าสุดท้าย กำหนดเป้าหมายลดเวลาทำงาน 50%"
    },
    {
        "id": 32,
        "module": "บทสรุป & ก้าวต่อไป",
        "badge": "Next Steps",
        "title": "ก้าวสู่ท้องถิ่นดิจิทัล (Smart Local Government)",
        "subtitle": "AI ไม่ได้มาแทนที่คน แต่คนทำงานท้องถิ่นที่ใช้ AI เป็น จะทำงานได้มีประสิทธิภาพและบริการประชาชนได้ดียิ่งขึ้น",
        "type": "hero",
        "content": {
            "features": [
                {"icon": "laptop", "title": "เปิดระบบ AI Hub", "desc": "ฝึกเขียน Prompt และทำแบบทดสอบได้ที่หน้าเว็บ ai.html"},
                {"icon": "file-text", "title": "เอกสาร Handout", "desc": "เอกสารสรุปและแม่แบบคำสั่ง A4 พร้อมใช้งานที่ handout.html"},
                {"icon": "award", "title": "ทำแบบทดสอบ Post-Test", "desc": "วัดผลสัมฤทธิ์หลังการฝึกอบรม 5 ข้อ เพื่อรับใบประกาศนียบัตร"},
                {"icon": "help-circle", "title": "ช่วงถาม-ตอบ (Q&A)", "desc": "เปิดรับข้อซักถาม แลกเปลี่ยนประสบการณ์ และข้อเสนอแนะ"}
            ],
            "footer_note": "ขอขอบคุณผู้บริหาร ข้าราชการ และบุคลากรองค์กรปกครองส่วนท้องถิ่นทุกท่าน"
        },
        "notes": "กล่าวสรุปปิดการบรรยาย ขอบคุณผู้บริหารและผู้เข้ารับการอบรมทุกคน พร้อมเปิดช่วงถาม-ตอบ"
    }
]

with open('/Users/hanaharper/Downloads/AI_LG/slides_data.js', 'w', encoding='utf-8') as f:
    f.write('const SLIDES_DATA = ' + json.dumps(slides, ensure_ascii=False, indent=2) + ';\n')

print(f"Updated slides_data.js successfully with {len(slides)} structured slides!")
