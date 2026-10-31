/**
 * =========================================================================
 * GOOGLE APPS SCRIPT: ระบบฐานข้อมูลผู้เข้าอบรม AI สำหรับ อปท. (4 รุ่น)
 * =========================================================================
 * คำแนะนำการติดตั้ง:
 * 1. เปิด Google Sheets ใหม่ (https://sheets.new)
 * 2. ตั้งชื่อไฟล์ เช่น "ฐานข้อมูลผู้เข้าอบรม AI อปท. 2569 (4 รุ่น)"
 * 3. ไปที่เมนู ส่วนขยาย (Extensions) > Apps Script
 * 4. ลบโค้ดเดิมทั้งหมด แล้ววางโค้ดชุดนี้ลงไปทั้งหมด
 * 5. กดปุ่ม "ทำให้ใช้งานได้" (Deploy) > "การทำให้ใช้งานได้รายการใหม่" (New Deployment)
 *    - ประเภท: เว็บแอป (Web App)
 *    - คำอธิบาย: AI LG Database v1
 *    - ดำเนินการในฐานะ: ตัวฉัน (Me)
 *    - ผู้มีสิทธิ์เข้าถึง: ทุกคน (Anyone)  *** สำคัญมาก ต้องเลือก Anyone ***
 * 6. กด "ทำให้ใช้งานได้" (Deploy) แล้วคัดลอก "URL ของเว็บแอป" (Web App URL)
 * 7. นำ Web App URL ไปวางในระบบ ai.html
 * =========================================================================
 */

function doGet(e) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheetsInfo = [];
  try {
    var allSheets = ss.getSheets();
    for (var i = 0; i < allSheets.length; i++) {
      sheetsInfo.push({
        name: allSheets[i].getName(),
        rows: allSheets[i].getLastRow()
      });
    }
  } catch (err) {}

  return ContentService.createTextOutput(JSON.stringify({
    status: "online",
    spreadsheetName: ss ? ss.getName() : "Unknown",
    spreadsheetUrl: ss ? ss.getUrl() : "Unknown",
    sheets: sheetsInfo,
    message: "AI Local Government Workshop Database API is running ready for 4 batches!"
  })).setMimeType(ContentService.MimeType.JSON);
}

function doPost(e) {
  try {
    var rawContent = e.postData.contents;
    var data = JSON.parse(rawContent);
    
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var timestamp = Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
    
    var batchName = data.batch || "รุ่นที่ 1";
    // Normalize batch name to standard Thai
    if (batchName.indexOf("1") > -1 || batchName.indexOf("๑") > -1) batchName = "รุ่นที่ 1";
    else if (batchName.indexOf("2") > -1 || batchName.indexOf("๒") > -1) batchName = "รุ่นที่ 2";
    else if (batchName.indexOf("3") > -1 || batchName.indexOf("๓") > -1) batchName = "รุ่นที่ 3";
    else if (batchName.indexOf("4") > -1 || batchName.indexOf("๔") > -1) batchName = "รุ่นที่ 4";
    
    var rowData = [
      timestamp,
      data.fullName || "ไม่ระบุชื่อ",
      data.position || "-",
      data.department || "-",
      data.organization || "-",
      batchName,
      data.quizScore !== undefined ? (data.quizScore + " / " + (data.quizTotal || 5)) : "ยังไม่สอบ",
      data.quizPassed ? "ผ่านเกณฑ์รับเกียรติบัตร" : (data.quizScore !== undefined ? "ต้องปรับปรุง" : "รอทดสอบ"),
      data.certificateId || "-",
      data.savedPromptsCount || 0
    ];
    
    // 1. Write to Specific Batch Tab (เช่น รุ่นที่ 1, รุ่นที่ 2...)
    var batchSheet = getOrCreateSheet(ss, batchName, [
      "วัน-เวลาบันทึก", "ชื่อ-นามสกุล", "ตำแหน่ง", "ฝ่าย/กอง", "อปท. / หน่วยงาน", 
      "รุ่นที่", "คะแนน Post-Test", "สถานะการประเมิน", "รหัสใบประกาศฯ (Cert ID)", "จำนวน Prompt ในแฟ้ม"
    ]);
    batchSheet.appendRow(rowData);
    
    // 2. Write to Master All Batches Tab (ภาพรวมทุกรุ่น)
    var masterSheet = getOrCreateSheet(ss, "ภาพรวม 4 รุ่น (Master)", [
      "วัน-เวลาบันทึก", "ชื่อ-นามสกุล", "ตำแหน่ง", "ฝ่าย/กอง", "อปท. / หน่วยงาน", 
      "รุ่นที่", "คะแนน Post-Test", "สถานะการประเมิน", "รหัสใบประกาศฯ (Cert ID)", "จำนวน Prompt ในแฟ้ม"
    ]);
    masterSheet.appendRow(rowData);

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      message: "บันทึกข้อมูลเรียบร้อยแล้ว (" + batchName + ")",
      batch: batchName,
      timestamp: timestamp
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function getOrCreateSheet(ss, sheetName, headers) {
  var sheet = ss.getSheetByName(sheetName);
  if (!sheet) {
    sheet = ss.insertSheet(sheetName);
    // Add header row
    sheet.appendRow(headers);
    // Format header row
    var headerRange = sheet.getRange(1, 1, 1, headers.length);
    headerRange.setBackground("#1e3a8a");
    headerRange.setFontColor("#ffffff");
    headerRange.setFontWeight("bold");
    headerRange.setHorizontalAlignment("center");
    sheet.setFrozenRows(1);
    
    // Auto-resize columns
    for (var i = 1; i <= headers.length; i++) {
      sheet.setColumnWidth(i, 160);
    }
  }
  return sheet;
}
