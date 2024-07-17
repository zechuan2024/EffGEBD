import json
import os
import subprocess

# 路径
json_path = '/workspace/GEBD/ZZC/.venv/testenvironment/EfficientGEBD/data/TAPOS/tapos_annotation.json'
video_folder = '/workspace/GEBD/ZZC/.venv/testenvironment/EfficientGEBD/data/TAPOS/rawvideo'
output_folder = '/workspace/GEBD/ZZC/.venv/testenvironment/EfficientGEBD/data/TAPOS/trim_video'

# 创建输出文件夹（如果不存在）
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 读取JSON文件
with open(json_path, 'r') as f:
    annotations = json.load(f)

# 遍历每个视频的注释
for video_id, segments in annotations.items():
    for segment_id, segment_info in segments.items():
        start_offset = float(segment_id.split('_')[1] + '.' + segment_id.split('_')[2])
        end_offset = float(segment_id.split('_')[3] + '.' + segment_id.split('_')[4])
        base_time = segment_info['shot_timestamps'][0]
        print(start_offset,end_offset,segment_id)
        assert 1==2
        # 计算起始和终止时间
        start_time = base_time + start_offset
        end_time = base_time + end_offset

        output_filename = f"{video_id}_{segment_id}.mp4"
        output_path = os.path.join(output_folder, output_filename)
        
        input_path = os.path.join(video_folder, f"{video_id}.mp4")

        if not os.path.exists(input_path):
            continue
        # ffmpeg命令
        command = [
            'ffmpeg',
            '-i', input_path,
            '-ss', str(start_time),
            '-to', str(end_time),
            output_path
        ]

        try:
            # 执行ffmpeg命令
            subprocess.run(command, check=True)
            print(f"成功剪切视频 {video_id} 到 {output_filename}")
        except subprocess.CalledProcessError as e:
            print(f"剪切视频 {video_id} 时出错: {e}")