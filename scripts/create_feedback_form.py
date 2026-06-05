#!/usr/bin/env python3
"""Create CHW staff training feedback Google Form via Service Account + Forms API."""

from __future__ import annotations

import os
import sys
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_KEY = ROOT / "config" / "gcp-service-account.json"

SCOPES = [
    "https://www.googleapis.com/auth/forms.body",
    "https://www.googleapis.com/auth/drive",
]

FORM_TITLE = "2026 AI 驅動校園培訓 — 課後回饋問卷"
FORM_DESCRIPTION = (
    "多謝參與 2026年6月5日培訓（約 90 分鐘）。回饋有助改善日後課程，約需 3–5 分鐘。"
    "除最後一題外，其餘可選「不願透露」或不填。本問卷僅作培訓改善，不影響考績或人事。"
)


def _opts(*labels: str) -> list[dict]:
    return [{"value": label} for label in labels]


def _section(title: str) -> dict:
    return {"title": title, "textItem": {}}


def _scale(title: str, *, required: bool = False) -> dict:
    return {
        "title": title,
        "questionItem": {
            "question": {
                "required": required,
                "scaleQuestion": {
                    "low": 1,
                    "high": 5,
                    "lowLabel": "非常不同意",
                    "highLabel": "非常同意",
                },
            }
        },
    }


def _radio(title: str, options: list[str], *, required: bool = False) -> dict:
    return {
        "title": title,
        "questionItem": {
            "question": {
                "required": required,
                "choiceQuestion": {
                    "type": "RADIO",
                    "options": _opts(*options),
                },
            }
        },
    }


def _checkbox(title: str, options: list[str], *, required: bool = False) -> dict:
    return {
        "title": title,
        "questionItem": {
            "question": {
                "required": required,
                "choiceQuestion": {
                    "type": "CHECKBOX",
                    "options": _opts(*options),
                },
            }
        },
    }


def _paragraph(title: str, *, required: bool = False) -> dict:
    return {
        "title": title,
        "questionItem": {
            "question": {
                "required": required,
                "textQuestion": {"paragraph": True},
            }
        },
    }


# Order = form order. Edit here to change questions.
ITEMS: list[dict] = [
    _section("一、整體"),
    _scale("整體而言，今次培訓對我有幫助。"),
    _scale("培訓節奏（90 分鐘）適中。"),
    _radio("整體難度", ["太淺", "適中", "稍難", "太難"]),
    _scale("講解清楚，我跟得上。"),
    _section("二、三個活動"),
    _scale("活動一（錄音→會議紀錄）實用，我願意在工作中嘗試。"),
    _scale("活動二（本機文件整理）實用，我願意在工作中嘗試。"),
    _scale("活動三（靜態網站小工具）實用，我願意在工作中嘗試。"),
    _checkbox(
        "邊個活動最有「哇」感？（可複選）",
        ["會議紀錄", "執檔", "網站", "都一般"],
    ),
    _radio(
        "邊個活動你想課後再學多啲？",
        ["活動一", "活動二", "活動三", "唔需要"],
    ),
    _section("三、概念"),
    _scale("我大致明白工作流（Workflow）：輸入→步驟→輸出，唔係淨係問一句。"),
    _scale("我大致明白 Skills / Rules 係咩分別、幾時有用。"),
    _radio("MCP 聽完後", ["明白會用", "有概念但未試", "仍然唔明"]),
    _scale("「老師係工作流設計師，AI 係實習文員」呢個定位，我認同。"),
    _section("四、環境與講義"),
    _radio(
        "Cursor 安裝／登入",
        ["順利", "有問題但課堂解決", "仍有問題"],
    ),
    _scale("講義（00–08）清晰有用。"),
    _checkbox(
        "課後最想睇邊份講義？（可複選）",
        ["FAQ", "API Key", "本機 MCP", "Google Drive MCP", "網站上線", "其他"],
    ),
    _radio(
        "年級／組別（選填）",
        ["行政", "中文", "英文", "數學", "理科", "文科", "其他", "不願透露"],
    ),
    _section("五、開放題"),
    _paragraph("最有用的一樣嘢係咩？"),
    _paragraph("最難／最卡的一環係咩？（例如：Approve、@ 引用、Model、網路…）"),
    _paragraph("若有多一節 90 分鐘進階班，你最想學咩？"),
    _paragraph("其他意見（選填）"),
]


def load_credentials():
    key_path = Path(
        os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", DEFAULT_KEY)
    )
    if not key_path.is_file():
        print(
            f"找不到金鑰檔：{key_path}\n"
            "請將 Service Account JSON 放到 config/gcp-service-account.json\n"
            "詳見 handouts/10-google-forms-service-account-setup.md",
            file=sys.stderr,
        )
        sys.exit(1)

    creds = service_account.Credentials.from_service_account_file(
        str(key_path),
        scopes=SCOPES,
    )
    delegated = os.environ.get("GOOGLE_FORMS_DELEGATED_USER", "").strip()
    if delegated:
        creds = creds.with_subject(delegated)
        print(f"使用網域授權，模擬使用者：{delegated}")
    else:
        print(
            "未設定 GOOGLE_FORMS_DELEGATED_USER；"
            "問卷將建立在 Service Account 名下。"
        )
    return creds


def build_create_requests(items: list[dict]) -> list[dict]:
    return [
        {
            "createItem": {
                "item": item,
                "location": {"index": i},
            }
        }
        for i, item in enumerate(items)
    ]


def share_form_edit(drive, form_id: str, email: str) -> None:
    drive.permissions().create(
        fileId=form_id,
        body={"type": "user", "role": "writer", "emailAddress": email},
        sendNotificationEmail=False,
    ).execute()
    print(f"已分享編輯權予：{email}")


def main() -> None:
    creds = load_credentials()
    forms = build("forms", "v1", credentials=creds, static_discovery=False)
    drive = build("drive", "v3", credentials=creds, static_discovery=False)

    created = (
        forms.forms()
        .create(body={"info": {"title": FORM_TITLE, "documentTitle": FORM_TITLE}})
        .execute()
    )
    form_id = created["formId"]
    print(f"已建立空白表單，formId={form_id}")

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
                        "settings": {
                            "emailCollectionType": "DO_NOT_COLLECT",
                        },
                        "updateMask": "emailCollectionType",
                    }
                },
            ]
        },
    ).execute()

    result = forms.forms().get(formId=form_id).execute()
    responder = result.get("responderUri", "")
    edit_url = f"https://docs.google.com/forms/d/{form_id}/edit"

    share_with = os.environ.get("GOOGLE_FORMS_SHARE_WITH", "").strip()
    if share_with:
        try:
            share_form_edit(drive, form_id, share_with)
        except Exception as exc:  # noqa: BLE001 — surface API message to trainer
            print(f"分享編輯權失敗（可手動分享）：{exc}", file=sys.stderr)

    print("\n=== 問卷已建立 ===")
    print(f"填寫連結：{responder}")
    print(f"編輯連結：{edit_url}")
    print("\n請到編輯連結 → 設定 → 開啟「限制每人回應 1 次」→ 傳送 → 取得短連結。")


if __name__ == "__main__":
    main()
