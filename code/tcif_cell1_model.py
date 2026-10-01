"""
TCIF Model + Loss Functions (Cell 1/3, v18 FINAL)
==================================================
FROZEN VERSION — v18
"""

import math
from typing import Dict, Tuple, Optional, List

import torch
import torch.nn as nn
import torch.nn.functional as F


class TCIFConfig:
    def __init__(
        self,
        n_features: int = 12,
        lookback: int = 90,
        n_fiscal_weeks: int = 13,
        n_fiscal_months: int = 12,
        fiscal_emb_dim: int = 16,
        close_emb_dim: int = 8,
        d_model: int = 128,
        n_heads: int = 4,
        d_head: int = 32,
        n_l2_blocks: int = 2,
        n_l3_encoder_layers: int = 3,
        n_l3_decoder_layers: int = 1,
        horizons: Tuple[int, ...] = (7, 30, 90),
        n_quantiles: int = 3,
        n_decision_categories: int = 6,
        das_dim: int = 64,
        dropout: float = 0.2,
    ):
        assert n_heads * d_head == d_model
        self.n_features = n_features
        self.lookback = lookback
        self.n_fiscal_weeks = n_fiscal_weeks
        self.n_fiscal_months = n_fiscal_months
        self.fiscal_emb_dim = fiscal_emb_dim
        self.close_emb_dim = close_emb_dim
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_head = d_head
        self.n_l2_blocks = n_l2_blocks
        self.n_l3_encoder_layers = n_l3_encoder_layers
        self.n_l3_decoder_layers = n_l3_decoder_layers
        self.horizons = horizons
        self.n_horizons = len(horizons)
        self.n_quantiles = n_quantiles
        self.n_decision_categories = n_decision_categories
        self.das_dim = das_dim
        self.dropout = dropout

    @property
    def fiscal_emb_total(self) -> int:
        return self.fiscal_emb_dim * 2 + self.close_emb_dim


# NOTE: The full implementation (FiscalAwareEncoding, TemporalEncoder, 
# MultiHorizonPrediction, DecisionSupportLayer, TCIF, QuantileLoss, 
# FocalDASLoss, TCIFLoss, make_severity_weights, das_metrics, 
# per_class_metrics, quantile_coverage) is available in the Colab notebook 
# and mirrored in the accompanying Jupyter notebook file.
