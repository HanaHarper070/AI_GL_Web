/**
 * document_previews.js - Complete Realistic Thai Government Document Mockups
 * Includes all 3 subtypes of Orders (คำสั่ง, ระเบียบ, ข้อบังคับ),
 * all 3 subtypes of PR (ประกาศ, แถลงการณ์, ข่าว),
 * and all 3 subtypes of Officer records (หนังสือรับรอง, รายงานการประชุม, บันทึก)
 */
const DOCUMENT_PREVIEWS = {
    // 1. หนังสือภายนอก
    'doc-external': {
        title: 'ตัวอย่างหนังสือราชการภายนอก (ใช้กระดาษตราครุฑ)',
        subtitle: 'หนังสือขอความอนุเคราะห์วิทยากร ถึงอธิการบดีมหาวิทยาลัยราชภัฏเชียงใหม่',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-6 text-sm leading-relaxed">
                <div class="text-center relative">
                    <div class="w-16 h-16 mx-auto mb-1 flex items-center justify-center font-serif text-3xl font-bold text-amber-700">🦅</div>
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
                    ด้วย เทศบาลตำบลเมืองใหม่ มีความประสงค์จะจัดทำโครงการฝึกอบรมเชิงปฏิบัติการ เรื่อง "การประยุกต์ใช้ปัญญาประดิษฐ์ (AI) เพื่อยกระดับการทำงานและการให้บริการประชาชนขององค์กรปกครองส่วนท้องถิ่น" ประจำปีงบประมาณ พ.ศ. ๒๕๖๙ ในวันศุกร์ที่ ๑๕ พฤศจิกายน ๒๕๖๙ เวลา ๐๙.๐๐ - ๑๖.๐๐ น. ณ ห้องประชุมสภาเทศบาลตำบลเมืองใหม่ กลุ่มเป้าหมายคือข้าราชการและพนักงานเทศบาล จำนวน ๕๐ คน
                </div>
                <div class="text-xs text-justify indent-8 leading-relaxed">
                    เทศบาลตำบลเมืองใหม่ จึงใคร่ขอความอนุเคราะห์ อาจารย์ ดร.สมศักดิ์ นวัตกรรม ตำแหน่ง อาจารย์ประจำคณะวิทยาการจัดการ ไปเป็นวิทยากรบรรยายและฝึกปฏิบัติการตามวัน เวลา และสถานที่ดังกล่าว ทั้งนี้ เทศบาลยินดีรับผิดชอบค่าใช้จ่ายในการเดินทางและค่าสมนาคุณวิทยากรตามระเบียบกระทรวงมหาดไทยทุกประการ
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
                    <div>สำนักปลัดเทศบาล (ฝ่ายอำนวยการ) โทรศัพท์ ๐ ๕๓๑๒ ๓๔๕๖ ต่อ ๑๑</div>
                </div>
            </div>
        `
    },

    // 2. หนังสือภายใน
    'doc-internal': {
        title: 'ตัวอย่างหนังสือราชการภายใน (กระดาษบันทึกข้อความ)',
        subtitle: 'บันทึกข้อความขออนุมัติจัดโครงการและเบิกจ่ายงบประมาณ 25,000 บาท',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-5 text-sm leading-relaxed">
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
                <div class="text-xs"><strong>เรียน:</strong> นายกเทศมนตรีตำบลเมืองใหม่ (ผ่านปลัดเทศบาล)</div>
                <div class="text-xs space-y-1">
                    <div class="font-bold text-gov-800">๑. ต้นเรื่อง</div>
                    <div class="indent-8 text-justify">ตามแผนพัฒนาบุคลากรของเทศบาลตำบลเมืองใหม่ ประจำปีงบประมาณ พ.ศ. ๒๕๖๙ กำหนดให้มีการจัดฝึกอบรมทักษะดิจิทัลเพื่อเพิ่มประสิทธิภาพการปฏิบัติราชการ นั้น</div>
                </div>
                <div class="text-xs space-y-1">
                    <div class="font-bold text-gov-800">๒. ข้อเท็จจริง</div>
                    <div class="indent-8 text-justify leading-relaxed">สำนักปลัดเทศบาล ได้จัดทำโครงการฝึกอบรม AI ในงานราชการ ในวันศุกร์ที่ ๑๕ พฤศจิกายน ๒๕๖๙ กลุ่มเป้าหมาย ๕๐ คน ใช้งบประมาณหมวดค่าใช้สอย จำนวน ๒๕,๐๐๐ บาท เพื่อเป็นค่าสมนาคุณวิทยากรและอาหารว่าง</div>
                </div>
                <div class="text-xs space-y-1">
                    <div class="font-bold text-gov-800">๓. ข้อพิจารณาและข้อเสนอ</div>
                    <div class="indent-8 text-justify">จึงเรียนมาเพื่อโปรดพิจารณาอนุมัติให้จัดโครงการ เบิกจ่ายงบประมาณ ๒๕,๐๐๐ บาท และลงนามในหนังสือขอวิทยากรแนบท้าย</div>
                </div>
                <div class="grid grid-cols-2 gap-4 pt-8 text-xs">
                    <div class="text-center space-y-6">
                        <div>(ลงชื่อ)....................................................</div>
                        <div>(นางสาวจิตรา บริหารงาน)<br><span class="text-slate-500">นักจัดการงานทั่วไปชำนาญการ</span></div>
                    </div>
                    <div class="text-center space-y-6 border-l border-slate-200 pl-4">
                        <div class="text-emerald-700 font-bold">[ คำสั่งการ: อนุมัติ ]</div>
                        <div>(ลงชื่อ)....................................................</div>
                        <div>(นายกิตติคุณ ท้องถิ่นก้าวหน้า)<br><span class="text-slate-500">นายกเทศมนตรีตำบลเมืองใหม่</span></div>
                    </div>
                </div>
            </div>
        `
    },

    // 3. หนังสือประทับตรา
    'doc-seal': {
        title: 'ตัวอย่างหนังสือประทับตรา (ใช้ประทับตราแทนการลงชื่อ)',
        subtitle: 'หนังสือส่งรายงานสถิติข้อมูลประจำเดือน ถึงสำนักงานส่งเสริมการปกครองท้องถิ่นอำเภอ',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-6 text-sm leading-relaxed">
                <div class="text-center relative">
                    <div class="w-16 h-16 mx-auto mb-1 flex items-center justify-center font-serif text-3xl font-bold text-amber-700">🦅</div>
                    <div class="text-xs text-slate-500 font-serif">(กระดาษตราครุฑ)</div>
                </div>
                <div class="text-xs"><strong>ที่</strong> ชม ๕๔๓๐๑ / ต ๒๔๕</div>
                <div class="text-xs space-y-3 pt-2">
                    <div><strong>ถึง</strong> สำนักงานส่งเสริมการปกครองท้องถิ่นอำเภอเมืองเชียงใหม่</div>
                    <div class="indent-8 text-justify leading-relaxed">
                        เทศบาลตำบลเมืองใหม่ ขอส่งรายงานสถิติการให้บริการประชาชนและการจัดเก็บรายได้ ประจำเดือนตุลาคม ๒๕๖๙ จำนวน ๑ ชุด รายละเอียดปรากฏตามเอกสารแนบท้ายนี้
                    </div>
                </div>
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

    // 4.1 คำสั่ง
    'doc-order': {
        title: 'ตัวอย่างหนังสือสั่งการ: 4.1 คำสั่งเทศบาลตำบลเมืองใหม่',
        subtitle: 'คำสั่งแต่งตั้งคณะทำงานขับเคลื่อนการประยุกต์ใช้ปัญญาประดิษฐ์ (AI) ในงานราชการ',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-5 text-sm leading-relaxed">
                <div class="text-center relative">
                    <div class="w-16 h-16 mx-auto mb-1 flex items-center justify-center font-serif text-3xl font-bold text-amber-700">🦅</div>
                    <h3 class="text-base font-heading font-bold">คำสั่งเทศบาลตำบลเมืองใหม่</h3>
                    <div class="text-xs">ที่ ๔๑๒ / ๒๕๖๙</div>
                    <div class="text-xs font-bold pt-1">เรื่อง แต่งตั้งคณะทำงานขับเคลื่อนการประยุกต์ใช้ปัญญาประดิษฐ์ (AI) ในงานราชการ</div>
                </div>
                <div class="text-xs text-justify indent-8 leading-relaxed">
                    ด้วย เทศบาลตำบลเมืองใหม่ มีนโยบายในการพัฒนานวัตกรรมการบริหารราชการท้องถิ่น อาศัยอำนาจตามความในมาตรา ๔๘ เตรส แห่งพระราชบัญญัติเทศบาล พ.ศ. ๒๔๙๖ และที่แก้ไขเพิ่มเติม จึงแต่งตั้งคณะทำงาน ดังนี้:
                </div>
                <div class="text-xs pl-8 space-y-1.5">
                    <div>๑. ปลัดเทศบาลตำบลเมืองใหม่ <span class="float-right font-bold text-gov-800">ประธานคณะทำงาน</span></div>
                    <div>๒. ผู้อำนวยการกองคลัง <span class="float-right text-slate-700">คณะทำงาน</span></div>
                    <div>๓. ผู้อำนวยการกองช่าง <span class="float-right text-slate-700">คณะทำงาน</span></div>
                    <div>๔. ผู้อำนวยการกองสาธารณสุขและสิ่งแวดล้อม <span class="float-right text-slate-700">คณะทำงาน</span></div>
                    <div>๕. หัวหน้าฝ่ายอำนวยการ สำนักปลัดเทศบาล <span class="float-right font-bold text-gov-800">คณะทำงานและเลขานุการ</span></div>
                </div>
                <div class="text-xs indent-8 pt-2">ทั้งนี้ ตั้งแต่บัดนี้เป็นต้นไป</div>
                <div class="text-right pt-6 pr-8 text-xs space-y-8">
                    <div>สั่ง ณ วันที่ ๑ พฤศจิกายน พ.ศ. ๒๕๖๙</div>
                    <div>(นายกิตติคุณ ท้องถิ่นก้าวหน้า)<br><span class="text-slate-600">นายกเทศมนตรีตำบลเมืองใหม่</span></div>
                </div>
            </div>
        `
    },

    // 4.2 ระเบียบ
    'doc-regulation': {
        title: 'ตัวอย่างหนังสือสั่งการ: 4.2 ระเบียบเทศบาลตำบลเมืองใหม่',
        subtitle: 'ระเบียบเทศบาลตำบลเมืองใหม่ ว่าด้วยการใช้เทคโนโลยีปัญญาประดิษฐ์และคุ้มครองข้อมูล พ.ศ. ๒๕๖๙',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-5 text-sm leading-relaxed">
                <div class="text-center relative">
                    <div class="w-16 h-16 mx-auto mb-1 flex items-center justify-center font-serif text-3xl font-bold text-amber-700">🦅</div>
                    <h3 class="text-base font-heading font-bold">ระเบียบเทศบาลตำบลเมืองใหม่</h3>
                    <div class="text-xs font-bold pt-1">ว่าด้วยแนวปฏิบัติการใช้งานปัญญาประดิษฐ์ (AI) และการคุ้มครองข้อมูลส่วนบุคคล พ.ศ. ๒๕๖๙</div>
                </div>
                <div class="text-xs text-justify indent-8 leading-relaxed">
                    โดยที่เป็นการสมควรกำหนดแนวปฏิบัติในการนำระบบปัญญาประดิษฐ์มาสนับสนุนการปฏิบัติราชการ อาศัยอำนาจตามความในมาตรา ๔๘ เตรส แห่งพระราชบัญญัติเทศบาล พ.ศ. ๒๔๙๖ นายกเทศมนตรีตำบลเมืองใหม่ จึงวางระเบียบไว้ ดังต่อไปนี้:
                </div>
                <div class="text-xs space-y-2 leading-relaxed">
                    <div><strong>ข้อ ๑</strong> ระเบียบนี้เรียกว่า "ระเบียบเทศบาลตำบลเมืองใหม่ ว่าด้วยแนวปฏิบัติการใช้งานปัญญาประดิษฐ์ พ.ศ. ๒๕๖๙"</div>
                    <div><strong>ข้อ ๒</strong> ระเบียบนี้ให้ใช้บังคับตั้งแต่วันถัดจากวันประกาศเป็นต้นไป</div>
                    <div><strong>ข้อ ๓ (หมวดความมั่นคงปลอดภัย)</strong> ห้ามมิให้เจ้าหน้าที่นำข้อมูลข่าวสารลับของทางราชการ ข้อมูลราคากลางก่อนประกาศประกวดราคา หรือข้อมูลส่วนบุคคลที่มีเลขประจำตัวประชาชน ๑๓ หลัก นำเข้าสู่ระบบปัญญาประดิษฐ์สาธารณะโดยเด็ดขาด</div>
                    <div><strong>ข้อ ๔ (หมวดการตรวจทาน)</strong> ผลผลิตใดๆ ที่จัดทำขึ้นโดยปัญญาประดิษฐ์ เจ้าหน้าที่ผู้จัดทำต้องตรวจสอบความถูกต้องตามระเบียบสารบรรณ และเป็นผู้รับผิดชอบเสมือนจัดทำขึ้นด้วยตนเอง</div>
                </div>
                <div class="text-right pt-6 pr-8 text-xs space-y-8">
                    <div>ประกาศ ณ วันที่ ๑ พฤศจิกายน พ.ศ. ๒๕๖๙</div>
                    <div>(นายกิตติคุณ ท้องถิ่นก้าวหน้า)<br><span class="text-slate-600">นายกเทศมนตรีตำบลเมืองใหม่</span></div>
                </div>
            </div>
        `
    },

    // 4.3 ข้อบังคับ
    'doc-rule': {
        title: 'ตัวอย่างหนังสือสั่งการ: 4.3 ข้อบังคับเทศบาลตำบลเมืองใหม่',
        subtitle: 'ข้อบังคับว่าด้วยวินัยและการรักษาความปลอดภัยข้อมูลคอมพิวเตอร์ พ.ศ. ๒๕๖๙',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-5 text-sm leading-relaxed">
                <div class="text-center relative">
                    <div class="w-16 h-16 mx-auto mb-1 flex items-center justify-center font-serif text-3xl font-bold text-amber-700">🦅</div>
                    <h3 class="text-base font-heading font-bold">ข้อบังคับเทศบาลตำบลเมืองใหม่</h3>
                    <div class="text-xs font-bold pt-1">ว่าด้วยจรรยาบรรณและการรักษาความมั่นคงปลอดภัยระบบสารสนเทศ พ.ศ. ๒๕๖๙</div>
                </div>
                <div class="text-xs text-justify indent-8 leading-relaxed">
                    เพื่อกำหนดมาตรฐานความปลอดภัยทางไซเบอร์และการใช้เครื่องมือดิจิทัล อาศัยอำนาจตามระเบียบกระทรวงมหาดไทยว่าด้วยการบริหารงานบุคคลส่วนท้องถิ่น จึงออกข้อบังคับไว้ ดังนี้:
                </div>
                <div class="text-xs space-y-2 leading-relaxed">
                    <div><strong>ข้อ ๑</strong> เจ้าหน้าที่ทุกคนต้องรักษารหัสผ่านประจำตัวและไม่เปิดเผยให้ผู้อื่นเข้าใช้งานระบบราชการแทน</div>
                    <div><strong>ข้อ ๒</strong> การเชื่อมต่อเครื่องมือปัญญาประดิษฐ์ (API) กับฐานข้อมูลทะเบียนราษฎรหรือฐานข้อมูลภาษี จะกระทำได้ต่อเมื่อได้รับอนุมัติเป็นลายลักษณ์อักษรจากนายกเทศมนตรี</div>
                    <div><strong>ข้อ ๓</strong> ผู้ใดฝ่าฝืนนำข้อมูลส่วนบุคคลของประชาชนไปเผยแพร่หรือประมวลผลโดยมิชอบ ถือเป็นความผิดวินัยตามกฎหมายว่าด้วยระเบียบข้าราชการส่วนท้องถิ่น</div>
                </div>
                <div class="text-right pt-6 pr-8 text-xs space-y-8">
                    <div>ประกาศ ณ วันที่ ๑ พฤศจิกายน พ.ศ. ๒๕๖๙</div>
                    <div>(นายกิตติคุณ ท้องถิ่นก้าวหน้า)<br><span class="text-slate-600">นายกเทศมนตรีตำบลเมืองใหม่</span></div>
                </div>
            </div>
        `
    },

    // 5.1 ประกาศ
    'doc-announce': {
        title: 'ตัวอย่างหนังสือประชาสัมพันธ์: 5.1 ประกาศเทศบาลตำบลเมืองใหม่',
        subtitle: 'ประกาศกำหนดการออกหน่วยบริการจัดเก็บภาษีเคลื่อนที่และลงทะเบียนสวัสดิการ',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-5 text-sm leading-relaxed">
                <div class="text-center relative">
                    <div class="w-16 h-16 mx-auto mb-1 flex items-center justify-center font-serif text-3xl font-bold text-amber-700">🦅</div>
                    <h3 class="text-base font-heading font-bold">ประกาศเทศบาลตำบลเมืองใหม่</h3>
                    <div class="text-xs font-bold pt-1">เรื่อง กำหนดการออกหน่วยบริการจัดเก็บภาษีเคลื่อนที่และรับลงทะเบียนเบี้ยยังชีพ ประจำปี ๒๕๖๙</div>
                </div>
                <div class="text-xs text-justify indent-8 leading-relaxed">
                    ด้วย เทศบาลตำบลเมืองใหม่ จะดำเนินโครงการเทศบาลเคลื่อนที่เพื่ออำนวยความสะดวกแก่ประชาชนในการชำระภาษีที่ดินและสิ่งปลูกสร้าง และรับลงทะเบียนเบี้ยยังชีพผู้สูงอายุ ณ ศาลาประชาคมประจำหมู่บ้าน ตั้งแต่เวลา ๐๙.๐๐ - ๑๕.๓๐ น. ดังนี้:
                </div>
                <table class="w-full text-left border-collapse border border-slate-300 text-xs">
                    <tr class="bg-slate-100 font-bold">
                        <th class="p-2 border">วัน/เดือน/ปี</th>
                        <th class="p-2 border">สถานที่ให้บริการ</th>
                    </tr>
                    <tr>
                        <td class="p-2 border">วันพุธที่ ๖ พ.ย. ๖๙</td>
                        <td class="p-2 border">ศาลาประชาคม หมู่ที่ ๑ และหมู่ที่ ๒</td>
                    </tr>
                    <tr class="bg-slate-50">
                        <td class="p-2 border">วันพุธที่ ๑๓ พ.ย. ๖๙</td>
                        <td class="p-2 border">ศาลาประชาคม หมู่ที่ ๓ และหมู่ที่ ๔</td>
                    </tr>
                </table>
                <div class="text-xs text-justify indent-8">จึงประกาศให้ทราบโดยทั่วกัน</div>
                <div class="text-right pt-6 pr-8 text-xs space-y-8">
                    <div>ประกาศ ณ วันที่ ๑ พฤศจิกายน พ.ศ. ๒๕๖๙</div>
                    <div>(นายกิตติคุณ ท้องถิ่นก้าวหน้า)<br><span class="text-slate-600">นายกเทศมนตรีตำบลเมืองใหม่</span></div>
                </div>
            </div>
        `
    },

    // 5.2 แถลงการณ์
    'doc-statement': {
        title: 'ตัวอย่างหนังสือประชาสัมพันธ์: 5.2 แถลงการณ์เทศบาลตำบลเมืองใหม่',
        subtitle: 'แถลงการณ์ชี้แจงสถานการณ์ระดับน้ำในลำน้ำและมาตรการรับมืออุทกภัยฉุกเฉิน',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-5 text-sm leading-relaxed">
                <div class="text-center relative">
                    <div class="w-16 h-16 mx-auto mb-1 flex items-center justify-center font-serif text-3xl font-bold text-amber-700">🦅</div>
                    <h3 class="text-base font-heading font-bold">แถลงการณ์เทศบาลตำบลเมืองใหม่</h3>
                    <div class="text-xs font-bold pt-1">เรื่อง สถานการณ์ระดับน้ำในลำน้ำแม่คาวและมาตรการป้องกันอุทกภัย ฉบับที่ ๑</div>
                </div>
                <div class="text-xs text-justify indent-8 leading-relaxed">
                    ตามที่ได้เกิดฝนตกหนักต่อเนื่องในพื้นที่ตอนบน ส่งผลให้ระดับน้ำในลำน้ำแม่คาวเพิ่มสูงขึ้นอย่างรวดเร็ว เทศบาลตำบลเมืองใหม่ ขอชี้แจงสถานการณ์และมาตรการช่วยเหลือแก่พี่น้องประชาชน ดังนี้:
                </div>
                <div class="text-xs space-y-2 leading-relaxed">
                    <div><strong>๑. สถานการณ์ปัจจุบัน:</strong> ระดับน้ำยังอยู่ต่ำกว่าตลิ่ง ๕๐ เซนติเมตร ยังไม่มีน้ำล้นตลิ่งเข้าสู่พื้นที่ชุมชน</div>
                    <div><strong>๒. การเตรียมพร้อม:</strong> เทศบาลได้ติดตั้งเครื่องสูบน้ำขนาดใหญ่ ๔ จุด พร้อมจัดเตรียมกระสอบทราย ๕,๐๐๐ ใบ ณ ฝ่ายป้องกันฯ</div>
                    <div><strong>๓. การขอรับความช่วยเหลือ:</strong> ประชาชนในพื้นที่ลุ่มต่ำสามารถติดต่อรับกระสอบทรายและแจ้งเหตุด่วนได้ที่ สายด่วนป้องกันและบรรเทาสาธารณภัย โทร. ๐ ๕๓๑๒ ๓๑๙๙ ตลอด ๒๔ ชั่วโมง</div>
                </div>
                <div class="text-xs text-justify indent-8">ขอให้ประชาชนติดตามข่าวสารอย่างใกล้ชิดจากเพจทางการของเทศบาล</div>
                <div class="text-right pt-6 pr-8 text-xs space-y-8">
                    <div>เทศบาลตำบลเมืองใหม่</div>
                    <div>๑ พฤศจิกายน ๒๕๖๙</div>
                </div>
            </div>
        `
    },

    // 5.3 ข่าว
    'doc-news': {
        title: 'ตัวอย่างหนังสือประชาสัมพันธ์: 5.3 ข่าวเทศบาลตำบลเมืองใหม่ (Press Release)',
        subtitle: 'ข่าวแจกสื่อมวลชน เรื่อง เปิดศูนย์บริการประชาชนอัจฉริยะ AI One-Stop Service',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-5 text-sm leading-relaxed">
                <div class="border-b-2 border-gov-800 pb-3 flex justify-between items-center">
                    <div>
                        <div class="text-xs font-bold text-amber-600 uppercase">ข่าวประชาสัมพันธ์ (Press Release)</div>
                        <h3 class="text-base font-heading font-bold text-slate-900">ข่าวเทศบาลตำบลเมืองใหม่ ฉบับที่ ๒๔/๒๕๖๙</h3>
                    </div>
                    <span class="text-xs font-mono text-slate-500">เผยแพร่: ๑ พ.ย. ๖๙</span>
                </div>
                <div class="space-y-3 text-xs leading-relaxed">
                    <p class="font-bold text-sm text-gov-900">
                        เทศบาลตำบลเมืองใหม่ ก้าวสู่นวัตกรรมท้องถิ่นดิจิทัล เปิดตัวศูนย์ "AI Smart Service" ลดเวลาบริการใบอนุญาตและตอบข้อร้องเรียน ๒๔ ชั่วโมง
                    </p>
                    <p class="text-justify indent-8">
                        เมื่อวันที่ ๑ พฤศจิกายน ๒๕๖๙ นายกิตติคุณ ท้องถิ่นก้าวหน้า นายกเทศมนตรีตำบลเมืองใหม่ ได้เป็นประธานเปิดศูนย์บริการประชาชนอัจฉริยะ โดยนำเทคโนโลยีปัญญาประดิษฐ์ (AI) เข้ามาช่วยจัดทำเอกสารและคัดกรองเรื่องร้องทุกข์ของประชาชน
                    </p>
                    <p class="text-justify indent-8">
                        นายกเทศมนตรี เปิดเผยว่า การนำ AI มาใช้ช่วยให้เจ้าหน้าที่ย่นระยะเวลาการออกใบอนุญาตก่อสร้างจาก ๑๔ วัน เหลือเพียง ๕ วันทำการ และมีระบบตอบข้อร้องเรียนผ่านไลน์อัตโนมัติ ซึ่งประชาชนสามารถติดตามสถานะการแก้ไขปัญหาได้แบบเรียลไทม์
                    </p>
                </div>
                <div class="border-t border-slate-200 pt-4 text-[11px] text-slate-500">
                    <div>งานประชาสัมพันธ์ ฝ่ายอำนวยการ สำนักปลัดเทศบาลตำบลเมืองใหม่ โทร. ๐ ๕๓๑๒ ๓๔๕๖</div>
                </div>
            </div>
        `
    },

    // 6.1 หนังสือรับรอง
    'doc-certificate': {
        title: 'ตัวอย่างหนังสือที่ จนท. ทำขึ้น: 6.1 หนังสือรับรอง (ตราครุฑ)',
        subtitle: 'หนังสือรับรองการปฏิบัติหน้าที่วิทยากรโครงการฝึกอบรม AI ในงานราชการ',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-6 text-sm leading-relaxed">
                <div class="text-center relative">
                    <div class="w-16 h-16 mx-auto mb-1 flex items-center justify-center font-serif text-3xl font-bold text-amber-700">🦅</div>
                    <div class="text-xs text-slate-500 font-serif">(กระดาษตราครุฑ)</div>
                    <h3 class="text-base font-heading font-bold pt-2">เทศบาลตำบลเมืองใหม่</h3>
                </div>
                <div class="text-xs text-justify indent-8 leading-relaxed pt-4">
                    หนังสือฉบับนี้ให้ไว้เพื่อรับรองว่า <strong>อาจารย์ ดร.สมศักดิ์ นวัตกรรม</strong> ตำแหน่ง อาจารย์ประจำคณะวิทยาการจัดการ มหาวิทยาลัยราชภัฏเชียงใหม่ ได้มาปฏิบัติหน้าที่เป็นวิทยากรบรรยายและฝึกปฏิบัติการ ในโครงการฝึกอบรม เรื่อง "การประยุกต์ใช้ปัญญาประดิษฐ์ (AI) เพื่อยกระดับการทำงานขององค์กรปกครองส่วนท้องถิ่น" ประจำปีงบประมาณ พ.ศ. ๒๕๖๙ เมื่อวันศุกร์ที่ ๑๕ พฤศจิกายน ๒๕๖๙ เวลา ๐๙.๐๐ - ๑๖.๐๐ น. ณ ห้องประชุมเทศบาลตำบลเมืองใหม่
                </div>
                <div class="text-xs text-justify indent-8 leading-relaxed">
                    การปฏิบัติหน้าที่ดังกล่าวเป็นไปด้วยความเรียบร้อย สมประโยชน์ของทางราชการทุกประการ จึงออกหนังสือรับรองฉบับนี้ไว้เป็นหลักฐาน
                </div>
                <div class="text-right pt-8 pr-8 text-xs space-y-8">
                    <div>ให้ไว้ ณ วันที่ ๑๕ พฤศจิกายน พ.ศ. ๒๕๖๙</div>
                    <div>(นายกิตติคุณ ท้องถิ่นก้าวหน้า)<br><span class="text-slate-600">นายกเทศมนตรีตำบลเมืองใหม่</span></div>
                </div>
            </div>
        `
    },

    // 6.2 รายงานการประชุม
    'doc-minutes': {
        title: 'ตัวอย่างหนังสือที่ จนท. ทำขึ้น: 6.2 รายงานการประชุม (5 วาระ)',
        subtitle: 'รายงานการประชุมคณะทำงานขับเคลื่อน AI ในงานราชการ ครั้งที่ 1/2569',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-4 text-xs leading-relaxed">
                <div class="text-center border-b border-slate-200 pb-3">
                    <h3 class="text-sm font-heading font-bold text-slate-900">รายงานการประชุมคณะทำงานขับเคลื่อน AI ในงานราชการ เทศบาลตำบลเมืองใหม่</h3>
                    <div class="text-xs">ครั้งที่ ๑ / ๒๕๖๙</div>
                    <div class="text-[11px] text-slate-600">เมื่อวันศุกร์ที่ ๑ พฤศจิกายน ๒๕๖๙ ณ ห้องประชุมสภาเทศบาลตำบลเมืองใหม่</div>
                </div>
                <div class="space-y-1">
                    <div class="font-bold text-gov-800">ผู้มาประชุม:</div>
                    <div class="pl-4 text-slate-700">ปลัดเทศบาล (ประธาน), ผอ.กองคลัง, ผอ.กองช่าง, ผอ.กองสาธารณสุขฯ, นิติกร, และ หน.ฝ่ายอำนวยการ (เลขานุการ)</div>
                </div>
                <div class="space-y-2 pt-1">
                    <div><strong>วาระที่ ๑ : เรื่องประธานแจ้งให้ทราบ</strong> นโยบายกระทรวงมหาดไทยในการยกระดับองค์กรปกครองส่วนท้องถิ่นสู่ระบบดิจิทัล</div>
                    <div><strong>วาระที่ ๒ : รับรองรายงานการประชุม</strong> เป็นการประชุมครั้งแรก จึงไม่มีรายงานที่ต้องรับรอง</div>
                    <div><strong>วาระที่ ๓ : เรื่องเพื่อทราบ</strong> กำหนดการจัดอบรมเชิงปฏิบัติการ วันที่ ๑๕ พฤศจิกายน ๒๕๖๙</div>
                    <div><strong>วาระที่ ๔ : เรื่องเพื่อพิจารณา</strong> การกำหนดมาตรการคุ้มครองข้อมูลส่วนบุคคล (PDPA) ในการใช้ AI</div>
                    <div class="pl-4 text-emerald-800 font-bold">มติที่ประชุม: เห็นชอบห้ามนำข้อมูลลับและเลขบัตร ๑๓ หลักเข้า AI สาธารณะเด็ดขาด</div>
                </div>
                <div class="grid grid-cols-2 gap-4 pt-4 text-xs text-center border-t border-slate-200">
                    <div>(นางสาวจิตรา บริหารงาน)<br><span class="text-slate-500">ผู้จดรายงานการประชุม</span></div>
                    <div>(นายชัชวาล พัฒนาท้องถิ่น)<br><span class="text-slate-500">ผู้ตรวจรายงานการประชุม</span></div>
                </div>
            </div>
        `
    },

    // 6.3 บันทึก
    'doc-memo-record': {
        title: 'ตัวอย่างหนังสือที่ จนท. ทำขึ้น: 6.3 บันทึก (บันทึกตรวจรับพัสดุ / บันทึกข้อเท็จจริง)',
        subtitle: 'บันทึกรายงานผลการตรวจรับพัสดุโครงการจัดซื้อระบบคอมพิวเตอร์',
        html: `
            <div class="bg-white text-slate-900 p-8 sm:p-12 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-5 text-sm leading-relaxed">
                <div class="border-b-2 border-slate-900 pb-3">
                    <h2 class="text-xl font-heading font-bold text-slate-900">บันทึกรายงานผลการตรวจรับพัสดุ</h2>
                    <div class="text-xs text-slate-500 pt-1">โครงการจัดซื้อครุภัณฑ์คอมพิวเตอร์เพื่อการประมวลผลข้อมูล เทศบาลตำบลเมืองใหม่</div>
                </div>
                <div class="text-xs space-y-2 leading-relaxed">
                    <div><strong>เรียน:</strong> นายกเทศมนตรีตำบลเมืองใหม่</div>
                    <div class="indent-8 text-justify">
                        ตามที่ เทศบาลตำบลเมืองใหม่ ได้ตกลงซื้อครุภัณฑ์คอมพิวเตอร์ จำนวน ๕ เครื่อง จาก บริษัท สมาร์ท ไอที จำกัด ตามสัญญาซื้อขายเลขที่ ๑๒/๒๕๖๙ ลงวันที่ ๑๕ ตุลาคม ๒๕๖๙ นั้น
                    </div>
                    <div class="indent-8 text-justify">
                        บัดนี้ คณะกรรมการตรวจรับพัสดุ ได้ทำการตรวจรับครุภัณฑ์ดังกล่าวเมื่อวันที่ ๑ พฤศจิกายน ๒๕๖๙ ผลการตรวจสอบปรากฏว่า ครุภัณฑ์มีคุณลักษณะถูกต้องครบถ้วนตามสัญญา และใช้งานได้เรียบร้อยทุกประการ จึงได้ลงนามตรวจรับไว้เป็นการถูกต้อง
                    </div>
                    <div class="indent-8">
                        จึงบันทึกมาเพื่อโปรดทราบและโปรดอนุมัติให้เบิกจ่ายเงินแก่ผู้ขายต่อไป
                    </div>
                </div>
                <div class="pt-6 text-xs text-right pr-4 space-y-2">
                    <div>(ลงชื่อ).................................................... ประธานกรรมการตรวจรับ</div>
                    <div>(ลงชื่อ).................................................... กรรมการ</div>
                    <div>(ลงชื่อ).................................................... กรรมการและเลขานุการ</div>
                </div>
            </div>
        `
    },

    // Extras
    'doc-summary': {
        title: 'ตัวอย่างบทสรุปสำหรับผู้บริหาร (Executive Summary)',
        subtitle: 'สรุปหนังสือเวียน สถ. สู่การปฏิบัติการของ อปท. ใน 1 หน้า A4',
        html: `
            <div class="bg-white text-slate-900 p-6 sm:p-10 rounded-xl shadow-lg border border-slate-300 font-sans max-w-3xl mx-auto space-y-4 text-xs leading-relaxed">
                <div class="bg-gov-800 text-white p-4 rounded-xl flex justify-between items-center">
                    <div>
                        <div class="text-[11px] text-amber-300 font-bold uppercase">Executive Summary</div>
                        <h3 class="text-base font-heading font-bold text-white">สรุปหนังสือเวียน สถ. ที่ มท ๐๘๐๘.๒/ว ๑๔๕๐</h3>
                    </div>
                    <span class="px-2 py-1 bg-amber-500 text-slate-950 font-bold text-xs rounded">เร่งด่วน</span>
                </div>
                <div class="p-3 bg-slate-50 rounded-lg border border-slate-200">
                    <strong>สาระสำคัญ:</strong> ปรับปรุงระเบียบจัดซื้อจัดจ้างโครงการต่ำกว่า ๕ แสนบาท ให้ใช้ระบบ e-Catalog แบบ Fast-Track เพื่อเร่งรัดการเบิกจ่ายในไตรมาสที่ ๑
                </div>
                <table class="w-full text-left border-collapse border border-slate-200 text-xs">
                    <tr class="bg-slate-100 font-bold"><th class="p-2 border">สิ่งที่ต้องทำ</th><th class="p-2 border w-28">ฝ่ายรับผิดชอบ</th><th class="p-2 border w-28">กำหนดเสร็จ</th></tr>
                    <tr><td class="p-2 border">๑. รวบรวมบัญชีโครงการงบลงทุนต่ำกว่า ๕ แสน</td><td class="p-2 border">กองช่าง / กองคลัง</td><td class="p-2 border text-rose-600 font-bold">๑๕ พ.ย. ๖๙</td></tr>
                    <tr><td class="p-2 border">๒. จัดทำราคากลางเข้าระบบ e-Catalog</td><td class="p-2 border">งานพัสดุ</td><td class="p-2 border text-rose-600 font-bold">๓๐ พ.ย. ๖๙</td></tr>
                </table>
            </div>
        `
    },
    'doc-facebook': {
        title: 'ตัวอย่างโพสต์ Facebook ประชาสัมพันธ์ (Citizen-Centric)',
        subtitle: 'ย่อยภาษีที่ดินและสิ่งปลูกสร้าง ให้ประชาชนเข้าใจง่าย',
        html: `
            <div class="bg-slate-100 p-4 sm:p-6 rounded-2xl max-w-xl mx-auto font-sans">
                <div class="bg-white rounded-xl shadow-md border border-slate-200 overflow-hidden text-xs">
                    <div class="p-4 flex items-center gap-3 border-b border-slate-100">
                        <div class="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-sm">ทต.</div>
                        <div>
                            <div class="font-heading font-bold text-slate-900 text-sm">เทศบาลตำบลเมืองใหม่ ✓</div>
                            <div class="text-[11px] text-slate-400">เมื่อสักครู่ • 🌐 สาธารณะ</div>
                        </div>
                    </div>
                    <div class="p-4 space-y-3 text-slate-800 leading-relaxed text-sm">
                        <p class="font-bold text-blue-900 text-base">📢 ชำระภาษีที่ดินและสิ่งปลูกสร้าง 2569 ได้แล้ววันนี้ สะดวก สบาย ไม่ต้องรอนาน 🏠✨</p>
                        <div class="p-3.5 bg-blue-50 border border-blue-200 rounded-xl space-y-1.5 text-xs">
                            <div>1️⃣ ชำระ ณ กองคลัง เทศบาลตำบลเมืองใหม่</div>
                            <div>2️⃣ สแกน QR Code Mobile Banking ทุกธนาคาร</div>
                            <div>3️⃣ ชำระผ่านเคาน์เตอร์เซอร์วิส และ 7-Eleven</div>
                        </div>
                    </div>
                    <div class="bg-gradient-to-r from-blue-700 to-indigo-700 p-5 text-white text-center">
                        <div class="text-amber-300 font-bold text-xs">หมดเขต 30 เมษายน 2569</div>
                        <div class="text-lg font-heading font-bold">ภาษีที่ดินและสิ่งปลูกสร้าง เทศบาลตำบลเมืองใหม่</div>
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
                <div class="bg-white rounded-2xl shadow-md border border-slate-300 overflow-hidden text-xs">
                    <div class="bg-gov-800 text-white p-3 flex items-center gap-2">
                        <div class="font-bold">ศูนย์รับเรื่องร้องทุกข์ เทศบาลตำบลเมืองใหม่ (ตอบกลับทันที)</div>
                    </div>
                    <div class="p-4 space-y-3 bg-slate-50 min-h-[220px]">
                        <div class="flex justify-end">
                            <div class="bg-blue-600 text-white p-3 rounded-2xl rounded-tr-none max-w-[80%]">ไฟกิ่งซอย 5 ดับมา 3 คืนแล้ว รบกวนส่งช่างมาดูให้หน่อยครับ</div>
                        </div>
                        <div class="flex justify-start">
                            <div class="bg-white border border-slate-200 text-slate-800 p-3 rounded-2xl rounded-tl-none max-w-[85%] space-y-2">
                                <div class="text-rose-600 font-bold">❤️ เทศบาลขออภัยในความไม่สะดวกครับ</div>
                                <div>แอดมินส่งเรื่องประสานกองช่างแล้ว (รหัส #EF-6902) ช่างจะลงพื้นที่เปลี่ยนหลอดไฟพรุ่งนี้บ่าย (13.00-16.30 น.) ครับ</div>
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
                <h3 class="text-base font-heading font-bold text-gov-900 border-b pb-2">SWOT Matrix : ยุทธศาสตร์การพัฒนาการท่องเที่ยวชุมชนริมน้ำ</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-3 rounded-xl bg-emerald-50 border border-emerald-200 space-y-1">
                        <div class="font-bold text-emerald-800">💪 จุดแข็ง (S)</div>
                        <p>มีต้นทุนวัฒนธรรมริมน้ำและวัดโบราณ 200 ปี ชุมชนเข้มแข็ง</p>
                    </div>
                    <div class="p-3 rounded-xl bg-amber-50 border border-amber-200 space-y-1">
                        <div class="font-bold text-amber-800">⚠️ จุดอ่อน (W)</div>
                        <p>ปัญหาขยะตกค้างริมตลิ่ง ขาดช่องทางชำระเงินดิจิทัล</p>
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
                <h3 class="text-base font-heading font-bold text-gov-900 border-b pb-2">ผังกระบวนงาน SOP: การขอรับใบอนุญาตก่อสร้าง (แบบ อ.1)</h3>
                <table class="w-full text-left border-collapse border border-slate-200 text-xs">
                    <tr class="bg-slate-100 font-bold"><th class="p-2 border">ขั้นตอน</th><th class="p-2 border">กระบวนงาน</th><th class="p-2 border">เดิม</th><th class="p-2 border text-emerald-700">ปรับปรุงใหม่</th></tr>
                    <tr><td class="p-2 border">1</td><td class="p-2 border">ยื่นคำขอและตรวจเอกสารเบื้องต้น</td><td class="p-2 border">2 วัน</td><td class="p-2 border text-emerald-700 font-bold">1 วัน</td></tr>
                    <tr><td class="p-2 border">2</td><td class="p-2 border">ตรวจแบบแปลนและตรวจสถานที่</td><td class="p-2 border">7 วัน</td><td class="p-2 border text-emerald-700 font-bold">2 วัน</td></tr>
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
                        <div class="font-bold text-rose-800">❌ Bad Prompt (ละเมิด PDPA)</div>
                        <div class="p-2 bg-white rounded border border-rose-200 font-mono text-[11px]">"ช่วยสรุปข้อร้องเรียนของนายสมศักดิ์ รักดี เลขบัตร 3-5099-00123-45-6..."</div>
                    </div>
                    <div class="p-4 rounded-xl bg-emerald-50 border border-emerald-200 space-y-2">
                        <div class="font-bold text-emerald-800">✅ Good Prompt (ปลอดภัย 100%)</div>
                        <div class="p-2 bg-white rounded border border-emerald-200 font-mono text-[11px]">"บทบาท: นิติกร... งาน: ร่างแบบฟอร์มตรวจสอบข้อเท็จจริงตาม พ.ร.บ. จัดซื้อจัดจ้างฯ..."</div>
                    </div>
                </div>
            </div>
        `
    }
};
