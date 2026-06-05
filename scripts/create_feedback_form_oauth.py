#!/usr/bin/env python3
"""Create feedback Google Form using your own Google login (OAuth). No domain-wide delegation."""

from __future__ import annotations

import sys
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from create_feedback_form import (
    FORM_DESCRIPTION,
    FORM_TITLE,
    ITEMS,
    SCOPES,
    build_create_requests,
)

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CLIENT = ROOT / "config" / "gcp-oauth.keys.json"
TOKEN_PATH = ROOT / "config" / "google-forms-oauth-token.json"


def get_user_credentials(client_secrets: Path) -> Credentials:
    creds = None
    if TOKEN_PATH.is_file():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    elif not creds or not creds.valid:
        if not client_secrets.is_file():
            print(
                f"找不到 OAuth 設定檔：{client_secrets}\n"
                "請在 GCP 建立 Desktop OAuth client，下載 JSON 到 config/gcp-oauth.keys.json\n"
                "詳見 handouts/10-google-forms-service-account-setup.md（Plan B）",
                file=sys.stderr,
            )
            sys.exit(1)
        flow = InstalledAppFlow.from_client_secrets_file(str(client_secrets), SCOPES)
        creds = flow.run_local_server(port=0, prompt="consent")
        TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")
        print(f"已儲存登入 token：{TOKEN_PATH}")
    return creds


def main() -> None:
    import os

    client = Path(os.environ.get("GOOGLE_OAUTH_CLIENT_SECRETS", DEFAULT_CLIENT))
    creds = get_user_credentials(client)
    forms = build("forms", "v1", credentials=creds, static_discovery=False)

    created = (
        forms.forms()
        .create(body={"info": {"title": FORM_TITLE, "documentTitle": FORM_TITLE}})
        .execute()
    )
    form_id = created["formId"]

    forms.forms().batchUpdate(
        formId=form_id,
        body={
            "requests": [
                {
                    "updateFormInfo": {
                        "info": {"description": FORM_DESCRIPTION},
                        "updateMask": "description",
                    }
                },
                *build_create_requests(ITEMS),
                {
                    "updateSettings": {
                        "settings": {"emailCollectionType": "DO_NOT_COLLECT"},
                        "updateMask": "emailCollectionType",
                    }
                },
            ]
        },
    ).execute()

    result = forms.forms().get(formId=form_id).execute()
    print("\n=== 問卷已建立（OAuth，你本人帳戶）===")
    print(f"填寫連結：{result.get('responderUri', '')}")
    print(f"編輯連結：https://docs.google.com/forms/d/{form_id}/edit")
    print("\n請到編輯連結 → Settings → 開啟「Limit to 1 response」→ Send → 短連結。")


if __name__ == "__main__":
    main()
