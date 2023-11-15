# %{ID_ARRIVAL_BLOCK_SPOTTARGETFORPLAYER}

%{help.spottargetforplayer.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_PLAYER}

    %{help.common.contexts.target}

2. %{PYRITE_TYPE_PLAYER}

    %{help.common.contexts.spotter}

3. %{PYRITE_TYPE_NUMBER}

    %{help.common.contexts.duration}

```
<block type="SpotTargetForPlayer">
    <value name="VALUE-0">
        <block type="FirstOf">
            <value name="VALUE-0">
                <block type="AllPlayers"></block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="EventPlayer"></block>
    </value>
    <value name="VALUE-2">
        <block type="Number">
            <field name="NUM">1</field>
        </block>
    </value>
</block>
```