# Output OIDC Claims Action

This action takes a GitHub Action job's OIDC claims and outputs them
as part of the Job Summary. Can potentially be helpful when debugging
Workload Identity Federation configuration issues.

See [GitHub Docs: OpenID Connect][1] for additional context.


## Example Usage

Temporarily add the following step to the GitHub Actions job that
needs to be debugged.

```YAML
- name: Output OIDC claims
  uses: andreaso/output-oidc-claims-action@bfbd5200fdc3b06bd7a1c5803d9b25f6c83f8bff # v0.2
```

There's also the option to select which claims to output.

```YAML
- name: Output selected OIDC claims
  uses: andreaso/output-oidc-claims-action@bfbd5200fdc3b06bd7a1c5803d9b25f6c83f8bff # v0.2
  with:
    claims: repository, sub
```


## Example Output

```JSON
{
  "actor": "andreaso",
  "actor_id": "285964",
  "aud": "MeadowLark",
  "base_ref": "",
  "check_run_id": "96193868770",
  "event_name": "push",
  "exp": 1787167057,
  "head_ref": "",
  "iat": 1787166757,
  "iss": "https://token.actions.githubusercontent.com",
  "job_workflow_ref": "andreaso/actions-tester/.github/workflows/claims.yaml@refs/heads/test-output-oidc-claims-action",
  "job_workflow_sha": "b8962f4eaff8e14fc646cb22c596c81e67d71362",
  "jti": "1e410ab1-302e-4e33-8c5f-869a4bd12c3b",
  "nbf": 1787166457,
  "ref": "refs/heads/test-output-oidc-claims-action",
  "ref_protected": "false",
  "ref_type": "branch",
  "repository": "andreaso/actions-tester",
  "repository_id": "1339936803",
  "repository_owner": "andreaso",
  "repository_owner_id": "285964",
  "repository_visibility": "private",
  "run_attempt": "1",
  "run_id": "32291736541",
  "run_number": "1",
  "runner_environment": "github-hosted",
  "sha": "b8962f4eaff8e14fc646cb22c596c81e67d71362",
  "sub": "repo:andreaso@285964/actions-tester@1339936803:ref:refs/heads/test-output-oidc-claims-action",
  "workflow": "Test andreaso/output-oidc-claims-action",
  "workflow_ref": "andreaso/actions-tester/.github/workflows/claims.yaml@refs/heads/test-output-oidc-claims-action",
  "workflow_sha": "b8962f4eaff8e14fc646cb22c596c81e67d71362"
}
```

```JSON
{
  "repository": "andreaso/actions-tester",
  "sub": "repo:andreaso@285964/actions-tester@1339936803:ref:refs/heads/test-output-oidc-claims-action"
}
```


[1]: https://docs.github.com/en/actions/concepts/security/openid-connect
