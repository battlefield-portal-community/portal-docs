# %{ID_ARRIVAL_BLOCK_SETWORLDICONOWNER}

%{help.setworldiconowner.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_ENUM_WORLDICONS}
2. %{PYRITE_TYPE_TEAMID}

```
<block type="SetWorldIconOwner">
    <value name="VALUE-0">
        <block type="WorldIconsItem">
            <field name="VALUE-0">WorldIcons</field>
            <field name="VALUE-1">C</field>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="GetTeamId">
            <value name="VALUE-0">
                <block type="EventPlayer"></block>
            </value>
        </block>
    </value>
</block>
```