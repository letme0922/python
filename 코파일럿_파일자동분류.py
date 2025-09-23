import os
import shutil
from pathlib import Path

# 다운로드 폴더 경로
download_dir = Path(r"C:\Users\JTG\Downloads")

# 이동할 폴더 경로
base_dir = download_dir.parent  # C:\Users\JTG
folders = {
    "images": ["*.jpg", "*.jpeg"],
    "data": ["*.csv", "*.xlsx"],
    "docs": ["*.txt", "*.doc", "*.pdf"],
    "archive": ["*.zip"]
}

# 폴더 생성
for folder in folders:
    target_path = base_dir / folder
    target_path.mkdir(exist_ok=True)

# 파일 이동
for folder, patterns in folders.items():
    target_path = base_dir / folder
    for pattern in patterns:
        for file_path in download_dir.glob(pattern):
            try:
                shutil.move(str(file_path), str(target_path / file_path.name))
                print(f"{file_path.name} → {target_path}")
            except Exception as e:
                print(f"오류: {file_path.name} 이동 실패 - {e}")