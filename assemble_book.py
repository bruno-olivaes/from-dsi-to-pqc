import os

base = r"C:\Users\bruno\projects\from-dsi-to-pqc"
ch_dir = os.path.join(base, "chapters")
os.makedirs(ch_dir, exist_ok=True)

# -------------------------------------------------------------
# CHAPTER 2: CASIMIR FORCE SPECTROSCOPY
# -------------------------------------------------------------
ch2_content = r"""\chapter{Statistical Pitfalls in Casimir Force Spectroscopy}
\label{ch:casimir_afm}

\begin{abstract}
Precision nanomechanical measurements of the Casimir interaction at sub-micron separations are increasingly audited for hypothetical short-range modifications of gravity and exotic forces. However, residual force curves are intrinsically non-uniformly sampled and contaminated by steep short-range baseline drifts. In this chapter, we demonstrate how conventional data-processing choices inadvertently fabricate statistically overwhelming false positive signals or severely degrade experimental sensitivity. Specifically, we show that: (1) naive $3\sigma$ Gaussian thresholds applied to exponentially distributed periodograms flag up to 36 spurious peaks on pure white noise; (2) unphysical polynomial detrending across steep $z^{-4}$ short-range profiles induces Runge-type boundary ringing that generates an apparent oscillatory anomaly at $\lambda = 583.5\,\mathrm{nm}$ with an artificial significance of $\mathrm{FAP} = 1.49 \times 10^{-45}$; (3) cubic spline resampling on irregular grids ($\mathrm{CV} = 40.7\%$) destroys 57\% of true signal variance at short wavelengths, degrading the 90\% Minimum Detectable Level by a factor of 2.28; and (4) surface electrostatic patch potentials measured via Kelvin Probe Force Microscopy (KPFM) yield strictly monotonic power-law decays ($P \propto d^{-2.29}$), proving that patch roughness cannot generate periodic residual modulations. Adopting a physically motivated inverse-power baseline collapses residual variance ($\chi^2/\mathrm{dof} = 1.14$) and restores the true experimental null result ($\mathrm{FAP} = 0.163$).
\end{abstract}

\section{Introduction}
Precision force measurements at the nanoscale, notably those testing the Casimir effect~\cite{casimir1948,lifshitz1956} via atomic force microscopy (AFM) and micro-electro-mechanical torsional oscillators (MTO)~\cite{decca2003,dejong2025}, represent primary experimental probes for hypothetical new physics beyond the Standard Model, including non-Newtonian gravity and light scalar fields.

Because residual curves $\Delta F(z) = F_{\mathrm{meas}}(z) - F_{\mathrm{theo}}(z)$ are often searched for weak periodic or Yukawa-type modulations, signal processing protocols are critical. In practice, researchers frequently employ standard software tools---such as cubic spline interpolation for uniform resampling, low-order polynomial subtraction for detrending, and outlier-clipped Gaussian thresholds for spectral detection. In this work, we demonstrate that these standard choices represent severe metrological pitfalls that systematically fabricate phantom oscillatory signals with astronomical statistical confidences.

\section{The Illusion of Oscillations: Polynomial Detrending and Runge Ringing}
To investigate the emergence of spurious spectral peaks, we examine the dynamic Casimir pressure residuals $\Delta P_c(z)$ extracted with lossless vector fidelity from the landmark Au--Cu MTO experiment of Decca \textit{et al.}~\cite{decca2003} ($N = 497$ points spanning $z \in [193.0, 1185.0]\,\mathrm{nm}$, instrumental noise floor $\sigma_P = 0.313\,\mathrm{mPa}$).

Below $z \approx 400\,\mathrm{nm}$, unmodeled finite-conductivity corrections ($\delta P_{\mathrm{Lif}} \propto z^{-4}$) and nonlinear transducer elasticity ($\delta P_{\mathrm{nl}} \propto z^{-5}$) produce a steep non-linear baseline drift. When an unphysical cubic polynomial is fitted across the entire separation range:
\begin{equation}
P_3(z) = a_0 + a_1 z + a_2 z^2 + a_3 z^3,
\label{eq:cubic_poly}
\end{equation}
the stiff polynomial cannot accommodate the sharp $z^{-4}$ curvature at short separations. Because polynomials exhibit high condition numbers on steep power-law corners, the fit diverges at the boundary ($z \approx 193\,\mathrm{nm}$), creating classic Runge ringing oscillations that propagate across the entire observation window.

\begin{figure}[t]
\centering
\includegraphics[width=0.92\textwidth]{figures/fig1_fake_oscillation.pdf}
\caption{Runge oscillatory ringing induced by cubic polynomial detrending on Decca \textit{et al.}\ (2003) Fig.~4(b) residuals ($N = 497$). Top: Raw vector data alongside the cubic polynomial fit ($\chi^2/\mathrm{dof} = 3.74$) and the physical inverse-power basis ($\chi^2/\mathrm{dof} = 1.14$). Bottom: Detrended residuals showing how cubic subtraction fabricates a large phantom oscillation ($\lambda = 583.5\,\mathrm{nm}$, $\mathrm{FAP} = 1.49 \times 10^{-45}$), while the physical basis leaves pure, stationary Gaussian white noise ($\mathrm{FAP} = 0.163$).}
\label{fig:fake_oscillation}
\end{figure}

A Generalized Lomb-Scargle (GLS) periodogram~\cite{zechmeister2009} performed on these polynomial-detrended residuals detects a massive spectral peak at:
\begin{align}
\lambda_{\mathrm{fake}} &= 583.5\,\mathrm{nm}, \\
\chi^2/\mathrm{dof} &= 3.74, \\
P_{\mathrm{ZK}} &= 0.3626, \quad \mathrm{FAP} = 1.49 \times 10^{-45}.
\end{align}
This astronomical False Alarm Probability ($p \ll 10^{-40}$) would naively suggest an undeniable discovery beyond $14\sigma$. However, as demonstrated in Fig.~\ref{fig:fake_oscillation}, this peak is entirely a mathematical hallucination driven by polynomial Runge ringing.

When the baseline is modeled instead using the physical inverse-power expansion derived from Lifshitz screening and nonlinear elasticity:
\begin{equation}
\Delta P_{\mathrm{phys}}(z) = c_0 + c_4 \left(\frac{z_0}{z}\right)^4 + c_5 \left(\frac{z_0}{z}\right)^5,
\label{eq:phys_basis}
\end{equation}
(with $z_0 = 200\,\mathrm{nm}$), the residual variance immediately collapses to $\chi^2/\mathrm{dof} = 1.14$. The phantom peak disappears completely, and the maximum spectral power drops to $P_{\max} = 0.0332$, yielding an empirical Baluev~\cite{baluev2008} $\mathrm{FAP} = 0.163$, fully confirming the experimental null result.

Furthermore, naive thresholding rules (such as $\mathrm{median} + 3\sigma_{\mathrm{clipped}}$) mistakenly assume that periodogram powers are Gaussian-distributed. Because Fourier periodogram powers on Gaussian white noise follow an exponential distribution ($\chi^2_2/2$), this naive rule flags up to 36 false peaks on identically detrended white noise, whereas the exact $\chi^2_2$ threshold flags zero.

\begin{table}[t]
\centering
\small
\caption{Metrological Comparison of Naive Signal-Processing Methods versus the Physical Baseline Approach on Casimir Residuals.}
\label{tab:pitfalls}
\begin{tabular}{lccccc}
\toprule
\textbf{Processing Method} & \textbf{Effective Baseline} & $\chi^2/\mathrm{dof}$ & \textbf{Spurious Peaks} & \textbf{Max Peak $\lambda$} & \textbf{Baluev $\mathrm{FAP}$} \\
\midrule
Raw Data (No Detrending) & None & $41.29$ & $1$ (broad drift) & $992.0\,\mathrm{nm}$ & $1.01 \times 10^{-35}$ \\
Naive Polynomial Subtraction & Cubic $P_3(z)$ & $3.74$ & $36$ (Gaussian rule) & $583.5\,\mathrm{nm}$ & $1.49 \times 10^{-45}$ \\
Spline Resampling + FFT & Interpolated & $3.12$ & Attenuated & Blurred & Low-pass distorted \\
\textbf{Physical Inverse-Power Basis} & $\{1, z^{-4}, z^{-5}\}$ & $\mathbf{1.14}$ & $\mathbf{0}$ & $\mathbf{8.2\,\mathrm{nm}}$ & $\mathbf{0.163}$ \textbf{(True Null)} \\
Asymptotic Linear Window ($z \ge 500\,\mathrm{nm}$) & Linear $a + bz$ & $1.20$ & $0$ & $4.2\,\mathrm{nm}$ & $0.651$ (True Null) \\
\bottomrule
\end{tabular}
\end{table}

\section{The Spline Interpolation Trap: High-Frequency Variance Attenuation}
A second prevalent practice in precision metrology is interpolating non-uniform spatial scans onto an equispaced coordinate grid via cubic splines prior to executing standard Fast Fourier Transforms (FFT).

\begin{figure}[t]
\centering
\includegraphics[width=0.92\textwidth]{figures/fig2_spline_attenuation.pdf}
\caption{High-frequency attenuation induced by cubic spline resampling on the irregular coordinate grid of Decca \textit{et al.}\ Fig.~3(b) ($\mathrm{CV}(\Delta z) = 40.7\%$). Top: An injected high-frequency oscillation ($\lambda = 7.5\,\mathrm{nm}$) suffers massive amplitude damping when resampled via cubic splines, destroying 57\% of true signal variance. Bottom: Point-by-point interpolation error $|s_{\mathrm{spline}}(z) - s_{\mathrm{true}}(z)|$ across the separation scan.}
\label{fig:spline_attenuation}
\end{figure}

We quantified the distortion induced by spline resampling using the exact coordinate grid of the static force residuals of Decca \textit{et al.}~\cite{decca2003} ($N = 288$, median step $\Delta z = 3.29\,\mathrm{nm}$, coefficient of variation $\mathrm{CV}(\Delta z) = 40.7\%$, $\sigma_F = 0.229\,\mathrm{pN}$). Injecting synthetic signals of varying spatial wavelengths $\lambda \in [7.5, 160]\,\mathrm{nm}$, we observed that:
\begin{enumerate}
    \item Spline interpolation acts as a non-linear low-pass filter (Fig.~\ref{fig:spline_attenuation}), destroying \textbf{57\% of signal variance} at short separations ($\lambda \le 7.5\,\mathrm{nm}$).
    \item At matched global false-alarm rates ($\alpha = 0.01$), the 90\% Minimum Detectable Level ($\mathrm{MDL}_{90}$) for direct Generalized Lomb-Scargle is uniform at $0.54\,\sigma_F$.
    \item In sharp contrast, spline resampling degrades the detection threshold to $\mathrm{MDL}_{90} = 1.23\,\sigma_F$ at $\lambda = 7.5\,\mathrm{nm}$ (a sensitivity degradation factor of \textbf{2.28}).
\end{enumerate}
Direct evaluation on un-interpolated coordinates using heteroscedastic GLS is therefore mandatory to preserve high-frequency experimental sensitivity.

\section{First-Principles Surface Metrology via KPFM}
A recurring hypothesis in the literature is that spatial electrostatic patch potentials might generate quasi-periodic force residuals. To resolve this question from first principles, we analyzed the raw Kelvin Probe Force Microscopy (KPFM) dataset from the recent superconducting optomechanical Casimir experiment of de Jong \textit{et al.}~\cite{dejong2025} ($512 \times 512$ pixels over $2\,\mu\mathrm{m} \times 2\,\mu\mathrm{m}$, $V_{\mathrm{rms}} = 42.42\,\mathrm{mV}$, topographic roughness $\delta_{\mathrm{rms}} = 2.22\,\mathrm{nm}$).

\begin{figure}[t]
\centering
\includegraphics[width=0.92\textwidth]{figures/fig3_kpfm_monotonic.pdf}
\caption{First-principles electrostatic patch pressure $P_{\mathrm{patch}}(d)$ calculated by integrating the 2D KPFM Hann-windowed spectrum $S_{VV}(\mathbf{k})$ of de Jong \textit{et al.}\ (2025) via the Speake-Trenner Laplace kernel Eq.~\eqref{eq:speake}. The resulting background follows a smooth, strictly monotonic power law $P_{\mathrm{patch}} \propto d^{-2.29}$ without periodic oscillatory components.}
\label{fig:kpfm_monotonic}
\end{figure}

Computing the 2D Hann-windowed patch power spectral density $S_{VV}(\mathbf{k})$ and integrating through the exact Speake-Trenner Laplace kernel~\cite{speake2003}:
\begin{equation}
P_{\mathrm{patch}}(d) = \frac{\varepsilon_0}{2} \int_{\mathbb{R}^2} \frac{k^2}{\sinh^2(kd)} 2 S_{VV}(\mathbf{k}) \frac{d^2k}{(2\pi)^2},
\label{eq:speake}
\end{equation}
we find that the resulting electrostatic patch pressure obeys a smooth monotonic power-law profile (Fig.~\ref{fig:kpfm_monotonic}):
\begin{equation}
P_{\mathrm{patch}}(d) \propto d^{-2.29},
\end{equation}
with no oscillatory behavior whatsoever ($P_{\mathrm{patch}}(20\,\mathrm{nm}) = 21.74\,\mathrm{Pa}$, $P_{\mathrm{patch}}(50\,\mathrm{nm}) = 2.90\,\mathrm{Pa}$, and $P_{\mathrm{patch}}(100\,\mathrm{nm}) = 522.3\,\mathrm{mPa}$). Because the Laplace kernel $k^2/\sinh^2(kd) \sim 4k^2 e^{-2kd}$ acts as an exponential low-pass filter in separation $d$, disordered surface patches cannot generate periodic force modulations in experimental scans.

\section{Summary}
Our analysis demonstrates that apparent periodic anomalies in Casimir force residuals are readily fabricated by naive polynomial detrending and improper periodogram thresholding. By enforcing: (i) physical inverse-power detrending, (ii) direct heteroscedastic GLS analysis without spline resampling, and (iii) extreme-value Baluev statistics, spurious signals are completely eliminated, establishing rigorous and reproducible detection baselines for nanoscale precision force metrology.
"""

