import yaml
import argparse
from pyannote.audio import Pipeline
import torch
from pydub import AudioSegment
import os

def main(audio_path):
    with open('./config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    use_auth_token = config['huggingface']['use_auth_token']

    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token=use_auth_token)

    # send pipeline to GPU (when available)
    pipeline.to(torch.device("cuda"))

    # apply pretrained pipeline
    diarization = pipeline(audio_path, min_speakers=2, max_speakers=5)

    segments = []
    # print the result
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        if (turn.end - turn.start) >= 3.0:
            segments.append([turn.start, turn.end, speaker])

    audio = AudioSegment.from_file(audio_path)

    # 处理每个时间段
    for segment in segments:
        [start_time, stop_time, speaker] = segment
        
        # 剪切音频
        cut_audio = audio[(start_time * 1000):(stop_time * 1000)]

        # 创建保存音频的文件夹（如果不存在）
        os.makedirs(speaker, exist_ok=True)

        # 保存剪切后的音频
        cut_audio.export(f"{speaker}/{start_time:.1f}_{stop_time:.1f}.wav", format="wav")

    print("处理完成！")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run speaker diarization on an audio file.")
    parser.add_argument("audio_path", help="Path to the audio file")
    args = parser.parse_args()
    main(args.audio_path)
