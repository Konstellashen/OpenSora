# sample size
num_frames = 1
frame_interval = 1
image_size = (256, 256)

# dataset
root = None
data_path = "/mnt/hdd/data/csv/imagenet_train.csv"
use_image_transform = True
num_workers = 4

# acceleration
dtype = "fp16"
grad_checkpoint = True
plugin = "zero2"
sp_size = 1

# model config
model = dict(
    type="DiT-XL/2",
    no_temporal_pos_emb=True,
    enable_flashattn=True,
    enable_layernorm_kernel=True,
)
vae = dict(
    type="VideoAutoencoderKL",
    from_pretrained="stabilityai/sd-vae-ft-ema",
)
text_encoder = dict(
    type="clip",
    from_pretrained="openai/clip-vit-base-patch32",
    model_max_length=77,
)
scheduler = dict(
    type="iddpm",
    timestep_respacing="",
)

# runtime
seed = 42
outputs = "outputs"
wandb = False

epochs = 1000
log_every = 10
ckpt_every = 1000
load = None

batch_size = 128
lr = 1e-4  # according to DiT repo
grad_clip = 1.0