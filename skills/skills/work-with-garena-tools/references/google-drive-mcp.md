# Google Drive MCP

Use for Google Drive file and folder search, metadata/content reads, uploads, updates, unsharing, and creating Google Docs/Sheets/Slides.

## Known Callable Surface

Discovered via `garena-vn-mcp-gw`:

- `google_drive_mcp_search_my_files`
- `google_drive_mcp_list_my_folders`
- `google_drive_mcp_how_to_connect_folders`
- `google_drive_mcp_get_file_metadata`
- `google_drive_mcp_get_folder_files`
- `google_drive_mcp_get_file_content`
- `google_drive_mcp_upload_file`
- `google_drive_mcp_update_file_content`
- `google_drive_mcp_unshare_drive_item`
- `google_drive_mcp_create_folder`
- `google_drive_mcp_create_google_doc`
- `google_drive_mcp_create_google_sheet`
- `google_drive_mcp_create_google_slide_deck`

The 2026-06-15 MCP admin screenshot showed 13 tools, matching this discovered list.

## Workflow

1. Search files/folders or list connected folders before reading content.
2. Use metadata to confirm identity, owner, type, and modified time when there are multiple candidates.
3. Use file content only after resolving the exact file.
4. For uploads or creates, confirm the destination folder and output type.
5. For updates, read the current content first and preserve the existing format when possible.

## Safety

- `unshare_drive_item` is destructive from a collaboration standpoint. Require explicit user intent.
- Do not update file content based on a fuzzy match.
- If a folder is not connected, use `how_to_connect_folders` and report the requirement.
