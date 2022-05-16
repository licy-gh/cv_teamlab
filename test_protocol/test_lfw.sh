# test lfw on rec_swin_18
python test_lfw.py \
    --test_set 'LFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swin_18' 2>&1 | tee ../log/test/rec/test_rec_swin_18_lfw.log

# test calfw on rec_swin_18
python test_lfw.py \
    --test_set 'CALFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swin_18' 2>&1 | tee ../log/test/rec/test_rec_swin_18_calfw.log

# test cplfw on rec_swin_18
python test_lfw.py \
    --test_set 'CPLFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swin_18' 2>&1 | tee ../log/test/rec/test_rec_swin_18_cplfw.log

# test lfw on rec_swin_cr_18
python test_lfw.py \
    --test_set 'LFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swin_cr_18' 2>&1 | tee ../log/test/rec/test_rec_swin_cr_18_lfw.log

# test calfw on rec_swin_cr_18
python test_lfw.py \
    --test_set 'CALFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swin_cr_18' 2>&1 | tee ../log/test/rec/test_rec_swin_cr_18_calfw.log

# test cplfw on rec_swin_cr_18
python test_lfw.py \
    --test_set 'CPLFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformer' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swin_cr_18' 2>&1 | tee ../log/test/rec/test_rec_swin_cr_18_cplfw.log

# test lfw on rec_swinnew_cr_18
python test_lfw.py \
    --test_set 'LFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerNew' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swinnew_cr_18' 2>&1 | tee ../log/test/rec/test_rec_swinnew_cr_18_lfw.log

# test calfw on rec_swinnew_cr_18
python test_lfw.py \
    --test_set 'CALFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerNew' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swinnew_cr_18' 2>&1 | tee ../log/test/rec/test_rec_swinnew_cr_18_calfw.log

# test cplfw on rec_swinnew_cr_18
python test_lfw.py \
    --test_set 'CPLFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerNew' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/rec_swinnew_cr_18' 2>&1 | tee ../log/test/rec/test_rec_swinnew_cr_18_cplfw.log
