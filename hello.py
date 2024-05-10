from huggingface_hub import login
login(token = "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")

tokenizer = AutoTokenizer.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    cache_dir="/kaggle/working/"
)

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    cache_dir="/kaggle/working/",
    device_map="auto",
)
