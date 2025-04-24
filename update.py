import os

folder_path = '/home/ubuntu/damf2/nielsen/data/tv3'
output_folder = '/home/ubuntu/damf2/nielsen/new/tv3'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        print(f"처리 중: {filename}")
        filepath = os.path.join(folder_path, filename)
        output_path = os.path.join(output_folder, filename)

        base_filename = os.path.splitext(filename)[0]

        try:
            with open(filepath, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
                for line in infile:
                    line = line.strip()
                    new_line = f"{line},{base_filename}\n"
                    outfile.write(new_line)
        except Exception as e:
            print(f"에러 발생 - 파일: {filename}, 메시지: {e}")

print("모든 파일 처리 완료!")