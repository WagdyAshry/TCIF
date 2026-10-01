# TCIF v18 — Transformer-based Cost Intelligence Framework

**A Proposed Framework for Near-Real-Time Cost Intelligence and Strategic Decision Support in Enterprise Information Systems: A Transformer-Based Approach**

---

## Overview

TCIF (Transformer-based Cost Intelligence Framework) is a four-layer architecture that integrates ERP-native data ingestion, fiscal-context-aware temporal attention, multi-horizon probabilistic forecasting, and a decision support layer producing severity-weighted recommendations.

This repository contains the **v18 frozen release** — the empirically validated version reported in the accompanying paper (submitted to IJISPM).

## Architecture

Four sequential layers:
1. **L1 — FiscalAware Encoding**: combines 12 ERP features + 3 fiscal metadata into 256-dim embeddings.
2. **L2 — Temporal Multi-Head Self-Attention**: 4 Transformer blocks, 8 heads each.
3. **L3 — Multi-Horizon Prediction**: 6-layer encoder + 2-layer decoder, forecasts at 7/30/90 days with P10/P50/P90 quantiles.
4. **L4 — Decision Support**: cosine-similarity classification over 6 severity-weighted decision categories (DAS).

## Key Results (Test Set, 5 Seeds)

| Metric | Value |
|---|---|
| **RMSE (all horizons)** | **0.0935 ± 0.0011** |
| **DAS macro F1** | **0.3629 ± 0.0071** |
| **Severity-weighted F1** | **0.3134 ± 0.0080** |
| **Severe-class recall** | **0.3441 ± 0.0256** |
| **Coverage (P10/P50/P90)** | 0.11 / 0.51 / 0.89 |

### Baseline Comparison

| Model | Avg RMSE | DAS | Training Time |
|---|---|---|---|
| XGBoost | **0.0884** | No | ~13 min |
| **TCIF v18** | **0.0935 ± 0.0011** | **Yes** | **~7 min** |
| LSTM | 0.1123 | No | ~6 min |

TCIF outperforms LSTM by **20.3%**, remains within **5.4%** of XGBoost, and provides the DAS capability that no forecasting-only baseline can produce.

## Repository Structure

```
tcif-v18/
├── code/                     # Model + training code
├── data/                     # Simulation config + class distribution
├── results/                  # Per-seed metrics + aggregated summary
├── figures/                  # Architecture diagram
└── docs/                     # Empirical validation section
```

## Reproducing Results

### Data Generation

See `code/generate_data.py` for full generation pipeline. Generates 53,360 windows from 23 cost centres over 2,500 days.

### Training (5 seeds)

See `code/run_5_seeds.py` for full pipeline. Training time: ~35 minutes on Tesla T4.

### Requirements

```bash
pip install -r requirements.txt
```

## Dataset

The dataset is a **synthetic ERP environment** calibrated against documented commodity, demand, and labour shock statistics. It spans:

- **23 cost centres** (2 plants, 3 production lines, plus shared services)
- **2,500 daily timesteps** (~10 fiscal years)
- **12 ERP features** per cost centre per day
- **6 decision categories** with severity-weighted labels

Raw data files (~50 MB) are **not included** in this repository due to GitHub's file size limits. To reproduce the dataset, run the generation script.

## Citation

If you use this code or dataset, please cite:

```bibtex
@article{tcif2026,
  title={A Proposed Framework for Near-Real-Time Cost Intelligence and Strategic Decision Support in Enterprise Information Systems: A Transformer-Based Approach},
  author={[Your Name]},
  journal={International Journal of Information Systems and Project Management},
  year={2026},
  note={Under review}
}
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

**Version**: v18 (frozen)  
**Last updated**: 2026