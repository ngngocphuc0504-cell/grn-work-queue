# PowerShell Local HTTP Server for FCO Operations Portal
Param(
    [int]$Port = 8080,
    [string]$PortalDir = "c:\Users\VEE0678\Downloads\ws-default-career-twin\ws-default-career-twin\outputs\fco-portal",
    [string]$AnalyticsDir = "c:\Users\VEE0678\Downloads\ws-default-career-twin\ws-default-career-twin\outputs\fco-event-analytics"
)

$ErrorActionPreference = "Stop"

$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:${Port}/")

function Serve-File {
    param($resp, $fPath, $contentType)
    if (Test-Path $fPath) {
        $content = Get-Content -Path $fPath -Raw -Encoding utf8
        $buffer = [System.Text.Encoding]::UTF8.GetBytes($content)
        $resp.ContentLength64 = $buffer.Length
        $resp.ContentType = if ($contentType) { $contentType } else { "text/html; charset=utf-8" }
        $resp.OutputStream.Write($buffer, 0, $buffer.Length)
    } else {
        $resp.StatusCode = 404
        $msg = "File not found: $fPath"
        $buffer = [System.Text.Encoding]::UTF8.GetBytes($msg)
        $resp.ContentLength64 = $buffer.Length
        $resp.OutputStream.Write($buffer, 0, $buffer.Length)
    }
}

try {
    $listener.Start()
    Write-Host "=========================================================="
    Write-Host "   FCO Operations Portal Local Server v2"
    Write-Host "   Portal:      http://localhost:${Port}/"
    Write-Host "   Analytics:   http://localhost:${Port}/analytics"
    Write-Host "   Monthly:     http://localhost:${Port}/monthly"
    Write-Host "   Press Ctrl+C to stop the server."
    Write-Host "=========================================================="

    Start-Process "http://localhost:${Port}/"

    while ($listener.IsListening) {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response
        $urlPath = $request.Url.AbsolutePath

        Write-Host "[$(Get-Date -Format 'HH:mm:ss')] $($request.HttpMethod) $urlPath"

        if ($urlPath -eq "/" -or $urlPath -eq "/index.html") {
            Serve-File $response (Join-Path $PortalDir "index.html")
        }
        elseif ($urlPath -eq "/monthly" -or $urlPath -eq "/monthly.html") {
            Serve-File $response (Join-Path $PortalDir "monthly.html")
        }
        elseif ($urlPath -eq "/analytics" -or $urlPath -eq "/analytics/" -or $urlPath -eq "/analytics/index") {
            # Analytics hub (tabbed view)
            Serve-File $response (Join-Path $AnalyticsDir "index.html")
        }
        elseif ($urlPath -eq "/analytics/manifest.json") {
            Serve-File $response (Join-Path $AnalyticsDir "manifest.json") "application/json; charset=utf-8"
        }
        elseif ($urlPath -match "^/analytics/(view/)?([^/]+\.(html|js|css|json))$") {
            # Serve individual dashboard files via iframe
            $fileName = $Matches[2]
            $filePath = Join-Path $AnalyticsDir $fileName
            Serve-File $response $filePath
        }
        elseif ($urlPath -eq "/analytics/compare" -or $urlPath -eq "/compare") {
            # Legacy direct route - redirect to hub
            Serve-File $response (Join-Path $AnalyticsDir "index.html")
        }
        elseif ($urlPath -match "^/data/(.+\.json)$") {
            # Serve JSON data files
            $fileName = $Matches[1]
            $filePath = Join-Path $PortalDir "data\$fileName"
            Serve-File $response $filePath "application/json; charset=utf-8"
        }
        else {
            $response.StatusCode = 404
            $msg = "Not Found: $urlPath"
            $buffer = [System.Text.Encoding]::UTF8.GetBytes($msg)
            $response.ContentLength64 = $buffer.Length
            $response.OutputStream.Write($buffer, 0, $buffer.Length)
        }

        $response.Close()
    }
}
catch {
    Write-Host "Error: $_"
}
finally {
    if ($listener -and $listener.IsListening) {
        $listener.Stop()
        Write-Host "Server stopped."
    }
}
