# %{ID_ARRIVAL_BLOCK_ISFACTION}

%{help.isfaction.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_TEAMID}
2. %{PYRITE_TYPE_ENUM_FACTIONS}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN}

```
<block type="IsFaction">
    <value name="VALUE-0">
        <block type="GetTeamId">
            <value name="VALUE-0">
                <block type="Number">
                    <field name="NUM">1</field>
                </block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="FactionsItem">
            <field name="VALUE-0">Factions</field>
            <field name="VALUE-1">Grafton_GER</field>
        </block>
    </value>
</block>
```