$portalData = Get-Item -Path 'maps.json' | ConvertFrom-JSON -Depth 99
$mdText = '# Maps'
foreach ($modeType in $portalData.modeTypes) {
    foreach ($mode in $portalData.modes) {
        foreach ($map in $portalData.maps) {
            foreach ($size in $portalData.sizes) {
    
            }
        }
    }
}