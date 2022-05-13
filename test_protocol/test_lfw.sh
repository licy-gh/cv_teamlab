python test_lfw.py \
    --test_set 'LFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/train_recog_out_dir' 2>&1 | tee test_lfw_log.log