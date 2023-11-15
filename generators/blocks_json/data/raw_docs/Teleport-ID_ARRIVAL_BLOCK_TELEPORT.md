# %{ID_ARRIVAL_BLOCK_TELEPORT}

%{help.teleport.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_PLAYER} | %{PYRITE_TYPE_VEHICLE}
2. %{PYRITE_TYPE_VECTOR}

    %{help.common.contexts.position}

3. %{PYRITE_TYPE_NUMBER}

    %{help.common.contexts.yaw}

```
<block type="Teleport">
    <value name="VALUE-0">
        <block type="EventPlayer"></block>
    </value>
    <value name="VALUE-1">
        <block type="CreateVector">
            <value name="VALUE-0">
                <block type="Number">
                    <field name="NUM">0</field>
                </block>
            </value>
            <value name="VALUE-1">
                <block type="Number">
                    <field name="NUM">0</field>
                </block>
            </value>
            <value name="VALUE-2">
                <block type="Number">
                    <field name="NUM">0</field>
                </block>
            </value>
        </block>
    </value>
    <value name="VALUE-2">
        <block type="Number">
            <field name="NUM">0</field>
        </block>
    </value>
</block>
```