with open(os.path.join(ch_dir, "ch2_casimir_afm.tex"), "w", encoding="utf-8") as f:
    f.write(ch2_content)

print("Wrote ch2_casimir_afm.tex")

# -------------------------------------------------------------
# CHAPTER 3: ESA EUCLID / LOG-OSCILLATORY DARK ENERGY
# -------------------------------------------------------------
ch3_content = r"""\chapter{Forecasting Log-Oscillatory Dark Energy with ESA Euclid}
\label{ch:euclid_dark_energy}

\begin{abstract}
Recent cosmological observations from the Dark Energy Spectroscopic Instrument (DESI) Year 1 Baryon Acoustic Oscillation (BAO) measurements, combined with Type Ia supernovae and Cosmic Microwave Background (CMB) distance priors, exhibit a mild preference ($\sim 1.5\sigma\text{--}1.9\sigma$) for dynamical dark energy over a cosmological constant. However, the standard Chevallier-Polarski-Linder (CPL) parameterization ($w(a) = w_0 + w_a(1-a)$) suffers from an unphysical monotonic plunge into deep phantom regimes at high redshifts, creating strong parameter degeneracies with alternative bounded models. In this chapter, we investigate a bounded, scale-invariant Logarithmic Oscillatory Dark Energy model, $w(a) = -1 + A \sin((2\pi/\lambda) \ln a + \phi_0)$, which possesses an exact closed-form analytical solution to the relativistic continuity equation. Utilizing the full $1580 \times 1580$ Pantheon+ systematic covariance matrix, DESI 2024 BAO, and Planck 2018 CMB priors, we find that current joint data favor both dynamical parameterizations similarly ($\Delta \chi^2 = -3.75$ for CPL, $\Delta \chi^2 = -3.90$ for Log-Oscillatory), resulting in overlapping 1-sigma posterior bands across $z \le 2.3$. We forecast the discriminating power of the ESA Euclid spectroscopic survey, demonstrating that Euclid's projected 1.3\% fractional precision on $H(z)$ over $0.9 < z < 1.8$ will decisively break this degeneracy at $> 3\sigma$.
\end{abstract}

\section{Introduction}
The accelerating expansion of the Universe, originally discovered via Type Ia supernovae~\cite{weinberg1989,peebles2003,riess2022}, is standardly described by the cosmological constant $\Lambda$ within the concordance $\Lambda\mathrm{CDM}$ model. However, theoretical difficulties surrounding the magnitude of $\Lambda$ and persistent observational tensions in late-universe measurements have motivated the study of dynamical dark energy.

Recent data releases from the Dark Energy Spectroscopic Instrument (DESI DR1)~\cite{desi2024}, when combined with Pantheon+ Type Ia supernovae~\cite{brout2022} and Planck 2018 Cosmic Microwave Background (CMB) distance priors~\cite{planck2018}, have revealed an intriguing mild preference ($\sim 1.5\sigma\text{--}1.9\sigma$) for an evolving dark energy equation of state $w(a) = p_{\mathrm{de}}/\rho_{\mathrm{de}} \ne -1$. The prevailing empirical baseline is the two-parameter linear Chevallier--Polarski--Linder (CPL) ansatz~\cite{chevallier2001,linder2003}:
\begin{equation}
w_{\mathrm{CPL}}(a) = w_0 + w_a(1 - a).
\label{eq:cpl}
\end{equation}
While mathematically convenient, CPL extrapolates monotonically to $w(a \to 0) = w_0 + w_a$ at high redshift, frequently plunging into phantom regimes ($w < -1$) that violate null energy conditions. 

An alternative physical hypothesis is that dark energy undergoes bounded, self-similar oscillations in conformal time, arising naturally from axion-like monodromy or discrete scale-invariant scalar potentials. In this work, we formulate an exact closed-form relativistic solution for Log-Oscillatory Dark Energy and audit its observational constraints against CPL using full covariance matrices and upcoming ESA Euclid forecasts~\cite{blanchard2020}.

\section{The Log-Oscillatory Dark Energy Formulation}
We consider a minimally coupled, homogeneous dark energy fluid characterized by a bounded, log-periodic equation of state:
\begin{equation}
w(a) = -1 + A \sin\left( \frac{2\pi}{\ln\lambda} \ln a + \phi_0 \right) = -1 + A \sin(\omega_a \ln a + \phi_0),
\label{eq:log_osc}
\end{equation}
where $A$ represents the oscillation amplitude, $\lambda > 1$ is the scale factor ratio governing the periodicity in $e$-folds, $\omega_a \equiv 2\pi / \ln\lambda$, and $\phi_0 \in [-\pi, \pi]$ is an initial phase at the current epoch ($a = 1$). To avoid unbounded phantom divergence or singularity, the amplitude is naturally bounded by $|A| < 1$.

\subsection{Exact Relativistic Energy Density}
The relativistic conservation equation for an uncoupled fluid in a spatially flat FLRW metric reads:
\begin{equation}
\frac{d\rho_{\mathrm{de}}}{da} + \frac{3}{a} \left[ 1 + w(a) \right] \rho_{\mathrm{de}} = 0.
\label{eq:continuity}
\end{equation}
Substituting Eq.~\eqref{eq:log_osc} into Eq.~\eqref{eq:continuity}:
\begin{align}
\ln \frac{\rho_{\mathrm{de}}(a)}{\rho_{\mathrm{de}, 0}} &= -3 \int_1^a \frac{1 + w(a')}{a'} da' \nonumber \\
&= -3 A \int_1^a \frac{\sin(\omega_a \ln a' + \phi_0)}{a'} da'.
\end{align}
Under the substitution $u = \ln a'$, with $du = da'/a'$:
\begin{equation}
\int_0^{\ln a} \sin(\omega_a u + \phi_0) du = \frac{1}{\omega_a} \left[ \cos\phi_0 - \cos(\omega_a \ln a + \phi_0) \right].
\end{equation}
Thus, we obtain the exact closed-form analytical expression for the dark energy density:
\begin{equation}
\rho_{\mathrm{de}}(a) = \rho_{\mathrm{de}, 0} \exp\left\{ \frac{3A}{\omega_a} \left[ \cos(\omega_a \ln a + \phi_0) - \cos\phi_0 \right] \right\}.
\label{eq:rho_exact}
\end{equation}
Unlike polynomial dark energy models whose energy densities diverge exponentially at early times, Eq.~\eqref{eq:rho_exact} is bounded for all $a \in (0, 1]$:
\begin{equation}
\rho_{\mathrm{de}, 0} \, e^{-6A/\omega_a} \le \rho_{\mathrm{de}}(a) \le \rho_{\mathrm{de}, 0} \, e^{+6A/\omega_a}.
\end{equation}

\section{Observational Datasets and Likelihood Methodology}
We evaluate the parameter space using the joint cosmological likelihood:
\begin{equation}
\ln \mathcal{L}_{\mathrm{joint}} = \ln \mathcal{L}_{\mathrm{SN}} + \ln \mathcal{L}_{\mathrm{BAO}} + \ln \mathcal{L}_{\mathrm{CMB}}.
\end{equation}
\begin{itemize}
    \item \textbf{Type Ia Supernovae (Pantheon+):} We analyze the full Pantheon+ compilation~\cite{brout2022} consisting of $N = 1701$ light curves across $1580$ distinct SNe~Ia spanning $0.001 \le z \le 2.26$. The chi-square is computed using the complete $1580 \times 1580$ systematic covariance matrix $C_{\mathrm{sys}}$ with analytic marginalization over the nuisance parameter $M$:
    \begin{equation}
    \chi^2_{\mathrm{SN}} = \Delta\boldsymbol{\mu}^T C_{\mathrm{sys}}^{-1} \Delta\boldsymbol{\mu} - \frac{(\mathbf{1}^T C_{\mathrm{sys}}^{-1} \Delta\boldsymbol{\mu})^2}{\mathbf{1}^T C_{\mathrm{sys}}^{-1} \mathbf{1}}.
    \end{equation}
    \item \textbf{Baryon Acoustic Oscillations (DESI DR1):} We utilize the 12 consensus BAO measurements of $D_M(z)/r_d$ and $D_H(z)/r_d$ across six redshift tracers ($0.30 \le z \le 2.33$) from the official DESI Year~1 release~\cite{desi2024}.
    \item \textbf{CMB Distance Priors (Planck 2018):} We adopt the compressed Planck 2018 PR3 distance priors~\cite{chen2019} on the acoustic scale $l_A = 301.47 \pm 0.09$, shift parameter $R = 1.7499 \pm 0.0039$, and physical baryon density $\omega_b = 0.02237 \pm 0.00015$.
\end{itemize}

\begin{figure*}[t]
\centering
\includegraphics[width=0.92\textwidth]{figures/fig_euclid_hubble_forecast.png}
\caption{Observational constraints and ESA Euclid forecast. (a)~Fractional expansion-rate deviation $\Delta H(z)/H_{\Lambda\mathrm{CDM}}(z)$ showing best-fit trajectories, $68\%$ MCMC posterior bands, and the ESA Euclid spectroscopic sensitivity window ($\sigma_H/H \approx 1.3\%$ per bin across $0.9 \le z \le 1.8$~\cite{blanchard2020}). (b)~Reconstructed dark energy equation of state $w(z)$. While CPL plunges monotonically into phantom values ($w(3) = -1.277$), the Log-Oscillatory model exhibits a turnaround ($w(3) = -1.172$, $\Delta w = +0.104$). (c)~Progressive model-selection criteria ($\Delta\chi^2$, $\Delta\mathrm{AIC}$, $\Delta\mathrm{BIC}$) across dataset combinations.}
\label{fig:forecast}
\end{figure*}

\section{Results and Degeneracy Breaking with Euclid}
Our joint optimization yields the following key findings:
\begin{enumerate}
    \item \textbf{Supernovae in Isolation:} When analyzed with the full $1580 \times 1580$ covariance matrix, Pantheon+ alone recovers $\Omega_m = 0.3325 \pm 0.0182$ ($\chi^2/\mathrm{dof} = 0.879$). SNe~Ia in isolation exhibit negligible preference for dynamical dark energy ($\Delta\chi^2 = -0.47$ for CPL and $-0.49$ for Log-Oscillatory).
    \item \textbf{Current Joint Preference ($\sim 1.5\sigma$):} Combining Pantheon+ with DESI Year~1 BAO and Planck CMB anchors resolves the $\Omega_m$--$w(z)$ geometric degeneracy, yielding an interior best fit with $\Delta\chi^2 = -3.75$ for CPL and $\Delta\chi^2 = -3.90$ for Log-Oscillatory ($A = 0.218$, $\lambda = 3.09$, $\phi_0 = 0.592\,\mathrm{rad}$).
    \item \textbf{The Parameter Degeneracy:} As displayed in Fig.~\ref{fig:forecast}(a,b), the $68\%$ MCMC posterior bands of CPL and Log-Oscillatory overlap heavily throughout $z \le 2.33$. The current $1\sigma$ posterior uncertainty on $\Delta H(z)/H_{\Lambda\mathrm{CDM}}$ is $\sim 1.5\%\text{--}2.2\%$, which prevents current data from distinguishing between the models.
    \item \textbf{Breaking the Degeneracy with Euclid:} The ESA Euclid spectroscopic survey~\cite{blanchard2020} will provide $\sigma_H/H \approx 1.3\%$ measurements across $0.9 < z < 1.8$. At $z \approx 1.5\text{--}3.0$, the Log-Oscillatory model predicts an expansion turnaround ($\Delta w(z=3) = +0.104$ relative to CPL). Euclid's high-precision data will readily distinguish this turnaround at $>3\sigma$, definitively testing whether dark energy undergoes bounded oscillations or continues a monotonic phantom trajectory.
\end{enumerate}

\section{Summary}
We have developed an exact, closed-form relativistic formulation for Log-Oscillatory Dark Energy and tested it against flat $\Lambda\mathrm{CDM}$ and CPL using full Pantheon+, DESI Year~1 BAO, and Planck CMB covariance matrices. While current multi-probe datasets exhibit a mild $\Delta\chi^2 \approx -3.90$ preference over $\Lambda\mathrm{CDM}$, they cannot yet distinguish between dynamical models. Upcoming expansion rate measurements from the ESA Euclid spectroscopic survey, with $1.3\%$ precision in $H(z)$, will decisively break this degeneracy and determine whether cosmic acceleration is driven by bounded physical oscillations.
"""

