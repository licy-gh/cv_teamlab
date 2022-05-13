# det_swin_18
export OMP_NUM_THREADS=2
python -m torch.distributed.launch --nproc_per_node=2 --nnodes=1 --node_rank=0 --master_addr="127.0.0.1" --master_port=1324 train.py --data_root '/root/autodl-tmp/msra_tiny_old' --train_file '/root/FaceX-Zoo/data/files/msra_tiny_det_train_list.txt' --backbone_type 'SwinTransformer' --backbone_conf_file '../backbone_conf.yaml' --head_type 'MV-Softmax' --head_conf_file '../head_conf.yaml' --lr 5e-4 --out_dir '/root/autodl-tmp/models_out/det_swin_18' --epoches 18 --warm_up_epoches 3 --print_freq 200 --save_freq 3000 --batch_size 64  --log_dir 'log' --tensorboardx_logdir 'mv-swin' 2>&1 | tee train_det_swin_18.log

# det_swin_cr_18
python -m torch.distributed.launch --nproc_per_node=2 --nnodes=1 --node_rank=0 --master_addr="127.0.0.1" --master_port=1324 train.py --data_root '/root/autodl-tmp/msra_tiny_cropped' --train_file '/root/FaceX-Zoo/data/files/msra_tiny_det_train_list.txt' --backbone_type 'SwinTransformer' --backbone_conf_file '../backbone_conf.yaml' --head_type 'MV-Softmax' --head_conf_file '../head_conf.yaml' --lr 5e-4 --out_dir '/root/autodl-tmp/models_out/det_swin_cr_18' --epoches 18 --warm_up_epoches 3 --print_freq 200 --save_freq 3000 --batch_size 64  --log_dir 'log' --tensorboardx_logdir 'mv-swin' 2>&1 | tee train_det_swin_cr_18.log

# det_swinnew_cr_18
python -m torch.distributed.launch --nproc_per_node=2 --nnodes=1 --node_rank=0 --master_addr="127.0.0.1" --master_port=1324 train.py --data_root '/root/autodl-tmp/msra_tiny_cropped' --train_file '/root/FaceX-Zoo/data/files/msra_tiny_det_train_list.txt' --backbone_type 'SwinTransformerNew' --backbone_conf_file '../backbone_conf.yaml' --head_type 'MV-Softmax' --head_conf_file '../head_conf.yaml' --lr 5e-4 --out_dir '/root/autodl-tmp/models_out/det_swinnew_cr_18' --epoches 18 --warm_up_epoches 3 --print_freq 200 --save_freq 3000 --batch_size 64  --log_dir 'log' --tensorboardx_logdir 'mv-swin' 2>&1 | tee train_det_swinnew_cr_18.log

cd /root/FaceX-Zoo/test_protocol/

# test lfw on rec_swin_18
python test_lfw.py \
    --test_set 'LFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swin_18' 2>&1 | tee test_rec_swin_18_lfw.log

# test calfw on rec_swin_18
python test_lfw.py \
    --test_set 'CALFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swin_18' 2>&1 | tee test_rec_swin_18_calfw.log

# test cplfw on rec_swin_18
python test_lfw.py \
    --test_set 'CPLFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swin_18' 2>&1 | tee test_rec_swin_18_cplfw.log

# test lfw on rec_swin_cr_18
python test_lfw.py \
    --test_set 'LFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swin_cr_18' 2>&1 | tee test_rec_swin_cr_18_lfw.log

# test calfw on rec_swin_cr_18
python test_lfw.py \
    --test_set 'CALFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swin_cr_18' 2>&1 | tee test_rec_swin_cr_18_calfw.log

# test cplfw on rec_swin_cr_18
python test_lfw.py \
    --test_set 'CPLFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swin_cr_18' 2>&1 | tee test_rec_swin_cr_18_cplfw.log

# test lfw on rec_swinnew_cr_18
python test_lfw.py \
    --test_set 'LFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerNew' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swinnew_cr_18' 2>&1 | tee test_rec_swinnew_cr_18_lfw.log

# test calfw on rec_swinnew_cr_18
python test_lfw.py \
    --test_set 'CALFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerNew' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swinnew_cr_18' 2>&1 | tee test_rec_swinnew_cr_18_calfw.log

# test cplfw on rec_swinnew_cr_18
python test_lfw.py \
    --test_set 'CPLFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerNew' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swinnew_cr_18' 2>&1 | tee test_rec_swinnew_cr_18_cplfw.log
