param(
  [int]$Port = 9226,
  [string]$Url = "about:blank",
  [string]$Profile = "",
  [int]$WaitSeconds = 8
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Profile)) {
  $safeUrl = ($Url -replace '[^a-zA-Z0-9]+', '-').Trim('-')
  if ([string]::IsNullOrWhiteSpace($safeUrl)) { $safeUrl = "browser" }
  if ($safeUrl.Length -gt 32) { $safeUrl = $safeUrl.Substring(0, 32) }
  $Profile = "C:\ChromeDebug-$safeUrl-$Port"
}

New-Item -ItemType Directory -Force -Path $Profile | Out-Null

$existing = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue | Select-Object -First 1
if ($existing) {
  $version = Invoke-RestMethod -Uri "http://127.0.0.1:$Port/json/version" -TimeoutSec 3
  [pscustomobject]@{
    action = "existing"
    port = $Port
    ownerPid = $existing.OwningProcess
    browser = $version.Browser
    webSocketDebuggerUrl = $version.webSocketDebuggerUrl
    profile = $Profile
  } | ConvertTo-Json -Depth 4
  exit 0
}

$chromeCandidates = @(
  "$env:LocalAppData\Google\Chrome\Application\chrome.exe",
  "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
  "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe"
)
$chrome = $chromeCandidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
if (-not $chrome) {
  throw "Chrome executable was not found in common install paths."
}

$args = @(
  "--new-window",
  "--remote-debugging-port=$Port",
  "--remote-debugging-address=127.0.0.1",
  "--remote-allow-origins=*",
  "--user-data-dir=$Profile",
  "--no-first-run",
  "--no-default-browser-check",
  "--window-size=1368,900",
  $Url
)

$process = Start-Process -FilePath $chrome -ArgumentList $args -PassThru

$version = $null
for ($i = 0; $i -lt ($WaitSeconds * 2); $i++) {
  Start-Sleep -Milliseconds 500
  try {
    $version = Invoke-RestMethod -Uri "http://127.0.0.1:$Port/json/version" -TimeoutSec 1
    break
  } catch {
    $version = $null
  }
}

$tcp = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue | Select-Object -First 1

[pscustomobject]@{
  action = if ($version) { "started-visible" } else { "started-but-debug-not-ready" }
  pid = $process.Id
  alive = [bool](Get-Process -Id $process.Id -ErrorAction SilentlyContinue)
  port = $Port
  portListening = [bool]$tcp
  ownerPid = if ($tcp) { $tcp.OwningProcess } else { $null }
  browser = if ($version) { $version.Browser } else { $null }
  webSocketDebuggerUrl = if ($version) { $version.webSocketDebuggerUrl } else { $null }
  profile = $Profile
  url = $Url
} | ConvertTo-Json -Depth 4