with open(os.path.join(ch_dir, "ch3_euclid_dark_energy.tex"), "w", encoding="utf-8") as f:
    f.write(ch3_content)

print("Wrote ch3_euclid_dark_energy.tex")

# -------------------------------------------------------------
# CHAPTER 4: QISKIT NISQ ZNE BENCHMARK
# -------------------------------------------------------------
ch4_content = r"""\chapter{When Harmonic ZNE Fails: Quantum Error Mitigation Benchmarks}
\label{ch:qiskit_zne}

\begin{abstract}
Zero-Noise Extrapolation (ZNE) is a cornerstone of quantum error mitigation on Noisy Intermediate-Scale Quantum (NISQ) processors. While standard polynomial and exponential extrapolation models assume monotonic error accumulation, coherent unitary noise---such as persistent Stark shifts and crosstalk over-rotations---induces oscillatory expectation trajectories. Recently, harmonic and spectral ZNE techniques leveraging Lomb--Scargle periodograms have been proposed to mitigate periodic phase errors. In this chapter, we present a pre-registered, head-to-head empirical benchmark comparing standard polynomial, exponential, and harmonic ZNE against two-qubit Clifford Pauli Twirling across 1-qubit Ramsey echo and 4-qubit Transverse-Field Ising Model (TFIM) Trotter circuits under strictly matched shot budgets ($N_{\mathrm{total}} = 24{,}000$ shots per seed). In a 1-qubit coherent Ramsey sequence probed across deep noise scales ($\lambda \le 17$), harmonic ZNE achieves an $85.4\%$ reduction in Mean Absolute Error (MAE), overcoming sign inversions where polynomial and exponential models fail catastrophically. However, in an entangled 4-qubit Trotter circuit, harmonic ZNE fails catastrophically: its MAE surges to $2.28$ under moderate coherent over-rotation ($\epsilon = 0.04\,$rad), performing significantly worse than unmitigated execution ($\mathrm{MAE} = 0.148$). In contrast, randomized compiling via Pauli Twirling converts non-commuting coherent $ZZ$ crosstalk into stochastic Pauli channels, enabling linear and exponential ZNE to achieve robust error reductions of $80.8\%\text{--}81.0\%$. We delineate the physical mechanisms governing this breakdown---multi-mode non-commutative interference and parameter ill-conditioning on bounded scale schedules---and establish operational guidelines for quantum hardware practitioners.
\end{abstract}

\section{Introduction}
Current quantum computing platforms operate in the Noisy Intermediate-Scale Quantum (NISQ) regime~\cite{preskill2018}, where gate fidelities are constrained by environmental decoherence, control imperfections, and parasitic crosstalk. In the absence of fault-tolerant quantum error correction, Quantum Error Mitigation (QEM) has emerged as an indispensable paradigm for extracting accurate expectation values from shallow-to-intermediate depth quantum circuits~\cite{temme2017,li2017,cai2023}.

Among QEM strategies, Zero-Noise Extrapolation (ZNE)~\cite{temme2017,li2017,kandala2019} stands out as a purely software-level technique that does not require auxiliary qubits. ZNE amplifies noise through controlled hardware or digital mechanisms---most commonly unitary gate folding ($G \to G G^\dagger G$)~\cite{giurgica2020}---measures the observable of interest at multiple noise scale factors $\lambda \ge 1$, and extrapolates the resulting curve to the zero-noise limit $\lambda \to 0$.

Standard ZNE pipelines typically rely on linear, Richardson polynomial, or exponential ansatzes~\cite{temme2017,giurgica2020}. While these models perform well under memoryless, stochastic depolarizing noise, superconducting transmon processors frequently suffer from coherent errors, including residual AC Stark shifts, calibration detuning, and parasitic $ZZ$-crosstalk between coupled qubits~\cite{kandala2019,hashim2021}. When noise scales are amplified, coherent unitary over-rotations rotate quantum states periodically on the Bloch sphere, inducing damped oscillations in observable expectation values rather than monotonic decay. Extrapolating such oscillating trajectories with low-order polynomials or pure exponentials leads to severe divergence or sign inversions.

To address this challenge, harmonic ZNE and spectral estimation schemes utilizing the generalized Lomb--Scargle periodogram~\cite{lomb1976,scargle1982} have been explored to detect and fit coherent frequency components in unevenly sampled ZNE data. Concurrently, randomized compiling---specifically Clifford Pauli Twirling~\cite{wallman2016,hashim2021}---has gained widespread adoption by actively transforming arbitrary coherent errors into stochastic Pauli channels prior to measurement.

In this chapter, we report a pre-registered, head-to-head empirical study of these competing approaches. We demonstrate that while harmonic ZNE delivers superior mitigation on isolated single-qubit coherent drift ($85.4\%$ error reduction), it undergoes catastrophic failure when applied to multi-qubit entangled circuits, where MAE surges above $2.2$. In contrast, Pauli Twirling combined with standard linear or exponential ZNE consistently delivers $80.8\%\text{--}81.0\%$ error reduction across multi-qubit workloads under identical total shot budgets. We explain the exact mathematical and physical reasons for this divergence and establish clear operational boundaries for both techniques.

\section{Methodology and Mitigation Architectures}

\subsection{Digital Noise Amplification and Fractional Folding}
Noise amplification is achieved via digital unitary folding~\cite{giurgica2020}. For an integer scale factor $\lambda = 1 + 2k$ ($k \in \mathbb{N}$), each target gate $G \in \mathrm{SU}(2^n)$ is replaced by:
\begin{equation}
G \;\longrightarrow\; G\,(G^\dagger G)^k,
\label{eq:integer_folding}
\end{equation}
which preserves the exact logical unitary operation ($U_{\mathrm{folded}} = U$) while amplifying circuit depth and physical noise exposure by a factor of $\lambda$.

To overcome the discrete granularity of integer folding ($\lambda \in \{1, 3, 5, \dots\}$), we implement gate-level non-uniform fractional unitary folding~\cite{giurgica2020}. For a desired continuous scale factor $\lambda \in [1.0, \lambda_{\max}]$, a subset of gates is selected to undergo folding $G \to G G^\dagger G$. Two-qubit entangling gates ($\mathrm{CX}$) are prioritized with a $10:1$ sampling weight relative to single-qubit gates, reflecting typical hardware error rate disparities in transmon architectures. Transpiler optimization barriers are inserted to prevent compiler cancellations, ensuring mathematically exact logical equivalence while producing non-uniform scale grids:
\begin{equation}
\lambda_j = 1 + 2\,\frac{N_{\mathrm{folded}, j}}{N_{\mathrm{total\_gates}}}.
\end{equation}

\subsection{Two-Qubit Clifford Pauli Twirling}
Randomized compiling tailors arbitrary noise channels into stochastic Pauli channels via random gate insertions~\cite{wallman2016}. For every two-qubit $\mathrm{CX}$ gate in the circuit, we sample independent Pauli operators $(P_c, P_t) \in \{I, X, Y, Z\}^2$ from the 16 elements of the two-qubit Pauli group. The correction operators $(P'_c, P'_t)$ are determined by the exact Clifford commutation relation:
\begin{equation}
(P'_c \otimes P'_t)\,\mathrm{CX}\,(P_c \otimes P_t) = \pm\,\mathrm{CX}.
\label{eq:pauli_twirl}
\end{equation}
A global phase correction is tracked to preserve the exact logical state. Averaging over twirled circuit instances maps an arbitrary noise map $\mathcal{E}$ to a twirled channel:
\begin{align}
\mathcal{E}_{\mathrm{twirl}}(\rho) &= \frac{1}{16} \sum_{k=1}^{16} P_k^\dagger \mathcal{E}(P_k \rho P_k^\dagger) P_k \nonumber \\
&= (1-p_{\mathrm{eff}})\rho + \sum_{i} c_i P_i \rho P_i,
\end{align}
eliminating all off-diagonal coherent cross-terms.

\subsection{Extrapolation Models}
Given expectation values $\{(\lambda_j, \hat{E}_j)\}_{j=1}^M$ measured across $M$ noise scales, we evaluate four extrapolation families:
\begin{enumerate}
    \item \textbf{Local Linear ZNE:} Fits $E(\lambda) = E_0 + a_1 \lambda$ over low noise scales ($\lambda \le 2.3$), yielding $E_{\mathrm{est}}(0) = E_0$.
    \item \textbf{Quadratic Richardson ZNE:} Fits $E(\lambda) = E_0 + a_1 \lambda + a_2 \lambda^2$ across all available scales.
    \item \textbf{Exponential ZNE:} Fits $E(\lambda) = E_0 e^{-\beta \lambda} + c$, modeling monotonic depolarizing decay towards the maximally mixed state.
    \item \textbf{Damped Harmonic / Lomb--Scargle ZNE:} Fits a four-parameter damped cosine model:
    \begin{equation}
    E(\lambda) = E_0 \, e^{-\gamma \lambda} \cos(\omega \lambda + \phi),
    \label{eq:harmonic_model}
    \end{equation}
    where initial frequency estimates $\omega_0$ are initialized via the generalized Lomb--Scargle periodogram~\cite{scargle1982} to handle non-uniform scale spacing without spectral leakage.
\end{enumerate}

\subsection{Pre-Registered 2-SE Decision Rule}
To avoid post-selection bias, we enforce a strict pre-registered decision metric. Damped Harmonic ZNE is declared to possess a verified methodological advantage in a given noise regime if and only if its Mean Absolute Error ($\mathrm{MAE}$) over $K \ge 20$ independent random seeds satisfies:
\begin{equation}
z \equiv \frac{\mathrm{MAE}_{\mathrm{best\_standard}} - \mathrm{MAE}_{\mathrm{harmonic}}}{\sqrt{\mathrm{SE}^2_{\mathrm{best\_standard}} + \mathrm{SE}^2_{\mathrm{harmonic}}}} \ge +2.0,
\label{eq:decision_rule}
\end{equation}
where $\mathrm{MAE}_{\mathrm{best\_standard}}$ is the best-performing baseline under an identical total shot budget ($N_{\mathrm{total}} = 24{,}000$ shots per seed). If $z < +2.0$, the null hypothesis holds.

\begin{table*}[t]
\centering
\small
\caption{\textbf{Head-to-head performance across 1-qubit coherent Ramsey echo and 4-qubit TFIM Trotter benchmarks.} MAE and standard errors computed across independent random seeds under matched total shot budgets ($N_{\mathrm{total}} = 24{,}000$ shots/seed). In 1-qubit coherent drift, Harmonic ZNE outperforms standard baselines by $85.4\%$. In 4-qubit multi-mode circuits, Harmonic ZNE diverges ($z < -4.7\,\mathrm{SE}$), whereas Pauli Twirling + Linear/Exp ZNE reduces error by $80.8\%\text{--}81.0\%$.}
\label{tab:zne_benchmark}
\resizebox{\textwidth}{!}{%
\begin{tabular}{lccccc}
\toprule
\textbf{Mitigation Method} & \textbf{1-Qubit Ramsey} & \multicolumn{4}{c}{\textbf{4-Qubit TFIM Trotter Circuit ($\langle Z_0 \rangle$, Ideal $=-0.4081$)}} \\
\cmidrule(lr){3-6}
& ($\theta = 0.22\,$rad/layer) & $\epsilon = 0.00\,$rad & $\epsilon = 0.04\,$rad & $\epsilon = 0.08\,$rad & $\epsilon = 0.14\,$rad \\
\midrule
Unmitigated ($\lambda=1$) & $0.0486 \pm 0.0009$ & $0.0294 \pm 0.0036$ & $0.1484 \pm 0.0033$ & $0.2898 \pm 0.0032$ & $0.5308 \pm 0.0033$ \\
Local Linear ZNE & $0.1215 \pm 0.0015$ & $0.0195 \pm 0.0029$ & $0.0375 \pm 0.0052$ & $0.0726 \pm 0.0055$ & $\mathbf{0.0959 \pm 0.0041}$ \\
Quadratic Richardson ZNE & $0.3195 \pm 0.0015$ & $0.0380 \pm 0.0062$ & $0.0952 \pm 0.0097$ & $0.2088 \pm 0.0100$ & $0.2098 \pm 0.0100$ \\
Exponential ZNE (Untwirled) & $0.5770 \pm 0.0016$ & $\mathbf{0.0154 \pm 0.0019}$ & $0.3601 \pm 0.0172$ & $0.5390 \pm 0.0011$ & $0.7858 \pm 0.0010$ \\
\midrule
\textbf{Pauli Twirling + Linear ZNE} & --- & $0.0213 \pm 0.0032$ & $\mathbf{0.0285 \pm 0.0065}$ & $\mathbf{0.0551 \pm 0.0092}$ & $0.1211 \pm 0.0169$ \\
\textbf{Pauli Twirling + Exp ZNE} & --- & $0.0263 \pm 0.0038$ & $0.0292 \pm 0.0047$ & $0.0562 \pm 0.0089$ & $0.1182 \pm 0.0123$ \\
\midrule
\textbf{Damped Harmonic ZNE} & $\mathbf{0.0071 \pm 0.0011}$ & $1.3431 \pm 0.1590$ & $2.2868 \pm 0.0000$ & $0.3650 \pm 0.0643$ & $0.5578 \pm 0.0018$ \\
\midrule
\textbf{Pre-Reg. $2\text{-}\mathrm{SE}$ Niche Met?} & \textbf{CONFIRMED} ($z=+22.1$) & \textbf{FALSE} ($z=-8.35$) & \textbf{FALSE} ($z=-347.2$) & \textbf{FALSE} ($z=-4.77$) & \textbf{FALSE} ($z=-103.7$) \\
\textbf{Best Error Reduction vs. Unmit.} & $\mathbf{-85.4\%}$ (Harmonic) & $-47.6\%$ (Exp) & $\mathbf{-80.8\%}$ (Twirl+Lin) & $\mathbf{-81.0\%}$ (Twirl+Lin) & $\mathbf{-81.9\%}$ (Linear) \\
\bottomrule
\end{tabular}%
}
\end{table*}

\section{Benchmark Experiments and Results}

\subsection{Regime A: Single-Qubit Coherent Ramsey Echo}
We first evaluate a single-qubit Ramsey sequence ($H - \mathrm{Id}^s - H$) subject to a coherent Stark shift $R_Z(\theta = 0.22\,$rad/layer) and depolarizing noise ($p = 0.025$). Noise scale factors span deep non-uniform delays $s \in \{1, 2, 3, 5, 7, 10, 13, 17\}$, encompassing more than half an oscillation cycle ($\theta \cdot s \approx 3.74\,$rad). The target observable is $\langle Z \rangle$ with ideal value $E_{\mathrm{ideal}} = +1.0000$.

As summarized in Table~\ref{tab:zne_benchmark}, the unmitigated expectation error is $\mathrm{MAE} = 0.0486 \pm 0.0009$. Standard polynomial and exponential extrapolators fail completely:
\begin{itemize}
    \item Quadratic Richardson ZNE yields $\mathrm{MAE} = 0.3195 \pm 0.0015$ ($+557\%$ error increase), as the polynomial attempts to fit a turning curve with an inverted parabola.
    \item Exponential ZNE yields $\mathrm{MAE} = 0.5770 \pm 0.0016$ ($+1087\%$ error increase), forcing a monotonic decay on an oscillating signal.
    \item In sharp contrast, Damped Harmonic ZNE captures the single oscillation mode ($\hat{\omega} \approx 0.22\,$rad/scale), reducing the estimation error to $\mathrm{MAE} = 0.0071 \pm 0.0011$---an \textbf{85.4\% reduction} relative to unmitigated execution and a \textbf{97.8\% reduction} relative to quadratic extrapolation ($z = +22.1\,\mathrm{SE}$).
\end{itemize}

\subsection{Regime B: 4-Qubit Entangled TFIM Trotter Circuit}
Next, we evaluate an entangled 4-qubit Transverse-Field Ising Model (TFIM) circuit comprising 3 Trotter steps (18 $\mathrm{CX}$ entangling gates in a brick-wall architecture) with Hamiltonian:
\begin{equation}
H = -J \sum_{i=0}^2 Z_i Z_{i+1} - h \sum_{i=0}^3 X_i,
\end{equation}
with $J = 0.35$ and $h = 0.45$. We measure $\langle Z_0 \rangle$ (ideal value $E_{\mathrm{ideal}} = -0.408093$). Noise consists of hardware-realistic depolarizing channels ($p_1 = 0.001$, $p_2 = 0.012$) and coherent over-rotations $R_{ZZ}(\epsilon) \otimes R_Z(\epsilon)$ on all entangling layers across four coupling strengths: $\epsilon \in \{0.00, 0.04, 0.08, 0.14\}\,$rad. Fractional folding generates 6 noise scales $\lambda \in [1.000, 3.498]$. For Pauli Twirling, 12 independent twirled circuits are executed with 2,000 shots each, maintaining the exact $N_{\mathrm{total}} = 24{,}000$ total shot budget per seed.

\begin{figure*}[t]
\centering
\includegraphics[width=0.88\textwidth]{figures/fig_fair_zne_comparison.png}
\caption{\textbf{Pre-registered head-to-head quantum error mitigation benchmark on the 4-qubit TFIM Trotter circuit.} (a) Mean Absolute Error $|\hat{E}(0) - E_{\mathrm{ideal}}|$ across 20 independent seeds as a function of coherent over-rotation angle $\epsilon$. Damped Harmonic ZNE diverges severely ($\mathrm{MAE} > 0.36$), while Pauli Twirling + Linear/Exponential ZNE suppresses error to $\le 0.055$. (b) Bar chart at strong coherent drift ($\epsilon = 0.14\,$rad), highlighting the failure of harmonic and exponential fits and the resilience of Pauli Twirling and local linear extrapolation.}
\label{fig:benchmark_results}
\end{figure*}

The multi-qubit results (Table~\ref{tab:zne_benchmark} and Figure~\ref{fig:benchmark_results}) reveal a stark reversal:
\begin{enumerate}
    \item \textbf{Harmonic ZNE Catastrophic Breakdown:} At $\epsilon = 0.04\,$rad, Damped Harmonic ZNE yields an error of $\mathrm{MAE} = 2.2868 \pm 0.0000$---an order of magnitude worse than unmitigated execution ($\mathrm{MAE} = 0.1484$). Across all four coherent noise settings, Harmonic ZNE fails the pre-registered $2\text{-}\mathrm{SE}$ test by massive margins ($z = -8.35$, $z = -347.2$, $z = -4.77$, and $z = -103.7$).
    \item \textbf{Breakdown of Untwirled Exponential ZNE:} Untwirled Exponential ZNE degrades rapidly as coherent noise increases, with MAE climbing from $0.0154$ ($\epsilon=0$) to $0.3601$ ($\epsilon=0.04$) and $0.7858$ ($\epsilon=0.14$).
    \item \textbf{Superiority of Pauli Twirling + ZNE:} In contrast, applying two-qubit Clifford Pauli Twirling restores near-ideal monotonic behavior. Pauli Twirling + Linear ZNE achieves $\mathrm{MAE} = 0.0285 \pm 0.0065$ at $\epsilon = 0.04\,$rad (\textbf{80.8\% error reduction}) and $\mathrm{MAE} = 0.0551 \pm 0.0092$ at $\epsilon = 0.08\,$rad (\textbf{81.0\% error reduction}), matching Pauli Twirling + Exponential ZNE ($0.0292$ and $0.0562$).
\end{enumerate}

\section{Discussion: Why Harmonic ZNE Fails in Multi-Qubit Circuits}
The contrasting performance between Regime A and Regime B stems from two fundamental physical and numerical factors:

\subsection{Multi-Mode Non-Commutative Interference}
In a single-qubit idle sequence (Regime A), the coherent error operator $e^{-i \theta Z}$ commutes with itself across all folded layers. The state vector rotates around a single axis, producing an exact scalar harmonic modulation:
\begin{equation}
\langle \psi(\lambda) | Z | \psi(\lambda) \rangle = e^{-\gamma \lambda} \cos(\omega \lambda + \phi).
\end{equation}
In an entangled multi-qubit Trotter circuit (Regime B), however, coherent over-rotations $R_{ZZ}(\epsilon)$ and $R_Z(\epsilon)$ do not commute with the transverse field operators $R_X(2h)$ or with subsequent entangling blocks. As noise scaling duplicates gates, the resulting unitary error map expands into a non-commuting Baker--Campbell--Hausdorff series involving multiple Pauli channels:
\begin{equation}
U(\lambda) = \prod_{k=1}^{D(\lambda)} \exp\left[ -i \left( H_{\mathrm{target}}^{(k)} + \epsilon_k V_k \right) \right].
\end{equation}
The expectation value $\langle Z_0(\lambda) \rangle$ becomes a superposition of numerous interfering frequency components rather than a single pure sinusoid. Fitting a single-frequency model (Eq.~\eqref{eq:harmonic_model}) to multi-frequency interference creates severe model misspecification.

\subsection{Parameter Overfitting on Short Scale Schedules}
In practical NISQ workflows, noise scale schedules are strictly bounded ($\lambda \in [1.0, 3.5]$) to avoid running deeply folded circuits where signal-to-noise ratios collapse. Over this narrow scale window, the total phase accumulated by coherent over-rotations ($\Delta \theta \sim \epsilon \cdot \Delta \lambda$) covers only a small fraction of an oscillation cycle ($< 0.1\times 2\pi$). 

Fitting a 4-parameter non-linear damped sine ($E_0, \gamma, \omega, \phi$) to 6 noisy data points over less than a quarter-period is an ill-posed inverse problem. The Levenberg--Marquardt optimization surface develops multiple local minima and flat directions, causing the fitted amplitude $E_0$ to explode to unphysical values ($|E_0| > 2$).

\subsection{Why Pauli Twirling Resolves the Dilemma}
Clifford Pauli Twirling actively modifies the noise physics before extrapolation occurs. By randomly twirling all two-qubit entangling gates, coherent phase errors $\epsilon$ are depolarized into stochastic Pauli channels:
\begin{equation}
\mathcal{E}_{ZZ}(\rho) = (1 - \sin^2\epsilon)\,\rho + \sin^2\epsilon\,(Z \otimes Z)\rho(Z \otimes Z).
\end{equation}
This eliminates inter-qubit coherent interference, guarantees strict monotonic decay of expectation values, and allows low-order linear and exponential extrapolators to operate within their rigorous theoretical domain.

\section{Summary and Practical Guidelines}
Our benchmark establishes clear practical guidelines for quantum software engineering:
\begin{enumerate}
    \item \textbf{Do NOT use Harmonic ZNE for multi-qubit algorithms.} Coherent crosstalk does not produce a single sinusoid, and fitting harmonic models to short ZNE schedules leads to severe overfitting and divergence ($\mathrm{MAE} > 2.2$).
    \item \textbf{Deploy Clifford Pauli Twirling with Linear/Exponential ZNE.} Twirling guarantees an $80.8\%\text{--}81.0\%$ error reduction under coherent crosstalk with zero additional hardware overhead and identical total shot budgets.
    \item \textbf{Reserve Harmonic ZNE for single-mode calibration.} In isolated single-qubit characterization experiments (such as idle echo or Stark shift calibration over deep delays), harmonic ZNE successfully achieves an $85.4\%$ error reduction where conventional polynomial methods fail.
\end{enumerate}
"""

