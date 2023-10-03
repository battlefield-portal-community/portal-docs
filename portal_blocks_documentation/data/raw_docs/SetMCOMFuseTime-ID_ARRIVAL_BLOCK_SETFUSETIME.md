# %{ID_ARRIVAL_BLOCK_SETFUSETIME}

%{help.setmcomfusetime.summary}

### %{help.common.input}

1.  %{PYRITE_TYPE_MCOM}
2.  %{PYRITE_TYPE_NUMBER}

```
<block type="SetMCOMFuseTime">
    <value name="VALUE-0">
        <block type="GetCapturePoint">
            <value name="VALUE-0">
                <block type="MCOMsItem">
                    <field name="VALUE-0">MCOMs</field>
                    <field name="VALUE-1">D</field>
                </block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="Number">
            <field name="NUM">10</field>
        </block>
    </value>
</block>
```