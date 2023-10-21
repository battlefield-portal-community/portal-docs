$portalData = Get-Content -Raw maps.json | ConvertFrom-JSON
$mdText = '---
title: Map Layouts
draft: false
---

{{< toc >}}

# Work in Progress

{{< hint type=note >}}
Work in progress... check back later!
{{< /hint >}}'
$mdText += '# Map Layouts'
foreach ($map in $portalData.maps) {
    $mdText += "`n`n## $map"
    foreach ($mode in $portalData.modes) {
        $mdText += "`n`n### $mode"
        foreach ($size in $portalData.sizes) {
            $mdText += "`n`n#### $map - $mode - $size"
            $mdText += "`n`n_No information available..._"
        }
    }
}
$mdText | Out-File -FilePath "maps.md"