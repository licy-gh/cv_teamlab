"""
@author: Haoran Jiang, Jun Wang
@date: 20201013
@contact: jun21wangustc@gmail.com
"""

import os
import sys
import numpy as np


class LFWEvaluator(object):
    """Implementation of LFW test protocal.
    
    Attributes:
        data_loader(object): a test data loader.
        pair_list(list): the pair list given by PairsParser.
        feature_extractor(object): a feature extractor.
    """

    def __init__(self, data_loader, feature_extractor):
        """Init LFWEvaluator.

        Args:
            data_loader(object): a test data loader. 
            pairs_parser_factory(object): factory to produce the parser to parse test pairs list.
            pair_list(list): the pair list given by PairsParser.
            feature_extractor(object): a feature extractor.
        """
        self.data_loader = data_loader
        self.feature_extractor = feature_extractor

    def test(self, model):
        image_name2feature = self.feature_extractor.extract_online(model, self.data_loader)
        # mean, std = self.test_one_model(self.pair_list, image_name2feature)
        acc, prec, recall = self.test_one_model(image_name2feature)
        return acc, prec, recall

    def test_one_model(self, image_name2feature, is_normalize=True):
        """Get the accuracy of a model.
        
        Args:
            test_pair_list(list): the pair list given by PairsParser. 
            image_name2feature(dict): the map of image name and it's feature.
            is_normalize(bool): wether the feature is normalized.

        Returns:
            mean: estimated mean accuracy.
            std: standard error of the mean.
        """

        tp = tn = fp = fn = 0
        for name, feature in image_name2feature.items():
            masked = 1 if name[name.rfind('.') - 1] == 'm' else 0
            # exp = np.exp(feature)
            # feature = exp / np.sum(exp)
            pred = np.argmax(feature)
            if masked == 1:
                if pred == 1:
                    tp += 1
                else:
                    fn += 1
            else:
                if pred == 1:
                    fp += 1
                else:
                    tn += 1
        
        accuracy = (tp + tn) / (tp + tn + fp + fn)
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        return accuracy, precision, recall

    def getThreshold(self, score_list, label_list, num_thresholds=1000):
        """Get the best threshold by train_score_list and train_label_list.
        Args:
            score_list(ndarray): the score list of all pairs.
            label_list(ndarray): the label list of all pairs.
            num_thresholds(int): the number of threshold that used to compute roc.
        Returns:
            best_thres(float): the best threshold that computed by train set.
        """
        pos_score_list = score_list[label_list == 1]
        neg_score_list = score_list[label_list == 0]
        pos_pair_nums = pos_score_list.size
        neg_pair_nums = neg_score_list.size
        score_max = np.max(score_list)
        score_min = np.min(score_list)
        score_span = score_max - score_min
        step = score_span / num_thresholds
        threshold_list = score_min + step * np.array(range(1, num_thresholds + 1))
        fpr_list = []
        tpr_list = []
        for threshold in threshold_list:
            fpr = np.sum(neg_score_list > threshold) / neg_pair_nums
            tpr = np.sum(pos_score_list > threshold) / pos_pair_nums
            fpr_list.append(fpr)
            tpr_list.append(tpr)
        fpr = np.array(fpr_list)
        tpr = np.array(tpr_list)
        best_index = np.argmax(tpr - fpr)
        best_thres = threshold_list[best_index]
        return best_thres
