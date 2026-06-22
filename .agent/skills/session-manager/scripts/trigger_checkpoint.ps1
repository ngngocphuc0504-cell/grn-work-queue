param (
    [Parameter(Mandatory=$true)]
    [string]$TriggerReason,
    
    [Parameter(Mandatory=$false)]
    [string]$InsightPayload = ""
)

$ErrorActionPreference = "Stop"

# Get ISO 8601 Timestamp
$Timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:sszzz")
$WorkspaceRoot = (Resolve-Path "$PSScriptRoot\..\..\..\..\").Path

$LedgerPath = Join-Path $WorkspaceRoot ".agent\memory_bus\ledger.md"
$InsightPath = Join-Path $WorkspaceRoot ".agent\memory_bus\insight_journal.md"
$StateJsonPath = Join-Path $WorkspaceRoot ".agent\memory_bus\coordinator\status\state.json"

try {
    # 1. Update Ledger
    $LedgerEntry = "| $Timestamp | SYSTEM | Session-Checkpoint | Done | $TriggerReason |"
    Add-Content -Path $LedgerPath -Value $LedgerEntry
    
    # 2. Update Insight Journal (Optional)
    if (![string]::IsNullOrWhiteSpace($InsightPayload)) {
        $InsightEntry = "`n### Checkpoint: $Timestamp`n$InsightPayload"
        Add-Content -Path $InsightPath -Value $InsightEntry
    }
    
    # 3. Update state.json Heartbeat
    if (Test-Path $StateJsonPath) {
        $StateJson = Get-Content -Path $StateJsonPath -Raw | ConvertFrom-Json
        $StateJson.last_updated = $Timestamp
        $StateJson | ConvertTo-Json -Depth 5 | Set-Content -Path $StateJsonPath -Encoding UTF8
    }

    Write-Host "✅ Checkpoint saved. $TriggerReason. Continuing..." -ForegroundColor Green
} catch {
    Write-Error "❌ Checkpoint failure: $_"
    exit 1
}
