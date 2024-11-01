import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import gc

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
model_id = "openai/whisper-large-v3"
print(f'{device = } | {torch_dtype = }')


model = AutoModelForSpeechSeq2Seq.from_pretrained(model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True,
                                             device_map=device).eval()
processor = AutoProcessor.from_pretrained(model_id)


pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=400,
    chunk_length_s=30,  # or Sequential or chunking
    batch_size=12,
    return_timestamps=True,
    torch_dtype=torch_dtype,
)


