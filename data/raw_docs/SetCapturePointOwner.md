# %{ID_ARRIVAL_BLOCK_SETCAPTUREPOINTOWNER}

%{help.setcapturepointowner.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_CAPTUREPOINT}
2. %{PYRITE_TYPE_TEAMID}

```
<block type="SetCapturePointOwner">
    <value name="VALUE-0">
        <block type="GetCapturePoint">
            <value name="VALUE-0">
                <block type="CapturePointsItem">
                    <field name="VALUE-0">CapturePoints</field>
                    <field name="VALUE-1">A1</field>
                </block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="GetTeamId">
            <value name="VALUE-0">
                <block type="Number">
                    <field name="NUM">1</field>
                </block>
            </value>
        </block>
    </value>
</block>
```
