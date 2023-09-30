# %{ID_ARRIVAL_BLOCK_TRIGGERAUDIO}

%{help.triggeraudio.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_ENUM_SOUNDS} | %{PYRITE_TYPE_ENUM_VOICEOVERS}
2. %{PYRITE_TYPE_TEAMID}

```
<block type="TriggerAudio">
    <value name="VALUE-0">
        <block type="SoundsItem">
            <field name="VALUE-0">Sounds</field>
            <field name="VALUE-1">ShowObjective</field>
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
