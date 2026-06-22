#!/usr/bin/env python3
"""HTTP fallback client for a local Agentation server."""

from __future__ import annotations

import argparse
import json
import sys
import time
from typing import Any
from urllib import error, parse, request


DEFAULT_BASE_URL = "http://localhost:4747"


def http_json(method: str, url: str, payload: dict[str, Any] | None = None) -> Any:
    data = None
    headers = {"Accept": "application/json"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = request.Request(url, data=data, headers=headers, method=method.upper())
    try:
        with request.urlopen(req, timeout=30) as response:
            raw = response.read().decode("utf-8")
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} for {url}: {body}") from exc
    except error.URLError as exc:
        raise RuntimeError(f"Cannot reach Agentation server at {url}: {exc.reason}") from exc

    if not raw:
        return None
    return json.loads(raw)


def normalize_sessions(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("value"), list):
        return payload["value"]
    raise RuntimeError("Unexpected sessions payload shape.")


def get_pending(base_url: str, session_id: str | None) -> dict[str, Any]:
    if session_id:
        return http_json("GET", f"{base_url}/sessions/{session_id}/pending")
    return http_json("GET", f"{base_url}/pending")


def print_json(payload: Any) -> None:
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def summarize_annotation(annotation: dict[str, Any]) -> str:
    nearby = annotation.get("nearbyText") or "-"
    comment = annotation.get("comment") or "-"
    status = annotation.get("status") or "pending"
    return f"{annotation.get('id')} | {status} | {comment} | nearby: {nearby}"


def cmd_health(args: argparse.Namespace) -> int:
    payload = http_json("GET", f"{args.base_url}/health")
    print_json(payload)
    return 0


def cmd_sessions(args: argparse.Namespace) -> int:
    sessions = normalize_sessions(http_json("GET", f"{args.base_url}/sessions"))
    if args.json:
        print_json(sessions)
        return 0

    print(f"{len(sessions)} session(s)")
    for session in sessions:
        print(
            f"- {session.get('id')} | {session.get('status')} | "
            f"{session.get('url')} | {session.get('createdAt')}"
        )
    return 0


def cmd_find_session(args: argparse.Namespace) -> int:
    needle = args.url_substring.lower()
    sessions = normalize_sessions(http_json("GET", f"{args.base_url}/sessions"))
    matches = [session for session in sessions if needle in str(session.get("url", "")).lower()]
    if args.json:
        print_json(matches)
        return 0

    print(f"{len(matches)} matching session(s)")
    for session in matches:
        print(
            f"- {session.get('id')} | {session.get('status')} | "
            f"{session.get('url')} | {session.get('createdAt')}"
        )
    return 0


def cmd_session(args: argparse.Namespace) -> int:
    payload = http_json("GET", f"{args.base_url}/sessions/{args.id}")
    if args.json:
        print_json(payload)
        return 0

    annotations = payload.get("annotations", [])
    print(f"session: {payload.get('id')}")
    print(f"url: {payload.get('url')}")
    print(f"status: {payload.get('status')}")
    print(f"annotations: {len(annotations)}")
    for annotation in annotations:
        print(f"- {summarize_annotation(annotation)}")
    return 0


def cmd_pending(args: argparse.Namespace) -> int:
    payload = get_pending(args.base_url, args.session)
    if args.json:
        print_json(payload)
        return 0

    annotations = payload.get("annotations", [])
    print(f"pending count: {payload.get('count', len(annotations))}")
    for annotation in annotations:
        print(f"- {summarize_annotation(annotation)}")
    return 0


def cmd_annotation(args: argparse.Namespace) -> int:
    payload = http_json("GET", f"{args.base_url}/annotations/{args.id}")
    if args.json:
        print_json(payload)
        return 0

    print(f"id: {payload.get('id')}")
    print(f"session: {payload.get('sessionId')}")
    print(f"status: {payload.get('status')}")
    print(f"url: {payload.get('url')}")
    print(f"comment: {payload.get('comment')}")
    print(f"nearbyText: {payload.get('nearbyText')}")
    print(f"elementPath: {payload.get('elementPath')}")
    print("thread:")
    for item in payload.get("thread", []) or []:
        print(f"- {item.get('role')}: {item.get('content')}")
    return 0


