#!/usr/bin/env python3
"""Generate a first-draft Thai official letter for a รพ.สต. from JSON data."""

import argparse
import json
import sys
from pathlib import Path


def value(data, key, default):
    item = data.get(key)
    if item is None or item == "":
        return default
    return str(item)


def optional_line(label, content):
    if content in (None, ""):
        return f"{label} [ถ้ามี]"
    return f"{label} {content}"


def external(data):
    org = value(data, "organization", "[ชื่อ รพ.สต./หน่วยงานเจ้าของหนังสือ]")
    address = value(data, "address", "[ที่อยู่หน่วยงาน]")
    ref = data.get("reference")
    enclosure = data.get("enclosure")
    return f"""[ตราครุฑ]

ที่ {value(data, "number", "[เลขที่หนังสือ]")}  
{org}  
{address}

{value(data, "date", "[วัน เดือน พ.ศ.]")}

เรื่อง {value(data, "subject", "[เรื่อง]")}

เรียน {value(data, "recipient", "[ตำแหน่ง/ชื่อผู้รับ]")}

{optional_line("อ้างถึง", ref)}

{optional_line("สิ่งที่ส่งมาด้วย", enclosure)}

{value(data, "background", "[ย่อหน้าเหตุ: ด้วย/ตามที่ + ข้อเท็จจริงหรือที่มา]")}

{value(data, "request", "[ย่อหน้าดำเนินการ: ในการนี้ + รายละเอียดกิจกรรม/คำขอ/กำหนดเวลา/สถานที่/เอกสารแนบ]")}

จึงเรียนมาเพื่อโปรด{value(data, "closing_purpose", "[ทราบ/พิจารณา/อนุมัติ/ดำเนินการ]")} {value(data, "closing_detail", "[ข้อความปิดท้ายให้ตรงวัตถุประสงค์]")}

ขอแสดงความนับถือ


({value(data, "signer_name", "[ชื่อผู้ลงนาม]")})  
{value(data, "signer_position", "[ตำแหน่งผู้ลงนาม]")}

{value(data, "owner_unit", "[หน่วยงานเจ้าของเรื่อง]")}  
โทร. {value(data, "phone", "[หมายเลขโทรศัพท์]")}  
อีเมล {value(data, "email", "[อีเมล ถ้ามี]")}
"""


def internal(data):
    return f"""บันทึกข้อความ

ส่วนราชการ {value(data, "organization", "[ชื่อ รพ.สต./กลุ่มงาน]")} โทร. {value(data, "phone", "[หมายเลขโทรศัพท์]")}

ที่ {value(data, "number", "[เลขที่หนังสือ]")} วันที่ {value(data, "date", "[วัน เดือน พ.ศ.]")}

เรื่อง {value(data, "subject", "[เรื่อง]")}

เรียน {value(data, "recipient", "[ตำแหน่ง/ชื่อผู้รับ]")}

{value(data, "background", "[ย่อหน้าเหตุ: ด้วย/ตามที่ + ข้อเท็จจริงหรือที่มา]")}

{value(data, "request", "[ย่อหน้าดำเนินการ: รายละเอียดที่ขออนุมัติ ขอความเห็นชอบ แจ้งเพื่อทราบ หรือมอบหมาย]")}

จึงเรียนมาเพื่อโปรด{value(data, "closing_purpose", "[ทราบ/พิจารณา/อนุมัติ/สั่งการ]")}


({value(data, "signer_name", "[ชื่อผู้ลงนาม]")})  
{value(data, "signer_position", "[ตำแหน่งผู้ลงนาม]")}
"""


def load_data(path):
    if path == "-":
        return json.load(sys.stdin)
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description="Generate Thai official correspondence drafts for รพ.สต.")
    parser.add_argument("--type", choices=("external", "internal"), required=True, help="Letter form to generate")
    parser.add_argument("--data", default="-", help="JSON file path, or '-' for stdin")
    args = parser.parse_args()

    data = load_data(args.data)
    if args.type == "external":
        print(external(data))
    else:
        print(internal(data))


if __name__ == "__main__":
    main()
