python test_lfw.py \
    --test_set 'LFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/FaceX-Zoo/training_mode/swin_training/out_dir'
