"""
@author: Jun Wang 
@date: 20201019 
@contact: jun21wangustc@gmail.com    
"""

import sys
import yaml
sys.path.append('../../')
from backbone.Swin_Transformer import SwinTransformer
from backbone.Swin_Transformer_new import SwinTransformerNew
from backbone.Swin_Transformer_det import SwinTransformerDet
from backbone.Swin_Transformer_new_det import SwinTransformerNewDet

class BackboneFactory:
    """Factory to produce backbone according the backbone_conf.yaml.
    
    Attributes:
        backbone_type(str): which backbone will produce.
        backbone_param(dict):  parsed params and it's value. 
    """
    def __init__(self, backbone_type, backbone_conf_file):
        self.backbone_type = backbone_type
        with open(backbone_conf_file) as f:
            backbone_conf = yaml.load(f, Loader=yaml.FullLoader)
            self.backbone_param = backbone_conf[backbone_type]
        print('backbone param:')
        print(self.backbone_param)

    def get_backbone(self):
        img_size = self.backbone_param['img_size']
        patch_size= self.backbone_param['patch_size']
        in_chans = self.backbone_param['in_chans']
        embed_dim = self.backbone_param['embed_dim']
        depths = self.backbone_param['depths']
        num_heads = self.backbone_param['num_heads']
        window_size = self.backbone_param['window_size']
        mlp_ratio = self.backbone_param['mlp_ratio']
        drop_rate = self.backbone_param['drop_rate']
        drop_path_rate = self.backbone_param['drop_path_rate']

        if self.backbone_type == 'SwinTransformer':
            backbone = SwinTransformer(img_size=img_size,
                                       patch_size=patch_size,
                                       in_chans=in_chans,
                                       embed_dim=embed_dim,
                                       depths=depths,
                                       num_heads=num_heads,
                                       window_size=window_size,
                                       mlp_ratio=mlp_ratio,
                                       qkv_bias=True,
                                       qk_scale=None,
                                       drop_rate=drop_rate,
                                       drop_path_rate=drop_path_rate,
                                       ape=False,
                                       patch_norm=True,
                                       use_checkpoint=False)

        elif self.backbone_type == 'SwinTransformerNew':
            backbone = SwinTransformerNew(img_size=img_size,
                                       patch_size=patch_size,
                                       in_chans=in_chans,
                                       embed_dim=embed_dim,
                                       depths=depths,
                                       num_heads=num_heads,
                                       window_size=window_size,
                                       mlp_ratio=mlp_ratio,
                                       qkv_bias=True,
                                       qk_scale=None,
                                       drop_rate=drop_rate,
                                       drop_path_rate=drop_path_rate,
                                       ape=False,
                                       patch_norm=True,
                                       use_checkpoint=False)

        elif self.backbone_type == 'SwinTransformerDet':
            backbone = SwinTransformerDet(img_size=img_size,
                                       patch_size=patch_size,
                                       in_chans=in_chans,
                                       embed_dim=embed_dim,
                                       depths=depths,
                                       num_heads=num_heads,
                                       window_size=window_size,
                                       mlp_ratio=mlp_ratio,
                                       qkv_bias=True,
                                       qk_scale=None,
                                       drop_rate=drop_rate,
                                       drop_path_rate=drop_path_rate,
                                       ape=False,
                                       patch_norm=True,
                                       use_checkpoint=False)


        elif self.backbone_type == 'SwinTransformerNewDet':
            backbone = SwinTransformerNewDet(img_size=img_size,
                                       patch_size=patch_size,
                                       in_chans=in_chans,
                                       embed_dim=embed_dim,
                                       depths=depths,
                                       num_heads=num_heads,
                                       window_size=window_size,
                                       mlp_ratio=mlp_ratio,
                                       qkv_bias=True,
                                       qk_scale=None,
                                       drop_rate=drop_rate,
                                       drop_path_rate=drop_path_rate,
                                       ape=False,
                                       patch_norm=True,
                                       use_checkpoint=False)

        else:
            pass
        return backbone
