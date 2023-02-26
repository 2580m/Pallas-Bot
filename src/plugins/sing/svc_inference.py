import os
import platform
from threading import Lock
from pathlib import Path
from pydub import AudioSegment

SVC_MAIN = (Path(__file__).parent / 'so_vits_svc' /
            'inference_main.py').absolute()
SVC_HUBERT = Path(
    'resource/sing/models/checkpoint_best_legacy_500.pt').absolute()
SVC_SLICE_DB = -40
SVC_OUPUT_FORMAT = 'flac'

cuda_devices = ''


def set_svc_cuda_devices(devices: str):
    global cuda_devices
    cuda_devices = devices


speaker_models = {}


def inference(song_path: Path, output_dir: Path, key: int = 0, speaker: str = "pallas", locker: Lock = Lock()):
    # 这个库不知道咋集成，似乎可以转成 ONNX，但是我不会
    # 先用 cmd 凑合跑了
    # TODO: 使用 ONNX Runtime 重新集成

    if platform.system() == "Windows":
        song_path = mp3_to_wav(song_path)

    stem = song_path.stem
    result = output_dir / \
        f'{stem}_{key}key_{speaker}.{SVC_OUPUT_FORMAT}'

    if not result.exists():
        global speaker_models

        model = ""
        if speaker not in speaker_models:
            models_dir = Path(f'resource/sing/models/{speaker}/')
            for m in os.listdir(models_dir):
                if m.startswith('G_') and m.endswith('.pth'):
                    speaker_models[speaker] = models_dir / m
                    break

        model = speaker_models[speaker].absolute()
        config = Path(f'resource/sing/models/{speaker}/config.json').absolute()

        if not os.path.exists(model) or not os.path.exists(config):
            print("!!! Model or config not found !!!")
            return None
        if not os.path.exists(SVC_HUBERT):
            print("!!! Hubert model not found !!!")
            return None

        cmd = ''
        if cuda_devices:
            cmd = f'CUDA_VISIBLE_DEVICES={cuda_devices} '
        cmd += f'python {SVC_MAIN} -m {model} -c {config} -hb {SVC_HUBERT.absolute()} \
            -f {song_path.absolute()} -t {key} -s {speaker} -sd {SVC_SLICE_DB} \
            -o {output_dir.absolute()} -wf {SVC_OUPUT_FORMAT}'
        with locker:
            print(cmd)
            os.system(cmd)

    if not result.exists():
        return None

    return result


def mp3_to_wav(mp3_file_path):
    mp3_dirname, mp3_filename = os.path.split(mp3_file_path)
    wav_filename = os.path.splitext(mp3_filename)[0] + '.wav'
    wav_file_path = os.path.join(mp3_dirname, wav_filename)

    if os.path.exists(wav_file_path):
        return Path(wav_file_path)

    sound = AudioSegment.from_mp3(mp3_file_path)
    sound.export(wav_file_path, format="wav")
    # os.remove(mp3_file_path)
    return Path(wav_file_path)
