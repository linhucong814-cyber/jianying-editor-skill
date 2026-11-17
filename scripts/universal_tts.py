import asyncio
import re
from typing import Optional, Tuple


async def _run_edge_tts(text: str, output_file: str, voice: str = "zh-CN-YunxiNeural"):
    try:
        import edge_tts

        actual_path = output_file
        if output_file.endswith(".ogg") and not output_file.endswith(".mp3"):
            actual_path = output_file + ".mp3"

        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(actual_path)
        return True, actual_path
    except Exception as e:
        return False, f"Edge-TTS Error: {str(e)}"


async def generate_voice_with_meta(
    text: str,
    output_path: str,
    speaker: str = "zh_male_huoli",
    *,
    backend: Optional[str] = None,
    allow_fallback: bool = True,
    sami_retries: int = 2,
) -> Tuple[Optional[str], Optional[str]]:
    """Return the audio path and backend used. Legacy SAMI retries are ignored."""
    if backend == "sami" or (backend is None and not allow_fallback):
        print("[!] Native JianYing TTS is unavailable in this community release.", flush=True)
        return None, None

    if re.fullmatch(r"[a-z]{2,3}-[A-Za-z]+-[A-Za-z0-9]+Neural", speaker):
        voice = speaker
    else:
        voice = "zh-CN-YunxiNeural" if speaker.startswith("zh_male_") else "zh-CN-XiaoxiaoNeural"

    ok_edge, res_edge = await _run_edge_tts(text, output_path, voice)
    if ok_edge:
        print(f"[+] Edge-TTS Success: {res_edge}", flush=True)
        return res_edge, "edge"
    print(f"[!] {res_edge}", flush=True)
    return None, None


async def generate_voice(
    text: str,
    output_path: str,
    speaker: str = "zh_male_huoli",
    *,
    backend: Optional[str] = None,
    allow_fallback: bool = True,
    sami_retries: int = 2,
):
    path, _backend_used = await generate_voice_with_meta(
        text,
        output_path,
        speaker,
        backend=backend,
        allow_fallback=allow_fallback,
        sami_retries=sami_retries,
    )
    return path


if __name__ == "__main__":
    asyncio.run(generate_voice("测试智能配音系统集成成功。", "test.ogg"))