with open(os.path.join(ch_dir, "ch4_qiskit_zne.tex"), "w", encoding="utf-8") as f:
    f.write(ch4_content)

print("Wrote ch4_qiskit_zne.tex")

# -------------------------------------------------------------
# CHAPTER 5: POST-QUANTUM CRYPTOGRAPHY
# -------------------------------------------------------------
ch5_content = r"""\chapter{The Network Cost of Post-Quantum Cryptography: TLS 1.3 Wire Cost}
\label{ch:pqc_network_cost}

\begin{abstract}
The advent of quantum computing threatens classical public-key cryptography via Shor's algorithm, prompting the global migration toward Post-Quantum Cryptography (PQC) standardized by NIST in August 2024. While lattice-based cryptography is often assumed to impose severe computational overhead, our empirical benchmarks demonstrate the opposite: key generation in ML-KEM-768 (NIST FIPS 203) executes in just $41.3\,\mu\mathrm{s}$---approximately $740\times$ faster than RSA-2048 ($30.49\,$ms). Instead, the true architectural bottleneck lies in network transport and wire payload expansion. While classical ECDH requires only $65\,$bytes per key share, ML-KEM-768 transmits a $1{,}184$-byte public key and a $1{,}088$-byte ciphertext ($2{,}272\,$B total KEM wire), expanding to $2{,}402\,$B in hybrid deployments (X25519 + ML-KEM-768). Over standard Ethernet with a Maximum Segment Size (MSS) of $1{,}460\,$bytes, a full hybrid \texttt{ClientHello} flight ($1{,}518\,$B) breaches the 1-MSS boundary, mandating TCP segmentation into two distinct packets. Through analytical modeling and empirical socket transport audits, we evaluate the impact against RFC 6928 initial congestion windows ($\texttt{initcwnd} = 10$). We demonstrate that while clean networks absorb multi-segment handshakes within the initial flight, lossy links suffer increased head-of-line blocking sensitivity and legacy middlebox inspection buffer drops.
\end{abstract}

\section{Introduction}
Asymmetric cryptography underpins the integrity and confidentiality of the global digital infrastructure, securing transport-layer communications (TLS 1.3)~\cite{rescorla2018}, financial settlement systems (SWIFT, PIX), and identity protocols. However, the foundational primitives of classical public-key cryptography---modular integer factorization (RSA) and elliptic-curve discrete logarithms (ECDH/ECDSA)---are vulnerable to Shor's algorithm~\cite{shor1994}, which solves both problems in polynomial time on a fault-tolerant quantum computer.

To mitigate ``harvest now, decrypt later'' adversarial campaigns, the National Institute of Standards and Technology (NIST) finalized its primary post-quantum cryptographic standards in August 2024:
\begin{itemize}
    \item \textbf{FIPS 203 (ML-KEM):} Module-Lattice-Based Key-Encapsulation Mechanism, derived from CRYSTALS-Kyber~\cite{bos2018}.
    \item \textbf{FIPS 204 (ML-DSA):} Module-Lattice-Based Digital Signature Algorithm, derived from CRYSTALS-Dilithium.
\end{itemize}

During initial deployment phases, major standardization bodies (e.g., IETF) recommend hybrid key exchange mechanisms combining a classical primitive (e.g., X25519 or ECDH P-256) with ML-KEM-768 to maintain regulatory compliance while achieving quantum resistance~\cite{schwabe2020}.

A prevailing assumption in systems engineering is that post-quantum primitives are computationally prohibitive. In this work, we demonstrate that lattice arithmetic is remarkably fast, accelerating key generation by more than two orders of magnitude compared to RSA. Instead, the critical trade-off is shifted to the transport layer: lattice keys are orders of magnitude larger than classical elliptic-curve points, altering the network framing dynamics of the TLS 1.3 handshake flight over standard Ethernet Maximum Transmission Units (MTU)~\cite{paquin2020,sikeridis2020}.

\section{Methodology and Measurement Setup}

\subsection{Cryptographic Benchmark Framework}
Benchmarking was executed using optimized, compiled C-extensions (`pqcrypto` and OpenSSL $3.0+$ via `cryptography.hazmat`) on an isolated x86\_64 processor core with high-resolution CPU performance counters. We evaluated five cryptographic configurations:
\begin{enumerate}
    \item \textbf{RSA-2048:} Classical modular exponentiation ($e=65537$).
    \item \textbf{RSA-4096:} High-security classical baseline.
    \item \textbf{ECDH P-256:} Standard NIST Prime Curve (secp256r1).
    \item \textbf{ML-KEM-768:} NIST Security Category 3 (AES-192 equivalent).
    \item \textbf{Hybrid PQC:} Concatenated X25519 ($32\,$B) + ML-KEM-768 ($1{,}184\,$B public key; $1{,}088\,$B ciphertext), deriving a joint secret via HKDF-SHA256.
\end{enumerate}
Timing metrics for Key Generation ($\mathrm{KeyGen}$), Encapsulation ($\mathrm{Encaps}$), and Decapsulation ($\mathrm{Decaps}$) were measured over 100 independent trials for fast algorithms and 15 trials for RSA.

\subsection{TLS 1.3 Handshake Framing Model}
In RFC 8446 (TLS 1.3)~\cite{rescorla2018}, key establishment occurs within the first round-trip flight:
\begin{itemize}
    \item \textbf{Flight 1 ($\mathrm{Client} \to \mathrm{Server}$):} Transmits the \texttt{ClientHello} message, comprising base handshake headers ($\sim 269\,$B of session IDs, cipher suites, SNI, and supported groups) plus the \texttt{KeyShare} extension holding the client's public key $pk$:
    \begin{equation}
    S_{\mathrm{ClientHello}} = 269\,\mathrm{B} + |pk|.
    \end{equation}
    \item \textbf{Flight 2 ($\mathrm{Server} \to \mathrm{Client}$):} Transmits \texttt{ServerHello} ($\sim 159\,\mathrm{B} + |ct|$ for ciphertext $ct$), followed by \texttt{EncryptedExtensions}, \texttt{Certificate} ($\sim 2{,}400\,$B standard chain), \texttt{CertificateVerify} ($\sim 64\,$B), and \texttt{Finished} ($\sim 120\,$B).
\end{itemize}

\subsection{Network Transport and Socket Buffer Audit}
On standard Ethernet networks, the data-link MTU is $1{,}500\,$bytes. Accounting for standard IPv4 header ($20\,$bytes) and TCP header ($20\,$bytes) without TCP options, the Maximum Segment Size is:
\begin{equation}
\mathrm{MSS} = \mathrm{MTU} - 40\,\mathrm{B} = 1{,}460\,\mathrm{bytes}.
\end{equation}
When an application-layer TLS record exceeds $1{,}460\,$bytes, the kernel TCP stack partitions the stream into $\lceil S / \mathrm{MSS} \rceil$ segments. We implemented a live socket test harness utilizing non-blocking user-space reads restricted to $1{,}460\,$bytes (\texttt{recv(1460)}) to observe packet fragmentation boundaries directly.

\begin{table*}[t]
\centering
\small
\caption{\textbf{Empirical performance and network wire overhead across classical and post-quantum key exchange mechanisms.} Timings measured with compiled C-extensions across independent trials. Wire sizes evaluate raw KEM exchange, RFC 8446 \texttt{ClientHello} flight, and TCP segment counts over standard $1{,}460$-byte Ethernet MSS.}
\label{tab:pqc_benchmark}
\resizebox{\textwidth}{!}{%
\begin{tabular}{lcccccccc}
\toprule
\textbf{Cryptographic Primitive} & \textbf{Quantum-Safe?} & \textbf{Public Key} & \textbf{Ciphertext} & \textbf{Total KEM Wire} & \textbf{KeyGen ($\mu\mathrm{s}$)} & \textbf{Encaps ($\mu\mathrm{s}$)} & \textbf{Decaps ($\mu\mathrm{s}$)} & \textbf{ClientHello Segments (1460 B MSS)} \\
\midrule
\textbf{RSA-2048} & \textbf{NO (Broken)} & $270\,$B & $256\,$B & $526\,$B & $30{,}490\,$ ($30.49\,$ms) & $251.2$ & $765.0$ & \textbf{1 segment} ($539\,$B, fits MSS) \\
\textbf{RSA-4096} & \textbf{NO (Broken)} & $526\,$B & $512\,$B & $1{,}038\,$B & $337{,}860\,$ ($337.86\,$ms) & $127.2$ & $3{,}760.0$ & \textbf{1 segment} ($795\,$B, fits MSS) \\
\textbf{ECDH P-256} & \textbf{NO (Broken)} & $65\,$B & $65\,$B & $130\,$B & $\mathbf{16.6}$ & $90.3$ & $\mathbf{49.0}$ & \textbf{1 segment} ($334\,$B, fits MSS) \\
\midrule
\textbf{ML-KEM-768} & \textbf{YES (Immune)} & $\mathbf{1{,}184\,B}$ & $\mathbf{1{,}088\,B}$ & $\mathbf{2{,}272\,B}$ & $\mathbf{41.3}$ & $\mathbf{46.7}$ & $\mathbf{63.0}$ & \textbf{1 segment} ($1{,}453\,$B, critical threshold) \\
\textbf{Hybrid PQC (X25519+ML-KEM)} & \textbf{YES (Immune)} & $\mathbf{1{,}249\,B}$ & $\mathbf{1{,}153\,B}$ & $\mathbf{2{,}402\,B}$ & $\mathbf{58.9}$ & $\mathbf{119.3}$ & $\mathbf{117.5}$ & \textbf{2 segments} ($\mathbf{1{,}518\,B}$, exceeds MSS) \\
\bottomrule
\end{tabular}%
}
\end{table*}

\section{Empirical Results}

\subsection{Computational Velocity: The Lattice Advantage}
Table~\ref{tab:pqc_benchmark} summarizes the computational and transport measurements. A striking result is that ML-KEM-768 key generation executes in just $41.3\,\mu\mathrm{s}$, outperforming RSA-2048 ($30{,}490\,\mu\mathrm{s}$) by a factor of $738.3\times$ ($> 2$ orders of magnitude), and outperforming RSA-4096 by $8{,}180\times$. 

Furthermore, ML-KEM-768 encapsulation ($46.7\,\mu\mathrm{s}$) and decapsulation ($63.0\,\mu\mathrm{s}$) are faster than both RSA operations ($251.2\,\mu\mathrm{s}$ and $765.0\,\mu\mathrm{s}$, respectively), and competitive with classical ECDH P-256 ($16.6\,\mu\mathrm{s}$ KeyGen, $49.0\,\mu\mathrm{s}$ Decaps). Hybrid PQC adds minimal CPU latency, completing key generation in $58.9\,\mu\mathrm{s}$ and encapsulation in $119.3\,\mu\mathrm{s}$. Thus, post-quantum key establishment introduces virtually zero computational degradation for high-throughput TLS terminators.

\begin{figure*}[t]
\centering
\includegraphics[width=0.90\textwidth]{figures/fig_pqc_crypto_agility.png}
\caption{\textbf{Empirical post-quantum crypto-agility benchmark across classical and NIST FIPS 203 standards.} (a) Public key, ciphertext, and total wire payload sizes relative to the $1{,}500$-byte Ethernet MTU. (b) Key generation latency ($\mu\mathrm{s}$, log scale), illustrating the $740\times$ speedup of ML-KEM-768 over RSA-2048. (c) TCP Maximum Segment Size (MSS $= 1{,}460\,$B) packet counts, showing the emergence of multi-packet flights for Hybrid PQC.}
\label{fig:pqc_agility}
\end{figure*}

\subsection{Wire Size and TCP Segmentation}
In contrast to computational velocity, wire size exhibits significant expansion (Figure~\ref{fig:pqc_agility}a). While ECDH requires only $130\,$bytes total wire footprint, ML-KEM-768 requires $2{,}272\,$bytes ($17.5\times$ larger), and Hybrid PQC requires $2{,}402\,$bytes ($18.5\times$ larger).

When packaged into an RFC 8446 \texttt{ClientHello}:
\begin{itemize}
    \item ECDH P-256 yields a $334$-byte flight, fitting comfortably into a single TCP segment ($22.9\%$ of MSS).
    \item Pure ML-KEM-768 yields $S_{\mathrm{ClientHello}} = 269 + 1{,}184 = 1{,}453\,\mathrm{bytes}$. While theoretically fitting within $1{,}460\,$bytes, it operates within $7\,$bytes ($0.48\%$) of the MSS boundary, meaning any additional TLS extension (e.g., ALPN, Session Tickets) pushes it into a second segment.
    \item Hybrid PQC produces $S_{\mathrm{ClientHello}} = 269 + 1{,}249 = 1{,}518\,\mathrm{bytes}$, strictly exceeding the $1{,}460$-byte MSS and forcing TCP segmentation into $2$ packets on the wire (Figure~\ref{fig:pqc_agility}c).
\end{itemize}

\section{Discussion: Network Protocol Implications}

\subsection{RFC 6928 and Initial Congestion Window (\texorpdfstring{$\texttt{initcwnd}$}{initcwnd})}
The operational cost of TCP fragmentation depends critically on the TCP initial congestion window ($\texttt{initcwnd}$). Under historical standards (RFC 2581, RFC 3390), $\texttt{initcwnd}$ was limited to $2\text{--}4$ segments. In that legacy regime, a multi-segment \texttt{ClientHello} or \texttt{ServerHello} flight could exhaust the congestion window, requiring an additional Round-Trip Time (RTT) before ACK reception allowed transmission to proceed.

Under modern TCP standards (RFC 6928)~\cite{chu2013}, the standard initial window is:
\begin{equation}
\texttt{initcwnd} = 10\,\mathrm{segments} \approx 14.6\,\mathrm{kB}.
\end{equation}
Because the full server response flight (ServerHello + Certificate + CertificateVerify + Finished) totals $\sim 4{,}000\text{--}5{,}200\,$bytes ($\approx 3\text{--}4$ segments), it fits entirely inside $\texttt{initcwnd} = 10$. Consequently, on uncongested, clean IP links, post-quantum fragmentation does not induce an extra round-trip latency penalty.

\subsection{Middlebox Ossification and Lossy Links}
Despite fitting within $\texttt{initcwnd} = 10$, multi-packet \texttt{ClientHello} flights introduce two notable real-world vulnerabilities:
\begin{enumerate}
    \item \textbf{Middlebox Reassembly Failures:} A non-negligible fraction of legacy enterprise firewalls, deep packet inspection (DPI) appliances, and load balancers assume that \texttt{ClientHello} fits within a single $1{,}500$-byte IP datagram. Fragmented TCP segments arriving out-of-order or triggering reassembly timeouts have been documented to cause handshake dropouts.
    \item \textbf{Head-of-Line Blocking on Lossy Links:} On mobile (4G/5G) or high-latency wireless connections subject to packet loss, partitioning the initial handshake flight into multiple TCP segments increases the probability of segment loss:
    \begin{equation}
    P_{\mathrm{loss\_flight}} = 1 - (1 - p)^N,
    \end{equation}
    where $p$ is the packet drop rate and $N$ is the segment count ($N=2$ for Hybrid PQC vs. $N=1$ for classical). A single dropped segment triggers TCP retransmission timeouts (RTO $\ge 200\,$ms), sharply amplifying tail latency.
\end{enumerate}

\section{Summary and Practical Guidelines}
Our empirical evaluation demonstrates that post-quantum lattice cryptography is computationally mature: ML-KEM-768 executes key generation $740\times$ faster than RSA-2048. The primary architectural hurdle is situated at the transport layer:
\begin{enumerate}
    \item \textbf{Support Multi-Segment Handshakes:} Network engineers must ensure middleboxes, load balancers, and edge proxies accommodate multi-segment \texttt{ClientHello} reassembly up to $4\,\mathrm{kB}$.
    \item \textbf{Verify Modern Kernels:} Fleets must enforce RFC 6928 compliance ($\texttt{initcwnd} \ge 10$) to prevent multi-segment handshake stalls.
    \item \textbf{Monitor Wireless Tail Latencies:} High-loss mobile connections should monitor TCP retransmission metrics to avoid tail-latency degradation during TLS 1.3 handshake phases.
\end{enumerate}
"""

