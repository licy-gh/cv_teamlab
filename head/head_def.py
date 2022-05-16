""" 
@author: Jun Wang
@date: 20201019
@contact: jun21wangustc@gmail.com   
""" 

import sys
import yaml
sys.path.append('../../')
from head.AdaCos import AdaCos
from head.AdaM_Softmax import Adam_Softmax
from head.AM_Softmax import AM_Softmax
from head.MV_Softmax import MV_Softmax

class HeadFactory:
    """Factory to produce head according to the head_conf.yaml
    
    Attributes:
        head_type(str): which head will be produce.
        head_param(dict): parsed params and it's value.
    """
    def __init__(self, head_type, head_conf_file):
        self.head_type = head_type
        with open(head_conf_file) as f:
            head_conf = yaml.load(f, Loader=yaml.FullLoader)
            self.head_param = head_conf[head_type]
        print('head param:')
        print(self.head_param)
    def get_head(self):
        if self.head_type == 'AdaCos':
            feat_dim = self.head_param['feat_dim'] # dimension of the output features, e.g. 512 
            num_class = self.head_param['num_class'] # number of classes in the training set.
            head = AdaCos(feat_dim, num_class)
        elif self.head_type == 'AdaM-Softmax':
            feat_dim = self.head_param['feat_dim'] # dimension of the output features, e.g. 512 
            num_class = self.head_param['num_class'] # number of classes in training set.
            scale = self.head_param['scale'] # the scaling factor for cosine values.
            lamda = self.head_param['lamda'] # controls the strength of the margin constraint Lm.
            head = Adam_Softmax(feat_dim, num_class, scale, lamda)
        elif self.head_type == 'AM-Softmax':
            feat_dim = self.head_param['feat_dim'] # dimension of the output features, e.g. 512 
            num_class = self.head_param['num_class'] # number of classes in the training set.
            margin = self.head_param['margin'] # cos_theta - margin
            scale = self.head_param['scale'] # the scaling factor for cosine values.
            head = AM_Softmax(feat_dim, num_class, margin, scale)
        elif self.head_type == 'MV-Softmax':
            feat_dim = self.head_param['feat_dim'] # dimension of the output features, e.g. 512 
            num_class = self.head_param['num_class'] # number of classes in the training set.
            is_am = self.head_param['is_am'] # am-softmax for positive samples.
            margin = self.head_param['margin'] # margin for positive samples.
            mv_weight = self.head_param['mv_weight'] # weight for hard negtive samples.
            scale = self.head_param['scale'] # the scaling factor for cosine values.
            head = MV_Softmax(feat_dim, num_class, is_am, margin, mv_weight, scale)
        else:
            pass
        return head
