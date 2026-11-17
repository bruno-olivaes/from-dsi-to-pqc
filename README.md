# The Matrioska Protocol: From Primordial Discrete Scale Invariance to Post-Quantum Agility

### *A Metrological Journey through Cosmology, Casimir Physics, Quantum Computing, Colliders, and Post-Quantum Cryptography*

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Zenodo DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.24124702-blue)](https://doi.org/10.5281/zenodo.24124702)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--5351--446X-green.svg)](https://orcid.org/0009-0003-5351-446X)

**Author:** Bruno Luçardo Olivaes  
*Independent Researcher, Brazil*  
**Date:** November 2026 | **Edition:** 1st Edition | **Pages:** 45

---

## 📖 Executive Abstract

This monograph brings together seven pre-registered scientific investigations conducted in 2026 across 45 orders of physical magnitude—spanning observational cosmology, nanomechanical force metrology, dynamical dark energy, quantum error mitigation, post-quantum network cryptography, and high-energy collider physics. Originating from an exploratory inquiry into Discrete Scale Invariance (DSI)—the "Matrioska Hypothesis"—this work documents how rigorous mathematical auditing and anti-hallucination protocols transformed speculative signal searches into a unified, reproducible metrological program.

Key empirical findings and methodological contributions across the seven chapters include:

1. **Constraints on Primordial Discrete Scale Invariance (Planck 2018 & DESI Mocks):** Using a certified three-stage radix-agnostic pipeline (Generalized Lomb-Scargle detection, non-linear parametric refinement, and bootstrap-of-maximum phase-scrambled certification) governed by five mandatory integrity gates on the official Planck `BestFit` $\Lambda$CDM spectrum, we find no evidence for DSI in Planck 2018 PR3 TT ($p_{\mathrm{corrected}} = 0.998$, $\Delta\mathrm{BIC} = -49.80$ for candidate $\hat\lambda = 1.2938 \pm 0.0072$) or synthetic DESI DR2 mocks ($p_{\mathrm{corrected}} = 0.314$, $\Delta\mathrm{BIC} = +8.80$), establishing 95% CL upper limits of $\epsilon < 0.05$ across $\lambda \in [1.1, 148]$.
2. **Statistical Pitfalls in Casimir Force Spectroscopy:** Auditing sub-micron Au-Cu MTO and KPFM datasets, we demonstrate that cubic polynomial detrending across steep $z^{-4}$ gradients fabricates Runge ringing oscillations ($\lambda = 583.5\,\text{nm}$, artificial $\mathrm{FAP} = 1.49 \times 10^{-45}$), while cubic spline resampling on irregular grids ($\mathrm{CV} = 40.7\%$) attenuates 22.6% of true signal variance at $\lambda = 7.5\,\text{nm}$ ($2.27\times$ $\mathrm{MDL}_{90}$ degradation). Adopting a physical inverse-power basis $\{1, z^{-4}, z^{-5}\}$—backed by an explicit first-order Taylor proof that contact-point drift $\delta z_0$ generates $-4 C_4 \delta z_0 z^{-5}$—collapses residual variance ($\chi^2/\mathrm{dof} = 1.14$) and restores the experimental null result (Baluev $\mathrm{FAP} = 0.163$), while Speake-Trenner integration of 2D KPFM patch potentials proves strictly monotonic decay ($P_{\mathrm{patch}} \propto d^{-2.29}$).
3. **Forecasting Log-Oscillatory Dark Energy with ESA Euclid:** We derive an exact closed-form relativistic energy density solution for bounded log-oscillatory dark energy, $w(a) = -1 + A \sin((2\pi/\lambda)\ln a + \phi_0)$. Joint likelihood analysis using the full $1580 \times 1580$ Pantheon+ systematic covariance matrix, DESI Year 1 BAO, and Planck 2018 CMB priors reveals a mild preference over flat $\Lambda\mathrm{CDM}$ ($\Delta \chi^2 = -3.90$ vs. $-3.75$ for CPL) with overlapping $1\sigma$ bands across $z \le 2.33$. A 7-bin Stage-IV ESA Euclid $H(z)$ Fisher matrix ($\sigma_H/H = 1.3\%$) shows that Euclid alone separates best-fit CPL and Log-Oscillatory by only $0.18\sigma$ ($\Delta\chi^2 = 0.031$), while mapping the exact $A_{3\sigma}(\lambda)$ discovery boundary ($A_{3\sigma} = 0.231$ phase-median at $\lambda = 3.09$).
4. **Quantum Error Mitigation Benchmarks on NISQ Devices:** In high-fidelity Qiskit 2.x (`AerSimulator`) emulations calibrated with heavy-hex superconducting transmon noise models under strictly matched shot budgets (24,000 shots/seed), we benchmark Damped Harmonic / Lomb-Scargle Zero-Noise Extrapolation (ZNE) against two-qubit Clifford Pauli Twirling. While Harmonic ZNE reduces Mean Absolute Error (MAE) by 85.4% in 1-qubit coherent Ramsey sequences ($z = +22.1\,\mathrm{SE}$), it fails catastrophically in 4-qubit entangled TFIM Trotter circuits (MAE surging to 2.28 at $\epsilon = 0.04\,\text{rad}$) due to non-commutative Baker-Campbell-Hausdorff crosstalk and short-schedule ill-conditioning. Conversely, Pauli Twirling + Linear/Exponential ZNE restores monotonic decay and achieves 80.8%–81.0% error reduction.
5. **The Network Cost of Post-Quantum Cryptography (TLS 1.3 Wire Cost):** Empirical C-extension benchmarks of NIST FIPS 203 (ML-KEM-768) show that lattice key generation executes in $41.3\,\mu\text{s}$—738x faster than RSA-2048 ($30.49\,\text{ms}$). Using deterministic socket transport auditing and exact $1{,}500\,$B MTU framing, we show hybrid key exchange (X25519 + ML-KEM-768) expands the KEM wire footprint to 2,402 B and pushes the RFC 8446 ClientHello flight to 1,518 B, breaching the 1,460 B Ethernet TCP Maximum Segment Size (MSS) and forcing multi-packet fragmentation.
6. **Discrete Scale Invariance Search in LHC Open Data:** Applying the five-gate protocol to $62,214$ physical CMS $\sqrt{s} = 7\,\mathrm{TeV}$ opposite-sign dimuon events confirms certified null results across both mass windows (Gate 2 residual RMS test, Gate 4 look-elsewhere $p_{\mathrm{corrected}}$, and Gate 5 $\Delta\mathrm{BIC}$).
7. **Breaking the Binning Barrier at the LHC (Unbinned Quadrature + NSBI):** Formulating a composite $4 \times 64$-node Gauss-Legendre unbinned profile likelihood over $N = 17,458$ Clean Drell-Yan events ($11 \le m \le 75\,\mathrm{GeV}$, calibrated at $\sigma_u^{\mathrm{barrel}} = 0.0120$) recovers **$29.1\times$** 95% CL sensitivity over 20-bin Poisson likelihoods at $\lambda = 1.10$ ($\varepsilon_{95}^{\mathrm{unb}} = 0.0337$ vs. $0.9800$) and **$5.70\times$** over 40-bin likelihoods, independently confirmed via a PyTorch `ConditionalDensityMLP` NSBI surrogate ($\varepsilon_{95}^{\mathrm{neural}} = 0.0324$, $p_{\mathrm{corr}} = 0.4500$, $\Delta\mathrm{BIC} = -18.15$).

The volume concludes with the complete, unedited Python implementation of the certified three-stage radix-agnostic detection and bootstrap certification engine.

---

## 🏛️ Sovereign DOIs & Graph Architecture (DataCite `HasPart`)

The monograph acts as the parent work (`IsPartOf` / `HasPart` graph) binding the seven pre-registered investigations:

| Chapter | Discipline / Topic | Sovereign DOI | DataCite Relation | Open Access PDF |
|:-------:|:-------------------|:-------------:|:-----------------:|:---------------:|
| **Ch. 1** | Primordial DSI (Planck 2018) | [`10.5281/zenodo.24121677`](https://doi.org/10.5281/zenodo.24121677) | `HasPart` | [Zenodo #24121677](https://zenodo.org/records/24121677) |
| **Ch. 2** | Casimir Force Metrology (AFM) | [`10.5281/zenodo.24121687`](https://doi.org/10.5281/zenodo.24121687) | `HasPart` | [Zenodo #24121687](https://zenodo.org/records/24121687) |
| **Ch. 3** | Dark Energy Forecast (ESA Euclid) | [`10.5281/zenodo.24121691`](https://doi.org/10.5281/zenodo.24121691) | `HasPart` | [Zenodo #24121691](https://zenodo.org/records/24121691) |
| **Ch. 4** | NISQ Quantum Error Mitigation (ZNE) | [`10.5281/zenodo.24121693`](https://doi.org/10.5281/zenodo.24121693) | `HasPart` | [Zenodo #24121693](https://zenodo.org/records/24121693) |
| **Ch. 5** | Post-Quantum TLS 1.3 Wire Cost | [`10.5281/zenodo.24121695`](https://doi.org/10.5281/zenodo.24121695) | `HasPart` | [Zenodo #24121695](https://zenodo.org/records/24121695) |
| **Ch. 6** | LHC Dimuon DSI Search (CMS) | [`10.5281/zenodo.24149840`](https://doi.org/10.5281/zenodo.24149840) | `HasPart` | [Zenodo #24149840](https://zenodo.org/records/24149840) |
| **Ch. 7** | LHC Unbinned Likelihood & NSBI | [`10.5281/zenodo.24149842`](https://doi.org/10.5281/zenodo.24149842) | `HasPart` | [Zenodo #24149842](https://zenodo.org/records/24149842) |

---

## 📂 Repository Structure

```text
from-dsi-to-pqc/
├── book.pdf                  # Compiled 45-page Master Monograph
├── book.tex                  # Main LaTeX master source file
├── refs.bib                  # Unified master bibliography
├── chapters/                 # Monograph chapters (LaTeX)
│   ├── preface.tex           # Methodological preface: The Matrioska Protocol
│   ├── ch1_planck_dsi.tex    # Chapter 1: Planck 2018 DSI null constraint
│   ├── ch2_casimir_afm.tex   # Chapter 2: Casimir force spectroscopy traps
│   ├── ch3_euclid_dark_energy.tex # Chapter 3: ESA Euclid dark energy Fisher forecast
│   ├── ch4_qiskit_zne.tex    # Chapter 4: NISQ ZNE & Pauli twirling benchmark
│   ├── ch5_pqc_network_cost.tex   # Chapter 5: PQC TLS 1.3 wire footprint
│   ├── ch6_lhc_dsi.tex            # Chapter 6: LHC Run 2010B dimuon DSI search
│   ├── ch7_lhc_unbinned_likelihood.tex # Chapter 7: Unbinned composite quadrature & NSBI
│   └── appendix_protocol_code.tex # Certified 5-gate protocol implementation
├── figures/                  # Publication-ready vector and raster figures
│   ├── fig1_fake_oscillation.pdf
│   ├── fig2_spline_attenuation.pdf
│   ├── fig3_kpfm_monotonic.pdf
│   ├── fig_euclid_hubble_forecast.png
│   ├── fig_fair_zne_comparison.png
│   └── fig_pqc_crypto_agility.png
├── scripts/
│   └── check_impact.py       # Live Zenodo REST API views & downloads tracker
└── README.md                 # Executive monograph summary
```

---

## 🛠️ Compilation & Verification

### Build from Source
```bash
pdflatex -interaction=nonstopmode book.tex
bibtex book
pdflatex -interaction=nonstopmode book.tex
pdflatex -interaction=nonstopmode book.tex
```

### Live Impact Monitor
To query Zenodo's DataCite metrics across all DOIs in real-time:
```bash
python scripts/check_impact.py
```

---

## 📜 Citation (BibTeX)

```bibtex
@book{olivaes2026matrioska,
  author    = {Olivaes, Bruno Lu{\c{c}}ardo},
  title     = {The Matrioska Protocol: From Primordial Discrete Scale Invariance to Post-Quantum Agility},
  subtitle  = {A Metrological Journey through Cosmology, Casimir Physics, Quantum Computing, Colliders, and Post-Quantum Cryptography},
  edition   = {1},
  year      = {2026},
  month     = nov,
  publisher = {Zenodo},
  note      = {ORCID: 0009-0003-5351-446X. Licensed under CC BY 4.0},
  doi       = {10.5281/zenodo.24124702},
  url       = {https://doi.org/10.5281/zenodo.24124702}
}
```