def cmd_reply(args: argparse.Namespace) -> int:
    payload = http_json(
        "POST",
        f"{args.base_url}/annotations/{args.id}/thread",
        {"role": args.role, "content": args.message},
    )
    print_json(payload)
    return 0


def patch_annotation(base_url: str, annotation_id: str, payload: dict[str, Any]) -> Any:
    return http_json("PATCH", f"{base_url}/annotations/{annotation_id}", payload)


def cmd_status(args: argparse.Namespace) -> int:
    payload: dict[str, Any] = {"status": args.status}
    if args.resolved_by:
        payload["resolvedBy"] = args.resolved_by
    response = patch_annotation(args.base_url, args.id, payload)
    print_json(response)
    return 0


def cmd_resolve(args: argparse.Namespace) -> int:
    if args.message:
        http_json(
            "POST",
            f"{args.base_url}/annotations/{args.id}/thread",
            {"role": args.role, "content": args.message},
        )
    response = patch_annotation(
        args.base_url,
        args.id,
        {"status": "resolved", "resolvedBy": args.resolved_by},
    )
    print_json(response)
    return 0


def cmd_dismiss(args: argparse.Namespace) -> int:
    payload: dict[str, Any] = {"status": "dismissed"}
    if args.reason:
        payload["comment"] = args.reason
    response = patch_annotation(args.base_url, args.id, payload)
    print_json(response)
    return 0


def cmd_watch(args: argparse.Namespace) -> int:
    deadline = None if args.timeout <= 0 else time.time() + args.timeout

    while True:
        payload = get_pending(args.base_url, args.session)
        annotations = payload.get("annotations", [])

        if args.url_substring:
            needle = args.url_substring.lower()
            annotations = [
                item for item in annotations if needle in str(item.get("url", "")).lower()
            ]
            payload = {"count": len(annotations), "annotations": annotations}

        if annotations:
            print_json(payload)
            return 0

        if deadline is not None and time.time() >= deadline:
            print_json(payload)
            return 1

        time.sleep(args.interval)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="HTTP fallback client for Agentation.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    subparsers = parser.add_subparsers(dest="command", required=True)

    health = subparsers.add_parser("health")
    health.set_defaults(func=cmd_health)

    sessions = subparsers.add_parser("sessions")
    sessions.add_argument("--json", action="store_true")
    sessions.set_defaults(func=cmd_sessions)

    find_session = subparsers.add_parser("find-session")
    find_session.add_argument("--url-substring", required=True)
    find_session.add_argument("--json", action="store_true")
    find_session.set_defaults(func=cmd_find_session)

    session = subparsers.add_parser("session")
    session.add_argument("--id", required=True)
    session.add_argument("--json", action="store_true")
    session.set_defaults(func=cmd_session)

    pending = subparsers.add_parser("pending")
    pending.add_argument("--session")
    pending.add_argument("--json", action="store_true")
    pending.set_defaults(func=cmd_pending)

    annotation = subparsers.add_parser("annotation")
    annotation.add_argument("--id", required=True)
    annotation.add_argument("--json", action="store_true")
    annotation.set_defaults(func=cmd_annotation)

    reply = subparsers.add_parser("reply")
    reply.add_argument("--id", required=True)
    reply.add_argument("--message", required=True)
    reply.add_argument("--role", default="agent")
    reply.set_defaults(func=cmd_reply)

    status = subparsers.add_parser("status")
    status.add_argument("--id", required=True)
    status.add_argument("--status", required=True)
    status.add_argument("--resolved-by")
    status.set_defaults(func=cmd_status)

    resolve = subparsers.add_parser("resolve")
    resolve.add_argument("--id", required=True)
    resolve.add_argument("--message")
    resolve.add_argument("--role", default="agent")
    resolve.add_argument("--resolved-by", default="agent")
    resolve.set_defaults(func=cmd_resolve)

    dismiss = subparsers.add_parser("dismiss")
    dismiss.add_argument("--id", required=True)
    dismiss.add_argument("--reason")
    dismiss.set_defaults(func=cmd_dismiss)

    watch = subparsers.add_parser("watch")
    watch.add_argument("--session")
    watch.add_argument("--url-substring")
    watch.add_argument("--interval", type=float, default=2.0)
    watch.add_argument("--timeout", type=float, default=300.0)
    watch.set_defaults(func=cmd_watch)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.func(args))
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
