import json
import os

import jwt
import requests


class ActionError(Exception):
    pass


def _set_error_message(title: str, message: str) -> None:
    print(f"::error title={title}::{message}")


def _request_github_jwt() -> str:
    try:
        req_token = os.environ["ACTIONS_ID_TOKEN_REQUEST_TOKEN"]
        req_url = os.environ["ACTIONS_ID_TOKEN_REQUEST_URL"]
    except KeyError as key_error:
        title = "GitHub Actions workflow/job permission error"
        message = "The `id-token: write` permission appear to be missing."
        _set_error_message(title, message)
        raise ActionError(title) from key_error

    full_url = f"{req_url}&audience=MeadowLark"
    headers = {"Authorization": f"Bearer {req_token}"}

    try:
        response = requests.get(full_url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as request_error:
        title = "GitHub Actions JWT token request error"
        message = f"{type(request_error).__name__}: {request_error}"
        _set_error_message(title, message)
        raise ActionError(title) from request_error

    jwt_token: str = response.json()["value"]
    return jwt_token


def _extract_claims(jwt_token: str) -> dict[str, str | int]:
    try:
        claims = jwt.decode(jwt_token, options={"verify_signature": False})
    except jwt.exceptions.DecodeError as decode_error:
        title = "GitHub Actions JWT token decode error"
        message = f"{type(decode_error).__name__}: {decode_error}"
        _set_error_message(title, message)
        raise ActionError(title) from decode_error

    return claims


def main() -> None:
    job_summary = os.getenv("GHA_JOB_SUMMARY", "true").strip()

    jwt_token = _request_github_jwt()
    claims = _extract_claims(jwt_token)
    json_pretty = json.dumps(claims, indent=2)
    json_plain = json.dumps(claims)

    if job_summary.lower() == "true":
        summary = "```JSON\n" + f"{json_pretty}\n" + "```"
        with open(os.environ["GITHUB_STEP_SUMMARY"], mode="a") as gss:
            gss.write(summary)

    with open(os.environ["GITHUB_OUTPUT"], mode="a") as ghof:
        ghof.write(f"claims={json_plain}")

    print(json_pretty)


if __name__ == "__main__":
    main()
