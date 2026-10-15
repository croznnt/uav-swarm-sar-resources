"""Build the curated Vietnamese resource index using only the standard library."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    entries = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    assert len({e['repo'] for e in entries}) == len(entries)
    fields = list(entries[0])
    with (ROOT / 'catalog.csv').open('w', newline='', encoding='utf-8-sig') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(entries)
    rows = []
    profiles = ROOT / 'repositories'
    profiles.mkdir(exist_ok=True)
    for e in entries:
        slug = e['repo'].replace('/', '__')
        url = 'https://github.com/' + e['repo']
        rows.append(f"| [{e['name']}]({url}) | {e['group']} | {e['stack']} | {e['sar']} | [Chi tiết](repositories/{slug}.md) |")
        (profiles / f'{slug}.md').write_text(
            f"# {e['name']}\n\n[Nguồn chính thức]({url})\n\n"
            f"## Vai trò\n\n{e['capability']}\n\n"
            f"## Liên hệ với tìm kiếm cứu nạn\n\n{e['sar']}\n\n{e['extension']}\n\n"
            f"## Bài tập đầu tiên đề xuất\n\n{e['exercise']}\n\n"
            f"## Điều kiện và giới hạn\n\n{e['caveat']}\n\n"
            f"Nền tảng: {e['stack']}.\n\n"
            f"Ngày đọc nguồn: {e['checked']}. Trạng thái kiểm chứng: chỉ đọc tài liệu, chưa cài đặt hoặc chạy mô phỏng. Bài tập là đề xuất của danh mục. Kiểm tra LICENSE ở phiên bản được chọn trước khi tái sử dụng mã.\n",
            encoding='utf-8')
    template = (ROOT / 'docs' / 'README.template.md').read_text(encoding='utf-8')
    (ROOT / 'README.md').write_text(template.replace('{{COUNT}}', str(len(entries))).replace('{{TABLE}}', '\n'.join(rows)), encoding='utf-8')
    print(f'Built {len(entries)} profiles, README.md and catalog.csv')


if __name__ == '__main__':
    main()
