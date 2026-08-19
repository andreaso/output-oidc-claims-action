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
  uses: andreaso/output-oidc-claims-action@main
```

[1]: https://docs.github.com/en/actions/concepts/security/openid-connect
