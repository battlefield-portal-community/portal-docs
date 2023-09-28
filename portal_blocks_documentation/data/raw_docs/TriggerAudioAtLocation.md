# %{ID_ARRIVAL_BLOCK_TRIGGERLOCATIONALAUDIO}

%{help.triggeraudioatlocation.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_ENUM_LOCATIONALSOUNDS}
2. %{PYRITE_TYPE_VECTOR}

```
<block type="TriggerAudioAtLocation">
    <value name="VALUE-0">
        <block type="LocationalSoundsItem">
            <field name="VALUE-0">LocationalSounds</field>
            <field name="VALUE-1">Ping</field>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="GetSoldierState">
            <value name="VALUE-0">
                <block type="EventPlayer"></block>
            </value>
            <value name="VALUE-1">
                <block type="SoldierStateVectorItem">
                    <field name="VALUE-0">SoldierStateVector</field>
                    <field name="VALUE-1">GetPosition</field>
                </block>
            </value>
        </block>
    </value>
</block>
```
