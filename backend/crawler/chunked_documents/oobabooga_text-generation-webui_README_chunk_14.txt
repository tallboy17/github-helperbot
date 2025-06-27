Repository: oobabooga/text-generation-webui
Language: Python
Stars: 44003
Forks: 5671
-----
From time to time, the `requirements*.txt` change. To update, use these commands:  
```
conda activate textgen
cd text-generation-webui
pip install -r <requirements file that you have used> --upgrade
```
</details>  
<details>
<summary>
List of command-line flags
</summary>  
```txt
usage: server.py [-h] [--multi-user] [--model MODEL] [--lora LORA [LORA ...]] [--model-dir MODEL_DIR] [--lora-dir LORA_DIR] [--model-menu] [--settings SETTINGS]
[--extensions EXTENSIONS [EXTENSIONS ...]] [--verbose] [--idle-timeout IDLE_TIMEOUT] [--loader LOADER] [--cpu] [--cpu-memory CPU_MEMORY] [--disk] [--disk-cache-dir DISK_CACHE_DIR]
[--load-in-8bit] [--bf16] [--no-cache] [--trust-remote-code] [--force-safetensors] [--no_use_fast] [--use_flash_attention_2] [--use_eager_attention] [--torch-compile] [--load-in-4bit]
[--use_double_quant] [--compute_dtype COMPUTE_DTYPE] [--quant_type QUANT_TYPE] [--flash-attn] [--threads THREADS] [--threads-batch THREADS_BATCH] [--batch-size BATCH_SIZE] [--no-mmap]
[--mlock] [--gpu-layers N] [--tensor-split TENSOR_SPLIT] [--numa] [--no-kv-offload] [--row-split] [--extra-flags EXTRA_FLAGS] [--streaming-llm] [--ctx-size N] [--cache-type N]
[--model-draft MODEL_DRAFT] [--draft-max DRAFT_MAX] [--gpu-layers-draft GPU_LAYERS_DRAFT] [--device-draft DEVICE_DRAFT] [--ctx-size-draft CTX_SIZE_DRAFT] [--gpu-split GPU_SPLIT]
[--autosplit] [--cfg-cache] [--no_flash_attn] [--no_xformers] [--no_sdpa] [--num_experts_per_token N] [--enable_tp] [--cpp-runner] [--deepspeed] [--nvme-offload-dir NVME_OFFLOAD_DIR]
[--local_rank LOCAL_RANK] [--alpha_value ALPHA_VALUE] [--rope_freq_base ROPE_FREQ_BASE] [--compress_pos_emb COMPRESS_POS_EMB] [--listen] [--listen-port LISTEN_PORT]
[--listen-host LISTEN_HOST] [--share] [--auto-launch] [--gradio-auth GRADIO_AUTH] [--gradio-auth-path GRADIO_AUTH_PATH] [--ssl-keyfile SSL_KEYFILE] [--ssl-certfile SSL_CERTFILE]
[--subpath SUBPATH] [--old-colors] [--portable] [--api] [--public-api] [--public-api-id PUBLIC_API_ID] [--api-port API_PORT] [--api-key API_KEY] [--admin-key ADMIN_KEY]
[--api-enable-ipv6] [--api-disable-ipv4] [--nowebui]

Text generation web UI

options:
-h, --help                                show this help message and exit

Basic settings:
--multi-user                              Multi-user mode. Chat histories are not saved or automatically loaded. Warning: this is likely not safe for sharing publicly.
--model MODEL                             Name of the model to load by default.
--lora LORA [LORA ...]                    The list of LoRAs to load. If you want to load more than one LoRA, write the names separated by spaces.
--model-dir MODEL_DIR                     Path to directory with all the models.
--lora-dir LORA_DIR                       Path to directory with all the loras.
--model-menu                              Show a model menu in the terminal when the web UI is first launched.
--settings SETTINGS                       Load the default interface settings from this yaml file. See user_data/settings-template.yaml for an example. If you create a file called
user_data/settings.yaml, this file will be loaded by default without the need to use the --settings flag.
--extensions EXTENSIONS [EXTENSIONS ...]  The list of extensions to load. If you want to load more than one extension, write the names separated by spaces.
--verbose                                 Print the prompts to the terminal.
--idle-timeout IDLE_TIMEOUT               Unload model after this many minutes of inactivity. It will be automatically reloaded when you try to use it again.

Model loader:
--loader LOADER                           Choose the model loader manually, otherwise, it will get autodetected. Valid options: Transformers, llama.cpp, ExLlamav3_HF, ExLlamav2_HF, ExLlamav2,
TensorRT-LLM.

Transformers/Accelerate:
--cpu                                     Use the CPU to generate text. Warning: Training on CPU is extremely slow.
--cpu-memory CPU_MEMORY                   Maximum CPU memory in GiB. Use this for CPU offloading.
--disk                                    If the model is too large for your GPU(s) and CPU combined, send the remaining layers to the disk.
--disk-cache-dir DISK_CACHE_DIR           Directory to save the disk cache to. Defaults to "user_data/cache".
--load-in-8bit                            Load the model with 8-bit precision (using bitsandbytes).
--bf16                                    Load the model with bfloat16 precision. Requires NVIDIA Ampere GPU.
--no-cache                                Set use_cache to False while generating text. This reduces VRAM usage slightly, but it comes at a performance cost.
--trust-remote-code                       Set trust_remote_code=True while loading the model. Necessary for some models.
--force-safetensors                       Set use_safetensors=True while loading the model. This prevents arbitrary code execution.
--no_use_fast                             Set use_fast=False while loading the tokenizer (it's True by default). Use this if you have any problems related to use_fast.
--use_flash_attention_2                   Set use_flash_attention_2=True while loading the model.
--use_eager_attention                     Set attn_implementation= eager while loading the model.
--torch-compile                           Compile the model with torch.compile for improved performance.

bitsandbytes 4-bit:
--load-in-4bit                            Load the model with 4-bit precision (using bitsandbytes).
--use_double_quant                        use_double_quant for 4-bit.
--compute_dtype COMPUTE_DTYPE             compute dtype for 4-bit. Valid options: bfloat16, float16, float32.
--quant_type QUANT_TYPE                   quant_type for 4-bit. Valid options: nf4, fp4.

llama.cpp:
--flash-attn                              Use flash-attention.
--threads THREADS                         Number of threads to use.
--threads-batch THREADS_BATCH             Number of threads to use for batches/prompt processing.
--batch-size BATCH_SIZE                   Maximum number of prompt tokens to batch together when calling llama_eval.
--no-mmap                                 Prevent mmap from being used.
--mlock                                   Force the system to keep the model in RAM.
--gpu-layers N, --n-gpu-layers N          Number of layers to offload to the GPU.
--tensor-split TENSOR_SPLIT               Split the model across multiple GPUs. Comma-separated list of proportions. Example: 60,40.
--numa                                    Activate NUMA task allocation for llama.cpp.
--no-kv-offload                           Do not offload the K, Q, V to the GPU. This saves VRAM but reduces the performance.
--row-split                               Split the model by rows across GPUs. This may improve multi-gpu performance.
--extra-flags EXTRA_FLAGS                 Extra flags to pass to llama-server. Format: "flag1=value1,flag2,flag3=value3". Example: "override-tensor=exps=CPU"
--streaming-llm                           Activate StreamingLLM to avoid re-evaluating the entire prompt when old messages are removed.

Context and cache:
--ctx-size N, --n_ctx N, --max_seq_len N  Context size in tokens.
--cache-type N, --cache_type N            KV cache type; valid options: llama.cpp - fp16, q8_0, q4_0; ExLlamaV2 - fp16, fp8, q8, q6, q4; ExLlamaV3 - fp16, q2 to q8 (can specify k_bits and v_bits
separately, e.g. q4_q8).

Speculative decoding:
--model-draft MODEL_DRAFT                 Path to the draft model for speculative decoding.
--draft-max DRAFT_MAX                     Number of tokens to draft for speculative decoding.
--gpu-layers-draft GPU_LAYERS_DRAFT       Number of layers to offload to the GPU for the draft model.
--device-draft DEVICE_DRAFT               Comma-separated list of devices to use for offloading the draft model. Example: CUDA0,CUDA1
--ctx-size-draft CTX_SIZE_DRAFT           Size of the prompt context for the draft model. If 0, uses the same as the main model.

ExLlamaV2:
--gpu-split GPU_SPLIT                     Comma-separated list of VRAM (in GB) to use per GPU device for model layers. Example: 20,7,7.
--autosplit                               Autosplit the model tensors across the available GPUs. This causes --gpu-split to be ignored.
--cfg-cache                               ExLlamav2_HF: Create an additional cache for CFG negative prompts. Necessary to use CFG with that loader.
--no_flash_attn                           Force flash-attention to not be used.
--no_xformers                             Force xformers to not be used.
--no_sdpa                                 Force Torch SDPA to not be used.
--num_experts_per_token N                 Number of experts to use for generation. Applies to MoE models like Mixtral.
--enable_tp                               Enable Tensor Parallelism (TP) in ExLlamaV2.

TensorRT-LLM:
--cpp-runner                              Use the ModelRunnerCpp runner, which is faster than the default ModelRunner but doesn't support streaming yet.

DeepSpeed:
--deepspeed                               Enable the use of DeepSpeed ZeRO-3 for inference via the Transformers integration.
--nvme-offload-dir NVME_OFFLOAD_DIR       DeepSpeed: Directory to use for ZeRO-3 NVME offloading.
--local_rank LOCAL_RANK                   DeepSpeed: Optional argument for distributed setups.

RoPE:
--alpha_value ALPHA_VALUE                 Positional embeddings alpha factor for NTK RoPE scaling. Use either this or compress_pos_emb, not both.
--rope_freq_base ROPE_FREQ_BASE           If greater than 0, will be used instead of alpha_value. Those two are related by rope_freq_base = 10000 * alpha_value ^ (64 / 63).
--compress_pos_emb COMPRESS_POS_EMB       Positional embeddings compression factor. Should be set to (context length) / (model's original context length). Equal to 1/rope_freq_scale.

Gradio:
--listen                                  Make the web UI reachable from your local network.
--listen-port LISTEN_PORT                 The listening port that the server will use.
--listen-host LISTEN_HOST                 The hostname that the server will use.
--share                                   Create a public URL. This is useful for running the web UI on Google Colab or similar.
--auto-launch                             Open the web UI in the default browser upon launch.
--gradio-auth GRADIO_AUTH                 Set Gradio authentication password in the format "username:password". Multiple credentials can also be supplied with "u1:p1,u2:p2,u3:p3".
--gradio-auth-path GRADIO_AUTH_PATH       Set the Gradio authentication file path. The file should contain one or more user:password pairs in the same format as above.
--ssl-keyfile SSL_KEYFILE                 The path to the SSL certificate key file.
--ssl-certfile SSL_CERTFILE               The path to the SSL certificate cert file.
--subpath SUBPATH                         Customize the subpath for gradio, use with reverse proxy
--old-colors                              Use the legacy Gradio colors, before the December/2024 update.
--portable                                Hide features not available in portable mode like training.

API:
--api                                     Enable the API extension.
--public-api                              Create a public URL for the API using Cloudfare.
--public-api-id PUBLIC_API_ID             Tunnel ID for named Cloudflare Tunnel. Use together with public-api option.
--api-port API_PORT                       The listening port for the API.
--api-key API_KEY                         API authentication key.
--admin-key ADMIN_KEY                     API authentication key for admin tasks like loading and unloading models. If not set, will be the same as --api-key.
--api-enable-ipv6                         Enable IPv6 for the API
--api-disable-ipv4                        Disable IPv4 for the API
--nowebui                                 Do not launch the Gradio UI. Useful for launching the API in standalone mode.
```  
</details>