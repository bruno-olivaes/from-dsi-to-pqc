import os
import subprocess
import sys

base = r"C:\Users\bruno\projects\from-dsi-to-pqc"
ch_dir = os.path.join(base, "chapters")
os.makedirs(ch_dir, exist_ok=True)

# -------------------------------------------------------------
# 1. PREFACE
# -------------------------------------------------------------
preface_content = r"""\chapter*{Preface: The Metrological Journey}
\addcontentsline{toc}{chapter}{Preface: The Metrological Journey}

\begin{flushright}
\textit{``The first principle is that you must not fool yourself --\\
and you are the easiest person to fool.''}\\
--- Richard P. Feynman
\end{flushright}

\vspace{1cm}

\noindent This volume brings together five peer-reviewed and pre-registered scientific investigations conducted throughout 2026. While they span disparate physical disciplines---from precision cosmic microwave background anisotropy and sub-micron nanomechanical force metrology to dynamic dark energy parameterizations, quantum circuit error mitigation, and post-quantum network cryptography---they are bound by a single, uncompromising epistemological principle: \textbf{the primacy of empirical data over mathematical aestheticism}.

\section*{The Origin: The Matrioska Hypothesis}
The trajectory that culminated in this work began with an audacious, speculative inquiry termed the \textit{Matrioska de Ouroboros}. The guiding intuition was that nature might exhibit nested, discrete self-similarity across physical scales---a discrete scale invariance (DSI) that could manifest simultaneously as log-periodic oscillations in cosmological power spectra, modified gravity anomalies at the nanometer scale, and discrete quantum phase signatures.

In theoretical physics, scale invariance is an intoxicating concept. When broken from a continuous symmetry to a discrete subgroup, it predicts characteristic logarithmic oscillatory modulations governed by a preferred scaling factor $\lambda$, producing Fourier-space modulations with angular log-frequency $\omega = 2\pi / \ln\lambda$. Early unconstrained exploratory analysis appeared promising; preliminary regressions on noisy signals revealed apparent peaks and intriguing numerical concordances.

\section*{The Crisis of Rigor and the Anti-Hallucination Audit}
However, science is distinguished from numerology by its willingness to institutionalize doubt. When subjected to mathematical audit, those early exploratory signatures began to crumble under closer scrutiny:
\begin{enumerate}
    \item \textbf{The Look-Elsewhere Effect in Cosmology:} In scanning continuous frequency bands without multiplicity correction, standard statistical thresholds are drastically inflated. What seemed like a $3\sigma$ signal was, in truth, an ordinary sample variance fluctuation ($p_{\text{corrected}} = 0.975$).
    \item \textbf{The Runge Phenomenon in Casimir Metrology:} An apparent oscillatory anomaly at $\lambda = 583.5\text{ nm}$ in nanomechanical force curves was not a new fundamental interaction, but a mathematical phantom manufactured by unphysical high-degree polynomial detrending across an irregular $z^{-4}$ gradient.
    \item \textbf{The Breakdown of Harmonic ZNE in Quantum Circuits:} While harmonic zero-noise extrapolation succeeded brilliantly in mitigating coherent over-rotations in a single qubit (reducing MAE by 85.4\%), it collapsed catastrophically in multi-qubit entangled systems (MAE surging to 2.28) due to multi-mode non-commutative Baker-Campbell-Hausdorff crosstalk.
    \item \textbf{The Real-World Bottleneck of Post-Quantum Cryptography:} While academic debate focused on the computational latency of lattice-based algebra, real-world deployment revealed that ML-KEM key generation takes a mere 41 microseconds, but network transport is bottlenecked by TCP packet fragmentation across standard Ethernet boundaries.
\end{enumerate}

Recognizing these traps did not represent a defeat; it marked the transformation of an exploratory speculation into a mature metrological program. Each failure was traced to its exact mathematical cause, codified into open-source software, verified against blind synthetic mocks, and frozen in pre-registered protocols.

\section*{Structure of this Volume}
This book is structured in five self-contained yet conceptually connected chapters:
\begin{itemize}
    \item \textbf{Chapter 1: Discrete Scale Invariance in Cosmological Spectra.} We detail the pre-registered three-stage search for DSI in the Planck 2018 cosmic microwave background temperature power spectrum, establishing 95\% confidence level upper limits ($\varepsilon < 0.05$) and confirming identical null behavior on synthetic DESI Large-Scale Structure mocks.
    \item \textbf{Chapter 2: Statistical Pitfalls in Casimir Force Spectroscopy.} We systematically dissect how conventional data-processing choices (naive Gaussian thresholds, polynomial detrending, and spline resampling) inadvertently fabricate statistically overwhelming false positive signals in AFM spectroscopy.
    \item \textbf{Chapter 3: Forecasting Log-Oscillatory Dark Energy with ESA Euclid.} We analyze bounded dynamical dark energy models using the full $1580 \times 1580$ Pantheon+ systematic covariance matrix, DESI 2024 BAO, and Planck 2018 CMB priors, presenting forecasts for the ESA Euclid spectroscopic survey to break model degeneracies at $>3\sigma$.
    \item \textbf{Chapter 4: Error Mitigation Benchmarks on NISQ Devices.} We present a head-to-head empirical benchmark comparing standard polynomial, exponential, and harmonic zero-noise extrapolation against Clifford Pauli Twirling across single-qubit and four-qubit Trotter circuits under strictly matched shot budgets.
    \item \textbf{Chapter 5: The Network Cost of Post-Quantum Cryptography.} We quantify the transport-layer impact of NIST FIPS 203 (ML-KEM-768), demonstrating how wire payload expansion breaches the Ethernet Maximum Segment Size (MSS) and induces TCP segmentation in TLS 1.3 handshakes.
    \item \textbf{Appendix: The Certified Three-Stage Protocol.} We provide the complete, unedited Python source code implementing the three-stage radix-agnostic detection, non-linear refinement, and bootstrap certification engine.
\end{itemize}

\vspace{0.8cm}
\noindent\textbf{Bruno Lu\c{c}ardo Olivaes}\\
\textit{Curitiba, Brazil --- November 2026}
"""

with open(os.path.join(ch_dir, "preface.tex"), "w", encoding="utf-8") as f:
    f.write(preface_content)

print("Wrote preface.tex")

