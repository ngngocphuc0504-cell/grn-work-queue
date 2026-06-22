Param(
    [string]$TemplatePath = "c:\Users\VEE0678\Downloads\ws-default-career-twin\ws-default-career-twin\.agent\skills\fco-event-analytics\assets\monthly-template.html",
    [string]$DataDir = "c:\Users\VEE0678\Downloads\ws-default-career-twin\ws-default-career-twin\outputs\fco-portal\data",
    [string]$OutputPath = "c:\Users\VEE0678\Downloads\ws-default-career-twin\ws-default-career-twin\outputs\fco-portal\monthly.html"
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

$template = Get-Content -Path $TemplatePath -Raw -Encoding utf8

# Collect all monthly plan JSON files
$jsonFiles = Get-ChildItem -Path $DataDir -Filter "monthly_plan*.json" | Sort-Object Name
Write-Output "Found $($jsonFiles.Count) month data files"

# Build a combined data object: { "2026-06": {...}, "2026-01": {...}, ... }
$allData = @{}
foreach ($f in $jsonFiles) {
    $data = Get-Content -Path $f.FullName -Raw -Encoding utf8 | ConvertFrom-Json
    $allData[$data.month] = $data
}

# Sort months descending (newest first) for the dropdown
$sortedMonths = $allData.Keys | Sort-Object -Descending

# Build the month options JSON array
$monthOptions = @()
foreach ($mk in $sortedMonths) {
    $monthOptions += @{
        key = $mk
        label = $allData[$mk].month_label
    }
}

# Convert all data to JSON for injection
$allDataJson = $allData | ConvertTo-Json -Depth 12 -Compress
$monthOptionsJson = $monthOptions | ConvertTo-Json -Depth 4 -Compress

# Load recurring events index
$recurringPath = Join-Path $DataDir "recurring_events.json"
$recurringJson = "{}"
if (Test-Path $recurringPath) {
    $recurringJson = Get-Content -Path $recurringPath -Raw -Encoding utf8
    Write-Output "Loaded recurring_events.json"
} else {
    Write-Output "WARNING: recurring_events.json not found, using empty object"
}

# Replace placeholders
$output = $template -replace '\{\{DATA_JSON\}\}', $allDataJson
$output = $output -replace '\{\{MONTH_OPTIONS_JSON\}\}', $monthOptionsJson
$output = $output -replace '\{\{RECURRING_JSON\}\}', $recurringJson
$output = $output -replace '\{\{DEFAULT_MONTH\}\}', $sortedMonths[0]

$outputDir = Split-Path $OutputPath
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

$output | Out-File -Encoding utf8 -FilePath $OutputPath
Write-Output "Generated: $OutputPath (months: $($sortedMonths -join ', '))"