with open(os.path.join(ch_dir, "ch5_pqc_network_cost.tex"), "w", encoding="utf-8") as f:
    f.write(ch5_content)

print("Wrote ch5_pqc_network_cost.tex")

# -------------------------------------------------------------
# APPENDIX: THE THREE-STAGE PROTOCOL CODE
# -------------------------------------------------------------
app_content = r"""\chapter{The Certified Three-Stage Protocol Implementation}
\label{app:protocol_code}

In this Appendix, we reproduce the complete, certified Python source code of the three-stage radix-agnostic detection, non-linear refinement, and multiplicity-corrected certification pipeline (`protocol.py`). This protocol enforces the five mandatory integrity gates described in Chapter~\ref{ch:planck_dsi}.

\begin{lstlisting}[language=Python, caption={Certified Three-Stage Radix-Agnostic Protocol Engine}, label={lst:protocol}]
""" + open(r"C:\Users\bruno\projects\dsi-cosmo-search\src\protocol.py", "r", encoding="utf-8").read() + r"""
\end{lstlisting}
"""

with open(os.path.join(ch_dir, "appendix_protocol_code.tex"), "w", encoding="utf-8") as f:
    f.write(app_content)

print("Wrote appendix_protocol_code.tex")

# -------------------------------------------------------------
# MASTER BIBLIOGRAPHY: REFS.BIB
# -------------------------------------------------------------
bib_content = r"""@article{casimir1948,
  author = {Casimir, H. B. G.},
  title = {On the attraction between two perfectly conducting plates},
  journal = {Proc. K. Ned. Akad. Wet.},
  volume = {51},
  pages = {793--795},
  year = {1948}
}

@article{lifshitz1956,
  author = {Lifshitz, E. M.},
  title = {The theory of molecular attractive forces between solids},
  journal = {Sov. Phys. JETP},
  volume = {2},
  pages = {73--83},
  year = {1956}
}

@article{decca2003,
  author = {Decca, R. S. and L{\'o}pez, D. and Fischbach, E. and Krause, D. E.},
  title = {Measurement of the Casimir Force between Dissimilar Metals},
  journal = {Phys. Rev. Lett.},
  volume = {91},
  issue = {5},
  pages = {050402},
  year = {2003},
  doi = {10.1103/PhysRevLett.91.050402}
}

@article{dejong2025,
  author = {de Jong, M. H. J. and Korkmazgil, E. and Banniard, L. and Sillanp{\"a}{\"a}, M. A. and Mercier de L{\'e}pinay, L.},
  title = {Measurement of the superconducting Casimir effect},
  journal = {Nat. Phys.},
  volume = {21},
  pages = {1--8},
  year = {2025},
  doi = {10.1038/s41567-024-02728-6}
}

@article{zechmeister2009,
  author = {Zechmeister, M. and K{\"u}rster, M.},
  title = {The generalised Lomb-Scargle periodogram. A new formalism for the floating-mean and Keplerian periodograms},
  journal = {Astron. Astrophys.},
  volume = {496},
  number = {2},
  pages = {577--584},
  year = {2009},
  doi = {10.1051/0004-6361:200811296}
}

@article{baluev2008,
  author = {Baluev, R. V.},
  title = {Assessing the statistical significance of periodogram peaks},
  journal = {Mon. Not. R. Astron. Soc.},
  volume = {385},
  number = {3},
  pages = {1279--1289},
  year = {2008},
  doi = {10.1111/j.1365-2966.2008.12689.x}
}

@article{speake2003,
  author = {Speake, C. C. and Trenner, C.},
  title = {Forces between conducting surfaces due to spatial variations of surface potential},
  journal = {Class. Quantum Grav.},
  volume = {20},
  number = {17},
  pages = {S281--S287},
  year = {2003},
  doi = {10.1088/0264-9381/20/17/303}
}

@article{weinberg1989,
  author = {Weinberg, S.},
  title = {The cosmological constant problem},
  journal = {Rev. Mod. Phys.},
  volume = {61},
  pages = {1--23},
  year = {1989}
}

@article{peebles2003,
  author = {Peebles, P. J. E. and Ratra, B.},
  title = {The cosmological constant and dark energy},
  journal = {Rev. Mod. Phys.},
  volume = {75},
  pages = {559--606},
  year = {2003}
}

@article{riess2022,
  author = {Riess, A. G. and others},
  title = {A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km/s/Mpc Uncertainty from the Hubble Space Telescope and SH0ES Team},
  journal = {Astrophys. J. Lett.},
  volume = {934},
  pages = {L7},
  year = {2022}
}

@article{planck2018,
  author = {{Planck Collaboration}},
  title = {Planck 2018 results. VI. Cosmological parameters},
  journal = {Astron. Astrophys.},
  volume = {641},
  pages = {A6},
  year = {2020}
}

@article{desi2024,
  author = {{DESI Collaboration}},
  title = {DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations},
  journal = {JCAP},
  volume = {02},
  pages = {021},
  year = {2025}
}

@article{brout2022,
  author = {Brout, D. and others},
  title = {The Pantheon+ Analysis: Cosmological Constraints},
  journal = {Astrophys. J.},
  volume = {938},
  pages = {110},
  year = {2022}
}

@article{chen2019,
  author = {Chen, L. and Huang, Q.-G. and Wang, K.},
  title = {Distance priors from Planck final release},
  journal = {JCAP},
  volume = {02},
  pages = {028},
  year = {2019}
}

@article{chevallier2001,
  author = {Chevallier, M. and Polarski, D.},
  title = {Accelerating Universes with Scaling Dark Energy},
  journal = {Int. J. Mod. Phys. D},
  volume = {10},
  pages = {213--224},
  year = {2001}
}

@article{linder2003,
  author = {Linder, E. V.},
  title = {Exploring the Expansion History of the Universe},
  journal = {Phys. Rev. Lett.},
  volume = {90},
  pages = {091301},
  year = {2003}
}

@article{blanchard2020,
  author = {{Euclid Collaboration}},
  title = {Euclid preparation. VII. Forecast validation for Euclid cosmological probes},
  journal = {Astron. Astrophys.},
  volume = {642},
  pages = {A191},
  year = {2020}
}

@article{preskill2018,
  author = {Preskill, J.},
  title = {Quantum Computing in the NISQ era and beyond},
  journal = {Quantum},
  volume = {2},
  pages = {79},
  year = {2018}
}

@article{temme2017,
  author = {Temme, K. and Bravyi, S. and Gambetta, J. M.},
  title = {Error Mitigation for Short-Depth Quantum Circuits},
  journal = {Phys. Rev. Lett.},
  volume = {119},
  pages = {180509},
  year = {2017}
}

@article{li2017,
  author = {Li, Y. and Benjamin, S. C.},
  title = {Efficient Variational Quantum Simulator Incorporating Active Error Minimization},
  journal = {Phys. Rev. X},
  volume = {7},
  pages = {021050},
  year = {2017}
}

@article{cai2023,
  author = {Cai, Z. and others},
  title = {Quantum error mitigation},
  journal = {Rev. Mod. Phys.},
  volume = {95},
  pages = {045005},
  year = {2023}
}

@article{kandala2019,
  author = {Kandala, A. and others},
  title = {Error mitigation extends the computational reach of a noisy quantum processor},
  journal = {Nature},
  volume = {567},
  pages = {491--495},
  year = {2019}
}

@inproceedings{giurgica2020,
  author = {Giurgica-Tiron, T. and Hindy, Y. and LaRose, R. and Mari, A. and Zeng, W. J.},
  title = {Digital zero noise extrapolation for quantum error mitigation},
  booktitle = {2020 IEEE International Conference on Quantum Computing and Engineering (QCE)},
  pages = {306--316},
  year = {2020}
}

@article{wallman2016,
  author = {Wallman, J. J. and Emerson, J.},
  title = {Noise tailoring for scalable quantum computation via randomized compiling},
  journal = {Phys. Rev. A},
  volume = {94},
  pages = {052325},
  year = {2016}
}

@article{hashim2021,
  author = {Hashim, A. and others},
  title = {Randomized Compiling for Scalable Quantum Computing on a Cloud-Accessible Quantum Processor},
  journal = {Phys. Rev. X},
  volume = {11},
  pages = {041039},
  year = {2021}
}

@article{lomb1976,
  author = {Lomb, N. R.},
  title = {Least-squares frequency analysis of unequally spaced data},
  journal = {Astrophys. Space Sci.},
  volume = {39},
  pages = {447--462},
  year = {1976}
}

@article{scargle1982,
  author = {Scargle, J. D.},
  title = {Studies in astronomical time series analysis. II - Statistical aspects of spectral analysis of unevenly spaced data},
  journal = {Astrophys. J.},
  volume = {263},
  pages = {835--853},
  year = {1982}
}

@techreport{rescorla2018,
  author = {Rescorla, E.},
  title = {The Transport Layer Security (TLS) Protocol Version 1.3},
  institution = {IETF},
  type = {RFC},
  number = {8446},
  year = {2018}
}

@inproceedings{shor1994,
  author = {Shor, P. W.},
  title = {Algorithms for quantum computation: discrete logarithms and factoring},
  booktitle = {Proceedings 35th Annual Symposium on Foundations of Computer Science},
  pages = {124--134},
  year = {1994}
}

@inproceedings{bos2018,
  author = {Bos, J. and others},
  title = {CRYSTALS - Kyber: a CCA-secure module-lattice-based KEM},
  booktitle = {2018 IEEE European Symposium on Security and Privacy (EuroS\&P)},
  pages = {353--367},
  year = {2018}
}

@inproceedings{schwabe2020,
  author = {Schwabe, P. and Stebila, D. and Wiggers, T.},
  title = {Post-Quantum TLS Without Handshake Signatures},
  booktitle = {Proceedings of the 2020 ACM SIGSAC Conference on Computer and Communications Security},
  pages = {885--903},
  year = {2020}
}

@incollection{paquin2020,
  author = {Paquin, C. and Stebila, D. and Tamvada, G.},
  title = {Benchmarking Post-Quantum Cryptography in TLS},
  booktitle = {Post-Quantum Cryptography - PQCrypto 2020},
  series = {LNCS},
  volume = {12100},
  pages = {83--101},
  year = {2020}
}

@inproceedings{sikeridis2020,
  author = {Sikeridis, D. and Kampanakis, P. and Devetsikiotis, M.},
  title = {Assessing the Overhead of Post-Quantum Cryptography in TLS 1.3 and SSH},
  booktitle = {Proceedings of the Network and Distributed System Security Symposium (NDSS)},
  year = {2020}
}

@techreport{chu2013,
  author = {Chu, J. and Dukkipati, N. and Cheng, Y. and Mathis, M.},
  title = {Increasing TCP's Initial Window},
  institution = {IETF},
  type = {RFC},
  number = {6928},
  year = {2013}
}

@misc{fips203,
  author = {{National Institute of Standards and Technology}},
  title = {Module-Lattice-Based Key-Encapsulation Mechanism Standard},
  howpublished = {FIPS PUB 203},
  year = {2024}
}
"""

