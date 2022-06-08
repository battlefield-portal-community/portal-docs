# %{ID_ARRIVAL_BLOCK_FORVARIABLE}

%{help.forvariable.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_VARIABLE}
2. %{PYRITE_TYPE_NUMBER}

    %{help.common.contexts.start}

3. %{PYRITE_TYPE_NUMBER}

    %{help.common.contexts.end}

4. %{PYRITE_TYPE_NUMBER}

    %{help.common.contexts.interval}

```
<block type="ForVariable">
    <value name="VALUE-0"></value>
    <value name="VALUE-1">
        <block type="Number">
            <field name="NUM">0</field>
        </block>
    </value>
    <value name="VALUE-2">
        <block type="Number">
            <field name="NUM">9</field>
        </block>
    </value>
    <value name="VALUE-3">
        <block type="Number">
            <field name="NUM">1</field>
        </block>
    </value>
    <statement name="DO">
        <block type="SetPlayerDamage">
            <value name="VALUE-0">
                <block type="EventPlayer"></block>
            </value>
            <value name="VALUE-1">
                <block type="Number">
                    <field name="NUM">5</field>
                </block>
            </value>
            <value name="VALUE-2"></value>
        </block>
    </statement>
</block>
```
