$portalData = Get-Content -Raw maps.json | ConvertFrom-JSON
$mdText = '---
title: Map Layouts
draft: false
---

{{< toc >}}
'
foreach ($map in $portalData.maps) {
    $mdText += "`n`n"
    $mdText += "# $map"
    #$mdText += "`n`n"
    #$mdText += '{{< tabs "' + $map + '" >}}'
    foreach ($mode in $portalData.modes) {
        $modePlain = $mode.replace(' ', '-').replace('(', '').replace(')', '')
        $mdText += "`n"
        $mdText += "`n"
        $mdText += "## $map - $mode"
        $mdText += "`n"
        $mdText += "`n"
        #$mdText += '{{< tab "' + $modePlain + '" >}}'
        #$mdText += "`n"
        $mdText += '{{< tabs "' + "$map-$modePlain" + '" >}}'
        foreach ($size in $portalData.sizes) {
            $mdText += "`n"
            $mdText += '{{< tab "' + $size + '" >}}'
            $mdText += "`n`n### $map - $mode - $size"
            if()
            $mdText += "`n`n_No information available..._"
            $mdText += "`n`n"
            $mdText += '{{< /tab >}}'
        }
        $mdText += "`n"
        $mdText += '{{< /tabs >}}'
        #$mdText += "`n"
        #$mdText += '{{< /tab >}}'
    }
    #$mdText += "`n"
    #$mdText += '{{< /tabs >}}'
}
$mdText | Out-File -FilePath "maps.md" -Encoding utf8