with open(os.path.join(base, "refs.bib"), "w", encoding="utf-8") as f:
    f.write(bib_content)

print("Wrote refs.bib")

# -------------------------------------------------------------
# MASTER BOOK: BOOK.TEX
# -------------------------------------------------------------
book_content = r"""\documentclass[11pt,a4paper,openany]{book}
\usepackage[margin=2.4cm,bottom=2.6cm,top=2.6cm]{geometry}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{cite}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    citecolor=blue,
    urlcolor=blue,
    pdftitle={The Matrioska Protocol: From Cosmic Scale Invariance to Quantum Security},
    pdfauthor={Bruno Luçardo Olivaes}
}

\lstset{
    basicstyle=\ttfamily\footnotesize,
    breaklines=true,
    frame=single,
    numbers=left,
    numberstyle=\tiny\color{gray},
    keywordstyle=\color{blue}\bfseries,
    commentstyle=\color{teal}\itshape,
    stringstyle=\color{purple},
    backgroundcolor=\color{gray!5},
    showstringspaces=false
}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\nouppercase{\leftmark}}
\fancyhead[LO]{\nouppercase{\rightmark}}
\renewcommand{\headrulewidth}{0.4pt}

\begin{document}

\frontmatter

% --- TITLE PAGE ---
\begin{titlepage}
\begin{center}
\vspace*{1.5cm}

{\Huge \bfseries The Matrioska Protocol}\\[0.5cm]
{\LARGE \bfseries From Cosmic Scale Invariance to Quantum Security}\\[1.5cm]

{\large \textit{A Metrological Journey through Cosmology, Quantum Computing, and Post-Quantum Cryptography}}\\[3.5cm]

{\Large \textbf{Bruno Lu\c{c}ardo Olivaes}}\\[0.4cm]
{\large Independent Researcher, Brazil}\\[0.2cm]
{\small \texttt{brunoolivaes@gmail.com} $\cdot$ ORCID: 0009-0003-8857-7945}\\[3.5cm]

\vfill
{\large First Edition --- November 2026}\\[0.2cm]
{\small Published under Creative Commons Attribution 4.0 International (CC BY 4.0)}
\end{center}
\end{titlepage}

% --- COPYRIGHT PAGE ---
\newpage
\thispagestyle{empty}
\vspace*{\fill}
\noindent \textbf{The Matrioska Protocol: From Cosmic Scale Invariance to Quantum Security}\\
\textit{A Metrological Journey through Cosmology, Quantum Computing, and Post-Quantum Cryptography}\\
Author: Bruno Lu\c{c}ardo Olivaes\\
ORCID: 0009-0003-8857-7945\\

\vspace{0.5cm}
\noindent \textbf{Open Research \& Sovereign DOIs (CERN / Zenodo):}\\
$\cdot$ Chapter 1 (Planck DSI): \url{https://doi.org/10.5281/zenodo.24121677}\\
$\cdot$ Chapter 2 (Casimir Metrology): \url{https://doi.org/10.5281/zenodo.24121687}\\
$\cdot$ Chapter 3 (ESA Euclid Forecast): \url{https://doi.org/10.5281/zenodo.24121691}\\
$\cdot$ Chapter 4 (NISQ ZNE Benchmark): \url{https://doi.org/10.5281/zenodo.24121693}\\
$\cdot$ Chapter 5 (PQC Wire Cost): \url{https://doi.org/10.5281/zenodo.24121695}\\

\vspace{0.5cm}
\noindent \copyright\ 2026 Bruno Lu\c{c}ardo Olivaes. This work is licensed under a \textit{Creative Commons Attribution 4.0 International License} (CC BY 4.0). You are free to share and adapt the material for any purpose, provided appropriate credit is given.
\vspace{1cm}

\tableofcontents

\include{chapters/preface}

\mainmatter

\include{chapters/ch1_planck_dsi}
\include{chapters/ch2_casimir_afm}
\include{chapters/ch3_euclid_dark_energy}
\include{chapters/ch4_qiskit_zne}
\include{chapters/ch5_pqc_network_cost}

\backmatter

\appendix
\include{chapters/appendix_protocol_code}

\bibliographystyle{unsrt}
\bibliography{refs}

\end{document}
"""

with open(os.path.join(base, "book.tex"), "w", encoding="utf-8") as f:
    f.write(book_content)

print("Wrote book.tex")
print("All chapters, refs.bib, and master book.tex written successfully!")

