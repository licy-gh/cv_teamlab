# test lfw on det_swin_18
python test_det.py \
    --test_set 'LFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerDet' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/det_swin_18' 2>&1 | tee ../log/test/det/test_det_swin_18_lfw.log

# test calfw on det_swin_18
python test_det.py \
    --test_set 'CALFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerDet' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/det_swin_18' 2>&1 | tee ../log/test/det/test_det_swin_18_calfw.log

# test cplfw on det_swin_18
python test_det.py \
    --test_set 'CPLFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerDet' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/det_swin_18' 2>&1 | tee ../log/test/det/test_det_swin_18_cplfw.log

# test lfw on det_swin_cr_18
python test_det.py \
    --test_set 'LFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerDet' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/det_swin_cr_18' 2>&1 | tee ../log/test/det/test_det_swin_cr_18_lfw.log

# test calfw on det_swin_cr_18
python test_det.py \
    --test_set 'CALFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerDet' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/det_swin_cr_18' 2>&1 | tee ../log/test/det/test_det_swin_cr_18_calfw.log

# test cplfw on det_swin_cr_18
python test_det.py \
    --test_set 'CPLFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerDet' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/det_swin_cr_18' 2>&1 | tee ../log/test/det/test_det_swin_cr_18_cplfw.log

# test lfw on det_swinnew_cr_18
python test_det.py \
    --test_set 'LFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerNewDet' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/det_swinnew_cr_18' 2>&1 | tee ../log/test/det/test_det_swinnew_cr_18_lfw.log

# test calfw on det_swinnew_cr_18
python test_det.py \
    --test_set 'CALFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerNewDet' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/det_swinnew_cr_18' 2>&1 | tee ../log/test/det/test_det_swinnew_cr_18_calfw.log

# test cplfw on det_swinnew_cr_18
python test_det.py \
    --test_set 'CPLFW' \
    --data_conf_file 'data_conf.yaml' \
    --backbone_type 'SwinTransformerNewDet' \
    --backbone_conf_file 'backbone_conf.yaml' \
    --batch_size 1024 \
    --model_path '/root/autodl-tmp/models_out/det_swinnew_cr_18' 2>&1 | tee ../log/test/det/test_det_swinnew_cr_18_cplfw.log
