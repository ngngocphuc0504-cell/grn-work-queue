Param(
    [string]$ExcelPath = "",
    [string]$OutputDir = "c:\Users\VEE0678\Downloads\ws-default-career-twin\ws-default-career-twin\outputs\fco-portal\data"
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
Import-Module ImportExcel

# Auto-find the Monthly Plan file if not provided
if ($ExcelPath -eq "") {
    $candidates = Get-ChildItem "c:\Users\VEE0678\Downloads\ws-default-career-twin\ws-default-career-twin\Garena\" -Filter "*Monthly*" -ErrorAction SilentlyContinue
    if ($candidates.Count -gt 0) {
        $ExcelPath = $candidates[0].FullName
    } else {
        $ExcelPath = "C:\Users\VEE0678\Downloads\monthly_plan.xlsx"
    }
}

Write-Output "Reading: $ExcelPath"

# Ensure output directory exists
if (-not (Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
}

# Helper: Convert Excel serial date to ISO string
function Convert-ExcelDate($serial) {
    if ($serial -eq $null -or $serial -eq "" -or $serial -eq "0") { return $null }
    try {
        $num = [double]$serial
        if ($num -lt 1000) { return $null }
        $date = [datetime]::FromOADate($num)
        return $date.ToString("yyyy-MM-dd")
    } catch {
        return $null
    }
}

# ============================================================
# 1. Event Summary _ VN
# ============================================================
Write-Output "Extracting Event Summary..."
$eventData = Import-Excel -Path $ExcelPath -WorksheetName "Event Summary _ VN" -NoHeader -StartRow 1

$revEvents = @()
$dauEvents = @()
$promotionEvents = @()
$currentCategory = ""

$knownRecurring = @("Long-term", "Foosball", "Monopoly", "TCSS", "Weekly DAU", "WG DAU", "3-tier top-up promotion", "Special top-up promotion")

foreach ($row in $eventData) {
    $props = @($row.PSObject.Properties)
    
    # Get values by column index (P18=Category, P19=Name, P20=Impact, P21=Mechanics, P23=Start, P24=End, P25=Duration)
    $cat = "$($props[17].Value)".Trim()
    $name = "$($props[18].Value)".Trim()
    $impact = "$($props[19].Value)".Trim()
    $mechanics = "$($props[20].Value)".Trim()
    $startSerial = "$($props[22].Value)"
    $endSerial = "$($props[23].Value)"
    $duration = "$($props[24].Value)"
    
    if ($cat -ne "" -and $cat -ne "0") { $currentCategory = $cat }
    if ($name -eq "" -or $name -eq "0") { continue }
    
    $startDate = Convert-ExcelDate $startSerial
    $endDate = Convert-ExcelDate $endSerial
    if ($startDate -eq $null) { continue }
    
    $isRecurring = $false
    foreach ($r in $knownRecurring) {
        if ($name -match [regex]::Escape($r)) { $isRecurring = $true; break }
    }
    
    $eventObj = @{
        name = $name
        start = $startDate
        end = $endDate
        duration = if ($duration -ne "" -and $duration -ne "0") { [int]$duration } else { $null }
        impact = if ($impact -ne "" -and $impact -ne "0") { $impact } else { $null }
        mechanics = if ($mechanics -ne "" -and $mechanics -ne "0") { $mechanics } else { $null }
        recurring = $isRecurring
    }
    
    switch -Regex ($currentCategory) {
        "REV" { $revEvents += $eventObj }
        "DAU" { $dauEvents += $eventObj }
        "Promotion" { $promotionEvents += $eventObj }
    }
    
    # Stop after row ~30 (before Mechanics section and in-game events)
    if ($revEvents.Count + $dauEvents.Count + $promotionEvents.Count -ge 20) { break }
}

# ============================================================
# 2. Reward Summary VN
# ============================================================
Write-Output "Extracting Reward Summary..."
$rewardData = Import-Excel -Path $ExcelPath -WorksheetName "Reward_Summary_VN" -NoHeader -StartRow 1

$rewards = @{
    pc_m_regular = @{ pp = 0; bp = 0; total = 0; bp_ratio = 0 }
    pc_regular = @{ pp = 0; bp = 0; total = 0; bp_ratio = 0 }
    mobile = @{ pp = 0; bp = 0; total = 0; bp_ratio = 0 }
    pc_m_web = @{ pp = 0; bp = 0; total = 0; bp_ratio = 0 }
    web = @{ pp = 0; bp = 0; total = 0 }
    pc_m_web_svip = @{ pp = 0; bp = 0; total = 0; bp_ratio = 0 }
    svip = @{ pp = 0; bp = 0; total = 0; bp_ratio = 0 }
    daily_usd = @{
        pc_m_regular = @{ pp = 0; bp = 0; total = 0 }
        web = @{ pp = 0; bp = 0; total = 0 }
        svip = @{ pp = 0; bp = 0; total = 0 }
    }
    last_month = @{
        pc_m_regular = @{ pp = 0; bp = 0; total = 0; bp_ratio = 0 }
        web = @{ pp = 0; bp = 0; total = 0 }
        svip = @{ pp = 0; bp = 0; total = 0; bp_ratio = 0 }
    }
}

$rowNum = 0
$section = "monthly"
foreach ($row in $rewardData) {
    $rowNum++
    $props = @($row.PSObject.Properties)
    $c2 = "$($props[1].Value)".Trim()
    $c3 = "$($props[2].Value)".Trim()
    $c4 = "$($props[3].Value)".Trim()
    
    if ($c2 -eq "Monthly") { $section = "monthly"; continue }
    if ($c2 -eq "Daily" -and $rowNum -lt 20) { $section = "daily_bp"; continue }
    if ($c2 -eq "Daily" -and $rowNum -ge 20) { $section = "daily_usd"; continue }
    if ($c2 -eq "Composition") { $section = "composition"; continue }
    if ($c1 -eq "INPUT") { break }
    
    if ($section -eq "monthly" -and $c3 -match "PC & M regular") {
        try {
            $rewards.pc_m_regular.pp = [double]"$($props[5].Value)"
            $rewards.pc_m_regular.bp = [double]"$($props[6].Value)"
            $rewards.pc_m_regular.total = [double]"$($props[7].Value)"
            $rewards.pc_m_regular.bp_ratio = [double]"$($props[8].Value)"
            $rewards.last_month.pc_m_regular.pp = [double]"$($props[12].Value)"
            $rewards.last_month.pc_m_regular.bp = [double]"$($props[13].Value)"
            $rewards.last_month.pc_m_regular.total = [double]"$($props[14].Value)"
            $rewards.last_month.pc_m_regular.bp_ratio = [double]"$($props[15].Value)"
        } catch {}
    }
    if ($section -eq "monthly" -and $c4 -eq "Web") {
        try {
            $rewards.web.pp = [double]"$($props[5].Value)"
            $rewards.web.total = [double]"$($props[7].Value)"
            $rewards.last_month.web.pp = [double]"$($props[12].Value)"
            $rewards.last_month.web.bp = [double]"$($props[13].Value)"
            $rewards.last_month.web.total = [double]"$($props[14].Value)"
        } catch {}
    }
    if ($section -eq "monthly" -and $c4 -eq "SVIP") {
        try {
            $rewards.svip.pp = [double]"$($props[5].Value)"
            $rewards.svip.bp = [double]"$($props[6].Value)"
            $rewards.svip.total = [double]"$($props[7].Value)"
            $rewards.svip.bp_ratio = [double]"$($props[8].Value)"
            $rewards.last_month.svip.pp = [double]"$($props[12].Value)"
            $rewards.last_month.svip.bp = [double]"$($props[13].Value)"
            $rewards.last_month.svip.total = [double]"$($props[14].Value)"
            $rewards.last_month.svip.bp_ratio = [double]"$($props[15].Value)"
        } catch {}
    }

    if ($rowNum -gt 44) { break }
}

# ============================================================
# 3. Promotion VN
# ============================================================
Write-Output "Extracting Promotions..."
$promoData = Import-Excel -Path $ExcelPath -WorksheetName "5.Promotion_VN" -NoHeader -StartRow 1

$promotionTiers = @()
$currentTier = ""
$currentItems = @()

$rowNum = 0
foreach ($row in $promoData) {
    $rowNum++
    if ($rowNum -le 3) { continue }
    if ($rowNum -gt 45) { break }
    
    $props = @($row.PSObject.Properties)
    $target = "$($props[4].Value)".Trim()
    $tierAmount = "$($props[5].Value)".Trim()
    $itemName = "$($props[10].Value)".Trim()
    $itemValueBP = "$($props[11].Value)"
    $itemValueUSD = "$($props[12].Value)"
    $count = "$($props[13].Value)"
    $efficiency = "$($props[20].Value)"
    
    if ($target -eq "TOPUP" -and $tierAmount -ne "" -and $tierAmount -ne "0") {
        if ($currentTier -ne "" -and $currentItems.Count -gt 0) {
            $promotionTiers += @{
                tier = $currentTier
                efficiency = $currentEfficiency
                items = $currentItems
            }
        }
        $currentTier = $tierAmount
        $currentEfficiency = if ($efficiency -ne "" -and $efficiency -ne "0") { [double]$efficiency } else { $null }
        $currentItems = @()
    }
    
    if ($itemName -ne "" -and $itemName -ne "0") {
        $currentItems += @{
            name = $itemName
            value_bp = if ($itemValueBP -ne "" -and $itemValueBP -ne "0") { try { [double]$itemValueBP } catch { 0 } } else { 0 }
            value_usd = if ($itemValueUSD -ne "" -and $itemValueUSD -ne "0") { try { [double]$itemValueUSD } catch { 0 } } else { 0 }
            count = if ($count -ne "" -and $count -ne "0") { try { [int]$count } catch { 1 } } else { 1 }
        }
    }
}
# Push last tier
if ($currentTier -ne "" -and $currentItems.Count -gt 0) {
    $promotionTiers += @{
        tier = $currentTier
        efficiency = $currentEfficiency
        items = $currentItems
    }
}

# ============================================================
# BUILD FINAL JSON
# ============================================================
$output = @{
    month = "2026-06"
    month_label = "June 2026"
    extracted_at = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ss")
    events = @{
        rev = $revEvents
        dau = $dauEvents
        promotion = $promotionEvents
    }
    rewards = $rewards
    promotion_tiers = $promotionTiers
}

$jsonPath = Join-Path $OutputDir "monthly_plan.json"
$output | ConvertTo-Json -Depth 10 | Out-File -Encoding utf8 -FilePath $jsonPath

Write-Output "JSON written to: $jsonPath"
Write-Output "Events: REV=$($revEvents.Count), DAU=$($dauEvents.Count), Promotion=$($promotionEvents.Count)"
Write-Output "Promotion Tiers: $($promotionTiers.Count)"
Write-Output "Done."
