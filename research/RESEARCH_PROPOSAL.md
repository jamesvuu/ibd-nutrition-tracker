# Research proposal (not a completed research paper)

**Title:** Does Dietary Information Improve Machine Learning Classification of Inflammatory Bowel Disease Activity? A Longitudinal Analysis of Ulcerative Colitis and Crohn's Disease

**Status:** Public research proposal / planned observational analysis. **No data analysis has been completed, no results have been generated, and this document has not undergone peer review.**

**Date:** October 16, 2026

## Research question

Among patients with ulcerative colitis (UC) and Crohn's disease (CD), does the addition of dietary questionnaire information improve classification of **contemporaneous symptom-based disease activity** compared with models relying on nondietary clinical characteristics alone?

This is not a study of the effects of diet on future flare risk, and it cannot establish that specific foods cause or prevent inflammation.

## Rationale

Inflammatory bowel disease has heterogeneous symptom trajectories. Longitudinal data provide an opportunity to study whether dietary self-reports contain incremental information about clinical symptom activity. The Integrative Human Microbiome Project (HMP2) followed 132 participants across approximately one year and generated longitudinal clinical and molecular measurements [1]. Publicly listed IBDMDB data products provide a starting point for a secondary analysis [2].

The **availability of diet-and-outcome matched records has not yet been verified by a direct file-level audit**. No claim of adequate sample size, new findings, or predictive performance is made here.

## Primary hypothesis

Adding eligible dietary predictors to nondietary clinical predictors may improve discrimination between active and inactive symptom-based disease activity, measured by a patient-grouped held-out AUROC comparison. The null hypothesis is no improvement.

## Data source and feasibility checkpoint

The intended data source is the **Inflammatory Bowel Disease Multi'omics Database (IBDMDB)** associated with HMP2 [1,2]. Before model development, the project will:

1. Download and inspect the actual metadata files and any dietary questionnaire tables, subject to applicable access and reuse terms.
2. Verify field definitions and participant IDs; identify diagnosis, sampling dates, validated symptom-activity variables, candidate clinical predictors, and dietary fields.
3. Count independent UC/CD participants, eligible visit-level records, active/remission outcomes, and diet-matched records; quantify missingness.
4. Determine whether enough independent participants and outcome events remain for a defensible modeling analysis. If not, revise the research question or report a feasibility study without fitted prediction models.

Exact names of dietary predictors, eligible sample sizes, and final outcome thresholds will be finalized after the audit against relevant clinical references and the data dictionary.

## Proposed methods

**Design:** Secondary, observational, longitudinal data analysis.

**Population:** Eligible UC and CD participants with usable symptom-activity data. Healthy controls are not part of the primary UC-versus-CD disease-activity analysis.

**Outcome:** Concurrent symptom-based disease activity, based on documented HBI for CD and SCCAI for UC, if available at the matching time points. A pre-specified threshold will be justified from clinical literature and locked before outcome modeling. Symptom scores are not equivalent to endoscopic or biomarker-confirmed inflammation.

**Predictors:** Two matched feature sets: (A) eligible nondietary clinical characteristics and (B) those identical clinical characteristics plus dietary questionnaire features. Exclude the outcome score and all direct outcome components from predictors to prevent target leakage. Record whether clinical measures precede or coincide with dietary reporting.

**Models:** Regularized logistic regression as a primary, relatively interpretable baseline, with random forest as a secondary nonlinear comparison. Model complexity and number of features will be constrained by the number of independent patients.

**Validation:** Keep every record from an individual participant in the same partition. Use patient-grouped cross-validation with any preprocessing, imputation, encoding, scaling, feature reduction, and hyperparameter tuning performed within training folds. Prefer nested grouped validation if sample size permits; otherwise make clear that conclusions are exploratory.

**Metrics:** Primary: paired difference in AUROC for diet-inclusive versus nondietary models. Secondary: sensitivity, specificity, PR-AUC, F1, and calibration where feasible. Report confidence intervals using patient-level resampling if the number of participants supports it.

**Subgroups:** Evaluate UC and CD separately first. Any pooled analysis must handle disease-specific outcome scales and diagnosis differences explicitly; report it as secondary.

**Sensitivity analyses:** Assess different clinically defensible activity thresholds, missing-data assumptions, temporal matching windows, and the effect of complete-case selection.

## Limitations and safeguards

Self-reported diet is susceptible to recall and measurement error, and patients may change what they eat *because* of symptoms (reverse causation). Repeated visits do not substitute for independent patients. Clinical indices represent symptom activity, not confirmed inflammatory severity. The small cohort may lead to unstable estimates; no clinical deployment or treatment recommendation is intended.

Before public release of any subject-level data, verify that source terms permit redistribution and that the records are appropriately protected. This repository does **not** include participant-level data.

## Expected outputs (not yet produced)

- Audited variable dictionary and cohort flow summary
- Reproducible Python preprocessing and grouped model-training scripts
- Actual model comparison table with uncertainty
- Completed manuscript separating Results from Discussion
- Transparent reporting guided by TRIPOD+AI [3]

## References

1. Lloyd-Price J, Arze C, Ananthakrishnan AN, et al. Multi-omics of the gut microbial ecosystem in inflammatory bowel diseases. *Nature*. 2019;569:655–662. https://doi.org/10.1038/s41586-019-1237-9
2. IBDMDB. HMP2 results and metadata downloads. https://www.ibdmdb.org/results
3. Collins GS, Moons KGM, Dhiman P, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. *BMJ*. 2024;385:e078378. https://doi.org/10.1136/bmj-2023-078378

---

**Publication note:** Making this proposal publicly accessible on GitHub is *not* publication of completed original findings, a journal submission, or peer review. The proposed experiments and manuscript are future work.
