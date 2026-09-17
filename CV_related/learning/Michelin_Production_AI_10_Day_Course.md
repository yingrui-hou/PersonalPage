# Michelin Mission - Production AI 10-Day Intensive Course

## Course Positioning

This course is designed for a scientific data scientist who already knows Python, statistical modelling, validation, monitoring, and Linux-based collaborative workflows, but lacks direct enterprise production experience.

Duration: **10 working days, 3-5 focused hours per day**  
Capstone: **Industrial predictive-maintenance inference service**  
Dataset: [UCI AI4I 2020 Predictive Maintenance](https://archive.ics.uci.edu/dataset/601/ai4i)  
Stack: Python, scikit-learn, FastAPI, Pydantic, pytest, Docker, Docker Compose, GitHub Actions, Prometheus, Grafana, MLflow

The realistic outcome is a production-style portfolio project and operational vocabulary. It does not replace experience operating a real enterprise service under Michelin's internal standards.

## Learning Outcomes

By the end of the course, the learner can:

- Explain the difference between a trained model, an inference application, and an operated AI service.
- expose a versioned ML model through a validated REST API and a batch interface;
- package the service and its dependencies in an immutable Docker image;
- implement unit, integration, contract, smoke, and model-behaviour tests;
- build a CI/CD pipeline that tests, builds, scans, tags, and promotes an image;
- emit structured logs and Prometheus service/model metrics;
- configure Grafana dashboards and actionable alert rules;
- version code, model, data schema, and configuration independently;
- deploy a new model version and roll back safely to the previous version;
- write technical documentation, a user guide, a runbook, and a rollback procedure;
- explain the limits of monitoring when labels arrive late or never arrive.

## Production AI in One Page

A notebook that produces a good score is not a production AI system. A production system is a controlled chain:

```text
Business need
  -> measurable decision and acceptance criteria
  -> governed data contract
  -> reproducible training pipeline
  -> validated model artifact
  -> versioned inference interface
  -> tested container image
  -> controlled deployment
  -> logs, metrics, dashboards and alerts
  -> incident response and rollback
  -> feedback, reassessment and retraining
```

Production quality has several independent dimensions:

- **Model quality:** predictive performance, calibration, robustness, uncertainty, subgroup behaviour.
- **Data quality:** schema, missing values, ranges, units, freshness, lineage, and distribution shift.
- **Software quality:** tests, modularity, dependency control, security, reproducible builds, API compatibility.
- **Service quality:** availability, latency, throughput, resource usage, graceful failure, recovery.
- **Operational quality:** ownership, dashboards, alerts, runbooks, deployment approvals, rollback and incident review.
- **Business quality:** the output is usable, documented, understood, and connected to a real decision or BI workflow.

For the Michelin mission, the critical insight is that model monitoring is only one part of operability. The team must also know whether the service is reachable, whether inputs remain valid, which model produced each prediction, what changed during deployment, and how to recover.

## Capstone Architecture

```text
Client / Data Engineer / BI pipeline
                |
                v
       FastAPI inference service
       /v1/predict
       /health/live
       /health/ready
       /metrics
          |             |
          v             v
   versioned model   JSON logs
   + preprocessing   + request IDs
          |
          v
   Prometheus -> Grafana -> alerts

Git push -> CI tests -> Docker build -> immutable image tag
         -> staging smoke test -> manual promotion -> production
                                      |
                                      v
                            rollback to previous image/model
```

## Repository Target

```text
industrial-ai-service/
  app/
    api.py
    schemas.py
    inference.py
    settings.py
    logging_config.py
    metrics.py
  model/
    train.py
    evaluate.py
    registry.py
  tests/
    unit/
    integration/
    contract/
  monitoring/
    prometheus.yml
    alerts.yml
    grafana/
  deploy/
    compose.yaml
    compose.staging.yaml
    rollback.sh
  docs/
    architecture.md
    model_card.md
    user_guide.md
    runbook.md
    rollback.md
  .github/workflows/ci.yml
  Dockerfile
  Makefile
  pyproject.toml
  README.md
```

## Week 1 - Build a Deployable Service

### Day 1 - From Model to Production Contract

Theory:

- Separate training code, model artifact, preprocessing, inference logic, and delivery interface.
- Define the business event: predict machine failure risk from sensor/process variables.
- Define the consumer: Data Engineer or BI pipeline, not a notebook user.
- Define model, feature-schema, API, and configuration versions.

Lab:

- Train a small scikit-learn baseline on the AI4I dataset.
- Persist the complete preprocessing-plus-model pipeline, not only the estimator.
- Record training code commit, feature names, expected units, metrics, and dependency versions.
- Write a model card with intended use, limitations, threshold, and known failure modes.

Deliverable:

- `model.joblib`, `model_card.md`, `input_schema.json`, and a reproducible training command.

Definition of done:

- A clean checkout can reproduce the artifact and evaluation within an explicitly documented tolerance.

### Day 2 - FastAPI and Interface Design

Theory:

- REST and JSON basics: methods, status codes, idempotency, timeouts, validation, compatibility.
- Difference between liveness and readiness.
- Why `/v1/predict` is safer than an unversioned `/predict` contract.
- Online inference versus batch inference and when BI integration prefers batch outputs.

Lab:

- Implement `POST /v1/predict` with Pydantic request and response schemas.
- Add `/health/live`, `/health/ready`, `/version`, and `/metrics`.
- Return `prediction`, `score`, `threshold`, `model_version`, and `schema_version`.
- Reject missing, extra, invalid, or out-of-range inputs with stable error responses.
- Add a batch CSV/Parquet command that uses the same inference core as the API.

Deliverable:

- Working interactive API documentation and example requests/responses for Data Engineers.

Definition of done:

- Invalid inputs fail explicitly; valid API and batch predictions are identical.

### Day 3 - Testing and Quality Gates

Theory:

- Unit tests validate isolated logic.
- Integration tests validate model loading plus API behaviour.
- Contract tests protect downstream consumers.
- Smoke tests answer whether the deployed service can perform one safe prediction.
- Model-behaviour tests check more than software correctness.

Lab:

- Test preprocessing, prediction shape, error handling, health endpoints, and API schema.
- Add a fixed golden dataset and expected predictions with numerical tolerances.
- Add behaviour checks for score range, missing features, extreme values, and deterministic output.
- Set minimum coverage for critical modules, without chasing 100% coverage.

Deliverable:

- Automated `pytest` suite and one-command `make test`.

Definition of done:

- Tests fail if a feature is renamed, preprocessing changes silently, or model output becomes incompatible.

### Day 4 - Containerisation with Docker

Theory:

- Image versus container; immutable artifact versus runtime instance.
- Build context, layers, cache, non-root users, dependency pinning, and small base images.
- Environment variables for configuration; never bake secrets into an image.
- Docker health checks and graceful shutdown.

Lab:

- Write a multi-stage or otherwise minimal Dockerfile based on an official Python image.
- Run the application as a non-root user.
- Add health checks and resource-conscious server settings.
- Build and run with a version tag based on the Git commit SHA.
- Create Docker Compose services for API, Prometheus, and Grafana.

Deliverable:

- `docker compose up` starts a locally observable stack from a clean machine.

Definition of done:

- The image contains no source-time secrets, health checks pass, and the exact image is reproducible from a tagged commit.

### Day 5 - Continuous Integration

Theory:

- CI validates every change; CD promotes an already validated immutable artifact.
- Quality gates: formatting, linting, tests, dependency checks, image build, image scan, smoke test.
- Branch protection, pull requests, approvals, protected environments, and secrets.

Lab:

- Create a GitHub Actions workflow; document how each stage maps to GitLab CI.
- On pull requests: install, lint, test, build image, start container, run smoke test.
- On version tags: generate metadata, tag the image with semantic version and Git SHA, and publish to a registry.
- Save test reports and build metadata as artifacts.

Deliverable:

- A failed test blocks the image publication and a successful tagged build produces an immutable image.

Definition of done:

- No deployment step rebuilds the application; staging and production use the same image digest.

## Week 2 - Operate, Monitor and Recover

### Day 6 - Controlled Deployment and Version Management

Theory:

- Dev, staging, and production are separate environments with separate controls.
- Code version, image version, model version, schema version, and configuration version are related but not identical.
- Mutable `latest` tags make incidents difficult to diagnose.
- Promotion, not rebuilding, moves an artifact between environments.

Lab:

- Register at least two model versions in MLflow.
- Use aliases such as `candidate` and `champion` rather than deprecated fixed stages.
- Deploy version 1 to a staging Compose environment, run smoke and contract tests, then promote it.
- Record a deployment manifest containing image digest, model version, schema version, commit, date, and approver.

Deliverable:

- A deployment record that answers exactly what code and model are running.

Definition of done:

- A prediction response, log line, and metric can all be linked to the same model and service version.

### Day 7 - Structured Logging and Service Metrics

Theory:

- Logs describe discrete events; metrics describe aggregate numerical behaviour; traces connect distributed calls.
- Logs must be machine-readable and useful during an incident.
- Do not log sensitive raw inputs by default.
- The basic service signals are traffic, errors, latency, and saturation.

Lab:

- Emit JSON logs with timestamp, severity, service, environment, request ID, endpoint, status, latency, model version, and schema version.
- Propagate or generate a request ID and return it to the caller.
- Expose Prometheus counters, gauges, and histograms.
- Record request count, error count, latency histogram, in-flight requests, schema rejection count, and prediction count.

Deliverable:

- Given one failed request ID, the relevant log event and deployed version can be identified in under two minutes.

Definition of done:

- Logs avoid raw sensor payloads and metrics avoid high-cardinality identifiers such as request IDs.

### Day 8 - AI Monitoring and Alerting

Theory:

Monitoring layers:

- **Service:** availability, error rate, latency, throughput, memory and CPU.
- **Data:** schema failures, missing values, range violations, freshness, feature distribution shift.
- **Model:** score distribution, predicted-positive rate, confidence, calibration, delayed performance.
- **Business:** alert usefulness, inspection yield, false-alarm cost, avoided downtime.

Lab:

- Create Grafana panels for request rate, error rate, p50/p95 latency, schema failures, score distribution, and predicted failure rate.
- Establish a reference feature distribution and calculate a simple drift indicator for selected features.
- Create actionable alerts with severity, owner, summary, impact, and runbook link.
- Add a simulated drift endpoint or replay script to demonstrate the alert.

Initial training thresholds, to be tuned rather than copied blindly:

- API 5xx rate above 2% for 5 minutes.
- p95 latency above the agreed service objective for 10 minutes.
- readiness failing for more than 2 evaluation intervals.
- schema rejection rate significantly above its recent baseline.
- selected feature drift above the validated threshold for two consecutive windows.
- prediction-rate shift large enough to affect the downstream BI process.

Deliverable:

- Dashboard, alert rules, and evidence that a controlled fault triggers and resolves an alert.

Definition of done:

- Every alert states who acts, what to check, and when escalation is required.

### Day 9 - Rollback, Reliability and Service Operations

Theory:

- Rollback is a designed capability, not an emergency improvisation.
- Application rollback and model rollback may be independent.
- Rollback is unsafe when schemas or stateful dependencies are not backward-compatible.
- Runbooks reduce recovery time and make knowledge transferable.

Lab:

- Deploy a deliberately degraded model or faulty API image to staging.
- Detect the regression through smoke tests or monitoring.
- Reassign the MLflow `champion` alias to the previous model when only the model is faulty.
- Re-deploy the previous immutable image digest when application code is faulty.
- Verify health, contract compatibility, and core metrics after rollback.
- Write a runbook with symptom, impact, diagnosis, mitigation, rollback, verification, escalation, and follow-up.

Optional advanced exercise:

- Deploy to a local Kubernetes cluster and practise rollout history and `kubectl rollout undo`.

Deliverable:

- Timed incident report showing detection time, decision, rollback command, recovery verification, and root cause.

Definition of done:

- Recovery does not require editing source code or rebuilding an old release.

### Day 10 - Operational Handover and Michelin-Style Demo

Theory:

- A service is not supportable if only its author understands it.
- Documentation must serve developers, operators, Data Engineers, BI users, and model users differently.
- Production readiness requires explicit ownership and acceptance, not only technical completion.

Lab:

- Write an architecture decision record explaining the selected deployment and monitoring approach.
- Complete the technical documentation, functional description, API contract, user guide, configuration guide, runbook, and rollback guide.
- Define an SLO, for example availability and p95 latency, plus exclusions and measurement window.
- Record a 10-minute demonstration: normal prediction, BI-ready output, dashboard, drift injection, alert, rollback, and recovery.
- Conduct a post-incident review without blame: timeline, impact, root cause, contributing factors, corrective actions, and owners.

Deliverable:

- A recruiter-ready repository and demonstration aligned with the Michelin mission deliverables.

Definition of done:

- Another technical user can start, test, monitor, configure, and roll back the service using documentation only.

## Minimum Production-Readiness Checklist

### Interface

- Versioned API and batch contract.
- Explicit schemas, units, ranges, error responses, and compatibility policy.
- Liveness, readiness, version, and metrics endpoints.
- Timeouts, bounded payloads, and graceful failure.

### Model and Data

- Model artifact includes preprocessing and input signature.
- Training data/reference metadata and evaluation are recorded.
- Model limitations and decision threshold are documented.
- Drift detection has a reference window, threshold, owner, and response.

### Build and Release

- Dependencies are pinned and builds are reproducible.
- Tests and image scan run in CI.
- Images use semantic and Git SHA tags plus immutable digests.
- Staging smoke tests pass before controlled production promotion.
- The deployment manifest records code, image, model, schema, and configuration versions.

### Observability and Operations

- Structured logs include request and version context without sensitive payloads.
- Service, data, model, and business metrics are separated.
- Alerts are actionable and linked to runbooks.
- Ownership, SLO, escalation, backup, recovery, and rollback are documented.
- A rollback drill has been completed and timed.

## What to Say in an Interview After Completion

Credible wording:

> My previous work already covered model validation, dataset shift, anomaly diagnosis, reproducible workflows, and shared Linux codebases. To close the deployment gap, I built a production-style industrial AI service with a versioned FastAPI contract, Docker packaging, CI quality gates, structured logging, Prometheus/Grafana monitoring, MLflow model versioning, and a tested rollback procedure. This is a portfolio environment rather than enterprise production, so I would still need a short onboarding period to learn Michelin's internal platform, security, operability, and support standards.

Do not claim:

- enterprise production ownership;
- on-call experience that did not occur;
- Michelin internal tooling knowledge;
- production-scale traffic or reliability figures that were only simulated;
- industrial business impact that the synthetic dataset cannot demonstrate.

## Recommended Official References

- [FastAPI in Containers](https://fastapi.tiangolo.com/deployment/docker/)
- [pytest Getting Started](https://docs.pytest.org/en/stable/getting-started.html)
- [Docker Build with GitHub Actions](https://docs.docker.com/build/ci/github-actions/)
- [GitHub Actions deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments)
- [Prometheus overview](https://prometheus.io/docs/introduction/overview/)
- [Prometheus client-library instrumentation guidance](https://prometheus.io/docs/instrumenting/writing_clientlibs/)
- [Grafana Alerting](https://grafana.com/docs/grafana/latest/alerting/)
- [MLflow Model Registry workflows](https://mlflow.org/docs/latest/ml/model-registry/workflow)
- [MLflow model serving](https://mlflow.org/docs/latest/ml/deployment)
- [Kubernetes rolling updates and rollback](https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/)
