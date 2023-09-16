from transformers import pipeline
from transformers import AutoTokenizer
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM , BitsAndBytesConfig
from langchain.llms import HuggingFacePipeline
import torch
from huggingface_hub import login
login(token="hf_xxx")
from elevenlabs import set_api_key

set_api_key("xxxx")
def local_llm() :
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=getattr(torch, "float16"),
        bnb_4bit_use_double_quant=False)
    model = AutoModelForCausalLM.from_pretrained(
            "meta-llama/Llama-2-13b-chat-hf",
            quantization_config=bnb_config,
            device_map={"": 0})
    model.config.use_cache = False
    model.config.pretraining_tp = 1
    model = PeftModel.from_pretrained(model, "TuningAI/Llama2_13B_startup_Assistant")
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-13b-chat-hf" , trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    pipe = pipeline("text-generation",model=model,tokenizer=tokenizer,max_length=2048,temperature=0.5,top_p=0.95,repetition_penalty=1.15)
    local_llm = HuggingFacePipeline(pipeline=pipe)
    return local_llm
from elevenlabs import generate, play
def audiof(text) : 
    audio = generate(text=text,voice="Charlie")
    play(audio=audio)